"""Generated client library for orgpolicy version v2."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.orgpolicy.v2 import orgpolicy_v2_messages as messages


class OrgpolicyV2(base_api.BaseApiClient):
  """Generated client library for service orgpolicy version v2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://orgpolicy.googleapis.com/'
  MTLS_BASE_URL = 'https://orgpolicy.mtls.googleapis.com/'

  _PACKAGE = 'orgpolicy'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v2'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'OrgpolicyV2'
  _URL_VERSION = 'v2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new orgpolicy handle."""
    url = url or self.BASE_URL
    super(OrgpolicyV2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.folders_constraints = self.FoldersConstraintsService(self)
    self.folders_policies = self.FoldersPoliciesService(self)
    self.folders = self.FoldersService(self)
    self.organizations_constraints = self.OrganizationsConstraintsService(self)
    self.organizations_customConstraints = self.OrganizationsCustomConstraintsService(self)
    self.organizations_policies = self.OrganizationsPoliciesService(self)
    self.organizations = self.OrganizationsService(self)
    self.projects_constraints = self.ProjectsConstraintsService(self)
    self.projects_policies = self.ProjectsPoliciesService(self)
    self.projects = self.ProjectsService(self)

  class FoldersConstraintsService(base_api.BaseApiService):
    """Service class for the folders_constraints resource."""

    _NAME = 'folders_constraints'

    def __init__(self, client):
      super(OrgpolicyV2.FoldersConstraintsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists `Constraints` that could be applied on the specified resource.

      Args:
        request: (OrgpolicyFoldersConstraintsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2ListConstraintsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/folders/{foldersId}/constraints',
        http_method='GET',
        method_id='orgpolicy.folders.constraints.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2/{+parent}/constraints',
        request_field='',
        request_type_name='OrgpolicyFoldersConstraintsListRequest',
        response_type_name='GoogleCloudOrgpolicyV2ListConstraintsResponse',
        supports_download=False,
    )

  class FoldersPoliciesService(base_api.BaseApiService):
    """Service class for the folders_policies resource."""

    _NAME = 'folders_policies'

    def __init__(self, client):
      super(OrgpolicyV2.FoldersPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Cloud resource.

      Args:
        request: (OrgpolicyFoldersPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/folders/{foldersId}/policies',
        http_method='POST',
        method_id='orgpolicy.folders.policies.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v2/{+parent}/policies',
        request_field='googleCloudOrgpolicyV2Policy',
        request_type_name='OrgpolicyFoldersPoliciesCreateRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or Org Policy does not exist.

      Args:
        request: (OrgpolicyFoldersPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/folders/{foldersId}/policies/{policiesId}',
        http_method='DELETE',
        method_id='orgpolicy.folders.policies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}',
        request_field='',
        request_type_name='OrgpolicyFoldersPoliciesDeleteRequest',
        response_type_name='GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a `Policy` on a resource. If no `Policy` is set on the resource, NOT_FOUND is returned. The `etag` value can be used with `UpdatePolicy()` to update a `Policy` during read-modify-write.

      Args:
        request: (OrgpolicyFoldersPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/folders/{foldersId}/policies/{policiesId}',
        http_method='GET',
        method_id='orgpolicy.folders.policies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}',
        request_field='',
        request_type_name='OrgpolicyFoldersPoliciesGetRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def GetEffectivePolicy(self, request, global_params=None):
      r"""Gets the effective `Policy` on a resource. This is the result of merging `Policies` in the resource hierarchy and evaluating conditions. The returned `Policy` will not have an `etag` or `condition` set because it is a computed `Policy` across multiple resources. Subtrees of Resource Manager resource hierarchy with 'under:' prefix will not be expanded.

      Args:
        request: (OrgpolicyFoldersPoliciesGetEffectivePolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('GetEffectivePolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetEffectivePolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/folders/{foldersId}/policies/{policiesId}:getEffectivePolicy',
        http_method='GET',
        method_id='orgpolicy.folders.policies.getEffectivePolicy',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}:getEffectivePolicy',
        request_field='',
        request_type_name='OrgpolicyFoldersPoliciesGetEffectivePolicyRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Retrieves all of the `Policies` that exist on a particular resource.

      Args:
        request: (OrgpolicyFoldersPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2ListPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/folders/{foldersId}/policies',
        http_method='GET',
        method_id='orgpolicy.folders.policies.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2/{+parent}/policies',
        request_field='',
        request_type_name='OrgpolicyFoldersPoliciesListRequest',
        response_type_name='GoogleCloudOrgpolicyV2ListPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields.

      Args:
        request: (OrgpolicyFoldersPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/folders/{foldersId}/policies/{policiesId}',
        http_method='PATCH',
        method_id='orgpolicy.folders.policies.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v2/{+name}',
        request_field='googleCloudOrgpolicyV2Policy',
        request_type_name='OrgpolicyFoldersPoliciesPatchRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

  class FoldersService(base_api.BaseApiService):
    """Service class for the folders resource."""

    _NAME = 'folders'

    def __init__(self, client):
      super(OrgpolicyV2.FoldersService, self).__init__(client)
      self._upload_configs = {
          }

  class OrganizationsConstraintsService(base_api.BaseApiService):
    """Service class for the organizations_constraints resource."""

    _NAME = 'organizations_constraints'

    def __init__(self, client):
      super(OrgpolicyV2.OrganizationsConstraintsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists `Constraints` that could be applied on the specified resource.

      Args:
        request: (OrgpolicyOrganizationsConstraintsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2ListConstraintsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/constraints',
        http_method='GET',
        method_id='orgpolicy.organizations.constraints.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2/{+parent}/constraints',
        request_field='',
        request_type_name='OrgpolicyOrganizationsConstraintsListRequest',
        response_type_name='GoogleCloudOrgpolicyV2ListConstraintsResponse',
        supports_download=False,
    )

  class OrganizationsCustomConstraintsService(base_api.BaseApiService):
    """Service class for the organizations_customConstraints resource."""

    _NAME = 'organizations_customConstraints'

    def __init__(self, client):
      super(OrgpolicyV2.OrganizationsCustomConstraintsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a CustomConstraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the organization does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the constraint already exists on the given organization.

      Args:
        request: (OrgpolicyOrganizationsCustomConstraintsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2CustomConstraint) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/customConstraints',
        http_method='POST',
        method_id='orgpolicy.organizations.customConstraints.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['validateOnly'],
        relative_path='v2/{+parent}/customConstraints',
        request_field='googleCloudOrgpolicyV2CustomConstraint',
        request_type_name='OrgpolicyOrganizationsCustomConstraintsCreateRequest',
        response_type_name='GoogleCloudOrgpolicyV2CustomConstraint',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a Custom Constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist.

      Args:
        request: (OrgpolicyOrganizationsCustomConstraintsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/customConstraints/{customConstraintsId}',
        http_method='DELETE',
        method_id='orgpolicy.organizations.customConstraints.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}',
        request_field='',
        request_type_name='OrgpolicyOrganizationsCustomConstraintsDeleteRequest',
        response_type_name='GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a CustomConstraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the CustomConstraint does not exist.

      Args:
        request: (OrgpolicyOrganizationsCustomConstraintsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2CustomConstraint) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/customConstraints/{customConstraintsId}',
        http_method='GET',
        method_id='orgpolicy.organizations.customConstraints.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}',
        request_field='',
        request_type_name='OrgpolicyOrganizationsCustomConstraintsGetRequest',
        response_type_name='GoogleCloudOrgpolicyV2CustomConstraint',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Retrieves all of the `CustomConstraints` that exist on a particular organization resource.

      Args:
        request: (OrgpolicyOrganizationsCustomConstraintsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2ListCustomConstraintsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/customConstraints',
        http_method='GET',
        method_id='orgpolicy.organizations.customConstraints.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2/{+parent}/customConstraints',
        request_field='',
        request_type_name='OrgpolicyOrganizationsCustomConstraintsListRequest',
        response_type_name='GoogleCloudOrgpolicyV2ListCustomConstraintsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a Custom Constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Note: the supplied policy will perform a full overwrite of all fields.

      Args:
        request: (OrgpolicyOrganizationsCustomConstraintsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2CustomConstraint) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/customConstraints/{customConstraintsId}',
        http_method='PATCH',
        method_id='orgpolicy.organizations.customConstraints.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['validateOnly'],
        relative_path='v2/{+name}',
        request_field='googleCloudOrgpolicyV2CustomConstraint',
        request_type_name='OrgpolicyOrganizationsCustomConstraintsPatchRequest',
        response_type_name='GoogleCloudOrgpolicyV2CustomConstraint',
        supports_download=False,
    )

  class OrganizationsPoliciesService(base_api.BaseApiService):
    """Service class for the organizations_policies resource."""

    _NAME = 'organizations_policies'

    def __init__(self, client):
      super(OrgpolicyV2.OrganizationsPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Cloud resource.

      Args:
        request: (OrgpolicyOrganizationsPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/policies',
        http_method='POST',
        method_id='orgpolicy.organizations.policies.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v2/{+parent}/policies',
        request_field='googleCloudOrgpolicyV2Policy',
        request_type_name='OrgpolicyOrganizationsPoliciesCreateRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or Org Policy does not exist.

      Args:
        request: (OrgpolicyOrganizationsPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/policies/{policiesId}',
        http_method='DELETE',
        method_id='orgpolicy.organizations.policies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}',
        request_field='',
        request_type_name='OrgpolicyOrganizationsPoliciesDeleteRequest',
        response_type_name='GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a `Policy` on a resource. If no `Policy` is set on the resource, NOT_FOUND is returned. The `etag` value can be used with `UpdatePolicy()` to update a `Policy` during read-modify-write.

      Args:
        request: (OrgpolicyOrganizationsPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/policies/{policiesId}',
        http_method='GET',
        method_id='orgpolicy.organizations.policies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}',
        request_field='',
        request_type_name='OrgpolicyOrganizationsPoliciesGetRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def GetEffectivePolicy(self, request, global_params=None):
      r"""Gets the effective `Policy` on a resource. This is the result of merging `Policies` in the resource hierarchy and evaluating conditions. The returned `Policy` will not have an `etag` or `condition` set because it is a computed `Policy` across multiple resources. Subtrees of Resource Manager resource hierarchy with 'under:' prefix will not be expanded.

      Args:
        request: (OrgpolicyOrganizationsPoliciesGetEffectivePolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('GetEffectivePolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetEffectivePolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/policies/{policiesId}:getEffectivePolicy',
        http_method='GET',
        method_id='orgpolicy.organizations.policies.getEffectivePolicy',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}:getEffectivePolicy',
        request_field='',
        request_type_name='OrgpolicyOrganizationsPoliciesGetEffectivePolicyRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Retrieves all of the `Policies` that exist on a particular resource.

      Args:
        request: (OrgpolicyOrganizationsPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2ListPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/policies',
        http_method='GET',
        method_id='orgpolicy.organizations.policies.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2/{+parent}/policies',
        request_field='',
        request_type_name='OrgpolicyOrganizationsPoliciesListRequest',
        response_type_name='GoogleCloudOrgpolicyV2ListPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields.

      Args:
        request: (OrgpolicyOrganizationsPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/organizations/{organizationsId}/policies/{policiesId}',
        http_method='PATCH',
        method_id='orgpolicy.organizations.policies.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v2/{+name}',
        request_field='googleCloudOrgpolicyV2Policy',
        request_type_name='OrgpolicyOrganizationsPoliciesPatchRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(OrgpolicyV2.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsConstraintsService(base_api.BaseApiService):
    """Service class for the projects_constraints resource."""

    _NAME = 'projects_constraints'

    def __init__(self, client):
      super(OrgpolicyV2.ProjectsConstraintsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists `Constraints` that could be applied on the specified resource.

      Args:
        request: (OrgpolicyProjectsConstraintsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2ListConstraintsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/projects/{projectsId}/constraints',
        http_method='GET',
        method_id='orgpolicy.projects.constraints.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2/{+parent}/constraints',
        request_field='',
        request_type_name='OrgpolicyProjectsConstraintsListRequest',
        response_type_name='GoogleCloudOrgpolicyV2ListConstraintsResponse',
        supports_download=False,
    )

  class ProjectsPoliciesService(base_api.BaseApiService):
    """Service class for the projects_policies resource."""

    _NAME = 'projects_policies'

    def __init__(self, client):
      super(OrgpolicyV2.ProjectsPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Cloud resource.

      Args:
        request: (OrgpolicyProjectsPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/projects/{projectsId}/policies',
        http_method='POST',
        method_id='orgpolicy.projects.policies.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v2/{+parent}/policies',
        request_field='googleCloudOrgpolicyV2Policy',
        request_type_name='OrgpolicyProjectsPoliciesCreateRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or Org Policy does not exist.

      Args:
        request: (OrgpolicyProjectsPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/projects/{projectsId}/policies/{policiesId}',
        http_method='DELETE',
        method_id='orgpolicy.projects.policies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}',
        request_field='',
        request_type_name='OrgpolicyProjectsPoliciesDeleteRequest',
        response_type_name='GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a `Policy` on a resource. If no `Policy` is set on the resource, NOT_FOUND is returned. The `etag` value can be used with `UpdatePolicy()` to update a `Policy` during read-modify-write.

      Args:
        request: (OrgpolicyProjectsPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/projects/{projectsId}/policies/{policiesId}',
        http_method='GET',
        method_id='orgpolicy.projects.policies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}',
        request_field='',
        request_type_name='OrgpolicyProjectsPoliciesGetRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def GetEffectivePolicy(self, request, global_params=None):
      r"""Gets the effective `Policy` on a resource. This is the result of merging `Policies` in the resource hierarchy and evaluating conditions. The returned `Policy` will not have an `etag` or `condition` set because it is a computed `Policy` across multiple resources. Subtrees of Resource Manager resource hierarchy with 'under:' prefix will not be expanded.

      Args:
        request: (OrgpolicyProjectsPoliciesGetEffectivePolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('GetEffectivePolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetEffectivePolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/projects/{projectsId}/policies/{policiesId}:getEffectivePolicy',
        http_method='GET',
        method_id='orgpolicy.projects.policies.getEffectivePolicy',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2/{+name}:getEffectivePolicy',
        request_field='',
        request_type_name='OrgpolicyProjectsPoliciesGetEffectivePolicyRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Retrieves all of the `Policies` that exist on a particular resource.

      Args:
        request: (OrgpolicyProjectsPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2ListPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/projects/{projectsId}/policies',
        http_method='GET',
        method_id='orgpolicy.projects.policies.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2/{+parent}/policies',
        request_field='',
        request_type_name='OrgpolicyProjectsPoliciesListRequest',
        response_type_name='GoogleCloudOrgpolicyV2ListPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields.

      Args:
        request: (OrgpolicyProjectsPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudOrgpolicyV2Policy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2/projects/{projectsId}/policies/{policiesId}',
        http_method='PATCH',
        method_id='orgpolicy.projects.policies.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v2/{+name}',
        request_field='googleCloudOrgpolicyV2Policy',
        request_type_name='OrgpolicyProjectsPoliciesPatchRequest',
        response_type_name='GoogleCloudOrgpolicyV2Policy',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(OrgpolicyV2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
