# @dynatrace-sdk/client-app-settings

Source: <https://developer.dynatrace.com/develop/sdks/client-app-settings/> (latest: `client-app-settings`).

## client-app-settings

`/develop/sdks/client-app-settings/`

- SDK for TypeScript
- App Settings V1 (deprecated)

## App Settings V1 (deprecated)
This API version is already deprecated. Please use v2 instead. A migration guide can be found here.
Retrieve, update and manage app settings.

 @dynatrace-sdk/client-app-settings v1.9.8 Latest (V1)

`tsx
npm install @dynatrace-sdk/client-app-settings
`

### appSettingsObjectsClient

`tsx
import { appSettingsObjectsClient } from '@dynatrace-sdk/client-app-settings';
`

#### deleteAppSettingsObjectByObjectId

⚠️ Deprecated

appSettingsObjectsClient.deleteAppSettingsObjectByObjectId(config): PromiseDeletes the specified settings objectRequired scope: app-settings:objects:write
Required permission: app-settings:objects:write

##### Parameters
 |
 | Name | Type | Description
 | config.objectId*required | string | The ID of the required settings object.
 | config.optimisticLockingVersion*required | string | The version of the object for optimistic locking. You can use it to detect simultaneous modifications by different users.

 It is generated upon retrieval (GET requests). If set on update (PUT request) or deletion, the update/deletion will be allowed only if there wasn't any change between the retrieval and the update.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | Success. Response doesn't have a body.

##### Throws
 |
 | Error Type | Error Message
 | AppSettingsErrorEnvelopeError | Failed. The input is invalid. | Failed. Forbidden. | Failed. The requested resource doesn't exist. | Failed. Conflicting resource.Code example
`tsx
import { appSettingsObjectsClient } from "@dynatrace-sdk/client-app-settings";const data = await appSettingsObjectsClient.deleteAppSettingsObjectByObjectId( { objectId: "...", optimisticLockingVersion: "..." }, );
`

#### getAppSettingsObjectByObjectId

⚠️ Deprecated

appSettingsObjectsClient.getAppSettingsObjectByObjectId(config): PromiseAppSettingsObject>Gets the specified settings objectRequired scope: app-settings:objects:read
Required permission: app-settings:objects:readGets the specified settings object. Properties of type secret will be included in plain text if the call originates from a serverless function of your app; they will have irreversibly masked values otherwise. This protects these secrets from leaking to users of your app or other third parties.

##### Parameters
 |
 | Name | Type | Description
 | config.objectId*required | string | The ID of the required settings object.

##### Returns
 |
 | Return type | Status code | Description
 | AppSettingsObject | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | AppSettingsErrorEnvelopeError | Failed. The input is invalid. | Failed. Forbidden. | No object available for the given objectIdCode example
`tsx
import { appSettingsObjectsClient } from "@dynatrace-sdk/client-app-settings";const data = await appSettingsObjectsClient.getAppSettingsObjectByObjectId( { objectId: "..." }, );
`

#### getAppSettingsObjects

⚠️ Deprecated

appSettingsObjectsClient.getAppSettingsObjects(config): PromiseAppSettingsObjectsList>Lists persisted settings objectsRequired scope: app-settings:objects:read
Required permission: app-settings:objects:readLists persisted settings objects for selected schemas.If nothing is persisted or if all persisted settings objects are not accessible due to missing permissions, no items will be returned.To query the effective values (including schema defaults) please see getEffectiveAppSettingsValues.Properties of type secret will be included in plain text if the call originates from a serverless function of your app; they will have irreversibly masked values otherwise. This protects these secrets from leaking to users of your app or other third parties.

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | string | A list of fields to be included to the response. The provided set of fields extends the default set.

 Specify the required top-level fields, separated by commas (for example, summary,value).

 Supported fields: objectId, version, summary, searchSummary, schemaId, schemaVersion, modificationInfo, resourceContext, value.

 Default fields: objectId, version.
 | config.pageKey | string | The cursor for the next page of results. You can find it in the nextPageKey field of the previous response.

 The first page is always returned if you don't specify the page-key query parameter.

 When the page-key is set to obtain subsequent pages, you must omit all other query parameters.
 | config.pageSize | number | The amount of settings objects in a single response payload.

 The maximal allowed page size is 500.

 If not set, 100 is used.
 | config.schemaIds | string | A list of comma-separated schema IDs to which the requested objects belong.

 To load the first page, when the nextPageKey is not set, this parameter is required.

