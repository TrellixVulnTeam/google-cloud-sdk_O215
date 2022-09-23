"""Generated message classes for assuredworkloads version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'assuredworkloads'


class AssuredworkloadsOrganizationsLocationsOperationsGetRequest(_messages.Message):
  r"""A AssuredworkloadsOrganizationsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class AssuredworkloadsOrganizationsLocationsOperationsListRequest(_messages.Message):
  r"""A AssuredworkloadsOrganizationsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class AssuredworkloadsOrganizationsLocationsWorkloadsCreateRequest(_messages.Message):
  r"""A AssuredworkloadsOrganizationsLocationsWorkloadsCreateRequest object.

  Fields:
    externalId: Optional. A identifier associated with the workload and
      underlying projects which allows for the break down of billing costs for
      a workload. The value provided for the identifier will add a label to
      the workload and contained projects with the identifier as the value.
    googleCloudAssuredworkloadsV1Workload: A
      GoogleCloudAssuredworkloadsV1Workload resource to be passed as the
      request body.
    parent: Required. The resource name of the new Workload's parent. Must be
      of the form `organizations/{org_id}/locations/{location_id}`.
  """

  externalId = _messages.StringField(1)
  googleCloudAssuredworkloadsV1Workload = _messages.MessageField('GoogleCloudAssuredworkloadsV1Workload', 2)
  parent = _messages.StringField(3, required=True)


class AssuredworkloadsOrganizationsLocationsWorkloadsDeleteRequest(_messages.Message):
  r"""A AssuredworkloadsOrganizationsLocationsWorkloadsDeleteRequest object.

  Fields:
    etag: Optional. The etag of the workload. If this is provided, it must
      match the server's etag.
    name: Required. The `name` field is used to identify the workload. Format:
      organizations/{org_id}/locations/{location_id}/workloads/{workload_id}
  """

  etag = _messages.StringField(1)
  name = _messages.StringField(2, required=True)


class AssuredworkloadsOrganizationsLocationsWorkloadsGetRequest(_messages.Message):
  r"""A AssuredworkloadsOrganizationsLocationsWorkloadsGetRequest object.

  Fields:
    name: Required. The resource name of the Workload to fetch. This is the
      workloads's relative path in the API, formatted as "organizations/{organ
      ization_id}/locations/{location_id}/workloads/{workload_id}". For
      example, "organizations/123/locations/us-east1/workloads/assured-
      workload-1".
  """

  name = _messages.StringField(1, required=True)


class AssuredworkloadsOrganizationsLocationsWorkloadsListRequest(_messages.Message):
  r"""A AssuredworkloadsOrganizationsLocationsWorkloadsListRequest object.

  Fields:
    filter: A custom filter for filtering by properties of a workload. At this
      time, only filtering by labels is supported.
    pageSize: Page size.
    pageToken: Page token returned from previous request. Page token contains
      context from previous request. Page token needs to be passed in the
      second and following requests.
    parent: Required. Parent Resource to list workloads from. Must be of the
      form `organizations/{org_id}/locations/{location}`.
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  parent = _messages.StringField(4, required=True)


