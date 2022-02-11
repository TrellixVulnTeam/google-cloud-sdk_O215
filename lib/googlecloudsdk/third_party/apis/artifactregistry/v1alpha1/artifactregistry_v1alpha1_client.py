"""Generated client library for artifactregistry version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.artifactregistry.v1alpha1 import artifactregistry_v1alpha1_messages as messages


class ArtifactregistryV1alpha1(base_api.BaseApiClient):
  """Generated client library for service artifactregistry version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://artifactregistry.googleapis.com/'
  MTLS_BASE_URL = 'https://artifactregistry.mtls.googleapis.com/'

  _PACKAGE = 'artifactregistry'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ArtifactregistryV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new artifactregistry handle."""
    url = url or self.BASE_URL
    super(ArtifactregistryV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_repositories_aptArtifacts = self.ProjectsLocationsRepositoriesAptArtifactsService(self)
    self.projects_locations_repositories_gooGetArtifacts = self.ProjectsLocationsRepositoriesGooGetArtifactsService(self)
    self.projects_locations_repositories_googetArtifacts = self.ProjectsLocationsRepositoriesGoogetArtifactsService(self)
    self.projects_locations_repositories_yumArtifacts = self.ProjectsLocationsRepositoriesYumArtifactsService(self)
    self.projects_locations_repositories = self.ProjectsLocationsRepositoriesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (ArtifactregistryProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesAptArtifactsService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories_aptArtifacts resource."""

    _NAME = 'projects_locations_repositories_aptArtifacts'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsRepositoriesAptArtifactsService, self).__init__(client)
      self._upload_configs = {
          'Upload': base_api.ApiUploadInfo(
              accept=['*/*'],
              max_size=None,
              resumable_multipart=None,
              resumable_path=None,
              simple_multipart=True,
              simple_path='/upload/v1alpha1/{+parent}/aptArtifacts:create',
          ),
          }

    def Import(self, request, global_params=None):
      r"""Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesAptArtifactsImportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Import')
      return self._RunMethod(
          config, request, global_params=global_params)

    Import.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/aptArtifacts:import',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.aptArtifacts.import',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}/aptArtifacts:import',
        request_field='googleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesAptArtifactsImportRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Upload(self, request, global_params=None, upload=None):
      r"""Directly uploads an Apt artifact. The returned Operation will complete once the resources are uploaded. Package, Version, and File resources are created based on the imported artifact. Imported artifacts that conflict with existing resources are ignored.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesAptArtifactsUploadRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        upload: (Upload, default: None) If present, upload
            this stream with the request.
      Returns:
        (GoogleDevtoolsArtifactregistryV1alpha1UploadAptArtifactMediaResponse) The response message.
      """
      config = self.GetMethodConfig('Upload')
      upload_config = self.GetUploadConfig('Upload')
      return self._RunMethod(
          config, request, global_params=global_params,
          upload=upload, upload_config=upload_config)

    Upload.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/aptArtifacts:create',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.aptArtifacts.upload',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}/aptArtifacts:create',
        request_field='googleDevtoolsArtifactregistryV1alpha1UploadAptArtifactRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesAptArtifactsUploadRequest',
        response_type_name='GoogleDevtoolsArtifactregistryV1alpha1UploadAptArtifactMediaResponse',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesGooGetArtifactsService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories_gooGetArtifacts resource."""

    _NAME = 'projects_locations_repositories_gooGetArtifacts'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsRepositoriesGooGetArtifactsService, self).__init__(client)
      self._upload_configs = {
          }

    def Import(self, request, global_params=None):
      r"""Imports GooGet artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesGooGetArtifactsImportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Import')
      return self._RunMethod(
          config, request, global_params=global_params)

    Import.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/gooGetArtifacts:import',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.gooGetArtifacts.import',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}/gooGetArtifacts:import',
        request_field='googleDevtoolsArtifactregistryV1alpha1ImportGooGetArtifactsRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesGooGetArtifactsImportRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesGoogetArtifactsService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories_googetArtifacts resource."""

    _NAME = 'projects_locations_repositories_googetArtifacts'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsRepositoriesGoogetArtifactsService, self).__init__(client)
      self._upload_configs = {
          'Upload': base_api.ApiUploadInfo(
              accept=['*/*'],
              max_size=None,
              resumable_multipart=None,
              resumable_path=None,
              simple_multipart=True,
              simple_path='/upload/v1alpha1/{+parent}/googetArtifacts:create',
          ),
          }

    def Upload(self, request, global_params=None, upload=None):
      r"""Directly uploads a GooGet artifact. The returned Operation will complete once the resources are uploaded. Package, Version, and File resources are created based on the imported artifact. Imported artifacts that conflict with existing resources are ignored.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesGoogetArtifactsUploadRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        upload: (Upload, default: None) If present, upload
            this stream with the request.
      Returns:
        (GoogleDevtoolsArtifactregistryV1alpha1UploadGooGetArtifactMediaResponse) The response message.
      """
      config = self.GetMethodConfig('Upload')
      upload_config = self.GetUploadConfig('Upload')
      return self._RunMethod(
          config, request, global_params=global_params,
          upload=upload, upload_config=upload_config)

    Upload.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/googetArtifacts:create',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.googetArtifacts.upload',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}/googetArtifacts:create',
        request_field='googleDevtoolsArtifactregistryV1alpha1UploadGooGetArtifactRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesGoogetArtifactsUploadRequest',
        response_type_name='GoogleDevtoolsArtifactregistryV1alpha1UploadGooGetArtifactMediaResponse',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesYumArtifactsService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories_yumArtifacts resource."""

    _NAME = 'projects_locations_repositories_yumArtifacts'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsRepositoriesYumArtifactsService, self).__init__(client)
      self._upload_configs = {
          'Upload': base_api.ApiUploadInfo(
              accept=['*/*'],
              max_size=None,
              resumable_multipart=None,
              resumable_path=None,
              simple_multipart=True,
              simple_path='/upload/v1alpha1/{+parent}/yumArtifacts:create',
          ),
          }

    def Import(self, request, global_params=None):
      r"""Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesYumArtifactsImportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Import')
      return self._RunMethod(
          config, request, global_params=global_params)

    Import.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/yumArtifacts:import',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.yumArtifacts.import',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}/yumArtifacts:import',
        request_field='googleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesYumArtifactsImportRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Upload(self, request, global_params=None, upload=None):
      r"""Directly uploads a Yum artifact. The returned Operation will complete once the resources are uploaded. Package, Version, and File resources are created based on the imported artifact. Imported artifacts that conflict with existing resources are ignored.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesYumArtifactsUploadRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        upload: (Upload, default: None) If present, upload
            this stream with the request.
      Returns:
        (GoogleDevtoolsArtifactregistryV1alpha1UploadYumArtifactMediaResponse) The response message.
      """
      config = self.GetMethodConfig('Upload')
      upload_config = self.GetUploadConfig('Upload')
      return self._RunMethod(
          config, request, global_params=global_params,
          upload=upload, upload_config=upload_config)

    Upload.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/yumArtifacts:create',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.yumArtifacts.upload',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}/yumArtifacts:create',
        request_field='googleDevtoolsArtifactregistryV1alpha1UploadYumArtifactRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesYumArtifactsUploadRequest',
        response_type_name='GoogleDevtoolsArtifactregistryV1alpha1UploadYumArtifactMediaResponse',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories resource."""

    _NAME = 'projects_locations_repositories'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsRepositoriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['repositoryId'],
        relative_path='v1alpha1/{+parent}/repositories',
        request_field='googleDevtoolsArtifactregistryV1alpha1Repository',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}',
        http_method='DELETE',
        method_id='artifactregistry.projects.locations.repositories.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a repository.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsArtifactregistryV1alpha1Repository) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesGetRequest',
        response_type_name='GoogleDevtoolsArtifactregistryV1alpha1Repository',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists repositories.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsArtifactregistryV1alpha1ListRepositoriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/repositories',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesListRequest',
        response_type_name='GoogleDevtoolsArtifactregistryV1alpha1ListRepositoriesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a repository.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsArtifactregistryV1alpha1Repository) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}',
        http_method='PATCH',
        method_id='artifactregistry.projects.locations.repositories.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='googleDevtoolsArtifactregistryV1alpha1Repository',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPatchRequest',
        response_type_name='GoogleDevtoolsArtifactregistryV1alpha1Repository',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (ArtifactregistryProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (ArtifactregistryProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='artifactregistry.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+name}/locations',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
