"""Generated message classes for cloudbuild version v1.

The Google Cloud Container Builder API lets you build container images in the
cloud.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages as _messages

from googlecloudsdk.third_party.apitools.base.py import encoding


package = 'cloudbuild'


class Build(_messages.Message):
  """A build resource in the CloudBuild API.  At a high level, a Build
  describes where to find source, how to build the source (i.e., the builder
  image to run on the source), and what tag to apply to the built image when
  it is pushed to Google Container Registry.

  Enums:
    StatusValueValuesEnum: The status of the build. @OutputOnly

  Fields:
    createTime: The time that the build was created. @OutputOnly
    finishTime: The time that execution of the build was finished. @OutputOnly
    foremanId: The ID for the foreman that is running this build.
    id: The unique identifier of the build. @OutputOnly
    images: The list of images expected to be built and pushed to GCR. If an
      image is listed here, the build will fail if that image is not produced
      by one of the build steps. If all the images are present when the build
      steps are complete, they will all be pushed and recorded in the build's
      results.
    projectId: The ID of the project. @OutputOnly.
    results: The results of this build. @OutputOnly
    source: Describes where to find source files to build.
    startTime: The time that execution of the build was started. @OutputOnly
    status: The status of the build. @OutputOnly
    steps: Describes the operations to be performed on the workspace.
    timeout: The amount of time that this build should be allowed to run, to
      second granularity. By default, this will be ten minutes.
    userId: The end user who initiated this build.
    workerId: The ID for the worker that is running this build.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """The status of the build. @OutputOnly

    Values:
      STATUS_UNKNOWN: The status of the build is unknown.
      QUEUED: The build is queued, work has not yet begun.
      WORKING: The build is being executed.
      SUCCESS: The build finished successfully.
      FAILURE: The build failed to complete successfully.
      INTERNAL_ERROR: The build failed due to an internal cause.
      TIMEOUT: The build took longer than was allowed.
      CANCELLED: The build was cancelled by a user.
    """
    STATUS_UNKNOWN = 0
    QUEUED = 1
    WORKING = 2
    SUCCESS = 3
    FAILURE = 4
    INTERNAL_ERROR = 5
    TIMEOUT = 6
    CANCELLED = 7

  createTime = _messages.StringField(1)
  finishTime = _messages.StringField(2)
  foremanId = _messages.StringField(3)
  id = _messages.StringField(4)
  images = _messages.StringField(5, repeated=True)
  projectId = _messages.StringField(6)
  results = _messages.MessageField('Results', 7)
  source = _messages.MessageField('Source', 8)
  startTime = _messages.StringField(9)
  status = _messages.EnumField('StatusValueValuesEnum', 10)
  steps = _messages.MessageField('BuildStep', 11, repeated=True)
  timeout = _messages.StringField(12)
  userId = _messages.IntegerField(13)
  workerId = _messages.StringField(14)


class BuildStep(_messages.Message):
  """BuildStep describes a step to perform in the build pipeline.

  Fields:
    args: Command-line arguments to use when running this operation's
      container.
    dir: Working directory (relative to project source root) to use when
      running this operation's container.
    env: Additional environment variables to set for this operation's
      container.
    name: The name of the container image to use for creating this stage in
      the pipeline, as presented to 'docker pull'.
  """

  args = _messages.StringField(1, repeated=True)
  dir = _messages.StringField(2)
  env = _messages.StringField(3, repeated=True)
  name = _messages.StringField(4)


class BuiltImage(_messages.Message):
  """BuiltImage describes an image built by the pipeline.

  Fields:
    imageId: The image ID of the image pushed.
    name: The name used to push the container image to GCR, as presented to
      'docker push'.
  """

  imageId = _messages.StringField(1)
  name = _messages.StringField(2)


class CancelOperationRequest(_messages.Message):
  """The request message for Operations.CancelOperation."""


class CitcWorkspaceSourceContext(_messages.Message):
  """A CitC workspace as represented by its ID and snapshot.

  Fields:
    branchName: See PiperDepotSourceContext.branch_name for documentation.
    isBaseline: If true, ignore local workspace changes and use the baseline
      of the workspace instead.
    snapshotVersion: The snapshot within the workspace. If zero, refers to the
      moving head of the workspace.  Clients which use zero should be robust
      against remote changes made to a workspace.  If non-zero, refers to an
      immutable CitC snapshot.  The current snapshot_version for USER's CLIENT
      can be found in /google/src/cloud/USER/CLIENT/.citc/snapshot_version
    workspaceId: A unique identifier for a citc workspace. The workspace_id
      for USER's CLIENT can be found in
      /google/src/cloud/USER/CLIENT/.citc/workspace_id
  """

  branchName = _messages.StringField(1)
  isBaseline = _messages.BooleanField(2)
  snapshotVersion = _messages.IntegerField(3, variant=_messages.Variant.UINT64)
  workspaceId = _messages.StringField(4)


