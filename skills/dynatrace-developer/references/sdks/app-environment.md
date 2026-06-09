# @dynatrace-sdk/app-environment

Source: <https://developer.dynatrace.com/develop/sdks/app-environment/v1/> (latest: `app-environment/v1`).

## app-environment/v1

`/develop/sdks/app-environment/v1/`

- SDK for TypeScript
- App Environment
- V1

## App Environment
Obtain the basic information about the app and the environment in which it's running.

 @dynatrace-sdk/app-environment v1.1.4 

`tsx
npm install @dynatrace-sdk/app-environment
`

### Functions

#### getAppId

getAppId(): stringRetrieves the app id.

##### Returns
 |
 | Return type | Description
 | string | app id defined in app config.

 Note: If the Dynatrace JavaScript runtime isn't available, 'dt.missing.app.id' will be returned and a warning will be logged to the console.Code example
`tsx
import { getAppId } from '@dynatrace-sdk/app-environment';// Get the current app's IDconst appId = getAppId();
`

#### getAppName

getAppName(): stringRetrieves the app name.

##### Returns
 |
 | Return type | Description
 | string | app name defined in app config.

 Note: If the Dynatrace JavaScript runtime isn't available, 'dt.missing.app.name' will be returned and a warning will be logged to the console.Code example
`tsx
import { getAppName } from '@dynatrace-sdk/platform/app-environment';// Get the current app's nameconst appName = getAppName();
`

#### getAppVersion

getAppVersion(): stringRetrieves the app version.

##### Returns
 |
 | Return type | Description
 | string | app version defined in app manifest.

 Note: If the Dynatrace JavaScript runtime isn't available, 'dt.missing.app.version' will be returned and a warning will be logged to the console.Code example
`tsx
import { getAppVersion } from '@dynatrace-sdk/platform/app-environment';// Get the current app's versionconst appVersion = getAppVersion();
`

#### getCurrentUserDetails

getCurrentUserDetails(): UserDetailsRetrieves the information about currently logged user

##### Returns
 |
 | Return type | Description
 | UserDetails | id, name and email of currently logged user.

 Note: If the Dynatrace JavaScript runtime isn't available, a default UserDetails placeholder object with values ('dt.missing.user.id', 'dt.missing.user.name', 'dt.missing.user.email') will be returned and a warning will be logged to the console.Code example
`tsx
import { getCurrentUserDetails } from '@dynatrace-sdk/platform/app-environment';// Get the details of the currently logged-in userconst userDetails = getCurrentUserDetails();// Use destructuring to extract specific propertiesconst { id, name, email } = getCurrentUserDetails();
`

#### getEnvironmentId

getEnvironmentId(): stringRetrieves the environment id.

##### Returns
 |
 | Return type | Description
 | string | environment id on which app is run.

 Note: If the Dynatrace JavaScript runtime isn't available, 'dt.missing.environment.id' will be returned and a warning will be logged to the console.Code example
`tsx
import { getEnvironmentId } from '@dynatrace-sdk/platform/app-environment';// Get the current environment IDconst environmentId = getEnvironmentId();
`

#### getEnvironmentUrl

getEnvironmentUrl(): stringRetrieves the environment url.

##### Returns
 |
 | Return type | Description
 | string | environment url on which app is run.

 Note: If the Dynatrace JavaScript runtime isn't available, 'https://dynatrace.com/' will be returned and a warning will be logged to the console.Code example
`tsx
import { getEnvironmentUrl } from '@dynatrace-sdk/platform/app-environment';// Get the current environment URLconst environmentUrl = getEnvironmentUrl();
`

### Types

#### UserDetails

Information about currently logged user

##### Properties

 |
 | Name | Type
 | email*required | string
 | id*required | string
 | name*required | string
