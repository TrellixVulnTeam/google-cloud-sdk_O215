# -*- coding: utf-8 -*- #
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Allows you to write surfaces in terms of logical Serverless operations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from collections import OrderedDict
import contextlib
import functools
import glob
import os
import ssl
import sys
from apitools.base.py import exceptions as api_exceptions
from googlecloudsdk.api_lib.serverless import build_template
from googlecloudsdk.api_lib.serverless import configuration
from googlecloudsdk.api_lib.serverless import gke
from googlecloudsdk.api_lib.serverless import metrics
from googlecloudsdk.api_lib.serverless import revision
from googlecloudsdk.api_lib.serverless import route
from googlecloudsdk.api_lib.serverless import service
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.api_lib.util import apis_internal
from googlecloudsdk.api_lib.util import waiter
from googlecloudsdk.command_lib.serverless import deployable as deployable_pkg
from googlecloudsdk.command_lib.serverless import exceptions as serverless_exceptions
from googlecloudsdk.command_lib.serverless import pretty_print
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources
from googlecloudsdk.core.console import progress_tracker
from googlecloudsdk.core.util import retry

DEFAULT_ENDPOINT_VERSION = 'v1'
_SERVERLESS_API_NAME = 'serverless'
_SERVERLESS_API_VERSION = 'v1alpha1'

# Wait 11 mins for each deployment. This is longer than the server timeout,
# making it more likely to get a useful error message from the server.
MAX_WAIT_MS = 660000

# Because gcloud cannot update multiple lines of output simultaneously, the
# order of conditions in this dictionary should match the order in which we
# expect Serverless resources to complete deployment.
_CONDITION_TO_STAGE = OrderedDict([
    ('ConfigurationsReady', progress_tracker.Stage(
        'Creating Revision...')),
    ('RoutesReady', progress_tracker.Stage('Routing traffic...')),
    ('Ready', progress_tracker.Stage('Readying...'))])


class UnknownAPIError(exceptions.Error):
  pass


@contextlib.contextmanager
def Connect(cluster_ref):
  """Provide a ServerlessOperations instance to use.

  Arguments:
    cluster_ref: Resource, the gke cluster to connect to if present. Otherwise,
      connect to Hosted Serverless.

  Yields:
    A ServerlessOperations instance.
  """
  if cluster_ref:
    if not hasattr(ssl, 'PROTOCOL_TLSv1_2'):
      raise serverless_exceptions.NoTLSError(
          'Your Python {}.{}.{} installation does not support TLS 1.2, which is'
          ' required to connect to the GKE Serverless add-on. Please upgrade to'
          ' Python 2.7.9 or greater.'.format(
              sys.version_info.major,
              sys.version_info.minor,
              sys.version_info.micro))
    with gke.ClusterConnectionInfo(cluster_ref) as (endpoint, ca_certs):

      k8s_apiserver = 'https://kubernetes.default/'
      with gke.MonkeypatchGetaddrinfo('kubernetes.default', endpoint):
        prev_endpoint = (
            properties.VALUES.api_endpoint_overrides.serverless.Get())
        properties.VALUES.api_endpoint_overrides.serverless.Set(k8s_apiserver)
        # Since we weirdly have to provide ca_certs directly, allow this
        # protected access internal method.
        try:
          yield ServerlessOperations(apis_internal._GetClientInstance(  # pylint: disable=protected-access
              _SERVERLESS_API_NAME, _SERVERLESS_API_VERSION, ca_certs=ca_certs))
        finally:
          properties.VALUES.api_endpoint_overrides.serverless.Set(prev_endpoint)

  else:
    yield ServerlessOperations(
        apis.GetClientInstance(_SERVERLESS_API_NAME, _SERVERLESS_API_VERSION))


