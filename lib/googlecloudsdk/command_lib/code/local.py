# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""Library for manipulating serverless local development setup."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import base64
import collections
import glob
import json
import os
import os.path
import re

from apitools.base.py import encoding_helper
from apitools.base.py import exceptions as apitools_exceptions
from googlecloudsdk.api_lib.run import container_resource
from googlecloudsdk.api_lib.run import service as k8s_service
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.api_lib.util import messages as messages_util
from googlecloudsdk.command_lib.auth import auth_util
from googlecloudsdk.command_lib.code import secrets
from googlecloudsdk.command_lib.code import yaml_helper
from googlecloudsdk.command_lib.iam import iam_util
from googlecloudsdk.command_lib.run import secrets_mapping
from googlecloudsdk.core import config
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import yaml
from googlecloudsdk.core.console import console_io
from googlecloudsdk.core.util import encoding
from googlecloudsdk.core.util import files
import six

IAM_MESSAGE_MODULE = apis.GetMessagesModule('iam', 'v1')
CRM_MESSAGE_MODULE = apis.GetMessagesModule('cloudresourcemanager', 'v1')
RUN_MESSAGES_MODULE = apis.GetMessagesModule('run', 'v1')

_C_IDENTIFIER = r'^[a-zA-Z_][a-zA-Z_0-9]*$'


class InvalidLocationError(exceptions.Error):
  """File is in an invalid location."""


class _DataType(type):
  """Dumb immutable data type."""

  # TODO(b/154131605): This a type that is an immutable data object. Can't use
  # attrs because it's not part of googlecloudsdk and can't use namedtuple
  # because it's not efficient on python 2 (it generates code, which needs
  # to be parsed and interpretted). Remove this code when we get support
  # for attrs or another dumb data object in gcloud.

  def __new__(mcs, classname, bases, class_dict):
    class_dict = class_dict.copy()
    names = class_dict.get('NAMES', tuple())
    class_dict.update(
        (name, mcs._CreateAccessor(i)) for i, name in enumerate(names))

    return super(_DataType, mcs).__new__(mcs, classname, bases, class_dict)

  @staticmethod
  def _CreateAccessor(i):
    """Create an tuple accessor property."""
    return property(lambda tpl: tpl[i])


class DataObject(six.with_metaclass(_DataType, tuple)):
  """Parent class of dumb data object."""

  def __new__(cls, **kwargs):
    names = getattr(cls, 'NAMES', tuple())
    invalid_names = set(kwargs) - set(names)
    if invalid_names:
      raise ValueError('Invalid names: ' + repr(invalid_names))

    tpl = tuple(kwargs[name] if name in kwargs else None for name in names)
    return super(DataObject, cls).__new__(cls, tpl)

  def replace(self, **changes):
    # https://docs.python.org/3/library/dataclasses.html#dataclasses.replace
    out = dict((n, changes.get(n, getattr(self, n, None))) for n in self.NAMES)
    return self.__class__(**out)


class ServiceAccountSetting(DataObject):
  """Setting object representing a service account."""
  NAMES = ('name',)


class ApplicationDefaultCredentialSetting(DataObject):
  """Setting object representing the application default credential."""

  _instance = None

  def __new__(cls, **kwargs):
    if not cls._instance:
      cls._instance = super(ApplicationDefaultCredentialSetting,
                            cls).__new__(cls, **kwargs)

    return cls._instance


class BuildpackBuilder(DataObject):
  """Settings for building with a buildpack.

    Attributes:
      builder: Name of the builder.
      trust: True if the lifecycle should trust this builder.
      devmode: Build with devmode.
  """

  NAMES = ('builder', 'trust', 'devmode')


class DockerfileBuilder(DataObject):
  """Data for a request to build with an existing Dockerfile."""

  # The 'dockerfile' attribute may be relative to the Settings.context dir or
  # it may be an absolute path. Note that Settings.context is determined later
  # than this instance is made, so it has to be passed into the methods below.
  NAMES = ('dockerfile',)

  def DockerfileAbsPath(self, context):
    return os.path.abspath(os.path.join(context, self.dockerfile))

  def DockerfileRelPath(self, context):
    return os.path.relpath(self.DockerfileAbsPath(context), context)

  def Validate(self, context):
    complete_path = self.DockerfileAbsPath(context)
    if os.path.commonprefix([context, complete_path]) != context:
      raise InvalidLocationError(
          'Invalid Dockerfile path. Dockerfile must be located in the build '
          'context directory.\n'
          'Dockerfile: {0}\n'
          'Build Context Directory: {1}'.format(complete_path, context))
    if not os.path.exists(complete_path):
      raise InvalidLocationError(complete_path + ' does not exist.')


def _GaeBuilderPackagePath(runtime):
  """GCR package path for a builder that works on the given appengine runtime.

  Args:
    runtime: Name of a runtime from app.yaml, e.g. 'python38'.

  Returns:
    gcr.io image path.
  """
  return 'gcr.io/gae-runtimes/buildpacks/%s/builder:latest' % runtime


