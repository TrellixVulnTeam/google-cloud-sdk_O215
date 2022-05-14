"""Generated message classes for sourcerepo version v1.

Accesses source code repositories hosted by Google.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'sourcerepo'


class AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs. If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted. Example Policy with
  multiple AuditConfigs: { "audit_configs": [ { "service": "allServices",
  "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [
  "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type":
  "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com",
  "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type":
  "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For
  sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ
  logging. It also exempts `jose@example.com` from DATA_READ logging, and
  `aliya@example.com` from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example: {
  "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [
  "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables
  'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from
  DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class Binding(_messages.Message):
  r"""Associates `members`, or principals, with a `role`.

  Fields:
    condition: The condition that is associated with this binding. If the
      condition evaluates to `true`, then this binding applies to the current
      request. If the condition evaluates to `false`, then this binding does
      not apply to the current request. However, a different role binding
      might grant the same role to one or more of the principals in this
      binding. To learn which resources support conditions in their IAM
      policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    members: Specifies the principals requesting access for a Google Cloud
      resource. `members` can have the following values: * `allUsers`: A
      special identifier that represents anyone who is on the internet; with
      or without a Google account. * `allAuthenticatedUsers`: A special
      identifier that represents anyone who is authenticated with a Google
      account or a service account. * `user:{emailid}`: An email address that
      represents a specific Google account. For example, `alice@example.com` .
      * `serviceAccount:{emailid}`: An email address that represents a service
      account. For example, `my-other-app@appspot.gserviceaccount.com`. *
      `group:{emailid}`: An email address that represents a Google group. For
      example, `admins@example.com`. *
      `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique
      identifier) representing a user that has been recently deleted. For
      example, `alice@example.com?uid=123456789012345678901`. If the user is
      recovered, this value reverts to `user:{emailid}` and the recovered user
      retains the role in the binding. *
      `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address
      (plus unique identifier) representing a service account that has been
      recently deleted. For example, `my-other-
      app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the
      service account is undeleted, this value reverts to
      `serviceAccount:{emailid}` and the undeleted service account retains the
      role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An
      email address (plus unique identifier) representing a Google group that
      has been recently deleted. For example,
      `admins@example.com?uid=123456789012345678901`. If the group is
      recovered, this value reverts to `group:{emailid}` and the recovered
      group retains the role in the binding. * `domain:{domain}`: The G Suite
      domain (primary) that represents all the users of that domain. For
      example, `google.com` or `example.com`.
    role: Role that is assigned to the list of `members`, or principals. For
      example, `roles/viewer`, `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('Expr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class Expr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec. Example (Comparison):
  title: "Summary size limit" description: "Determines if a summary is less
  than 100 chars" expression: "document.summary.size() < 100" Example
  (Equality): title: "Requestor is owner" description: "Determines if
  requestor is the document owner" expression: "document.owner ==
  request.auth.claims.email" Example (Logic): title: "Public documents"
  description: "Determine whether the document should be publicly visible"
  expression: "document.type != 'private' && document.type != 'internal'"
  Example (Data Manipulation): title: "Notification string" description:
  "Create a notification string with a timestamp." expression: "'New message
  received at ' + string(document.create_time)" The exact variables and
  functions that may be referenced within an expression are determined by the
  service that evaluates it. See the service documentation for additional
  information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class ListReposResponse(_messages.Message):
  r"""Response for ListRepos. The size is not set in the returned
  repositories.

  Fields:
    nextPageToken: If non-empty, additional repositories exist within the
      project. These can be retrieved by including this value in the next
      ListReposRequest's page_token field.
    repos: The listed repos.
  """

  nextPageToken = _messages.StringField(1)
  repos = _messages.MessageField('Repo', 2, repeated=True)


class MirrorConfig(_messages.Message):
  r"""Configuration to automatically mirror a repository from another hosting
  service, for example GitHub or Bitbucket.

  Fields:
    deployKeyId: ID of the SSH deploy key at the other hosting service.
      Removing this key from the other service would deauthorize Google Cloud
      Source Repositories from mirroring.
    url: URL of the main repository at the other hosting service.
    webhookId: ID of the webhook listening to updates to trigger mirroring.
      Removing this webhook from the other hosting service will stop Google
      Cloud Source Repositories from receiving notifications, and thereby
      disabling mirroring.
  """

  deployKeyId = _messages.StringField(1)
  url = _messages.StringField(2)
  webhookId = _messages.StringField(3)


class Operation(_messages.Message):
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
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class Policy(_messages.Message):
  r"""An Identity and Access Management (IAM) policy, which specifies access
  controls for Google Cloud resources. A `Policy` is a collection of
  `bindings`. A `binding` binds one or more `members`, or principals, to a
  single `role`. Principals can be user accounts, service accounts, Google
  groups, and domains (such as G Suite). A `role` is a named list of
  permissions; each `role` can be an IAM predefined role or a user-created
  custom role. For some types of Google Cloud resources, a `binding` can also
  specify a `condition`, which is a logical expression that allows access to a
  resource only if the expression evaluates to `true`. A condition can add
  constraints based on attributes of the request, the resource, or both. To
  learn which resources support conditions in their IAM policies, see the [IAM
  documentation](https://cloud.google.com/iam/help/conditions/resource-
  policies). **JSON example:** { "bindings": [ { "role":
  "roles/resourcemanager.organizationAdmin", "members": [
  "user:mike@example.com", "group:admins@example.com", "domain:google.com",
  "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role":
  "roles/resourcemanager.organizationViewer", "members": [
  "user:eve@example.com" ], "condition": { "title": "expirable access",
  "description": "Does not grant access after Sep 2020", "expression":
  "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag":
  "BwWWja0YfJA=", "version": 3 } **YAML example:** bindings: - members: -
  user:mike@example.com - group:admins@example.com - domain:google.com -
  serviceAccount:my-project-id@appspot.gserviceaccount.com role:
  roles/resourcemanager.organizationAdmin - members: - user:eve@example.com
  role: roles/resourcemanager.organizationViewer condition: title: expirable
  access description: Does not grant access after Sep 2020 expression:
  request.time < timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA=
  version: 3 For a description of IAM and its features, see the [IAM
  documentation](https://cloud.google.com/iam/docs/).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members`, or principals, with a `role`.
      Optionally, may specify a `condition` that determines how and when the
      `bindings` are applied. Each of the `bindings` must contain at least one
      principal. The `bindings` in a `Policy` can refer to up to 1,500
      principals; up to 250 of these principals can be Google groups. Each
      occurrence of a principal counts towards these limits. For example, if
      the `bindings` grant 50 different roles to `user:alice@example.com`, and
      not to any other principal, then you can add another 1,450 principals to
      the `bindings` in the `Policy`.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy. **Important:** If you use IAM Conditions, you must include the
      `etag` field whenever you call `setIamPolicy`. If you omit this field,
      then IAM allows you to overwrite a version `3` policy with a version `1`
      policy, and all of the conditions in the version `3` policy are lost.
    version: Specifies the format of the policy. Valid values are `0`, `1`,
      and `3`. Requests that specify an invalid value are rejected. Any
      operation that affects conditional role bindings must specify version
      `3`. This requirement applies to the following operations: * Getting a
      policy that includes a conditional role binding * Adding a conditional
      role binding to a policy * Changing a conditional role binding in a
      policy * Removing any role binding, with or without a condition, from a
      policy that includes conditions **Important:** If you use IAM
      Conditions, you must include the `etag` field whenever you call
      `setIamPolicy`. If you omit this field, then IAM allows you to overwrite
      a version `3` policy with a version `1` policy, and all of the
      conditions in the version `3` policy are lost. If a policy does not
      include any conditions, operations on that policy may specify any valid
      version or leave the field unset. To learn which resources support
      conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
  """

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class ProjectConfig(_messages.Message):
  r"""Cloud Source Repositories configuration of a project.

  Messages:
    PubsubConfigsValue: How this project publishes a change in the
      repositories through Cloud Pub/Sub. Keyed by the topic names.

  Fields:
    enablePrivateKeyCheck: Reject a Git push that contains a private key.
    name: The name of the project. Values are of the form `projects/`.
    pubsubConfigs: How this project publishes a change in the repositories
      through Cloud Pub/Sub. Keyed by the topic names.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class PubsubConfigsValue(_messages.Message):
    r"""How this project publishes a change in the repositories through Cloud
    Pub/Sub. Keyed by the topic names.

    Messages:
      AdditionalProperty: An additional property for a PubsubConfigsValue
        object.

    Fields:
      additionalProperties: Additional properties of type PubsubConfigsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a PubsubConfigsValue object.

      Fields:
        key: Name of the additional property.
        value: A PubsubConfig attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('PubsubConfig', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  enablePrivateKeyCheck = _messages.BooleanField(1)
  name = _messages.StringField(2)
  pubsubConfigs = _messages.MessageField('PubsubConfigsValue', 3)


class PubsubConfig(_messages.Message):
  r"""Configuration to publish a Cloud Pub/Sub message.

  Enums:
    MessageFormatValueValuesEnum: The format of the Cloud Pub/Sub messages.

  Fields:
    messageFormat: The format of the Cloud Pub/Sub messages.
    serviceAccountEmail: Email address of the service account used for
      publishing Cloud Pub/Sub messages. This service account needs to be in
      the same project as the PubsubConfig. When added, the caller needs to
      have iam.serviceAccounts.actAs permission on this service account. If
      unspecified, it defaults to the compute engine default service account.
    topic: A topic of Cloud Pub/Sub. Values are of the form
      `projects//topics/`. The project needs to be the same project as this
      config is in.
  """

  class MessageFormatValueValuesEnum(_messages.Enum):
    r"""The format of the Cloud Pub/Sub messages.

    Values:
      MESSAGE_FORMAT_UNSPECIFIED: Unspecified.
      PROTOBUF: The message payload is a serialized protocol buffer of
        SourceRepoEvent.
      JSON: The message payload is a JSON string of SourceRepoEvent.
    """
    MESSAGE_FORMAT_UNSPECIFIED = 0
    PROTOBUF = 1
    JSON = 2

  messageFormat = _messages.EnumField('MessageFormatValueValuesEnum', 1)
  serviceAccountEmail = _messages.StringField(2)
  topic = _messages.StringField(3)


class Repo(_messages.Message):
  r"""A repository (or repo) is a Git repository storing versioned source
  content.

  Messages:
    PubsubConfigsValue: How this repository publishes a change in the
      repository through Cloud Pub/Sub. Keyed by the topic names.

  Fields:
    mirrorConfig: How this repository mirrors a repository managed by another
      service. Read-only field.
    name: Resource name of the repository, of the form `projects//repos/`. The
      repo name may contain slashes. eg,
      `projects/myproject/repos/name/with/slash`
    pubsubConfigs: How this repository publishes a change in the repository
      through Cloud Pub/Sub. Keyed by the topic names.
    size: The disk usage of the repo, in bytes. Read-only field. Size is only
      returned by GetRepo.
    url: URL to clone the repository from Google Cloud Source Repositories.
      Read-only field.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class PubsubConfigsValue(_messages.Message):
    r"""How this repository publishes a change in the repository through Cloud
    Pub/Sub. Keyed by the topic names.

    Messages:
      AdditionalProperty: An additional property for a PubsubConfigsValue
        object.

    Fields:
      additionalProperties: Additional properties of type PubsubConfigsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a PubsubConfigsValue object.

      Fields:
        key: Name of the additional property.
        value: A PubsubConfig attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('PubsubConfig', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  mirrorConfig = _messages.MessageField('MirrorConfig', 1)
  name = _messages.StringField(2)
  pubsubConfigs = _messages.MessageField('PubsubConfigsValue', 3)
  size = _messages.IntegerField(4)
  url = _messages.StringField(5)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Google Cloud services (such as Projects) might
      reject them.
    updateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
      modify. Only the fields in the mask will be modified. If no mask is
      provided, the following default mask is used: `paths: "bindings, etag"`
  """

  policy = _messages.MessageField('Policy', 1)
  updateMask = _messages.StringField(2)


class SourcerepoProjectsGetConfigRequest(_messages.Message):
  r"""A SourcerepoProjectsGetConfigRequest object.

  Fields:
    name: The name of the requested project. Values are of the form
      `projects/`.
  """

  name = _messages.StringField(1, required=True)


class SourcerepoProjectsReposCreateRequest(_messages.Message):
  r"""A SourcerepoProjectsReposCreateRequest object.

  Fields:
    parent: The project in which to create the repo. Values are of the form
      `projects/`.
    repo: A Repo resource to be passed as the request body.
  """

  parent = _messages.StringField(1, required=True)
  repo = _messages.MessageField('Repo', 2)


class SourcerepoProjectsReposDeleteRequest(_messages.Message):
  r"""A SourcerepoProjectsReposDeleteRequest object.

  Fields:
    name: The name of the repo to delete. Values are of the form
      `projects//repos/`.
  """

  name = _messages.StringField(1, required=True)


class SourcerepoProjectsReposGetIamPolicyRequest(_messages.Message):
  r"""A SourcerepoProjectsReposGetIamPolicyRequest object.

  Fields:
    options_requestedPolicyVersion: Optional. The maximum policy version that
      will be used to format the policy. Valid values are 0, 1, and 3.
      Requests specifying an invalid value will be rejected. Requests for
      policies with any conditional role bindings must specify version 3.
      Policies with no conditional role bindings may specify any valid value
      or leave the field unset. The policy in the response might use the
      policy version that you specified, or it might use a lower policy
      version. For example, if you specify version 3, but the policy has no
      conditional role bindings, the response uses version 1. To learn which
      resources support conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  options_requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  resource = _messages.StringField(2, required=True)


class SourcerepoProjectsReposGetRequest(_messages.Message):
  r"""A SourcerepoProjectsReposGetRequest object.

  Fields:
    name: The name of the requested repository. Values are of the form
      `projects//repos/`.
  """

  name = _messages.StringField(1, required=True)


class SourcerepoProjectsReposListRequest(_messages.Message):
  r"""A SourcerepoProjectsReposListRequest object.

  Fields:
    name: The project ID whose repos should be listed. Values are of the form
      `projects/`.
    pageSize: Maximum number of repositories to return; between 1 and 500. If
      not set or zero, defaults to 100 at the server.
    pageToken: Resume listing repositories where a prior ListReposResponse
      left off. This is an opaque token that must be obtained from a recent,
      prior ListReposResponse's next_page_token field.
  """

  name = _messages.StringField(1, required=True)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)


class SourcerepoProjectsReposPatchRequest(_messages.Message):
  r"""A SourcerepoProjectsReposPatchRequest object.

  Fields:
    name: The name of the requested repository. Values are of the form
      `projects//repos/`.
    updateRepoRequest: A UpdateRepoRequest resource to be passed as the
      request body.
  """

  name = _messages.StringField(1, required=True)
  updateRepoRequest = _messages.MessageField('UpdateRepoRequest', 2)


class SourcerepoProjectsReposSetIamPolicyRequest(_messages.Message):
  r"""A SourcerepoProjectsReposSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class SourcerepoProjectsReposSyncRequest(_messages.Message):
  r"""A SourcerepoProjectsReposSyncRequest object.

  Fields:
    name: The name of the repo to synchronize. Values are of the form
      `projects//repos/`.
    syncRepoRequest: A SyncRepoRequest resource to be passed as the request
      body.
  """

  name = _messages.StringField(1, required=True)
  syncRepoRequest = _messages.MessageField('SyncRepoRequest', 2)


class SourcerepoProjectsReposTestIamPermissionsRequest(_messages.Message):
  r"""A SourcerepoProjectsReposTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class SourcerepoProjectsUpdateConfigRequest(_messages.Message):
  r"""A SourcerepoProjectsUpdateConfigRequest object.

  Fields:
    name: The name of the requested project. Values are of the form
      `projects/`.
    updateProjectConfigRequest: A UpdateProjectConfigRequest resource to be
      passed as the request body.
  """

  name = _messages.StringField(1, required=True)
  updateProjectConfigRequest = _messages.MessageField('UpdateProjectConfigRequest', 2)


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


class Status(_messages.Message):
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


class SyncRepoMetadata(_messages.Message):
  r"""Metadata of SyncRepo. This message is in the metadata field of
  Operation.

  Fields:
    name: The name of the repo being synchronized. Values are of the form
      `projects//repos/`.
    startTime: The time this operation is started.
    statusMessage: The latest status message on syncing the repository.
    updateTime: The time this operation's status message is updated.
  """

  name = _messages.StringField(1)
  startTime = _messages.StringField(2)
  statusMessage = _messages.StringField(3)
  updateTime = _messages.StringField(4)


class SyncRepoRequest(_messages.Message):
  r"""Request for SyncRepo."""


class TestIamPermissionsRequest(_messages.Message):
  r"""Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as `*` or `storage.*`) are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  r"""Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


class UpdateProjectConfigRequest(_messages.Message):
  r"""Request for UpdateProjectConfig.

  Fields:
    projectConfig: The new configuration for the project.
    updateMask: A FieldMask specifying which fields of the project_config to
      modify. Only the fields in the mask will be modified. If no mask is
      provided, this request is no-op.
  """

  projectConfig = _messages.MessageField('ProjectConfig', 1)
  updateMask = _messages.StringField(2)


class UpdateRepoRequest(_messages.Message):
  r"""Request for UpdateRepo.

  Fields:
    repo: The new configuration for the repository.
    updateMask: A FieldMask specifying which fields of the repo to modify.
      Only the fields in the mask will be modified. If no mask is provided,
      this request is no-op.
  """

  repo = _messages.MessageField('Repo', 1)
  updateMask = _messages.StringField(2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