class ConditionPoller(waiter.OperationPoller):
  """A poller for serverless deployment."""

  def __init__(self, resource_getter, tracker):
    self._resource_getter = resource_getter
    self._tracker = tracker
    self._completed_stages = []
    self._failed_stages = []

  def IsDone(self, conditions):
    """Overrides.

    Args:
      conditions: A condition.Conditions object.

    Returns:
      a bool indicates whether `conditions` is terminal.
    """
    if conditions is None:
      return False
    return conditions.IsTerminal()

  def Poll(self, unused_ref):
    """Overrides.

    Args:
      unused_ref: A string representing the operation reference. Currently it
        must be 'deploy'.

    Returns:
      A condition.Conditions object.
    """
    conditions = self.GetConditions()

    if conditions is None or not conditions.IsFresh():
      return None

    for condition in conditions:
      message = conditions[condition]['message']
      stage = _CONDITION_TO_STAGE[condition]
      status = conditions[condition]['status']
      if message:
        self._tracker.UpdateStage(stage, message)
      if status is None:
        continue
      elif status and condition not in self._completed_stages:
        self._completed_stages.append(condition)
        self._tracker.CompleteStage(stage, message)
      elif not status and condition not in self._failed_stages:
        self._failed_stages.append(condition)
        self._tracker.FailStage(
            stage, serverless_exceptions.DeploymentFailedError, message)

    return conditions

  def GetResult(self, conditions):
    """Overrides.

    Get terminal conditions as the polling result.

    Args:
      conditions: A condition.Conditions object.

    Returns:
      A condition.Conditions object.
    """
    return conditions

  def GetConditions(self):
    """Returns the resource conditions wrapped in condition.Conditions.

    Returns:
      A condition.Conditions object.
    """
    resource = self._resource_getter()
    if resource is None:
      return None
    return resource.conditions