##### Returns
 |
 | Return type | Status code | Description
 | AppSettingsObjectsList | 200 | Success. Accessible objects returned.Even if a response returns a successful response code it is possible that the result is incomplete due to an internal error.In this case an 'error' property with information about the problem is added. The caller may decide to work with the incomplete result or do a retry of the operation.|

##### Throws
 |
 | Error Type | Error Message
 | AppSettingsErrorEnvelopeError | Failed. The input is invalid. | Failed. Forbidden. | Failed. The specified schema was not found.Code example
`tsx
import { appSettingsObjectsClient } from "@dynatrace-sdk/client-app-settings";const data = await appSettingsObjectsClient.getAppSettingsObjects();
`

#### getEffectiveAppSettingsValues

⚠️ Deprecated

appSettingsObjectsClient.getEffectiveAppSettingsValues(config): PromiseEffectiveAppSettingsValuesList>Lists effective settings valuesRequired scope: app-settings:objects:read
Required permission: app-settings:objects:readLists effective settings values for selected schemas.
If no object is persisted for a schema with "multiObject": false, the default value as defined in the schema will be returned.Properties of type secret will be included in plain text if the call originates from a serverless function of your app; they will have irreversibly masked values otherwise. This protects these secrets from leaking to users of your app or other third parties.

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | string | A list of fields to be included to the response. The provided set of fields extends the default set.

 Specify the required top-level fields, separated by commas (for example, summary,schemaId).

 Supported fields: summary, searchSummary, schemaId, schemaVersion, modificationInfo, value.

 Default fields: value.
 | config.pageKey | string | The cursor for the next page of results. You can find it in the nextPageKey field of the previous response.

 The first page is always returned if you don't specify the page-key query parameter.

 When the page-key is set to obtain subsequent pages, you must omit all other query parameters.
 | config.pageSize | number | The amount of settings objects in a single response payload.

 The maximal allowed page size is 500.

 If not set, 100 is used.
 | config.schemaIds | string | A list of comma-separated schema IDs to which the requested objects belong.

 Only considered on load of the first page, when the nextPageKey is not set.

##### Returns
 |
 | Return type | Status code | Description
 | EffectiveAppSettingsValuesList | 200 | SuccessEven if a response returns a successful response code it is possible that the result is incomplete due to an internal error.In this case an 'error' property with information about the problem is added. The caller may decide to work with the incomplete result or do a retry of the operation.|

##### Throws
 |
 | Error Type | Error Message
 | AppSettingsErrorEnvelopeError | Failed. The input is invalid. | Failed. The specified schema is not found.Code example
`tsx
import { appSettingsObjectsClient } from "@dynatrace-sdk/client-app-settings";const data = await appSettingsObjectsClient.getEffectiveAppSettingsValues();
`

#### postAppSettingsObject

⚠️ Deprecated

appSettingsObjectsClient.postAppSettingsObject(config): PromiseAppSettingsObjectResponse>Creates a new settings objectRequired scope: app-settings:objects:write
Required permission: app-settings:objects:writeCreates a new settings object.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | AppSettingsObjectCreate |
 | config.validateOnly | boolean | If `true`, the request runs only validation of the submitted settings objects, without saving them.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. No validation errors.
 | AppSettingsObjectResponse | 201 | Created

##### Throws
 |
 | Error Type | Error Message
 | AppSettingsErrorEnvelopeError | Failed. The input is invalid. | Failed. Forbidden. | Failed. The requested resource doesn't exist. | Failed. Conflicting resource.Code example
`tsx
import { appSettingsObjectsClient } from "@dynatrace-sdk/client-app-settings";const data = await appSettingsObjectsClient.postAppSettingsObject({ body: { schemaId: "jira-connection", value: {} }, });
`

#### putAppSettingsObjectByObjectId

⚠️ Deprecated

appSettingsObjectsClient.putAppSettingsObjectByObjectId(config): PromiseUpdates an existing settings objectRequired scope: app-settings:objects:write
Required permission: app-settings:objects:writeUpdates an existing settings object with new values. To update a property of the `secret` type you need to pass the new value unmasked. To keep the current value, send the current masked secret. You can obtain it via GET an object endpoint.Some schemas don't allow passing of the masked secret. In that case you need to send the unmasked secret with every update of the object.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | AppSettingsObjectUpdate |
 | config.objectId*required | string | The ID of the required settings object.
 | config.optimisticLockingVersion*required | string | The version of the object for optimistic locking. You can use it to detect simultaneous modifications by different users.

 It is generated upon retrieval (GET requests). If set on update (PUT request) or deletion, the update/deletion will be allowed only if there wasn't any change between the retrieval and the update.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | AppSettingsErrorEnvelopeError | Failed. The input is invalid. | Failed. Forbidden. | Failed. The requested resource doesn't exist. | Failed. Conflicting resource.Code example