class CloudRepoSourceContext(_messages.Message):
  """A CloudRepoSourceContext denotes a particular revision in a cloud repo (a
  repo hosted by the Google Cloud Platform).

  Fields:
    aliasName: The name of an alias (branch, tag, etc.).
    repoId: The ID of the repo.
    revisionId: A revision ID.
  """

  aliasName = _messages.StringField(1)
  repoId = _messages.MessageField('RepoId', 2)
  revisionId = _messages.StringField(3)


class CloudWorkspaceId(_messages.Message):
  """A CloudWorkspaceId is a unique identifier for a cloud workspace. A cloud
  workspace is a place associated with a repo where modified files can be
  stored before they are committed.

  Fields:
    name: The unique name of the workspace within the repo.  This is the name
      chosen by the client in the Source API's CreateWorkspace method.
    repoId: The ID of the repo containing the workspace.
  """

  name = _messages.StringField(1)
  repoId = _messages.MessageField('RepoId', 2)


class CloudWorkspaceSourceContext(_messages.Message):
  """A CloudWorkspaceSourceContext denotes a workspace at a particular
  snapshot.

  Fields:
    snapshotId: The ID of the snapshot. An empty snapshot_id refers to the
      most recent snapshot.
    workspaceId: The ID of the workspace.
  """

  snapshotId = _messages.StringField(1)
  workspaceId = _messages.MessageField('CloudWorkspaceId', 2)


class CloudbuildOperationsCancelRequest(_messages.Message):
  """A CloudbuildOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class CloudbuildOperationsDeleteRequest(_messages.Message):
  """A CloudbuildOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class CloudbuildOperationsGetRequest(_messages.Message):
  """A CloudbuildOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class CloudbuildOperationsListRequest(_messages.Message):
  """A CloudbuildOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation collection.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class CloudbuildProjectsBuildsCancelRequest(_messages.Message):
  """A CloudbuildProjectsBuildsCancelRequest object.

  Fields:
    id: The ID of the build.
    projectId: The ID of the project.
  """

  id = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)


class CloudbuildProjectsBuildsCreateRequest(_messages.Message):
  """A CloudbuildProjectsBuildsCreateRequest object.

  Fields:
    build: A Build resource to be passed as the request body.
    projectId: The ID of the project.
  """

  build = _messages.MessageField('Build', 1)
  projectId = _messages.StringField(2, required=True)


class CloudbuildProjectsBuildsGetRequest(_messages.Message):
  """A CloudbuildProjectsBuildsGetRequest object.

  Fields:
    id: The ID of the build.
    projectId: The ID of the project.
  """

  id = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)


class CloudbuildProjectsBuildsListRequest(_messages.Message):
  """A CloudbuildProjectsBuildsListRequest object.

  Fields:
    foremanId: If present only builds with the provided foreman id will be
      returned
    pageSize: Number of results to return in the list.
    pageToken: Token to provide to skip to a particular spot in the list.
    projectId: The ID of the project.
    repoName: If present, only builds from source repos with the given name
      will be returned.
    revisionId: If present, only builds from source repos, from the given
      revision ID will be returned. A revision ID may be either a branch/tag
      name (e.g., "master") or a commit SHA.  If a revision ID is specified, a
      repo_name must also be specified.
  """

  foremanId = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  projectId = _messages.StringField(4, required=True)
  repoName = _messages.StringField(5)
  revisionId = _messages.StringField(6)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class GerritSourceContext(_messages.Message):
  """A SourceContext referring to a Gerrit project.

  Fields:
    aliasName: The name of an alias (branch, tag, etc.).
    gerritProject: The full project name within the host. Projects may be
      nested, so "project/subproject" is a valid project name. The "repo name"
      is hostURI/project.
    hostUri: The URI of a running Gerrit instance.
    revisionId: A revision (commit) ID.
  """

  aliasName = _messages.StringField(1)
  gerritProject = _messages.StringField(2)
  hostUri = _messages.StringField(3)
  revisionId = _messages.StringField(4)


class GitSourceContext(_messages.Message):
  """A GitSourceContext denotes a particular revision in a third party Git
  repository (e.g. GitHub).

  Fields:
    revisionId: Git commit hash. required.
    url: Git repository URL.
  """

  revisionId = _messages.StringField(1)
  url = _messages.StringField(2)