def _IsGcpBaseBuilder(builder):
  """Return true if the builder is the GCP base builder.

  Args:
    builder: Name of the builder.

  Returns:
    True if the builder is the GCP base builder.
  """
  return builder == 'gcr.io/buildpack/builder:v1'


class _SecretPath(DataObject):
  """Configuration for a single secret version.

    Attributes:
      key: The secret version to mount.
      path: The file path to mount it on.
  """

  NAMES = ('key', 'path')


class _SecretVolume(DataObject):
  """Configuration for a single volume that mounts secret versions.

    Attributes:
      name: (str) The name of the volume to be referenced in the k8s resource.
      mount_path: (str) The filesystem location where the volume is mounted.
      secret_name: (str) The secret manager reference.
      items: (List[SecretPath]) The list of keys and paths for the secret.
  """
  NAMES = ('name', 'mount_path', 'secret_name', 'items')

  @classmethod
  def FromParsedYaml(cls, mount, volume_secret):
    """Make a _SecretVolume based on the volumeMount and secret from the yaml."""
    items = []
    for item in volume_secret.items:
      items.append(_SecretPath(key=item.key, path=item.path))
    return cls(
        name=mount.name,
        mount_path=mount.mountPath,
        secret_name=volume_secret.secretName,
        items=items)


class Settings(DataObject):
  """Settings for local development environments.

    Attributes:
      service_name: Name of the kuberntes service.
      image: Docker image tag.
      credential: Credential setting for either service account or application
        default credential.
      context: Path to directory to use as the current working directory for the
        docker build.
      builder: The builder specification or None.
      local_port: Local port to which to forward the service connection.
      env_vars: Container environment variables.
      env_vars_secrets: Container environment variables where the values come
        from Secret Manager.
      volumes_secrets: Volumes where the values come from secret manager.
      cloudsql_instances: Cloud SQL instances.
      memory: Memory limit.
      cpu: CPU limit.
      namespace: Kubernetes namespace to run in.
      readiness_probe: If true, create readiness probe.
      allow_secret_manager: If true, allow fetching secrets from secret manager
  """

  NAMES = ('service_name', 'image', 'credential', 'context', 'builder',
           'local_port', 'env_vars', 'env_vars_secrets', 'volumes_secrets',
           'cloudsql_instances', 'memory', 'cpu', 'namespace',
           'readiness_probe', 'allow_secret_manager')

  @classmethod
  def Defaults(cls):
    """The settings you get with no args or other overrides."""

    dir_name = os.path.basename(files.GetCWD())
    # Service names may not include _ and upper case characters.
    service_name = dir_name.replace('_', '-').lower()

    dockerfile_arg_default = 'Dockerfile'
    builder = DockerfileBuilder(dockerfile=dockerfile_arg_default)

    return cls(
        builder=builder,
        cloudsql_instances=[],
        context=os.path.abspath(files.GetCWD()),
        image=None,  # See Build() below.
        service_name=service_name,
        env_vars={},
        env_vars_secrets={},
        volumes_secrets=[],
        allow_secret_manager=None,
    )

  def WithServiceYaml(self, yaml_path):
    """Overrides settings with service.yaml and returns a new Settings object."""
    yaml_dict = yaml.load_path(yaml_path)
    message = messages_util.DictToMessageWithErrorCheck(
        yaml_dict, RUN_MESSAGES_MODULE.Service)
    knative_service = k8s_service.Service(message, RUN_MESSAGES_MODULE)

    replacements = {
        'service_name': knative_service.metadata.name,
    }

    try:
      [container] = knative_service.spec.template.spec.containers
    except ValueError:
      raise exceptions.Error('knative Service must have exactly one container.')

    # Aliased secrets from other projects are currently not supported
    # so check for the label and fail if that's the case
    # TODO(b/187972361): support secrets from other projects.
    for label in knative_service.annotations:
      if label == container_resource.SECRETS_ANNOTATION:
        raise exceptions.Error('Referencing secrets from other projects is '
                               'not currently supported by local dev.')
    new_env_vars = {}
    new_env_vars_secrets = {}
    for var in container.env:
      if var.valueFrom:
        if var.valueFrom.configMapKeyRef:
          raise exceptions.Error('env_vars from config_maps are not supported')
        elif var.valueFrom.secretKeyRef:
          new_env_vars_secrets[var.name] = {
              'key': var.valueFrom.secretKeyRef.key,
              'name': var.valueFrom.secretKeyRef.name
          }
      else:
        new_env_vars[var.name] = var.value
    replacements.update(
        _MergedEnvVars(self.env_vars, self.env_vars_secrets, new_env_vars,
                       new_env_vars_secrets))
    service_account_name = knative_service.spec.template.spec.serviceAccountName
    if service_account_name:
      replacements['credential'] = ServiceAccountSetting(
          name=service_account_name)

    image_name = container.image
    if image_name:
      replacements['image'] = image_name

    replacements.update(self._ResourceRequests(container))

    all_vols = {}
    for vol in knative_service.spec.template.spec.volumes:
      if vol.secret:
        all_vols[vol.name] = vol.secret
      else:
        raise exceptions.Error('Could not process volume "{}". Only volumes '
                               'from secrets are supported.'.format(vol.name))
    referenced_vols = []
    for vol in container.volumeMounts:
      if vol.name not in all_vols:
        raise exceptions.Error('Container referenced volume "{}" which was not '
                               'found.'.format(vol.name))
      referenced_vols.append(
          _SecretVolume.FromParsedYaml(vol, all_vols[vol.name]))
    replacements['volumes_secrets'] = referenced_vols

    return self.replace(**replacements)

  def _ResourceRequests(self, container):
    if not container.resources or not container.resources.limits:
      return {}
    ret = {}
    for prop in container.resources.limits.additionalProperties:
      if prop.key == 'cpu':
        ret['cpu'] = prop.value
      if prop.key == 'memory':
        ret['memory'] = prop.value
    return ret

  def WithArgs(self, args):
    """Overrides settings with args and returns a new Settings object."""

    replacements = {}
    for override_arg in [
        'local_port',
        'memory',
        'cpu',
        'namespace',
        'readiness_probe',
        'cloudsql_instances',
        'image',
        'service_name',
        'allow_secret_manager',
    ]:
      if args.IsKnownAndSpecified(override_arg):
        replacements[override_arg] = getattr(args, override_arg)

    if args.IsSpecified('application_default_credential'):
      replacements['credential'] = ApplicationDefaultCredentialSetting()
    elif args.IsSpecified('service_account'):
      replacements['credential'] = ServiceAccountSetting(
          name=args.service_account)

    if args.source:
      replacements['context'] = os.path.abspath(args.source)

    if getattr(args, 'no_skaffold_file', False):
      replacements['builder'] = None
    else:
      if args.IsKnownAndSpecified('builder'):
        replacements['builder'] = _BuilderFromArg(args.builder)
      elif args.IsKnownAndSpecified('dockerfile'):
        replacements['builder'] = DockerfileBuilder(dockerfile=args.dockerfile)
    if getattr(args, 'env_vars', None):
      new_envs = args.env_vars
    else:
      new_envs = getattr(args, 'env_vars_file', {}) or {}
    replacements.update(
        _MergedEnvVars(self.env_vars, self.env_vars_secrets, new_envs, {}))

    return self.replace(**replacements)

  def Build(self):
    """Validate and compute settings after all user inputs have been read."""
    if isinstance(self.builder, DockerfileBuilder):
      self.builder.Validate(self.context)
    replacements = {}
    if self.image is None:
      replacements['image'] = _DefaultImageName(self.service_name)
    return self.replace(**replacements)


