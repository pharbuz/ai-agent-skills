# @dynatrace-sdk/client-classic-environment-v2

Source: <https://developer.dynatrace.com/develop/sdks/client-classic-environment-v2/v6/> (latest: `client-classic-environment-v2/v6`).

> Truncated — this SDK's auto-generated reference is large. Key exports/usage are below; see the full reference at the URL above.

## client-classic-environment-v2/v6

`/develop/sdks/client-classic-environment-v2/v6/`

- SDK for TypeScript
- Classic Environment V2
- V6

## Classic Environment V2
Documentation of the Dynatrace Environment API v2. Resources here generally supersede those in v1. Migration of resources from v1 is in progress.

If you miss a resource, consider using the Dynatrace Environment API v1.

To read about use cases and examples, see Dynatrace Documentation.

Notes about compatibility:

- Operations marked as early adopter or preview may be changed in non-compatible ways, although we try to avoid this.

- We may add new enum constants without incrementing the API version; thus, clients need to handle unknown enum constants gracefully.

 @dynatrace-sdk/client-classic-environment-v2 v6.1.0 

`tsx
npm install @dynatrace-sdk/client-classic-environment-v2
`

### accessTokensActiveGateTokensClient

`tsx
import { accessTokensActiveGateTokensClient } from '@dynatrace-sdk/client-classic-environment-v2';
`

#### createToken

accessTokensActiveGateTokensClient.createToken(config): PromiseActiveGateTokenCreated>Creates a new ActiveGate tokenOne of the following scopes is required:

- environment-api:activegate-tokens:create

- environment-api:activegate-tokens:write

- fleet-management:activegate.tokens:create

- fleet-management:activegate.tokens:write
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegate.tokens:write
The newly created token will be owned by the same user who owns the token used for authentication of the call.

##### Parameters
 |
 | Name | Type
 | config.body*required | ActiveGateTokenCreate

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateTokenCreated | 201 | Success. The token has been created. The body of the response contains the token secret.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Client side error. | Server side error.Code example
`tsx
import { accessTokensActiveGateTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensActiveGateTokensClient.createToken({ body: { activeGateType: "ENVIRONMENT", name: "myToken", }, });
`

#### getToken

accessTokensActiveGateTokensClient.getToken(config): PromiseActiveGateToken>Gets metadata of an ActiveGate tokenOne of the following scopes is required:

- environment-api:activegate-tokens:read

- fleet-management:activegate.tokens:read
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegate.tokens:read
The token secret is not exposed.

##### Parameters
 |
 | Name | Type | Description
 | config.activeGateTokenIdentifier*required | string | The ActiveGate token identifier, consisting of prefix and public part of the token.

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateToken | 200 | Success. The response contains the metadata of the tokens.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Failed. The requested resource doesn't exist. | Client side error. | Server side error.Code example
`tsx
import { accessTokensActiveGateTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensActiveGateTokensClient.getToken({ activeGateTokenIdentifier: "...", });
`

#### listTokens

accessTokensActiveGateTokensClient.listTokens(config): PromiseActiveGateTokenList>Lists all available ActiveGate tokensOne of the following scopes is required:

- environment-api:activegate-tokens:read

- fleet-management:activegate.tokens:read
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegate.tokens:read
You can limit the output by using pagination:

- Specify the number of results per page in the pageSize query parameter.

- Use the cursor from the nextPageKey field of the previous response in the nextPageKey query parameter to obtain subsequent pages.

##### Parameters
 |
 | Name | Type | Description
 | config.nextPageKey | string | The cursor for the next page of results. You can find it in the nextPageKey field of the previous response.

 The first page is always returned if you don't specify the nextPageKey query parameter.

 When the nextPageKey is set to obtain subsequent pages, you must omit all other query parameters.
 | config.pageSize | number | The amount of ActiveGate tokens in a single response payload.

 The maximal allowed page size is 3000 and the minimal size is 100.

 If not set, 100 is used.

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateTokenList | 200 | Success. The response contains the list of ActiveGate tokens.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Failed. The requested resource doesn't exist. | Client side error. | Server side error.Code example
`tsx
import { accessTokensActiveGateTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensActiveGateTokensClient.listTokens();
`

#### revokeToken