`tsx
import { appSettingsObjectsClient } from "@dynatrace-sdk/client-app-settings";const data = await appSettingsObjectsClient.putAppSettingsObjectByObjectId( { objectId: "...", optimisticLockingVersion: "...", body: { value: {} }, }, );
`

#### resolveEffectivePermissions

⚠️ Deprecated

appSettingsObjectsClient.resolveEffectivePermissions(config): PromiseEffectivePermissions>Get the effective settings permissions of the calling user in the environmentRequired scope: app-settings:objects:read or app-settings:objects:write
Required permission: app-settings:objects:read or app-settings:objects:write

##### Parameters
 |
 | Name | Type
 | config.body*required | ResolutionRequest

##### Throws
 |
 | Error Type | Error Message
 | AppSettingsErrorEnvelopeError | Failed. The input is invalid. | Failed. Forbidden. No access to any schema. | Failed.Code example
`tsx
import { appSettingsObjectsClient } from "@dynatrace-sdk/client-app-settings";const data = await appSettingsObjectsClient.resolveEffectivePermissions( { body: { permissions: [ { permission: "app-settings:objects:read", context: { schemaId: "..." }, }, ], }, }, );
`

### Types

#### AppSettingsError

 |
 | Name | Type | Description
 | code | number | The HTTP status code
 | details | AppSettingsErrorDetails | The error details
 | message*required | string | The error message

#### AppSettingsErrorDetails

The error details

 |
 | Name | Type | Description
 | constraintViolations | ArrayConstraintViolation> | A list of constraint violations
 | missingScopes | Arraystring> | In case of a 403 - Forbidden response, a list of missing scopes necessary to successfully execute the request

#### AppSettingsErrorEnvelope

 |
 | Name | Type
 | error*required | AppSettingsError

#### AppSettingsErrorIncomplete

Error object for an incomplete response

 |
 | Name | Type | Description
 | code | number | The HTTP status code
 | details | AppSettingsErrorDetails | The error details
 | message*required | string | The error message

#### AppSettingsModificationInfo

Modification information about the app setting.

 |
 | Name | Type | Description
 | createdBy | string | The unique identifier of the user who created the app setting.
 | createdTime | Date | Timestamp when the app settings was created in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSS'Z')
 | lastModifiedBy | string | The unique identifier of the user who performed the most recent modification.
 | lastModifiedTime | Date | Timestamp when the app setting was last modified in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSS'Z')

#### AppSettingsObject

A settings object.

 |
 | Name | Type | Description
 | modificationInfo | AppSettingsModificationInfo | Modification information about the app setting.
 | objectId*required | string | The ID of the settings object.
 | resourceContext | ResourceContext | The resource context, which contains additional permission information about the object.
 | schemaId | string | The schema on which the object is based.
 | schemaVersion | string | The version of the schema on which the object is based.
 | searchSummary | string | A searchable summary string of the setting value. Plain text without Markdown.
 | summary | string | A short summary of settings. This can contain Markdown and will be escaped accordingly.
 | value | AppSettingsValue | The value of the setting.

 It defines the actual values of settings' parameters.

 The actual content depends on the object's schema.
 | version*required | string | The version of the object for optimistic locking. You can use it to detect simultaneous modifications by different users.

 It is generated upon retrieval (GET requests). If set on update (PUT request) or deletion, the update/deletion will be allowed only if there wasn't any change between the retrieval and the update.

#### AppSettingsObjectCreate

