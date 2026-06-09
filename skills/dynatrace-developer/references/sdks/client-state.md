# @dynatrace-sdk/client-state

Source: <https://developer.dynatrace.com/develop/sdks/client-state/> (latest: `client-state`).

## client-state

`/develop/sdks/client-state/`

- SDK for TypeScript
- State

## State
Provides key-value storage for apps so that app developers can persist and get small chunks of
state in the context of their app.

States can either be stored in the context of an app (= app states) or in the context of an app and user (= user app states).

- States stored per app can be read by every user of the app.

- States stored per app and user can only be read and updated by the user who originally set that state.
Please visit the Dynatrace Developer to learn more about app states and user app states.

 @dynatrace-sdk/client-state v1.9.2 Latest (V1)

`tsx
npm install @dynatrace-sdk/client-state
`

### stateClient

`tsx
import { stateClient } from '@dynatrace-sdk/client-state';
`

#### deleteAppState

stateClient.deleteAppState(config): PromiseDeletes app stateRequired scope: state:app-states:delete

##### Parameters
 |
 | Name | Type | Description
 | config.key*required | string | Specify the key of the state

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | Unauthorized
 | Forbidden | Forbidden
 | NotFound | Not found
 | InternalServerError | Internal server error
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.deleteAppState({ key: "some-key",});
`

#### deleteAppStates

stateClient.deleteAppStates(config): PromiseDelete all app statesRequired scope: state:app-states:deleteDeletes all app states for an app to reset the app into a clean state.

##### Throws
 |
 | Error Type | Error Message
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.deleteAppStates();
`

#### deleteUserAppState

stateClient.deleteUserAppState(config): PromiseDelete user app stateRequired scope: state:user-app-states:delete

##### Parameters
 |
 | Name | Type | Description
 | config.key*required | string | Specify the key of the state

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | Unauthorized
 | Forbidden | Forbidden
 | NotFound | Not found
 | InternalServerError | Internal server error
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.deleteUserAppState({ key: "some-key",});
`

#### deleteUserAppStates

stateClient.deleteUserAppStates(config): PromiseDelete all user app statesRequired scope: state:user-app-states:deleteDeletes all user app states for the calling user and app.

##### Throws
 |
 | Error Type | Error Message
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.deleteUserAppStates();
`

#### getAppState

stateClient.getAppState(config): PromiseAppState>Gets app stateRequired scope: state:app-states:read

##### Parameters
 |
 | Name | Type | Description
 | config.key*required | string | Specify the key of the state

##### Returns
 |
 | Return type | Status code | Description
 | AppState | 200 | The app state

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | Unauthorized
 | Forbidden | Forbidden
 | NotFound | Not found
 | InternalServerError | Internal server error
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.getAppState({ key: "some-key",});
`

#### getAppStates

stateClient.getAppStates(config): PromiseAppStates>List app statesRequired scope: state:app-states:readLists app states. By default, only provides property key per state. Use add-fields parameter to include more fields and the filter parameter to narrow down the returned states.

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | string | Provide a comma separated list of additional properties to be included in the response.
 | config.filter | string | The filter parameter for filtering the set of returned resources If this parameter is omitted, no filtering is applied and all states will be returned.

 Filtering by string type parameters `key`, `modificationInfo.lastModifiedBy` when using one of the operators `contains`, `starts-with` and `ends-with` is case insensitive.

 When using the operators `=`and `!=`, filtering is case sensitive.

 The following fields are legal filtering parameters - any other field names will result in a HTTP 400 response:

- `key`, supported operators: `=`, `!=`, `contains`, `starts-with`, `ends-with`:

- `modificationInfo.lastModifiedTime`, supported operators:	`=`, `!=`, , `>=`

- `modificationInfo.lastModifiedBy`, supported operators: `=`, `!=`, `contains`, `starts-with`, `ends-with`

- `validUntilTime`, supported operators:	`=`, `!=`, , `>=`

 The following constraints apply:

- Field names are case-sensitive.

- Conditions can be connected via operators `and` and `or`. A single condition can be negated by `not`.

- Strings must be enclosed in single quotes. e.g. `key contains 'my-string'`

- Single quotes within a string must be escaped with a backslash: e.g. `key starts-with 'it\'s a string'`

- Maximum nesting depth (via brackets) is 2.

- Maximum length is 256 characters.

 Examples:

- `key starts-with 'game-'`

- `modificationInfo.lastModifiedTime >= '2022-07-01T00:10:05.000Z' and not (key contains 'new')`

##### Returns
 |
 | Return type | Status code | Description
 | AppStates | 200 | The list of app states

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | Unauthorized
 | Forbidden | Forbidden
 | InternalServerError | Internal server error
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.getAppStates();
`

