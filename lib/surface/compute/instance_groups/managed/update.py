# -*- coding: utf-8 -*- #
# Copyright 2017 Google LLC. All Rights Reserved.
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
"""Command for updating managed instance group."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute import managed_instance_groups_utils
from googlecloudsdk.api_lib.compute.instance_groups.managed import stateful_policy_utils as policy_utils
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute import flags
from googlecloudsdk.command_lib.compute import scope as compute_scope
from googlecloudsdk.command_lib.compute.instance_groups import flags as instance_groups_flags
from googlecloudsdk.command_lib.compute.instance_groups.managed import flags as managed_flags
from googlecloudsdk.command_lib.compute.managed_instance_groups import auto_healing_utils
import six

# Flags valid only for regional MIGs.
REGIONAL_FLAGS = ['instance_redistribution_type', 'target_distribution_shape']


@base.ReleaseTracks(base.ReleaseTrack.GA)
class UpdateGA(base.UpdateCommand):
  r"""Update a Compute Engine managed instance group."""

  @staticmethod
  def Args(parser):
    instance_groups_flags.MULTISCOPE_INSTANCE_GROUP_MANAGER_ARG.AddArgument(
        parser, operation_type='update')

    autohealing_group = parser.add_mutually_exclusive_group()
    autohealing_group.add_argument(
        '--clear-autohealing',
        action='store_true',
        default=None,
        help="""\
        Clears all autohealing policy fields for the managed instance group.
        """)
    autohealing_params_group = autohealing_group.add_group()
    auto_healing_utils.AddAutohealingArgs(autohealing_params_group)
    instance_groups_flags.AddMigUpdateStatefulFlags(parser)
    instance_groups_flags.AddDescriptionFlag(parser, for_update=True)
    managed_flags.AddMigInstanceRedistributionTypeFlag(parser)
    managed_flags.AddMigDistributionPolicyTargetShapeFlag(parser)
    # When adding RMIG-specific flag, update REGIONAL_FLAGS constant.

  def _GetUpdatedStatefulPolicyForDisks(self,
                                        client,
                                        current_stateful_policy,
                                        update_disks=None,
                                        remove_device_names=None):
    # Extract disk protos from current stateful policy proto
    if (current_stateful_policy and current_stateful_policy.preservedState
        and current_stateful_policy.preservedState.disks):
      current_disks = (current_stateful_policy
                       .preservedState.disks.additionalProperties)
    else:
      current_disks = []
    # Map of disks to have in the stateful policy, after updating and removing
    # the disks specified by the update and remove flags.
    final_disks_map = {
        disk_entry.key: disk_entry for disk_entry in current_disks
    }

    # Update the disks specified in --stateful-disk
    for update_disk in (update_disks or []):
      device_name = update_disk.get('device-name')
      updated_preserved_state_disk = (
          policy_utils.MakeStatefulPolicyPreservedStateDiskEntry(
              client.messages, update_disk))
      # Patch semantics on the `--stateful-disk` flag
      if device_name in final_disks_map:
        policy_utils.PatchStatefulPolicyDisk(final_disks_map[device_name],
                                             updated_preserved_state_disk)
      else:
        final_disks_map[device_name] = updated_preserved_state_disk

    # Remove the disks specified in --remove-stateful-disks
    for device_name in remove_device_names or []:
      del final_disks_map[device_name]

    stateful_disks = sorted(
        [stateful_disk for _, stateful_disk in six.iteritems(final_disks_map)],
        key=lambda x: x.key)
    return stateful_disks

  def _GetUpdatedStatefulPolicy(self, client, current_stateful_policy, args):
    """Create an updated stateful policy based on specified args."""
    update_disks = args.stateful_disk
    remove_device_names = args.remove_stateful_disks
    stateful_disks = self._GetUpdatedStatefulPolicyForDisks(
        client, current_stateful_policy, update_disks, remove_device_names)
    return policy_utils.MakeStatefulPolicy(client.messages, stateful_disks)

  def _StatefulArgsSet(self, args):
    return (args.IsSpecified('stateful_disk') or
            args.IsSpecified('remove_stateful_disks'))

  def _StatefulnessIntroduced(self, args):
    return args.IsSpecified('stateful_disk')

  def _ValidateStatefulPolicyParams(self, args, stateful_policy):
    instance_groups_flags.ValidateUpdateStatefulPolicyParams(args,
                                                             stateful_policy)

  def _PatchStatefulPolicy(self, igm_patch, args, igm_resource, client, holder):
    """Patch the stateful policy specified in args, to igm_patch."""
    # If we're potentially introducing statefulness to the MIG, we should
    # validate if this MIG is allowed to be stateful
    if self._StatefulnessIntroduced(args):
      managed_instance_groups_utils.ValidateIgmReadyForStatefulness(
          igm_resource, client)
    self._ValidateStatefulPolicyParams(args, igm_resource.statefulPolicy)

    igm_patch.statefulPolicy = self._GetUpdatedStatefulPolicy(
        client, igm_resource.statefulPolicy, args)
    return igm_patch

  def _GetValidatedAutohealingPolicies(self, holder, client, args,
                                       igm_resource):
    health_check = managed_instance_groups_utils.GetHealthCheckUri(
        holder.resources, args)
    auto_healing_policies = (
        managed_instance_groups_utils.ModifyAutohealingPolicies(
            igm_resource.autoHealingPolicies, client.messages, args,
            health_check))
    managed_instance_groups_utils.ValidateAutohealingPolicies(
        auto_healing_policies)
    return auto_healing_policies

  def _PatchRedistributionType(self, igm_patch, args, igm_resource, client):
    igm_patch.updatePolicy = (managed_instance_groups_utils
                              .ApplyInstanceRedistributionTypeToUpdatePolicy)(
                                  client,
                                  args.GetValue('instance_redistribution_type'),
                                  igm_resource.updatePolicy)

  def _PatchTargetDistributionShape(self, patch_instance_group_manager,
                                    target_distribution_shape, igm_resource,
                                    client):
    distribution_policy = igm_resource.distributionPolicy
    if distribution_policy is None:
      distribution_policy = client.messages.DistributionPolicy()
    distribution_policy.targetShape = (
        client.messages.DistributionPolicy.TargetShapeValueValuesEnum)(
            target_distribution_shape)
    patch_instance_group_manager.distributionPolicy = distribution_policy

  def _MakePatchRequest(self, client, igm_ref, igm_updated_resource):
    if igm_ref.Collection() == 'compute.instanceGroupManagers':
      service = client.apitools_client.instanceGroupManagers
      request = client.messages.ComputeInstanceGroupManagersPatchRequest(
          instanceGroupManager=igm_ref.Name(),
          instanceGroupManagerResource=igm_updated_resource,
          project=igm_ref.project,
          zone=igm_ref.zone)
    else:
      service = client.apitools_client.regionInstanceGroupManagers
      request = client.messages.ComputeRegionInstanceGroupManagersPatchRequest(
          instanceGroupManager=igm_ref.Name(),
          instanceGroupManagerResource=igm_updated_resource,
          project=igm_ref.project,
          region=igm_ref.region)
    return client.MakeRequests([(service, 'Patch', request)])

  def _CreateInstanceGroupManagerPatch(self, args, igm_ref, igm_resource,
                                       client, holder):
    """Create IGM resource patch."""
    managed_flags.ValidateRegionalMigFlagsUsage(args, REGIONAL_FLAGS, igm_ref)
    patch_instance_group_manager = client.messages.InstanceGroupManager()
    auto_healing_policies = self._GetValidatedAutohealingPolicies(
        holder, client, args, igm_resource)
    if auto_healing_policies is not None:
      patch_instance_group_manager.autoHealingPolicies = auto_healing_policies
    if args.IsSpecified('instance_redistribution_type'):
      self._PatchRedistributionType(patch_instance_group_manager, args,
                                    igm_resource, client)
    if self._StatefulArgsSet(args):
      patch_instance_group_manager = (
          self._PatchStatefulPolicy(patch_instance_group_manager, args,
                                    igm_resource, client, holder))
    if args.target_distribution_shape:
      self._PatchTargetDistributionShape(patch_instance_group_manager,
                                         args.target_distribution_shape,
                                         igm_resource, client)
    if args.IsSpecified('description'):
      patch_instance_group_manager.description = args.description
    return patch_instance_group_manager

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    client = holder.client
    igm_ref = (instance_groups_flags.MULTISCOPE_INSTANCE_GROUP_MANAGER_ARG
               .ResolveAsResource)(
                   args,
                   holder.resources,
                   default_scope=compute_scope.ScopeEnum.ZONE,
                   scope_lister=flags.GetDefaultScopeLister(client))

    if igm_ref.Collection() not in [
        'compute.instanceGroupManagers', 'compute.regionInstanceGroupManagers'
    ]:
      raise ValueError('Unknown reference type {0}'.format(
          igm_ref.Collection()))

    igm_resource = managed_instance_groups_utils.GetInstanceGroupManagerOrThrow(
        igm_ref, client)

    patch_instance_group_manager = self._CreateInstanceGroupManagerPatch(
        args, igm_ref, igm_resource, client, holder)
    return self._MakePatchRequest(client, igm_ref, patch_instance_group_manager)


UpdateGA.detailed_help = {
    'brief':
        'Update a Compute Engine managed instance group.',
    'DESCRIPTION':
        """\
      Update a Compute Engine managed instance group.

      *{command}* allows you to specify or modify the stateful policy and
      autohealing policy for an existing managed instance group.

      A stateful policy defines which resources should be preserved across the
      group. When instances in the group are recreated, stateful resources are
      preserved. This command allows you to update stateful resources,
      specifically to add or remove stateful disks.

      When updating the autohealing policy, you can specify the health check,
      initial delay, or both. If either field is unspecified, its value won't
      be modified. If `--health-check` is specified, the health check monitors
      the health of your application. Whenever the health check signal for an
      instance becomes `UNHEALTHY`, the autohealer recreates the instance.

      If no health check exists, instance autohealing is triggered only by
      instance status: if an instance is not `RUNNING`, the group recreates it.
      """
}


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class UpdateBeta(UpdateGA):
  """Update a Compute Engine managed instance group."""

  @classmethod
  def Args(cls, parser):
    UpdateGA.Args(parser)


UpdateBeta.detailed_help = UpdateGA.detailed_help


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class UpdateAlpha(UpdateBeta):
  """Update a Compute Engine managed instance group."""

  @classmethod
  def Args(cls, parser):
    UpdateBeta.Args(parser)
    instance_groups_flags.AddMigUpdateStatefulFlagsIPs(parser)

  def _StatefulArgsSet(self, args):
    return (super(UpdateAlpha, self)._StatefulArgsSet(args) or
            args.IsSpecified('stateful_internal_ip') or
            args.IsSpecified('remove_stateful_internal_ips') or
            args.IsSpecified('stateful_external_ip') or
            args.IsSpecified('remove_stateful_external_ips'))

  def _StatefulnessIntroduced(self, args):
    return (super(UpdateAlpha, self)._StatefulnessIntroduced(args) or
            args.IsSpecified('stateful_internal_ip') or
            args.IsSpecified('stateful_external_ip'))

  def _ValidateStatefulPolicyParams(self, args, stateful_policy):
    super(UpdateAlpha, self)._ValidateStatefulPolicyParams(args,
                                                           stateful_policy)
    instance_groups_flags.ValidateUpdateStatefulPolicyParamsWithIPs(
        args, stateful_policy)

  def _GetUpdatedStatefulPolicyForStatefulIPsCommon(
      self, client, current_ips, update_ip_to_ip_entry_lambda,
      update_ips=None, remove_interface_names=None):
    # Map of ips to have in the stateful policy, after updating and removing
    # the interfaces specified by the update and remove flags.
    final_ips_map = {
        ip_entry.key: ip_entry for ip_entry in current_ips
    }

    # Update the interfaces specified in IPs to be updated.
    for update_ip in (update_ips or []):
      interface_name = update_ip.get('interface-name')
      updated_preserved_state_ip = update_ip_to_ip_entry_lambda(update_ip)
      # Patch semantics on the stateful IP flag.
      if interface_name in final_ips_map:
        policy_utils.PatchStatefulPolicyIP(
            final_ips_map[interface_name], updated_preserved_state_ip)
      else:
        final_ips_map[interface_name] = updated_preserved_state_ip

    # Remove the interfaces specified for removal.
    for interface_name in remove_interface_names or []:
      del final_ips_map[interface_name]
    stateful_ips = sorted(
        [stateful_ip for key, stateful_ip in six.iteritems(final_ips_map)],
        key=lambda x: x.key)
    return stateful_ips

  def _GetUpdatedStatefulPolicyForInternalIPs(
      self, client, current_stateful_policy,
      update_internal_ips=None, remove_interface_names=None):
    # Extract internal IPs protos from current stateful policy proto.
    if (current_stateful_policy and current_stateful_policy.preservedState
        and current_stateful_policy.preservedState.internalIPs):
      current_ips = (current_stateful_policy
                     .preservedState.internalIPs.additionalProperties)
    else:
      current_ips = []
    return self._GetUpdatedStatefulPolicyForStatefulIPsCommon(
        client, current_ips,
        lambda ip: policy_utils.MakeInternalIPEntry(client.messages, ip),
        update_internal_ips, remove_interface_names)

  def _GetUpdatedStatefulPolicyForExternalIPs(
      self, client, current_stateful_policy,
      update_external_ips=None, remove_interface_names=None):
    # Extract internal IPs protos from current stateful policy proto.
    if (current_stateful_policy and current_stateful_policy.preservedState
        and current_stateful_policy.preservedState.externalIPs):
      current_ips = (current_stateful_policy
                     .preservedState.externalIPs.additionalProperties)
    else:
      current_ips = []
    return self._GetUpdatedStatefulPolicyForStatefulIPsCommon(
        client, current_ips,
        lambda ip: policy_utils.MakeExternalIPEntry(client.messages, ip),
        update_external_ips, remove_interface_names)

  def _GetUpdatedStatefulPolicy(self, client, current_stateful_policy, args):
    """Create an updated stateful policy based on specified args."""
    stateful_policy = super(UpdateAlpha, self)._GetUpdatedStatefulPolicy(
        client, current_stateful_policy, args)

    stateful_internal_ips = self._GetUpdatedStatefulPolicyForInternalIPs(
        client, current_stateful_policy, args.stateful_internal_ip,
        args.remove_stateful_internal_ips)

    stateful_external_ips = self._GetUpdatedStatefulPolicyForExternalIPs(
        client, current_stateful_policy, args.stateful_external_ip,
        args.remove_stateful_external_ips)

    return policy_utils.UpdateStatefulPolicy(
        client.messages, stateful_policy,
        None, stateful_internal_ips, stateful_external_ips)


UpdateAlpha.detailed_help = UpdateBeta.detailed_help
