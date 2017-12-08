"""Generated message classes for clouddebugger version v2.

Lets you examine the stack and variables of your running application without
stopping or slowing it down.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudsdk.third_party.apitools.base.protorpclite import messages as _messages
from googlecloudsdk.third_party.apitools.base.py import encoding


package = 'clouddebugger'


class AliasContext(_messages.Message):
  """An alias to a repo revision.

  Enums:
    KindValueValuesEnum: The alias kind.

  Fields:
    kind: The alias kind.
    name: The alias name.
  """

  class KindValueValuesEnum(_messages.Enum):
    """The alias kind.

    Values:
      ANY: Do not use.
      FIXED: Git tag
      MOVABLE: Git branch
      OTHER: OTHER is used to specify non-standard aliases, those not of the
        kinds above. For example, if a Git repo has a ref named
        "refs/foo/bar", it is considered to be of kind OTHER.
    """
    ANY = 0
    FIXED = 1
    MOVABLE = 2
    OTHER = 3

  kind = _messages.EnumField('KindValueValuesEnum', 1)
  name = _messages.StringField(2)


class Breakpoint(_messages.Message):
  """Represents the breakpoint specification, status and results.

  Enums:
    ActionValueValuesEnum: Action that the agent should perform when the code
      at the breakpoint location is hit.
    LogLevelValueValuesEnum: Indicates the severity of the log. Only relevant
      when action is `LOG`.

  Messages:
    LabelsValue: A set of custom breakpoint properties, populated by the
      agent, to be displayed to the user.

  Fields:
    action: Action that the agent should perform when the code at the
      breakpoint location is hit.
    condition: Condition that triggers the breakpoint. The condition is a
      compound boolean expression composed using expressions in a programming
      language at the source location.
    createTime: Time this breakpoint was created by the server in seconds
      resolution.
    evaluatedExpressions: Values of evaluated expressions at breakpoint time.
      The evaluated expressions appear in exactly the same order they are
      listed in the `expressions` field. The `name` field holds the original
      expression text, the `value` or `members` field holds the result of the
      evaluated expression. If the expression cannot be evaluated, the
      `status` inside the `Variable` will indicate an error and contain the
      error text.
    expressions: List of read-only expressions to evaluate at the breakpoint
      location. The expressions are composed using expressions in the
      programming language at the source location. If the breakpoint action is
      `LOG`, the evaluated expressions are included in log statements.
    finalTime: Time this breakpoint was finalized as seen by the server in
      seconds resolution.
    id: Breakpoint identifier, unique in the scope of the debuggee.
    isFinalState: When true, indicates that this is a final result and the
      breakpoint state will not change from here on.
    labels: A set of custom breakpoint properties, populated by the agent, to
      be displayed to the user.
    location: Breakpoint source location.
    logLevel: Indicates the severity of the log. Only relevant when action is
      `LOG`.
    logMessageFormat: Only relevant when action is `LOG`. Defines the message
      to log when the breakpoint hits. The message may include parameter
      placeholders `$0`, `$1`, etc. These placeholders are replaced with the
      evaluated value of the appropriate expression. Expressions not
      referenced in `log_message_format` are not logged.  Example: `Message
      received, id = $0, count = $1` with `expressions` = `[ message.id,
      message.count ]`.
    stackFrames: The stack at breakpoint time.
    status: Breakpoint status.  The status includes an error flag and a human
      readable message. This field is usually unset. The message can be either
      informational or an error message. Regardless, clients should always
      display the text message back to the user.  Error status indicates
      complete failure of the breakpoint.  Example (non-final state): `Still
      loading symbols...`  Examples (final state):  *   `Invalid line number`
      referring to location *   `Field f not found in class C` referring to
      condition
    userEmail: E-mail address of the user that created this breakpoint
    variableTable: The `variable_table` exists to aid with computation, memory
      and network traffic optimization.  It enables storing a variable once
      and reference it from multiple variables, including variables stored in
      the `variable_table` itself. For example, the same `this` object, which
      may appear at many levels of the stack, can have all of its data stored
      once in this table.  The stack frame variables then would hold only a
      reference to it.  The variable `var_table_index` field is an index into
      this repeated field. The stored objects are nameless and get their name
      from the referencing variable. The effective variable is a merge of the
      referencing variable and the referenced variable.
  """

  class ActionValueValuesEnum(_messages.Enum):
    """Action that the agent should perform when the code at the breakpoint
    location is hit.

    Values:
      CAPTURE: Capture stack frame and variables and update the breakpoint.
        The data is only captured once. After that the breakpoint is set in a
        final state.
      LOG: Log each breakpoint hit. The breakpoint remains active until
        deleted or expired.
    """
    CAPTURE = 0
    LOG = 1

  class LogLevelValueValuesEnum(_messages.Enum):
    """Indicates the severity of the log. Only relevant when action is `LOG`.

    Values:
      INFO: Information log message.
      WARNING: Warning log message.
      ERROR: Error log message.
    """
    INFO = 0
    WARNING = 1
    ERROR = 2

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """A set of custom breakpoint properties, populated by the agent, to be
    displayed to the user.

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

  action = _messages.EnumField('ActionValueValuesEnum', 1)
  condition = _messages.StringField(2)
  createTime = _messages.StringField(3)
  evaluatedExpressions = _messages.MessageField('Variable', 4, repeated=True)
  expressions = _messages.StringField(5, repeated=True)
  finalTime = _messages.StringField(6)
  id = _messages.StringField(7)
  isFinalState = _messages.BooleanField(8)
  labels = _messages.MessageField('LabelsValue', 9)
  location = _messages.MessageField('SourceLocation', 10)
  logLevel = _messages.EnumField('LogLevelValueValuesEnum', 11)
  logMessageFormat = _messages.StringField(12)
  stackFrames = _messages.MessageField('StackFrame', 13, repeated=True)
  status = _messages.MessageField('StatusMessage', 14)
  userEmail = _messages.StringField(15)
  variableTable = _messages.MessageField('Variable', 16, repeated=True)