def _ChooseExistingServiceYaml(context, arg):
  """Rules for choosing a service.yaml file depending on SERVICE_CONFIG arg.

  The rules are meant to discover common filename variants like
  'service.dev.yml' or 'staging-service.yaml'.

  Args:
    context: Build context dir. Could be '.'.
    arg: User's path (relative to context or absolute) to a yaml file with a
      knative Service description, or None.

  Returns:
    Absolute path to a yaml file, or None.
  """
  if arg is not None:
    complete_abs_path = os.path.abspath(os.path.join(context, arg))
    if os.path.exists(complete_abs_path):
      return complete_abs_path
    raise ValueError("file '{}' not found".format(complete_abs_path))
  for pattern in [
      '*service.dev.yaml',
      '*service.dev.yml',
      '*service.yaml',
      '*service.yml',
  ]:
    matches = glob.glob(os.path.join(context, pattern))
    if matches:
      return sorted(matches)[0]
  return None


def _MergedEnvVars(env_vars, env_vars_secrets, new_env_vars,
                   new_env_vars_secrets):
  """Add the new env vars (both values and secrets) to the existing ones."""

  env_vars = env_vars.copy()
  env_vars_secrets = env_vars_secrets.copy()

  # Env Vars can either be values or secrets, but not both.
  # If the variable is set as both, error.
  conflicts = set(new_env_vars).intersection(new_env_vars_secrets)
  if conflicts:
    raise exceptions.Error('{} cannot be secret and literal'.format(conflicts))

  # If the user is overriding an existing env var that was a secret with a
  # literal or vice versa, make sure to remove the old value from the other
  # dict.
  for new_env, val in new_env_vars.items():
    if new_env in env_vars_secrets:
      del env_vars_secrets[new_env]
    env_vars[new_env] = val
  for new_secret, val in new_env_vars_secrets.items():
    if new_secret in env_vars:
      del env_vars[new_secret]
    env_vars_secrets[new_secret] = val
  return {'env_vars': env_vars, 'env_vars_secrets': env_vars_secrets}


def AssembleSettings(args):
  """Layer the default values, service.yaml values, and cmdline overrides."""
  settings = Settings.Defaults()
  yaml_file = _ChooseExistingServiceYaml(
      getattr(args, 'source', None) or os.path.curdir,
      getattr(args, 'service_config', None))
  if yaml_file:
    settings = settings.WithServiceYaml(yaml_file)
  settings = settings.WithArgs(args)
  settings = settings.Build()
  return settings


