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
"""Command for running a local development environment."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import contextlib
import subprocess

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.code import cross_platform_temp_file
from googlecloudsdk.command_lib.code import flags
from googlecloudsdk.command_lib.code import kubernetes
from googlecloudsdk.command_lib.code import local
from googlecloudsdk.command_lib.code import local_files
from googlecloudsdk.command_lib.code import run_subprocess
from googlecloudsdk.command_lib.code import skaffold
from googlecloudsdk.command_lib.code import yaml_helper
from googlecloudsdk.core import config
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import properties
from googlecloudsdk.core import yaml
from googlecloudsdk.core.updater import update_manager
from googlecloudsdk.core.util import files as file_utils
import portpicker
import six


class RuntimeMissingDependencyError(exceptions.Error):
  """A runtime dependency is missing."""


@contextlib.contextmanager
def _SetImagePush(skaffold_file, shared_docker):
  """Set build.local.push value in skaffold file.

  Args:
    skaffold_file: Skaffold file handle.
    shared_docker: Boolean that is true if docker instance is shared between the
      kubernetes cluster and local docker builder.

  Yields:
    Path of skaffold file with build.local.push value set to the proper value.
  """
  # TODO(b/149935260): This function can be removed when
  # https://github.com/GoogleContainerTools/skaffold/issues/3668 is resolved.
  if not shared_docker:
    # If docker is not shared, use the default value (false). There is no need
    # to rewrite the skaffold file.
    yield skaffold_file
  else:
    skaffold_yaml = yaml.load_path(skaffold_file.name)
    local_block = yaml_helper.GetOrCreate(skaffold_yaml, ('build', 'local'))
    local_block['push'] = False
    with cross_platform_temp_file.NamedTempFile(
        yaml.dump(skaffold_yaml)) as patched_skaffold_file:
      yield patched_skaffold_file


def _IsDebug():
  """Return true if the verbosity is equal to debug."""
  return properties.VALUES.core.verbosity.Get() == 'debug'


@base.ReleaseTracks(base.ReleaseTrack.BETA, base.ReleaseTrack.ALPHA)
class Dev(base.Command):
  r"""Run a Cloud Run service in a local development environment."""
  detailed_help = {
      'DESCRIPTION':
          """\
          Run a Cloud Run service in a local development environment.

          This command takes Cloud Run source, builds it, and runs it on the
          local machine. This command also watches the relevant source files and
          updates the container when they change.
          """,
      'EXAMPLES':
          """\
          If building images using a Dockerfile:

            $ {command} --dockerfile=<path_to_dockerfile>

          If the Dockerfile is named `Dockerfile` and is located in the current
          directory, the `--dockerfile` flag may be omitted:

            $ {command}

          To access Google Cloud Platform services with the current user's
          credentials, login to obtain the application default credentials and
          invoke this command with the `--application-default-credential` flag.

            $ gcloud auth application-default login
            $ {command} --dockerfile=<path_to_dockerfile> \
            --application-default-credential
          """
  }

  @classmethod
  def Args(cls, parser):
    common = flags.CommonFlags()
    common.AddBetaFlags()

    if cls.ReleaseTrack() == base.ReleaseTrack.ALPHA:
      common.AddAlphaFlags()

    common.ConfigureParser(parser)

    group = parser.add_mutually_exclusive_group(required=False)

    group.add_argument('--kube-context', help='Kubernetes context.')

    group.add_argument('--minikube-profile', help='Minikube profile.')

    parser.add_argument(
        '--stop-cluster',
        default=True,
        action='store_true',
        help='If running on minikube, stop the minkube profile at the end of '
        'the session.')

    if cls.ReleaseTrack() == base.ReleaseTrack.ALPHA:
      parser.add_argument(
          '--minikube-vm-driver',
          default='docker',
          help='If running on minikube, use this vm driver.')

      parser.add_argument(
          '--namespace',
          help='Kubernetes namespace for development kubernetes objects.')

    # For testing only
    parser.add_argument(
        '--skaffold-events-port',
        type=int,
        hidden=True,
        help='Local port on which the skaffold events api is exposed. If not '
        'set, a random port is selected.')

  def Run(self, args):
    _EnsureComponentsInstalled(args)
    if _IsDebug():
      _PrintDependencyVersions(args)

    settings = local.Settings.FromArgs(args)
    local_file_generator = local_files.LocalRuntimeFiles(settings)

    kubernetes_config = six.ensure_text(local_file_generator.KubernetesConfig())

    _EnsureDockerRunning()
    with cross_platform_temp_file.NamedTempFile(
        kubernetes_config) as kubernetes_file:
      skaffold_config = six.ensure_text(
          local_file_generator.SkaffoldConfig(kubernetes_file.name))
      skaffold_event_port = (
          args.skaffold_events_port or portpicker.pick_unused_port())
      with cross_platform_temp_file.NamedTempFile(skaffold_config) as skaffold_file, \
           self._GetKubernetesEngine(args) as kube_context, \
           self._WithKubeNamespace(getattr(args, 'namespace', None), kube_context.context_name), \
           _SetImagePush(skaffold_file, kube_context.shared_docker) as patched_skaffold_file, \
           skaffold.Skaffold(patched_skaffold_file.name, kube_context.context_name,
                             getattr(args, 'namespace', None), kube_context.env_vars,
                             _IsDebug(), skaffold_event_port) as running_process, \
           skaffold.PrintUrlThreadContext(settings.service_name, skaffold_event_port):
        running_process.wait()

  @staticmethod
  def _GetKubernetesEngine(args):
    """Get the appropriate kubernetes implementation from the args.

    Args:
      args: The namespace containing the args.

    Returns:
      The context manager for the appropriate kubernetes implementation.
    """

    def External():
      return kubernetes.ExternalClusterContext(args.kube_context)

    def Minikube():
      if args.IsSpecified('minikube_profile'):
        cluster_name = args.minikube_profile
      else:
        cluster_name = kubernetes.DEFAULT_CLUSTER_NAME

      return kubernetes.Minikube(cluster_name, args.stop_cluster,
                                 getattr(args, 'minikube_vm_driver', 'docker'),
                                 _IsDebug())

    if args.IsSpecified('kube_context'):
      return External()
    else:
      return Minikube()

  @staticmethod
  @contextlib.contextmanager
  def _WithKubeNamespace(namespace_name, context_name):
    """Create and destory a kubernetes namespace if one is specified.

    Args:
      namespace_name: Namespace name.
      context_name: Kubernetes context name.

    Yields:
      None
    """
    if namespace_name:
      with kubernetes.KubeNamespace(namespace_name, context_name):
        yield
    else:
      yield


def _EnsureDockerRunning():
  """Make sure docker is running."""
  docker = file_utils.FindExecutableOnPath('docker')
  if not docker:
    raise RuntimeMissingDependencyError(
        'Cannot locate docker on $PATH. Install docker from '
        'https://docs.docker.com/get-docker/.')
  try:
    # docker info returns 0 if it can connect to the docker daemon and
    # returns a non-zero error code if it cannot. run_subprocess
    # checks raises an error if the process does not return 0.
    run_subprocess.Run([docker, 'info'], timeout_sec=20, show_output=_IsDebug())
  except subprocess.CalledProcessError:
    raise RuntimeMissingDependencyError(
        'Unable to reach docker daemon. Make sure docker is running '
        'and reachable.')


def _EnsureComponentsInstalled(args):
  """Make sure the components needed later are installed."""
  if not config.Paths().sdk_root:
    # Not currently in a packaged build. Currently in a unit test or a
    # gcloud_lite build.
    return

  components = ['skaffold']

  if args.IsSpecified('kube_context'):
    pass
  else:
    components.append('minikube')

  update_manager.UpdateManager.EnsureInstalledAndRestart(components)


def _PrintDependencyVersions(args):
  """Print the version strings of the dependencies."""
  dependency_versions = {'skaffold': skaffold.GetVersion()}

  if args.IsSpecified('kube_context'):
    pass
  else:
    dependency_versions['minikube'] = kubernetes.GetMinikubeVersion()

  for name, version in sorted(dependency_versions.items()):
    print('%s: %s\n' % (name, version))