Configuration of a new settings object.

 |
 | Name | Type | Description
 | insertAfter | string | The position of the new object. The new object will be added after the specified one.

 If `null`, the new object will be placed in the last position.

 If set to empty string, the new object will be placed in the first position.

 Only applicable for objects based on schemas with ordered objects (schema's `ordered` parameter is set to `true`).
 | schemaId*required | string | The schema on which the object is based.
 | value*required | AppSettingsValue | The value of the setting.

 It defines the actual values of settings' parameters.

 The actual content depends on the object's schema.

#### AppSettingsObjectResponse

The response to a creation request.

 |
 | Name | Type | Description
 | objectId*required | string | The ID of the created settings object.
 | version*required | string | The version of the object for optimistic locking. You can use it to detect simultaneous modifications by different users.

 It is generated upon retrieval (GET requests). If set on update (PUT request) or deletion, the update/deletion will be allowed only if there wasn't any change between the retrieval and the update.

#### AppSettingsObjectUpdate

An update of a settings object.

 |
 | Name | Type | Description
 | insertAfter | string | The position of the updated object. The new object will be moved behind the specified one.

 insertAfter and insertBefore are evaluated together and only one of both can be set.

 If `null` and insertBefore 'null', the existing object keeps the current position.

 If set to empty string, the updated object will be placed in the first position.

 Only applicable for objects based on schemas with ordered objects (schema's ordered parameter is set to `true`).
 | insertBefore | string | The position of the updated object. The new object will be moved in front of the specified one.

 insertAfter and insertBefore are evaluated together and only one of both can be set.

 If `null` and insertAfter 'null', the existing object keeps the current position.

 If set to empty string, the updated object will be placed in the last position.

 Only applicable for objects based on schemas with ordered objects (schema's ordered parameter is set to `true`).
 | value*required | AppSettingsValue | The value of the setting.

 It defines the actual values of settings' parameters.

 The actual content depends on the object's schema.

#### AppSettingsObjectsList

A list of settings objects.

 |
 | Name | Type | Description
 | error | AppSettingsErrorIncomplete | Error object for an incomplete response
 | items*required | ArrayAppSettingsObject> | A list of settings objects.
 | nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.

 Use it in the nextPageKey query parameter to obtain subsequent pages of the result.
 | pageSize*required | number | The number of entries per page.
 | totalCount*required | number | The total number of entries in the result.

#### ConstraintViolation

A list of constraint violations

 |
 | Name | Type
 | location | string
 | message | string
 | parameterLocation | "HEADER" | "PATH" | "PAYLOAD_BODY" | "QUERY"
 | path | string

#### EffectiveAppSettingsValue

An effective settings value.

 |
 | Name | Type | Description
 | modificationInfo | AppSettingsModificationInfo | Modification information about the app setting.
 | schemaId | string | The schema on which the object is based.
 | schemaVersion | string | The version of the schema on which the object is based.
 | searchSummary | string | A searchable summary string of the setting value. Plain text without Markdown.
 | summary | string | A short summary of settings. This can contain Markdown and will be escaped accordingly.
 | value | AppSettingsValue | The value of the setting.

 It defines the actual values of settings' parameters.

 The actual content depends on the object's schema.

#### EffectiveAppSettingsValuesList

A list of effective settings values.

 |
 | Name | Type | Description
 | error | AppSettingsErrorIncomplete | Error object for an incomplete response
 | items*required | ArrayEffectiveAppSettingsValue> | A list of effective settings values.
 | nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.

 Use it in the nextPageKey query parameter to obtain subsequent pages of the result.
 | pageSize*required | number | The number of entries per page.
 | totalCount*required | number | The total number of entries in the result.

#### EffectivePermission

 |
 | Name | Type
 | context | PermissionContext
 | granted*required | "true" | "false" | "condition"
 | permission*required | string

#### EffectivePermissions

type: ArrayEffectivePermission>

#### Modifications

The additional modification details for this settings object.

 |
 | Name | Type | Description
 | first | boolean | If non-moveable settings object is in the first group of non-moveable settings, or in the last (start or end of list).
 | modifiablePaths*required | Arraystring> | Property paths which are modifiable, regardless if the `write` operation is allowed.
 | movable | boolean | If settings object can be moved/reordered. Only applicable for ordered list schema.
 | nonModifiablePaths*required | Arraystring> | Property paths which are not modifiable, even if the `write` operation is allowed.

#### PermissionContext

 |
 | Name | Type
 | schemaId*required | string

#### ResolutionRequest

 |
 | Name | Type
 | permissions*required | ArraySinglePermissionRequest>

#### ResourceContext

The resource context, which contains additional permission information about the object.

 |
 | Name | Type | Description
 | modifications*required | Modifications | The additional modification details for this settings object.
 | operations*required | Array | The allowed operations on this settings object.

#### SinglePermissionRequest

optional generic set of context data

 |
 | Name | Type
 | context | PermissionContext
 | permission*required | "app-settings:objects:read" | "app-settings:objects:write"

### Enums

#### ConstraintViolationParameterLocation

⚠️ Deprecated
Use literal values.

##### Enum keys
`Header` | `Path` | `PayloadBody` | `Query`

#### EffectivePermissionGranted

⚠️ Deprecated
Use literal values.

##### Enum keys
`Condition` | `False` | `True`

#### ResourceContextOperationsItem

⚠️ Deprecated
Use literal values.

##### Enum keys
`Delete` | `Read` | `Write`

#### SinglePermissionRequestPermission

⚠️ Deprecated
Use literal values.

##### Enum keys
`AppSettingsObjectsRead` | `AppSettingsObjectsWrite`
