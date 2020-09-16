"""Generated message classes for binaryauthorization version v1.

The management interface for Binary Authorization, a system providing policy
control for images deployed to Kubernetes Engine clusters.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'binaryauthorization'


class AdmissionRule(_messages.Message):
  r"""An admission rule specifies either that all container images used in a
  pod creation request must be attested to by one or more attestors, that all
  pod creations will be allowed, or that all pod creations will be denied.
  Images matching an admission whitelist pattern are exempted from admission
  rules and will never block a pod creation.

  Enums:
    EnforcementModeValueValuesEnum: Required. The action when a pod creation
      is denied by the admission rule.
    EvaluationModeValueValuesEnum: Required. How this admission rule will be
      evaluated.

  Fields:
    enforcementMode: Required. The action when a pod creation is denied by the
      admission rule.
    evaluationMode: Required. How this admission rule will be evaluated.
    requireAttestationsBy: Optional. The resource names of the attestors that
      must attest to a container image, in the format
      `projects/*/attestors/*`. Each attestor must exist before a policy can
      reference it. To add an attestor to a policy the principal issuing the
      policy change request must be able to read the attestor resource. Note:
      this field must be non-empty when the evaluation_mode field specifies
      REQUIRE_ATTESTATION, otherwise it must be empty.
  """

  class EnforcementModeValueValuesEnum(_messages.Enum):
    r"""Required. The action when a pod creation is denied by the admission
    rule.

    Values:
      ENFORCEMENT_MODE_UNSPECIFIED: Do not use.
      ENFORCED_BLOCK_AND_AUDIT_LOG: Enforce the admission rule by blocking the
        pod creation.
      DRYRUN_AUDIT_LOG_ONLY: Dryrun mode: Audit logging only. This will allow
        the pod creation as if the admission request had specified break-
        glass.
    """
    ENFORCEMENT_MODE_UNSPECIFIED = 0
    ENFORCED_BLOCK_AND_AUDIT_LOG = 1
    DRYRUN_AUDIT_LOG_ONLY = 2

  class EvaluationModeValueValuesEnum(_messages.Enum):
    r"""Required. How this admission rule will be evaluated.

    Values:
      EVALUATION_MODE_UNSPECIFIED: Do not use.
      ALWAYS_ALLOW: This rule allows all all pod creations.
      REQUIRE_ATTESTATION: This rule allows a pod creation if all the
        attestors listed in 'require_attestations_by' have valid attestations
        for all of the images in the pod spec.
      ALWAYS_DENY: This rule denies all pod creations.
    """
    EVALUATION_MODE_UNSPECIFIED = 0
    ALWAYS_ALLOW = 1
    REQUIRE_ATTESTATION = 2
    ALWAYS_DENY = 3

  enforcementMode = _messages.EnumField('EnforcementModeValueValuesEnum', 1)
  evaluationMode = _messages.EnumField('EvaluationModeValueValuesEnum', 2)
  requireAttestationsBy = _messages.StringField(3, repeated=True)


class AdmissionWhitelistPattern(_messages.Message):
  r"""An admission whitelist pattern exempts images from checks by admission
  rules.

  Fields:
    namePattern: An image name pattern to whitelist, in the form
      `registry/path/to/image`. This supports a trailing `*` as a wildcard,
      but this is allowed only in text after the `registry/` part.
  """

  namePattern = _messages.StringField(1)


class Attestor(_messages.Message):
  r"""An attestor that attests to container image artifacts. An existing
  attestor cannot be modified except where indicated.

  Fields:
    description: Optional. A descriptive comment. This field may be updated.
      The field may be displayed in chooser dialogs.
    name: Required. The resource name, in the format:
      `projects/*/attestors/*`. This field may not be updated.
    updateTime: Output only. Time when the attestor was last updated.
    userOwnedGrafeasNote: This specifies how an attestation will be read, and
      how it will be used during policy enforcement.
  """

  description = _messages.StringField(1)
  name = _messages.StringField(2)
  updateTime = _messages.StringField(3)
  userOwnedGrafeasNote = _messages.MessageField('UserOwnedGrafeasNote', 4)


class AttestorPublicKey(_messages.Message):
  r"""An attestor public key that will be used to verify attestations signed
  by this attestor.

  Fields:
    asciiArmoredPgpPublicKey: ASCII-armored representation of a PGP public
      key, as the entire output by the command `gpg --export --armor
      foo@example.com` (either LF or CRLF line endings). When using this
      field, `id` should be left blank. The BinAuthz API handlers will
      calculate the ID and fill it in automatically. BinAuthz computes this ID
      as the OpenPGP RFC4880 V4 fingerprint, represented as upper-case hex. If
      `id` is provided by the caller, it will be overwritten by the API-
      calculated ID.
    comment: Optional. A descriptive comment. This field may be updated.
    id: The ID of this public key. Signatures verified by BinAuthz must
      include the ID of the public key that can be used to verify them, and
      that ID must match the contents of this field exactly. Additional
      restrictions on this field can be imposed based on which public key type
      is encapsulated. See the documentation on `public_key` cases below for
      details.
    pkixPublicKey: A raw PKIX SubjectPublicKeyInfo format public key. NOTE:
      `id` may be explicitly provided by the caller when using this type of
      public key, but it MUST be a valid RFC3986 URI. If `id` is left blank, a
      default one will be computed based on the digest of the DER encoding of
      the public key.
  """

  asciiArmoredPgpPublicKey = _messages.StringField(1)
  comment = _messages.StringField(2)
  id = _messages.StringField(3)
  pkixPublicKey = _messages.MessageField('PkixPublicKey', 4)


class BinaryauthorizationProjectsAttestorsCreateRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsAttestorsCreateRequest object.

  Fields:
    attestor: A Attestor resource to be passed as the request body.
    attestorId: Required. The attestors ID.
    parent: Required. The parent of this attestor.
  """

  attestor = _messages.MessageField('Attestor', 1)
  attestorId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class BinaryauthorizationProjectsAttestorsDeleteRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsAttestorsDeleteRequest object.

  Fields:
    name: Required. The name of the attestors to delete, in the format
      `projects/*/attestors/*`.
  """

  name = _messages.StringField(1, required=True)


class BinaryauthorizationProjectsAttestorsGetIamPolicyRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsAttestorsGetIamPolicyRequest object.

  Fields:
    options_requestedPolicyVersion: Optional. The policy format version to be
      returned. Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected. Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset. To learn
      which resources support conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  options_requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  resource = _messages.StringField(2, required=True)


class BinaryauthorizationProjectsAttestorsGetRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsAttestorsGetRequest object.

  Fields:
    name: Required. The name of the attestor to retrieve, in the format
      `projects/*/attestors/*`.
  """

  name = _messages.StringField(1, required=True)


class BinaryauthorizationProjectsAttestorsListRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsAttestorsListRequest object.

  Fields:
    pageSize: Requested page size. The server may return fewer results than
      requested. If unspecified, the server will pick an appropriate default.
    pageToken: A token identifying a page of results the server should return.
      Typically, this is the value of ListAttestorsResponse.next_page_token
      returned from the previous call to the `ListAttestors` method.
    parent: Required. The resource name of the project associated with the
      attestors, in the format `projects/*`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class BinaryauthorizationProjectsAttestorsSetIamPolicyRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsAttestorsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class BinaryauthorizationProjectsAttestorsTestIamPermissionsRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsAttestorsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class BinaryauthorizationProjectsGetPolicyRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsGetPolicyRequest object.

  Fields:
    name: Required. The resource name of the policy to retrieve, in the format
      `projects/*/policy`.
  """

  name = _messages.StringField(1, required=True)


class BinaryauthorizationProjectsPolicyGetIamPolicyRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsPolicyGetIamPolicyRequest object.

  Fields:
    options_requestedPolicyVersion: Optional. The policy format version to be
      returned. Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected. Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset. To learn
      which resources support conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  options_requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  resource = _messages.StringField(2, required=True)


class BinaryauthorizationProjectsPolicySetIamPolicyRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsPolicySetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class BinaryauthorizationProjectsPolicyTestIamPermissionsRequest(_messages.Message):
  r"""A BinaryauthorizationProjectsPolicyTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    bindingId: A client-specified ID for this binding. Expected to be globally
      unique to support the internal bindings-by-ID API.
    condition: The condition that is associated with this binding. If the
      condition evaluates to `true`, then this binding applies to the current
      request. If the condition evaluates to `false`, then this binding does
      not apply to the current request. However, a different role binding
      might grant the same role to one or more of the members in this binding.
      To learn which resources support conditions in their IAM policies, see
      the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    members: Specifies the identities requesting access for a Cloud Platform
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
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  bindingId = _messages.StringField(1)
  condition = _messages.MessageField('Expr', 2)
  members = _messages.StringField(3, repeated=True)
  role = _messages.StringField(4)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } The JSON
  representation for `Empty` is empty JSON object `{}`.
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


