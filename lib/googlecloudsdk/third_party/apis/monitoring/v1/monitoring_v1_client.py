"""Generated client library for monitoring version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.monitoring.v1 import monitoring_v1_messages as messages


class MonitoringV1(base_api.BaseApiClient):
  """Generated client library for service monitoring version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://monitoring.googleapis.com/'
  MTLS_BASE_URL = 'https://monitoring.mtls.googleapis.com/'

  _PACKAGE = 'monitoring'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/monitoring', 'https://www.googleapis.com/auth/monitoring.read', 'https://www.googleapis.com/auth/monitoring.write']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'MonitoringV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new monitoring handle."""
    url = url or self.BASE_URL
    super(MonitoringV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.locations_global_metricsScopes_projects = self.LocationsGlobalMetricsScopesProjectsService(self)
    self.locations_global_metricsScopes = self.LocationsGlobalMetricsScopesService(self)
    self.locations_global = self.LocationsGlobalService(self)
    self.locations = self.LocationsService(self)
    self.operations = self.OperationsService(self)
    self.projects_dashboards = self.ProjectsDashboardsService(self)
    self.projects_location_prometheus_api_v1_label = self.ProjectsLocationPrometheusApiV1LabelService(self)
    self.projects_location_prometheus_api_v1_metadata = self.ProjectsLocationPrometheusApiV1MetadataService(self)
    self.projects_location_prometheus_api_v1 = self.ProjectsLocationPrometheusApiV1Service(self)
    self.projects_location_prometheus_api = self.ProjectsLocationPrometheusApiService(self)
    self.projects_location_prometheus = self.ProjectsLocationPrometheusService(self)
    self.projects_location = self.ProjectsLocationService(self)
    self.projects = self.ProjectsService(self)

  class LocationsGlobalMetricsScopesProjectsService(base_api.BaseApiService):
    """Service class for the locations_global_metricsScopes_projects resource."""

    _NAME = 'locations_global_metricsScopes_projects'

    def __init__(self, client):
      super(MonitoringV1.LocationsGlobalMetricsScopesProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Adds a MonitoredProject with the given project ID to the specified Metrics Scope.

      Args:
        request: (MonitoringLocationsGlobalMetricsScopesProjectsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/locations/global/metricsScopes/{metricsScopesId}/projects',
        http_method='POST',
        method_id='monitoring.locations.global.metricsScopes.projects.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/projects',
        request_field='monitoredProject',
        request_type_name='MonitoringLocationsGlobalMetricsScopesProjectsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a MonitoredProject from the specified Metrics Scope.

      Args:
        request: (MonitoringLocationsGlobalMetricsScopesProjectsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/locations/global/metricsScopes/{metricsScopesId}/projects/{projectsId}',
        http_method='DELETE',
        method_id='monitoring.locations.global.metricsScopes.projects.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MonitoringLocationsGlobalMetricsScopesProjectsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class LocationsGlobalMetricsScopesService(base_api.BaseApiService):
    """Service class for the locations_global_metricsScopes resource."""

    _NAME = 'locations_global_metricsScopes'

    def __init__(self, client):
      super(MonitoringV1.LocationsGlobalMetricsScopesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Returns a specific Metrics Scope, including the list of projects monitored by the specified Metrics Scope.

      Args:
        request: (MonitoringLocationsGlobalMetricsScopesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (MetricsScope) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/locations/global/metricsScopes/{metricsScopesId}',
        http_method='GET',
        method_id='monitoring.locations.global.metricsScopes.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MonitoringLocationsGlobalMetricsScopesGetRequest',
        response_type_name='MetricsScope',
        supports_download=False,
    )

    def ListMetricsScopesByMonitoredProject(self, request, global_params=None):
      r"""Returns a list of every Metrics Scope that a specific MonitoredProject has been added to. The metrics scope representing the specified monitored project will always be the first entry in the response.

      Args:
        request: (MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListMetricsScopesByMonitoredProjectResponse) The response message.
      """
      config = self.GetMethodConfig('ListMetricsScopesByMonitoredProject')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListMetricsScopesByMonitoredProject.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='monitoring.locations.global.metricsScopes.listMetricsScopesByMonitoredProject',
        ordered_params=[],
        path_params=[],
        query_params=['monitoredResourceContainer'],
        relative_path='v1/locations/global/metricsScopes:listMetricsScopesByMonitoredProject',
        request_field='',
        request_type_name='MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequest',
        response_type_name='ListMetricsScopesByMonitoredProjectResponse',
        supports_download=False,
    )

  class LocationsGlobalService(base_api.BaseApiService):
    """Service class for the locations_global resource."""

    _NAME = 'locations_global'

    def __init__(self, client):
      super(MonitoringV1.LocationsGlobalService, self).__init__(client)
      self._upload_configs = {
          }

  class LocationsService(base_api.BaseApiService):
    """Service class for the locations resource."""

    _NAME = 'locations'

    def __init__(self, client):
      super(MonitoringV1.LocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(MonitoringV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (MonitoringOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}',
        http_method='GET',
        method_id='monitoring.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MonitoringOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsDashboardsService(base_api.BaseApiService):
    """Service class for the projects_dashboards resource."""

    _NAME = 'projects_dashboards'

    def __init__(self, client):
      super(MonitoringV1.ProjectsDashboardsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see Managing dashboards by API (https://cloud.google.com/monitoring/dashboards/api-dashboard). This method requires the monitoring.dashboards.create permission on the specified project. For more information about permissions, see Cloud Identity and Access Management (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dashboard) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards',
        http_method='POST',
        method_id='monitoring.projects.dashboards.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['validateOnly'],
        relative_path='v1/{+parent}/dashboards',
        request_field='dashboard',
        request_type_name='MonitoringProjectsDashboardsCreateRequest',
        response_type_name='Dashboard',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an existing custom dashboard.This method requires the monitoring.dashboards.delete permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards/{dashboardsId}',
        http_method='DELETE',
        method_id='monitoring.projects.dashboards.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MonitoringProjectsDashboardsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Fetches a specific dashboard.This method requires the monitoring.dashboards.get permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dashboard) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards/{dashboardsId}',
        http_method='GET',
        method_id='monitoring.projects.dashboards.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MonitoringProjectsDashboardsGetRequest',
        response_type_name='Dashboard',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the existing dashboards.This method requires the monitoring.dashboards.list permission on the specified project. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDashboardsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards',
        http_method='GET',
        method_id='monitoring.projects.dashboards.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/dashboards',
        request_field='',
        request_type_name='MonitoringProjectsDashboardsListRequest',
        response_type_name='ListDashboardsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Replaces an existing custom dashboard with a new definition.This method requires the monitoring.dashboards.update permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dashboard) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards/{dashboardsId}',
        http_method='PATCH',
        method_id='monitoring.projects.dashboards.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['validateOnly'],
        relative_path='v1/{+name}',
        request_field='dashboard',
        request_type_name='MonitoringProjectsDashboardsPatchRequest',
        response_type_name='Dashboard',
        supports_download=False,
    )

  class ProjectsLocationPrometheusApiV1LabelService(base_api.BaseApiService):
    """Service class for the projects_location_prometheus_api_v1_label resource."""

    _NAME = 'projects_location_prometheus_api_v1_label'

    def __init__(self, client):
      super(MonitoringV1.ProjectsLocationPrometheusApiV1LabelService, self).__init__(client)
      self._upload_configs = {
          }

    def Values(self, request, global_params=None):
      r"""Lists possible values for a given label name.

      Args:
        request: (MonitoringProjectsLocationPrometheusApiV1LabelValuesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (HttpBody) The response message.
      """
      config = self.GetMethodConfig('Values')
      return self._RunMethod(
          config, request, global_params=global_params)

    Values.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/location/{location}/prometheus/api/v1/label/{label}/values',
        http_method='GET',
        method_id='monitoring.projects.location.prometheus.api.v1.label.values',
        ordered_params=['name', 'location', 'label'],
        path_params=['label', 'location', 'name'],
        query_params=['end', 'match', 'start'],
        relative_path='v1/{+name}/location/{location}/prometheus/api/v1/label/{label}/values',
        request_field='',
        request_type_name='MonitoringProjectsLocationPrometheusApiV1LabelValuesRequest',
        response_type_name='HttpBody',
        supports_download=False,
    )

  class ProjectsLocationPrometheusApiV1MetadataService(base_api.BaseApiService):
    """Service class for the projects_location_prometheus_api_v1_metadata resource."""

    _NAME = 'projects_location_prometheus_api_v1_metadata'

    def __init__(self, client):
      super(MonitoringV1.ProjectsLocationPrometheusApiV1MetadataService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists metadata for metrics.

      Args:
        request: (MonitoringProjectsLocationPrometheusApiV1MetadataListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (HttpBody) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/location/{location}/prometheus/api/v1/metadata',
        http_method='GET',
        method_id='monitoring.projects.location.prometheus.api.v1.metadata.list',
        ordered_params=['name', 'location'],
        path_params=['location', 'name'],
        query_params=['limit', 'metric'],
        relative_path='v1/{+name}/location/{location}/prometheus/api/v1/metadata',
        request_field='',
        request_type_name='MonitoringProjectsLocationPrometheusApiV1MetadataListRequest',
        response_type_name='HttpBody',
        supports_download=False,
    )

  class ProjectsLocationPrometheusApiV1Service(base_api.BaseApiService):
    """Service class for the projects_location_prometheus_api_v1 resource."""

    _NAME = 'projects_location_prometheus_api_v1'

    def __init__(self, client):
      super(MonitoringV1.ProjectsLocationPrometheusApiV1Service, self).__init__(client)
      self._upload_configs = {
          }

    def Query(self, request, global_params=None):
      r"""Evaluate a PromQL query at a single point in time.

      Args:
        request: (MonitoringProjectsLocationPrometheusApiV1QueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (HttpBody) The response message.
      """
      config = self.GetMethodConfig('Query')
      return self._RunMethod(
          config, request, global_params=global_params)

    Query.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/location/{location}/prometheus/api/v1/query',
        http_method='POST',
        method_id='monitoring.projects.location.prometheus.api.v1.query',
        ordered_params=['name', 'location'],
        path_params=['location', 'name'],
        query_params=[],
        relative_path='v1/{+name}/location/{location}/prometheus/api/v1/query',
        request_field='queryInstantRequest',
        request_type_name='MonitoringProjectsLocationPrometheusApiV1QueryRequest',
        response_type_name='HttpBody',
        supports_download=False,
    )

    def QueryRange(self, request, global_params=None):
      r"""Evaluate a PromQL query with start, end time range.

      Args:
        request: (MonitoringProjectsLocationPrometheusApiV1QueryRangeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (HttpBody) The response message.
      """
      config = self.GetMethodConfig('QueryRange')
      return self._RunMethod(
          config, request, global_params=global_params)

    QueryRange.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/location/{location}/prometheus/api/v1/query_range',
        http_method='POST',
        method_id='monitoring.projects.location.prometheus.api.v1.query_range',
        ordered_params=['name', 'location'],
        path_params=['location', 'name'],
        query_params=[],
        relative_path='v1/{+name}/location/{location}/prometheus/api/v1/query_range',
        request_field='queryRangeRequest',
        request_type_name='MonitoringProjectsLocationPrometheusApiV1QueryRangeRequest',
        response_type_name='HttpBody',
        supports_download=False,
    )

    def Series(self, request, global_params=None):
      r"""Lists metadata for metrics.

      Args:
        request: (MonitoringProjectsLocationPrometheusApiV1SeriesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (HttpBody) The response message.
      """
      config = self.GetMethodConfig('Series')
      return self._RunMethod(
          config, request, global_params=global_params)

    Series.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/location/{location}/prometheus/api/v1/series',
        http_method='POST',
        method_id='monitoring.projects.location.prometheus.api.v1.series',
        ordered_params=['name', 'location'],
        path_params=['location', 'name'],
        query_params=[],
        relative_path='v1/{+name}/location/{location}/prometheus/api/v1/series',
        request_field='querySeriesRequest',
        request_type_name='MonitoringProjectsLocationPrometheusApiV1SeriesRequest',
        response_type_name='HttpBody',
        supports_download=False,
    )

  class ProjectsLocationPrometheusApiService(base_api.BaseApiService):
    """Service class for the projects_location_prometheus_api resource."""

    _NAME = 'projects_location_prometheus_api'

    def __init__(self, client):
      super(MonitoringV1.ProjectsLocationPrometheusApiService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationPrometheusService(base_api.BaseApiService):
    """Service class for the projects_location_prometheus resource."""

    _NAME = 'projects_location_prometheus'

    def __init__(self, client):
      super(MonitoringV1.ProjectsLocationPrometheusService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationService(base_api.BaseApiService):
    """Service class for the projects_location resource."""

    _NAME = 'projects_location'

    def __init__(self, client):
      super(MonitoringV1.ProjectsLocationService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(MonitoringV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