accessTokensActiveGateTokensClient.revokeToken(config): PromiseDeletes an ActiveGate tokenOne of the following scopes is required:

- environment-api:activegate-tokens:write

- fleet-management:activegate.tokens:write
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegate.tokens:write

##### Parameters
 |
 | Name | Type | Description
 | config.activeGateTokenIdentifier*required | string | The ActiveGate token identifier, consisting of prefix and public part of the token to be deleted.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | Success. Response doesn't have a body.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Failed. The requested resource doesn't exist. | Client side error. | Server side error.Code example
`tsx
import { accessTokensActiveGateTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensActiveGateTokensClient.revokeToken({ activeGateTokenIdentifier: "...", });
`

### accessTokensAgentTokensClient

`tsx
import { accessTokensAgentTokensClient } from '@dynatrace-sdk/client-classic-environment-v2';
`

#### getAgentConnectionToken

accessTokensAgentTokensClient.getAgentConnectionToken(config): PromiseAgentConnectionToken>Gets the agent connection token | maturity=EARLY_ADOPTEROne of the following scopes is required:

- environment-api:agent-connection-tokens:read

- fleet-management:oneagent.tokens:read
One of the following permissions is required:

- environment:roles:agent-install

- fleet-management:oneagent.tokens:read
Returns the agent connection token.

##### Returns
 |
 | Return type | Status code | Description
 | AgentConnectionToken | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Failed. The requested resource doesn't exist. | Client side error. | Server side error.Code example
`tsx
import { accessTokensAgentTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensAgentTokensClient.getAgentConnectionToken();
`

### accessTokensApiTokensClient

`tsx
import { accessTokensApiTokensClient } from '@dynatrace-sdk/client-classic-environment-v2';
`

#### createApiToken

accessTokensApiTokensClient.createApiToken(config): PromiseApiTokenCreated>Creates a new API tokenOne of the following scopes is required:

- environment-api:api-tokens:write

- api-tokens:tokens:write
One of the following permissions is required:

- environment:roles:viewer

- api-tokens:tokens:write
The newly created token will be owned by the same user who owns the token used for authentication of the call.Creating personal access tokens requires the `environment:roles:viewer` permission. Creating access tokens requires the `environment:roles:manage-settings` permission.

##### Parameters
 |
 | Name | Type
 | config.body*required | ApiTokenCreate

##### Returns
 |
 | Return type | Status code | Description
 | ApiTokenCreated | 201 | Success. The token has been created. The body of the response contains the token secret.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Client side error. | Server side error.Code example
`tsx
import { accessTokensApiTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensApiTokensClient.createApiToken({ body: { name: "tokenName", scopes: ["metrics.read"] }, });
`

#### deleteApiToken

accessTokensApiTokensClient.deleteApiToken(config): PromiseDeletes an API tokenOne of the following scopes is required:

- environment-api:api-tokens:write

- api-tokens:tokens:write
One of the following permissions is required:

- environment:roles:viewer

- api-tokens:tokens:write

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | The ID of the token to be deleted.

 You can specify either the ID or the secret of the token.

 You can't delete the token you're using for authentication of the request.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | Success. Response doesn't have a body.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. You can't delete the token you're using for authentication of the request. | Client side error. | Server side error.Code example
`tsx
import { accessTokensApiTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensApiTokensClient.deleteApiToken({ id: "...", });
`

#### getApiToken

accessTokensApiTokensClient.getApiToken(config): PromiseApiToken>Gets API token metadata by token IDOne of the following scopes is required:

- environment-api:api-tokens:read

- api-tokens:tokens:read
One of the following permissions is required:

- environment:roles:viewer

- api-tokens:tokens:read
The token secret is not exposed.

##### Parameters
 |
 | Name | Type
 | config.id*required | string

##### Returns
 |
 | Return type | Status code | Description
 | ApiToken | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Client side error. | Server side error.Code example
`tsx
import { accessTokensApiTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensApiTokensClient.getApiToken({ id: "...",});
`

#### listApiTokens

accessTokensApiTokensClient.listApiTokens(config): PromiseApiTokenList>Lists all available API tokensOne of the following scopes is required:

- environment-api:api-tokens:read

- api-tokens:tokens:read
One of the following permissions is required:

- environment:roles:viewer