def _DefaultImageName(service_name):
  """Computes a default image name."""
  project_name = properties.VALUES.core.project.Get()
  if project_name:
    image = 'gcr.io/{project}/{service}'.format(
        project=project_name, service=service_name)
  else:
    image = service_name

  # Image names cannot have upper case characters. If the image name is
  # autogenerated, then make sure the image name is lower case. If the
  # user enters an image name manually, it's OK to stop the user and tell
  # them about the illegal image name.
  image = image.lower()
  return image


def _BuilderFromArg(builder_arg):
  is_gcp_base_builder = _IsGcpBaseBuilder(builder_arg)
  return BuildpackBuilder(
      builder=builder_arg,
      trust=is_gcp_base_builder,
      devmode=is_gcp_base_builder)


_POD_TEMPLATE = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {service}
  labels:
    service: {service}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {service}
  template:
    metadata:
      labels:
        app: {service}
    spec:
      containers: []
      terminationGracePeriodSeconds: 0
"""

_CONTAINER_TEMPLATE = """
name: {service}-container
image: {image}
env:
- name: PORT
  value: "8080"
ports:
- containerPort: 8080
"""

# The readiness probe container sits in an infinite wait loop and waits until
# port 8080 (1F90 in hex) is in use. This prevents the reload cycle from being
# considered "complete" until the developer's application binds to $PORT.
_READINESS_PROBE_CONTAINER_TEMPLATE = """
name: {service}-readiness-probe
image: gcr.io/gcp-runtimes/ubuntu_18_0_4:latest
command: ["sleep"]
args: ["infinity"]
readinessProbe:
  exec:
    command:
    - "grep"
    - ":1F90"
    - "/proc/net/tcp"
    - "/proc/net/tcp6"
  periodSeconds: 1
"""


def _CreateDeployment(service_name,
                      image_name,
                      memory_limit=None,
                      cpu_limit=None,
                      cpu_request=None,
                      readiness_probe=False):
  """Create a deployment specification for a service.

  Args:
    service_name: Name of the service.
    image_name: Image tag.
    memory_limit: Container memory limit.
    cpu_limit: Container cpu limit.
    cpu_request: Container cpu request.
    readiness_probe: If true, add a readiness probe.

  Returns:
    Dictionary object representing the deployment yaml, and the main container.
  """
  deployment = yaml.load(_POD_TEMPLATE.format(service=service_name))
  container = yaml.load(
      _CONTAINER_TEMPLATE.format(service=service_name, image=image_name))
  if memory_limit is not None:
    limits = yaml_helper.GetOrCreate(container, ('resources', 'limits'))
    limits['memory'] = memory_limit
  if cpu_limit is not None:
    limits = yaml_helper.GetOrCreate(container, ('resources', 'limits'))
    limits['cpu'] = six.text_type(cpu_limit)
  if cpu_request is not None:
    requests = yaml_helper.GetOrCreate(container, ('resources', 'requests'))
    requests['cpu'] = six.text_type(cpu_request)
  containers = yaml_helper.GetOrCreate(
      deployment, ('spec', 'template', 'spec', 'containers'), constructor=list)
  containers.append(container)

  if readiness_probe:
    readiness_container = yaml.load(
        _READINESS_PROBE_CONTAINER_TEMPLATE.format(service=service_name))
    containers.append(readiness_container)

  return deployment, container


_SERVICE_TEMPLATE = """
apiVersion: v1
kind: Service
metadata:
  name: {service}