class ServerlessOperations(object):
  """Client used by Serverless to communicate with the actual Serverless API.
  """

  def __init__(self, client):
    self._client = client
    self._registry = resources.REGISTRY.Clone()
    self._registry.RegisterApiByName(_SERVERLESS_API_NAME,
                                     _SERVERLESS_API_VERSION)
    self._temporary_build_template_registry = {}

  @property
  def _messages_module(self):
    return self._client.MESSAGES_MODULE

  def IsSourceBranch(self):
    # TODO(b/112662240): Remove once the build field is public
    return hasattr(self._client.MESSAGES_MODULE.ConfigurationSpec, 'build')

  # For internal-only source testing. Codepaths inaccessable except on
  # build from dev branch.
  # TODO(b/112662240): productionalize when source is landing
  def _TemporaryBuildTemplateRegistry(self, namespace_ref):
    """Return the list of build templates available, mocking the server."""
    if namespace_ref.RelativeName() in self._temporary_build_template_registry:
      return self._temporary_build_template_registry[
          namespace_ref.RelativeName()]

    detect = build_template.BuildTemplate.New(
        self._client, 'default')
    detect.name = 'detect'
    detect.annotations[build_template.IGNORE_GLOB_ANNOTATION] = (
        '["/*", "!package.json","!Pipfile.lock"]')

    nodejs_8_9_4 = build_template.BuildTemplate.New(
        self._client, 'default')
    nodejs_8_9_4.name = 'nodejs_8_9_4'
    nodejs_8_9_4.annotations[build_template.IGNORE_GLOB_ANNOTATION] = (
        '["node_modules/"]')
    nodejs_8_9_4.labels[build_template.LANGUAGE_LABEL] = 'nodejs'
    nodejs_8_9_4.labels[build_template.VERSION_LABEL] = '8.9.4'
    nodejs_8_9_4.annotations[build_template.DEV_IMAGE_ANNOTATION] = (
        'gcr.io/local-run-demo/nodejs_dev:latest')

    go_1_10_1 = build_template.BuildTemplate.New(
        self._client, 'default')
    go_1_10_1.name = 'go_1_10_1'
    go_1_10_1.labels[build_template.LANGUAGE_LABEL] = 'go'
    go_1_10_1.labels[build_template.VERSION_LABEL] = '1.10.1'
    lst = [detect, nodejs_8_9_4, go_1_10_1]
    self._temporary_build_template_registry[namespace_ref.RelativeName()] = lst
    return lst

  def Detect(self, namespace_ref, source_ref, function_entrypoint=None):
    """Detects important properties and returns a Deployable.

    Args:
      namespace_ref: str, the namespace to look for build templates in
      source_ref: source_ref.SourceRef, refers to some source code
      function_entrypoint: str, allows you to specify this is a function, and
                           the function to run.

    Returns:
      a new Deployable referring to the source
    """
    template = self._DetectBuildTemplate(namespace_ref, source_ref)

    if (source_ref.source_type == source_ref.SourceType.IMAGE
        and not template and not function_entrypoint):
      return deployable_pkg.ServerlessContainer(source_ref)

    if not self.IsSourceBranch():
      raise serverless_exceptions.UnknownDeployableError()
    # TODO(b/112662240): Put at top when source lands.
    from googlecloudsdk.command_lib.serverless import source_deployable  # pylint: disable=g-import-not-at-top
    if (function_entrypoint and
        template and
        source_ref.source_type == source_ref.SourceType.DIRECTORY):
      return source_deployable.ServerlessFunction(source_ref, template,
                                                  function_entrypoint)

    if (source_ref.source_type == source_ref.SourceType.DIRECTORY and
        template and
        not function_entrypoint):
      return source_deployable.ServerlessApp(source_ref, template)

    raise serverless_exceptions.UnknownDeployableError()

  def GetRevision(self, revision_ref):
    """Get the revision.

    Args:
      revision_ref: Resource, revision to get.

    Returns:
      A revision.Revision object.
    """
    messages = self._messages_module
    revision_name = revision_ref.RelativeName()
    request = messages.ServerlessNamespacesRevisionsGetRequest(
        name=revision_name)
    try:
      with metrics.record_duration(metrics.GET_REVISION):
        response = self._client.namespaces_revisions.Get(request)
      return revision.Revision(response, messages)
    except api_exceptions.HttpNotFoundError:
      return None

  def Upload(self, deployable):
    """Upload the code for the given deployable."""
    deployable.UploadFiles()

  def _GetRoute(self, service_ref):
    """Return the relevant Route from the server, or None if 404."""
    messages = self._messages_module
    # GET the Route
    route_name = self._registry.Parse(
        service_ref.servicesId,
        params={
            'namespacesId': service_ref.namespacesId,
        },
        collection='serverless.namespaces.routes').RelativeName()
    route_get_request = messages.ServerlessNamespacesRoutesGetRequest(
        name=route_name,
    )

    try:
      with metrics.record_duration(metrics.GET_ROUTE):
        route_get_response = self._client.namespaces_routes.Get(
            route_get_request)
      return route.Route(route_get_response, messages)
    except api_exceptions.HttpNotFoundError:
      return None

  def _GetBuildTemplateByName(self, namespace_ref, name):
    """Return the BuildTemplate with the given name, or None."""
    # Implementation to be replaced once the concept exists on the server.
    for templ in self._TemporaryBuildTemplateRegistry(namespace_ref):
      if templ.name == name:
        return templ
    return None

  def _GetBuildTemplateByLanguageVersion(self, namespace_ref,
                                         language, version):
    """Return the BuildTemplate with the given language & version, or None."""
    # Implementation to be replaced once the concept exists on the server.
    del namespace_ref
    for templ in self._temporary_build_template_registry:
      if (templ.language, templ.version) == (language, version):
        return templ
    return None

  def WaitForCondition(self, getter):
    """Wait for a configuration to be ready in latest revision."""
    with progress_tracker.StagedProgressTracker(
        'Deploying...',
        _CONDITION_TO_STAGE.values(),
        failure_message='Deployment failed') as tracker:
      for stage in _CONDITION_TO_STAGE.values():
        tracker.StartStage(stage)

      config_poller = ConditionPoller(getter, tracker)
      try:
        conditions = waiter.PollUntilDone(config_poller, None)
      except retry.RetryException as err:
        conditions = config_poller.GetConditions()
        # err.message already indicates timeout. Check ready_cond_type for more
        # information.
        msg = conditions.DescriptiveMessage() if conditions else None
        if msg:
          log.error('Still waiting: {}'.format(msg))
        raise err
      if not conditions.IsReady():
        raise serverless_exceptions.ConfigurationError(
            conditions.DescriptiveMessage())

  def GetServiceUrl(self, service_ref):
    """Return the main URL for the service."""
    serv = self.GetService(service_ref)
    if serv.domain:
      return serv.domain
    # Older versions of knative don't populate domain on Service, only Route.
    serv_route = self._GetRoute(service_ref)
    return serv_route.domain

  def GetActiveRevisions(self, service_ref):
    """Return the actively serving revisions.

    Args:
      service_ref: the service Resource reference.

    Returns:
      {str, int}, A dict mapping revisionID to its traffic percentage target.

    Raises:
      serverless_exceptions.NoActiveRevisionsError: if no serving revisions
        were found.
    """
    serv_route = self._GetRoute(service_ref)
    active_revisions = serv_route.active_revisions

    if len(active_revisions) < 1:
      raise serverless_exceptions.NoActiveRevisionsError()

    return serv_route.active_revisions

  def _DetectBuildTemplate(self, namespace_ref, source_ref):
    """Determine the appropriate build template from source.

    Args:
      namespace_ref: Resource, namespace to find build templates in.
      source_ref: SourceRef, The service's image repo or source directory.

    Returns:
      The detected build template name.
    """
    if source_ref.source_type == source_ref.SourceType.IMAGE:
      return None
    elif glob.glob(os.path.join(source_ref.source_path, '*.go')):
      return self._GetBuildTemplateByName(namespace_ref, 'go_1_10_1')
    else:
      return self._GetBuildTemplateByName(namespace_ref, 'nodejs_8_9_4')

  def ListServices(self, namespace_ref):
    messages = self._messages_module
    request = messages.ServerlessNamespacesServicesListRequest(
        parent=namespace_ref.RelativeName())
    with metrics.record_duration(metrics.LIST_SERVICES):
      response = self._client.namespaces_services.List(request)
    return [service.Service(item, messages) for item in response.items]

  def GetService(self, service_ref):
    """Return the relevant Service from the server, or None if 404."""
    messages = self._messages_module
    service_get_request = messages.ServerlessNamespacesServicesGetRequest(
        name=service_ref.RelativeName())

    try:
      with metrics.record_duration(metrics.GET_SERVICE):
        service_get_response = self._client.namespaces_services.Get(
            service_get_request)
      return service.Service(service_get_response, messages)
    except api_exceptions.HttpNotFoundError:
      return None

  def GetConfiguration(self, service_ref):
    """Return the relevant Configuration from the server, or None if 404."""
    messages = self._messages_module
    name = self._registry.Parse(
        service_ref.servicesId,
        params={
            'namespacesId': service_ref.namespacesId,
        },
        collection='serverless.namespaces.configurations').RelativeName()
    configuration_get_request = (
        messages.ServerlessNamespacesConfigurationsGetRequest(
            name=name))

    try:
      with metrics.record_duration(metrics.GET_CONFIGURATION):
        configuration_get_response = self._client.namespaces_configurations.Get(
            configuration_get_request)
      return configuration.Configuration(configuration_get_response, messages)
    except api_exceptions.HttpNotFoundError:
      return None

  def DeleteService(self, service_ref):
    """Delete the provided Service.

    Args:
      service_ref: Resource, a reference to the Service to delete

    Raises:
      ServiceNotFoundError: if provided service is not found.
    """
    messages = self._messages_module
    service_name = service_ref.RelativeName()
    service_delete_request = messages.ServerlessNamespacesServicesDeleteRequest(
        name=service_name,
    )

    try:
      with metrics.record_duration(metrics.DELETE_SERVICE):
        self._client.namespaces_services.Delete(service_delete_request)
    except api_exceptions.HttpNotFoundError:
      raise serverless_exceptions.ServiceNotFoundError(
          'Service [{}] could not be found.'.format(service_ref.servicesId))

  def DeleteRevision(self, revision_ref):
    """Delete the provided Revision.

    Args:
      revision_ref: Resource, a reference to the Revision to delete

    Raises:
      RevisionNotFoundError: if provided revision is not found.
    """
    messages = self._messages_module
    revision_name = revision_ref.RelativeName()
    request = messages.ServerlessNamespacesRevisionsDeleteRequest(
        name=revision_name)
    try:
      with metrics.record_duration(metrics.DELETE_REVISION):
        self._client.namespaces_revisions.Delete(request)
    except api_exceptions.HttpNotFoundError:
      raise serverless_exceptions.RevisionNotFoundError(
          'Revision [{}] could not be found.'.format(revision_ref.revisionsId))

  def _UpdateOrCreateService(self, service_ref,
                             config_changes):
    """Apply config_changes to the service. Create it if necessary."""
    messages = self._messages_module
    # GET the Service
    serv = self.GetService(service_ref)
    if serv:
      # PUT the changed Service
      for config_change in config_changes:
        config_change.AdjustConfiguration(serv.configuration, serv.metadata)
      serv_name = service_ref.RelativeName()
      serv_update_req = (
          messages.ServerlessNamespacesServicesReplaceServiceRequest(
              service=serv.Message(),
              name=serv_name))
      with metrics.record_duration(metrics.UPDATE_SERVICE):
        updated = self._client.namespaces_services.ReplaceService(
            serv_update_req)
      return service.Service(updated, messages)

    else:
      # POST a new Service
      new_serv = service.Service.New(self._client, service_ref.namespacesId)
      new_serv.name = service_ref.servicesId
      pretty_print.Info('Creating new service [{bold}{service}{reset}]',
                        service=new_serv.name)
      parent = service_ref.Parent().RelativeName()
      for config_change in config_changes:
        config_change.AdjustConfiguration(new_serv.configuration,
                                          new_serv.metadata)
      serv_create_req = (
          messages.ServerlessNamespacesServicesCreateRequest(
              service=new_serv.Message(),
              parent=parent))
      with metrics.record_duration(metrics.CREATE_SERVICE):
        raw_service = self._client.namespaces_services.Create(
            serv_create_req)
      return service.Service(raw_service, messages)

  def ReleaseService(self, service_ref, config_changes, asyn=False):
    """Change the given service in prod using the given config_changes.

    Arguments:
      service_ref: Resource, the service to release
      config_changes: list, objects that implement AdjustConfiguration().
      asyn: bool, if True release asyncronously
    """

    self._UpdateOrCreateService(service_ref, config_changes)
    if not asyn:
      getter = functools.partial(self.GetService, service_ref)
      self.WaitForCondition(getter)

  def ListRevisions(self, namespace_ref, service_name):
    """List all revisions for the given service.

    Args:
      namespace_ref: Resource, namespace to list revisions in
      service_name: str, The service for which to list revisions.

    Returns:
      A list of revisions for the given service.
    """
    messages = self._messages_module
    request = messages.ServerlessNamespacesRevisionsListRequest(
        parent=namespace_ref.RelativeName(),
    )
    if service_name is not None:
      # For now, same as the service name, and keeping compatible with
      # 'service-less' operation.
      request.labelSelector = 'serving.knative.dev/service = {}'.format(
          service_name)
    with metrics.record_duration(metrics.LIST_REVISIONS):
      response = self._client.namespaces_revisions.List(request)
    return [revision.Revision(item, messages) for item in response.items]
