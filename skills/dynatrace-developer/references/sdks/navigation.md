# @dynatrace-sdk/navigation

Source: <https://developer.dynatrace.com/develop/sdks/navigation/> (latest: `navigation`).

## navigation

`/develop/sdks/navigation/`

- SDK for TypeScript
- Navigation

## Navigation
Navigate within the AppEngine and send Intents from one app to another.

 @dynatrace-sdk/navigation v2.2.0 Latest (V2)

`tsx
npm install @dynatrace-sdk/navigation
`

### Functions

#### getAppLink

getAppLink(appId,pageToken?): stringGenerates a link that launches the specified app on current environment, with an optional internal route specified by pageTokenNote: There is no guarantee that the specified app will be launched since different sets of apps could be installed on different platform instances.
Relying on explicitly hardcoded app could lead to broken UX.Note: A page token isn't a URL or route within your app.
It's a specific identifier in your app manifest that serves as a public API for navigation purposes.
App developers need to explicitly define these tokens in their manifest.
Learn more about registering page tokens for routes.

##### Parameters
 |
 | Name | Type | Description
 | appId*required | string | ID of the app that will be launched.
 | pageToken | string | Id of the static path segment defining an internal route in app. Warning: not the same thing as URL or route.

##### Returns
 |
 | Return type | Description
 | string | URL to the specified app on current environment.

#### getDocumentLink

getDocumentLink(documentId): stringGenerates a link that opens the specified document on current environment.Note: Due to varying document availability across environments, there's no guarantee the link will always successfully open the document.

##### Parameters
 |
 | Name | Type | Description
 | documentId*required | string | The unique identifier (UUID or external ID) of the document to open.

##### Returns
 |
 | Return type | Description
 | string | A URL for the document in the current environment.

#### getIntent

getIntent(): Intent | nullRetrieves the intent data passed to the app.`getIntent` method should be used only if the current app route is the intent handling route (`/intent/:intentId`). Otherwise, it returns `null`.Note: The intent is passed to the destination app via the intent handling route (`/intent/:intentId`).
If the app has routing already configured, a new route for handling intents must be declared. Otherwise, it won't be possible to retrieve the intent.
If the app has no routing at all, it's not required to configure it.
To register intents your app can handle, you must declare them in your app manifest.
Learn more about declaring the intents.

##### Returns
 |
 | Return type | Description
 | Intent | Intent accessor, including definition of desired action (intent id) and its payload.

#### getIntentLink

getIntentLink(intentPayload): stringGenerates a link that launches the App Shell on current environment and lets it handle the specified intent.Note: There is no guarantee that the specified app will be launched since different sets of apps could be installed on different platform instances.
Relying on explicitly hardcoded app could lead to broken UX.

##### Parameters
 |
 | Name | Type | Description
 | intentPayload*required | IntentPayload | Set of properties to pass to the platform.

##### Returns
 |
 | Return type | Description
 | string | URL to the specified intent on current environment.
getIntentLink(intentPayload,appId?,intentId?): stringGenerates a link that launches the specified app on current environment and lets it handle the specified intent of given id.Note: There is no guarantee that the specified app will be launched since different sets of apps could be installed on different platform instances.
Relying on explicitly hardcoded app could lead to broken UX.

##### Parameters
 |
 | Name | Type | Description
 | intentPayload*required | IntentPayload | Set of properties to pass to the specified app.
 | appId | string |
 | intentId | string | ID of the action that will be passed to the app.

##### Returns
 |
 | Description
 | URL to the specified intent on current environment.

#### openApp

openApp(appId,pageToken?): voidNavigates user to the specified app, or its internal route if the `pageToken` is specified.Note: A page token isn't a URL or route within your app.
It's a specific identifier in your app manifest that serves as a public API for navigation purposes.
App developers need to explicitly define these tokens in their manifest.
Learn more about registering page tokens for routes.
Note: There is no guarantee that the specified app exists since different sets of apps could be installed on different platform instances.
Relying on explicitly hardcoded app could lead to broken UX.

##### Parameters
 |
 | Name | Type | Description
 | appId*required | string | ID of the app that will be launched.
 | pageToken | string | Id of the static path segment defining an internal route in app. Warning: not the same thing as URL or route.

#### openDocument

openDocument(documentId): voidNavigates the user to the specified document on current environment.Note: Due to varying document availability across environments, this function might not open the document if it doesn't exist in the environment.