#### getUserAppState

stateClient.getUserAppState(config): PromiseUserAppState>Get user app stateRequired scope: state:user-app-states:read

##### Parameters
 |
 | Name | Type | Description
 | config.key*required | string | Specify the key of the state

##### Returns
 |
 | Return type | Status code | Description
 | UserAppState | 200 | The user app state

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | Unauthorized
 | Forbidden | Forbidden
 | NotFound | Not found
 | InternalServerError | Internal server error
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.getUserAppState({ key: "some-key",});
`

#### getUserAppStates

stateClient.getUserAppStates(config): PromiseUserAppStates>List user app statesRequired scope: state:user-app-states:readLists user app states. By default, only provides property key per state. Use add-fields parameter to include more fields and the filter parameter to narrow down the returned states

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | string | Provide a comma separated list of additional properties to be included in the response.
 | config.filter | string | The filter parameter for filtering the set of returned resources If this parameter is omitted, no filtering is applied and all states will be returned.

 Filtering by string type parameters `key`, `modificationInfo.lastModifiedBy` when using one of the operators `contains`, `starts-with` and `ends-with` is case insensitive.

 When using the operators `=`and `!=`, filtering is case sensitive.

 The following fields are legal filtering parameters - any other field names will result in a HTTP 400 response:

- `key`, supported operators: `=`, `!=`, `contains`, `starts-with`, `ends-with`:

- `modificationInfo.lastModifiedTime`, supported operators:	`=`, `!=`, , `>=`

- `modificationInfo.lastModifiedBy`, supported operators: `=`, `!=`, `contains`, `starts-with`, `ends-with`

- `validUntilTime`, supported operators:	`=`, `!=`, , `>=`

 The following constraints apply:

- Field names are case-sensitive.

- Conditions can be connected via operators `and` and `or`. A single condition can be negated by `not`.

- Strings must be enclosed in single quotes. e.g. `key contains 'my-string'`

- Single quotes within a string must be escaped with a backslash: e.g. `key starts-with 'it\'s a string'`

- Maximum nesting depth (via brackets) is 2.

- Maximum length is 256 characters.

 Examples:

- `key starts-with 'game-'`

- `modificationInfo.lastModifiedTime >= '2022-07-01T00:10:05.000Z' and not (key contains 'new')`

##### Returns
 |
 | Return type | Status code | Description
 | UserAppStates | 200 | The list of user app states

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | Unauthorized
 | Forbidden | Forbidden
 | InternalServerError | Internal server error
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.getUserAppStates();
`

#### setAppState

stateClient.setAppState(config): PromiseUpdates app stateRequired scope: state:app-states:writeUpdates the cross-user app state for the given key. Be aware that other users will be able to read the value.
Use the user-scoped user-app-state to only store values for the authenticated user.Certain limits apply when updating app states.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | AppState |
 | config.key*required | string | Specify the key of the state

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | OK