- api-tokens:tokens:read
You can limit the output by using pagination:

- Specify the number of results per page in the pageSize query parameter.

- Use the cursor from the nextPageKey field of the previous response in the nextPageKey query parameter to obtain subsequent pages.

##### Parameters
 |
 | Name | Type | Description
 | config.apiTokenSelector | string | Filters the resulting sets of tokens. Only tokens matching the specified criteria are included into response.

 You can set one or more of the following criteria:

- Owner: `owner("value")`. The user that owns the token. Case-sensitive.
- Personal access token: `personalAccessToken(false)`. Set to `true` to include only personal access tokens or to `false` to include only API tokens.
- Token scope: `scope("scope1","scope2")`. If several values are specified, the OR logic applies. To set multiple criteria, separate them with commas (`,`). Only results matching all criteria are included into response.
 | config.fields | string | Specifies the fields to be included in the response.

 The following fields are included by default:

- `id`
- `name`
- `enabled`
- `owner`
- `creationDate` To remove fields from the response, specify them with the minus (`-`) operator as a comma-separated list (for example, `-creationDate,-owner`).

 You can include additional fields:

- `personalAccessToken`

- `expirationDate`

- `lastUsedDate`

- `lastUsedIpAddress`

- `modifiedDate`

- `scopes`

- `additionalMetadata`

 To add fields to the response, specify them with the plus (`+`) operator as a comma-separated list (for example, `+expirationDate,+scopes`). You can combine adding and removing of fields (for example, `+scopes,-creationDate`).

 Alternatively, you can define the desired set of fields in the response. Specify the required fields as a comma-separated list, without operators (for example, `creationDate,expirationDate,owner`). The ID is always included in the response.

 The fields string must be URL-encoded.
 | config.from | string | Filters tokens based on the last usage time. The start of the requested timeframe.

 You can use one of the following formats:

- Timestamp in UTC milliseconds.
- Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional.
- Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week. You can also specify relative timeframe without an alignment: `now-NU`. Supported time units for the relative timeframe are:
- `m`: minutes
- `h`: hours
- `d`: days
- `w`: weeks
- `M`: months
- `y`: years
 | config.nextPageKey | string | The cursor for the next page of results. You can find it in the nextPageKey field of the previous response.

 The first page is always returned if you don't specify the nextPageKey query parameter.

 When the nextPageKey is set to obtain subsequent pages, you must omit all other query parameters.
 | config.pageSize | number | The amount of API tokens in a single response payload.

 The maximal allowed page size is 10000 and the minimal allowed page size is 100.

 If not set, 200 is used.
 | config.sort | string | The sort order of the token list.

 You can sort by the following properties with a sign prefix for the sort order:

- `name`: token name (`+` a...z or `-` z...a)
- `lastUsedDate` last used (`+` never used tokens first `-` most recently used tokens first)
- `creationDate` (`+` oldest tokens first `-` newest tokens first)
- `expirationDate` (`+` tokens that expire soon first `-` unlimited tokens first)
- `modifiedDate` last modified (`+` never modified tokens first `-` most recently modified tokens first) If no prefix is set, + is used.

 If not set, tokens are sorted by creation date with newest first.
 | config.to | string | Filters tokens based on the last usage time. The end of the requested timeframe.

 You can use one of the following formats:

- Timestamp in UTC milliseconds.
- Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional.
- Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week. You can also specify relative timeframe without an alignment: `now-NU`. Supported time units for the relative timeframe are:
- `m`: minutes
- `h`: hours
- `d`: days
- `w`: weeks
- `M`: months
- `y`: years If not set, the current timestamp is used.

##### Returns
 |
 | Return type | Status code | Description
 | ApiTokenList | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Client side error. | Server side error.Code example
`tsx
import { accessTokensApiTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensApiTokensClient.listApiTokens();
`

#### lookupApiToken

accessTokensApiTokensClient.lookupApiToken(config): PromiseApiToken>Gets API token metadata by token secretOne of the following scopes is required:

- environment-api:api-tokens:read

- api-tokens:tokens:read
One of the following permissions is required:

- environment:roles:viewer

- api-tokens:tokens:read

##### Parameters
 |
 | Name | Type
 | config.body*required | ApiTokenSecret

