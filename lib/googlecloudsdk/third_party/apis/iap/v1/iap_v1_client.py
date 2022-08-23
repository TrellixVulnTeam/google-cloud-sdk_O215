"""Generated client library for iap version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.iap.v1 import iap_v1_messages as messages


class IapV1(base_api.BaseApiClient):
  """Generated client library for service iap version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://iap.googleapis.com/'
  MTLS_BASE_URL = 'https://iap.mtls.googleapis.com/'

  _PACKAGE = 'iap'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'IapV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new iap handle."""
    url = url or self.BASE_URL
    super(IapV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_brands_identityAwareProxyClients = self.ProjectsBrandsIdentityAwareProxyClientsService(self)
    self.projects_brands = self.ProjectsBrandsService(self)
    self.projects_iap_tunnel_locations_destGroups = self.ProjectsIapTunnelLocationsDestGroupsService(self)
    self.projects_iap_tunnel_locations = self.ProjectsIapTunnelLocationsService(self)
    self.projects_iap_tunnel = self.ProjectsIapTunnelService(self)
    self.projects = self.ProjectsService(self)
    self.v1 = self.V1Service(self)

  class ProjectsBrandsIdentityAwareProxyClientsService(base_api.BaseApiService):
    """Service class for the projects_brands_identityAwareProxyClients resource."""

    _NAME = 'projects_brands_identityAwareProxyClients'

    def __init__(self, client):
      super(IapV1.ProjectsBrandsIdentityAwareProxyClientsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates an Identity Aware Proxy (IAP) OAuth client. The client is owned by IAP. Requires that the brand for the project exists and that it is set for internal-only use.

      Args:
        request: (IapProjectsBrandsIdentityAwareProxyClientsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IdentityAwareProxyClient) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/brands/{brandsId}/identityAwareProxyClients',
        http_method='POST',
        method_id='iap.projects.brands.identityAwareProxyClients.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/identityAwareProxyClients',
        request_field='identityAwareProxyClient',
        request_type_name='IapProjectsBrandsIdentityAwareProxyClientsCreateRequest',
        response_type_name='IdentityAwareProxyClient',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an Identity Aware Proxy (IAP) OAuth client. Useful for removing obsolete clients, managing the number of clients in a given project, and cleaning up after tests. Requires that the client is owned by IAP.

      Args:
        request: (IapProjectsBrandsIdentityAwareProxyClientsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/brands/{brandsId}/identityAwareProxyClients/{identityAwareProxyClientsId}',
        http_method='DELETE',
        method_id='iap.projects.brands.identityAwareProxyClients.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='IapProjectsBrandsIdentityAwareProxyClientsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves an Identity Aware Proxy (IAP) OAuth client. Requires that the client is owned by IAP.

      Args:
        request: (IapProjectsBrandsIdentityAwareProxyClientsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IdentityAwareProxyClient) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/brands/{brandsId}/identityAwareProxyClients/{identityAwareProxyClientsId}',
        http_method='GET',
        method_id='iap.projects.brands.identityAwareProxyClients.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='IapProjectsBrandsIdentityAwareProxyClientsGetRequest',
        response_type_name='IdentityAwareProxyClient',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the existing clients for the brand.

      Args:
        request: (IapProjectsBrandsIdentityAwareProxyClientsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListIdentityAwareProxyClientsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/brands/{brandsId}/identityAwareProxyClients',
        http_method='GET',
        method_id='iap.projects.brands.identityAwareProxyClients.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/identityAwareProxyClients',
        request_field='',
        request_type_name='IapProjectsBrandsIdentityAwareProxyClientsListRequest',
        response_type_name='ListIdentityAwareProxyClientsResponse',
        supports_download=False,
    )

    def ResetSecret(self, request, global_params=None):
      r"""Resets an Identity Aware Proxy (IAP) OAuth client secret. Useful if the secret was compromised. Requires that the client is owned by IAP.

      Args:
        request: (IapProjectsBrandsIdentityAwareProxyClientsResetSecretRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IdentityAwareProxyClient) The response message.
      """
      config = self.GetMethodConfig('ResetSecret')
      return self._RunMethod(
          config, request, global_params=global_params)

    ResetSecret.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/brands/{brandsId}/identityAwareProxyClients/{identityAwareProxyClientsId}:resetSecret',
        http_method='POST',
        method_id='iap.projects.brands.identityAwareProxyClients.resetSecret',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:resetSecret',
        request_field='resetIdentityAwareProxyClientSecretRequest',
        request_type_name='IapProjectsBrandsIdentityAwareProxyClientsResetSecretRequest',
        response_type_name='IdentityAwareProxyClient',
        supports_download=False,
    )

  class ProjectsBrandsService(base_api.BaseApiService):
    """Service class for the projects_brands resource."""

    _NAME = 'projects_brands'

    def __init__(self, client):
      super(IapV1.ProjectsBrandsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Constructs a new OAuth brand for the project if one does not exist. The created brand is "internal only", meaning that OAuth clients created under it only accept requests from users who belong to the same Google Workspace organization as the project. The brand is created in an un-reviewed status. NOTE: The "internal only" status can be manually changed in the Google Cloud Console. Requires that a brand does not already exist for the project, and that the specified support email is owned by the caller.

      Args:
        request: (IapProjectsBrandsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Brand) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/brands',
        http_method='POST',
        method_id='iap.projects.brands.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/brands',
        request_field='brand',
        request_type_name='IapProjectsBrandsCreateRequest',
        response_type_name='Brand',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves the OAuth brand of the project.

      Args:
        request: (IapProjectsBrandsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Brand) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/brands/{brandsId}',
        http_method='GET',
        method_id='iap.projects.brands.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='IapProjectsBrandsGetRequest',
        response_type_name='Brand',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the existing brands for the project.

      Args:
        request: (IapProjectsBrandsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBrandsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/brands',
        http_method='GET',
        method_id='iap.projects.brands.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/brands',
        request_field='',
        request_type_name='IapProjectsBrandsListRequest',
        response_type_name='ListBrandsResponse',
        supports_download=False,
    )

  class ProjectsIapTunnelLocationsDestGroupsService(base_api.BaseApiService):
    """Service class for the projects_iap_tunnel_locations_destGroups resource."""

    _NAME = 'projects_iap_tunnel_locations_destGroups'

    def __init__(self, client):
      super(IapV1.ProjectsIapTunnelLocationsDestGroupsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new TunnelDestGroup.

      Args:
        request: (IapProjectsIapTunnelLocationsDestGroupsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TunnelDestGroup) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/iap_tunnel/locations/{locationsId}/destGroups',
        http_method='POST',
        method_id='iap.projects.iap_tunnel.locations.destGroups.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['tunnelDestGroupId'],
        relative_path='v1/{+parent}/destGroups',
        request_field='tunnelDestGroup',
        request_type_name='IapProjectsIapTunnelLocationsDestGroupsCreateRequest',
        response_type_name='TunnelDestGroup',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a TunnelDestGroup.

      Args:
        request: (IapProjectsIapTunnelLocationsDestGroupsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/iap_tunnel/locations/{locationsId}/destGroups/{destGroupsId}',
        http_method='DELETE',
        method_id='iap.projects.iap_tunnel.locations.destGroups.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='IapProjectsIapTunnelLocationsDestGroupsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves an existing TunnelDestGroup.

      Args:
        request: (IapProjectsIapTunnelLocationsDestGroupsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TunnelDestGroup) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/iap_tunnel/locations/{locationsId}/destGroups/{destGroupsId}',
        http_method='GET',
        method_id='iap.projects.iap_tunnel.locations.destGroups.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='IapProjectsIapTunnelLocationsDestGroupsGetRequest',
        response_type_name='TunnelDestGroup',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the existing TunnelDestGroups. To group across all locations, use a `-` as the location ID. For example: `/v1/projects/123/iap_tunnel/locations/-/destGroups`.

      Args:
        request: (IapProjectsIapTunnelLocationsDestGroupsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTunnelDestGroupsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/iap_tunnel/locations/{locationsId}/destGroups',
        http_method='GET',
        method_id='iap.projects.iap_tunnel.locations.destGroups.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/destGroups',
        request_field='',
        request_type_name='IapProjectsIapTunnelLocationsDestGroupsListRequest',
        response_type_name='ListTunnelDestGroupsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a TunnelDestGroup.

      Args:
        request: (IapProjectsIapTunnelLocationsDestGroupsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TunnelDestGroup) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/iap_tunnel/locations/{locationsId}/destGroups/{destGroupsId}',
        http_method='PATCH',
        method_id='iap.projects.iap_tunnel.locations.destGroups.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='tunnelDestGroup',
        request_type_name='IapProjectsIapTunnelLocationsDestGroupsPatchRequest',
        response_type_name='TunnelDestGroup',
        supports_download=False,
    )

  class ProjectsIapTunnelLocationsService(base_api.BaseApiService):
    """Service class for the projects_iap_tunnel_locations resource."""

    _NAME = 'projects_iap_tunnel_locations'

    def __init__(self, client):
      super(IapV1.ProjectsIapTunnelLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsIapTunnelService(base_api.BaseApiService):
    """Service class for the projects_iap_tunnel resource."""

    _NAME = 'projects_iap_tunnel'

    def __init__(self, client):
      super(IapV1.ProjectsIapTunnelService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(IapV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class V1Service(base_api.BaseApiService):
    """Service class for the v1 resource."""

    _NAME = 'v1'

    def __init__(self, client):
      super(IapV1.V1Service, self).__init__(client)
      self._upload_configs = {
          }

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for an Identity-Aware Proxy protected resource. More information about managing access via IAP can be found at: https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api.

      Args:
        request: (IapGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}:getIamPolicy',
        http_method='POST',
        method_id='iap.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:getIamPolicy',
        request_field='getIamPolicyRequest',
        request_type_name='IapGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def GetIapSettings(self, request, global_params=None):
      r"""Gets the IAP settings on a particular IAP protected resource.

      Args:
        request: (IapGetIapSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IapSettings) The response message.
      """
      config = self.GetMethodConfig('GetIapSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIapSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}:iapSettings',
        http_method='GET',
        method_id='iap.getIapSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:iapSettings',
        request_field='',
        request_type_name='IapGetIapSettingsRequest',
        response_type_name='IapSettings',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy for an Identity-Aware Proxy protected resource. Replaces any existing policy. More information about managing access via IAP can be found at: https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api.

      Args:
        request: (IapSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}:setIamPolicy',
        http_method='POST',
        method_id='iap.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='IapSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the Identity-Aware Proxy protected resource. More information about managing access via IAP can be found at: https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api.

      Args:
        request: (IapTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}:testIamPermissions',
        http_method='POST',
        method_id='iap.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='IapTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

    def UpdateIapSettings(self, request, global_params=None):
      r"""Updates the IAP settings on a particular IAP protected resource. It replaces all fields unless the `update_mask` is set.

      Args:
        request: (IapUpdateIapSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IapSettings) The response message.
      """
      config = self.GetMethodConfig('UpdateIapSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateIapSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}:iapSettings',
        http_method='PATCH',
        method_id='iap.updateIapSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}:iapSettings',
        request_field='iapSettings',
        request_type_name='IapUpdateIapSettingsRequest',
        response_type_name='IapSettings',
        supports_download=False,
    )
