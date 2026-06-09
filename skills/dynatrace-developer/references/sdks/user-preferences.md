# @dynatrace-sdk/user-preferences

Source: <https://developer.dynatrace.com/develop/sdks/user-preferences/v1/> (latest: `user-preferences/v1`).

## user-preferences/v1

`/develop/sdks/user-preferences/v1/`

- SDK for TypeScript
- User Preferences
- V1

## User Preferences
Obtain the currently logged-in user preferences, like theme or language.

 @dynatrace-sdk/user-preferences v1.1.4 

`tsx
npm install @dynatrace-sdk/user-preferences
`

### Functions

#### getLanguage

getLanguage(): stringRetrieves the user preferred language.

##### Returns
 |
 | Return type | Description
 | string | language defined in user preferences.Code example
`tsx
// Import the getLanguage functionimport { getLanguage } from '@dynatrace-sdk/user-preferences';// Get the user's language preferenceconst language = getLanguage();
`

#### getRegionalFormat

getRegionalFormat(): stringRetrieves the user regional format.

##### Returns
 |
 | Return type | Description
 | string | regional format defined in user preferences.Code example
`tsx
// Import the getRegionalFormat functionimport { getRegionalFormat } from '@dynatrace-sdk/user-preferences';// Get the user's regional format preferenceconst regionalFormat = getRegionalFormat();
`

#### getTheme

getTheme(): ThemeTypeRetrieves the user preferred theme.

##### Returns
 |
 | Return type | Description
 | ThemeType | theme defined in user preferences.Code example
`tsx
// Import the getTheme functionimport { getTheme } from '@dynatrace-sdk/user-preferences';// Get the user's theme preferenceconst theme = getTheme();
`

#### getTimezone

getTimezone(): stringRetrieves the user preferred timezone.Timezone can be either in ISO 8601 or tz database format.

##### Returns
 |
 | Return type | Description
 | string | timezone defined in user preferences.Code example
`tsx
// Import the getTimezone functionimport { getTimezone } from '@dynatrace-sdk/user-preferences';// Get the user's timezone preferenceconst timezone = getTimezone();
`