class IamPolicy(_messages.Message):
  r"""An Identity and Access Management (IAM) policy, which specifies access
  controls for Google Cloud resources. A `Policy` is a collection of
  `bindings`. A `binding` binds one or more `members` to a single `role`.
  Members can be user accounts, service accounts, Google groups, and domains
  (such as G Suite). A `role` is a named list of permissions; each `role` can
  be an IAM predefined role or a user-created custom role. For some types of
  Google Cloud resources, a `binding` can also specify a `condition`, which is
  a logical expression that allows access to a resource only if the expression
  evaluates to `true`. A condition can add constraints based on attributes of
  the request, the resource, or both. To learn which resources support
  conditions in their IAM policies, see the [IAM
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
  request.time < timestamp('2020-10-01T00:00:00.000Z') - etag: BwWWja0YfJA= -
  version: 3 For a description of IAM and its features, see the [IAM
  documentation](https://cloud.google.com/iam/docs/).

  Fields:
    bindings: Associates a list of `members` to a `role`. Optionally, may
      specify a `condition` that determines how and when the `bindings` are
      applied. Each of the `bindings` must contain at least one member.
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

  bindings = _messages.MessageField('Binding', 1, repeated=True)
  etag = _messages.BytesField(2)
  version = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class ListAttestorsResponse(_messages.Message):
  r"""Response message for BinauthzManagementService.ListAttestors.

  Fields:
    attestors: The list of attestors.
    nextPageToken: A token to retrieve the next page of results. Pass this
      value in the ListAttestorsRequest.page_token field in the subsequent
      call to the `ListAttestors` method to retrieve the next page of results.
  """

  attestors = _messages.MessageField('Attestor', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class PkixPublicKey(_messages.Message):
  r"""A public key in the PkixPublicKey format (see
  https://tools.ietf.org/html/rfc5280#section-4.1.2.7 for details). Public
  keys of this type are typically textually encoded using the PEM format.

  Enums:
    SignatureAlgorithmValueValuesEnum: The signature algorithm used to verify
      a message against a signature using this key. These signature algorithm
      must match the structure and any object identifiers encoded in
      `public_key_pem` (i.e. this algorithm must match that of the public
      key).

  Fields:
    publicKeyPem: A PEM-encoded public key, as described in
      https://tools.ietf.org/html/rfc7468#section-13
    signatureAlgorithm: The signature algorithm used to verify a message
      against a signature using this key. These signature algorithm must match
      the structure and any object identifiers encoded in `public_key_pem`
      (i.e. this algorithm must match that of the public key).
  """

  class SignatureAlgorithmValueValuesEnum(_messages.Enum):
    r"""The signature algorithm used to verify a message against a signature
    using this key. These signature algorithm must match the structure and any
    object identifiers encoded in `public_key_pem` (i.e. this algorithm must
    match that of the public key).

    Values:
      SIGNATURE_ALGORITHM_UNSPECIFIED: Not specified.
      RSA_PSS_2048_SHA256: RSASSA-PSS 2048 bit key with a SHA256 digest.
      RSA_PSS_3072_SHA256: RSASSA-PSS 3072 bit key with a SHA256 digest.
      RSA_PSS_4096_SHA256: RSASSA-PSS 4096 bit key with a SHA256 digest.
      RSA_PSS_4096_SHA512: RSASSA-PSS 4096 bit key with a SHA512 digest.
      RSA_SIGN_PKCS1_2048_SHA256: RSASSA-PKCS1-v1_5 with a 2048 bit key and a
        SHA256 digest.
      RSA_SIGN_PKCS1_3072_SHA256: RSASSA-PKCS1-v1_5 with a 3072 bit key and a
        SHA256 digest.
      RSA_SIGN_PKCS1_4096_SHA256: RSASSA-PKCS1-v1_5 with a 4096 bit key and a
        SHA256 digest.
      RSA_SIGN_PKCS1_4096_SHA512: RSASSA-PKCS1-v1_5 with a 4096 bit key and a
        SHA512 digest.
      ECDSA_P256_SHA256: ECDSA on the NIST P-256 curve with a SHA256 digest.
      EC_SIGN_P256_SHA256: ECDSA on the NIST P-256 curve with a SHA256 digest.
      ECDSA_P384_SHA384: ECDSA on the NIST P-384 curve with a SHA384 digest.
      EC_SIGN_P384_SHA384: ECDSA on the NIST P-384 curve with a SHA384 digest.
      ECDSA_P521_SHA512: ECDSA on the NIST P-521 curve with a SHA512 digest.
      EC_SIGN_P521_SHA512: ECDSA on the NIST P-521 curve with a SHA512 digest.
    """
    SIGNATURE_ALGORITHM_UNSPECIFIED = 0
    RSA_PSS_2048_SHA256 = 1
    RSA_PSS_3072_SHA256 = 2
    RSA_PSS_4096_SHA256 = 3
    RSA_PSS_4096_SHA512 = 4
    RSA_SIGN_PKCS1_2048_SHA256 = 5
    RSA_SIGN_PKCS1_3072_SHA256 = 6
    RSA_SIGN_PKCS1_4096_SHA256 = 7
    RSA_SIGN_PKCS1_4096_SHA512 = 8
    ECDSA_P256_SHA256 = 9
    EC_SIGN_P256_SHA256 = 10
    ECDSA_P384_SHA384 = 11
    EC_SIGN_P384_SHA384 = 12
    ECDSA_P521_SHA512 = 13
    EC_SIGN_P521_SHA512 = 14

  publicKeyPem = _messages.StringField(1)
  signatureAlgorithm = _messages.EnumField('SignatureAlgorithmValueValuesEnum', 2)


class Policy(_messages.Message):
  r"""A policy for container image binary authorization.

  Enums:
    GlobalPolicyEvaluationModeValueValuesEnum: Optional. Controls the
      evaluation of a Google-maintained global admission policy for common
      system-level images. Images not covered by the global policy will be
      subject to the project admission policy. This setting has no effect when
      specified inside a global admission policy.

  Messages:
    ClusterAdmissionRulesValue: Optional. Per-cluster admission rules. Cluster
      spec format: `location.clusterId`. There can be at most one admission
      rule per cluster spec. A `location` is either a compute zone (e.g. us-
      central1-a) or a region (e.g. us-central1). For `clusterId` syntax
      restrictions see https://cloud.google.com/container-
      engine/reference/rest/v1/projects.zones.clusters.

  Fields:
    admissionWhitelistPatterns: Optional. Admission policy whitelisting. A
      matching admission request will always be permitted. This feature is
      typically used to exclude Google or third-party infrastructure images
      from Binary Authorization policies.
    clusterAdmissionRules: Optional. Per-cluster admission rules. Cluster spec
      format: `location.clusterId`. There can be at most one admission rule
      per cluster spec. A `location` is either a compute zone (e.g. us-
      central1-a) or a region (e.g. us-central1). For `clusterId` syntax
      restrictions see https://cloud.google.com/container-
      engine/reference/rest/v1/projects.zones.clusters.
    defaultAdmissionRule: Required. Default admission rule for a cluster
      without a per-cluster, per- kubernetes-service-account, or per-istio-
      service-identity admission rule.
    description: Optional. A descriptive comment.
    globalPolicyEvaluationMode: Optional. Controls the evaluation of a Google-
      maintained global admission policy for common system-level images.
      Images not covered by the global policy will be subject to the project
      admission policy. This setting has no effect when specified inside a
      global admission policy.
    name: Output only. The resource name, in the format `projects/*/policy`.
      There is at most one policy per project.
    updateTime: Output only. Time when the policy was last updated.
  """

  class GlobalPolicyEvaluationModeValueValuesEnum(_messages.Enum):
    r"""Optional. Controls the evaluation of a Google-maintained global
    admission policy for common system-level images. Images not covered by the
    global policy will be subject to the project admission policy. This
    setting has no effect when specified inside a global admission policy.

    Values:
      GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED: Not specified: DISABLE is
        assumed.
      ENABLE: Enables global policy evaluation.
      DISABLE: Disables global policy evaluation.
    """
    GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED = 0
    ENABLE = 1
    DISABLE = 2

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ClusterAdmissionRulesValue(_messages.Message):
    r"""Optional. Per-cluster admission rules. Cluster spec format:
    `location.clusterId`. There can be at most one admission rule per cluster
    spec. A `location` is either a compute zone (e.g. us-central1-a) or a
    region (e.g. us-central1). For `clusterId` syntax restrictions see
    https://cloud.google.com/container-
    engine/reference/rest/v1/projects.zones.clusters.

    Messages:
      AdditionalProperty: An additional property for a
        ClusterAdmissionRulesValue object.

    Fields:
      additionalProperties: Additional properties of type
        ClusterAdmissionRulesValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ClusterAdmissionRulesValue object.

      Fields:
        key: Name of the additional property.
        value: A AdmissionRule attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('AdmissionRule', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  admissionWhitelistPatterns = _messages.MessageField('AdmissionWhitelistPattern', 1, repeated=True)
  clusterAdmissionRules = _messages.MessageField('ClusterAdmissionRulesValue', 2)
  defaultAdmissionRule = _messages.MessageField('AdmissionRule', 3)
  description = _messages.StringField(4)
  globalPolicyEvaluationMode = _messages.EnumField('GlobalPolicyEvaluationModeValueValuesEnum', 5)
  name = _messages.StringField(6)
  updateTime = _messages.StringField(7)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
  """

  policy = _messages.MessageField('IamPolicy', 1)


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


class TestIamPermissionsRequest(_messages.Message):
  r"""Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
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


class UserOwnedGrafeasNote(_messages.Message):
  r"""An user owned Grafeas note references a Grafeas Attestation.Authority
  Note created by the user.

  Fields:
    delegationServiceAccountEmail: Output only. This field will contain the
      service account email address that this Attestor will use as the
      principal when querying Container Analysis. Attestor administrators must
      grant this service account the IAM role needed to read attestations from
      the note_reference in Container Analysis
      (`containeranalysis.notes.occurrences.viewer`). This email address is
      fixed for the lifetime of the Attestor, but callers should not make any
      other assumptions about the service account email; future versions may
      use an email based on a different naming pattern.
    noteReference: Required. The Grafeas resource name of a
      Attestation.Authority Note, created by the user, in the format:
      `projects/*/notes/*`. This field may not be updated. An attestation by
      this attestor is stored as a Grafeas Attestation.Authority Occurrence
      that names a container image and that links to this Note. Grafeas is an
      external dependency.
    publicKeys: Optional. Public keys that verify attestations signed by this
      attestor. This field may be updated. If this field is non-empty, one of
      the specified public keys must verify that an attestation was signed by
      this attestor for the image specified in the admission request. If this
      field is empty, this attestor always returns that no valid attestations
      exist.
  """

  delegationServiceAccountEmail = _messages.StringField(1)
  noteReference = _messages.StringField(2)
  publicKeys = _messages.MessageField('AttestorPublicKey', 3, repeated=True)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
