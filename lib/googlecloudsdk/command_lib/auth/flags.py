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
"""Defines arguments for gcloud auth."""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import actions


def AddAccountArg(parser):
  parser.add_argument(
      'account',
      nargs='?',
      help=('Account to print the identity token for. If not specified, '
            'the current active account will be used.'))


def AddAudienceArg(parser):
  parser.add_argument(
      '--audiences',
      type=str,
      metavar='AUDIENCES',
      help='Intended recipient of the token. '
           'Currently, only one audience can be specified.')


def AddIncludeEmailArg(parser):
  parser.add_argument(
      '--include-email',
      action='store_true',
      help=('Specify whether or not service account email is included in the '
            "identity token. If specified, the token will contain 'email' and "
            "'email_verified' claims. This flag should only be used for "
            'impersonate service account.'))


def AddGCESpecificArgs(parser):
  """Add GCE specific arguments to parser."""
  gce_arg_group = parser.add_argument_group(
      help='Parameters for Google Compute Engine instance identity tokens.')
  gce_arg_group.add_argument(
      '--token-format',
      choices=['standard', 'full'],
      default='standard',
      help='Specify whether or not the project and instance details are '
      'included in the identity token payload. This flag only applies to '
      'Google Compute Engine instance identity tokens. '
      'See https://cloud.google.com/compute/docs/instances/verifying-instance-identity#token_format '
      'for more details on token format.')
  gce_arg_group.add_argument(
      '--include-license',
      action='store_true',
      help='Specify whether or not license codes for images associated with '
      'this instance are included in the identity token payload. Default '
      'is False. This flag does not have effect unless '
      '`--token-format=full`.')


def _AddDisableQuotaProject(parser):
  parser.add_argument(
      '--disable-quota-project',
      default=False,
      action='store_true',
      help="""\
      By default, the project in billing/quota_project or core/project will
      be written to application default credentials (ADC) as the quota project.
      When both are set, billing/quota_project takes precedence.
      You can use --billing-project to overwrite the value in
      billing/quota_project. Similarly, you can use --project to overwrite
      the value in core/project. Client libraries will send it to services
      and use it for quota and billing. To be able to use a project as the
      quota project, the account in ADC must have the serviceusage.services.use
      permission on the project. This permission is granted to the
      project editor and project owner. You can create custom roles to
      include this permission.

      Note that some cloud services may ignore this quota project and still
      bill the project owning the resources.

      In the following situations, you may use this flag to skip setting the
      quota project:

        * The account in ADC cannot be granted the project editor or owner
          role or any role with the serviceusage.services.use permission.
        * You always want to bill the project owning the resources.
      """
  )


def AddQuotaProjectFlags(parser):
  _AddDisableQuotaProject(parser)


def AddNoBrowserFlag(parser, auth_target):
  parser.add_argument(
      '--no-browser',
      default=False,
      action='store_true',
      help='Use this flag to authenticate {} on a machine without a '
      'web browser.'.format(auth_target))


def AddRemoteBootstrapFlag(parser):
  parser.add_argument(
      '--remote-bootstrap',
      # Never un-hide this flag because it should not be used directly by users.
      hidden=True,
      default=None,
      help='Use this flag to pass login parameters to a gcloud instance '
           'which will help this gcloud to login. '
           'This flag is reserved for bootstrapping remote workstation without '
           'access to web browsers, which should be initiated by using '
           'the --no-browser. Users should not use this flag directly.')


def AddRemoteLoginArgGroup(parser, for_adc=False):
  group = parser.add_mutually_exclusive_group()
  auth_target = 'client libraries' if for_adc else 'gcloud CLI'
  AddNoBrowserFlag(group, auth_target=auth_target)
  AddRemoteBootstrapFlag(group)


def AddNoLaunchBrowserFlag(parser):
  parser.add_argument(
      '--launch-browser',
      default=True,
      dest='launch_browser',
      help='Launch a browser for authorization. If not enabled or if it '
      'is not possible to launch a browser, prints a URL to standard output '
      'to be copied.',
      action=actions.DeprecationAction(
          '--launch-browser',
          warn='The --[no-]launch-browser flags are deprecated and will be '
          'removed in future updates. '
          'Use --no-browser to replace --no-launch-browser.\n',
          removed=False,
          action='store_true'))
