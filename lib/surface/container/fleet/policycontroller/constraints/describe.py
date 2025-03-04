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
"""Describe constraint command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.container.fleet.policycontroller import status_api_utils
from googlecloudsdk.calliope import base as calliope_base
from googlecloudsdk.command_lib.container.fleet.policycontroller import utils
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
import six


@calliope_base.Hidden
@calliope_base.ReleaseTracks(calliope_base.ReleaseTrack.ALPHA)
class Describe(calliope_base.DescribeCommand):
  """Describe a Policy Controller constraint from the Policy Library.

  ## EXAMPLES

  To describe the "all-must-have-owner" constraint for the template
  "k8srequiredlabels":

      $ {command} k8srequiredlabels/all-must-have-owner
  """

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'CONSTRAINT_NAME',
        type=str,
        help='The constraint template name and constraint name joined by a slash, e.g. "k8srequiredlabels/all-must-have-owner".'
    )

  def Run(self, args):
    calliope_base.EnableUserProjectQuota()

    project_id = properties.VALUES.core.project.Get(required=True)

    client = status_api_utils.GetClientInstance(
        self.ReleaseTrack())
    messages = status_api_utils.GetMessagesModule(
        self.ReleaseTrack())

    request = messages.AnthospolicycontrollerstatusPaProjectsMembershipConstraintsListRequest(
        parent='projects/{}'.format(project_id))
    response = client.projects_membershipConstraints.List(request)

    if not response.membershipConstraints:
      log.status.Print('Constraint {} not found.'.format(args.CONSTRAINT_NAME))
      return {}

    formatted_constraints = {}
    for constraint in response.membershipConstraints:
      if args.CONSTRAINT_NAME == '{}/{}'.format(
          constraint.constraintRef.constraintTemplateName,
          constraint.constraintRef.name):
        formatted_constraints[constraint.membershipRef.name] = {
            'name':
                constraint.constraintRef.name,
            'template':
                constraint.constraintRef.constraintTemplateName,
            'enforcementAction':
                utils.get_enforcement_action_label(
                    six.text_type(constraint.spec.enforcementAction)),
            'violationCount':
                constraint.status.numViolations or 0,
            'violations': [],
            'match':
                constraint.spec.kubernetesMatch or {},
            'parameters':
                constraint.spec.parameters or {}
        }

    # Add violations to formatted constraints
    if formatted_constraints:
      request = messages.AnthospolicycontrollerstatusPaProjectsMembershipConstraintAuditViolationsListRequest(
          parent='projects/{}'.format(project_id))
      response = client.projects_membershipConstraintAuditViolations.List(
          request)
      for violation in response.membershipConstraintAuditViolations:
        if args.CONSTRAINT_NAME == '{}/{}'.format(
            violation.constraintRef.constraintTemplateName,
            violation.constraintRef.name
        ) and violation.membershipRef.name in formatted_constraints:
          formatted_constraint = {
              'resource_name':
                  violation.resourceRef.name,
              'resource_api_group':
                  violation.resourceRef.groupKind.apiGroup,
              'resource_kind':
                  violation.resourceRef.groupKind.kind
          }

          if violation.resourceRef.resourceNamespace is not None:
            formatted_constraint['resource_namespace'] = (
                violation.resourceRef.resourceNamespace)
          else:
            formatted_constraint['resource_namespace'] = 'N/A'

          formatted_constraints[violation.membershipRef.
                                name]['violations'].append(formatted_constraint)

    return formatted_constraints
