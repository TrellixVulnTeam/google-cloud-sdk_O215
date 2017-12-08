"""Generated message classes for cloudbuild version v1.

Builds container images in the cloud.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudbuild'


class Build(_messages.Message):
  """A build resource in the Container Builder API.  At a high level, a Build
  describes where to find source code, how to build it (for example, the
  builder image to run on the source), and what tag to apply to the built
  image when it is pushed to Google Container Registry.  Fields can include
  the following variables which will be expanded when the build is created:  -
  $PROJECT_ID: the project ID of the build. - $BUILD_ID: the autogenerated ID
  of the build. - $REPO_NAME: the source repository name specified by
  RepoSource. - $BRANCH_NAME: the branch name specified by RepoSource. -
  $TAG_NAME: the tag name specified by RepoSource. - $REVISION_ID or
  $COMMIT_SHA: the commit SHA specified by RepoSource or   resolved from the
  specified branch or tag.

  Enums:
    StatusValueValuesEnum: Status of the build. @OutputOnly

  Fields:
    buildTriggerId: The ID of the BuildTrigger that triggered this build, if
      it was triggered automatically. @OutputOnly
    createTime: Time at which the request to create the build was received.
      @OutputOnly
    finishTime: Time at which execution of the build was finished.  The
      difference between finish_time and start_time is the duration of the
      build's execution. @OutputOnly
    id: Unique identifier of the build. @OutputOnly
    images: A list of images to be pushed upon the successful completion of
      all build steps.  The images will be pushed using the builder service
      account's credentials.  The digests of the pushed images will be stored
      in the Build resource's results field.  If any of the images fail to be
      pushed, the build is marked FAILURE.
    logUrl: URL to logs for this build in Google Cloud Logging. @OutputOnly
    logsBucket: Google Cloud Storage bucket where logs should be written (see
      [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-
      naming#requirements)). Logs file names will be of the format
      `${logs_bucket}/log-${build_id}.txt`.
    options: Special options for this build.
    projectId: ID of the project. @OutputOnly.
    results: Results of the build. @OutputOnly
    source: Describes where to find the source files to build.
    sourceProvenance: A permanent fixed identifier for source. @OutputOnly
    startTime: Time at which execution of the build was started. @OutputOnly
    status: Status of the build. @OutputOnly
    statusDetail: Customer-readable message about the current status.
      @OutputOnly
    steps: Describes the operations to be performed on the workspace.
    timeout: Amount of time that this build should be allowed to run, to
      second granularity. If this amount of time elapses, work on the build
      will cease and the build status will be TIMEOUT.  Default time is ten
      minutes.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """Status of the build. @OutputOnly

    Values:
      STATUS_UNKNOWN: Status of the build is unknown.
      QUEUED: Build is queued; work has not yet begun.
      WORKING: Build is being executed.
      SUCCESS: Build finished successfully.
      FAILURE: Build failed to complete successfully.
      INTERNAL_ERROR: Build failed due to an internal cause.
      TIMEOUT: Build took longer than was allowed.
      CANCELLED: Build was canceled by a user.
    """
    STATUS_UNKNOWN = 0
    QUEUED = 1
    WORKING = 2
    SUCCESS = 3
    FAILURE = 4
    INTERNAL_ERROR = 5
    TIMEOUT = 6
    CANCELLED = 7

  buildTriggerId = _messages.StringField(1)
  createTime = _messages.StringField(2)
  finishTime = _messages.StringField(3)
  id = _messages.StringField(4)
  images = _messages.StringField(5, repeated=True)
  logUrl = _messages.StringField(6)
  logsBucket = _messages.StringField(7)
  options = _messages.MessageField('BuildOptions', 8)
  projectId = _messages.StringField(9)
  results = _messages.MessageField('Results', 10)
  source = _messages.MessageField('Source', 11)
  sourceProvenance = _messages.MessageField('SourceProvenance', 12)
  startTime = _messages.StringField(13)
  status = _messages.EnumField('StatusValueValuesEnum', 14)
  statusDetail = _messages.StringField(15)
  steps = _messages.MessageField('BuildStep', 16, repeated=True)
  timeout = _messages.StringField(17)


class BuildOperationMetadata(_messages.Message):
  """Metadata for build operations.

  Fields:
    build: The build that the operation is tracking.
  """

  build = _messages.MessageField('Build', 1)


class BuildOptions(_messages.Message):
  """Optional arguments to enable specific features of builds.

  Enums:
    RequestedVerifyOptionValueValuesEnum: Requested verifiability options.
    SourceProvenanceHashValueListEntryValuesEnum:

  Fields:
    requestedVerifyOption: Requested verifiability options.
    sourceProvenanceHash: Requested hash for SourceProvenance.
  """

  class RequestedVerifyOptionValueValuesEnum(_messages.Enum):
    """Requested verifiability options.

    Values:
      NOT_VERIFIED: Not a verifiable build. (default)
      VERIFIED: Verified build.
    """
    NOT_VERIFIED = 0
    VERIFIED = 1

  class SourceProvenanceHashValueListEntryValuesEnum(_messages.Enum):
    """SourceProvenanceHashValueListEntryValuesEnum enum type.

    Values:
      NONE: <no description>
      SHA256: <no description>
    """
    NONE = 0
    SHA256 = 1

  requestedVerifyOption = _messages.EnumField('RequestedVerifyOptionValueValuesEnum', 1)
  sourceProvenanceHash = _messages.EnumField('SourceProvenanceHashValueListEntryValuesEnum', 2, repeated=True)


class BuildStep(_messages.Message):
  """BuildStep describes a step to perform in the build pipeline.

  Fields:
    args: A list of arguments that will be presented to the step when it is
      started.  If the image used to run the step's container has an
      entrypoint, these args will be used as arguments to that entrypoint. If
      the image does not define an entrypoint, the first element in args will
      be used as the entrypoint, and the remainder will be used as arguments.
    dir: Working directory (relative to project source root) to use when
      running this operation's container.
    entrypoint: Optional entrypoint to be used instead of the build step
      image's default If unset, the image's default will be used.
    env: A list of environment variable definitions to be used when running a
      step.  The elements are of the form "KEY=VALUE" for the environment
      variable "KEY" being given the value "VALUE".
    id: Optional unique identifier for this build step, used in wait_for to
      reference this build step as a dependency.
    name: The name of the container image that will run this particular build
      step.  If the image is already available in the host's Docker daemon's
      cache, it will be run directly. If not, the host will attempt to pull
      the image first, using the builder service account's credentials if
      necessary.  The Docker daemon's cache will already have the latest
      versions of all of the officially supported build steps
      (https://github.com/GoogleCloudPlatform/cloud-builders). The Docker
      daemon will also have cached many of the layers for some popular images,
      like "ubuntu", "debian", but they will be refreshed at the time you
      attempt to use them.  If you built an image in a previous build step, it
      will be stored in the host's Docker daemon's cache and is available to
      use as the name for a later build step.
    waitFor: The ID(s) of the step(s) that this build step depends on. This
      build step will not start until all the build steps in wait_for have
      completed successfully. If wait_for is empty, this build step will start
      when all previous build steps in the Build.Steps list have completed
      successfully.
  """

  args = _messages.StringField(1, repeated=True)
  dir = _messages.StringField(2)
  entrypoint = _messages.StringField(3)
  env = _messages.StringField(4, repeated=True)
  id = _messages.StringField(5)
  name = _messages.StringField(6)
  waitFor = _messages.StringField(7, repeated=True)


class BuildTrigger(_messages.Message):
  """Configuration for an automated build in response to source repository
  changes.

  Fields:
    build: Contents of the build template.
    createTime: Time when the trigger was created.  @OutputOnly
    description: Human-readable description of this trigger.
    disabled: If true, the trigger will never result in a build.
    filename: Path, from the source root, to a file whose contents is used for
      the template.
    id: Unique identifier of the trigger.  @OutputOnly
    triggerTemplate: Template describing the types of source changes to
      trigger a build.  Branch and tag names in trigger templates are
      interpreted as regular expressions. Any branch or tag change that
      matches that regular expression will trigger a build.
  """

  build = _messages.MessageField('Build', 1)
  createTime = _messages.StringField(2)
  description = _messages.StringField(3)
  disabled = _messages.BooleanField(4)
  filename = _messages.StringField(5)
  id = _messages.StringField(6)
  triggerTemplate = _messages.MessageField('RepoSource', 7)


class BuiltImage(_messages.Message):
  """BuiltImage describes an image built by the pipeline.

  Fields:
    digest: Docker Registry 2.0 digest.
    name: Name used to push the container image to Google Container Registry,
      as presented to `docker push`.
  """

  digest = _messages.StringField(1)
  name = _messages.StringField(2)


class CancelBuildRequest(_messages.Message):
  """Request to cancel an ongoing build."""


class CancelOperationRequest(_messages.Message):
  """The request message for Operations.CancelOperation."""


class CloudbuildOperationsCancelRequest(_messages.Message):
  """A CloudbuildOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


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
    cancelBuildRequest: A CancelBuildRequest resource to be passed as the
      request body.
    id: ID of the build.
    projectId: ID of the project.
  """

  cancelBuildRequest = _messages.MessageField('CancelBuildRequest', 1)
  id = _messages.StringField(2, required=True)
  projectId = _messages.StringField(3, required=True)


class CloudbuildProjectsBuildsCreateRequest(_messages.Message):
  """A CloudbuildProjectsBuildsCreateRequest object.

  Fields:
    build: A Build resource to be passed as the request body.
    projectId: ID of the project.
  """

  build = _messages.MessageField('Build', 1)
  projectId = _messages.StringField(2, required=True)


class CloudbuildProjectsBuildsGetRequest(_messages.Message):
  """A CloudbuildProjectsBuildsGetRequest object.

  Fields:
    id: ID of the build.
    projectId: ID of the project.
  """

  id = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)


class CloudbuildProjectsBuildsListRequest(_messages.Message):
  """A CloudbuildProjectsBuildsListRequest object.

  Fields:
    filter: The raw filter text to constrain the results.
    pageSize: Number of results to return in the list.
    pageToken: Token to provide to skip to a particular spot in the list.
    projectId: ID of the project.
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  projectId = _messages.StringField(4, required=True)


class CloudbuildProjectsTriggersCreateRequest(_messages.Message):
  """A CloudbuildProjectsTriggersCreateRequest object.

  Fields:
    buildTrigger: A BuildTrigger resource to be passed as the request body.
    projectId: ID of the project for which to configure automatic builds.
  """

  buildTrigger = _messages.MessageField('BuildTrigger', 1)
  projectId = _messages.StringField(2, required=True)


class CloudbuildProjectsTriggersDeleteRequest(_messages.Message):
  """A CloudbuildProjectsTriggersDeleteRequest object.

  Fields:
    projectId: ID of the project that owns the trigger.
    triggerId: ID of the BuildTrigger to delete.
  """

  projectId = _messages.StringField(1, required=True)
  triggerId = _messages.StringField(2, required=True)


class CloudbuildProjectsTriggersGetRequest(_messages.Message):
  """A CloudbuildProjectsTriggersGetRequest object.

  Fields:
    projectId: ID of the project that owns the trigger.
    triggerId: ID of the BuildTrigger to get.
  """

  projectId = _messages.StringField(1, required=True)
  triggerId = _messages.StringField(2, required=True)


class CloudbuildProjectsTriggersListRequest(_messages.Message):
  """A CloudbuildProjectsTriggersListRequest object.

  Fields:
    projectId: ID of the project for which to list BuildTriggers.
  """

  projectId = _messages.StringField(1, required=True)


class CloudbuildProjectsTriggersPatchRequest(_messages.Message):
  """A CloudbuildProjectsTriggersPatchRequest object.

  Fields:
    buildTrigger: A BuildTrigger resource to be passed as the request body.
    projectId: ID of the project that owns the trigger.
    triggerId: ID of the BuildTrigger to update.
  """

  buildTrigger = _messages.MessageField('BuildTrigger', 1)
  projectId = _messages.StringField(2, required=True)
  triggerId = _messages.StringField(3, required=True)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class FileHashes(_messages.Message):
  """Container message for hashes of byte content of files, used in
  SourceProvenance messages to verify integrity of source input to the build.

  Fields:
    fileHash: Collection of file hashes.
  """

  fileHash = _messages.MessageField('Hash', 1, repeated=True)


class Hash(_messages.Message):
  """Container message for hash values.

  Enums:
    TypeValueValuesEnum: The type of hash that was performed.

  Fields:
    type: The type of hash that was performed.
    value: The hash value.
  """

  class TypeValueValuesEnum(_messages.Enum):
    """The type of hash that was performed.

    Values:
      NONE: No hash requested.
      SHA256: Use a sha256 hash.
    """
    NONE = 0
    SHA256 = 1

  type = _messages.EnumField('TypeValueValuesEnum', 1)
  value = _messages.BytesField(2)


class ListBuildTriggersResponse(_messages.Message):
  """Response containing existing BuildTriggers.

  Fields:
    triggers: BuildTriggers for the project, sorted by create_time descending.
  """

  triggers = _messages.MessageField('BuildTrigger', 1, repeated=True)


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
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
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
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
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
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
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


class RepoSource(_messages.Message):
  """RepoSource describes the location of the source in a Google Cloud Source
  Repository.

  Fields:
    branchName: Name of the branch to build.
    commitSha: Explicit commit SHA to build.
    projectId: ID of the project that owns the repo. If omitted, the project
      ID requesting the build is assumed.
    repoName: Name of the repo. If omitted, the name "default" is assumed.
    tagName: Name of the tag to build.
  """

  branchName = _messages.StringField(1)
  commitSha = _messages.StringField(2)
  projectId = _messages.StringField(3)
  repoName = _messages.StringField(4)
  tagName = _messages.StringField(5)


class Results(_messages.Message):
  """Results describes the artifacts created by the build pipeline.

  Fields:
    buildStepImages: List of build step digests, in order corresponding to
      build step indices.
    images: Images that were built as a part of the build.
  """

  buildStepImages = _messages.StringField(1, repeated=True)
  images = _messages.MessageField('BuiltImage', 2, repeated=True)


class Source(_messages.Message):
  """Source describes the location of the source in a supported storage
  service.

  Fields:
    repoSource: If provided, get source from this location in a Cloud Repo.
    storageSource: If provided, get the source from this location in in Google
      Cloud Storage.
  """

  repoSource = _messages.MessageField('RepoSource', 1)
  storageSource = _messages.MessageField('StorageSource', 2)


class SourceProvenance(_messages.Message):
  """Provenance of the source. Ways to find the original source, or verify
  that some source was used for this build.

  Messages:
    FileHashesValue: Hash(es) of the build source, which can be used to verify
      that the original source integrity was maintained in the build. Note
      that FileHashes will only be populated if BuildOptions has requested a
      SourceProvenanceHash.  The keys to this map are file paths used as build
      source and the values contain the hash values for those files.  If the
      build source came in a single package such as a gzipped tarfile
      (.tar.gz), the FileHash will be for the single path to that file.
      @OutputOnly

  Fields:
    fileHashes: Hash(es) of the build source, which can be used to verify that
      the original source integrity was maintained in the build. Note that
      FileHashes will only be populated if BuildOptions has requested a
      SourceProvenanceHash.  The keys to this map are file paths used as build
      source and the values contain the hash values for those files.  If the
      build source came in a single package such as a gzipped tarfile
      (.tar.gz), the FileHash will be for the single path to that file.
      @OutputOnly
    resolvedRepoSource: A copy of the build's source.repo_source, if exists,
      with any revisions resolved.
    resolvedStorageSource: A copy of the build's source.storage_source, if
      exists, with any generations resolved.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class FileHashesValue(_messages.Message):
    """Hash(es) of the build source, which can be used to verify that the
    original source integrity was maintained in the build. Note that
    FileHashes will only be populated if BuildOptions has requested a
    SourceProvenanceHash.  The keys to this map are file paths used as build
    source and the values contain the hash values for those files.  If the
    build source came in a single package such as a gzipped tarfile (.tar.gz),
    the FileHash will be for the single path to that file. @OutputOnly

    Messages:
      AdditionalProperty: An additional property for a FileHashesValue object.

    Fields:
      additionalProperties: Additional properties of type FileHashesValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a FileHashesValue object.

      Fields:
        key: Name of the additional property.
        value: A FileHashes attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('FileHashes', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  fileHashes = _messages.MessageField('FileHashesValue', 1)
  resolvedRepoSource = _messages.MessageField('RepoSource', 2)
  resolvedStorageSource = _messages.MessageField('StorageSource', 3)


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
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
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
  """StorageSource describes the location of the source in an archive file in
  Google Cloud Storage.

  Fields:
    bucket: Google Cloud Storage bucket containing source (see [Bucket Name
      Requirements](https://cloud.google.com/storage/docs/bucket-
      naming#requirements)).
    generation: Google Cloud Storage generation for the object. If the
      generation is omitted, the latest generation will be used.
    object: Google Cloud Storage object containing source.  This object must
      be a gzipped archive file (.tar.gz) containing source to build.
  """

  bucket = _messages.StringField(1)
  generation = _messages.IntegerField(2)
  object = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'cloudbuild')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'cloudbuild')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'cloudbuild')