##### Parameters
 |
 | Name | Type | Description
 | documentId*required | string | The unique identifier (UUID or external ID) of the document to navigate to.

#### sendIntent

sendIntent(intentPayload): voidPasses the specified `IntentPayload` to the Dynatrace platform, which then gets forwarded to the destination app selected by the user.Note: The list of possible actions and destination apps includes only these actions/apps whose intent declarations are matched against the intent payload.
The matching checks whether the payload contains all the properties required in the intent declaration and whether the properties have the correct types.
All the undeclared properties are removed from the intent payload when passing it to the destination app.

##### Parameters
 |
 | Name | Type | Description
 | intentPayload*required | IntentPayload | an intent payload object to pass, it may include one or more properties
sendIntent(intentPayload,sendIntentOptions): voidPasses the specified `IntentPayload` to the specified app and lets it handle the specified intent of given id.
If the specified app does not exist or the specified intent payload does not match,
Dynatrace platform handles the intent as if regular `sendIntent(intentPayload: IntentPayload)` is used.Note: There is no guarantee that the specified app will be launched since different sets of apps could be installed on different platform instances.
And even if the app is installed, its version may not be capable of handling the specified intent payload.

##### Parameters
 |
 | Name | Type | Description
 | intentPayload*required | T | an intent payload object to pass, it may include one or more properties
 | sendIntentOptions*required | SendIntentOptions | an options object with:

- recommendedAppId - ID of the app that will be launched to handle the intent
- recommendedIntentId - ID of the action that will be passed to the app
- keyProperties - list of property names of the intent payload that must be matched with intent declarations

#### sendIntentWithResponse

sendIntentWithResponse(intentPayload,sendIntentWithResponseOptions): Promise | undefined>Unlike regular `sendIntent` method, it requests what properties will be returned by the specified app handling the specified intent of given id.Note: The list of possible actions and destination apps includes only these actions/apps whose intent declarations are matched against the intent payload and response properties.

##### Parameters
 |
 | Name | Type | Description
 | intentPayload*required | IntentPayload | an intent payload object to pass, it may be empty when sending an intent with response
 | sendIntentWithResponseOptions*required | SendIntentWithResponseOptions | an options object with:

- responseProperties - expected intent response, requested as a list of property names
- recommendedAppId - ID of the app that will be launched to handle the intent
- recommendedIntentId - ID of the action that will be passed to the app

#### setPathChangeHandler

setPathChangeHandler(handler): voidRegisters a custom handler for changing the app's URL path.
It is used only for the changes that are triggered externally, outside the app.If a custom handler is not set, the application is reloaded
by replacing the current document location with a new path.

##### Parameters
 |
 | Name | Type | Description
 | handler*required | PathChangeHandler | Custom handler for changing the app's URL path.

### Types

#### Intent

Intent accessor API for retrieving received intent.

Use it to retrieve the intent payload passed from the source app and the intent id selected by the user.

##### Methods

###### getId

getId(): stringRetrieves the intent id selected by the user.It is passed via the intent handling route (`/intent/:intentId`).

##### Returns
 |
 | Return type | Description
 | string | intent id

###### getPayload

getPayload(): IntentPayloadRetrieves the intent payload object that was passed from the source app.It contains only these properties that are declared in the app manifest.

##### Returns
 |
 | Return type | Description
 | IntentPayload | Intent payload

###### getProperty

getProperty(propertyName): anyRetrieves value of a given property name from the intent payload.

##### Parameters
 |
 | Name | Type
 | propertyName*required | string

#### IntentPayload

Set of properties that could be passed between apps.

Note: The intent payload contains one or more properties. The properties may be a resource-like (i.e., `dt.entity`, `dt.query`) and may define an additional context (i.e., chosen timeframe, associated problem)
Intents mechanism is the essential part of the platform navigation. It allows to pass the user flow from one app to another and provides the way to plug different apps into these flows, making the platform open and extendable.
Use sendIntent to pass the intent payload to the platform.
Use getIntent to handle intents in your app.

#### IntentResponseErrorEnvelope

##### Properties

 |
 | Name | Type
 | error*required | IntentError
 | ok*required | false

#### IntentResponseOkEnvelope

##### Properties

 |
 | Name | Type
 | data*required |
 | ok*required | true