class CloudRepoSourceContext(_messages.Message):
  """A CloudRepoSourceContext denotes a particular revision in a cloud repo (a
  repo hosted by the Google Cloud Platform).

  Fields:
    aliasContext: An alias, which may be a branch or tag.
    aliasName: The name of an alias (branch, tag, etc.).
    repoId: The ID of the repo.
    revisionId: A revision ID.
  """

  aliasContext = _messages.MessageField('AliasContext', 1)
  aliasName = _messages.StringField(2)
  repoId = _messages.MessageField('RepoId', 3)
  revisionId = _messages.StringField(4)


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


class ClouddebuggerControllerDebuggeesBreakpointsListRequest(_messages.Message):
  """A ClouddebuggerControllerDebuggeesBreakpointsListRequest object.

  Fields:
    debuggeeId: Identifies the debuggee.
    successOnTimeout: If set to `true`, returns `google.rpc.Code.OK` status
      and sets the `wait_expired` response field to `true` when the server-
      selected timeout has expired (recommended).  If set to `false`, returns
      `google.rpc.Code.ABORTED` status when the server-selected timeout has
      expired (deprecated).
    waitToken: A wait token that, if specified, blocks the method call until
      the list of active breakpoints has changed, or a server selected timeout
      has expired.  The value should be set from the last returned response.
  """

  debuggeeId = _messages.StringField(1, required=True)
  successOnTimeout = _messages.BooleanField(2)
  waitToken = _messages.StringField(3)


class ClouddebuggerControllerDebuggeesBreakpointsUpdateRequest(_messages.Message):
  """A ClouddebuggerControllerDebuggeesBreakpointsUpdateRequest object.

  Fields:
    debuggeeId: Identifies the debuggee being debugged.
    id: Breakpoint identifier, unique in the scope of the debuggee.
    updateActiveBreakpointRequest: A UpdateActiveBreakpointRequest resource to
      be passed as the request body.
  """

  debuggeeId = _messages.StringField(1, required=True)
  id = _messages.StringField(2, required=True)
  updateActiveBreakpointRequest = _messages.MessageField('UpdateActiveBreakpointRequest', 3)


