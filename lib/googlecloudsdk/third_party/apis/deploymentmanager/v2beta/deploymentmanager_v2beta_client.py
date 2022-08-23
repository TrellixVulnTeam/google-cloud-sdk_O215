"""Generated client library for deploymentmanager version v2beta."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.deploymentmanager.v2beta import deploymentmanager_v2beta_messages as messages


class DeploymentmanagerV2beta(base_api.BaseApiClient):
  """Generated client library for service deploymentmanager version v2beta."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://www.googleapis.com/deploymentmanager/v2beta/'
  MTLS_BASE_URL = ''

  _PACKAGE = 'deploymentmanager'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only', 'https://www.googleapis.com/auth/ndev.cloudman', 'https://www.googleapis.com/auth/ndev.cloudman.readonly']
  _VERSION = 'v2beta'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DeploymentmanagerV2beta'
  _URL_VERSION = 'v2beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new deploymentmanager handle."""
    url = url or self.BASE_URL
    super(DeploymentmanagerV2beta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.compositeTypes = self.CompositeTypesService(self)
    self.deployments = self.DeploymentsService(self)
    self.manifests = self.ManifestsService(self)
    self.operations = self.OperationsService(self)
    self.resources = self.ResourcesService(self)
    self.typeProviders = self.TypeProvidersService(self)
    self.types = self.TypesService(self)

  class CompositeTypesService(base_api.BaseApiService):
    """Service class for the compositeTypes resource."""

    _NAME = 'compositeTypes'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.CompositeTypesService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='deploymentmanager.compositeTypes.delete',
        ordered_params=['project', 'compositeType'],
        path_params=['compositeType', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/compositeTypes/{compositeType}',
        request_field='',
        request_type_name='DeploymentmanagerCompositeTypesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a specific composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CompositeType) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.compositeTypes.get',
        ordered_params=['project', 'compositeType'],
        path_params=['compositeType', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/compositeTypes/{compositeType}',
        request_field='',
        request_type_name='DeploymentmanagerCompositeTypesGetRequest',
        response_type_name='CompositeType',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      r"""Creates a composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.compositeTypes.insert',
        ordered_params=['project'],
        path_params=['project'],
        query_params=[],
        relative_path='projects/{project}/global/compositeTypes',
        request_field='compositeType',
        request_type_name='DeploymentmanagerCompositeTypesInsertRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all composite types for Deployment Manager.

      Args:
        request: (DeploymentmanagerCompositeTypesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CompositeTypesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.compositeTypes.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken', 'returnPartialSuccess'],
        relative_path='projects/{project}/global/compositeTypes',
        request_field='',
        request_type_name='DeploymentmanagerCompositeTypesListRequest',
        response_type_name='CompositeTypesListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patches a composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='deploymentmanager.compositeTypes.patch',
        ordered_params=['project', 'compositeType'],
        path_params=['compositeType', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/compositeTypes/{compositeType}',
        request_field='compositeTypeResource',
        request_type_name='DeploymentmanagerCompositeTypesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='deploymentmanager.compositeTypes.update',
        ordered_params=['project', 'compositeType'],
        path_params=['compositeType', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/compositeTypes/{compositeType}',
        request_field='compositeTypeResource',
        request_type_name='DeploymentmanagerCompositeTypesUpdateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class DeploymentsService(base_api.BaseApiService):
    """Service class for the deployments resource."""

    _NAME = 'deployments'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.DeploymentsService, self).__init__(client)
      self._upload_configs = {
          }

    def CancelPreview(self, request, global_params=None):
      r"""Cancels and removes the preview currently associated with the deployment.

      Args:
        request: (DeploymentmanagerDeploymentsCancelPreviewRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('CancelPreview')
      return self._RunMethod(
          config, request, global_params=global_params)

    CancelPreview.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.cancelPreview',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/deployments/{deployment}/cancelPreview',
        request_field='deploymentsCancelPreviewRequest',
        request_type_name='DeploymentmanagerDeploymentsCancelPreviewRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a deployment and all of the resources in the deployment.

      Args:
        request: (DeploymentmanagerDeploymentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='deploymentmanager.deployments.delete',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['deletePolicy'],
        relative_path='projects/{project}/global/deployments/{deployment}',
        request_field='',
        request_type_name='DeploymentmanagerDeploymentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a specific deployment.

      Args:
        request: (DeploymentmanagerDeploymentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Deployment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.deployments.get',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/deployments/{deployment}',
        request_field='',
        request_type_name='DeploymentmanagerDeploymentsGetRequest',
        response_type_name='Deployment',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. May be empty if no such policy or resource exists.

      Args:
        request: (DeploymentmanagerDeploymentsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.deployments.getIamPolicy',
        ordered_params=['project', 'resource'],
        path_params=['project', 'resource'],
        query_params=['optionsRequestedPolicyVersion'],
        relative_path='projects/{project}/global/deployments/{resource}/getIamPolicy',
        request_field='',
        request_type_name='DeploymentmanagerDeploymentsGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      r"""Creates a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.insert',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['createPolicy', 'preview'],
        relative_path='projects/{project}/global/deployments',
        request_field='deployment',
        request_type_name='DeploymentmanagerDeploymentsInsertRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all deployments for a given project.

      Args:
        request: (DeploymentmanagerDeploymentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeploymentsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.deployments.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken', 'returnPartialSuccess'],
        relative_path='projects/{project}/global/deployments',
        request_field='',
        request_type_name='DeploymentmanagerDeploymentsListRequest',
        response_type_name='DeploymentsListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patches a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='deploymentmanager.deployments.patch',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['createPolicy', 'deletePolicy', 'preview'],
        relative_path='projects/{project}/global/deployments/{deployment}',
        request_field='deploymentResource',
        request_type_name='DeploymentmanagerDeploymentsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy.

      Args:
        request: (DeploymentmanagerDeploymentsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.setIamPolicy',
        ordered_params=['project', 'resource'],
        path_params=['project', 'resource'],
        query_params=[],
        relative_path='projects/{project}/global/deployments/{resource}/setIamPolicy',
        request_field='globalSetPolicyRequest',
        request_type_name='DeploymentmanagerDeploymentsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def Stop(self, request, global_params=None):
      r"""Stops an ongoing operation. This does not roll back any work that has already been completed, but prevents any new work from being started.

      Args:
        request: (DeploymentmanagerDeploymentsStopRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Stop')
      return self._RunMethod(
          config, request, global_params=global_params)

    Stop.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.stop',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/deployments/{deployment}/stop',
        request_field='deploymentsStopRequest',
        request_type_name='DeploymentmanagerDeploymentsStopRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.

      Args:
        request: (DeploymentmanagerDeploymentsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.testIamPermissions',
        ordered_params=['project', 'resource'],
        path_params=['project', 'resource'],
        query_params=[],
        relative_path='projects/{project}/global/deployments/{resource}/testIamPermissions',
        request_field='testPermissionsRequest',
        request_type_name='DeploymentmanagerDeploymentsTestIamPermissionsRequest',
        response_type_name='TestPermissionsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='deploymentmanager.deployments.update',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['createPolicy', 'deletePolicy', 'preview'],
        relative_path='projects/{project}/global/deployments/{deployment}',
        request_field='deploymentResource',
        request_type_name='DeploymentmanagerDeploymentsUpdateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ManifestsService(base_api.BaseApiService):
    """Service class for the manifests resource."""

    _NAME = 'manifests'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.ManifestsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a specific manifest.

      Args:
        request: (DeploymentmanagerManifestsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Manifest) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.manifests.get',
        ordered_params=['project', 'deployment', 'manifest'],
        path_params=['deployment', 'manifest', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/deployments/{deployment}/manifests/{manifest}',
        request_field='',
        request_type_name='DeploymentmanagerManifestsGetRequest',
        response_type_name='Manifest',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all manifests for a given deployment.

      Args:
        request: (DeploymentmanagerManifestsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManifestsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.manifests.list',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken', 'returnPartialSuccess'],
        relative_path='projects/{project}/global/deployments/{deployment}/manifests',
        request_field='',
        request_type_name='DeploymentmanagerManifestsListRequest',
        response_type_name='ManifestsListResponse',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a specific operation.

      Args:
        request: (DeploymentmanagerOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.operations.get',
        ordered_params=['project', 'operation'],
        path_params=['operation', 'project'],
        query_params=[],
        relative_path='projects/{project}/global/operations/{operation}',
        request_field='',
        request_type_name='DeploymentmanagerOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all operations for a project.

      Args:
        request: (DeploymentmanagerOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (OperationsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.operations.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken', 'returnPartialSuccess'],
        relative_path='projects/{project}/global/operations',
        request_field='',
        request_type_name='DeploymentmanagerOperationsListRequest',
        response_type_name='OperationsListResponse',
        supports_download=False,
    )

  class ResourcesService(base_api.BaseApiService):
    """Service class for the resources resource."""

    _NAME = 'resources'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.ResourcesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a single resource.

      Args:
        request: (DeploymentmanagerResourcesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Resource) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.resources.get',
        ordered_params=['project', 'deployment', 'resource'],
        path_params=['deployment', 'project', 'resource'],
        query_params=[],
        relative_path='projects/{project}/global/deployments/{deployment}/resources/{resource}',
        request_field='',
        request_type_name='DeploymentmanagerResourcesGetRequest',
        response_type_name='Resource',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all resources in a given deployment.

      Args:
        request: (DeploymentmanagerResourcesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourcesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.resources.list',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken', 'returnPartialSuccess'],
        relative_path='projects/{project}/global/deployments/{deployment}/resources',
        request_field='',
        request_type_name='DeploymentmanagerResourcesListRequest',
        response_type_name='ResourcesListResponse',
        supports_download=False,
    )

  class TypeProvidersService(base_api.BaseApiService):
    """Service class for the typeProviders resource."""

    _NAME = 'typeProviders'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.TypeProvidersService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='deploymentmanager.typeProviders.delete',
        ordered_params=['project', 'typeProvider'],
        path_params=['project', 'typeProvider'],
        query_params=[],
        relative_path='projects/{project}/global/typeProviders/{typeProvider}',
        request_field='',
        request_type_name='DeploymentmanagerTypeProvidersDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a specific type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypeProvider) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.typeProviders.get',
        ordered_params=['project', 'typeProvider'],
        path_params=['project', 'typeProvider'],
        query_params=[],
        relative_path='projects/{project}/global/typeProviders/{typeProvider}',
        request_field='',
        request_type_name='DeploymentmanagerTypeProvidersGetRequest',
        response_type_name='TypeProvider',
        supports_download=False,
    )

    def GetType(self, request, global_params=None):
      r"""Gets a type info for a type provided by a TypeProvider.

      Args:
        request: (DeploymentmanagerTypeProvidersGetTypeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypeInfo) The response message.
      """
      config = self.GetMethodConfig('GetType')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetType.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.typeProviders.getType',
        ordered_params=['project', 'typeProvider', 'type'],
        path_params=['project', 'type', 'typeProvider'],
        query_params=[],
        relative_path='projects/{project}/global/typeProviders/{typeProvider}/types/{type}',
        request_field='',
        request_type_name='DeploymentmanagerTypeProvidersGetTypeRequest',
        response_type_name='TypeInfo',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      r"""Creates a type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.typeProviders.insert',
        ordered_params=['project'],
        path_params=['project'],
        query_params=[],
        relative_path='projects/{project}/global/typeProviders',
        request_field='typeProvider',
        request_type_name='DeploymentmanagerTypeProvidersInsertRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all resource type providers for Deployment Manager.

      Args:
        request: (DeploymentmanagerTypeProvidersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypeProvidersListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.typeProviders.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken', 'returnPartialSuccess'],
        relative_path='projects/{project}/global/typeProviders',
        request_field='',
        request_type_name='DeploymentmanagerTypeProvidersListRequest',
        response_type_name='TypeProvidersListResponse',
        supports_download=False,
    )

    def ListTypes(self, request, global_params=None):
      r"""Lists all the type info for a TypeProvider.

      Args:
        request: (DeploymentmanagerTypeProvidersListTypesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypeProvidersListTypesResponse) The response message.
      """
      config = self.GetMethodConfig('ListTypes')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListTypes.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.typeProviders.listTypes',
        ordered_params=['project', 'typeProvider'],
        path_params=['project', 'typeProvider'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken', 'returnPartialSuccess'],
        relative_path='projects/{project}/global/typeProviders/{typeProvider}/types',
        request_field='',
        request_type_name='DeploymentmanagerTypeProvidersListTypesRequest',
        response_type_name='TypeProvidersListTypesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patches a type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='deploymentmanager.typeProviders.patch',
        ordered_params=['project', 'typeProvider'],
        path_params=['project', 'typeProvider'],
        query_params=[],
        relative_path='projects/{project}/global/typeProviders/{typeProvider}',
        request_field='typeProviderResource',
        request_type_name='DeploymentmanagerTypeProvidersPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='deploymentmanager.typeProviders.update',
        ordered_params=['project', 'typeProvider'],
        path_params=['project', 'typeProvider'],
        query_params=[],
        relative_path='projects/{project}/global/typeProviders/{typeProvider}',
        request_field='typeProviderResource',
        request_type_name='DeploymentmanagerTypeProvidersUpdateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class TypesService(base_api.BaseApiService):
    """Service class for the types resource."""

    _NAME = 'types'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.TypesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists all resource types for Deployment Manager.

      Args:
        request: (DeploymentmanagerTypesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.types.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken', 'returnPartialSuccess'],
        relative_path='projects/{project}/global/types',
        request_field='',
        request_type_name='DeploymentmanagerTypesListRequest',
        response_type_name='TypesListResponse',
        supports_download=False,
    )