class AssuredworkloadsOrganizationsLocationsWorkloadsPatchRequest(_messages.Message):
  r"""A AssuredworkloadsOrganizationsLocationsWorkloadsPatchRequest object.

  Fields:
    googleCloudAssuredworkloadsV1Workload: A
      GoogleCloudAssuredworkloadsV1Workload resource to be passed as the
      request body.
    name: Optional. The resource name of the workload. Format:
      organizations/{organization}/locations/{location}/workloads/{workload}
      Read-only.
    updateMask: Required. The list of fields to be updated.
  """

  googleCloudAssuredworkloadsV1Workload = _messages.MessageField('GoogleCloudAssuredworkloadsV1Workload', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class AssuredworkloadsOrganizationsLocationsWorkloadsRestrictAllowedResourcesRequest(_messages.Message):
  r"""A AssuredworkloadsOrganizationsLocationsWorkloadsRestrictAllowedResource
  sRequest object.

  Fields:
    googleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest: A
      GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest resource to
      be passed as the request body.
    name: Required. The resource name of the Workload. This is the workloads's
      relative path in the API, formatted as "organizations/{organization_id}/
      locations/{location_id}/workloads/{workload_id}". For example,
      "organizations/123/locations/us-east1/workloads/assured-workload-1".
  """

  googleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest = _messages.MessageField('GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest', 1)
  name = _messages.StringField(2, required=True)


class GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadata(_messages.Message):
  r"""Operation metadata to give request details of CreateWorkload.

  Enums:
    ComplianceRegimeValueValuesEnum: Optional. Compliance controls that should
      be applied to the resources managed by the workload.

  Fields:
    complianceRegime: Optional. Compliance controls that should be applied to
      the resources managed by the workload.
    createTime: Optional. Time when the operation was created.
    displayName: Optional. The display name of the workload.
    parent: Optional. The parent of the workload.
  """

  class ComplianceRegimeValueValuesEnum(_messages.Enum):
    r"""Optional. Compliance controls that should be applied to the resources
    managed by the workload.

    Values:
      COMPLIANCE_REGIME_UNSPECIFIED: Unknown compliance regime.
      IL4: Information protection as per DoD IL4 requirements.
      CJIS: Criminal Justice Information Services (CJIS) Security policies.
      FEDRAMP_HIGH: FedRAMP High data protection controls
      FEDRAMP_MODERATE: FedRAMP Moderate data protection controls
      US_REGIONAL_ACCESS: Assured Workloads For US Regions data protection
        controls
      HIPAA: Health Insurance Portability and Accountability Act controls
      HITRUST: Health Information Trust Alliance controls
      EU_REGIONS_AND_SUPPORT: Assured Workloads For EU Regions and Support
        controls
      CA_REGIONS_AND_SUPPORT: Assured Workloads For Canada Regions and Support
        controls
      ITAR: International Traffic in Arms Regulations
    """
    COMPLIANCE_REGIME_UNSPECIFIED = 0
    IL4 = 1
    CJIS = 2
    FEDRAMP_HIGH = 3
    FEDRAMP_MODERATE = 4
    US_REGIONAL_ACCESS = 5
    HIPAA = 6
    HITRUST = 7
    EU_REGIONS_AND_SUPPORT = 8
    CA_REGIONS_AND_SUPPORT = 9
    ITAR = 10

  complianceRegime = _messages.EnumField('ComplianceRegimeValueValuesEnum', 1)
  createTime = _messages.StringField(2)
  displayName = _messages.StringField(3)
  parent = _messages.StringField(4)


class GoogleCloudAssuredworkloadsV1ListWorkloadsResponse(_messages.Message):
  r"""Response of ListWorkloads endpoint.

  Fields:
    nextPageToken: The next page token. Return empty if reached the last page.
    workloads: List of Workloads under a given parent.
  """

  nextPageToken = _messages.StringField(1)
  workloads = _messages.MessageField('GoogleCloudAssuredworkloadsV1Workload', 2, repeated=True)


class GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest(_messages.Message):
  r"""Request for restricting list of available resources in Workload
  environment.

  Enums:
    RestrictionTypeValueValuesEnum: Required. The type of restriction for
      using gcp products in the Workload environment.

  Fields:
    restrictionType: Required. The type of restriction for using gcp products
      in the Workload environment.
  """

  class RestrictionTypeValueValuesEnum(_messages.Enum):
    r"""Required. The type of restriction for using gcp products in the
    Workload environment.

    Values:
      RESTRICTION_TYPE_UNSPECIFIED: Unknown restriction type.
      ALLOW_ALL_GCP_RESOURCES: Allow the use all of all gcp products,
        irrespective of the compliance posture. This effectively removes
        gcp.restrictServiceUsage OrgPolicy on the AssuredWorkloads Folder.
      ALLOW_COMPLIANT_RESOURCES: Based on Workload's compliance regime,
        allowed list changes. See - https://cloud.google.com/assured-
        workloads/docs/supported-products for the list of supported resources.
    """
    RESTRICTION_TYPE_UNSPECIFIED = 0
    ALLOW_ALL_GCP_RESOURCES = 1
    ALLOW_COMPLIANT_RESOURCES = 2

  restrictionType = _messages.EnumField('RestrictionTypeValueValuesEnum', 1)


class GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponse(_messages.Message):
  r"""Response for restricting the list of allowed resources."""


class GoogleCloudAssuredworkloadsV1Workload(_messages.Message):
  r"""An Workload object for managing highly regulated workloads of cloud
  customers.

  Enums:
    ComplianceRegimeValueValuesEnum: Required. Immutable. Compliance Regime
      associated with this workload.
    KajEnrollmentStateValueValuesEnum: Output only. Represents the KAJ
      enrollment state of the given workload.

  Messages:
    LabelsValue: Optional. Labels applied to the workload.

  Fields:
    billingAccount: Optional. The billing account used for the resources which
      are direct children of workload. This billing account is initially
      associated with the resources created as part of Workload creation.
      After the initial creation of these resources, the customer can change
      the assigned billing account. The resource name has the form
      `billingAccounts/{billing_account_id}`. For example,
      `billingAccounts/012345-567890-ABCDEF`.
    complianceRegime: Required. Immutable. Compliance Regime associated with
      this workload.
    compliantButDisallowedServices: Output only. Urls for services which are
      compliant for this Assured Workload, but which are currently disallowed
      by the ResourceUsageRestriction org policy. Invoke
      RestrictAllowedResources endpoint to allow your project developers to
      use these services in their environment."
    createTime: Output only. Immutable. The Workload creation timestamp.
    displayName: Required. The user-assigned display name of the Workload.
      When present it must be between 4 to 30 characters. Allowed characters
      are: lowercase and uppercase letters, numbers, hyphen, and spaces.
      Example: My Workload
    enableSovereignControls: Optional. Indicates the sovereignty status of the
      given workload. Currently meant to be used by Europe/Canada customers.
    etag: Optional. ETag of the workload, it is calculated on the basis of the
      Workload contents. It will be used in Update & Delete operations.
    kajEnrollmentState: Output only. Represents the KAJ enrollment state of
      the given workload.
    kmsSettings: Input only. Settings used to create a CMEK crypto key. When
      set, a project with a KMS CMEK key is provisioned. This field is
      deprecated as of Feb 28, 2022. In order to create a Keyring, callers
      should specify, ENCRYPTION_KEYS_PROJECT or KEYRING in
      ResourceSettings.resource_type field.
    labels: Optional. Labels applied to the workload.
    name: Optional. The resource name of the workload. Format:
      organizations/{organization}/locations/{location}/workloads/{workload}
      Read-only.
    provisionedResourcesParent: Input only. The parent resource for the
      resources managed by this Assured Workload. May be either empty or a
      folder resource which is a child of the Workload parent. If not
      specified all resources are created under the parent organization.
      Format: folders/{folder_id}
    resourceSettings: Input only. Resource properties that are used to
      customize workload resources. These properties (such as custom project
      id) will be used to create workload resources if possible. This field is
      optional.
    resources: Output only. The resources associated with this workload. These
      resources will be created when creating the workload. If any of the
      projects already exist, the workload creation will fail. Always read
      only.
    saaEnrollmentResponse: Output only. Represents the SAA enrollment response
      of the given workload. SAA enrollment response is queried during
      GetWorkload call. In failure cases, user friendly error message is shown
      in SAA details page.
  """

  class ComplianceRegimeValueValuesEnum(_messages.Enum):
    r"""Required. Immutable. Compliance Regime associated with this workload.

    Values:
      COMPLIANCE_REGIME_UNSPECIFIED: Unknown compliance regime.
      IL4: Information protection as per DoD IL4 requirements.
      CJIS: Criminal Justice Information Services (CJIS) Security policies.
      FEDRAMP_HIGH: FedRAMP High data protection controls
      FEDRAMP_MODERATE: FedRAMP Moderate data protection controls
      US_REGIONAL_ACCESS: Assured Workloads For US Regions data protection
        controls
      HIPAA: Health Insurance Portability and Accountability Act controls
      HITRUST: Health Information Trust Alliance controls
      EU_REGIONS_AND_SUPPORT: Assured Workloads For EU Regions and Support
        controls
      CA_REGIONS_AND_SUPPORT: Assured Workloads For Canada Regions and Support
        controls
      ITAR: International Traffic in Arms Regulations
    """
    COMPLIANCE_REGIME_UNSPECIFIED = 0
    IL4 = 1
    CJIS = 2
    FEDRAMP_HIGH = 3
    FEDRAMP_MODERATE = 4
    US_REGIONAL_ACCESS = 5
    HIPAA = 6
    HITRUST = 7
    EU_REGIONS_AND_SUPPORT = 8
    CA_REGIONS_AND_SUPPORT = 9
    ITAR = 10

  class KajEnrollmentStateValueValuesEnum(_messages.Enum):
    r"""Output only. Represents the KAJ enrollment state of the given
    workload.

    Values:
      KAJ_ENROLLMENT_STATE_UNSPECIFIED: Default State for KAJ Enrollment.
      KAJ_ENROLLMENT_STATE_PENDING: Pending State for KAJ Enrollment.
      KAJ_ENROLLMENT_STATE_COMPLETE: Complete State for KAJ Enrollment.
    """
    KAJ_ENROLLMENT_STATE_UNSPECIFIED = 0
    KAJ_ENROLLMENT_STATE_PENDING = 1
    KAJ_ENROLLMENT_STATE_COMPLETE = 2

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Optional. Labels applied to the workload.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  billingAccount = _messages.StringField(1)
  complianceRegime = _messages.EnumField('ComplianceRegimeValueValuesEnum', 2)
  compliantButDisallowedServices = _messages.StringField(3, repeated=True)
  createTime = _messages.StringField(4)
  displayName = _messages.StringField(5)
  enableSovereignControls = _messages.BooleanField(6)
  etag = _messages.StringField(7)
  kajEnrollmentState = _messages.EnumField('KajEnrollmentStateValueValuesEnum', 8)
  kmsSettings = _messages.MessageField('GoogleCloudAssuredworkloadsV1WorkloadKMSSettings', 9)
  labels = _messages.MessageField('LabelsValue', 10)
  name = _messages.StringField(11)
  provisionedResourcesParent = _messages.StringField(12)
  resourceSettings = _messages.MessageField('GoogleCloudAssuredworkloadsV1WorkloadResourceSettings', 13, repeated=True)
  resources = _messages.MessageField('GoogleCloudAssuredworkloadsV1WorkloadResourceInfo', 14, repeated=True)
  saaEnrollmentResponse = _messages.MessageField('GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponse', 15)


class GoogleCloudAssuredworkloadsV1WorkloadKMSSettings(_messages.Message):
  r"""Settings specific to the Key Management Service.

  Fields:
    nextRotationTime: Required. Input only. Immutable. The time at which the
      Key Management Service will automatically create a new version of the
      crypto key and mark it as the primary.
    rotationPeriod: Required. Input only. Immutable. [next_rotation_time] will
      be advanced by this period when the Key Management Service automatically
      rotates a key. Must be at least 24 hours and at most 876,000 hours.
  """

  nextRotationTime = _messages.StringField(1)
  rotationPeriod = _messages.StringField(2)


class GoogleCloudAssuredworkloadsV1WorkloadResourceInfo(_messages.Message):
  r"""Represent the resources that are children of this Workload.

  Enums:
    ResourceTypeValueValuesEnum: Indicates the type of resource.

  Fields:
    resourceId: Resource identifier. For a project this represents
      project_number.
    resourceType: Indicates the type of resource.
  """

  class ResourceTypeValueValuesEnum(_messages.Enum):
    r"""Indicates the type of resource.

    Values:
      RESOURCE_TYPE_UNSPECIFIED: Unknown resource type.
      CONSUMER_PROJECT: Consumer project. AssuredWorkloads Projects are no
        longer supported. This field will be ignored only in CreateWorkload
        requests. ListWorkloads and GetWorkload will continue to provide
        projects information. Use CONSUMER_FOLDER instead.
      CONSUMER_FOLDER: Consumer Folder.
      ENCRYPTION_KEYS_PROJECT: Consumer project containing encryption keys.
      KEYRING: Keyring resource that hosts encryption keys.
    """
    RESOURCE_TYPE_UNSPECIFIED = 0
    CONSUMER_PROJECT = 1
    CONSUMER_FOLDER = 2
    ENCRYPTION_KEYS_PROJECT = 3
    KEYRING = 4

  resourceId = _messages.IntegerField(1)
  resourceType = _messages.EnumField('ResourceTypeValueValuesEnum', 2)


class GoogleCloudAssuredworkloadsV1WorkloadResourceSettings(_messages.Message):
  r"""Represent the custom settings for the resources to be created.

  Enums:
    ResourceTypeValueValuesEnum: Indicates the type of resource. This field
      should be specified to correspond the id to the right project type
      (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT)

  Fields:
    displayName: User-assigned resource display name. If not empty it will be
      used to create a resource with the specified name.
    resourceId: Resource identifier. For a project this represents project_id.
      If the project is already taken, the workload creation will fail. For
      KeyRing, this represents the keyring_id. For a folder, don't set this
      value as folder_id is assigned by Google.
    resourceType: Indicates the type of resource. This field should be
      specified to correspond the id to the right project type
      (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT)
  """

  class ResourceTypeValueValuesEnum(_messages.Enum):
    r"""Indicates the type of resource. This field should be specified to
    correspond the id to the right project type (CONSUMER_PROJECT or
    ENCRYPTION_KEYS_PROJECT)

    Values:
      RESOURCE_TYPE_UNSPECIFIED: Unknown resource type.
      CONSUMER_PROJECT: Consumer project. AssuredWorkloads Projects are no
        longer supported. This field will be ignored only in CreateWorkload
        requests. ListWorkloads and GetWorkload will continue to provide
        projects information. Use CONSUMER_FOLDER instead.
      CONSUMER_FOLDER: Consumer Folder.
      ENCRYPTION_KEYS_PROJECT: Consumer project containing encryption keys.
      KEYRING: Keyring resource that hosts encryption keys.
    """
    RESOURCE_TYPE_UNSPECIFIED = 0
    CONSUMER_PROJECT = 1
    CONSUMER_FOLDER = 2
    ENCRYPTION_KEYS_PROJECT = 3
    KEYRING = 4

  displayName = _messages.StringField(1)
  resourceId = _messages.StringField(2)
  resourceType = _messages.EnumField('ResourceTypeValueValuesEnum', 3)


class GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponse(_messages.Message):
  r"""Signed Access Approvals (SAA) enrollment response.

  Enums:
    SetupErrorsValueListEntryValuesEnum:
    SetupStatusValueValuesEnum: Indicates SAA enrollment status of a given
      workload.

  Fields:
    setupErrors: Indicates SAA enrollment setup error if any.
    setupStatus: Indicates SAA enrollment status of a given workload.
  """

  class SetupErrorsValueListEntryValuesEnum(_messages.Enum):
    r"""SetupErrorsValueListEntryValuesEnum enum type.

    Values:
      SETUP_ERROR_UNSPECIFIED: Unspecified.
      ERROR_INVALID_BASE_SETUP: Invalid states for all customers, to be
        redirected to AA UI for additional details.
      ERROR_MISSING_EXTERNAL_SIGNING_KEY: Returned when there is not an EKM
        key configured.
      ERROR_NOT_ALL_SERVICES_ENROLLED: Returned when there are no enrolled
        services or the customer is enrolled in CAA only for a subset of
        services.
      ERROR_SETUP_CHECK_FAILED: Returned when exception was encountered during
        evaluation of other criteria.
    """
    SETUP_ERROR_UNSPECIFIED = 0
    ERROR_INVALID_BASE_SETUP = 1
    ERROR_MISSING_EXTERNAL_SIGNING_KEY = 2
    ERROR_NOT_ALL_SERVICES_ENROLLED = 3
    ERROR_SETUP_CHECK_FAILED = 4

  class SetupStatusValueValuesEnum(_messages.Enum):
    r"""Indicates SAA enrollment status of a given workload.

    Values:
      SETUP_STATE_UNSPECIFIED: Unspecified.
      STATUS_PENDING: SAA enrollment pending.
      STATUS_COMPLETE: SAA enrollment comopleted.
    """
    SETUP_STATE_UNSPECIFIED = 0
    STATUS_PENDING = 1
    STATUS_COMPLETE = 2

  setupErrors = _messages.EnumField('SetupErrorsValueListEntryValuesEnum', 1, repeated=True)
  setupStatus = _messages.EnumField('SetupStatusValueValuesEnum', 2)


class GoogleLongrunningListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('GoogleLongrunningOperation', 2, repeated=True)


class GoogleLongrunningOperation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success. If
      the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success. If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('GoogleRpcStatus', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class GoogleProtobufEmpty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class GoogleRpcStatus(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
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
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
