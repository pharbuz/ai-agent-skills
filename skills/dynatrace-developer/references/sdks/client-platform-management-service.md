# @dynatrace-sdk/client-platform-management-service

Source: <https://developer.dynatrace.com/develop/sdks/client-platform-management-service/v1/> (latest: `client-platform-management-service/v1`).

## client-platform-management-service/v1

`/develop/sdks/client-platform-management-service/v1/`

- SDK for TypeScript
- Platform Management
- V1

## Platform Management
Basic read-only information about the currently logged-in environment

 @dynatrace-sdk/client-platform-management-service v1.8.0 

`tsx
npm install @dynatrace-sdk/client-platform-management-service
`

### effectivePermissionsClient

`tsx
import { effectivePermissionsClient } from '@dynatrace-sdk/client-platform-management-service';
`

#### resolveEffectivePermissions

effectivePermissionsClient.resolveEffectivePermissions(config): PromiseEffectivePermissions>Get the effective permissions of the calling user in the environmentOne of the following scopes is required:

- app-engine:apps:run

- app-engine:functions:run

- platform-management:effective-permissions:resolve
This endpoint resolves whether the caller (based on the provided OAuth token when calling this endpoint) has the requested permissions (see IAM policy reference for a list of permissions and their conditions). It resolves the permission via IAM and uses the optional context to evaluate conditional results. The provided context consists of key-value pairs where the `key` must correspond to the name of a supported condition of the requested permission and the `value` is the value that it this condition is evaluated against given a user's policies.For each requested permission the response indicates whether the user has the requested permission (`"granted": "true"`), does not have it (`"granted": "false"`) or only has it conditionally (`"granted": "condition"`), meaning that the provided values for conditions in the context are not sufficient to decide whether the caller has the permission.For environment API v2 scopes (i.e. scopes starting with environment-api:) roles on the environment and management zone level will also be considered.> ℹ️ Settings permission requests for scopes `settings:schemas:read`, `settings:objects:read`, and `settings:objects:write` will always result in a result with `"granted": "condition"`. You can use the dedicated effective permissions endpoint for settings instead.> ℹ️ Apps must list all permissions they check in the list of `scopes` in their app configuration.You can learn more about querying user permissions on Dynatrace Developer.

##### Parameters
 |
 | Name | Type
 | config.body*required | ResolutionRequest

##### Throws
 |
 | Error Type | Error Message
 | DefaultErrorResponse | Unexpected errorCode example
`tsx
import { effectivePermissionsClient } from "@dynatrace-sdk/client-platform-management-service";const data = await effectivePermissionsClient.resolveEffectivePermissions( { body: { permissions: [ { permission: "state:app-states:write" }, ], }, }, );
`

### environmentInformationClient

`tsx
import { environmentInformationClient } from '@dynatrace-sdk/client-platform-management-service';
`

#### getEnvironmentInformation

environmentInformationClient.getEnvironmentInformation(config): PromiseEnvironmentInfo>Get basic environment informationOne of the following scopes is required:

- app-engine:apps:run

- app-engine:functions:run

- platform-management:environments:read
Get basic information about the current environment.

##### Returns
 |
 | Return type | Status code | Description
 | EnvironmentInfo | 200 | Info about the requested environment.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Bad request
 | Unauthorized | Authentication failed
 | NotFound | Resource not found
 | ServiceUnavailable | There is a temporary problem in the backend.
 | DefaultErrorResponse | Unexpected errorCode example
`tsx
import { environmentInformationClient } from "@dynatrace-sdk/client-platform-management-service";const data = await environmentInformationClient.getEnvironmentInformation();
`

### environmentSettingsClient

`tsx
import { environmentSettingsClient } from '@dynatrace-sdk/client-platform-management-service';
`

#### getEnvironmentSettings

environmentSettingsClient.getEnvironmentSettings(config): PromiseSettingsResponse>Get settings for the environmentOne of the following scopes is required:

- app-engine:apps:run

- app-engine:functions:run

- platform-management:environments:read
Gets settings for environment.

##### Returns
 |
 | Return type | Status code | Description
 | SettingsResponse | 200 | The settings for the requested environment

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Bad request
 | Unauthorized | Authentication failed
 | NotFound | Resource not found
 | ServiceUnavailable | There is a temporary problem in the backend.
 | DefaultErrorResponse | Unexpected errorCode example
`tsx
import { environmentSettingsClient } from "@dynatrace-sdk/client-platform-management-service";const data = await environmentSettingsClient.getEnvironmentSettings();
`

