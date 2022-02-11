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
"""Job-specific printer."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from frozendict import frozendict
from googlecloudsdk.command_lib.run.integrations.formatters import custom_domain_formatter
from googlecloudsdk.command_lib.run.integrations.formatters import fallback_formatter
from googlecloudsdk.core.console import console_attr
from googlecloudsdk.core.resource import custom_printer_base as cp

INTEGRATION_PRINTER_FORMAT = 'integration'

_FALLBACK_FORMATTER = fallback_formatter.FallbackFormatter()
_INTEGRATION_FORMATTER_MAPS = frozendict({
    'custom-domain': custom_domain_formatter.CustomDomainFormatter(),
})


class IntegrationPrinter(cp.CustomPrinterBase):
  """Prints the run Integration in a custom human-readable format."""

  def Transform(self, record):
    """Transform an integration into the output structure of marker classes."""

    integration_type = record['type']
    formatter = self.GetFormatter(integration_type)
    config_block = formatter.TransformConfig(record)
    component_block = None
    if 'status' in record and record['status'] is not None:
      component_block = formatter.TransformComponentStatus(record)
    if not component_block:
      component_block = 'Status not available'
    return cp.Lines([
        self.Header(record),
        ' ',
        config_block,
        ' ',
        cp.Labeled([
            cp.Lines([
                'Integration Components',
                component_block
            ])
        ]),
    ])

  def Header(self, record):
    """Print the header of the integration.

    Args:
      record: dict, the integration.

    Returns:
      The printed output.
    """
    con = console_attr.GetConsoleAttr()
    return con.Emphasize('{} integration {} in region {}'.format(
        record.get('type'), record.get('name'), record.get('region')))

  def GetFormatter(self, integration_type):
    """Returns the formatter for the given integration type.

    Args:
      integration_type: string, the integration type.

    Returns:
      A formatter object.
    """
    return _INTEGRATION_FORMATTER_MAPS.get(integration_type,
                                           _FALLBACK_FORMATTER)