##### Returns
 |
 | Return type | Status code | Description
 | ApiToken | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { accessTokensApiTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensApiTokensClient.lookupApiToken({ body: { token: "dt0c01.<REDACTED_EXAMPLE_TOKEN>", }, });
`

#### updateApiToken

accessTokensApiTokensClient.updateApiToken(config): PromiseUpdates an API tokenOne of the following scopes is required:

- environment-api:api-tokens:write

- api-tokens:tokens:write
One of the following permissions is required:

- environment:roles:viewer

- api-tokens:tokens:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | ApiTokenUpdate |
 | config.id*required | string | The ID of the token to be updated.

 You can't disable the token you're using for authentication of the request.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | Success. Response doesn't have a body.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Client side error. | Server side error.Code example
`tsx
import { accessTokensApiTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensApiTokensClient.updateApiToken({ id: "...", body: {}, });
`

### accessTokensTenantTokensClient

`tsx
import { accessTokensTenantTokensClient } from '@dynatrace-sdk/client-classic-environment-v2';
`

#### cancelRotation

accessTokensTenantTokensClient.cancelRotation(config): PromiseTenantTokenConfig>Cancels tenant token rotationOne of the following scopes is required:

- environment-api:tenant-token-rotation:write

- fleet-management:tenant-token:rotate
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:tenant-token:rotate
To learn how to rotate tokens, see Token rotation in Dynatrace Documentation.

##### Returns
 |
 | Return type | Status code | Description
 | TenantTokenConfig | 200 | Success. Rotation process has been cancelled. The current tenant token remains valid.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. There is no ongoing rotation process. | Client side error. | Server side error.Code example
`tsx
import { accessTokensTenantTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensTenantTokensClient.cancelRotation();
`

#### finishRotation

accessTokensTenantTokensClient.finishRotation(config): PromiseTenantTokenConfig>Finishes tenant token rotationOne of the following scopes is required:

- environment-api:tenant-token-rotation:write

- fleet-management:tenant-token:rotate
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:tenant-token:rotate
To learn how to rotate tokens, see Token rotation in Dynatrace Documentation.

##### Returns
 |
 | Return type | Status code | Description
 | TenantTokenConfig | 200 | Success. The rotation process is completed. The active field of the response contains the new tenant token.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | No ongoing rotation process. | Client side error. | Server side error.Code example
`tsx
import { accessTokensTenantTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensTenantTokensClient.finishRotation();
`

#### startRotation

accessTokensTenantTokensClient.startRotation(config): PromiseTenantTokenConfig>Starts tenant token rotationOne of the following scopes is required:

- environment-api:tenant-token-rotation:write

- fleet-management:tenant-token:rotate
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:tenant-token:rotate
To learn how to rotate tokens, see Token rotation in Dynatrace Documentation.

##### Returns
 |
 | Return type | Status code | Description
 | TenantTokenConfig | 200 | Success. The new tenant token is created and will replace the old one. The active field of the response contains the new tenant token.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. Another rotation process is already in progress. | Client side error. | Server side error.Code example
`tsx
import { accessTokensTenantTokensClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await accessTokensTenantTokensClient.startRotation();
`

### activeGatesActiveGateGroupsClient

`tsx
import { activeGatesActiveGateGroupsClient } from '@dynatrace-sdk/client-classic-environment-v2';
`

#### getActiveGateGroups

activeGatesActiveGateGroupsClient.getActiveGateGroups(config): PromiseActiveGateGroups>Lists ActiveGate groupsOne of the following scopes is required:

- environment-api:activegates:read

- fleet-management:activegates:read
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegates:read

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateGroups | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { activeGatesActiveGateGroupsClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await activeGatesActiveGateGroupsClient.getActiveGateGroups();
`

### activeGatesActiveGateTokensEnforcementClient

`tsx
import { activeGatesActiveGateTokensEnforcementClient } from '@dynatrace-sdk/client-classic-environment-v2';
`

#### getTokenEnforcement

activeGatesActiveGateTokensEnforcementClient.getTokenEnforcement(config): PromiseActiveGateTokenEnforcement>Gets the status of ActiveGate tokens enforcementRequired scope: fleet-management:activegates:read
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegates:read

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateTokenEnforcement | 200 | Success. The response contains the status of ActiveGate tokens enforcement

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { activeGatesActiveGateTokensEnforcementClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await activeGatesActiveGateTokensEnforcementClient.getTokenEnforcement();
`

### activeGatesAutoUpdateConfigurationClient

`tsx
import { activeGatesAutoUpdateConfigurationClient } from '@dynatrace-sdk/client-classic-environment-v2';
`

#### getAutoUpdateConfigById

⚠️ Deprecated

activeGatesAutoUpdateConfigurationClient.getAutoUpdateConfigById(config): PromiseActiveGateAutoUpdateConfig>Gets the configuration of auto-update for the specified ActiveGateOne of the following scopes is required:

- environment-api:activegates:read

- fleet-management:activegates:read
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegates:read
Gets the configuration of auto-update for the specified ActiveGateDeprecation notice: This endpoint is deprecated. Use the Settings API endpoint `GET /api/v2/settings/objects` with schemaId `builtin:deployment.activegate.updates` and `scopes=ENVIRONMENT_ACTIVE_GATE-{ActiveGate ID}` to retrieve the auto-update setting of a specific ActiveGate.

##### Parameters
 |
 | Name | Type | Description
 | config.agId*required | string | The ID of the required ActiveGate.

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateAutoUpdateConfig | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Not found. See response body for details. | Client side error. | Server side error.Code example
`tsx
import { activeGatesAutoUpdateConfigurationClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await activeGatesAutoUpdateConfigurationClient.getAutoUpdateConfigById( { agId: "..." }, );
`

#### getGlobalAutoUpdateConfigForTenant

⚠️ Deprecated

activeGatesAutoUpdateConfigurationClient.getGlobalAutoUpdateConfigForTenant(config): PromiseActiveGateGlobalAutoUpdateConfig>Gets the global auto-update configuration of environment ActiveGates.One of the following scopes is required:

- environment-api:activegates:read

- fleet-management:activegates:read
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegates:read
Gets the global auto-update configuration of environment ActiveGates.Deprecation notice: This endpoint is deprecated. Use the Settings API endpoint `GET /api/v2/settings/objects` with schemaId `builtin:deployment.activegate.updates` and `scopes=tenant` to retrieve the global auto-update setting of environment ActiveGates.

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateGlobalAutoUpdateConfig | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { activeGatesAutoUpdateConfigurationClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await activeGatesAutoUpdateConfigurationClient.getGlobalAutoUpdateConfigForTenant();
`

#### putAutoUpdateConfigById

⚠️ Deprecated

activeGatesAutoUpdateConfigurationClient.putAutoUpdateConfigById(config): PromiseUpdates the configuration of auto-update for the specified ActiveGateOne of the following scopes is required:

- environment-api:activegates:write

- fleet-management:activegates:write
One of the following permissions is required:

- environment:roles:manage-settings

- fleet-management:activegates:write
Updates the configuration of auto-update for the specified ActiveGateDeprecation notice: This endpoint is deprecated. Use the Settings API endpoint `POST /api/v2/settings/objects` with schemaId `builtin:deployment.activegate.updates` and `scope=ENVIRONMENT_ACTIVE_GATE-{ActiveGate ID}` to change the auto-update setting of a specific ActiveGate.

##### Parameters
 |
 | Name | Type | Description
 | config.agId*required | string | The ID of the required ActiveGate.
 | config.body*required | ActiveGateAutoUpdateConfig |

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | Success. The auto-update configuration have been updated. Response doesn't have a body.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Failed. The input is invalid. | Client side error. | Server side error.Code example
`tsx
import { activeGatesAutoUpdateConfigurationClient } from "@dynatrace-sdk/client-classic-environment-v2";const data = await activeGatesAutoUpdateConfigurationClient.putAutoUpdateConfigById( { agId: "...", body: { setting: "INHERITED" } }, );
`

#### putGlobalAutoUpdateConfigForTenant

⚠️ Deprecated

activeGatesAutoUpdateConfigurationClient.putGlobalAutoUpdateConfigForTenant(config): PromisePuts the global auto-update configuration of environment ActiveGates.One of the following scopes is required:

- environment-api:activegates:write

- fleet-management:activegates:write
One of the following permissions is required:

- environment:roles:manage-settings

