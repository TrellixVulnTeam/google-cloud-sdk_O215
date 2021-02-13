# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
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
"""Command for initializing eventing in a Cloud Run cluster."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.services import services_util
from googlecloudsdk.api_lib.services import serviceusage
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.events import eventflow_operations
from googlecloudsdk.command_lib.events import exceptions
from googlecloudsdk.command_lib.events import flags
from googlecloudsdk.command_lib.kuberun.core.events import init_shared
from googlecloudsdk.command_lib.kuberun.core.events import operator
from googlecloudsdk.command_lib.run import connection_context
from googlecloudsdk.command_lib.run import flags as serverless_flags
from googlecloudsdk.command_lib.run import platforms
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core.console import console_io


class Init(base.Command):
  """Initialize a cluster for eventing."""

  detailed_help = {
      'DESCRIPTION': """
          {description}
          Enables necessary services for the project, adds necessary IAM policy
          bindings to the provided service account, and creates a new key for
          the provided service account.
          This command is only available with Cloud Run for Anthos.
          """,
      'EXAMPLES': """
          To initialize a cluster:

              $ {command}
          """,
  }

  @staticmethod
  def CommonArgs(parser):
    """Defines arguments common to all release tracks."""
    flags.AddControlPlaneServiceAccountFlag(parser)
    flags.AddBrokerServiceAccountFlag(parser)
    flags.AddSourcesServiceAccountFlag(parser)

  @staticmethod
  def Args(parser):
    Init.CommonArgs(parser)

  def Run(self, args):
    """Executes when the user runs the init command."""
    if platforms.GetPlatform() == platforms.PLATFORM_MANAGED:
      raise exceptions.UnsupportedArgumentError(
          'This command is only available with Cloud Run for Anthos.')
    project = properties.VALUES.core.project.Get(required=True)
    conn_context = connection_context.GetConnectionContext(
        args, serverless_flags.Product.EVENTS, self.ReleaseTrack())

    with eventflow_operations.Connect(conn_context) as client:
      operator.install_eventing_via_operator(client, self.ReleaseTrack())

      # Eventing has been installed and enabled, but not initialized yet.
      cluster_eventing_type = init_shared.determine_cluster_eventing_type(
          client)

      if client.IsClusterInitialized(cluster_eventing_type):
        console_io.PromptContinue(
            message='This cluster has already been initialized.',
            prompt_string='Would you like to re-run initialization?',
            cancel_on_no=True)

      _EnableMissingServices(project)

      # Dict[ServiceAccountConfig, GsaEmail].
      gsa_emails = {}

      # Creates services accounts, if missing.
      for sa_config in init_shared.SERVICE_ACCOUNT_CONFIGS:
        gsa_emails[sa_config] = init_shared.construct_service_account_email(
            sa_config, args, cluster_eventing_type)

      # Creates secrets for each google service account and adds to cluster.
      init_shared.initialize_eventing_secrets(client, gsa_emails,
                                              cluster_eventing_type)

    log.status.Print(_InitializedMessage(
        self.ReleaseTrack(), conn_context.cluster_name))


def _EnableMissingServices(project):
  """Enables any required services for the project."""
  enabled_services = set(
      service.config.name for service in
      serviceusage.ListServices(project, True, 100, None))
  missing_services = list(
      sorted(
          set(init_shared.CONTROL_PLANE_REQUIRED_SERVICES) - enabled_services))
  if not missing_services:
    return

  formatted_services = '\n'.join(
      ['- {}'.format(s) for s in missing_services])
  init_shared.prompt_if_can_prompt(
      '\nThis will enable the following services:\n'
      '{}'.format(formatted_services))
  if len(missing_services) == 1:
    op = serviceusage.EnableApiCall(project, missing_services[0])
  else:
    op = serviceusage.BatchEnableApiCall(project, missing_services)
  if not op.done:
    op = services_util.WaitOperation(op.name, serviceusage.GetOperation)
  log.status.Print('Services successfully enabled.')


def _InitializedMessage(release_track, cluster_name):
  command_prefix = 'gcloud '
  if release_track != base.ReleaseTrack.GA:
    command_prefix += release_track.prefix + ' '
  ns_init_command = command_prefix + ('events namespaces init '
                                      '--copy-default-secret')
  brokers_create_command = command_prefix + 'events brokers create default'
  return ('Initialized cluster [{}] for Cloud Run eventing. '
          'Next, initialize the namespace(s) you plan to use and '
          'create a broker via `{}` and `{}`.'.format(
              cluster_name,
              ns_init_command,
              brokers_create_command,
          ))
