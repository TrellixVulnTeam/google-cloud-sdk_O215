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
"""The command to enable the Cloud Build Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base as gbase
from googlecloudsdk.command_lib.container.hub.features import base


@gbase.Hidden
class Enable(base.EnableCommand):
  """Enable the Cloud Build Hybrid Feature.

  Enables the Cloud Build Hybrid Feature in the Fleet.

  ## EXAMPLES

  To enable the Cloud Build Hybrid Feature, run:

    $ {command}
  """

  feature_name = 'cloudbuild'
