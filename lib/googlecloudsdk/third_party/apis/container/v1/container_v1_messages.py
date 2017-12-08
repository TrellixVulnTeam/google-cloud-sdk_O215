"""Generated message classes for container version v1.

Builds and manages clusters that run container-based applications, powered by
open source Kubernetes technology.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudsdk.third_party.apitools.base.protorpclite import messages as _messages
from googlecloudsdk.third_party.apitools.base.py import encoding


package = 'container'


class AddonsConfig(_messages.Message):
  """Configuration for the addons that can be automatically spun up in the
  cluster, enabling additional functionality.

  Fields:
    horizontalPodAutoscaling: Configuration for the horizontal pod autoscaling
      feature, which increases or decreases the number of replica pods a
      replication controller has based on the resource usage of the existing
      pods.
    httpLoadBalancing: Configuration for the HTTP (L7) load balancing
      controller addon, which makes it easy to set up HTTP load balancers for
      services in a cluster.
  """

  horizontalPodAutoscaling = _messages.MessageField('HorizontalPodAutoscaling', 1)
  httpLoadBalancing = _messages.MessageField('HttpLoadBalancing', 2)


class Cluster(_messages.Message):
  """A Google Container Engine cluster.

  Enums:
    StatusValueValuesEnum: [Output only] The current status of this cluster.

  Fields:
    addonsConfig: Configurations for the various addons available to run in
      the cluster.
    clusterIpv4Cidr: The IP address range of the container pods in this
      cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-
      Domain_Routing) notation (e.g. `10.96.0.0/14`). Leave blank to have one
      automatically chosen or specify a `/14` block in `10.0.0.0/8`.
    createTime: [Output only] The time the cluster was created, in
      [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.
    currentMasterVersion: [Output only] The current software version of the
      master endpoint.
    currentNodeCount: [Output only] The number of nodes currently in the
      cluster.
    currentNodeVersion: [Output only] The current version of the node software
      components. If they are currently at multiple versions because they're
      in the process of being upgraded, this reflects the minimum version of
      all nodes.
    description: An optional description of this cluster.
    endpoint: [Output only] The IP address of this cluster's master endpoint.
      The endpoint can be accessed from the internet at
      `https://username:password@endpoint/`.  See the `masterAuth` property of
      this resource for username and password information.
    initialClusterVersion: [Output only] The software version of the master
      endpoint and kubelets used in the cluster when it was first created. The
      version can be upgraded over time.
    initialNodeCount: The number of nodes to create in this cluster. You must
      ensure that your Compute Engine <a href="/compute/docs/resource-
      quotas">resource quota</a> is sufficient for this number of instances.
      You must also have available firewall and routes quota. For requests,
      this field should only be used in lieu of a "node_pool" object, since
      this configuration (along with the "node_config") will be used to create
      a "NodePool" object with an auto-generated name. Do not use this and a
      node_pool at the same time.
    instanceGroupUrls: [Output only] The resource URLs of [instance
      groups](/compute/docs/instance-groups/) associated with this cluster.
    loggingService: The logging service the cluster should use to write logs.
      Currently available options:  * `logging.googleapis.com` - the Google
      Cloud Logging service. * `none` - no logs will be exported from the
      cluster. * if left as an empty string,`logging.googleapis.com` will be
      used.
    masterAuth: The authentication information for accessing the master
      endpoint.
    monitoringService: The monitoring service the cluster should use to write
      metrics. Currently available options:  * `monitoring.googleapis.com` -
      the Google Cloud Monitoring service. * `none` - no metrics will be
      exported from the cluster. * if left as an empty string,
      `monitoring.googleapis.com` will be used.
    name: The name of this cluster. The name must be unique within this
      project and zone, and can be up to 40 characters with the following
      restrictions:  * Lowercase letters, numbers, and hyphens only. * Must
      start with a letter. * Must end with a number or a letter.
    network: The name of the Google Compute Engine [network](/compute/docs
      /networks-and-firewalls#networks) to which the cluster is connected. If
      left unspecified, the `default` network will be used.
    nodeConfig: Parameters used in creating the cluster's nodes. See
      `nodeConfig` for the description of its properties. For requests, this
      field should only be used in lieu of a "node_pool" object, since this
      configuration (along with the "initial_node_count") will be used to
      create a "NodePool" object with an auto-generated name. Do not use this
      and a node_pool at the same time. For responses, this field will be
      populated with the node configuration of the first node pool.  If
      unspecified, the defaults are used.
    nodeIpv4CidrSize: [Output only] The size of the address space on each node
      for hosting containers. This is provisioned from within the
      `container_ipv4_cidr` range.
    nodePools: The node pools associated with this cluster. When creating a
      new cluster, only a single node pool should be specified. This field
      should not be set if "node_config" and "initial_node_count" are
      specified.
    selfLink: [Output only] Server-defined URL for the resource.
    servicesIpv4Cidr: [Output only] The IP address range of the Kubernetes
      services in this cluster, in [CIDR](http://en.wikipedia.org/wiki
      /Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). Service
      addresses are typically put in the last `/16` from the container CIDR.
    status: [Output only] The current status of this cluster.
    statusMessage: [Output only] Additional information about the current
      status of this cluster, if available.
    subnetwork: The name of the Google Compute Engine
      [subnetwork](/compute/docs/subnetworks) to which the cluster is
      connected.  Specification of subnetworks is an alpha feature, and
      require that the Google Compute Engine alpha API be enabled.
    zone: [Output only] The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """[Output only] The current status of this cluster.

    Values:
      STATUS_UNSPECIFIED: Not set.
      PROVISIONING: The PROVISIONING state indicates the cluster is being
        created.
      RUNNING: The RUNNING state indicates the cluster has been created and is
        fully usable.
      RECONCILING: The RECONCILING state indicates that some work is actively
        being done on the cluster, such as upgrading the master or node
        software. Details can be found in the `statusMessage` field.
      STOPPING: The STOPPING state indicates the cluster is being deleted.
      ERROR: The ERROR state indicates the cluster may be unusable. Details
        can be found in the `statusMessage` field.
    """
    STATUS_UNSPECIFIED = 0
    PROVISIONING = 1
    RUNNING = 2
    RECONCILING = 3
    STOPPING = 4
    ERROR = 5

  addonsConfig = _messages.MessageField('AddonsConfig', 1)
  clusterIpv4Cidr = _messages.StringField(2)
  createTime = _messages.StringField(3)
  currentMasterVersion = _messages.StringField(4)
  currentNodeCount = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  currentNodeVersion = _messages.StringField(6)
  description = _messages.StringField(7)
  endpoint = _messages.StringField(8)
  initialClusterVersion = _messages.StringField(9)
  initialNodeCount = _messages.IntegerField(10, variant=_messages.Variant.INT32)
  instanceGroupUrls = _messages.StringField(11, repeated=True)
  loggingService = _messages.StringField(12)
  masterAuth = _messages.MessageField('MasterAuth', 13)
  monitoringService = _messages.StringField(14)
  name = _messages.StringField(15)
  network = _messages.StringField(16)
  nodeConfig = _messages.MessageField('NodeConfig', 17)
  nodeIpv4CidrSize = _messages.IntegerField(18, variant=_messages.Variant.INT32)
  nodePools = _messages.MessageField('NodePool', 19, repeated=True)
  selfLink = _messages.StringField(20)
  servicesIpv4Cidr = _messages.StringField(21)
  status = _messages.EnumField('StatusValueValuesEnum', 22)
  statusMessage = _messages.StringField(23)
  subnetwork = _messages.StringField(24)
  zone = _messages.StringField(25)


class ClusterUpdate(_messages.Message):
  """ClusterUpdate describes an update to the cluster. Exactly one update can
  be applied to a cluster with each request, so at most one field can be
  provided.

  Fields:
    desiredAddonsConfig: Configurations for the various addons available to
      run in the cluster.
    desiredMasterMachineType: The name of a Google Compute Engine [machine
      type](/compute/docs/machine-types) (e.g. `n1-standard-8`) to change the
      master to.
    desiredMasterVersion:  Whitelisted and internal users can change the
      master to any version.  The Kubernetes version to change the master to.
      The only valid value is the latest supported version. Use "-" to have
      the server automatically select the latest version.
    desiredMonitoringService: The monitoring service the cluster should use to
      write metrics. Currently available options:  *
      "monitoring.googleapis.com" - the Google Cloud Monitoring service *
      "none" - no metrics will be exported from the cluster
    desiredNodePoolId: The node pool to be upgraded. This field is mandatory
      if the "desired_node_version" is specified and there is more than one
      node pool on the cluster.
    desiredNodeVersion: The Kubernetes version to change the nodes to
      (typically an upgrade). Use `-` to upgrade to the latest version
      supported by the server.
  """

  desiredAddonsConfig = _messages.MessageField('AddonsConfig', 1)
  desiredMasterMachineType = _messages.StringField(2)
  desiredMasterVersion = _messages.StringField(3)
  desiredMonitoringService = _messages.StringField(4)
  desiredNodePoolId = _messages.StringField(5)
  desiredNodeVersion = _messages.StringField(6)


class ContainerMasterProjectsZonesSignedUrlsCreateRequest(_messages.Message):
  """A ContainerMasterProjectsZonesSignedUrlsCreateRequest object.

  Fields:
    createSignedUrlsRequest: A CreateSignedUrlsRequest resource to be passed
      as the request body.
    masterProjectId: The hosted master project in which this master resides.
      This can be either a [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The zone of this master's cluster.
  """

  createSignedUrlsRequest = _messages.MessageField('CreateSignedUrlsRequest', 1)
  masterProjectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerMasterProjectsZonesTokensCreateRequest(_messages.Message):
  """A ContainerMasterProjectsZonesTokensCreateRequest object.

  Fields:
    createTokenRequest: A CreateTokenRequest resource to be passed as the
      request body.
    masterProjectId: The hosted master project in which this master resides.
      This can be either a [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The zone of this master's cluster.
  """

  createTokenRequest = _messages.MessageField('CreateTokenRequest', 1)
  masterProjectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesClustersCreateRequest(_messages.Message):
  """A ContainerProjectsZonesClustersCreateRequest object.

  Fields:
    createClusterRequest: A CreateClusterRequest resource to be passed as the
      request body.
    projectId: The Google Developers Console [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  createClusterRequest = _messages.MessageField('CreateClusterRequest', 1)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesClustersDeleteRequest(_messages.Message):
  """A ContainerProjectsZonesClustersDeleteRequest object.

  Fields:
    clusterId: The name of the cluster to delete.
    projectId: The Google Developers Console [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  clusterId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesClustersGetRequest(_messages.Message):
  """A ContainerProjectsZonesClustersGetRequest object.

  Fields:
    clusterId: The name of the cluster to retrieve.
    projectId: The Google Developers Console [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  clusterId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesClustersListRequest(_messages.Message):
  """A ContainerProjectsZonesClustersListRequest object.

  Fields:
    projectId: The Google Developers Console [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides, or
      "-" for all zones.
  """

  projectId = _messages.StringField(1, required=True)
  zone = _messages.StringField(2, required=True)


class ContainerProjectsZonesClustersNodePoolsCreateRequest(_messages.Message):
  """A ContainerProjectsZonesClustersNodePoolsCreateRequest object.

  Fields:
    clusterId: The name of the cluster.
    createNodePoolRequest: A CreateNodePoolRequest resource to be passed as
      the request body.
    projectId: The Google Developers Console [project ID or project
      number](https://developers.google.com/console/help/new/#projectnumber).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  clusterId = _messages.StringField(1, required=True)
  createNodePoolRequest = _messages.MessageField('CreateNodePoolRequest', 2)
  projectId = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ContainerProjectsZonesClustersNodePoolsDeleteRequest(_messages.Message):
  """A ContainerProjectsZonesClustersNodePoolsDeleteRequest object.

  Fields:
    clusterId: The name of the cluster.
    nodePoolId: The name of the node pool to delete.
    projectId: The Google Developers Console [project ID or project
      number](https://developers.google.com/console/help/new/#projectnumber).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  clusterId = _messages.StringField(1, required=True)
  nodePoolId = _messages.StringField(2, required=True)
  projectId = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ContainerProjectsZonesClustersNodePoolsGetRequest(_messages.Message):
  """A ContainerProjectsZonesClustersNodePoolsGetRequest object.

  Fields:
    clusterId: The name of the cluster.
    nodePoolId: The name of the node pool.
    projectId: The Google Developers Console [project ID or project
      number](https://developers.google.com/console/help/new/#projectnumber).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  clusterId = _messages.StringField(1, required=True)
  nodePoolId = _messages.StringField(2, required=True)
  projectId = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ContainerProjectsZonesClustersNodePoolsListRequest(_messages.Message):
  """A ContainerProjectsZonesClustersNodePoolsListRequest object.

  Fields:
    clusterId: The name of the cluster.
    projectId: The Google Developers Console [project ID or project
      number](https://developers.google.com/console/help/new/#projectnumber).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  clusterId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesClustersUpdateRequest(_messages.Message):
  """A ContainerProjectsZonesClustersUpdateRequest object.

  Fields:
    clusterId: The name of the cluster to upgrade.
    projectId: The Google Developers Console [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    updateClusterRequest: A UpdateClusterRequest resource to be passed as the
      request body.
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  clusterId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  updateClusterRequest = _messages.MessageField('UpdateClusterRequest', 3)
  zone = _messages.StringField(4, required=True)


class ContainerProjectsZonesGetServerconfigRequest(_messages.Message):
  """A ContainerProjectsZonesGetServerconfigRequest object.

  Fields:
    projectId: The Google Developers Console [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) to return operations for.
  """

  projectId = _messages.StringField(1, required=True)
  zone = _messages.StringField(2, required=True)


class ContainerProjectsZonesOperationsGetRequest(_messages.Message):
  """A ContainerProjectsZonesOperationsGetRequest object.

  Fields:
    operationId: The server-assigned `name` of the operation.
    projectId: The Google Developers Console [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the cluster resides.
  """

  operationId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesOperationsListRequest(_messages.Message):
  """A ContainerProjectsZonesOperationsListRequest object.

  Fields:
    projectId: The Google Developers Console [project ID or project
      number](https://support.google.com/cloud/answer/6158840).
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) to return operations for, or `-`
      for all zones.
  """

  projectId = _messages.StringField(1, required=True)
  zone = _messages.StringField(2, required=True)


class CreateClusterRequest(_messages.Message):
  """CreateClusterRequest creates a cluster.

  Fields:
    cluster: A [cluster resource](/container-
      engine/reference/rest/v1/projects.zones.clusters)
  """

  cluster = _messages.MessageField('Cluster', 1)


class CreateNodePoolRequest(_messages.Message):
  """CreateNodePoolRequest creates a node pool for a cluster.

  Fields:
    initialNodeCount: The number of nodes to create in this pool. You must
      ensure that your Compute Engine <a href="/compute/docs/resource-
      quotas">resource quota</a> is sufficient for this number of instances.
      You must also have available firewall and routes quota.
    nodePool: The node pool to create.
  """

  initialNodeCount = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  nodePool = _messages.MessageField('NodePool', 2)


class CreateSignedUrlsRequest(_messages.Message):
  """A request for signed URLs that allow for writing a file to a private GCS
  bucket for storing backups of hosted master data.

  Fields:
    clusterId: The name of this master's cluster.
    filenames: The names of the files for which a signed URLs are being
      requested.
    projectNumber: The project number for which the signed URLs are being
      requested.  This is the project in which this master's cluster resides.
      Note that this must be a project number, not a project ID.
  """

  clusterId = _messages.StringField(1)
  filenames = _messages.StringField(2, repeated=True)
  projectNumber = _messages.IntegerField(3)


class CreateTokenRequest(_messages.Message):
  """A request for a compute-read-write
  (https://www.googleapis.com/auth/compute) scoped OAuth2 access token for
  <project_number>, to allow hosted masters to make modifications to a user's
  project.

  Fields:
    clusterId: The name of this master's cluster.
    projectNumber: The project number for which the access is being requested.
      This is the project in which this master's cluster resides.  Note that
      this must be a project number, not a project ID.
  """

  clusterId = _messages.StringField(1)
  projectNumber = _messages.IntegerField(2)


class HorizontalPodAutoscaling(_messages.Message):
  """Configuration options for the horizontal pod autoscaling feature, which
  increases or decreases the number of replica pods a replication controller
  has based on the resource usage of the existing pods.

  Fields:
    disabled: Whether the Horizontal Pod Autoscaling feature is enabled in the
      cluster. When enabled, it ensures that a Heapster pod is running in the
      cluster, which is also used by the Cloud Monitoring service.
  """

  disabled = _messages.BooleanField(1)


class HttpLoadBalancing(_messages.Message):
  """Configuration options for the HTTP (L7) load balancing controller addon,
  which makes it easy to set up HTTP load balancers for services in a cluster.

  Fields:
    disabled: Whether the HTTP Load Balancing controller is enabled in the
      cluster. When enabled, it runs a small pod in the cluster that manages
      the load balancers.
  """

  disabled = _messages.BooleanField(1)


class ListClustersResponse(_messages.Message):
  """ListClustersResponse is the result of ListClustersRequest.

  Fields:
    clusters: A list of clusters in the project in the specified zone, or
      across all ones.
    missingZones: If any zones are listed here, the list of clusters returned
      may be missing those zones.
  """

  clusters = _messages.MessageField('Cluster', 1, repeated=True)
  missingZones = _messages.StringField(2, repeated=True)


class ListNodePoolsResponse(_messages.Message):
  """ListNodePoolsResponse is the result of ListNodePoolsRequest.

  Fields:
    nodePools: A list of node pools for a cluster.
  """

  nodePools = _messages.MessageField('NodePool', 1, repeated=True)


class ListOperationsResponse(_messages.Message):
  """ListOperationsResponse is the result of ListOperationsRequest.

  Fields:
    missingZones: If any zones are listed here, the list of operations
      returned may be missing the operations from those zones.
    operations: A list of operations in the project in the specified zone.
  """

  missingZones = _messages.StringField(1, repeated=True)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class MasterAuth(_messages.Message):
  """The authentication information for accessing the master endpoint.
  Authentication can be done using HTTP basic auth or using client
  certificates.

  Fields:
    clientCertificate: [Output only] Base64-encoded public certificate used by
      clients to authenticate to the cluster endpoint.
    clientKey: [Output only] Base64-encoded private key used by clients to
      authenticate to the cluster endpoint.
    clusterCaCertificate: [Output only] Base64-encoded public certificate that
      is the root of trust for the cluster.
    password: The password to use for HTTP basic authentication to the master
      endpoint. Because the master endpoint is open to the Internet, you
      should create a strong password.
    username: The username to use for HTTP basic authentication to the master
      endpoint.
  """

  clientCertificate = _messages.StringField(1)
  clientKey = _messages.StringField(2)
  clusterCaCertificate = _messages.StringField(3)
  password = _messages.StringField(4)
  username = _messages.StringField(5)


class NodeConfig(_messages.Message):
  """Parameters that describe the nodes in a cluster.

  Messages:
    LabelsValue: The map of Kubernetes labels (key/value pairs) to be applied
      to each node. These will added in addition to any default label(s) that
      Kubernetes may apply to the node. In case of conflict in label keys, the
      applied set may differ depending on the Kubernetes version -- it's best
      to assume the behavior is undefined and conflicts should be avoided. For
      more information, including usage and the valid values, see:
      http://kubernetes.io/v1.1/docs/user-guide/labels.html
    MetadataValue: The metadata key/value pairs assigned to instances in the
      cluster.  Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less
      than 128 bytes in length. These are reflected as part of a URL in the
      metadata server. Additionally, to avoid ambiguity, keys must not
      conflict with any other metadata keys for the project or be one of the
      four reserved keys: "instance-template", "kube-env", "startup-script",
      and "user-data"  Values are free-form strings, and only have meaning as
      interpreted by the image running in the instance. The only restriction
      placed on them is that each value's size must be less than or equal to
      32 KB.  The total size of all keys and values must be less than 512 KB.

  Fields:
    diskSizeGb: Size of the disk attached to each node, specified in GB. The
      smallest allowed disk size is 10GB.  If unspecified, the default disk
      size is 100GB.
    image: The image track to use for this node. Note that for a given image
      track, the latest version of it will be used. TODO(user): This will
      NOT be exposed to the user in the first iteration, since we're still
      working through what an "image track" means and what we'll support.
      Discussion on the possibility of supporting different versions will be
      done then as well.
    labels: The map of Kubernetes labels (key/value pairs) to be applied to
      each node. These will added in addition to any default label(s) that
      Kubernetes may apply to the node. In case of conflict in label keys, the
      applied set may differ depending on the Kubernetes version -- it's best
      to assume the behavior is undefined and conflicts should be avoided. For
      more information, including usage and the valid values, see:
      http://kubernetes.io/v1.1/docs/user-guide/labels.html
    machineType: The name of a Google Compute Engine [machine
      type](/compute/docs/machine-types) (e.g. `n1-standard-1`).  If
      unspecified, the default machine type is `n1-standard-1`.
    metadata: The metadata key/value pairs assigned to instances in the
      cluster.  Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less
      than 128 bytes in length. These are reflected as part of a URL in the
      metadata server. Additionally, to avoid ambiguity, keys must not
      conflict with any other metadata keys for the project or be one of the
      four reserved keys: "instance-template", "kube-env", "startup-script",
      and "user-data"  Values are free-form strings, and only have meaning as
      interpreted by the image running in the instance. The only restriction
      placed on them is that each value's size must be less than or equal to
      32 KB.  The total size of all keys and values must be less than 512 KB.
    oauthScopes: The set of Google API scopes to be made available on all of
      the node VMs under the "default" service account.  The following scopes
      are recommended, but not required, and by default are not included:  *
      `https://www.googleapis.com/auth/compute` is required for mounting
      persistent storage on your nodes. *
      `https://www.googleapis.com/auth/devstorage.read_only` is required for
      communicating with **gcr.io** (the [Google Container Registry
      ](/container-registry/)).  If unspecified, no scopes are added, unless
      Cloud Logging or Cloud Monitoring are enabled, in which case their
      required scopes will be added.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """The map of Kubernetes labels (key/value pairs) to be applied to each
    node. These will added in addition to any default label(s) that Kubernetes
    may apply to the node. In case of conflict in label keys, the applied set
    may differ depending on the Kubernetes version -- it's best to assume the
    behavior is undefined and conflicts should be avoided. For more
    information, including usage and the valid values, see:
    http://kubernetes.io/v1.1/docs/user-guide/labels.html

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """The metadata key/value pairs assigned to instances in the cluster.
    Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes
    in length. These are reflected as part of a URL in the metadata server.
    Additionally, to avoid ambiguity, keys must not conflict with any other
    metadata keys for the project or be one of the four reserved keys:
    "instance-template", "kube-env", "startup-script", and "user-data"  Values
    are free-form strings, and only have meaning as interpreted by the image
    running in the instance. The only restriction placed on them is that each
    value's size must be less than or equal to 32 KB.  The total size of all
    keys and values must be less than 512 KB.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Additional properties of type MetadataValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  diskSizeGb = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  image = _messages.StringField(2)
  labels = _messages.MessageField('LabelsValue', 3)
  machineType = _messages.StringField(4)
  metadata = _messages.MessageField('MetadataValue', 5)
  oauthScopes = _messages.StringField(6, repeated=True)


class NodePool(_messages.Message):
  """NodePool contains the name and configuration for a cluster's node pool.
  Node pools are a set of nodes (i.e. VM's), with a common configuration and
  specification, under the control of the cluster master. They may have a set
  of Kubernetes labels applied to them, which may be used to reference them
  during pod scheduling. They may also be resized up or down, to accommodate
  the workload.

  Fields:
    config: The node configuration of the pool.
    initialNodeCount: The initial node count for the pool.
    instanceGroupUrl: [Output only] The resource URLs of [instance
      groups](/compute/docs/instance-groups/) associated with this node pool.
    name: The name of the node pool.
    selfLink: Server-defined URL for the resource.
    version: The version of the Kubernetes of this node.
  """

  config = _messages.MessageField('NodeConfig', 1)
  initialNodeCount = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  instanceGroupUrl = _messages.StringField(3)
  name = _messages.StringField(4)
  selfLink = _messages.StringField(5)
  version = _messages.StringField(6)


class Operation(_messages.Message):
  """This operation resource represents operations that may have happened or
  are happening on the cluster. All fields are output only.

  Enums:
    OperationTypeValueValuesEnum: The operation type.
    StatusValueValuesEnum: The current status of the operation.

  Fields:
    detail: Detailed operation progress, if available.
    name: The server-assigned ID for the operation.
    operationType: The operation type.
    selfLink: Server-defined URL for the resource.
    status: The current status of the operation.
    statusMessage: If an error has occurred, a textual description of the
      error.
    targetLink: Server-defined URL for the target of the operation.
    zone: The name of the Google Compute Engine
      [zone](/compute/docs/zones#available) in which the operation is taking
      place.
  """

  class OperationTypeValueValuesEnum(_messages.Enum):
    """The operation type.

    Values:
      TYPE_UNSPECIFIED: Not set.
      CREATE_CLUSTER: Cluster create.
      DELETE_CLUSTER: Cluster delete.
      UPGRADE_MASTER: A master upgrade.
      UPGRADE_NODES: A node upgrade.
      REPAIR_CLUSTER: Cluster repair.
      UPDATE_CLUSTER: Cluster update.
      CREATE_NODE_POOL: Node pool create.
      DELETE_NODE_POOL: Node pool delete.
    """
    TYPE_UNSPECIFIED = 0
    CREATE_CLUSTER = 1
    DELETE_CLUSTER = 2
    UPGRADE_MASTER = 3
    UPGRADE_NODES = 4
    REPAIR_CLUSTER = 5
    UPDATE_CLUSTER = 6
    CREATE_NODE_POOL = 7
    DELETE_NODE_POOL = 8

  class StatusValueValuesEnum(_messages.Enum):
    """The current status of the operation.

    Values:
      STATUS_UNSPECIFIED: Not set.
      PENDING: The operation has been created.
      RUNNING: The operation is currently running.
      DONE: The operation is done, either cancelled or completed.
    """
    STATUS_UNSPECIFIED = 0
    PENDING = 1
    RUNNING = 2
    DONE = 3

  detail = _messages.StringField(1)
  name = _messages.StringField(2)
  operationType = _messages.EnumField('OperationTypeValueValuesEnum', 3)
  selfLink = _messages.StringField(4)
  status = _messages.EnumField('StatusValueValuesEnum', 5)
  statusMessage = _messages.StringField(6)
  targetLink = _messages.StringField(7)
  zone = _messages.StringField(8)


class ServerConfig(_messages.Message):
  """Container Engine service configuration.

  Fields:
    buildClientInfo: apiserver build BuildData::ClientInfo()
    defaultClusterVersion: Version of Kubernetes the service deploys by
      default.
    validNodeVersions: List of valid node upgrade target versions.
  """

  buildClientInfo = _messages.StringField(1)
  defaultClusterVersion = _messages.StringField(2)
  validNodeVersions = _messages.StringField(3, repeated=True)


class SignedUrls(_messages.Message):
  """Signed URLs that allow for writing a file to a private GCS bucket for
  storing backups of hosted master data.

  Fields:
    signedUrls: The signed URLs for writing the request files, in the same
      order as the filenames in the request.
  """

  signedUrls = _messages.StringField(1, repeated=True)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class Token(_messages.Message):
  """A compute-read-write (https://www.googleapis.com/auth/compute) scoped
  OAuth2 access token, to allow hosted masters to make modifications to a
  user's project.

  Fields:
    accessToken: The OAuth2 access token
    expireTime: The expiration time of the token.
  """

  accessToken = _messages.StringField(1)
  expireTime = _messages.StringField(2)


class UpdateClusterRequest(_messages.Message):
  """UpdateClusterRequest updates the settings of a cluster.

  Fields:
    update: A description of the update.
  """

  update = _messages.MessageField('ClusterUpdate', 1)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'container')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'container')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'container')
