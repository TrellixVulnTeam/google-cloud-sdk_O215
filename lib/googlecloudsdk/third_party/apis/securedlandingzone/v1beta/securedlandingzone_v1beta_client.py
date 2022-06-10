"""Generated client library for securedlandingzone version v1beta."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.securedlandingzone.v1beta import securedlandingzone_v1beta_messages as messages


class SecuredlandingzoneV1beta(base_api.BaseApiClient):
  """Generated client library for service securedlandingzone version v1beta."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://securedlandingzone.googleapis.com/'
  MTLS_BASE_URL = 'https://securedlandingzone.mtls.googleapis.com/'

  _PACKAGE = 'securedlandingzone'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'SecuredlandingzoneV1beta'
  _URL_VERSION = 'v1beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new securedlandingzone handle."""
    url = url or self.BASE_URL
    super(SecuredlandingzoneV1beta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.organizations_locations_operations = self.OrganizationsLocationsOperationsService(self)
    self.organizations_locations_overwatches = self.OrganizationsLocationsOverwatchesService(self)
    self.organizations_locations = self.OrganizationsLocationsService(self)
    self.organizations = self.OrganizationsService(self)

  class OrganizationsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the organizations_locations_operations resource."""

    _NAME = 'organizations_locations_operations'

    def __init__(self, client):
      super(SecuredlandingzoneV1beta.OrganizationsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='securedlandingzone.organizations.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='SecuredlandingzoneOrganizationsLocationsOperationsGetRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class OrganizationsLocationsOverwatchesService(base_api.BaseApiService):
    """Service class for the organizations_locations_overwatches resource."""

    _NAME = 'organizations_locations_overwatches'

    def __init__(self, client):
      super(SecuredlandingzoneV1beta.OrganizationsLocationsOverwatchesService, self).__init__(client)
      self._upload_configs = {
          }

    def Activate(self, request, global_params=None):
      r"""Activate an overwatch resource. This sets the state to ACTIVE, response actions will now be taken against signals according to the playbook.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsOverwatchesActivateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudSecuredlandingzoneV1betaOverwatch) The response message.
      """
      config = self.GetMethodConfig('Activate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Activate.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}/overwatches/{overwatchesId}:activate',
        http_method='POST',
        method_id='securedlandingzone.organizations.locations.overwatches.activate',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}:activate',
        request_field='googleCloudSecuredlandingzoneV1betaActivateOverwatchRequest',
        request_type_name='SecuredlandingzoneOrganizationsLocationsOverwatchesActivateRequest',
        response_type_name='GoogleCloudSecuredlandingzoneV1betaOverwatch',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Create a new overwatch resource.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsOverwatchesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}/overwatches',
        http_method='POST',
        method_id='securedlandingzone.organizations.locations.overwatches.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['overwatchId'],
        relative_path='v1beta/{+parent}/overwatches',
        request_field='googleCloudSecuredlandingzoneV1betaOverwatch',
        request_type_name='SecuredlandingzoneOrganizationsLocationsOverwatchesCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an overwatch resource.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsOverwatchesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}/overwatches/{overwatchesId}',
        http_method='DELETE',
        method_id='securedlandingzone.organizations.locations.overwatches.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='SecuredlandingzoneOrganizationsLocationsOverwatchesDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an overwatch resource.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsOverwatchesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudSecuredlandingzoneV1betaOverwatch) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}/overwatches/{overwatchesId}',
        http_method='GET',
        method_id='securedlandingzone.organizations.locations.overwatches.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='SecuredlandingzoneOrganizationsLocationsOverwatchesGetRequest',
        response_type_name='GoogleCloudSecuredlandingzoneV1betaOverwatch',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List overwatch resources created under a parent resource.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsOverwatchesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudSecuredlandingzoneV1betaListOverwatchesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}/overwatches',
        http_method='GET',
        method_id='securedlandingzone.organizations.locations.overwatches.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1beta/{+parent}/overwatches',
        request_field='',
        request_type_name='SecuredlandingzoneOrganizationsLocationsOverwatchesListRequest',
        response_type_name='GoogleCloudSecuredlandingzoneV1betaListOverwatchesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update the blueprint deployed resources of an overwatch resource.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsOverwatchesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}/overwatches/{overwatchesId}',
        http_method='PATCH',
        method_id='securedlandingzone.organizations.locations.overwatches.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta/{+name}',
        request_field='googleCloudSecuredlandingzoneV1betaOverwatch',
        request_type_name='SecuredlandingzoneOrganizationsLocationsOverwatchesPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Suspend(self, request, global_params=None):
      r"""Suspend an overwatch resource. This sets the state to SUSPENDED, and will stop all future response actions.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsOverwatchesSuspendRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudSecuredlandingzoneV1betaOverwatch) The response message.
      """
      config = self.GetMethodConfig('Suspend')
      return self._RunMethod(
          config, request, global_params=global_params)

    Suspend.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}/overwatches/{overwatchesId}:suspend',
        http_method='POST',
        method_id='securedlandingzone.organizations.locations.overwatches.suspend',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}:suspend',
        request_field='googleCloudSecuredlandingzoneV1betaSuspendOverwatchRequest',
        request_type_name='SecuredlandingzoneOrganizationsLocationsOverwatchesSuspendRequest',
        response_type_name='GoogleCloudSecuredlandingzoneV1betaOverwatch',
        supports_download=False,
    )

  class OrganizationsLocationsService(base_api.BaseApiService):
    """Service class for the organizations_locations resource."""

    _NAME = 'organizations_locations'

    def __init__(self, client):
      super(SecuredlandingzoneV1beta.OrganizationsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def EnableOverwatch(self, request, global_params=None):
      r"""Enables the Secured Landing Zone Overwatch service for an organization in a region.

      Args:
        request: (SecuredlandingzoneOrganizationsLocationsEnableOverwatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudSecuredlandingzoneV1betaEnableOverwatchResponse) The response message.
      """
      config = self.GetMethodConfig('EnableOverwatch')
      return self._RunMethod(
          config, request, global_params=global_params)

    EnableOverwatch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/organizations/{organizationsId}/locations/{locationsId}:enableOverwatch',
        http_method='POST',
        method_id='securedlandingzone.organizations.locations.enableOverwatch',
        ordered_params=['organization'],
        path_params=['organization'],
        query_params=[],
        relative_path='v1beta/{+organization}:enableOverwatch',
        request_field='googleCloudSecuredlandingzoneV1betaEnableOverwatchRequest',
        request_type_name='SecuredlandingzoneOrganizationsLocationsEnableOverwatchRequest',
        response_type_name='GoogleCloudSecuredlandingzoneV1betaEnableOverwatchResponse',
        supports_download=False,
    )

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(SecuredlandingzoneV1beta.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }
