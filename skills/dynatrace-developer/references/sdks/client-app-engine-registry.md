# @dynatrace-sdk/client-app-engine-registry

Source: <https://developer.dynatrace.com/develop/sdks/client-app-engine-registry/v3/> (latest: `client-app-engine-registry/v3`).

## client-app-engine-registry/v3

`/develop/sdks/client-app-engine-registry/v3/`

- SDK for TypeScript
- AppEngine - Registry
- V3

## AppEngine - Registry
The Registry is mainly responsible for

- installing / updating / storing apps

- uninstalling / removing apps

- getting apps

#### Asynchronous behavior

Both the install and the uninstall process are performed asynchronously. The Registry persists
the app bundle and defines the desired state of the app (e.g. installed, uninstalled). The
installation / uninstallation process is then handled asynchronously by a separate service.

The current status of the app is provided by the status in the response body of the
respective GET request, e.g. `/apps/{id}`.

 @dynatrace-sdk/client-app-engine-registry v3.3.1 

`tsx
npm install @dynatrace-sdk/client-app-engine-registry
`

### appEngineRegistryAppsClient

`tsx
import { appEngineRegistryAppsClient } from '@dynatrace-sdk/client-app-engine-registry';
`

#### getApp

appEngineRegistryAppsClient.getApp(config): PromiseAppInfo>Get an installed appRequired scope: app-engine:apps:runDuring an app update, when a current version and a new version exists, the current one is returned.

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | string | Comma-separated list of field names that are added to the default set of fields.

 You can include the following additional fields:

- `resourceContext`
- `resourceStatus.subResourceTypes`
- `resourceStatus.subResourceStatuses`
- `manifest`
- any top-level manifest field to include a part of the manifest, for example, `manifest.scopes` or `manifest.intents`
- `isBuiltin`
- `isolatedUri`
- `deactivationReasons`
 | config.id*required | string | The unique identifier for the app
 | config.latestAppVersion | boolean | If `true`, the latest version of the app is returned.

 If `false`, the current version of the app is returned.

 This is relevant while an app is being updated. During this time typically two versions of the same app exist, the current version and the latest version with `status=PENDING`.

##### Returns
 |
 | Return type | Status code | Description
 | AppInfo | 200 | OK

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { appEngineRegistryAppsClient } from "@dynatrace-sdk/client-app-engine-registry";const data = await appEngineRegistryAppsClient.getApp({ id: "...",});
`

#### getApps

appEngineRegistryAppsClient.getApps(config): PromiseAppInfoList>List all installed apps.Required scope: app-engine:apps:run

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | string | Comma-separated list of field names that are added to the default set of fields.

 You can include the following additional fields:

- `resourceContext`
- `resourceStatus.subResourceTypes`
- `resourceStatus.subResourceStatuses`
- `manifest`
- any top-level manifest field to include a part of the manifest, for example, `manifest.scopes` or `manifest.intents`
- `isBuiltin`
- `isolatedUri`
- `deactivationReasons`
 | config.filter | string | The filter parameter, as explained here.

 Filtering is supported on the following fields:

- `id`
- `resourceStatus.subResourceTypes`
- top-level manifest fields, for example `manifest.description` or `manifest.version` Examples:
- `id = 'my.custom-app'`
- `id contains 'custom'`
- `id starts-with 'my.'`
- `not(id starts-with 'my.')`
- `id in ('my.custom-app', 'my.other-custom-app')`
- `resourceStatus.subResourceTypes contains 'DOCUMENTS'`
- `resourceStatus.subResourceTypes contains 'DOCUMENTS' or resourceStatus.subResourceTypes contains 'FUNCTIONS'`
- `not (id starts-with 'dynatrace.classic.')` (to exclude classic apps)
- `not (manifest.document-types is-empty)`
- `manifest.document-types contains 'Notebook'` (to filter the json content of the top-level manifest field `document-types` for apps that provide the `Notebook` document type) If this parameter is omitted, all apps will be returned.

 The maximum nesting depth (via parentheses) is 3. The maximum expression length is 256 characters.

 Fields that are used for filtering are always included in the response, even if they are not in the default set of fields.
 | config.includeAllAppVersions | boolean | If `true`, all versions of every app are included in the response.

 If `false`, only the current version of every app is included.

 This is relevant while an app is being updated. During this time typically two versions of the same app exist, the current version and the latest version with `status=PENDING`.
 | config.includeDeactivated | boolean | If `true`, apps that are `DEACTIVATED` are included in the response.
 | config.includeNonRunnable | boolean | If `true`, apps that the user is not allowed to run because of missing permissions are included in the response.

##### Returns
 |
 | Return type | Status code | Description
 | AppInfoList | 200 | OK

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { appEngineRegistryAppsClient } from "@dynatrace-sdk/client-app-engine-registry";const data = await appEngineRegistryAppsClient.getApps();
`

#### installApp

appEngineRegistryAppsClient.installApp(config): PromiseAppStub>Install or update an app.Required scope: app-engine:apps:installAn app ID always starts with a namespace and a dot, e.g. `dynatrace.` for Dynatrace apps. Custom apps can be installed in the `my` namespace, e.g. `my.first-app`.The zipped app bundle has to be provided via the request body

##### Parameters
 |
 | Name | Type
 | config.body*required | Blob

##### Returns
 |
 | Return type | Status code | Description
 | AppStub | 202 | Accepted; new app will be installed/updated

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Bad Request | Client side error. | Server side error.Code example
`tsx
import { appEngineRegistryAppsClient } from "@dynatrace-sdk/client-app-engine-registry";const data = await appEngineRegistryAppsClient.installApp({ body: new Blob(),});
`

#### searchActions

appEngineRegistryAppsClient.searchActions(config): PromiseSearchAppActionList>Search actions of installed apps.Required scope: app-engine:apps:run

##### Parameters
 |
 | Name | Type | Description
 | config.query | string | A whitespace separated list of search terms. For an action to match, each search term must be contained in either: app name, app description, action name or action description.

 Search terms are case insensitive and each additional search term restricts actions further. Maximum length is 256 characters.

##### Returns
 |
 | Return type | Status code | Description
 | SearchAppActionList | 200 | OK

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { appEngineRegistryAppsClient } from "@dynatrace-sdk/client-app-engine-registry";const data = await appEngineRegistryAppsClient.searchActions();
`

#### uninstallApp

appEngineRegistryAppsClient.uninstallApp(config): PromiseUninstall an app.Required scope: app-engine:apps:delete

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | The unique identifier for the app

##### Returns
 |
 | Return type | Status code | Description
 | void | 202 | Accepted; app will be uninstalled

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { appEngineRegistryAppsClient } from "@dynatrace-sdk/client-app-engine-registry";const data = await appEngineRegistryAppsClient.uninstallApp( { id: "..." },);
`

### appEngineRegistrySchemaManifestClient

`tsx
import { appEngineRegistrySchemaManifestClient } from '@dynatrace-sdk/client-app-engine-registry';
`

#### getAppManifestSchema

appEngineRegistrySchemaManifestClient.getAppManifestSchema(config): Promisestring | any>>Get JSON schema for app manifests

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | OK

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { appEngineRegistrySchemaManifestClient } from "@dynatrace-sdk/client-app-engine-registry";const data = await appEngineRegistrySchemaManifestClient.getAppManifestSchema();
`

#### getDefaultCspProperties

appEngineRegistrySchemaManifestClient.getDefaultCspProperties(config): PromiseAppDefaultCsp>Get default CSP rules for apps

##### Returns
 |
 | Return type | Status code | Description
 | AppDefaultCsp | 200 | OK

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { appEngineRegistrySchemaManifestClient } from "@dynatrace-sdk/client-app-engine-registry";const data = await appEngineRegistrySchemaManifestClient.getDefaultCspProperties();
`

### Types

#### AppDefaultCsp

Default Content Security Policies for apps.

 |
 | Name | Type | Description
 | policyDirectives*required | AppDefaultCspPolicyDirectives | The policy directives

#### AppDefaultCspPolicyDirectives

The policy directives

type: Record

#### AppIcon

Representation of an app icon.

 |
 | Name | Type | Description
 | href*required | string | The reference to an app icon

#### AppInfo

A minimal representation of an app.

 |
 | Name | Type | Description
 | appIcon | AppIcon | Representation of an app icon.
 | deactivationReasons | Array | Contains the reasons if the app has the status `DEACTIVATED`
 | description*required | string | The description of the app
 | id*required | string | The id of the app
 | isBuiltin | boolean | Whether this is a built-in app or not. Built-in apps are provided by Dynatrace and installed on every environment.
 | isolatedUri | AppIsolatedUri | Representation of an app's isolated uri.
 | manifest | AppInfoManifest | The manifest of the app
 | modificationInfo*required | ModificationInfo | Modification information about the app
 | name*required | string | The name of the app
 | resourceContext | ResourceContext | Additional resource context information
 | resourceStatus*required | ResourceStatus | The status of the app plus additional details.
 | signatureInfo*required | AppSignatureInfo | Representation of an app's signature verification.
 | version*required | string | The version of the app

#### AppInfoList

A list of minimal app representations.

 |
 | Name | Type | Description
 | apps*required | ArrayAppInfo> | The list of minimal app representations.

#### AppIsolatedUri

Representation of an app's isolated uri.

 |
 | Name | Type | Description
 | baseUrl*required | string | The base URL of an app
 | url*required | string | The URL of an app
 | widgetUrl*required | string | The base URL for widgets of an app

#### AppSignatureInfo

Representation of an app's signature verification.

 |
 | Name | Type | Description
 | publisher | string | The organization name of the app publisher.
 | signed*required | boolean | App is signed and its signature has been verified.

#### AppStub

A minimal representation of an installed/updated app.

 |
 | Name | Type | Description
 | id*required | string | Id of the installed/updated app
 | warnings | ArrayWarning> | Contains warning information although the request was successful

#### ConstraintViolation

Contains information about a constraint violation caused by invalid input.

 |
 | Name | Type | Description
 | errorCode | "DependencyVersionIncompatible" | "DependencyUnknown" | An optional error code that contains more detailed error information.

 Possible error codes:

- `DependencyVersionIncompatible`: The app's manifest contains a dependency with an incompatible version.
- `DependencyUnknown`: The app's manifest contains a dependency that is unknown.
 | errorCodeProperties | ConstraintViolationErrorCodeProperties | Additional properties related to the provided error code.
 | message*required | string | The error message
 | path*required | string | The path of the property that caused the constraint violation

#### ConstraintViolationErrorCodeProperties

Additional properties related to the provided error code.

 |
 | Name | Type | Description
 | availableVersion | string | The version that is available. This value is present if the error code is `DependencyVersionIncompatible`.
 | dependency | string | The name of the dependency. This value is present if the error code is `DependencyUnknown` or `DependencyVersionIncompatible`.
 | incompatibleVersion | string | The version that is incompatible. This value is present if the error code is `DependencyVersionIncompatible`.

#### Error

Contains information for 4xx and 5xx errors.

 |
 | Name | Type | Description
 | code*required | number | The HTTP status code
 | details | ErrorDetails | Contains details for 4xx and 5xx errors.
 | help | string | Additional information related to the error
 | message*required | string | The error message
 | retryAfterSeconds | number | Seconds to wait until the next retry

#### ErrorDetails

Contains details for 4xx and 5xx errors.

 |
 | Name | Type | Description
 | constraintViolations | ArrayConstraintViolation> | A list of constraint violations
 | errorCode | "MaxNumberOfInstalledAppsExceeded" | An optional error code that contains more detailed error information than the HTTP response code alone.

 Possible error codes:

- `MaxNumberOfInstalledAppsExceeded`: The app bundle couldn't be uploaded because the max number of apps was exceeded. Learn more: https://dt-url.net/upgrade-license
 | errorCodeProperties | ErrorDetailsErrorCodeProperties | Additional properties related to the provided error code
 | errorRef | string | Generated unique value for 5xx errors.
 | traceId | string | OpenTelemetry trace id of the trace where error occurs.

#### ErrorDetailsErrorCodeProperties

Additional properties related to the provided error code

 |
 | Name | Type | Description
 | appLimit | string | Limit for number of installed apps in an environment. This value is present if the error code is `MaxNumberOfInstalledAppsExceeded'.

#### ErrorEnvelope

Error response for all 4xx and 5xx errors.

 |
 | Name | Type | Description
 | error*required | Error | Contains information for 4xx and 5xx errors.

#### ModificationInfo

Modification information about the app

 |
 | Name | Type | Description
 | createdAt*required | string | Timestamp when the resource was created in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSS'Z')
 | createdBy*required | string | UserId of the user that created the resource
 | lastModifiedAt*required | string | Timestamp when the resource was last modified in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSS'Z')
 | lastModifiedBy*required | string | UserId of the user that last modified the resource

#### ResourceContext

Additional resource context information

 |
 | Name | Type | Description
 | operations*required | Array | Operations that are allowed on the app depending on the user's permissions.

- `run`: user is allowed to run the app.

- `update`: user is allowed to update the app.

- `uninstall`: user is allowed to uninstall the app.

#### ResourceStatus

The status of the app plus additional details.

 |
 | Name | Type | Description
 | operationStateBeforeError | "OK" | "PENDING_INSTALL" | "PENDING_UPDATE" | "PENDING_DELETE" | Details about the state when an error occurred. Only present if the app's `status` is `ERROR`.

- `PENDING_INSTALL`: The error occurred while installing the app.

- `PENDING_UPDATE`: The error occurred while updating the app.

- `PENDING_DELETE`: The error occurred while deleting the app.

- `OK`: At least one sub resource failed while the app was already running.

 | pendingOperation | "INSTALL" | "UPDATE" | "DELETE" | The pending operation of the app. Only present if the app's `status` is `PENDING`.

- `INSTALL`: The app is currently being installed.

- `UPDATE`: The app is currently being updated.

- `DELETE`: The app is currently being deleted.

 | status*required | "OK" | "PENDING" | "PENDING_DELETION" | "DEACTIVATED" | "ERROR" | The status of the app.

- `OK`: The app is fully installed and running.

- `PENDING`: The app is currently being installed, updated or deleted.

- `PENDING_DELETION`: A new version of the app was successfully installed and this version is scheduled for deletion.

- `DEACTIVATED`: The app is deactivated and cannot be executed.

- `ERROR`: The app failed with an error.

 | subResourceStatuses | ArraySubResourceStatus> | The statuses of the app's sub resources.
 | subResourceTypes | Array | The sub resource types that the app contains.

#### SearchAppAction

 |
 | Name | Type | Description
 | actions*required | Array | List of app actions. Actions are sorted by name in ascending order. Actions without name are last.
 | id*required | string | App id
 | name*required | string | App name

#### SearchAppActionList

 |
 | Name | Type | Description
 | apps*required | ArraySearchAppAction> | List of apps with actions. Apps are sorted by name in ascending order.
 | totalCount*required | number | Total actions count.

#### SubResourceConstraintViolation

Contains information about a constraint violation caused by invalid input.

 |
 | Name | Type | Description
 | message*required | string | The error message
 | path | string | The path of the property that caused the constraint violation

#### SubResourceError

Additional error information that can be present if the sub resource `status` is `FAILED`

 |
 | Name | Type | Description
 | constraintViolations | ArraySubResourceConstraintViolation> | A list of constraint violations
 | errorCode | string | An error code that can be used determine the nature of an error and why it occurred.
 | errorRef | string | Optional generated unique value to reference this error.
 | message*required | string | The error message.

#### SubResourceStatus

The status of the sub resource.

 |
 | Name | Type | Description
 | error | SubResourceError | Additional error information that can be present if the sub resource `status` is `FAILED`
 | status*required | "SCHEDULED" | "DEPLOYING" | "DEPLOYED" | "FAILED" | "NO_RESOURCES" | The deployment status of the app's sub resource:

- `SCHEDULED`: Only the uploaded app bundle is persisted.

- `DEPLOYING`: The app's sub resources are currently being deployed.

- `DEPLOYED`: The app's sub resources were successfully deployed.

- `FAILED`: The deployment of the app's sub resources failed.

- `NO_RESOURCES`: The app bundle does not contain any sub resources of this type

 | subResourceType*required | "FUNCTIONS" | "FILES" | "SETTINGS_SCHEMAS" | "DOCUMENTS" | The sub resource type.

- `FUNCTIONS`: app functions.

- `FILES`: static files of an app.

- `SETTINGS_SCHEMAS`: settings schemas of an app.

- `DOCUMENTS`: documents, e.g. templates, that are part of an app bundle.

#### Warning

A warning.

 |
 | Name | Type | Description
 | message | string | The warning message.

### Enums

#### ConstraintViolationErrorCode

⚠️ Deprecated
Use literal values.

An optional error code that contains more detailed error information.Possible error codes:

- `DependencyVersionIncompatible`: The app's manifest contains a dependency with an incompatible version.

- `DependencyUnknown`: The app's manifest contains a dependency that is unknown.

##### Enum keys
`DependencyUnknown` | `DependencyVersionIncompatible`

#### DeactivationReason

⚠️ Deprecated
Use literal values.

Possible reasons why app has deactivated status

##### Enum keys
`AppCertificateRevoked` | `CapabilityAppEngineFunctionsSmallDisabled`

#### DeploymentStatus

⚠️ Deprecated
Use literal values.

The deployment status of the app's sub resource:

`SCHEDULED`: Only the uploaded app bundle is persisted.

`DEPLOYING`: The app's sub resources are currently being deployed.

`DEPLOYED`: The app's sub resources were successfully deployed.

`FAILED`: The deployment of the app's sub resources failed.

`NO_RESOURCES`: The app bundle does not contain any sub resources of this type

##### Enum keys
`Deployed` | `Deploying` | `Failed` | `NoResources` | `Scheduled`

#### ErrorDetailsErrorCode

⚠️ Deprecated
Use literal values.

An optional error code that contains more detailed error information than the HTTP response code alone.Possible error codes:

- `MaxNumberOfInstalledAppsExceeded`: The app bundle couldn't be uploaded because the max number of apps was exceeded. Learn more: https://dt-url.net/upgrade-license

##### Enum keys
`MaxNumberOfInstalledAppsExceeded`

#### OperationStateBeforeError

⚠️ Deprecated
Use literal values.

Details about the state when an error occurred. Only present if the app's `status` is `ERROR`.

`PENDING_INSTALL`: The error occurred while installing the app.

`PENDING_UPDATE`: The error occurred while updating the app.

`PENDING_DELETE`: The error occurred while deleting the app.

`OK`: At least one sub resource failed while the app was already running.

##### Enum keys
`Ok` | `PendingDelete` | `PendingInstall` | `PendingUpdate`

#### PendingOperation

⚠️ Deprecated
Use literal values.

The pending operation of the app. Only present if the app's `status` is `PENDING`.

`INSTALL`: The app is currently being installed.

`UPDATE`: The app is currently being updated.

`DELETE`: The app is currently being deleted.

##### Enum keys
`Delete` | `Install` | `Update`

#### ResourceContextOperationsItem

⚠️ Deprecated
Use literal values.

##### Enum keys
`Run` | `Uninstall` | `Update`

#### Status

⚠️ Deprecated
Use literal values.

The status of the app.

`OK`: The app is fully installed and running.

`PENDING`: The app is currently being installed, updated or deleted.

`PENDING_DELETION`: A new version of the app was successfully installed and this version is scheduled for
deletion.

`DEACTIVATED`: The app is deactivated and cannot be executed.

`ERROR`: The app failed with an error.

##### Enum keys
`Deactivated` | `Error` | `Ok` | `Pending` | `PendingDeletion`

#### SubResourceType

⚠️ Deprecated
Use literal values.

The sub resource type.

`FUNCTIONS`: app functions.

`FILES`: static files of an app.

`SETTINGS_SCHEMAS`: settings schemas of an app.

`DOCUMENTS`: documents, e.g. templates, that are part of an app bundle.

##### Enum keys
`Documents` | `Files` | `Functions` | `SettingsSchemas`
