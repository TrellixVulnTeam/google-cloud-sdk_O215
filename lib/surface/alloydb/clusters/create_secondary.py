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
"""Creates a new AlloyDB secondary cluster."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.alloydb import api_util
from googlecloudsdk.api_lib.alloydb import cluster_operations
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.alloydb import flags
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class CreateSecondary(base.CreateCommand):
  """Creates a new AlloyDB Secondary cluster within a given project."""

  @staticmethod
  def Args(parser):
    """Specifies additional command flags.

    Args:
      parser: argparse.Parser: Parser object for command line inputs.
    """
    base.ASYNC_FLAG.AddToParser(parser)
    flags.AddRegion(parser)
    flags.AddCluster(parser)
    flags.AddPrimaryCluster(parser)

  def Run(self, args):
    """Constructs and sends request.

    Args:
      args: argparse.Namespace, An object that contains the values for the
        arguments specified in the .Args() method.

    Returns:
      ProcessHttpResponse of the request made
    """
    client = api_util.AlloyDBClient(self.ReleaseTrack())
    alloydb_client = client.alloydb_client
    alloydb_messages = client.alloydb_messages
    location_ref = client.resource_parser.Create(
        'alloydb.projects.locations',
        projectsId=properties.VALUES.core.project.GetOrFail,
        locationsId=args.region)
    cluster_resource = alloydb_messages.Cluster()
    cluster_resource.secondaryConfig = alloydb_messages.SecondaryConfig(
        primaryClusterName=args.primary_cluster)
    req = alloydb_messages.AlloydbProjectsLocationsClustersCreatesecondaryRequest(
        cluster=cluster_resource,
        clusterId=args.cluster,
        parent=location_ref.RelativeName())
    op = alloydb_client.projects_locations_clusters.Createsecondary(req)
    op_ref = resources.REGISTRY.ParseRelativeName(
        op.name, collection='alloydb.projects.locations.operations')
    log.status.Print('Operation ID: {}'.format(op_ref.Name()))
    if not args.async_:
      cluster_operations.Await(op_ref, 'Creating cluster', self.ReleaseTrack())
    return op