class ClouddebuggerDebuggerDebuggeesBreakpointsDeleteRequest(_messages.Message):
  """A ClouddebuggerDebuggerDebuggeesBreakpointsDeleteRequest object.

  Fields:
    breakpointId: ID of the breakpoint to delete.
    clientVersion: The client version making the call. Following:
      `domain/type/version` (e.g., `google.com/intellij/v1`).
    debuggeeId: ID of the debuggee whose breakpoint to delete.
  """

  breakpointId = _messages.StringField(1, required=True)
  clientVersion = _messages.StringField(2)
  debuggeeId = _messages.StringField(3, required=True)


class ClouddebuggerDebuggerDebuggeesBreakpointsGetRequest(_messages.Message):
  """A ClouddebuggerDebuggerDebuggeesBreakpointsGetRequest object.

  Fields:
    breakpointId: ID of the breakpoint to get.
    clientVersion: The client version making the call. Following:
      `domain/type/version` (e.g., `google.com/intellij/v1`).
    debuggeeId: ID of the debuggee whose breakpoint to get.
  """

  breakpointId = _messages.StringField(1, required=True)
  clientVersion = _messages.StringField(2)
  debuggeeId = _messages.StringField(3, required=True)


class ClouddebuggerDebuggerDebuggeesBreakpointsListRequest(_messages.Message):
  """A ClouddebuggerDebuggerDebuggeesBreakpointsListRequest object.

  Enums:
    ActionValueValueValuesEnum: Only breakpoints with the specified action
      will pass the filter.

  Fields:
    action_value: Only breakpoints with the specified action will pass the
      filter.
    clientVersion: The client version making the call. Following:
      `domain/type/version` (e.g., `google.com/intellij/v1`).
    debuggeeId: ID of the debuggee whose breakpoints to list.
    includeAllUsers: When set to `true`, the response includes the list of
      breakpoints set by any user. Otherwise, it includes only breakpoints set
      by the caller.
    includeInactive: When set to `true`, the response includes active and
      inactive breakpoints. Otherwise, it includes only active breakpoints.
    stripResults: When set to `true`, the response breakpoints are stripped of
      the results fields: `stack_frames`, `evaluated_expressions` and
      `variable_table`.
    waitToken: A wait token that, if specified, blocks the call until the
      breakpoints list has changed, or a server selected timeout has expired.
      The value should be set from the last response. The error code
      `google.rpc.Code.ABORTED` (RPC) is returned on wait timeout, which
      should be called again with the same `wait_token`.
  """

  class ActionValueValueValuesEnum(_messages.Enum):
    """Only breakpoints with the specified action will pass the filter.

    Values:
      CAPTURE: <no description>
      LOG: <no description>
    """
    CAPTURE = 0
    LOG = 1

  action_value = _messages.EnumField('ActionValueValueValuesEnum', 1)
  clientVersion = _messages.StringField(2)
  debuggeeId = _messages.StringField(3, required=True)
  includeAllUsers = _messages.BooleanField(4)
  includeInactive = _messages.BooleanField(5)
  stripResults = _messages.BooleanField(6)
  waitToken = _messages.StringField(7)


class ClouddebuggerDebuggerDebuggeesBreakpointsSetRequest(_messages.Message):
  """A ClouddebuggerDebuggerDebuggeesBreakpointsSetRequest object.

  Fields:
    breakpoint: A Breakpoint resource to be passed as the request body.
    clientVersion: The client version making the call. Following:
      `domain/type/version` (e.g., `google.com/intellij/v1`).
    debuggeeId: ID of the debuggee where the breakpoint is to be set.
  """

  breakpoint = _messages.MessageField('Breakpoint', 1)
  clientVersion = _messages.StringField(2)
  debuggeeId = _messages.StringField(3, required=True)


class ClouddebuggerDebuggerDebuggeesListRequest(_messages.Message):
  """A ClouddebuggerDebuggerDebuggeesListRequest object.

  Fields:
    clientVersion: The client version making the call. Following:
      `domain/type/version` (e.g., `google.com/intellij/v1`).
    includeInactive: When set to `true`, the result includes all debuggees.
      Otherwise, the result includes only debuggees that are active.
    project: Project number of a Google Cloud project whose debuggees to list.
  """

  clientVersion = _messages.StringField(1)
  includeInactive = _messages.BooleanField(2)
  project = _messages.StringField(3)


class Debuggee(_messages.Message):
  """Represents the application to debug. The application may include one or
  more replicated processes executing the same code. Each of these processes
  is attached with a debugger agent, carrying out the debugging commands. The
  agents attached to the same debuggee are identified by using exactly the
  same field values when registering.

  Messages:
    LabelsValue: A set of custom debuggee properties, populated by the agent,
      to be displayed to the user.

  Fields:
    agentVersion: Version ID of the agent release. The version ID is
      structured as following: `domain/type/vmajor.minor` (for example
      `google.com/gcp-java/v1.1`).
    description: Human readable description of the debuggee. Including a
      human-readable project name, environment name and version information is
      recommended.
    extSourceContexts: References to the locations and revisions of the source
      code used in the deployed application.  Contexts describing a remote
      repo related to the source code have a `category` label of
      `remote_repo`. Source snapshot source contexts have a `category` of
      `snapshot`.
    id: Unique identifier for the debuggee generated by the controller
      service.
    isDisabled: If set to `true`, indicates that the agent should disable
      itself and detach from the debuggee.
    isInactive: If set to `true`, indicates that the debuggee is considered as
      inactive by the Controller service.
    labels: A set of custom debuggee properties, populated by the agent, to be
      displayed to the user.
    project: Project the debuggee is associated with. Use the project number
      when registering a Google Cloud Platform project.
    sourceContexts: References to the locations and revisions of the source
      code used in the deployed application.  NOTE: This field is deprecated.
      Consumers should use `ext_source_contexts` if it is not empty. Debug
      agents should populate both this field and `ext_source_contexts`.
    status: Human readable message to be displayed to the user about this
      debuggee. Absence of this field indicates no status. The message can be
      either informational or an error status.
    uniquifier: Debuggee uniquifier within the project. Any string that
      identifies the application within the project can be used. Including
      environment and version or build IDs is recommended.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """A set of custom debuggee properties, populated by the agent, to be
    displayed to the user.

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

  agentVersion = _messages.StringField(1)
  description = _messages.StringField(2)
  extSourceContexts = _messages.MessageField('ExtendedSourceContext', 3, repeated=True)
  id = _messages.StringField(4)
  isDisabled = _messages.BooleanField(5)
  isInactive = _messages.BooleanField(6)
  labels = _messages.MessageField('LabelsValue', 7)
  project = _messages.StringField(8)
  sourceContexts = _messages.MessageField('SourceContext', 9, repeated=True)
  status = _messages.MessageField('StatusMessage', 10)
  uniquifier = _messages.StringField(11)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class ExtendedSourceContext(_messages.Message):
  """An ExtendedSourceContext is a SourceContext combined with additional
  details describing the context.

  Messages:
    LabelsValue: Labels with user defined metadata.

  Fields:
    context: Any source context.
    labels: Labels with user defined metadata.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """Labels with user defined metadata.

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

  context = _messages.MessageField('SourceContext', 1)
  labels = _messages.MessageField('LabelsValue', 2)


class FormatMessage(_messages.Message):
  """Represents a message with parameters.

  Fields:
    format: Format template for the message. The `format` uses placeholders
      `$0`, `$1`, etc. to reference parameters. `$$` can be used to denote the
      `$` character.  Examples:  *   `Failed to load '$0' which helps debug $1
      the first time it     is loaded.  Again, $0 is very important.` *
      `Please pay $$10 to use $0 instead of $1.`
    parameters: Optional parameters to be embedded into the message.
  """

  format = _messages.StringField(1)
  parameters = _messages.StringField(2, repeated=True)


class GerritSourceContext(_messages.Message):
  """A SourceContext referring to a Gerrit project.

  Fields:
    aliasContext: An alias, which may be a branch or tag.
    aliasName: The name of an alias (branch, tag, etc.).
    gerritProject: The full project name within the host. Projects may be
      nested, so "project/subproject" is a valid project name. The "repo name"
      is hostURI/project.
    hostUri: The URI of a running Gerrit instance.
    revisionId: A revision (commit) ID.
  """

  aliasContext = _messages.MessageField('AliasContext', 1)
  aliasName = _messages.StringField(2)
  gerritProject = _messages.StringField(3)
  hostUri = _messages.StringField(4)
  revisionId = _messages.StringField(5)


class GetBreakpointResponse(_messages.Message):
  """Response for getting breakpoint information.

  Fields:
    breakpoint: Complete breakpoint state. The fields `id` and `location` are
      guaranteed to be set.
  """

  breakpoint = _messages.MessageField('Breakpoint', 1)


class GitSourceContext(_messages.Message):
  """A GitSourceContext denotes a particular revision in a third party Git
  repository (e.g. GitHub).

  Fields:
    revisionId: Git commit hash. required.
    url: Git repository URL.
  """

  revisionId = _messages.StringField(1)
  url = _messages.StringField(2)


class ListActiveBreakpointsResponse(_messages.Message):
  """Response for listing active breakpoints.

  Fields:
    breakpoints: List of all active breakpoints. The fields `id` and
      `location` are guaranteed to be set on each breakpoint.
    nextWaitToken: A wait token that can be used in the next method call to
      block until the list of breakpoints changes.
    waitExpired: The `wait_expired` field is set to true by the server when
      the request times out and the field `success_on_timeout` is set to true.
  """

  breakpoints = _messages.MessageField('Breakpoint', 1, repeated=True)
  nextWaitToken = _messages.StringField(2)
  waitExpired = _messages.BooleanField(3)


class ListBreakpointsResponse(_messages.Message):
  """Response for listing breakpoints.

  Fields:
    breakpoints: List of all breakpoints with complete state. The fields `id`
      and `location` are guaranteed to be set on each breakpoint.
    nextWaitToken: A wait token that can be used in the next call to `list`
      (REST) or `ListBreakpoints` (RPC) to block until the list of breakpoints
      has changes.
  """

  breakpoints = _messages.MessageField('Breakpoint', 1, repeated=True)
  nextWaitToken = _messages.StringField(2)


class ListDebuggeesResponse(_messages.Message):
  """Response for listing debuggees.

  Fields:
    debuggees: List of debuggees accessible to the calling user. Note that the
      `description` field is the only human readable field that should be
      displayed to the user. The fields `debuggee.id` and  `description`
      fields are guaranteed to be set on each debuggee.
  """

  debuggees = _messages.MessageField('Debuggee', 1, repeated=True)


class ProjectRepoId(_messages.Message):
  """Selects a repo using a Google Cloud Platform project ID (e.g. winged-
  cargo-31) and a repo name within that project.

  Fields:
    projectId: The ID of the project.
    repoName: The name of the repo. Leave empty for the default repo.
  """

  projectId = _messages.StringField(1)
  repoName = _messages.StringField(2)


class RegisterDebuggeeRequest(_messages.Message):
  """Request to register a debuggee.

  Fields:
    debuggee: Debuggee information to register. The fields `project`,
      `uniquifier`, `description` and `agent_version` of the debuggee must be
      set.
  """

  debuggee = _messages.MessageField('Debuggee', 1)


class RegisterDebuggeeResponse(_messages.Message):
  """Response for registering a debuggee.

  Fields:
    debuggee: Debuggee resource. The field `id` is guranteed to be set (in
      addition to the echoed fields).
  """

  debuggee = _messages.MessageField('Debuggee', 1)


class RepoId(_messages.Message):
  """A unique identifier for a cloud repo.

  Fields:
    projectRepoId: A combination of a project ID and a repo name.
    uid: A server-assigned, globally unique identifier.
  """

  projectRepoId = _messages.MessageField('ProjectRepoId', 1)
  uid = _messages.StringField(2)


class SetBreakpointResponse(_messages.Message):
  """Response for setting a breakpoint.

  Fields:
    breakpoint: Breakpoint resource. The field `id` is guaranteed to be set
      (in addition to the echoed fileds).
  """

  breakpoint = _messages.MessageField('Breakpoint', 1)


class SourceContext(_messages.Message):
  """A SourceContext is a reference to a tree of files. A SourceContext
  together with a path point to a unique revision of a single file or
  directory.

  Fields:
    cloudRepo: A SourceContext referring to a revision in a cloud repo.
    cloudWorkspace: A SourceContext referring to a snapshot in a cloud
      workspace.
    gerrit: A SourceContext referring to a Gerrit project.
    git: A SourceContext referring to any third party Git repo (e.g. GitHub).
  """

  cloudRepo = _messages.MessageField('CloudRepoSourceContext', 1)
  cloudWorkspace = _messages.MessageField('CloudWorkspaceSourceContext', 2)
  gerrit = _messages.MessageField('GerritSourceContext', 3)
  git = _messages.MessageField('GitSourceContext', 4)


class SourceLocation(_messages.Message):
  """Represents a location in the source code.

  Fields:
    line: Line inside the file. The first line in the file has the value `1`.
    path: Path to the source file within the source context of the target
      binary.
  """

  line = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  path = _messages.StringField(2)


class StackFrame(_messages.Message):
  """Represents a stack frame context.

  Fields:
    arguments: Set of arguments passed to this function. Note that this might
      not be populated for all stack frames.
    function: Demangled function name at the call site.
    locals: Set of local variables at the stack frame location. Note that this
      might not be populated for all stack frames.
    location: Source location of the call site.
  """

  arguments = _messages.MessageField('Variable', 1, repeated=True)
  function = _messages.StringField(2)
  locals = _messages.MessageField('Variable', 3, repeated=True)
  location = _messages.MessageField('SourceLocation', 4)


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


class StatusMessage(_messages.Message):
  """Represents a contextual status message. The message can indicate an error
  or informational status, and refer to specific parts of the containing
  object. For example, the `Breakpoint.status` field can indicate an error
  referring to the `BREAKPOINT_SOURCE_LOCATION` with the message `Location not
  found`.

  Enums:
    RefersToValueValuesEnum: Reference to which the message applies.

  Fields:
    description: Status message text.
    isError: Distinguishes errors from informational messages.
    refersTo: Reference to which the message applies.
  """

  class RefersToValueValuesEnum(_messages.Enum):
    """Reference to which the message applies.

    Values:
      UNSPECIFIED: Status doesn't refer to any particular input.
      BREAKPOINT_SOURCE_LOCATION: Status applies to the breakpoint and is
        related to its location.
      BREAKPOINT_CONDITION: Status applies to the breakpoint and is related to
        its condition.
      BREAKPOINT_EXPRESSION: Status applies to the breakpoint and is related
        to its expressions.
      VARIABLE_NAME: Status applies to the entire variable.
      VARIABLE_VALUE: Status applies to variable value (variable name is
        valid).
    """
    UNSPECIFIED = 0
    BREAKPOINT_SOURCE_LOCATION = 1
    BREAKPOINT_CONDITION = 2
    BREAKPOINT_EXPRESSION = 3
    VARIABLE_NAME = 4
    VARIABLE_VALUE = 5

  description = _messages.MessageField('FormatMessage', 1)
  isError = _messages.BooleanField(2)
  refersTo = _messages.EnumField('RefersToValueValuesEnum', 3)


class UpdateActiveBreakpointRequest(_messages.Message):
  """Request to update an active breakpoint.

  Fields:
    breakpoint: Updated breakpoint information. The field 'id' must be set.
  """

  breakpoint = _messages.MessageField('Breakpoint', 1)


class UpdateActiveBreakpointResponse(_messages.Message):
  """Response for updating an active breakpoint. The message is defined to
  allow future extensions.
  """



