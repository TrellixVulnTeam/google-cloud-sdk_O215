# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
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
"""Cloud Speech-to-text recognizers create command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.ml.speech import client
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.ml.speech import flags_v2
from googlecloudsdk.core import log

public_allowed_locations = ('us', 'eu', 'global')
private_allowed_locations = frozenset(public_allowed_locations) | {
    # TODO(b/246590388): Remove when multiregion support is complete.
    'us-central1'
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Create(base.Command):
  """Create a speech-to-text recognizer."""

  @staticmethod
  def Args(parser):
    """Register flags for this command."""
    flags_v2.AddAllFlagsToParser(parser, create=True)

  def Run(self, args):
    recognizer = args.CONCEPTS.recognizer.Parse()
    if args.location not in private_allowed_locations:
      raise exceptions.InvalidArgumentException(
          '--location', '[--location] must be set to one of ' +
          ', '.join(public_allowed_locations) + '.')

    speech_client = client.SpeechV2Client()
    is_async = args.async_
    operation = speech_client.Create(
        recognizer, args.display_name, args.model, args.language_codes,
        args.profanity_filter, args.enable_word_time_offsets,
        args.enable_word_confidence, args.enable_automatic_punctuation,
        args.enable_spoken_punctuation, args.enable_spoken_emojis)

    if is_async:
      log.CreatedResource(
          operation.name, kind='speech recognizer', is_async=True)
      return operation

    resource = client.WaitForOperation(
        operation_ref=client.GetOperationRef(operation),
        message='waiting for recognizer [{}] to be created'.format(
            recognizer.RelativeName()))
    log.CreatedResource(resource, kind='speech recognizer')

    return resource
