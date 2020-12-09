# -*- coding: utf-8 -*- #
# Copyright 2014 Google LLC. All Rights Reserved.
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

"""'logging sinks update' command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.logging import util
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions as calliope_exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core.console import console_io


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Update(base.UpdateCommand):
  """Updates a sink.

  Changes the *[DESTINATION]* or *--log-filter* associated with a sink.
  The new destination must already exist and Cloud Logging must have
  permission to write to it.

  Log entries are exported to the new destination immediately.

  ## EXAMPLES

  To only update a sink filter, run:

    $ {command} my-sink --log-filter='severity>=ERROR'

  Detailed information about filters can be found at:
  [](https://cloud.google.com/logging/docs/view/advanced_filters)
  """

  @staticmethod
  def Args(parser):
    """Register flags for this command."""
    parser.add_argument(
        'sink_name', help='The name of the sink to update.')
    parser.add_argument(
        'destination', nargs='?',
        help=('A new destination for the sink. '
              'If omitted, the sink\'s existing destination is unchanged.'))
    parser.add_argument(
        '--log-filter',
        help=('A new filter expression for the sink. '
              'If omitted, the sink\'s existing filter (if any) is unchanged.'))
    util.AddParentArgs(parser, 'Update a sink')

  def GetSink(self, parent, sink_ref):
    """Returns a sink specified by the arguments."""
    return util.GetClient().projects_sinks.Get(
        util.GetMessages().LoggingProjectsSinksGetRequest(
            sinkName=util.CreateResourceName(
                parent, 'sinks', sink_ref.sinksId)))

  def PatchSink(self, parent, sink_data, update_mask):
    """Patches a sink specified by the arguments."""
    messages = util.GetMessages()
    return util.GetClient().projects_sinks.Patch(
        messages.LoggingProjectsSinksPatchRequest(
            sinkName=util.CreateResourceName(parent, 'sinks',
                                             sink_data['name']),
            logSink=messages.LogSink(**sink_data),
            uniqueWriterIdentity=True,
            updateMask=','.join(update_mask)))

  def _Run(self, args, is_alpha_or_beta=False):
    sink_ref = util.GetSinkReference(args.sink_name, args)
    sink = self.GetSink(util.GetParentFromArgs(args), sink_ref)

    sink_data = {'name': sink_ref.sinksId}
    update_mask = []
    if args.IsSpecified('destination'):
      sink_data['destination'] = args.destination
      update_mask.append('destination')
    if args.IsSpecified('log_filter'):
      sink_data['filter'] = args.log_filter
      update_mask.append('filter')

    parameter_names = ['[destination]', '--log-filter']
    if is_alpha_or_beta:
      parameter_names.extend(
          ['--use-partitioned-tables', '--clear-exclusions'])

      if args.IsSpecified('use_partitioned_tables'):
        bigquery_options = {}
        bigquery_options['usePartitionedTables'] = args.use_partitioned_tables
        sink_data['bigqueryOptions'] = bigquery_options
        update_mask.append('bigquery_options.use_partitioned_tables')

      if args.IsSpecified('description'):
        sink_data['description'] = args.description
        update_mask.append('description')

      if args.IsSpecified('disabled'):
        sink_data['disabled'] = args.disabled
        update_mask.append('disabled')

      if (args.IsSpecified('clear_exclusions') or
          args.IsSpecified('remove_exclusions') or
          args.IsSpecified('add_exclusion') or
          args.IsSpecified('update_exclusion')):
        sink_data['exclusions'] = []
        update_mask.append('exclusions')
        exclusions_to_remove = (args.remove_exclusions
                                if args.IsSpecified('remove_exclusions')
                                else [])
        exclusions_to_update = (args.update_exclusion
                                if args.IsSpecified('update_exclusion')
                                else [])
        for exclusion in sink.exclusions:
          if exclusion.name in exclusions_to_remove:
            exclusions_to_remove.remove(exclusion.name)
          else:
            for i in range(len(exclusions_to_update)):
              if exclusion.name == exclusions_to_update[i]['name']:
                for key, value in exclusions_to_update[i].items():
                  if key == 'description':
                    exclusion.description = value
                  if key == 'filter':
                    exclusion.filter = value
                  if key == 'disabled':
                    exclusion.disabled = value
                exclusions_to_update.pop(i)
                break
            sink_data['exclusions'].append(exclusion)

        if exclusions_to_remove:
          raise calliope_exceptions.InvalidArgumentException(
              '--remove-exclusions',
              'Exclusions {0} do not exist'.format(
                  ','.join(exclusions_to_remove)))

        if exclusions_to_update:
          raise calliope_exceptions.InvalidArgumentException(
              '--update-exclusion',
              'Exclusions {0} do not exist'.format(
                  ','.join([exclusion['name']
                            for exclusion in exclusions_to_update])))

        if args.IsSpecified('clear_exclusions'):
          sink_data['exclusions'] = []

        if args.IsSpecified('add_exclusion'):
          sink_data['exclusions'] += args.add_exclusion

    if not update_mask:
      raise calliope_exceptions.MinimumArgumentException(
          parameter_names, 'Please specify at least one property to update')

    # Check for legacy configuration, and let users decide if they still want
    # to update the sink with new settings.
    if sink.writerIdentity and 'cloud-logs@' in sink.writerIdentity:
      console_io.PromptContinue(
          'This update will create a new writerIdentity (service account) for '
          'the sink. In order for the sink to continue working, grant that '
          'service account correct permission on the destination. The service '
          'account will be displayed after a successful update operation.',
          cancel_on_no=True, default=False)

    result = self.PatchSink(
        util.GetParentFromArgs(args), sink_data, update_mask)

    log.UpdatedResource(sink_ref)
    if args.IsSpecified('destination'):
      self._epilog_result_destination = result.destination
      self._epilog_writer_identity = result.writerIdentity
    return result

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      The updated sink with its new destination.
    """
    return self._Run(args)

  def Epilog(self, unused_resources_were_displayed):
    if hasattr(self, '_epilog_result_destination'):
      util.PrintPermissionInstructions(self._epilog_result_destination,
                                       self._epilog_writer_identity)


# pylint: disable=missing-docstring
@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class UpdateAlphaBeta(Update):
  r"""Updates a sink.

  Use this command to change a sink's *[DESTINATION]*, *--log-filter*, or
  *--description*. Disable a sink by specifying *--disabled*, enable a disabled
  sink by specifying *--no-disabled*. Add, update, or remove, or clear
  exclusions from the sink using *--add-exclusion=*, *--update-exclusion=*,
  *--remove-exclusions=*, or *--clear-exclusions*.

  When changing the *[DESTINATION]* of a sink, the new destination must already
  exist and Cloud Logging must be granted permission to write to it using the
  service account identified by the sink's `writerIdentity` field.

  ## EXAMPLES

  To only update a sink filter, run:

    $ {command} my-sink --log-filter='severity>=ERROR'

  Detailed information about filters can be found at:
  [](https://cloud.google.com/logging/docs/view/advanced_filters)

  To disable a sink, run:

    $ {command} my-sink --disabled

  To enable a disabled sink, run:

    $ {command} my-sink --no-disabled

  To add an exclusion to a sink, run:

    $ {command} my-sink --add-exclusion=\
      'name=my-exclusion,description=My description,filter=logName:foo'

  To add a disabled exclusion to a sink, include the `disabled` key and set it
  to any value. For example:

    $ {command} my-sink --add-exclusion=\
      'name=my-exclusion,filter=logName:foo,disabled=True'

  To update the description on an exclusion for a sink, run:

    $ {command} my-sink --add-exclusion=\
      'name=my-exclusion,description=New description'

  Note: Do not include keys for any fields that you do not intend to update.

  To enable a disabled exclusion for the sink, include the `disabled` key and
  do not set it to any value. For example:

    $ {command} my-sink --update-exclusion=\
      'name=my-exclusion,disabled='

  To delete an exclusion from a sink, run:

    $ {command} my-sink --remove-exclusions=my-exclusion1

  To delete multiple exclusions from a sink, run:

    $ {command} my-sink --remove-exclusions=my-exclusion1,my-exclusion2

  To clear all exclusions from a sink, run:

    $ {command} my-sink --clear-exclusions

  """

  @staticmethod
  def Args(parser):
    Update.Args(parser)

    bigquery_group = parser.add_argument_group(
        help='Settings for sink exporting data to BigQuery.')
    bigquery_group.add_argument(
        '--use-partitioned-tables', action='store_true',
        help=('If specified, use BigQuery\'s partitioned tables. By default, '
              'Logging creates dated tables based on the log entries\' '
              'timestamps, e.g. \'syslog_20170523\'. Partitioned tables remove '
              'the suffix and special query syntax '
              '(https://cloud.google.com/bigquery/docs/'
              'querying-partitioned-tables) must be used.'))

    parser.add_argument(
        '--clear-exclusions', action='store_true',
        help=('Remove all logging exclusions from the sink.'))
    parser.add_argument(
        '--remove-exclusions',
        type=arg_parsers.ArgList(),
        metavar='EXCLUSION ID',
        help=('Specify the name of the Logging exclusion(s) to delete.'))
    parser.add_argument(
        '--add-exclusion', action='append',
        type=arg_parsers.ArgDict(
            spec={
                'name': str,
                'filter': str,
                'description': str,
                'disabled': bool
            },
            required_keys=['name', 'filter']
        ),
        help=('Add an exclusion filter for log entries that are not to be '
              'routed to the sink\' destination. This flag can be repeated.\n\n'
              'The ``name\'\' and ``filter\'\' attributes are required. The '
              'following keys are accepted:\n\n'
              '*name*::: Required. An identifier, such as '
              '``load-balancer-exclusion\'\'. '
              'Identifiers are limited to 100 characters and can include only '
              'letters, digits, underscores, hyphens, and periods.\n\n'
              '*description*::: Optional. A description of this exclusion.\n\n'
              '*filter*::: Required. Entries that match this advanced log '
              'filter will be excluded. Filter cannot be empty.\n\n'
              '*disabled*::: Optional. By default, an exclusion is not '
              'disabled. To disable an exclusion, include this key and specify '
              'any value.\n\n'))

    parser.add_argument(
        '--update-exclusion', action='append',
        type=arg_parsers.ArgDict(
            spec={
                'name': str,
                'filter': str,
                'description': str,
                'disabled': bool
            },
            required_keys=['name']
        ),
        help=('Update an exclusion filter for a log entry that is not to be '
              'exported. This flag can be repeated.\n\n'
              'The ``name\'\' attribute is required. The '
              'following keys are accepted:\n\n'
              '*name*::: Required. An identifier, such as '
              '``load-balancer-exclusion\'\'. '
              'Identifiers are limited to 100 characters and can include only '
              'letters, digits, underscores, hyphens, and periods.\n\n'
              '*description*::: Optional. A description of this exclusion.\n\n'
              '*filter*::: Optional. Entries that match this advanced log '
              'filter will be excluded. Filter cannot be empty.\n\n'
              '*disabled*::: Optional. To disable an exclusion, include this '
              'key and specify any value. To enable a disabled exclusion, '
              'include this key, but do not specify any value. Do not include '
              'this key unless you want to change its value.\n\n'))

    parser.add_argument(
        '--description',
        help='Description of the sink.')

    parser.add_argument(
        '--disabled', action='store_true',
        help=('Disable the sink. Disabled sinks do not route logs to the sink '
              'destination. Specify --no-disabled to enable a disabled sink. '
              'If this flag is not specified, the value will not be updated.'))

  def Run(self, args):
    return self._Run(args, is_alpha_or_beta=True)
