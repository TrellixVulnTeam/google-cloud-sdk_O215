# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
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
"""Command for spanner instance configs create."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import textwrap

from googlecloudsdk.api_lib.spanner import instance_configs
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.spanner import flags
from googlecloudsdk.command_lib.util.args import labels_util


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
@base.Hidden
class Create(base.CreateCommand):
  """Create a Cloud Spanner instance config."""

  detailed_help = {
      'EXAMPLES':
          textwrap.dedent("""\
        To create a Cloud Spanner instance config, run:

          $ {command} custom-instance-config
            --display-name=custom-instance-config-name
            --base-config=projects/{projectID}/instanceConfigs/{google_managed_config_id}
            --replicas="location=us-east4,type=READ_WRITE;location=us-east4,type=READ_WRITE;location=us-east1,type=READ_WRITE;location=us-east1,type=READ_WRITE;location=us-central1,type=READ_ONLY"
        """),
  }

  @staticmethod
  def Args(parser):
    """Args is called by calliope to gather arguments for this command.

    Args:
      parser: An argparse parser that you can use to add arguments that go on
        the command line after this command. Positional arguments are allowed.
    """
    parser.add_argument(
        'config',
        metavar='INSTANCE_CONFIG',
        completer=flags.InstanceConfigCompleter,
        help='Cloud Spanner instance config. The `custom-` prefix is required '
        'to avoid name conflicts with Google managed configurations.')

    parser.add_argument(
        '--base-config',
        required=True,
        help='Base configuration name. '
        'e.g. projects/<projectID>/instanceConfigs/<google_managed_config_id>, '
        'based on which this configuration is created.')

    parser.add_argument(
        '--display-name',
        required=True,
        help='The name of this instance configuration as it appears in UIs.')

    parser.add_argument(
        '--etag', help='Used for optimistic concurrency control.')

    labels_util.AddCreateLabelsFlags(parser)

    parser.add_argument(
        '--validate-only',
        action='store_true',
        default=False,
        help='Validate the create action, but don\'t actually perform it.')

    parser.add_argument(
        '--replicas',
        required=True,
        metavar='location=LOCATION,type=TYPE',
        action='store',
        type=arg_parsers.ArgList(
            custom_delim_char=';',
            min_length=1,
            element_type=arg_parsers.ArgDict(
                spec={
                    'location': str,
                    # TODO(b/399093071): Change type to
                    # ReplicaInfo.TypeValueValuesEnum instead of str.
                    'type': str
                },
                required_keys=['location', 'type']),
        ),
        help="""\
        The geographic placement of nodes in this instance configuration and
        their replication properties.

        *location*::: The location of the serving resources, e.g. "us-central1".

        *type*::: The type of replica.

        The allowed values and formats are as follows.

        *READ_ONLY*::::

        Read-only replicas only support reads (not writes). Read-only
        replicas:

          * Maintain a full copy of your data.

          * Serve reads.

          * Do not participate in voting to commit writes.

          * Are not eligible to become a leader.

        *READ_WRITE*::::

        Read-write replicas support both reads and writes. These
        replicas:

          * Maintain a full copy of your data.

          * Serve reads.

          * Can vote whether to commit a write.

          * Participate in leadership election.

          * Are eligible to become a leader.

        *WITNESS*::::

        Witness replicas don't support reads but do participate in
        voting to commit writes. Witness replicas:

          * Do not maintain a full copy of data.

          * Do not serve reads.

          * Vote whether to commit writes.

          * Participate in leader election but are not eligible to become
            leader.

        """)

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Instance config create response.
    """
    return instance_configs.Create(args.config, args.display_name,
                                   args.base_config, args.replicas,
                                   args.validate_only, args.labels, args.etag)