spec:
  type: LoadBalancer
  selector:
    app: {service}
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 8080
"""


def CreateService(service_name):
  """Create a service specification.

  Args:
    service_name: Name of the service.

  Returns:
    Dictionary objects representing the service yaml.
  """
  yaml_text = _SERVICE_TEMPLATE.format(service=service_name)
  return yaml.load(yaml_text)


def _AddEnvironmentVariables(container, env_vars):
  """Add environment variable settings to a container.

  Args:
    container: (dict) Container to edit.
    env_vars: (dict) Key value environment variable pairs.
  """
  env_list = yaml_helper.GetOrCreate(container, ('env',), constructor=list)
  invalid_keys = []
  for key, value in sorted(env_vars.items()):
    if not re.match(_C_IDENTIFIER, key):
      invalid_keys.append(six.ensure_str(key))
      continue
    env_list.append({'name': key, 'value': value})
  if invalid_keys:
    raise ValueError('Environment variable name must be a C_IDENTIFIER. '
                     'Invalid names: %r' % invalid_keys)


def _AddSecretEnvironmentVariables(container, env_vars_secrets):
  """Add environment variables from secrets to a container.

  Args:
    container: (dict) Container to edit.
    env_vars_secrets: (dict) Key value environment variable pairs. Values are
      dict with key/name keys in them.
  """
  env_list = yaml_helper.GetOrCreate(container, ('env',), constructor=list)
  for key, value in sorted(env_vars_secrets.items()):
    env_list.append({'name': key, 'valueFrom': {'secretKeyRef': value.copy()}})


def CreateDevelopmentServiceAccount(service_account_email):
  """Creates a service account for local development.

  Args:
    service_account_email: Email of the service account.

  Returns:
    The resource name of the service account.
  """
  project_id = _GetServiceAccountProject(service_account_email)
  service_account_name = 'projects/{project}/serviceAccounts/{account}'.format(
      project=project_id, account=service_account_email)

  exists = _ServiceAccountExists(service_account_name)
  if _IsReservedServiceAccountName(service_account_email):
    if not exists:
      raise ValueError('%s cannot be created because it is a service '
                       'account name' % service_account_email)
    else:
      return service_account_name

  if not exists:
    account_id = _GetServiceAccountId(service_account_email)
    _CreateAccount('Serverless Local Development Service Account', account_id,
                   project_id)

    permission_msg = ('The project editor role allows the service account '
                      'to create, delete, and modify most resources in the '
                      'project.')
    prompt_string = (
        'Add project editor role to {}?'.format(service_account_email))
    # Make the service account an editor on the project
    if console_io.PromptContinue(
        message=permission_msg, prompt_string=prompt_string):
      _AddBinding(project_id, 'serviceAccount:' + service_account_email,
                  'roles/editor')

  return service_account_name


# Regular expression for parsing a service account email address.
# Format is [id]@[project].iam.gserviceaccount.com
_PROJECT_SERVICE_ACCOUNT_RE = re.compile(
    r'(?P<id>[^@]+)@(?P<project>[^\.]+).iam.gserviceaccount.com')

# Regular expression for parsing a compute service account email address.
# Format is [project-id]-compute@developer.gserviceaccount.com
_APPENGINE_SERVICE_ACCOUNT = re.compile(
    r'(?P<project_id>[^\.]+).google.com@appspot.gserviceaccount.com')

# Regular expression for parsing a compute service account email address.
# Format is [project-number]-compute@developer.gserviceaccount.com
_COMPUTE_SERVICE_ACCOUNT = re.compile(
    r'(?P<project_number>\d+)-compute@developer.gserviceaccount.com')


def _GetServiceAccountProject(service_account_email):
  """Get the project id from a service account email.

  Args:
    service_account_email: (str) Email address of service account.

  Returns:
    The project id of the project to which the service account belongs.
  """
  matcher = _PROJECT_SERVICE_ACCOUNT_RE.match(service_account_email)
  if matcher:
    return matcher.group('project')

  matcher = _APPENGINE_SERVICE_ACCOUNT.match(service_account_email)
  if matcher:
    return matcher.group('project_id')

  matcher = _COMPUTE_SERVICE_ACCOUNT.match(service_account_email)
  if matcher:
    return _ProjectNumberToId(matcher.group('project_number'))

  raise ValueError(service_account_email +
                   ' is not a valid service account address')


_SERVICE_ACCOUNT_RE = re.compile(r'(?P<id>[^@]+)@.*\.gserviceaccount\.com')


def _GetServiceAccountId(service_account_email):
  matcher = _SERVICE_ACCOUNT_RE.match(service_account_email)
  if not matcher:
    raise ValueError(service_account_email +
                     ' is not a valid service account address')
  return matcher.group('id')


def _ProjectNumberToId(project_number):
  """Coverts project number to project id.

  Args:
    project_number: (str) The project number as a string.

  Returns:
    The project id.
  """
  resource_manager = apis.GetClientInstance('cloudresourcemanager', 'v1')
  req = CRM_MESSAGE_MODULE.CloudresourcemanagerProjectsGetRequest(
      projectId=project_number)
  project = resource_manager.projects.Get(req)
  return six.ensure_text(project.projectId)


def _IsReservedServiceAccountName(service_account_email):
  return (_APPENGINE_SERVICE_ACCOUNT.match(service_account_email) or
          _COMPUTE_SERVICE_ACCOUNT.match(service_account_email))


def _ServiceAccountExists(service_account_name):
  """Tests if service account email.

  Args:
    service_account_name: (str) Service account resource name.

  Returns:
    True if the service account exists.
  """
  service = apis.GetClientInstance('iam', 'v1')
  try:
    request = IAM_MESSAGE_MODULE.IamProjectsServiceAccountsGetRequest(
        name=service_account_name)
    service.projects_serviceAccounts.Get(request)
    return True
  except apitools_exceptions.HttpNotFoundError:
    return False


def _CreateAccount(display_name, account_id, project):
  """Create an account if it does not already exist.

  Args:
    display_name: (str) Display name.
    account_id: (str) User account id.
    project: (str) Project name.
  """
  service = apis.GetClientInstance('iam', 'v1')
  try:
    service_account_msg = IAM_MESSAGE_MODULE.ServiceAccount(
        displayName=display_name)
    request = IAM_MESSAGE_MODULE.CreateServiceAccountRequest(
        accountId=account_id, serviceAccount=service_account_msg)
    service.projects_serviceAccounts.Create(
        IAM_MESSAGE_MODULE.IamProjectsServiceAccountsCreateRequest(
            name='projects/' + project, createServiceAccountRequest=request))
  except apitools_exceptions.HttpConflictError:
    # If account already exists, we can ignore the error
    pass


def _AddBinding(project, account, role):
  """Adds a binding.

  Args:
    project: (str) Project name.
    account: (str) User account.
    role: (str) Role.
  """
  crm_client = apis.GetClientInstance('cloudresourcemanager', 'v1')
  policy = crm_client.projects.GetIamPolicy(
      CRM_MESSAGE_MODULE.CloudresourcemanagerProjectsGetIamPolicyRequest(
          resource=project))

  if not iam_util.BindingInPolicy(policy, account, role):
    iam_util.AddBindingToIamPolicy(CRM_MESSAGE_MODULE.Binding, policy, account,
                                   role)
    req = CRM_MESSAGE_MODULE.CloudresourcemanagerProjectsSetIamPolicyRequest(
        resource=project,
        setIamPolicyRequest=CRM_MESSAGE_MODULE.SetIamPolicyRequest(
            policy=policy))
    crm_client.projects.SetIamPolicy(req)


class KubeConfigGenerator(object):
  """The base code generator with default return values.

  Subclasses may override any of the member methods.
  """

  def CreateConfigs(self):
    """Create top level kubernetes configs.

    Returns:
      List of kubernetes configuration yamls encoded as dictionaries.
    """
    return []

  def ModifyDeployment(self, deployment):
    """Modify a deployment.

    Subclasses that override this method should use this method for adding
    or deleting resources (e.g. containers, volumes, metadata) to the
    deployment.

    Args:
      deployment: (dict) Deployment yaml in dictionary form.
    """

  def ModifyContainer(self, container):
    """Modify a container.

    Subclasses that override this method should use this method for adding,
    deleting, or modifying any of the yaml for a container.

    Args:
      container: (dict) Container yaml in dictionary form.
    """


class AppContainerGenerator(KubeConfigGenerator):
  """Generate deployment and service for a developer's app."""

  def __init__(self,
               service_name,
               image_name,
               env_vars=None,
               env_vars_secrets=None,
               memory_limit=None,
               cpu_limit=None,
               cpu_request=None,
               readiness_probe=False):
    self._service_name = service_name
    self._image_name = image_name
    self._env_vars = env_vars
    self._env_vars_secrets = env_vars_secrets
    self._memory_limit = memory_limit
    self._cpu_limit = cpu_limit
    self._cpu_request = cpu_request
    self._readiness_probe = readiness_probe

  def CreateConfigs(self):
    deployment, container = _CreateDeployment(
        self._service_name, self._image_name, self._memory_limit,
        self._cpu_limit, self._cpu_request, self._readiness_probe)
    default_env_vars = {
        'K_SERVICE': self._service_name,
        'K_CONFIGURATION': 'dev',
        'K_REVISION': 'dev-0001',
    }

    _AddEnvironmentVariables(container, default_env_vars)
    if self._env_vars:
      _AddEnvironmentVariables(container, self._env_vars)
    if self._env_vars_secrets:
      _AddSecretEnvironmentVariables(container, self._env_vars_secrets)
    service = CreateService(self._service_name)
    return [deployment, service]