### licenseInformationClient

`tsx
import { licenseInformationClient } from '@dynatrace-sdk/client-platform-management-service';
`

#### getLicense

licenseInformationClient.getLicense(config): PromiseLicense>Get basic license informationOne of the following scopes is required:

- app-engine:apps:run

- app-engine:functions:run

- platform-management:environments:read
Get basic license information about the current environment.

##### Returns
 |
 | Return type | Status code | Description
 | License | 200 | The license info of the requested environment.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Bad request
 | Unauthorized | Authentication failed
 | NotFound | Resource not found
 | ServiceUnavailable | There is a temporary problem in the backend.
 | DefaultErrorResponse | Unexpected errorCode example
`tsx
import { licenseInformationClient } from "@dynatrace-sdk/client-platform-management-service";const data = await licenseInformationClient.getLicense();
`

#### getLicenseSettings

licenseInformationClient.getLicenseSettings(config): PromiseLicenseSettingsResponse>Get basic license settings informationOne of the following scopes is required:

- app-engine:apps:run

- app-engine:functions:run

- platform-management:environments:read
Get basic license settings information about the current environment

##### Parameters
 |
 | Name | Type
 | config.keys | Arraystring>

##### Returns
 |
 | Return type | Status code | Description
 | LicenseSettingsResponse | 200 | The license settings info of the requested environment.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Bad request
 | Unauthorized | Authentication failed
 | NotFound | Resource not found
 | ServiceUnavailable | There is a temporary problem in the backend.
 | DefaultErrorResponse | Unexpected errorCode example
`tsx
import { licenseInformationClient } from "@dynatrace-sdk/client-platform-management-service";const data = await licenseInformationClient.getLicenseSettings();
`

### Types

#### EffectivePermission

 |
 | Name | Type | Description
 | context | ArrayPermissionContext> |
 | granted*required | "true" | "false" | "condition" | true: The caller has the permission false: The caller does not have the permission condition: The caller conditionally has the permission or in case of scopes starting with 'environment-api:' the caller only has the permission for specific management zones.
 | permission*required | string |

#### EffectivePermissions

type: ArrayEffectivePermission>

#### EnvironmentInfo

 |
 | Name | Type
 | blockTime | Date
 | createTime*required | Date
 | environmentId*required | string
 | state*required | "BEING_CREATED" | "CREATED_NOT_INITIALIZED" | "ACTIVE" | "DEACTIVATED" | "BEING_DELETED" | "BLOCKED" | "DELETION_FAILED" | "PRE_ALLOCATED"
 | type*required | "INTERNAL" | "CUSTOMER" | "SELF_MONITORING"

#### Error

Standard error response

 |
 | Name | Type
 | code*required | number
 | message*required | string

#### ErrorEnvelope

 |
 | Name | Type | Description
 | error*required | Error | Standard error response

#### License

 |
 | Name | Type
 | platformSubscription*required | boolean
 | trial*required | boolean

#### LicenseSetting

 |
 | Name | Type
 | key*required | string
 | value*required | string

#### LicenseSettingsResponse

 |
 | Name | Type
 | settings*required | ArrayLicenseSetting>

#### PermissionContext

 |
 | Name | Type
 | key*required | string
 | value*required | string

#### ResolutionRequest

 |
 | Name | Type
 | permissions*required | ArraySinglePermissionRequest>

#### SettingsResponse

 |
 | Name | Type | Description
 | activeTrialSubscriptionEndDate | Date | Date when the trial period ends.
 | chatEnabled*required | boolean |
 | countryCode | string | ISO3166-1 alpha-2 two letter country code. See: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

#### SinglePermissionRequest

Optional generic set of context data

 |
 | Name | Type
 | context | null | ArrayPermissionContext>
 | permission*required | string

### Enums

#### EffectivePermissionGranted

⚠️ Deprecated
Use literal values.

true: The caller has the permission false: The caller does not have the permission condition: The caller conditionally has the permission or in case of scopes starting with 'environment-api:' the caller only has the permission for specific management zones.

##### Enum keys
`Condition` | `False` | `True`

#### EnvironmentInfoType

⚠️ Deprecated
Use literal values.

##### Enum keys
`Customer` | `Internal` | `SelfMonitoring`

#### EnvironmentState

⚠️ Deprecated
Use literal values.

##### Enum keys
`Active` | `BeingCreated` | `BeingDeleted` | `Blocked` | `CreatedNotInitialized` | `Deactivated` | `DeletionFailed` | `PreAllocated`