class ListBuildsResponse(_messages.Message):
  """Response including listed builds.

  Fields:
    builds: Builds will be sorted by create_time, descending.
    nextPageToken: Token to receive the next page of results.
  """

  builds = _messages.MessageField('Build', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  """The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Operation(_messages.Message):
  """This resource represents a long-running operation that is the result of a
  network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If true, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping
      above, the `name` should have the format of
      `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @ype with
        type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    """The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @ype with
        type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a ResponseValue object.

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


class PiperDepotSourceContext(_messages.Message):
  """Source code in the Piper depot as of a certain change.

  Fields:
    branchName: Specifies that the source context refers to a branch, rather
      than the depot root.  For example, if the branch files live under
      //depot/branches/mybranch/25, then branch_name should be "mybranch/25".
    changeNumber: CL number. If zero, represents depot head.
    disableComponents: If false, use the released components as of the CL. If
      true, use true head.
    versionMap: The complete components state description. If present,
      disable_components is ignored.  Not all services accept arbitrary
      version map.  Services not supporting arbitrary version maps must emit
      an error if this field is set, instead of silently falling back on
      disable_components.  This is a serialized VersionMap from
      //devtools/components/proto/version_map.proto. We use bytes instead of
      the actual type to avoid having a file under //google depend on one
      outside of //google.
  """

  branchName = _messages.StringField(1)
  changeNumber = _messages.IntegerField(2)
  disableComponents = _messages.BooleanField(3)
  versionMap = _messages.BytesField(4)


class ProjectRepoId(_messages.Message):
  """Selects a repo using a Google Cloud Platform project ID (e.g. winged-
  cargo-31) and a repo name within that project.

  Fields:
    projectId: The ID of the project.
    repoName: The name of the repo. Leave empty for the default repo.
  """

  projectId = _messages.StringField(1)
  repoName = _messages.StringField(2)


class RepoId(_messages.Message):
  """A unique identifier for a cloud repo.

  Fields:
    projectRepoId: A combination of a project ID and a repo name.
    uid: A server-assigned, globally unique identifier.
  """

  projectRepoId = _messages.MessageField('ProjectRepoId', 1)
  uid = _messages.StringField(2)


class Results(_messages.Message):
  """Results describes the artifacts created by the build pipeline.

  Fields:
    images: The container images created by this build.
    revision: The revision of the source used for the workspace, if available.
  """

  images = _messages.MessageField('BuiltImage', 1, repeated=True)
  revision = _messages.StringField(2)


class Source(_messages.Message):
  """Source describes the location of source either in a source repository, or
  in an object in Google Cloud Storage.

  Fields:
    repoSource: If provided, get source from this location in source control.
    storageSource: If provided, get source from this location in in Google
      Cloud Storage.
  """

  repoSource = _messages.MessageField('SourceContext', 1)
  storageSource = _messages.MessageField('StorageSource', 2)


class SourceContext(_messages.Message):
  """A SourceContext is a reference to a tree of files. A SourceContext
  together with a path point to a unique revision of a single file or
  directory.

  Fields:
    citc: A SourceContext referring to a Citc client.
    cloudRepo: A SourceContext referring to a revision in a cloud repo.
    cloudWorkspace: A SourceContext referring to a snapshot in a cloud
      workspace.
    gerrit: A SourceContext referring to a Gerrit project.
    git: A SourceContext referring to any third party Git repo (e.g. GitHub).
    piper: A SourceContext referring to a CL in Piper.
  """

  citc = _messages.MessageField('CitcWorkspaceSourceContext', 1)
  cloudRepo = _messages.MessageField('CloudRepoSourceContext', 2)
  cloudWorkspace = _messages.MessageField('CloudWorkspaceSourceContext', 3)
  gerrit = _messages.MessageField('GerritSourceContext', 4)
  git = _messages.MessageField('GitSourceContext', 5)
  piper = _messages.MessageField('PiperDepotSourceContext', 6)


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
    trace: A tracing token of the form "token:<tokenid>" or "email:<ldap>" to
      include in api requests.
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


class Status(_messages.Message):
  """The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` which can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting purpose.  - Batch operations. If
  a client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There will be a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @ype with
        type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

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


class StorageSource(_messages.Message):
  """StorageSource describes the location of source in an archive file in
  Google Cloud Storage.

  Fields:
    bucket: Google Cloud Storage bucket containing source (see [Bucket Name
      Requirements](https://cloud.google.com/storage/docs/bucket-
      naming#requirements)).
    object: Google Cloud Storage object containing source.  This object must
      be an archive file (zip, tar, tar.gz) containing source to build.
  """

  bucket = _messages.StringField(1)
  object = _messages.StringField(2)


encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'cloudbuild')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'cloudbuild')
encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'cloudbuild')