class SecretInfo(object):
  """Information about a generated secret."""

  def __init__(self):
    self.secret_name = 'local-development-credential'
    self.path = ('/etc/' + self.secret_name.replace('-', '_') +
                 '/local_development_service_account.json')


def GetServiceAccountSecret(account_name):
  """Get a service account secret file as text.

  Args:
    account_name: (str) Name of the service account.

  Returns:
    Context of the service account secret as a string.
  """
  service_account = CreateDevelopmentServiceAccount(account_name)
  return CreateServiceAccountKey(service_account)


def GetUserCredential():
  """Get a copy of the application default credential for a user.

  Returns:
    Text version of the user's application default credential.
  """
  auth_util.AssertADCExists()
  return json.dumps(auth_util.GetADCAsJson())


class CredentialGenerator(KubeConfigGenerator):
  """Configures service account secret."""

  def __init__(self, credential_fetcher):
    self._credential_fetcher = credential_fetcher

  def GetInfo(self):
    return SecretInfo()

  def CreateConfigs(self):
    """Create a secret."""
    return [LocalDevelopmentSecretSpec(self._credential_fetcher())]

  def ModifyDeployment(self, deployment):
    """Add a secret volume to a deployment."""
    secret_info = self.GetInfo()
    volumes = yaml_helper.GetOrCreate(deployment,
                                      ('spec', 'template', 'spec', 'volumes'),
                                      list)
    _AddSecretVolume(volumes, secret_info.secret_name)

  def ModifyContainer(self, container):
    """Add volume mount and set application credential environment variable."""
    secret_info = self.GetInfo()
    mounts = yaml_helper.GetOrCreate(container, ('volumeMounts',), list)
    _AddSecretVolumeMount(mounts, secret_info.secret_name)
    envs = yaml_helper.GetOrCreate(container, ('env',), list)
    _AddSecretEnvVar(envs, secret_info.path)


