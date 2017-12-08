# Copyright 2014 Google Inc. All Rights Reserved.

"""'logging sinks describe' command."""

from googlecloudsdk.api_lib.logging import util
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import list_printer
from googlecloudsdk.third_party.apitools.base.py import exceptions as apitools_exceptions


class Describe(base.Command):
  """Displays information about a sink."""

  @staticmethod
  def Args(parser):
    """Register flags for this command."""
    parser.add_argument('sink_name', help='The name of the sink to describe.')

  def GetLogSink(self):
    """Returns a log sink specified by the arguments."""
    client = self.context['logging_client_v1beta3']
    return client.projects_logs_sinks.Get(
        self.context['sink_reference'].Request())

  def GetLogServiceSink(self):
    """Returns a log service sink specified by the arguments."""
    client = self.context['logging_client_v1beta3']
    return client.projects_logServices_sinks.Get(
        self.context['sink_reference'].Request())

  def GetProjectSink(self):
    """Returns a project sink specified by the arguments."""
    client = self.context['logging_client_v1beta3']
    return client.projects_sinks.Get(
        self.context['sink_reference'].Request())

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      The specified sink with its destination.
    """
    try:
      if args.log:
        return util.TypedLogSink(self.GetLogSink(), log_name=args.log)
      elif args.service:
        return util.TypedLogSink(self.GetLogServiceSink(),
                                 service_name=args.service)
      else:
        return util.TypedLogSink(self.GetProjectSink())
    except apitools_exceptions.HttpError as error:
      raise exceptions.HttpException(util.GetError(error))

  def Display(self, unused_args, result):
    """This method is called to print the result of the Run() method.

    Args:
      unused_args: The arguments that command was run with.
      result: The value returned from the Run() method.
    """
    list_printer.PrintResourceList('logging.typedSinks', [result])
    util.PrintPermissionInstructions(result.destination)


Describe.detailed_help = {
    'DESCRIPTION': """\
        Displays information about a sink.
        If you don't include one of the *--log* or *--log-service* flags,
        this command displays information about a project sink.
     """,
}