##### Throws
 |
 | Error Type | Error Message
 | AppStateLimitsExceeded | Exceeded size limit for combined size of app states of this app
 | Unauthorized | Unauthorized
 | Forbidden | Forbidden
 | InternalServerError | Internal server error
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.setAppState({ key: "some-key", body: { value: "some-state", validUntilTime: "now+2d" },});
`

#### setUserAppState

stateClient.setUserAppState(config): PromiseUpdates user app stateRequired scope: state:user-app-states:writeUpdates the user specific app state for the given key and calling user.Certain limits apply when updating user app states.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | UserAppState |
 | config.key*required | string | Specify the key of the state

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | OK

##### Throws
 |
 | Error Type | Error Message
 | UserAppStateLimitsExceeded | Exceeded limit for number of user app states to be stored for this user and app
 | Unauthorized | Unauthorized
 | Forbidden | Forbidden
 | InternalServerError | Internal server error
 | GeneralError | Unexpected errorCode example
`tsx
import { stateClient } from "@dynatrace-sdk/client-state";const data = await stateClient.setUserAppState({ key: "some-key", body: { value: "some-state", validUntilTime: "now+2d" },});
`

### Types

#### AppState

 |
 | Name | Type | Description
 | modificationInfo | ModificationInfo |
 | validUntilTime | null | string | Specify the date until the state is persisted. Allowed are values from now+1m to now+90d! Returned validUntilTimes are always a string formatted in ISO 8601
 | value*required | string |

#### AppStates

type: ArrayListAppState>

#### Error

 |
 | Name | Type
 | code*required | number
 | details | ErrorDetails
 | message*required | string

#### ErrorDetails

 |
 | Name | Type | Description
 | errorCode | "AppStateOverallSizeLimitExceeded" | "AppStateSizeLimitExceeded" | "UserAppStateSizeLimitExceeded" | "UserAppStateCountLimitExceeded" | "UserAppStateSizeLimitPerUserExceeded" | Error code indicating the reason why the request failed

- `AppStateOverallSizeLimitExceeded` - The overall size limit for the combined size of app states of this app was exceeded
- `AppStateSizeLimitExceeded` - The app state value exceeded the size limit for a single app state
- `UserAppStateSizeLimitPerUserExceeded` - The size of user app state values of a user for an app exceeds the limit
- `UserAppStateSizeLimitExceeded` - deprecated The user app state content exceeded the size limit for a single user app state. No longer returned by the API.
- `UserAppStateCountLimitExceeded` - deprecated The maximum number of user app states for this user and app was exceeded. No longer returned by the API.

#### ErrorResponse

 |
 | Name | Type
 | error*required | Error

#### ListAppState

 |
 | Name | Type | Description
 | key*required | string |
 | modificationInfo | ModificationInfo |
 | validUntilTime | null | string | Specify the date until the state is persisted. Allowed are values from now+1m to now+90d! Returned validUntilTimes are always a string formatted in ISO 8601
 | value | string |

#### ListUserAppState

 |
 | Name | Type | Description
 | key*required | string |
 | modificationInfo | ModificationInfo |
 | validUntilTime | null | string | Specify the date until the state is persisted. Allowed are values from now+1m to now+90d! Returned validUntilTimes are always a string formatted in ISO 8601
 | value | string |

#### ModificationInfo

 |
 | Name | Type
 | lastModifiedBy*required | string
 | lastModifiedTime*required | Date

#### PersistenceState

 |
 | Name | Type | Description
 | modificationInfo | ModificationInfo |
 | validUntilTime | null | string | Specify the date until the state is persisted. Allowed are values from now+1m to now+90d! Returned validUntilTimes are always a string formatted in ISO 8601
 | value | string |

#### UserAppState

 |
 | Name | Type | Description
 | modificationInfo | ModificationInfo |
 | validUntilTime | null | string | Specify the date until the state is persisted. Allowed are values from now+1m to now+90d! Returned validUntilTimes are always a string formatted in ISO 8601
 | value*required | string |

#### UserAppStates

type: ArrayListUserAppState>

### Enums

#### ErrorDetailsErrorCode

⚠️ Deprecated
Use literal values.

Error code indicating the reason why the request failed

- `AppStateOverallSizeLimitExceeded` - The overall size limit for the combined size of app states of this app was exceeded

- `AppStateSizeLimitExceeded` - The app state value exceeded the size limit for a single app state

- `UserAppStateSizeLimitPerUserExceeded` - The size of user app state values of a user for an app exceeds the limit

- `UserAppStateSizeLimitExceeded` - deprecated The user app state content exceeded the size limit for a single user app state. No longer returned by the API.

- `UserAppStateCountLimitExceeded` - deprecated The maximum number of user app states for this user and app was exceeded. No longer returned by the API.

##### Enum keys
`AppStateOverallSizeLimitExceeded` | `AppStateSizeLimitExceeded` | `UserAppStateCountLimitExceeded` | `UserAppStateSizeLimitExceeded` | `UserAppStateSizeLimitPerUserExceeded`