_CLOUD_PROXY_CONTAINER_NAME = 'cloud-sql-proxy'


class CloudSqlProxyGenerator(KubeConfigGenerator):
  """Generate kubernetes configurations for a Cloud SQL proxy connection."""

  def __init__(self, instance_names, secret_info):
    self._instance_names = instance_names
    self._secret_info = secret_info

  def ModifyDeployment(self, deployment):
    """Add sidecar container and empty volume for unix socket."""
    volumes = yaml_helper.GetOrCreate(
        deployment, ('spec', 'template', 'spec', 'volumes'), constructor=list)
    volumes.append({'name': 'cloudsql', 'emptyDir': {}})

    containers = yaml_helper.GetOrCreate(
        deployment, ('spec', 'template', 'spec', 'containers'),
        constructor=list)
    containers.append(
        _CreateCloudSqlProxyContainer(self._instance_names,
                                      self._secret_info.path))

  def ModifyContainer(self, container):
    """Add volume mount to continer.

    This method will not modify the CloudSql proxy container.

    Args:
      container: (dict) Container yaml as a dict.
    """
    if container['name'] == _CLOUD_PROXY_CONTAINER_NAME:
      return
    volume_mounts = yaml_helper.GetOrCreate(
        container, ('volumeMounts',), constructor=list)
    volume_mounts.append({
        'name': 'cloudsql',
        'mountPath': '/cloudsql',
        'readOnly': True
    })


class SecretsNotAllowedError(exceptions.Error):
  """Error thrown when the deploy is not allowed to access secret manager."""
  pass


class SecretsGenerator(KubeConfigGenerator):
  """Generate kubernetes secrets for referenced secrets."""

  def __init__(self,
               service_name,
               env_secrets,
               secret_volumes,
               namespace,
               allow_secret_manager=None):
    self.project_name = properties.VALUES.core.project.Get()
    self.service_name = service_name
    self.secret_volumes = secret_volumes
    self.secret_map = collections.defaultdict(list)
    for _, secret in env_secrets.items():
      self.secret_map[secret['name']].append(secret['key'])

    for secret in secret_volumes:
      if not secret.items:
        # This is currently unsupported for secrets pulled from secret manager.
        self.secret_map[secret.secret_name].append(
            secrets_mapping.SpecialVersion.MOUNT_ALL)
      else:
        for item in secret.items:
          self.secret_map[secret.secret_name].append(item.key)
    self.namespace = namespace
    self.allow_secret_manager = allow_secret_manager

  def CreateConfigs(self):
    if not self.secret_map:
      return []
    # If secret manager was unspecified, prompt to continue
    if self.allow_secret_manager is None:
      secrets_msg = ('This config references secrets stored in secret manager.'
                     ' Continuing will fetch the secret values and download '
                     'the secrets to your local machine.')
      prompt_string = ('Fetch secrets from secret manager for {}?'.format(
          list(self.secret_map.keys())))
      # Make the service account an editor on the project
      if console_io.CanPrompt() and console_io.PromptContinue(
          message=secrets_msg, prompt_string=prompt_string):
        log.status.Print(
            'You can skip this message in the future by passing the '
            'flag --use-secret-manager=true')
        self.allow_secret_manager = True

    if not self.allow_secret_manager:
      raise SecretsNotAllowedError(
          'Config requires secrets but access to secret manager was not '
          'allowed. Replace secrets with environment variables or '
          'allow secret manager with --allow-secret-manager to proceed.')
    return secrets.BuildSecrets(self.project_name, self.secret_map,
                                self.namespace)

  def ModifyDeployment(self, deployment):
    # There's only one deployment for now, but let's make sure it's the right
    # one in case there's more later
    if deployment['metadata']['name'] != self.service_name:
      return
    # If there's no volumes, don't do anything
    if not self.secret_volumes:
      return
    volumes = yaml_helper.GetOrCreate(deployment,
                                      ('spec', 'template', 'spec', 'volumes'),
                                      list)
    for volume in self.secret_volumes:
      _AddSecretVolumeByName(volumes, volume.secret_name, volume.name,
                             volume.items)

  def ModifyContainer(self, container):
    if container['name'] != '{}-container'.format(self.service_name):
      return
    if not self.secret_volumes:
      return
    mounts = yaml_helper.GetOrCreate(container, ('volumeMounts',), list)
    for volume in self.secret_volumes:
      _AddVolumeMount(mounts, volume.name, volume.mount_path)


_CLOUD_SQL_PROXY_VERSION = '1.16'


def _CreateCloudSqlProxyContainer(instances, secret_path):
  return {
      'name': _CLOUD_PROXY_CONTAINER_NAME,
      'image': 'gcr.io/cloudsql-docker/gce-proxy:' + _CLOUD_SQL_PROXY_VERSION,
      'command': ['/cloud_sql_proxy'],
      'args': [
          '-dir=/cloudsql', '-instances=' + ','.join(instances),
          '-credential_file=' + secret_path
      ],
      'volumeMounts': [{
          'name': 'cloudsql',
          'mountPath': '/cloudsql',
      }]
  }