class Variable(_messages.Message):
  """Represents a variable or an argument possibly of a compound object type.
  Note how the following variables are represented:  1) A simple variable:
  int x = 5      { name: "x", value: "5", type: "int" }  // Captured variable
  2) A compound object:      struct T {         int m1;         int m2;     };
  T x = { 3, 7 };      {  // Captured variable         name: "x",
  type: "T",         members { name: "m1", value: "3", type: "int" },
  members { name: "m2", value: "7", type: "int" }     }  3) A pointer where
  the pointee was captured:      T x = { 3, 7 };     T* p = &x;      {   //
  Captured variable         name: "p",         type: "T*",         value:
  "0x00500500",         members { name: "m1", value: "3", type: "int" },
  members { name: "m2", value: "7", type: "int" }     }  4) A pointer where
  the pointee was not captured:      T* p = new T;      {   // Captured
  variable         name: "p",         type: "T*",         value: "0x00400400"
  status { is_error: true, description { format: "unavailable" } }     }  The
  status should describe the reason for the missing value, such as `<optimized
  out>`, `<inaccessible>`, `<pointers limit reached>`.  Note that a null
  pointer should not have members.  5) An unnamed value:      int* p = new
  int(7);      {   // Captured variable         name: "p",         value:
  "0x00500500",         type: "int*",         members { value: "7", type:
  "int" } }  6) An unnamed pointer where the pointee was not captured:
  int* p = new int(7);     int** pp = &p;      {  // Captured variable
  name: "pp",         value: "0x00500500",         type: "int**",
  members {             value: "0x00400400",             type: "int*"
  status {                 is_error: true,                 description: {
  format: "unavailable" } }             }         }     }  To optimize
  computation, memory and network traffic, variables that repeat in the output
  multiple times can be stored once in a shared variable table and be
  referenced using the `var_table_index` field.  The variables stored in the
  shared table are nameless and are essentially a partition of the complete
  variable. To reconstruct the complete variable, merge the referencing
  variable with the referenced variable.  When using the shared variable
  table, the following variables:      T x = { 3, 7 };     T* p = &x;     T& r
  = x;      { name: "x", var_table_index: 3, type: "T" }  // Captured
  variables     { name: "p", value "0x00500500", type="T*", var_table_index: 3
  }     { name: "r", type="T&", var_table_index: 3 }      {  // Shared
  variable table entry #3:         members { name: "m1", value: "3", type:
  "int" },         members { name: "m2", value: "7", type: "int" }     }  Note
  that the pointer address is stored with the referencing variable and not
  with the referenced variable. This allows the referenced variable to be
  shared between pointers and references.  The type field is optional. The
  debugger agent may or may not support it.

  Fields:
    members: Members contained or pointed to by the variable.
    name: Name of the variable, if any.
    status: Status associated with the variable. This field will usually stay
      unset. A status of a single variable only applies to that variable or
      expression. The rest of breakpoint data still remains valid. Variables
      might be reported in error state even when breakpoint is not in final
      state.  The message may refer to variable name with `refers_to` set to
      `VARIABLE_NAME`. Alternatively `refers_to` will be set to
      `VARIABLE_VALUE`. In either case variable value and members will be
      unset.  Example of error message applied to name: `Invalid expression
      syntax`.  Example of information message applied to value: `Not
      captured`.  Examples of error message applied to value:  *   `Malformed
      string`, *   `Field f not found in class C` *   `Null pointer
      dereference`
    type: Variable type (e.g. `MyClass`). If the variable is split with
      `var_table_index`, `type` goes next to `value`. The interpretation of a
      type is agent specific. It is recommended to include the dynamic type
      rather than a static type of an object.
    value: Simple value of the variable.
    varTableIndex: Reference to a variable in the shared variable table. More
      than one variable can reference the same variable in the table. The
      `var_table_index` field is an index into `variable_table` in Breakpoint.
  """

  members = _messages.MessageField('Variable', 1, repeated=True)
  name = _messages.StringField(2)
  status = _messages.MessageField('StatusMessage', 3)
  type = _messages.StringField(4)
  value = _messages.StringField(5)
  varTableIndex = _messages.IntegerField(6, variant=_messages.Variant.INT32)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'clouddebugger')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'clouddebugger')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'clouddebugger')