_SECRET_TEMPLATE = """
apiVersion: v1
kind: Secret
metadata:
  name: local-development-credential
type: Opaque
"""


def CreateServiceAccountKey(service_account_name):
  """Create a service account key.

  Args:
    service_account_name: Name of service acccount.

  Returns:
    The contents of the generated private key file as a string.
  """
  default_credential_path = os.path.join(
      config.Paths().global_config_dir,
      _Utf8ToBase64(service_account_name) + '.json')
  credential_file_path = encoding.GetEncodedValue(os.environ,
                                                  'LOCAL_CREDENTIAL_PATH',
                                                  default_credential_path)
  if os.path.exists(credential_file_path):
    return files.ReadFileContents(credential_file_path)

  warning_msg = ('Creating a user-managed service account key for '
                 '{service_account_name}. This service account key will be '
                 'the default credential pointed to by '
                 'GOOGLE_APPLICATION_CREDENTIALS in the local development '
                 'environment. The user is responsible for the storage,'
                 'rotation, and deletion of this key. A copy of this key will '
                 'be stored at {local_key_path}.\n'
                 'Only use service accounts from a test project. Do not use '
                 'service accounts from a production project.').format(
                     service_account_name=service_account_name,
                     local_key_path=credential_file_path)
  console_io.PromptContinue(
      message=warning_msg, prompt_string='Continue?', cancel_on_no=True)

  service = apis.GetClientInstance('iam', 'v1')
  message_module = service.MESSAGES_MODULE

  create_key_request = (
      message_module.IamProjectsServiceAccountsKeysCreateRequest(
          name=service_account_name,
          createServiceAccountKeyRequest=message_module
          .CreateServiceAccountKeyRequest(
              privateKeyType=message_module.CreateServiceAccountKeyRequest
              .PrivateKeyTypeValueValuesEnum.TYPE_GOOGLE_CREDENTIALS_FILE)))
  key = service.projects_serviceAccounts_keys.Create(create_key_request)

  files.WriteFileContents(credential_file_path, key.privateKeyData)

  return six.ensure_text(key.privateKeyData)


def LocalDevelopmentSecretSpec(key):
  """Create a kubernetes yaml spec for a secret.

  Args:
    key: (str) The private key as a JSON string.

  Returns:
    Dictionary representing yaml dictionary.
  """
  yaml_config = yaml.load(_SECRET_TEMPLATE)
  yaml_config['data'] = {
      'local_development_service_account.json': _Utf8ToBase64(key)
  }
  return yaml_config


def _AddSecretVolume(volumes, secret_name):
  _AddSecretVolumeByName(
      volumes, secret_name=secret_name, volume_name=secret_name)


def _AddSecretVolumeByName(volumes, secret_name, volume_name, items=None):
  """Add a secret volume to a list of volumes.

  Args:
    volumes: (list[dict]) List of volume specifications.
    secret_name: (str) Name of the secret.
    volume_name: (str) Name of the volume to add.
    items: (list[_SecretPath]) Optional list of SecretPaths to map on the
      filesystem.
  """
  if any(volume['name'] == volume_name for volume in volumes):
    return
  items_lst = [
      RUN_MESSAGES_MODULE.KeyToPath(key=secpath.key, path=secpath.path)
      for secpath in (items or [])
  ]
  volumes.append(
      encoding_helper.MessageToDict(
          RUN_MESSAGES_MODULE.Volume(
              name=volume_name,
              secret=RUN_MESSAGES_MODULE.SecretVolumeSource(
                  secretName=secret_name, items=items_lst))))


def _AddSecretVolumeMount(mounts, secret_name):
  """Add a secret volume mount.

  Args:
    mounts: (list[dict]) List of volume mount dictionaries.
    secret_name: (str) Name of the secret.
  """
  _AddVolumeMount(
      mounts,
      mount_name=secret_name,
      mount_path='/etc/' + secret_name.replace('-', '_'))


def _AddVolumeMount(mounts, mount_name, mount_path):
  if any(mount_name == mount['name'] for mount in mounts):
    return
  mount = RUN_MESSAGES_MODULE.VolumeMount(
      name=mount_name, mountPath=mount_path, readOnly=True)
  mounts.append(encoding_helper.MessageToDict(mount))


def _AddSecretEnvVar(envs, path):
  """Adds a environmental variable that points to the secret file.

  Add a environment varible where GOOGLE_APPLICATION_CREDENTIALS is the name
  and the path to the secret file is the value.

  Args:
    envs: (list[dict]) List of dictionaries with a name entry and value entry.
    path: (str) Path to secret.
  """
  if 'GOOGLE_APPLICATION_CREDENTIALS' not in (var['name'] for var in envs):
    envs.append({'name': 'GOOGLE_APPLICATION_CREDENTIALS', 'value': path})


def _Utf8ToBase64(s):
  """Encode a utf-8 string as a base 64 string."""
  return six.ensure_text(base64.b64encode(six.ensure_binary(s)))
