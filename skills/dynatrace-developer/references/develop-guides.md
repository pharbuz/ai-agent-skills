# Develop — Guides

Scraped from <https://developer.dynatrace.com/develop/>. Each section is one doc page (its path is shown) with the prose and code captured.

## access-platform-apis-from-outside

`/develop/guides/access-platform-apis-from-outside/`

- Access platform APIs

## Access platform APIs from outside

- How-to guide
- 3-min readThe Dynatrace platform provides a set of platform APIs you can call in your Dynatrace app via their relative URL. The same is true for the app functions you deploy with your app. The platform will handle the authentication and routing to the right environment for you. However, if you want to call one of these APIs from outside the platform, for example, from any shell script, you need to follow some additional steps.

### Use the correct URL

You need to use the absolute URL of the respective API endpoint to call a platform API or app function from outside the platform.
The URL for platform APIs is always following the following pattern: `https://abc12345.apps.dynatrace.com/platform/`

App functions are available via this URL pattern: `https://abc12345.apps.dynatrace.com/platform/app-engine/app-functions/v1/apps//api/`

A complete list of available platform APIs is available in the SwaggerUI of your environment. You can find a link to swagger by using the in-product search and searching for "Dynatrace API" or access it via `/platform/swagger-ui/index.html`

NoteYou need to replace the placeholders ,, and with your values.

### Authentication

Classical authentication methods like username and password aren't suitable for machine-to-machine communication, such as shell scripts or backend services. On the Dynatrace platform, there are two supported methods for authenticating API access:

- OAuth Client Credentials Flow – Recommended for enterprise-grade integrations, delegated access, and secure automation.

- Platform tokens – A simpler alternative for individual users, scripts, or internal tools.

This guide focuses on the OAuth Client Credentials Flow, where your script or service authenticates using a Client ID and Client Secret to obtain an access token for API calls.

NoteIf you're looking for a more straightforward setup for personal or internal use, consider using a Platform token, which can be used directly in the `Authorization: Bearer ` header.
The following diagram illustrates this OAuth-based workflow:

### Create an OAuth client

Before you can call an API from outside the platform, you need to create an OAuth client with the required scopes for yourself or your team. Currently, only account admins can create OAuth clients.

To create a new OAuth client, do the following steps:

- Go to account settings.

- Select the desired account

- Navigate to Identity & access management and select OAuth clients.

- Click the Create client button.

- Fill in the service user email field and, optionally, the description of your OAuth client.

- After selecting the appropriate OAuth permissions, click the Create client button at the bottom of the page to generate the OAuth client.

- Ensure you copy the generated client secret immediately and store it safely since you'll only be able to see it once.

### Get Bearer token and call app function

As described above, you need to pass a Bearer token to authenticate API calls. You need to retrieve the Bearer token from the `token` endpoint of the SSO API.

#### Example

The following example shows how you can call the `calculate` function from your `my.custom.app` app via curl from outside the platform.
First, you have to get a Bearer token from the SSO. You have to specify your client id, the corresponding client secret, and the scope for which you want to get a Bearer token.

`tsx
curl --request POST 'https://sso.dynatrace.com/sso/oauth2/token' \--header 'Content-Type: application/x-www-form-urlencoded' \--data-urlencode 'grant_type=client_credentials' \--data-urlencode 'client_id={your-client-id}' \--data-urlencode 'client_secret={your-client-secret}' \--data-urlencode 'scope=app-engine:apps:run storage:buckets:read storage:logs:read'
`

NoteIn this example `app-engine:apps:run` and `storage:logs:read` are passed as scopes. `app-engine:apps:run` is always needed to access any function of your custom app.
This request returns the following response object, including the Bearer token you must pass to the actual API call.

`tsx
{ "scope": "app-engine:apps:run storage:buckets:read storage:logs:read", "token_type": "Bearer", "expires_in": 300, "access_token": "{your-bearer-token}", "resource": "urn:dtaccount:{dynatrace-account-urn}"}
`

After getting a Bearer token, you can now call the API endpoint by passing this exact Bearer token via an authorization header:

`tsx
curl --request GET 'https://abc12345.apps.dynatrace.com/platform/app-engine/app-functions/v1/apps/my.custom.app/api/calculate' \--header 'Authorization: Bearer {your-bearer-token}'
`

### Related topics

- Create and consume app function

- OAuth Client Credentials Flow

---

## app-functions

`/develop/guides/app-functions/`

- App functions

## App functions

- Explanation
- 4-min readApp functions represent an app's backend. They're built, bundled, and deployed together with your Dynatrace app. The App Toolkit makes developing and deploying app functions easy.

Every TypeScript file in your project's `/api` directory is automatically deployed as an app function and exposed as an API endpoint.

Currently, you can deploy functions built with JavaScript/TypeScript, which run within the Dynatrace JavaScript runtime. To see the list of supported APIs, visit Web APIs

### Use cases

When does it make sense to use app functions? The most important use cases are:

- Accessing third-party APIs over the internet that you want to use within your app

- Heavy data processing that ideally shouldn't take place in the browser

- Data wrangling to make the data easily consumable within the app's web UI

- Requests that need credentials for authentication that you don't want to expose in the app's UI code

NoteSince app functions require some setup effort, only use them for these use cases. For example, you don't need an app function to execute a DQL query. Instead, you can query directly in your app's UI code. Most of the time, accessing external APIs or data is the use case that will apply to you.

### Function interface

The Dynatrace JavaScript runtime expects a single default function exported from your function files. This function can contain a single `payload` parameter, which is the request body of the incoming request.

Each input to your function needs to pass through the function body. You can consume it via the `payload` parameter in your function.

Here's an example:

api/hello-world.function.ts
`tsx
export default (payload) => { return 'Hello World';};
`

### Logs

Since the app functions run in the Dynatrace JavaScript runtime environment, you can use all the `console` methods such as `console.log`, `console.info`, `console.warn`, and `console.error` in your code.

They'll appear in your terminal when you run them locally. However, when you deploy the app, all the logs are stored in Grail. To learn more, have a look at Accessing app function logs.

### HTTP status code

Each time you run an app function, it returns a specific response type that includes the HTTP status code. The following table explains each HTTP status code, and the reason behind the code:

 |
 | HTTP code | Reason | Definition
 | 200 | No Error | Function executed successfully.
 | 400 | Bad request | The app function can't or won't process the request due to perceived client error—for example, malformed request syntax, etc.
 | 404 | The app or the function name wasn't found | The app or function doesn't exist.
 | 409 | The app's backend is being deployed and isn't able to serve requests yet | The app's backend can't serve the request because it's currently being deployed.
 | 500 | Internal server error | The app function encountered something unexpected and couldn't fulfill the request.
 | 540 | JavaScript errors, event loop errors | There is an error in the application code. It can be TypeError, JavaScript error, unhandled exceptions, or event loop error.
 | 541 | Runtime errors (Mem exceeded, Timeout, etc.) | This is an error thrown by the runtime. It can occur because the code exceeds the timeout or memory limit.

### Runtime limitations

Read more about capabilities and limitations of the Dynatrace Javascript Runtime here: JavaScript runtime.

###

#### Allow external requests
Enable request to external hosts.How-to guide

#### Create and consume app function
Create an app function for your Dynatrace App.How-to guide

#### Handle errors in app functions
Handle errors in app functions within your Dynatrace Apps.How-to guide

#### Pass input to functions
Send dynamic content to your app functions.How-to guide

### Related topics

- Automate app function runs

- JavaScript runtime

---

## app-functions/allow-outbound-connections

`/develop/guides/app-functions/allow-outbound-connections/`

- App functions
- Allow external requests

## Allow external requests

- How-to guide
- 1-min readExternal requests from functions are not allowed by default due to security restrictions. Learn how to configure the environment to access external hosts from app functions and ad-hoc functions.

### Add a host to the allowlist

To perform a call to an external host, you need to allow requests to this host.
Open the `Settings` app from the Dynatrace Launcher on your environment and select `General` from the side menu. You will find `External requests` in the `Environment management` group.

NoteAfter adding or modifying the allowed hosts, the change might take up to 10 seconds.
You can configure allowed hosts by IP address or DNS name. DNS names with at least three segments can start with wildcards.

Examples for allowed entries:

`tsx
123.123.123.123www.example.comapi.example.com*.api.example.com*.example.com
`

Examples for invalid entries:

`tsx
http://123.123.123.123 # Protocol must not be part of the entryhttps://example.com # Protocol must not be part of the entryexample.com/api # Only the domain is allowed*.com # Wildcards are only allowed with at least three segments123.*.123.123 # Wildcards are not allowed for IP addresses*api.example.com # Wildcards must match a whole segmentapi.*.example.com # Wildcards must be at the beginning of the entry
`

You can also turn off allowlist enforcement to allow connections to any external host.

CautionDisabling the allowlist enforcement permits connections to any external host, which can pose significant security risks.

---

## app-functions/create-consume

`/develop/guides/app-functions/create-consume/`

- App functions
- Create and consume

## Create and consume app function

- How-to guide
- 2-min readFor specific use cases within your app, such as querying third-party data, heavy data processing, and others, you need to utilize app functions as part of your app.

This guide shows you how to create an app function and how you can consume this function.

### Create a new app function

The App Toolkit helps you to create a new app function easily. It provides you with a command that creates a function file with an example function.

Execute this command in your project directory:

`tsx
npx dt-app function create function-name>
`

The App Toolkit creates a file with the function's name in the `api` directory within your root project directory.
Every created TypeScript file in the api directory is exposed as an app function via the relative URL `/api/filename`.

The created function file already contains the function signature together with a very basic example:

api/hello-world.function.ts
`tsx
export default async function (payload: unknown) { return 'Hello world';}
`

### Consume the function

There are multiple places from which you can consume the app function. You can consume it in your Dynatrace App, from a Notebook, Workflow, or from outside the platform.

#### In your app code

To consume the app function in your app, you can use the `useAppFunction` hook provided by the `@dynatrace-sdk/react-hooks` package. Install it with the following command:

`tsx
npm install @dynatrace-sdk/react-hooks
`

Now you can use it in your component:

ui/app/App.tsx
`tsx
import React from 'react';import { useAppFunction } from '@dynatrace-sdk/react-hooks';export const App = () => { const response = useAppFunctionstring>({ name: 'hello-world', responseType: 'text', }); return ( > {response.isLoading && p>Loading...p>} {response.data && p>{response.data}p>} > );};
`

#### From Notebooks or Workflows

The `@dynatrace-sdk/adhoc-utils` package allows you to call app functions exposed by an app from Notebooks or Workflows.

The `call` function exposed by the `functions` namespace expects both the `appId` and the `functionName` as well as an optional `data` parameter to pass in the function payload:

`tsx
import { functions } from '@dynatrace-sdk/adhoc-utils';const response = await functions.call('my.app.id', 'hello-world').then((res) => res.text());
`

#### From outside the platform

App functions are exposed via a public API endpoint and can be called from anywhere outside the platform.
When calling your function from outside the platform, you need to consider the following points:

- You need to call the absolute API URL address

- `https://abc12345.apps.dynatrace.com/platform/app-engine/app-functions/v1/apps//api/`

- You need to take care of authentication by yourself. App function requests are authenticated via OAuth. Read Access platform APIs from outside for more details.

After obtaining a Bearer token from the single sign-on (SSO) token endpoint, a curl request to your app function could look like this:

`tsx
curl --request GET 'https://abc12345.apps.dynatrace.com/platform/app-engine/app-functions/v1/apps/my.app.id/api/hello-world' \--header 'Authorization: Bearer {your-bearer-token}'
`

---

## app-functions/handle-errors

`/develop/guides/app-functions/handle-errors/`

- App functions
- Handle errors

## Handle errors in app functions

- How-to guide
- 2-min readIn case something isn't working as expected in your app function, you want to react accordingly on the function consumer's side.
This guide describes how to handle errors in your function code and report them back to the consumer.

### Return error code

By default, app functions return HTTP status code `200` if there's no error thrown.
If something unexpected happens in your function code, you can throw an error anytime, leading to an HTTP `540` status code returned by the app function.

This could look like this in case a call to a 3rd party API is failing in your function:

api/fetch-user.function.ts
`tsx
export default async function (): Promiseunknown> { const apiResponse = await fetch('https://dummyjson.com/users/1'); if (!apiResponse.ok) { throw new Error(); } return apiResponse.json();}
`

CautionThrowing an error in your app function leads to a generic `Execution crashed` error message. You can't create a custom error with this approach. If you want to report custom errors read the next section.

### Custom error reporting

If you want to report a different kind of error information back to your consumer based on the type of error you are facing, you can also include all kinds of error information in your return object.

The following example demonstrates how you could return a different response object with error information from the external API.

api/fetch-user-custom-error-reporting.function.ts
`tsx
interface Result { data: unknown; error?: string;}export default async function (): PromiseResult> { const apiResponse = await fetch('https://dummyjson.com/users/1'); if (!apiResponse.ok) { const responseText = await apiResponse.text(); return { data: null, error: 'External API failed to handle the request: ' + responseText, }; } const data = (await apiResponse.json()) as unknown; return { data, };}
`

---

## app-functions/pass-input

`/develop/guides/app-functions/pass-input/`

- App functions
- Pass input

## Pass input to functions

- How-to guide
- 2-min readIn many cases, you need to pass dynamic content to your app functions to perform a specific task based on it.
This guide will explain how to pass data to your function from within your app and how to process it accordingly.

### Send data to your function

Sending data to your app function is straightforward. To send the data, you can use the `useAppFunction` hook provided by the `@dynatrace-sdk/react-hooks` package.

In the following example, we're sharing types between app function and the function call for end-to-end type safety and then calling the app function:

shared/types.ts
`tsx
export type Input = { id: string; name: string; age: number;};
`

ui/app/App.tsx
`tsx
import React from 'react';import { Input } from '../shared/types';import { useAppFunction } from '@dynatrace-sdk/react-hooks';export const App = () => { const input: Input = { id: 'john-doe', name: 'John Doe', age: 38, }; const response = useAppFunction({ name: 'hello-world', data: input }); return >{JSON.stringify(response.data)}>;};
`

TipQuery string parameters and HTTP headers aren't passed to your function. Use the body of the HTTP request for any input of your function.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

### Consume payload in your function

You can access the data you passed to your function via the `payload` parameter. As mentioned above, you can benefit from all the advantages of TypeScript by using the same type for both your app code and your function code.
Your function would look like this eventually:

api/consume.function.ts
`tsx
import { Input } from '../shared/types';type Output = { result: string;};export default (payload: Input): Output => { return { result: 'Hello ' + payload.name, };};
`

---

## automate-dependency-updates

`/develop/guides/automate-dependency-updates/`

- Automate dependency updates

## Automate dependency updates

- How-to guide
- 1-min readWe strongly recommend you to keep your application dependencies up to date, as it helps mitigate security risks, resolve known bugs, and leverage the latest features available in your ecosystem.

We recommend using Renovate to automate dependency updates for your Dynatrace Apps. Below, we outline our recommended configuration to make sure your apps stay updated with our SDKs, CLI, and libraries.

### Presets

As a starting point, we have the presets `config:best-practices` and `config:js-app` for a general, ecosystem-agnostic set of dependency management rules. Among other configurations, `config:best-practices` includes `security:minimumReleaseAgeNpm` to make sure the packages we update have been published for at least three days, for the sake of security and stability.

renovate.json
`tsx
{ "extends": ["config:best-practices", "config:js-app"]}
`

### PackageRules

We have divided our custom `packageRules` into four.

First, all the patches on strato dependencies will be grouped together and have a higher priority.

renovate.json
`tsx
{ "groupName": "Strato - Patches", "description": "Update Strato patches with priority, without migrations", "enabled": true, "matchPackageNames": ["@dynatrace/strato-**"], "matchUpdateTypes": ["patch"], "prPriority": 1}
`

- Second, all minor and major versions of Strato dependencies are grouped together, updated once a week, and have the proper migrations applied automatically, if available.

renovate.json
`tsx
{ "groupName": "Strato", "description": "Weekly Strato update with migrations", "matchPackageNames": ["@dynatrace/strato-**"], "matchUpdateTypes": ["major", "minor"], "postUpgradeTasks": { "commands": [ "npm ci --ignore-scripts", "npx dt-app migration execute --package \"{{{depName}}}\" --from \"{{{currentVersion}}}\" --to \"{{{newVersion}}}\"", "npx eslint . --fix" ], "executionMode": "update" }, "schedule": ["on monday"]}
`

- Third, all major and minor versions of `dt-app` are updated and migrated automatically.

renovate.json
`tsx
{ "matchPackageNames": ["dt-app"], "description": "dt-app updates with migrations", "matchUpdateTypes": ["major", "minor"], "postUpgradeTasks": { "commands": [ "npm ci --ignore-scripts", "npx dt-app migration execute --package \"{{{depName}}}\" --from \"{{{currentVersion}}}\" --to \"{{{newVersion}}}\"", "npx eslint . --fix" ], "executionMode": "update" }}
`

- Finally, the rest of Dynatrace libraries and SDKs are updated independently regardless of the update type, to have smaller PRs which are less likely to have a failed build. Additionally, you can ignore an update by declining the PR, since it won't be triggered again, which isn't the case for groups.

renovate.json
`tsx
{ "description": "All Dynatrace packages have increased update frequency", "matchPackageNames": ["@dynatrace/**", "@dynatrace-sdk/**"], "minimumReleaseAge": "0 days", "internalChecksFilter": "strict"}
`

### Complete configuration example

renovate.json
`tsx
{ "$schema": "https://docs.renovatebot.com/renovate-schema.json", "extends": ["config:best-practices", "config:js-app"], "timezone": "Europe/Vienna", "npmrcMerge": true, "enabledManagers": ["npm"], "baseBranches": ["main"], "packageRules": [ { "description": "All Dynatrace packages have increased update frequency", "matchPackageNames": ["@dynatrace/**", "@dynatrace-sdk/**"], "minimumReleaseAge": "0 days", "internalChecksFilter": "strict" }, { "matchPackageNames": ["dt-app"], "description": "dt-app updates with migrations", "matchUpdateTypes": ["major", "minor"], "postUpgradeTasks": { "commands": [ "npm ci --ignore-scripts", "npx dt-app migration execute --package \"{{{depName}}}\" --from \"{{{currentVersion}}}\" --to \"{{{newVersion}}}\"", "npx eslint . --fix" ], "executionMode": "update" } }, { "groupName": "Strato", "description": "Weekly Strato update with migrations", "matchPackageNames": ["@dynatrace/strato-**"], "matchUpdateTypes": ["major", "minor"], "postUpgradeTasks": { "commands": [ "npm ci --ignore-scripts", "npx dt-app migration execute --package \"{{{depName}}}\" --from \"{{{currentVersion}}}\" --to \"{{{newVersion}}}\"", "npx eslint . --fix" ], "executionMode": "update" }, "schedule": ["on monday"] }, { "groupName": "Strato - Patches", "description": "Update Strato patches with priority, without migrations", "enabled": true, "matchPackageNames": ["@dynatrace/strato-**"], "matchUpdateTypes": ["patch"], "prPriority": 1 } ]}
`

For more information, refer to the official Noise Reduction guide on how to get a smooth Renovate bot experience, and to Dependency pinning for more stable updates.

---

## code-optimization

`/develop/guides/code-optimization/`

- Code optimization

## Code optimization

- Concept
- 1-min readOptimizing your app's code is crucial for delivering a fast and responsive user experience. By reducing the size of your JavaScript bundles and loading code on demand, you can significantly improve your app's load times and performance.

###

#### Lazy loading quickstart
Improve your Dynatrace app's load performance by splitting your code into smaller chunks and implementing lazy loading.How-to guide

#### Understand lazy loading
Learn the principles of lazy loading in React and how to apply it effectively in your Dynatrace app to optimize load performance and Core Web Vitals.Explanation

---

## code-optimization/lazy-loading

`/develop/guides/code-optimization/lazy-loading/`

- Code optimization
- Understand lazy loading

## Understand lazy loading

- New
- Explanation
- 14-min readCode splitting is about breaking your app into smaller bundles so you're not shipping everything upfront, while lazy loading is about delaying the loading of those bundles until they're actually needed. In practice, code splitting makes lazy loading possible, and lazy loading is how you get the real performance wins from those split chunks. Together, they keep initial loads fast and only download code when the user hits the feature that needs it.

The App Toolkit now supports fine-grained asynchronous module loading via React's `lazy()` method and `Suspense` component. This allows you to split your app bundle into smaller chunks that are loaded on demand, reducing initial load times, improving time-to-interactive, and keeping your Core Web Vitals in check. Core Web Vitals are Google's metrics for measuring real-world user experience:

LCP (Largest Contentful Paint)—measures loading performance. It marks when the largest visible element such as an image, text block, or video finishes rendering.

INP (Interaction to Next Paint)—measures interactivity and responsiveness. It tracks the delay between a user interaction such as a click, tap, or key press and the next visual update.

CLS (Cumulative Layout Shift)—measures visual stability. It scores how much page elements unexpectedly shift during the page's lifetime. For example, an image loads and pushes content down.

Kick off lazy loading on your Dynatrace appTo learn how to enable code splitting in your Dynatrace app, see Lazy loading quickstart.

### How it works

React's `lazy()` method accepts a function that returns a dynamic `import()`. The returned component is loaded asynchronously and must be rendered inside a component boundary that provides a fallback UI while the chunk is in flight.

See the following example of lazy loading a heavy component:

ui/app/App.tsx
`tsx
import React, { lazy, Suspense } from 'react';import { ProgressBar } from '@dynatrace/strato-components/content';const HeavyComponent = lazy(() => import('./components/HeavyComponent'));export const App = () => ( Suspense fallback={ProgressBar />}> HeavyComponent /> Suspense>);
`

The component module is only fetched when is first rendered. Subsequent renders use the cached module and there is no per-render overhead.

### Route-based lazy loading

The highest-impact and lowest-risk place to introduce lazy loading is at the route level. Each page of your app is already a natural boundary: users navigate to one page at a time, and there is an inherent expectation of a brief transition between pages.

#### Before

A typical Dynatrace app imports all page components eagerly in `App.tsx`:

ui/app/App.tsx
`tsx
import React from 'react';import { Route, Routes } from 'react-router-dom';import { Overview } from './pages/Overview';import { HostDetails } from './pages/HostDetails';import { Settings } from './pages/Settings';import { Changelog } from './pages/Changelog';export const App = () => ( Routes> Route path="/" element={Overview />} /> Route path="/host/:id" element={HostDetails />} /> Route path="/settings" element={Settings />} /> Route path="/changelog" element={Changelog />} /> Routes>);
`

Every page and all of its transitive dependencies ship in the initial bundle regardless of which route the user actually navigates to.

#### After

Replace static imports with `lazy()` and wrap your route tree in a boundary:

ui/app/App.tsx
`tsx
import React, { lazy, Suspense } from 'react';import { Route, Routes } from 'react-router-dom';import { ProgressBar } from '@dynatrace/strato-components/content';const Overview = lazy(() => import('./pages/Overview'));const HostDetails = lazy(() => import('./pages/HostDetails'));const Settings = lazy(() => import('./pages/Settings'));const Changelog = lazy(() => import('./pages/Changelog'));export const App = () => ( Suspense fallback={ProgressBar />}> Routes> Route path="/" element={Overview />} /> Route path="/host/:id" element={HostDetails />} /> Route path="/settings" element={Settings />} /> Route path="/changelog" element={Changelog />} /> Routes> Suspense>);
`

Now only the code for the active route is fetched on initial load. Navigating to `/settings` triggers a network request for the Settings chunk, with the fallback shown until it resolves.

#### Default exports

`React.lazy()` expects the dynamically imported module to have a default export containing the React component. Make sure your page modules export accordingly:

ui/app/pages/Settings.tsx
`tsx
import React from 'react';const Settings = () => { return div>Settingsdiv>; // ...};export default Settings;
`

If your component uses a named export, wrap the import:

ui/app/App.tsx
`tsx
const Settings = lazy(() => import('./pages/Settings').then((module) => ({ default: module.Settings })));
`

The default export pattern is cleaner. If you're introducing lazy loading to an existing app, switching page entry points to default exports is a reasonable refactor.

### View-based lazy loading

Not every meaningful split is a route. Within a single page, you often have distinct views or panels that the user doesn't see upfront such as tabs, drawers, detail panels, modals, or expandable sections. These are the next tier of lazy loading candidates.

#### When to lazy load a view

Apply lazy loading to in-page views when:

- The view is behind an interaction—a tab the user has to click, a drawer that opens, a modal triggered by a button. The user expects a brief moment of loading when they perform the action.

- The view has significant weight—it pulls in heavy dependencies (charting libraries, complex forms, code editors) or renders large component trees.

- The view is not on the default visible area—a secondary tab, an "Advanced" section, a detail panel that appears on row selection.

TipDon't lazy load things that are visible immediately on page render. If a component is above the fold and visible on initial paint, eagerly load it; lazy loading it just delays the LCP with no benefit.

#### Example: tabbed layout

ui/app/pages/HostDetails.tsx
`tsx
import React, { lazy, Suspense } from 'react';import { Tabs, Tab } from '@dynatrace/strato-components/navigation';import { Skeleton } from '@dynatrace/strato-components/content';// The overview tab is the default — load it eagerlyimport { OverviewTab } from './tabs/OverviewTab';// Secondary tabs are lazy loadedconst MetricsTab = lazy(() => import('./tabs/MetricsTab'));const LogsTab = lazy(() => import('./tabs/LogsTab'));const ConfigTab = lazy(() => import('./tabs/ConfigTab'));export const HostDetails = () => ( Tabs> Tab title="Overview"> OverviewTab /> Tab> Tab title="Metrics"> Suspense fallback={Skeleton />}> MetricsTab /> Suspense> Tab> Tab title="Logs"> Suspense fallback={Skeleton />}> LogsTab /> Suspense> Tab> Tab title="Configuration"> Suspense fallback={Skeleton />}> ConfigTab /> Suspense> Tab> Tabs>);export default HostDetails;
`

The default `Overview` tab loads eagerly because it's visible immediately. Secondary tabs load their chunks only when selected. The fallback matches the expected layout shape, avoiding jarring layout shifts.

#### Example: modal or drawer

ui/app/components/HostActions.tsx
`tsx
import React, { lazy, Suspense, useState } from 'react';import { Button } from '@dynatrace/strato-components/buttons';import { Modal } from '@dynatrace/strato-components/overlays';import { ProgressBar } from '@dynatrace/strato-components/content';const BulkEditForm = lazy(() => import('./BulkEditForm'));export const HostActions = () => { const [isOpen, setIsOpen] = useState(false); return ( > Button onClick={() => setIsOpen(true)}>Bulk EditButton> {isOpen && ( Modal title="Bulk Edit" show onDismiss={() => setIsOpen(false)}> Suspense fallback={ProgressBar />}> BulkEditForm onClose={() => setIsOpen(false)} /> Suspense> Modal> )} > );};
`

The chunk is only fetched when the modal opens. The `{isOpen && ...}` conditional rendering ensures the lazy component isn't even mounted until needed.

### Parallelizing chunk loading with Grail queries

A common pattern in Dynatrace apps is that the user navigates to a page that needs to run a heavy DQL query against Grail and render a complex visualization component. Without lazy loading, the browser first downloads the entire bundle (including the visualization code), then mounts the component, and only then fires the query. The user waits for both sequentially.

With lazy loading, you can kick off the Grail query and the chunk download at the same time. The query starts immediately in the parent component—which is already loaded—while the heavy child component streams in via a lazy import. By the time the chunk arrives, the query may already have results or at least a head start.

#### The pattern

The key insight is that `useDql` runs in the parent component that's already in the bundle. The lazy-loaded child only handles rendering the results. This decouples data fetching from component loading. See the following example:

ui/app/pages/TopologyPage.tsx
`tsx
import React, { lazy, Suspense } from 'react';import { useDql } from '@dynatrace-sdk/react-hooks';import { Skeleton } from '@dynatrace/strato-components/content';import { Paragraph } from '@dynatrace/strato-components/typography';// The visualization component is heavy — lazy load itconst HostTopologyMap = lazy(() => import('./HostTopologyMap'));export const TopologyPage = () => { // Query fires immediately when this page mounts — no waiting for the chunk const { data, isLoading, error } = useDql({ query: `fetch dt.entity.host | fieldsAdd tags, managementZones, hostGroupName | join [ fetch dt.entity.process_group | fieldsAdd run_hosts = runs_on[dt.entity.host], pg_name = entity.name | expand run_hosts ], on: { left[id] == right[run_hosts] }, fields: { pg_name } | fieldsAdd processGroups = pg_name | fields id, entity.name, tags, managementZones, hostGroupName, processGroups | sort entity.name asc | limit 500`, }); if (error) { return Paragraph>Error: {error.message}Paragraph>; } return ( Suspense fallback={Skeleton height={400} />}> HostTopologyMap data={data} isLoading={isLoading} /> Suspense> );};export default TopologyPage;
`

What's happening at runtime:

- User navigates to the topology page.

- `TopologyPage` is either already bundled, if it's the current route, or loaded via its own lazy boundary.

- Immediately on mount, `useDql` fires the Grail query. This is a network request to the backend.

- Simultaneously, React hits the boundary, which triggers the dynamic `import()` for the `HostTopologyMap` chunk. This is a network request for the JavaScript asset.

- Both requests fly in parallel. The fallback is shown until the chunk resolves.

- Once `HostTopologyMap` mounts, it receives `data` (possibly already resolved) and `isLoading` as props and renders accordingly.

Without this pattern, steps 3 and 4 would be sequential: first download everything, then mount, then query. The parallel approach can save seconds on pages with heavy queries and heavy visualization components.

#### When this matters most

This pattern has the highest impact when:

- The query is slow—complex joins, large result sets, or cross-entity lookups that take multiple seconds.

- The visualization component is heavy—topology maps, complex charts, or anything pulling in large rendering dependencies.

- Both conditions are true—which is often the case, since the pages that need heavy queries are usually the same pages that need heavy visualizations to display them.

TipFor lightweight queries that return in under 200ms, the parallelization gain is negligible. However, lazy-loading the component itself is still valuable for reducing initial bundle size.

### Finding the right boundary

Not every component should be lazy loaded. There's overhead involved: a new chunk, a network request, a `Suspense` boundary, or a fallback UI. The question is whether the code you're deferring is worth that trade-off.

#### Good candidates

 |
 | Pattern | Why
 | Pages / Routes | Natural navigation boundary. Users expect a brief transition. High impact because each page pulls in its own dependency tree.
 | Secondary tabs | Hidden behind interaction. Often heavy with dedicated data fetching and visualizations.
 | Modals and drawers | Not rendered until triggered. Can contain complex forms or detail views.
 | Settings / Configuration panels | Rarely visited. Often includes form libraries and validation logic.
 | Heavy visualization components | Charting, graphing, or topology views that import large rendering libraries.

#### Poor candidates

 |
 | Pattern | Why
 | Small, shared UI components | Buttons, labels, icons — the overhead of a lazy boundary far outweighs the bytes saved.
 | Components visible on initial render | Lazy loading them delays LCP. You're making the first paint worse, not better.
 | Deeply nested internal components | Splitting at too granular a level creates a waterfall of chunk requests.
 | Components used on every page | They'll be loaded on the first navigation regardless. Shared code belongs in the main bundle.

#### Rule of thumb

If you're deferring less than ~20-30 KB of uncompressed JavaScript, the overhead of a separate chunk probably isn't worth it. Focus on boundaries where you're deferring entire feature surfaces with their own dependency subtrees.

### Strato components and lazy loading

Larger Strato components from `@dynatrace/strato-components`—such as `DataTable`, `CodeEditor`, and complex charting components—already implement internal lazy loading. Their heavier rendering internals are split into separate chunks that load on demand. You don't need to wrap these in your own `lazy()`, their chunk splitting is handled transparently. This means your app benefits from Strato's internal optimizations automatically, as long as you keep Strato up to date.

What you should still lazy load is the page or view that uses these components. Even if `DataTable` handles its own internals, the page component that composes it with your app's data fetching, layout, and business logic is still worth deferring if it's behind a route or interaction boundary.

### Impact on Largest Contentful Paint (LCP)

Lazy loading directly influences your Largest Contentful Paint (LCP), which is the Core Web Vital that measures how quickly the largest visible element renders. The target is less than 2.5 seconds. The relationship isn't always straightforward though; lazy loading can improve or hurt LCP depending on where you apply it.

#### Why it helps

A monolithic bundle forces the browser to download, parse, and execute all of your app's JavaScript before anything renders. The LCP element—typically a data table, a chart, or a heading within the active page—can't paint until this work completes.

By splitting non-critical routes and views into separate chunks, you reduce the size of the initial bundle. Less JavaScript to parse means the browser reaches first render faster, which brings LCP forward.

##### Typical impact on a multi-page app

The numbers depend on your app, but the direction is consistent: less upfront JavaScript means faster LCP.

 |
 | Scenario | Initial bundle | LCP (approx.)
 | No lazy loading (4 pages, all eagerly loaded) | ~1.2 MB | ~3.8s
 | Route-level lazy loading (only active page in initial bundle) | ~450 KB | ~2.1s
 | Route + view-level lazy loading (secondary tabs deferred) | ~320 KB | ~1.7s

#### Where it can hurt

If you lazy load a component that is the LCP element itself—for example, the main data table or the primary heading on the landing page—you introduce an additional network round-trip before that element can render. The `Suspense` fallback such as a skeleton or a progress bar, renders first, and only after the chunk arrives does the actual LCP element paint. This delays LCP rather than improving it.

The rule is simple: the component responsible for your LCP element must be in the initial bundle. Everything else is a candidate for deferral.

#### Fallbacks and Cumulative Layout Shift (CLS)

Your `Suspense` fallback also matters for Cumulative Layout Shift (CLS). If the fallback has a different height or layout than the resolved component, the page shifts when the real content renders. This is why using components that approximate the final layout is important not just for perceived performance, but to keep CLS under the 0.1 threshold.

#### Measuring the effect

Use the browser Developer Tools Performance panel or Lighthouse to measure LCP before and after introducing lazy loading. Pay attention to:

- LCP element identification—make sure you know which element the browser considers the LCP. It may not be what you expect.

- Chunk waterfall—in the Network tab, verify that lazy chunks load in parallel with (or after) the initial bundle, not in a sequential waterfall.

- Suspense duration—the time between fallback render and actual component render is the cost of lazy loading that boundary. If it's consistently > 500ms for above-the-fold content, that boundary is in the wrong place.

### Guidelines

To recap, here are some best practices for applying lazy loading in your Dynatrace app:

Start at the route level—this is the highest leverage point and requires the least architectural change. Every app with more than one page should do this.

Default tab eagerly, secondary tabs lazily—if a page has a tabbed layout, load the initially visible tab eagerly and lazy load the rest.

Lazy load what's behind interactions—modals, drawers, expandable panels — anything that requires a user action to become visible is a safe lazy boundary.

Don't lazy load what's immediately visible—components that render above the fold on page load should be in the main bundle.

Match your fallback to the expected layout—use components that approximate the shape of the incoming content. Avoid full-page spinners for in-page views — they cause unnecessary layout shift.

Combine with error boundaries—always pair with an error boundary for lazy-loaded content to degrade gracefully on network failures.

Keep Strato up to date—larger Strato components from `@dynatrace/strato-components` handle their own internal lazy loading. Staying current ensures you benefit from ongoing bundle optimizations.

### Related topics

- Lazy loading quickstart

- App toolkit

- React's lazy() method

---

## code-optimization/lazy-loading-quickstart

`/develop/guides/code-optimization/lazy-loading-quickstart/`

- Code optimization
- Lazy loading quickstart

## Lazy loading quickstart

- How-to guide
- 5-min readCode splitting breaks an app into smaller chunks so only the necessary code is loaded initially, reducing the upfront bundle size. Lazy loading then delays loading those chunks until they're actually needed, delivering the real performance gains by fetching code on demand.

When a user opens your app, the browser first downloads and parses `main.js`, the primary JavaScript bundle, before anything appears on screen. In large apps, this bundle can grow to several megabytes, causing slow initial load times. Keeping `main.js` below 1 MB is a good target; the smaller it is, the faster your app starts.

Lazy loading conceptsHere are the essential steps to enable code splitting in your Dynatrace app. For a more thorough explanation, see Understand lazy loading.

### Prerequisites

- `dt-app` CLI version 1.9.0 or higher.

### Steps

#### 1. Convert static route imports to lazy-loaded routes

Route-based splitting is the most impactful technique for most apps. Each route loads only the code it needs, so users navigating to the home page never download the code for the data page, and vice versa.

Replace static `import` statements for your page components with `React.lazy()` and wrap your routes in a `Suspense` boundary:

ui/app/App.tsx
`tsx
import { Page } from '@dynatrace/strato-components/layouts';import React, { Suspense, lazy } from 'react';import { Route, Routes } from 'react-router-dom';import { Header } from './components/Header';import { ProgressCircle } from '@dynatrace/strato-components/content';const Home = lazy(() => import('./pages/Home'));const Data = lazy(() => import('./pages/Data'));export const App = () => { return ( Page> Page.Header> Header /> Page.Header> Page.Main> Suspense fallback={ProgressCircle />}> Routes> Route path="/" element={Home />} /> Route path="/data" element={Data />} /> Routes> Suspense> Page.Main> Page> );};
`

Each page component must use a default export:

ui/app/pages/Home.tsx
`tsx
const Home = () => { return div>Welcome To Your Dynatrace Appdiv>;};export default Home;
`

ui/app/pages/Data.tsx
`tsx
const Data = () => { return div>Explore Datadiv>;};export default Data;
`

Note`React.lazy()` requires the dynamically imported module to have a default export containing a React component. If your pages use named exports, see the named exports section below.

##### Handle named exports

If your page components use named exports (for example, `export const Home = () => { ... }`), wrap the dynamic import to map the named export to a default export:

ui/app/App.tsx
`tsx
const Home = lazy(() => import('./pages/Home').then((module) => ({ default: module.Home })));
`

#### 2. Split heavy components

You can also split individual components that are heavy or not immediately visible. This is useful for components like charts, editors, or modals that add significant JavaScript weight but are only needed after user interaction.

For example, if your `Data` page includes a heavy chart library, lazy-load just the chart and add a button to trigger loading it:

ui/app/pages/Data.tsx
`tsx
import React, { Suspense, lazy, useState } from 'react';import { Button } from '@dynatrace/strato-components/buttons';import { Flex } from '@dynatrace/strato-components/layouts';import { Heading } from '@dynatrace/strato-components/typography';import { ProgressCircle } from '@dynatrace/strato-components/content';const DataChart = lazy(() => import('../components/DataChart'));export const Data = () => { const [isOpen, setIsOpen] = useState(false); return ( Flex flexDirection="column" padding={32}> Heading level={2}>Explore DataHeading> Button onClick={() => setIsOpen(true)}>Explore DataButton> {isOpen && ( Modal title="Explore Data" show onDismiss={() => setIsOpen(false)}> Suspense fallback={ProgressCircle />}> DataChart onClose={() => setIsOpen(false)} /> Suspense> Modal> )} Flex> );};
`

#### 3. Load non-component code on demand

For non-component code such as utility functions or data processing libraries, use dynamic `import()` directly. This gives you fine-grained control over when a module is loaded.

ui/app/pages/Data.tsx
`tsx
import React, { useState } from 'react';const Data = () => { const [result, setResult] = useState(null); const handleAnalyze = () => { void import('../utils/analyze').then(({ analyzeData }) => { setResult(analyzeData()); }); }; return ( div> button onClick={handleAnalyze}>Analyzebutton> {result && pre>{JSON.stringify(result, null, 2)}pre>} div> );};export default Data;
`

The `../utils/analyze` module is only downloaded when the user clicks the button.

#### 4. Add loading feedback to Suspense boundaries

Every `Suspense` boundary needs a `fallback` that shows while the chunk loads. Use Strato's `ProgressCircle` to give users visual feedback instead of a plain text placeholder. For example, the `MapView` component is large and benefits from a spinner while it loads:

ui/app/pages/Map.tsx
`tsx
import React, { Suspense, lazy } from 'react';import { Flex } from '@dynatrace/strato-components/layouts';import { ProgressCircle } from '@dynatrace/strato-components/content';const MapView = lazy(() => import('@dynatrace/strato-geo').then((mod) => ({ default: mod.MapView })));const Map = () => { return ( Flex flexDirection="column" padding={32}> Suspense fallback={ProgressCircle />}> MapView /> Suspense> Flex> );};export default Map;
`

#### 5. Build and verify

Build and deploy the app to confirm code splitting works by enabling code splitting in your build scripts:

`tsx
npx dt-app build --optimize --enable-code-splittingnpx dt-app deploy --optimize --enable-code-splitting
`

The build command creates a `dist` folder containing the compiled output. You should see multiple `.js` files instead of a single bundle, confirming that code splitting is active.

### Summary

 |
 | Technique | Best for | How it works
 | Route-based splitting | Pages / views | `React.lazy()` + `Suspense` on route components
 | Component-based splitting | Heavy components | `React.lazy()` + `Suspense` on individual components
Combine these techniques to progressively reduce your app's initial bundle size and improve load performance.

### Related topics

- Understand lazy loading

- App toolkit

---

## data

`/develop/guides/data/`

- Data

## Data

- Explanation
- 1-min readDynatrace provides different types of storage for different types of data. On this page, you'll see when to use which storage when working with Dynatrace Apps.

Following is the list of Dynatrace storage:

- Observability data: To store observability data, use Grail. Grail is a unified storage for logs, metrics, traces, events, etc. You can retrieve the data using Dynatrace Query Language. You can also ingest observability data from within our apps.

- App state: You might want to persist the state of your app across many sessions. You can do that using app state. The app state allows you to store user-specific states using user app states. To learn more, visit Store app and user states.

- User-generated content: If you want to persist user-generated content in your app, you can use document storage. To learn more, visit Store user-generated data.

- Settings: If you want to allow your app to be configurable by the environment administrator, you can use settings storage. You can also store secrets in settings. To learn more, visit Store app settings.

NoteDynatrace also provides a specific credential storage. It's helpful if you want to sync your credentials with an external vault. If not, you should use Settings to store your secrets.

###

#### Access external APIs
Create app functions, query data from third-party APIs, and use the data in your app.How-to guide

#### Cache data using app state
Use the app state to cache data from external systems.How-to guide

#### Ingest data
Ingest observability data such as metrics, logs, and events within your app into Dynatrace.How-to guide

#### Store app settings
Create a settings schema and store settings for your app.How-to guide

#### Store app and user states
Create, update, and delete app and user app states.How-to guide

#### Store static data in Grail
This how-to guide explains how you can store static data in Grail and query and combine it with other data.How-to guide

#### Store user-generated data
Save user-generated data so it's available across several user sessions.How-to guide

---

## data/access-external-apis

`/develop/guides/data/access-external-apis/`

- Data
- Access external APIs

## Access external APIs

- How-to guide
- 1-min readIf you fetch data from external APIs in a Dynatrace App, you'll get the following error in the console:

`tsx
Refused to connect to example.com/api because it violates the following Content Security Policy directive: "connect-src https://widget.usersnap.com https://fonts.googleapis.com https://dt-cdn.net 'self'"
`

This is because the Content Security Policy rules don't allow external APIs.
By using app functions you can access any external APIs.

#### Create app function

Run the following command in your project directory to create an app function:

`tsx
npx dt-app function create third-party-api
`

It will create a `api/third-party-api.function.ts` file. Replace the default content of the file with the following:

api/third-party-api.function.ts
`tsx
export default async () => { return (await fetch('https://dummyjson.com/users/1').then((response) => response.json())) as object;};
`

This app function makes a call to an external API `https://dummyjson.com/users/1` and returns the `json` response.

Ensure the external host is declared in the allowlist (see this guide for more details).

#### Call app function

Following the API call, the app function is now available via `/api/third-party-api` in our app.

Here is how you can fetch this API:

ui/app/App.tsx
`tsx
import React from 'react';import { useAppFunction } from '@dynatrace-sdk/react-hooks';export const App = () => { const response = useAppFunctionstring>({ name: 'third-party-api', responseType: 'json', }); return ( > {response.isLoading && p>Loading...p>} {response.data && p>{JSON.stringify(response.data)}p>} > );};
`

NoteThe response from `fetch` has two methods: `json()` and `text()`. These methods return a promise which resolves with the result of parsing the body text as `json` or `text` respectively, as shown in the earlier example.

### Related topics

- Fetch API

- Promises

- Async await

- Allow external requests

---

## data/cache-data-using-app-state

`/develop/guides/data/cache-data-using-app-state/`

- Data
- Cache data using app state

## Cache data using app state

- How-to guide
- 2-min readIn this guide, you'll learn how to use the app state to cache expensive requests to external systems.

Calls to external systems can be slow, or you might run into request throttling, or the system might be unavailable sometimes. When you use the app state to cache responses from external systems, the information will be available even when the external system isn't.

### Code

Let's assume you have a function like the following, calling the API of an external system:

api/external-call.function.ts
`tsx
export default async function (): Promiseunknown> { const apiResponse = await fetch('https://dummyjson.com/users/1'); if (!apiResponse.ok) { throw new Error(); } return apiResponse.json();}
`

TipIf the response contains user-specific or sensitive information, use user app state to persist information.
You can call the function from your UI using the package `@dynatrace-sdk/app-utils`.
If you want to cache the response, store the function's response using the app state via the package `@dynatrace-sdk/client-state`.

To install both packages, run the following command:

`tsx
npm install @dynatrace-sdk/app-utils @dynatrace-sdk/client-state
`

The following snippet combines the app state with the app function. We also use the `validUntilTime` property since, typically, the app state should cache the data only for a limited time.

ui/call-cachable-function.ts
`tsx
import { functions } from '@dynatrace-sdk/app-utils';import { stateClient } from '@dynatrace-sdk/client-state';export const callCachableFunction = async (functionName: string, appStateKey: string, validUntilTime: string) => stateClient .getAppState({ key: appStateKey, }) .then((appState) => { // Saved app state found. Return the saved value as a JSON object return JSON.parse(appState.value); }) .catch(async (e) => { // No app state found. Trigger the function, then store the response in the app state const response = await functions.call(functionName); const json = await response.json(); await stateClient.setAppState({ key: appStateKey, body: { validUntilTime, value: JSON.stringify(json), }, }); return json; });
`

TipThis operation requires the following scopes:
- `state:app-states:read`
- `state:app-states:write`Read more about scopes in this guide.
You can then use this helper with e.g. `callCachableFunction("external-call", "users", "now+30d")`.

### Summary

With these few lines of code, you can cache the response of an app function and improve the user experience in your app.

If you're looking for further ideas, check out Zod for typesafe data processing.

---

## data/ingest-data

`/develop/guides/data/ingest-data/`

- Data
- Ingest data

## Ingest data

- How-to guide
- 4-min readEnrich data on the Dynatrace platform by ingesting metrics, logs, and events within your app. You can do this by using the ingest endpoints of the Dynatrace API. Alternatively, you can use Extensions to collect observability data from different data sources not covered by OneAgent.

Dynatrace provides various SDK packages to make your life easier. Here are some examples of what you can do:

### Metrics

To ingest metrics, you can use the `ingest` method of the `metricsClient` namespace, which is provided by the `@dynatrace-sdk/client-classic-environment-v2` package.
You have to pass the metric values in the form of a string based on the Metrics ingestion protocol. Further ways of ingesting metrics can be found here.

`tsx
import { metricsClient } from '@dynatrace-sdk/client-classic-environment-v2';metricsClient .ingest({ body: 'cpu.temperature,hostname=host 55' }) .then((response) => { console.log(response); }) .catch((e) => { console.error(e); });
`

The ingested metrics can be queried with the following DQL statement:

`tsx
timeseries avg(cpu.temperature)
`

TipThis operation requires the scope `storage:metrics:write`. Read more about scopes in this guide.

### Logs

To ingest logs, you can use the `storeLog` method of the `logsClient` namespace, which is provided by the `@dynatrace-sdk/client-classic-environment-v2` package.
The method accepts a single log line as a JSON object or multiple log lines as an array.

An example of this could look like the following:

`tsx
import { logsClient } from '@dynatrace-sdk/client-classic-environment-v2';const logs = [ { 'content': 'example log content 1', 'log.source': '/var/log/syslog', 'log.tag': ['tag1', 'tag2'], }, { content: 'example log content 2' },];logsClient .storeLog({ body: logs, type: 'application/json; charset=utf-8', }) .then((response) => console.log(response)) .catch((e) => console.error(e));
`

In case of a successful ingest, the API returns an empty response body (see API docs). So the `response` object of the `storeLog` method is `undefined`.

You can query the ingested logs with the following DQL statement:

`tsx
fetch logs| filter contains(content, "example")
`

TipThis operation requires the scope `storage:logs:write`. Read more about scopes in this guide.

### Business events

To ingest business events, you can use the `ingest` function from the `businessEventsClient` namespace provided by the `@dynatrace-sdk/client-classic-environment-v2` package. In the following example, you're ingesting a CloudEvent.

`tsx
import { businessEventsClient } from '@dynatrace-sdk/client-classic-environment-v2';const bizevent = { specversion: '1.0', source: 'booking.app.tutorial', id: crypto.randomUUID().toString(), type: 'booking.process.started', data: { amount: 869, startdate: '2020-04-06', arrivaldate: '2022-04-16', currency: 'USD', numbertravelers: 2, product: 'Vienna - New York', },};businessEventsClient .ingest({ body: bizevent, type: 'application/cloudevent+json', }) .then(() => console.log('Event ingested')) .catch((e) => console.error('Failed to ingest event: ' + e));
`

#### Key things to remember

- It's important that you specify the correct content `type` as highlighted in the previous code.

- Dynatrace support both CloudEvent and pure JSON data. For cloud events, the content type is `application/cloudevent+json` and for pure JSON data it is `application/json; charset=utf-8`.

You can query this event with the following DQL statement:

`tsx
fetch bizevents| filter event.type == "booking.process.started"
`

TipThis operation requires the scope `storage:events:write`. Read more about scopes in this guide.

### Events

To ingest events, you need to use the `createEvent` method of the `eventsClient` namespace within the `@dynatrace-sdk/client-classic-environment-v2` package:

`tsx
import { EventIngest, eventsClient } from '@dynatrace-sdk/client-classic-environment-v2';const terminationEvent: EventIngest = { eventType: 'MARKED_FOR_TERMINATION', title: 'Planned host downscale', entitySelector: 'type(HOST),entityId(HOST-7DB082B3599E3EA9)', properties: { 'job.number': '21234346' },};eventsClient.createEvent({ body: terminationEvent });
`

The example above shows how to ingest an event that should mark a host with a specific host id for termination.

The ingested event can be queried with the following DQL statement:

`tsx
fetch events| filter event.kind == "DAVIS_EVENT"| filter event.type == "MARKED_FOR_TERMINATION"
`

TipThis operation requires the scope `storage:events:write`. Read more about scopes in this guide.

### Extensions 2.0

Dynatrace provides capabilities for monitoring and analyzing the performance of all aspects of your application environment. With OneAgent, you can monitor everything that runs on a host. However, you often need to look deeper into other technologies that don't accept agents, for example, network devices. Extensions can cover these cases.

You can install extensions on both OneAgent and ActiveGates. They connect to the monitored technologies in the best way that fits that technology. Dynatrace develops the extension data acquisition layer (data source), which allows you to easily manage your extensions declaratively by creating a YAML file specifying what data you want and from where.

To learn more, visit Extensions

### Related topics

- Environment API documentation

- Log data ingest

- Ingest a custom event to Dynatrace

- Extensions 2.0

---

## data/store-app-settings

`/develop/guides/data/store-app-settings/`

- Data
- Store app settings

## Store app settings

- How-to guide
- 13-min readThis guide shows you how to create a settings schema and consume settings values in your UI.

NoteAll authenticated users of the app can read app settings. Read more about the general concept of App settings.

### Install the SDK

First, you need to install the required SDK via the terminal as follows:

`tsx
npm i @dynatrace-sdk/client-app-settings-v2
`

#### Migration guide

The `@dynatrace-sdk/client-app-settings-v2` SDK replaces `@dynatrace-sdk/client-app-settings`.

The following methods now only accept a single `schemaId`, since the `schemaIds` parameter has been replaced by `schemaId`:

- `getEffectiveAppSettingsValues`

- `getAppSettingsObjects`

The `AppSettingsErrorEnvelope` parameter has been replaced by `ErrorResponse`.

Only version 2 supports new features such as filtering, sorting, and owner-based access control. We recommend using the `@dynatrace-sdk/client-app-settings-v2` SDK.

### Define a settings schema

A settings schema is a JSON file that defines the structure of the values stored in the app settings. You can create any number of schemas in your project's `/settings/schemas` directory, with the only restriction that each schema definition file name must end in `.schema.json`.

TipIf you want your IDE to provide autocompletion and detailed documentation, use the `$schema` keyword in your setting schema to reference the JSON Schema. You can also import it manually if your IDE doesn't support that mechanism.
Here is an example of a schema that allows you to configure connections to a fictional messaging service:

my-example.schema.jsonsettings/schemas/my-example.schema.json
`tsx
{ "$schema": "https://developer.dynatrace.com/docs-assets/schema_strict_apps.json", "dynatrace": "1", "schemaId": "my-example", "version": "1.0.0", "displayName": "Allows you to configure connections to a fictional messaging service", "description": "", "multiObject": true, "maxObjects": 10, "summaryPattern": "Messaging Service {url} via {tokenType}", "ordered": false, "maturity": "GENERAL_AVAILABILITY", "ownerBasedAccessControl": false, "enums": { "Type": { "displayName": "Type", "description": "", "documentation": "", "items": [ { "value": "basic", "displayName": "Basic Authentication" }, { "value": "pat", "displayName": "Personal Access Token" }, { "value": "cloud-token", "displayName": "Access Token" } ], "type": "enum" } }, "properties": { "url": { "displayName": "URL", "description": "The URL of the messaging service", "type": "text", "default": "", "nullable": false, "constraints": [ { "type": "PATTERN", "customMessage": "The URL must be secure (https://) and must not contain a trailing slash", "pattern": "^https://.*[^/]$" } ] }, "token": { "displayName": "Token", "description": "A secret token", "type": "secret", "default": "", "nullable": false }, "tokenType": { "displayName": "Type", "description": "Type of authentication method that should be used", "default": "basic", "type": { "$ref": "#/enums/Type" }, "nullable": false }, "channels": { "displayName": "Channels", "description": "A list of channels on the messaging service", "type": "list", "items": { "type": "text" } }, "isEnabled": { "displayName": "Enabled", "description": "Enable the integration of the messaging service", "type": "boolean", "default": false, "nullable": false } }}
`

#### Schema maturity

The `maturity` field indicates the stability and readiness of the schema for production use. The available maturity levels are: `IN_DEVELOPMENT`, `EARLY_ADOPTER` and `GENERAL_AVAILABILITY`.

Schemas with `IN_DEVELOPMENT` maturity are hidden from the settings menu and can't be accessed via either the Settings Schemas or Settings Objects Environment API.
However, you can still access and manage the setting objects of such schemas as described in this document or directly via the App Settings V2 API.

Schemas with `EARLY_ADOPTER` maturity are available in all environments, but are less mature that those with the `GENERAL_AVAILABILITY` maturity. Even though incompatible changes for these schemas are not expected, since they aren't fully stable yet, incompatible changes may be necessary in rare cases.

Schemas with `GENERAL_AVAILABILITY` maturity are considered the most stable. While the schemas will still evolve over time, you should only worry about backward-compatible features.

#### Use secrets

When you use secrets in your app settings, a default security mechanism protects them from exfiltration.

For example, if you store an access token along with the URL for a service to authenticate, any URL change ideally requires you to resubmit the secret. Otherwise, your app could connect to the changed URL and leak the access token. You can prevent such a leak by resubmitting the secret after changing any properties related to it, such as URLs, IP addresses, port numbers, service names, and others.

To make this easy, app settings have a secret resubmission validation in place, which is achieved and configured with the help of a built-in container constraint.

Suppose the schema has secrets, and you haven't manually added a resubmission constraint. In this case, the schema will behave as if it had a constraint that requires you to resubmit the secret on any property change.

Therefore, by default, you'll have to resubmit the secret after any changes to its related properties. Add a constraint object to the list of constraints to change this default behavior. The constraint object has two mandatory fields, `"type": "SECRET_RESUBMISSION"`, `"checkAllProperties": false`, and an optional one, `"customMessage"`.

For every property related to the secret, add `"forceSecretResubmission": true`.
The `forceSecretResubmission` property on an input property is only available if a validator constraint of type SECRET_RESUBMISSION exists.
Otherwise, the schema registration will fail with a validation error, which means the automatism fallback always considers all properties and doesn't have to deal with the `forceSecretResubmission` properties.

Here is an example of a schema with a manually configured resubmission validation:

my-example-secrets.schema.jsonsettings/schemas/my-example-secrets.schema.json
`tsx
{ "dynatrace": "1", "schemaId": "my-example-secrets", "version": "1.0.0", "displayName": "Allows you to configure connections to a fictional messaging service", "description": "", "multiObject": true, "maxObjects": 10, "maturity": "GENERAL_AVAILABILITY", "summaryPattern": "Messaging Service {url}", "ordered": false, "properties": { "isEnabled": { "displayName": "Enabled", "description": "Enable the integration of the messaging service", "type": "boolean", "default": false, "nullable": false }, "description": { "displayName": "Description of the connection", "type": "text", "default": "", "nullable": false }, "url": { "displayName": "URL", "description": "The URL of the messaging service", "type": "text", "default": "", "nullable": false, "forceSecretResubmission": true, "constraints": [ { "type": "PATTERN", "customMessage": "The URL must be secure (https://) and must not contain a trailing slash", "pattern": "^https://.*[^/]$" } ] }, "token": { "displayName": "Token", "description": "A secret token", "type": "secret", "default": "", "nullable": false } }, "constraints": [ { "type": "SECRET_RESUBMISSION", "customMessage": "For security reasons, please re-enter the token before saving the settings.", "checkAllProperties": false } ]}
`

#### Limitations

- Each schema can't exceed 100KiB.

- The settings folder can't exceed 1MiB.

### Local development

CautionThe app settings plugin described in this chapter is still experimental and might change.
Although the autogenerated settings UI is available only after you deploy your app, you can mock the settings values locally for easier development. The app settings plugin allows you to provide, access, and update these mocked values during development.

First, install the plugin as a dev dependency:

`tsx
npm install --save-dev @dynatrace-sdk/dt-app-plugin-client-app-settings-v2
`

Next, register the plugin in your app configuration file and add the `app-settings:objects:read` app scope:

app.config.json
`tsx
{ "environmentUrl": "", "app": { "id": "", "name": "", "version": "0.0.0", "description": "", "scopes": [{ "name": "app-settings:objects:read", "comment": "Read app settings" }] }, "plugins": ["@dynatrace-sdk/dt-app-plugin-client-app-settings-v2"]}
`

After you start the development server, the app settings plugin creates some files:

- `settings/local-mock-data/values.json`

- `settings/local-mock-data/secrets.json`

- `settings/local-mock-data/permissions.json`

Let's examine these files in the next sections.

#### Use local values

The `settings/local-mock-data/values.json` file allows you to provide the mocked values for your settings schema. When you fetch settings in your app locally, the plugin will handle the request and return the mocked values. Following is an example that shows all the properties you can set (`schemaId` and `value` are required; the rest is optional):

values.jsonsettings/local-mock-data/values.json
`tsx
[ { "schemaId": "my-example", "value": { "url": "https://foo.bar/messaging", "token": "a-secret-basic-token", "tokenType": "basic", "channels": ["admin-notifications", "user-notifications"], "isEnabled": true }, "schemaVersion": "1", "summary": "Messaging Service https://foo.bar/messaging via Basic Authentication", "searchSummary": "Messaging Service https://foo.bar/messaging via Basic Authentication", "modificationInfo": { "createdBy": "foo", "createdTime": "2023-10-10T10:00:00.000Z", "lastModifiedBy": "bar", "lastModifiedTime": "2023-11-11T11:00:00.000Z" } }, { "schemaId": "my-example", "value": { "url": "https://foo.bar/messaging", "token": "a-secret-personal-access-token", "tokenType": "pat", "channels": ["admin-notifications", "user-notifications"], "isEnabled": true }, "schemaVersion": "1", "summary": "Messaging Service https://foo.bar/messaging via Personal Access Token", "searchSummary": "Messaging Service https://foo.bar/messaging via Personal Access Token", "modificationInfo": { "createdBy": "foo", "createdTime": "2023-08-08T08:00:00.000Z", "lastModifiedBy": "baz", "lastModifiedTime": "2023-09-09T09:00:00.000Z" } }]
`

The above example has one issue: the access tokens are exposed as plain text. The app settings plugin also offers a solution to this problem.

#### Use local secrets

A common use case for app settings is storing secrets. The app settings plugin provides a way to simulate the same behavior locally by defining them in the `settings/local-mock-data/secrets.json` file. Following is an example:

settings/local-mock-data/secrets.json
`tsx
{ "basicToken": "a-secret-basic-token", "personalAccessToken": "a-secret-personal-access-token"}
`

After the secrets are defined, you can now use them in the `values.json` file:

settings/local-mock-data/values.json
`tsx
[ { "schemaId": "my-example", "value": { "url": "https://foo.bar/messaging", "token": "{{basicToken}}", "tokenType": "basic", "channels": ["admin-notifications", "user-notifications"], "isEnabled": true } }, { "schemaId": "my-example", "value": { "url": "https://foo.bar/messaging", "token": "{{personalAccessToken}}", "tokenType": "pat", "channels": ["admin-notifications", "user-notifications"], "isEnabled": true } }]
`

If the settings are now read via App functions, the secrets are returned in plain text. However, if you read them elsewhere, they will be returned as a masked value, similar to when deploying the app.

Note, however, that when you update a value locally via the SDK, the `secrets.json` file isn't updated, and the property loses its secret attributes.

#### Use local permissions

The `settings/local-mock-data/permissions.json` file allows you to provide the mocked permissions for your settings schema. The plugin will use this to handle requests to resolve effective permissions and to fill the `resourceContext` field in the response to the fetch settings values request.
Following is an example of defining permissions for settings schema with id "my-example":

`tsx
{ "my-example": [ { "permission": "app-settings:objects:read", "granted": "true" }, { "permission": "app-settings:objects:write", "granted": "false" } ]}
`

The plugin considers each of the two possible permissions (`app-settings:objects:read`, `app-settings:objects:write`) as granted for the current user unless the `permissions.json` file contains another value for the `"granted"` field for the given schema and permission.

For the `resourceContext` part of the settings values response, only `"granted": "false"` is treated as if the user wouldn't have the correspondent permission.
Any other value (like `"true"`, `"condition"` or missing value) is considered as `"granted": "true"`.
Also, note that the plugin doesn't use the `permissions.json` file to control user access while performing read or write operations with settings values.

#### Update local settings

Of course, you can update your `values.json` file at any point to update the settings for your app, but the plugin also supports modifications.
For this purpose, when you execute one such operation, the plugin creates a copy of the `values.json` file in `settings/local-mock-data/persistence/values.shadow.json`.
If this file exists, all read and write operations will use it instead of the `settings/local-mock-data/values.json` you created manually.

To restore the state you configured, simply delete the `settings/local-mock-data/persistence` folder.

#### Limitations

- Local settings values aren't validated against the local schemas.

- Intents to open settings pages don't work.

### Get effective settings value

Effective values are the values that are stored in the settings or the default value. Use this method if you want to use settings in your app.

To retrieve the effective values for one or many settings schemas, use the `useSettingsV2` React hook from the `@dynatrace-sdk/react-hooks` package. This hook expects the schema identifier in the `schemaId` parameter. A single call will get you the effective values for a single schema.

By default, `useSettingsV2` only returns the `value`. The hook can return additional fields when you specify them in a comma-separated string in the `addFields` parameter.

In the following example, you're getting effective settings values for the `my-example` schemas:

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsV2 } from '@dynatrace-sdk/react-hooks';import { ExternalLink, Paragraph } from '@dynatrace/strato-components/typography';import { Flex } from '@dynatrace/strato-components/layouts';export const App = () => { const { data, isLoading } = useSettingsV2({ schemaId: 'my-example', addFields: 'summary, schemaId', }); return ( Flex> {!isLoading && data && ( > Paragraph>{data.items[0]?.summary}Paragraph> ExternalLink href={data.items[0]?.value?.url as string}>My external linkExternalLink> > )} Flex> );};
`

The default value depends on the `multiObject` property of the schema:

- `false`: if it's false, a single default object is created. Its properties are propagated with the default values defined in your schema.

- `true`: if it's true, an empty collection is created.

TipThis operation requires the scope `app-settings:objects:read`. Read more about scopes in this guide.

### Store settings values

To store new values for a settings schema, use the `useCreateSettingsV2` hook.

The `useCreateSettingsV2` hook returns the `objectId` and `version` of the created settings object. You can use them to subsequently update or delete settings.

In the following example, you store a value accessible to the fictional messaging service integration from the `my-example` schema. The service can now use the specific URL and basic access token:

ui/app/App.tsx
`tsx
import React from 'react';import { useCreateSettingsV2 } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';export const App = () => { const { execute } = useCreateSettingsV2(); const handleOnClick = () => { execute({ body: { schemaId: 'my-example', value: { url: 'https://foo.bar/messaging', token: 'a-secret-basic-token', tokenType: 'basic', channels: ['admin-notifications', 'user-notifications'], isEnabled: true, }, }, }); }; return Button onClick={handleOnClick}>Create settingsButton>;};
`

TipThis operation requires the scope `app-settings:objects:write`. Read more about scopes in this guide.

### Get stored settings values

To fetch previously stored values for a settings schema, use the `useSettingsObjectsV2` hook. Use this and the `useUpdateSettingsV2` hook if you want to manage settings in your app.

This hook expects the schema identifier in the `schemaId` parameter.

By default, `useSettingsObjectsV2` only returns the `objectId` and `version` parameters. You can define extra fields to return by specifying them in a comma-separated string in the `addFields` parameter.

By specifying the respective parameters, you can also filter and sort the effective values. You can use the following fields to filter:

- `modificationInfo.createdBy`

- `modificationInfo.createdTime`

- `modificationInfo.lastModifiedBy`

- `modificationInfo.lastModifiedTime`

- `value` with properties and sub-properties separated by dot. For example, `value.isEnabled = true`.

- `owner.type`

- `owner.id`

You can use the following fields to sort:

- `modificationInfo.createdBy`

- `modificationInfo.createdTime`

- `modificationInfo.lastModifiedBy`

- `modificationInfo.lastModifiedTime`

- `value` with properties and sub-properties separated by dot (for example, `value.isEnabled`)

Note that only fields included in the response via `addFields` can be used for filtering and sorting.

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsObjectsV2 } from '@dynatrace-sdk/react-hooks';import { ExternalLink, Paragraph } from '@dynatrace/strato-components/typography';import { Flex } from '@dynatrace/strato-components/layouts';export const App = () => { const { data, isLoading } = useSettingsObjectsV2({ schemaId: 'my-example', addFields: 'value, summary', }); return ( Flex> {!isLoading && data && ( > Paragraph>{data.items[0]?.summary}Paragraph> ExternalLink href={data.items[0]?.value?.url as string}>My external urlExternalLink> > )} Flex> );};
`

TipThis operation requires the scope `app-settings:objects:read`. Read more about scopes in this guide.

### Update settings values

To update the value for a settings schema, use the `useUpdateSettingsV2` hook.

The `useUpdateSettingsV2` hook returns the `version` of the updated settings object, which you can use to update the object again.

In the following example, you edit a value accessible to the fictional messaging service integration from the `my-example` schema. The service can now use the personal access token:

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsObjectsV2, useUpdateSettingsV2 } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';export const App = () => { const { data } = useSettingsObjectsV2({ schemaId: 'my-example', }); const { execute } = useUpdateSettingsV2(); const handleOnClick = () => { if (data) { execute({ objectId: data.items[0].objectId, optimisticLockingVersion: data.items[0].version, body: { value: { url: 'https://foo.bar/messaging', token: 'a-secret-personal-access-token', tokenType: 'pat', channels: ['admin-notifications', 'user-notifications'], isEnabled: true, }, }, }); } }; return Button onClick={handleOnClick}>Update settingsButton>;};
`

Remember that each setting has a `version` that changes each time its value changes. You need to pass the current `version` for any operation that modifies the value.

TipThis operation requires the scope `app-settings:objects:write`. Read more about scopes in this guide.

### Delete settings values

To delete a value for a settings schema, use the `useDeleteSettingsV2` hook. You need to provide the `optimisticLockingVersion` of the value you want to delete, as shown in the following example:

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsObjectsV2, useDeleteSettingsV2 } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';export const App = () => { const { data } = useSettingsObjectsV2({ schemaId: 'my-example', }); const { execute } = useDeleteSettingsV2(); const handleOnClick = () => { if (data) { execute({ objectId: data.items[0].objectId, optimisticLockingVersion: data.items[0].version, }); } }; return Button onClick={handleOnClick}>Delete settingsButton>;};
`

TipThis operation requires the scope `app-settings:objects:write`. Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

### Get effective settings permissions

To get the effective settings permissions for the calling user in the environment, use the `useEffectivePermissionsV2` hook.
In the following example, you're checking whether the user has `app-settings:objects:read` and `app-settings:objects:write` permissions for `my-example-1` and `my-example-2` schemas:

ui/app/App.tsx
`tsx
import React from 'react';import { Container, Flex } from '@dynatrace/strato-components/layouts';import { Text } from '@dynatrace/strato-components/typography';import { BlockIcon } from '@dynatrace/strato-icons';import { useEffectivePermissionsV2 } from '@dynatrace-sdk/react-hooks';export const App = () => { const { data } = useEffectivePermissionsV2({ body: { permissions: [ { permission: 'app-settings:objects:read', context: { schemaId: 'my-example-1' }, }, { permission: 'app-settings:objects:write', context: { schemaId: 'my-example-2' }, }, ], }, }); return ( Container> {data && data[0].granted === 'false' && ( Flex> BlockIcon /> Text>Permission denied. Contact your account admin.Text> Flex> )} Container> );};
`

The function returns an array containing information about requested permissions in the following format:

`tsx
[ { "permission": "app-settings:objects:read", "granted": "true", "context": { "schemaId": "my-example-1" } }, { "permission": "app-settings:objects:write", "granted": "false", "context": { "schemaId": "my-example-2" } }]
`

TipThis operation requires one of the following scopes:
- `app-settings:objects:read`
- `app-settings:objects:write`Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.
TipYou can also query user permissions.

### Owner-based access control

If a schema has the `ownerBasedAccessControl` property set to `true`, users can more finely control which users can access specific settings.
For these types of schemas, the user that first stores a settings object is the `owner` of that object.
By default, only the `owner` can access these objects, but the following sections explain how to share control over these objects. These APIs only work on a single-settings object per request.
For the examples listed below, assume the `my-example` schema has the `ownerBasedAccessControl` property set to `true`.

The following sections mention accessors. An accessor can be a specific `user`, a `group`, or the `all-users` type, which applies to all users. When using the `all-users` type, you don't need to specify any ID.

#### Transfer ownership

An owner has read and write access to their object. A settings object can have only one owner, but the owner can be any kind of accessor.

To transfer this ownership of a settings object to a different accessor, use the `useTransferOwnershipV2` hook.

After the request is sent, the previous owner loses access, so owners might want to use the permission mechanism described in the next section to add permissions they want to retain before transferring ownership.

In the following example, you transfer the ownership of a settings object to a fictional user on the first object of the `my-example` schema, assuming you have ownership over that object:

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsObjectsV2, useTransferOwnershipV2 } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';export const App = () => { const { data } = useSettingsObjectsV2({ schemaId: 'my-example', }); const { execute } = useTransferOwnershipV2(); const handleOnClick = () => { if (data) { execute({ objectId: data.items[0].objectId, body: { newOwner: { type: 'user', id: '550e8400-e29b-41d4-a716-446655440000', }, }, }); } }; return Button onClick={handleOnClick}>Transfer ownershipButton>;};
`

TipThis operation requires the scope `app-settings:objects:write`. Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

#### Add permissions for an accessor to an object

To grant permissions for an accessor to an existing settings object, use the `useCreatePermissionsV2` hook.

You can grant the accessor either read-only or read-and-write access. You can only use an accessor without permission on the object. For the others, you should use the update function, which is documented further below.

Only users with read and write access on the object can add permissions for a new accessor.

In the following example, you grant read and write access to a fictional group on the first object of the `my-example` schema. This means that all users belonging to this group receive read and write access:

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsObjectsV2, useCreatePermissionsV2 } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';export const App = () => { const { data } = useSettingsObjectsV2({ schemaId: 'my-example', }); const { execute } = useCreatePermissionsV2(); const handleOnClick = () => { if (data) { execute({ objectId: data.items[0].objectId, body: { accessor: { type: 'group', id: 'f81d4fae-7dec-11d0-a765-00a0c91e6bf6', }, permissions: ['r', 'w'], }, }); } }; return Button onClick={handleOnClick}>Add permissionsButton>;};
`

TipThis operation requires the scope `app-settings:objects:write`. Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

#### Get permissions of all accessors of an object

Use the `usePermissionsV2` hook to get an overview of all permissions for each accessor of a specific settings object.

Only users with read access to the object can get the permissions overview.

In the following example, you get a permission overview for the object with a specific `objectId`:

ui/app/App.tsx
`tsx
import React from 'react';import { usePermissionsV2 } from '@dynatrace-sdk/react-hooks';import { ExternalLink, Paragraph, List, Text } from '@dynatrace/strato-components/typography';import { Flex } from '@dynatrace/strato-components/layouts';export const App = () => { const { data, isLoading } = usePermissionsV2({ objectId: '', }); return ( Flex> {!isLoading && data && ( List> {data.accessors.map((item) => ( Text key={item.accessor.id}> {item.accessor.type} {item.accessor.id} Text> ))} List> )} Flex> );};
`

TipThis operation requires the scope `app-settings:objects:read`. Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

#### Update permissions for an accessor on an object

To update the permissions of an accessor for a specific settings object, use either the `useUpdateAccessorPermissionsV2` or the `useUpdateAllUsersPermissionsV2` hook.

The first function is for accessors of type `user` and `group`, the second for the `all-users` type. To update permissions for an accessor, you must first add them via the hook documented above.

Only users that have read and write access on the object can update permissions for an accessor.

In the following example, you update the permission of a fictional group for the first object of the `my-example` schema to read-only:

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsObjectsV2, useUpdateAccessorPermissionsV2 } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';export const App = () => { const { data } = useSettingsObjectsV2({ schemaId: 'my-example', }); const { execute } = useUpdateAccessorPermissionsV2(); const handleOnClick = () => { if (data) { execute({ objectId: data.items[0].objectId, accessorType: 'group', accessorId: 'f81d4fae-7dec-11d0-a765-00a0c91e6bf6', body: { permissions: ['r'], }, }); } }; return Button onClick={handleOnClick}>Update accessor permissionsButton>;};
`

TipThis operation requires the scope `app-settings:objects:write`. Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

#### Remove permissions for an accessor on an object

To remove all granted permissions for an accessor on an object, use either the `useDeleteAccessorPermissionsV2` or the `useDeleteAllUsersPermissionsV2` hook.

If the accessor doesn't have access via different means, such as a group or via the `owner`, the object will be inaccessible after this call.

Only users with read and write access on the object can remove permissions for an accessor.

In the following example, you remove all permissions of the `all-users` accessor of the first object of the `my-example` schema:

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsObjectsV2, useDeleteAllUsersPermissionsV2 } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';export const App = () => { const { data } = useSettingsObjectsV2({ schemaId: 'my-example', }); const { execute } = useDeleteAllUsersPermissionsV2(); const handleOnClick = () => { if (data) { execute({ objectId: data.items[0].objectId, }); } }; return Button onClick={handleOnClick}>Delete all-users permissionsButton>;};
`

TipThis operation requires the scope `app-settings:objects:write`. Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

#### Administrator access

You can bypass the access checks for specific administrator users to avoid:

- A user locking themselves out of a settings object.

- The owner of a settings object being unavailable.

- Not having sufficient permissions for a settings object.

All documented hooks besides `useEffectivePermissionsV2` and `useCreateSettingsV2` accept the `adminAccess` parameter.
Passing this parameter with the value `true` allows users to modify any object they want, without having to worry about the permissions granted or owner assigned.

This requires the additional scope of `app-settings:objects:admin`.

In the following example, you transfer the ownership of a settings object to a fictional user on the first object of the `my-example` schema, without needing to be the current owner and without having access to the settings object:

ui/app/App.tsx
`tsx
import React from 'react';import { useSettingsObjectsV2, useTransferOwnershipV2 } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';export const App = () => { const { data } = useSettingsObjectsV2({ schemaId: 'my-example', adminAccess: true, }); const { execute } = useTransferOwnershipV2(); const handleOnClick = () => { if (data) { execute({ objectId: data.items[0].objectId, adminAccess: true, body: { newOwner: { type: 'user', id: '550e8400-e29b-41d4-a716-446655440000', }, }, }); } }; return Button onClick={handleOnClick}>Transfer ownershipButton>;};
`

TipThis operation requires the following scopes:
- `app-settings:objects:write`
- `app-settings:objects:admin`Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

### Related topics

- App settings service

- Locking strategies

---

## data/store-app-user-state

`/develop/guides/data/store-app-user-state/`

- Data
- Store app and user states

## Store app and user states

- How-to guide
- 6-min readThe state service is your best option if your app needs internal global states or user-specific states. One common usage is caching the result of an app function.

This guide explains how to create, update, and delete app states and user app states. The `@dynatrace-sdk/react-hooks` package provides hooks so you can do all these operations.

When you run your app on your local development server, the states are confined to the local development's scope. So, you won't be in danger of overriding the deployed app's states during development.

States are persistent across updates of an app. So, you must migrate any states needed for a new app version in the app's code.

### Set a state by key

To set the app or user app state, you can use the `setAppState` or `setUserAppState` hooks from the `@dynatrace-sdk/react-hooks` package. These hooks provide an `execute` function to create a new state, and additional fields about the loading status, errors, and response. These fields are common to all the app and user app state hooks. The example below shows how to create an app state for storing weather information:

TipAdd a `version` field to your state to make future migrations easier.
ui/app/App.tsx
`tsx
import React from 'react';import { useSetAppState } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';import { Page } from '@dynatrace/strato-components/layouts';export const App = () => { const { execute } = useSetAppState(); const handleClick = () => { execute({ key: 'weather', body: { value: JSON.stringify({ version: '1', timestamp: Date.now(), weather: { city: 'Vienna', temperature: 23, unit: 'celsius' }, }), validUntilTime: 'now+1d', }, }); }; return ( Page> Button onClick={handleClick}>Set app stateButton> Page> );};
`

TipThis operation requires the following scopes:
- `state:app-states:write`
- `state:user-app-states:write`Read more about scopes in this guide.

#### State validity

By default, app states and user app states don't expire. To define states that are only valid for a certain period, you can provide an optional `validUntilTime`, which ensures the presence of the state until the time expires. States are deleted after their `validUntilTime` elapses.

You can provide the `validUntilTime` in two ways:

- A relative time format such as `now+1m` or `now+30d`:

- The format is `now+NU` where `N` is the amount of time, `U` is the unit of time (s - seconds, m - minutes, h - hours, d - days).

- A timestamp in ISO 8601 format.

For both types, you can specify a timeframe of 1 minute to 90 days.

NoteEvery app state hook has an equivalent user app state hook. For instance, the equivalent of `useSetAppState` is `useSetUserAppState`. All the examples in this guide use the app state hooks.

### Get a state by key

To fetch a previously stored state, you can use the `useAppState` and `useUserAppState` hooks and pass the key of the write operation as the parameter. The `validUntilTime` follows an ISO 8601 syntax. The hooks also provide a function to `refetch` the latest state. The following code fetches the state from the previous example.

ui/app/App.tsx
`tsx
import React, { useState, useEffect } from 'react';import { useAppState } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';import { Flex } from '@dynatrace/strato-components/layouts';import { Text } from '@dynatrace/strato-components/typography';import { Page } from '@dynatrace/strato-components/layouts';interface Weather { city: string; temperature: number; unit: string;}export const App = () => { const [weather, setWeather] = useStateWeather>(); const { data, refetch } = useAppState({ key: 'weather' }); useEffect(() => { if (data) { setWeather((JSON.parse(data.value) as { weather: Weather }).weather); } }, [data]); const handleClick = () => { refetch(); }; return ( Page> {weather && ( Flex> Text>{weather.city}Text> Text> {weather.temperature} {weather.unit} Text> Flex> )} Button onClick={handleClick}>Refetch app stateButton> Page> );};
`

TipThis operation requires the following scopes:
- `state:app-states:read`
- `state:user-app-states:read`Read more about scopes in this guide.
These operations throw an exception when the state you try to retrieve doesn't exist. If that's an expected scenario in your app, you should add
some exception handling. Alternatively, you could use the useAppStates hook and filter for a specific key to get an empty array if it doesn't exist.

### List all states

If your app uses dynamicaly created keys instead of a fixed set of known static keys, you can get a list of all app states or user app states with the `useAppStates` and `useUserAppStates` hooks.

By default, `useAppStates` and `useUserAppStates` only return the keys. You can request additional fields by specifying them in a comma-separated string in the `addFields` parameter.

ui/app/App.tsx
`tsx
import React from 'react';import { useAppStates } from '@dynatrace-sdk/react-hooks';import { Flex } from '@dynatrace/strato-components/layouts';import { List, Text } from '@dynatrace/strato-components/typography';import { Page } from '@dynatrace/strato-components/layouts';export const App = () => { const { data } = useAppStates({ addFields: 'value,modificationInfo.lastModifiedBy,validUntilTime', }); return ( Page> {data && ( List> {data.map((state) => ( Flex key={state.key}> Text>{state.value}Text> Text>{state.modificationInfo?.lastModifiedBy}Text> Text>{state.validUntilTime}Text> Flex> ))} List> )} Page> );};
`

TipThis operation requires the following scopes:
- `state:app-states:read`
- `state:user-app-states:read`Read more about scopes in this guide.

#### Filter states

The `useAppStates` and `useUserAppStates` hooks let you filter states via the `filter` parameter for the following fields:

- `key`, supports operators: `=`, `!=`, `contains`, `starts-with`, and `ends-with`

- `modificationInfo.lastModifiedTime`, supports operators: `=`, `!=`, , and `>=`

- `modificationInfo.lastModifiedBy`, supports operators: `=`, `!=`, `contains`, `starts-with`, and `ends-with`

- `validUntilTime`, supports operators: `=`, `!=`, , and `>=`

Operators `contains`, `starts-with`, and `ends-with` are case-insensitive. Comparisons via `=`, `!=` are case-sensitive.

Conditions can be connected via `and` and `or`. Individual conditions can be negated by `not`.
The filter string can be up to 256 characters long. You can nest conditions (using round brackets) up to 2 levels deep.

Here are some examples of how to use filters:

`tsx
const appStates = useAppStates({ filter: "modificationInfo.lastModifiedTime > '2022-07-01T00:10:05.000Z'",});const appStatesComplexFilter = useAppStates({ filter: "(key starts-with 'favourite' or key starts-with 'favorite') and not(key contains 'disk' or key contains 'process')",});const appStatesOrEmpty = useAppStates({ filter: "key = 'might-not-exist'",});
`

### Delete a state by key

You can delete app states and user app states that aren't needed anymore with the `useDeleteAppState` and `useDeleteUserAppState` hooks. In addition, this will free up the equivalent of the deleted value's size in the state storage quota currently available to the app:

ui/app/App.tsx
`tsx
import React from 'react';import { useDeleteAppState } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';import { Page } from '@dynatrace/strato-components/layouts';export const App = () => { const { execute } = useDeleteAppState(); const handleClick = () => { execute({ key: 'weather', }); }; return ( Page> Button onClick={handleClick}>Delete app stateButton> Page> );};
`

TipThis operation requires the following scopes:
- `state:app-states:delete`
- `state:user-app-states:delete`Read more about scopes in this guide.

### Delete all states

The `useDeleteAppStates` and `useDeleteUserAppStates` allow you to delete all app states and user app states to completely reset the app's states:

ui/app/App.tsx
`tsx
import React from 'react';import { useDeleteAppStates } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';import { Page } from '@dynatrace/strato-components/layouts';export const App = () => { const { execute } = useDeleteAppStates(); const handleClick = () => { execute(); }; return ( Page> Button onClick={handleClick}>Delete app statesButton> Page> );};
`

TipThis operation requires the following scopes:
- `state:app-states:delete`
- `state:user-app-states:delete`Read more about scopes in this guide.

### Reset app state

Environment admins can also manually reset an app's state. They can do so via the Hub, by following these steps:

- Open the Manage tab in the Hub app

- Find the app you want to reset the state for

- From the kebab menu on the right, click Reset state

- Select whether you want to reset your own user's state or the whole app state

- Finish by clicking Reset State, and then Confirm

### Related topics

- State service

---

## data/store-static-data-in-grail

`/develop/guides/data/store-static-data-in-grail/`

- Data
- Store static data in Grail

## Store static data in Grail

- How-to guide
- 5-min readThe lookup upload API allows you to upload static data and store it as a tabular file in the . This guide will walk you through using the `/files/tabular/lookup:upload` endpoint to upload your data.

### Use case

Imagine a scenario where you're storing user event information in Grail. This data includes the user's email, current balance, and the currency of the balance. You want to convert the balance into a different currency using conversion rates fetched from a third-party API. By storing the user event data and the conversion rates in Grail, you can perform this conversion and generate balances in the desired currency directly within Grail.

#### User event data structure

Here is an example of the user event data stored in Grail:

`tsx
[ { "email": "first@first.com", "balance": 10, "currency": "USD" }, { "email": "second@first.com", "balance": 130, "currency": "USD" }, { "email": "third@first.com", "balance": 20, "currency": "USD" }]
`

#### Conversion rate data

The conversion rates, fetched from a third-party API, are stored in Grail as follows:

`tsx
[ { "source": "USD", "EUR": 0.88, "AUD": 1.39, "PLN": 3.94 }, { "source": "EUR", "USD": 1.14, "AUD": 0.72, "PLN": 0.25 }]
`

You can calculate each user's balance in a specific currency using these two datasets. For example, you can convert USD balances into EUR using the stored conversion rates.

### Upload static data in Grail

The endpoint is used to upload lookup data and store it as a new tabular file or replace an existing one. The data is parsed using the Dynatrace Pattern Language (DPL), which allows you to define patterns for extracting records from the uploaded data.

The request must be submitted as `multipart/form-data` with the following parts:

- request: Contains the request parameters in JSON format

- content: Contains the lookup data in text format

#### Key request parameters

Here are details of important request parameters:

- filePath (required): A file path where the data will be stored in Grail. It must start with a `/lookups/` prefix. It is later used to fetch the data.

- parsePattern (required): A DPL (Dynatrace Pattern Language) expression to parse the uploaded data.

- lookupField (required): The unique field in the lookup data that acts as ID.

- overwrite: If set to true, the API will overwrite previously written content in the file.

- displayName: A user-friendly name for the file.

- description: A description of the file.

- skippedRecords: The number of initial records to skip in the uploaded data. The default is 0.

- timezone: The timezone for parsing time and date fields.

- locale: The local for parsing locale-specific information.

- autoFlatten: Set it to true to extract nested fields to the root level when the specified DPL pattern results in a single record-type field.

#### Upload data in Dynatrace app

In the following example, when the user selects the button Store Currency rates, the app will upload the currency rate information to the Grail Resource Store into filePath `/lookups/currencyrates`. In the example, we're hardcoding the currency rates, but you can easily use an app function to fetch the data from a third-party API and store it.

ui/app/pages/Home.tsx
`tsx
import React, { useCallback } from 'react';import { Flex } from '@dynatrace/strato-components/layouts';import { Button } from '@dynatrace/strato-components/buttons';const data = [ { source: 'USD', EUR: 0.88, AUD: 1.39, PLN: 3.94 }, { source: 'EUR', USD: 1.14, AUD: 0.72, PLN: 0.25 },];export const Home = () => { const handleClick = useCallback(() => { if (!data) { console.error('No conversion rate data available.'); return; } const request = { lookupField: 'data', filePath: '/lookups/currencyrates', overwrite: true, displayName: 'Currency Rates', skippedRecords: 0, autoFlatten: false, timezone: 'UTC', locale: 'en_US', description: 'Currency Rates for Conversion', parsePattern: 'JSON:data', }; const blob = new Blob([JSON.stringify(data)], { type: 'application/json', }); const file = new File([blob], 'currencyrates.json', { type: 'application/json', }); const formData = new FormData(); formData.append('request', JSON.stringify(request)); formData.append('content', file); fetch('/platform/storage/resource-store/v1/files/tabular/lookup:upload', { method: 'POST', body: formData, }) .then((response) => { if (!response.ok) { throw new Error(`HTTP error! status: ${response.status}`); } }) .then((json) => { console.log('Lookup data uploaded successfully:'); }) .catch((error) => { console.error('Error uploading lookup data:', error); }); }, []); return ( Flex flexDirection="column" alignItems="center" padding={32}> Button onClick={handleClick}>Store Currency RatesButton> Flex> );};
`

TipThis operation requires the scope `storage:files:write`. Read more about scopes in this guide.

### Fetch the uploaded data

The uploaded data in Grail can be accessed using the DQL `load` command. Here is a DQL example:

`tsx
load "/lookups/currencyrates"
`

#### Fetch data in Dynatrace app

In the following example, we mimic real user event data with DQL's `data` command and convert the balance from USD into EUR with the uploaded currency rates. We'll fetch this data using the `useDql` React hook and show it in the Strato `DataTable` component.

ui/app/App.tsx
`tsx
import React from 'react';import { Flex } from '@dynatrace/strato-components/layouts';import { useDql } from '@dynatrace-sdk/react-hooks';import { convertToColumns, DataTable } from '@dynatrace/strato-components/tables';export const App = () => { const query = `data json:""" [ { "email": "first@first.com", "balance": 10, "currency": "USD" }, { "email": "second@first.com", "balance": 130, "currency": "USD" }, { "email": "third@first.com", "balance": 20, "currency": "USD" } ] """| fieldsAdd eurBalance = balance * lookup([ load "/lookups/currencyrates"], sourceField: currency, lookupField:data[source])[data][EUR]`; const result = useDql(query); return ( Flex flexDirection="column" alignItems="center" padding={32}> {result.data && DataTable data={result.data?.records} columns={convertToColumns(result.data?.types)} />} Flex> );};
`

TipThis operation requires the scope `storage:files:read`. Read more about scopes in this guide.

### Handling user permission

Most users may not have permission to write lookup data or may only have access to specific folders. Applications must gracefully handle such restrictions, allowing users to choose where to store data within the customer-managed `/lookups/` directory. To respect user control and permissions, avoid creating predefined structures like `/lookups/dt/`.

In the future, Dynatrace may introduce a `/dt/` prefix for structured data management and enhanced permission handling. This feature is under development and will align with evolving use cases.

---

## data/store-user-generated-data

`/develop/guides/data/store-user-generated-data/`

- Data
- Store user-generated data

## Store user-generated data

- How-to guide
- 4-min readIf your app allows the user to save user-generated data that needs to be available across multiple user sessions, our document service is your best option. One example of such user-defined data is to-do items that the user enters in a Todo app.
This guide explains how you can store, update, and delete data from the document service.

In the following examples, you'll see two code snippets for each type of operation.

- The React hook version uses the `@dynatrace-sdk/react-hooks` package for all the operations. You can use this in your React frontend code.

- The Client SDK version uses the `@dynatrace-sdk/client-document`) package for all the operations. The example code shown uses this package in an app function. You can use the same code in Notebook, Dashboard, and Workflow as well.

### Create a document

To create a document, use the `useCreateDocument` hook. This hook provides an `execute` function that you can use to create a new document. It also provides some additional fields with information about the loading status, errors, and the response. These fields are common to all the document hooks. The example below shows how to create a Todo list document:

- React Hook
- Client SDKui/app/App.tsx
`tsx
import React from 'react';import { useCreateDocument } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';import { Page } from '@dynatrace/strato-components/layouts';const todos = [ { title: 'Send email to John about vacation', done: false, }, { title: 'Plan workshop for next week', done: false, },];export const App = () => { const { execute, data, error, isLoading } = useCreateDocument(); const handleClick = () => { execute({ body: { name: 'My Todos', type: 'TodoList', content: new Blob([JSON.stringify(todos)], { type: 'application/json', }), }, }); }; return ( Page> Page.Main> Button onClick={handleClick}>Create TodosButton> Page.Main> Page> );};
`
api/todo-create.function.ts
`tsx
import { documentsClient } from '@dynatrace-sdk/client-document';const todos = [ { title: 'Send email to John about vacation', done: false }, { title: 'Plan workshop for next week', done: false },];export default async function (payload: unknown = undefined) { try { const data = await documentsClient.createDocument({ body: { name: 'My Todos', type: 'TodoList', content: new Blob([JSON.stringify(todos)], { type: 'application/json', }), }, }); return data ? 'document created successfully' : 'document creation failed'; } catch (error) { console.error('Error creating document:', error); return 'document creation failed due to an error'; }}
`

TipThis operation requires the scope `document:documents:write`. Read more about scopes in this guide.

### List documents

The `useListDocuments` hook lets you to get a filtered list of the available documents. Besides the common fields, this hook also provides a `refetch` function to refetch the list of documents. The following code fetches the documents of type TodoList.

- React Hook
- Client SDKui/app/App.tsx
`tsx
import React from 'react';import { useListDocuments } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';import { List, Text } from '@dynatrace/strato-components/typography';import { Page } from '@dynatrace/strato-components/layouts';export const App = () => { const { data, refetch } = useListDocuments({ filter: `type == 'TodoList'`, }); const handleClick = () => { refetch().then((list) => console.log(list.documents)); }; return ( Page> Page.Main> {data && ( List> {data.documents.map((doc) => ( Text key={doc.id}>{doc.name}Text> ))} List> )} Button onClick={handleClick}>Refetch TodosButton> Page.Main> Page> );};
`
api/todo-list.function.ts
`tsx
import { documentsClient } from '@dynatrace-sdk/client-document';export default async function (payload: unknown = undefined) { try { const list = await documentsClient.listDocuments({ filter: `type == 'TodoList'`, }); return list?.documents ?? []; } catch (error) { console.error('Error fetching TodoList documents:', error); return []; }}
`

TipThis operation requires the scope `document:documents:read`. Read more about scopes in this guide.

### Get document content

To retrieve the content of a specific document, you can use the `useDownloadDocument` hook. This hook expects the document ID as a parameter and returns binary data with the document's contents, which you can extract by calling the `get` function. This example shows how to fetch the content for the Todo list document that we created in the first step:

- React Hook
- Client SDKui/app/App.tsx
`tsx
import React, { useState, useEffect } from 'react';import { useDownloadDocument } from '@dynatrace-sdk/react-hooks';import { Page } from '@dynatrace/strato-components/layouts';import { Checkbox } from '@dynatrace/strato-components/forms';interface Todo { title: string; done: boolean;}export const App = () => { const [todos, setTodos] = useStateTodo[]>(); const { data } = useDownloadDocument({ id: 'ff96e29d-2622-48f0-8c88-b2f20b2cf532', }); useEffect(() => { if (data) { data.get('json').then((todos) => { setTodos(todos as Todo[]); }); } }, [data]); return ( Page> Page.Main> {todos && todos.map((todo) => ( Checkbox key={todo.title} name="done" defaultValue={todo.done}> {todo.title} Checkbox> ))} Page.Main> Page> );};
`
api/todo-get.function.ts
`tsx
import { documentsClient } from '@dynatrace-sdk/client-document';export default async function () { try { const documentContent = await documentsClient.downloadDocumentContent({ id: 'ff96e29d-2622-48f0-8c88-b2f20b2cf532', }); const jsonContent = (await documentContent?.get('json')) as string; if (!jsonContent) { console.warn('No JSON content found in the document.'); return null; } return jsonContent; } catch (error) { console.error('Error downloading document content:', error); return null; }}
`

TipThis operation requires the scope `document:documents:read`. Read more about scopes in this guide.

### Update document

Whenever you need to change the contents of a document, use the `useUpdateDocument` or the `useUpdateDocumentMetadata` hooks.
For all modifying operations, keep optimistic locking in mind. Every document has a version that's incremented whenever its metadata or content is modified. For every modifying operation, you have to pass this exact version, which you can retrieve with the `useDocumentMetadata` hook. It could look like the following:

- React Hook
- Client SDKui/app/App.tsx
`tsx
import React from 'react';import { useDocumentMetaData, useUpdateDocument } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';import { Page } from '@dynatrace/strato-components/layouts';const updatedTodos = [ { title: 'Send e-mail to John concerning vacation', done: true, }, { title: 'Plan workshop for next week', done: false, },];export const App = () => { const metadata = useDocumentMetaData({ id: 'ff96e29d-2622-48f0-8c88-b2f20b2cf532', }); const { execute } = useUpdateDocument(); const handleClick = () => { if (metadata.data) { execute({ id: metadata.data.id, optimisticLockingVersion: metadata.data.version, body: { content: new Blob([JSON.stringify(updatedTodos)], { type: 'application/json', }), }, }); } }; return ( Page> Page.Main> Button onClick={handleClick}>Update TodosButton> Page.Main> Page> );};
`
api/todo-update.function.ts
`tsx
import { documentsClient } from '@dynatrace-sdk/client-document';export default async function (payload: unknown = undefined) { const updatedTodos = [ { title: 'Send e-mail to John concerning vacation', done: true, }, { title: 'Plan workshop for next week', done: false, }, ]; try { const metadata = await documentsClient.getDocumentMetadata({ id: 'ff96e29d-2622-48f0-8c88-b2f20b2cf532', }); if (!metadata) { console.warn('No metadata found for the document.'); return 'document updation failed'; } const data = await documentsClient.updateDocumentContent({ id: metadata.id, optimisticLockingVersion: metadata.version, body: { content: new Blob([JSON.stringify(updatedTodos)], { type: 'application/json', }), }, }); return data ? 'document updated successfully' : 'document updation failed'; } catch (error) { console.error('Error updating document:', error); return 'document updation failed'; }}
`

TipThis operation requires the scope `document:documents:write`. Read more about scopes in this guide.

### Delete document

You can delete documents as well. To do so, use the `useDeleteDocument` hook. To delete a document, you need to provide the optimistic locking version of the document you want to delete.
To delete the document we created in the first step, your code should look like this:

- React Hook
- Client SDKui/app/App.tsx
`tsx
import React from 'react';import { useDocumentMetaData, useDeleteDocument } from '@dynatrace-sdk/react-hooks';import { Button } from '@dynatrace/strato-components/buttons';import { Page } from '@dynatrace/strato-components/layouts';export const App = () => { const metadata = useDocumentMetaData({ id: 'ff96e29d-2622-48f0-8c88-b2f20b2cf532', }); const { execute } = useDeleteDocument(); const handleClick = () => { if (metadata.data) { execute({ id: metadata.data.id, optimisticLockingVersion: metadata.data.version, }); } }; return ( Page> Page.Main> Button onClick={handleClick}>Delete TodosButton> Page.Main> Page> );};
`
api/todo-delete.function.ts
`tsx
import { documentsClient } from '@dynatrace-sdk/client-document';export default async function (payload: unknown = undefined) { try { const metadata = await documentsClient.getDocumentMetadata({ id: 'ff96e29d-2622-48f0-8c88-b2f20b2cf532', }); if (!metadata) { console.warn('No metadata found for the document.'); return 'document deletion failed'; } await documentsClient.deleteDocument({ id: metadata.id, optimisticLockingVersion: metadata.version, }); return 'document successfully delete'; } catch (error) { console.error('Error deleting document:', error); return 'document deletion failed'; }}
`

TipThis operation requires the scope `document:documents:delete`. Read more about scopes in this guide.

### Related topics

- Document service

---

## deploy-your-app

`/develop/guides/deploy-your-app/`

- Deploy your app

## Deploy your app

- How-to guide
- 1-min read

### Permissions

To deploy your Dynatrace app, you need the following IAM permissions:

- `app-engine:apps:install`

- `app-engine:apps:run`

If you're planning to uninstall it completely, you might also need the following permission:

- `app-engine:apps:delete`

### Deploy from a local device

- Ensure your user has the required IAM permissions.

- Navigate to the root of your project.

- Run the following command in your terminal:

`tsx
npx dt-app deploy
`

### Deploy from a CI/CD pipeline

- Create an OAuth client that has the required IAM permissions.

- In your CI/CD pipeline, set the environment variables `DT_APP_OAUTH_CLIENT_ID` and `DT_APP_OAUTH_CLIENT_SECRET` with the generated client ID and client secret.

- Run the following command within your pipeline:

`tsx
npx dt-app deploy
`

#### Examples

- Jenkins
- Github Actions
- GitlabJenkinsfile
`tsx
pipeline { // Replace the following lines with a Docker or Kubernetes agent with an image with node v24 agent { kubernetes { // Example of a Kubernetes agent cloud 'linux-amd64' yaml """ kind: Pod spec: containers: - name: nodejs image: node24 args: - cat tty: true """ defaultContainer 'nodejs' } } stages { stage('Install') { steps { sh('npm ci') } } stage('Lint') { steps { sh 'npm run lint' } } stage('Build') { steps { sh('npx dt-app build') } } stage('Deploy') { steps { sh('npx dt-app deploy --skip-build') } } }}
`
.github/workflows/main.yml
`tsx
name: CIon: push: branches: - main pull_request: branches: - mainjobs: build: runs-on: ubuntu-latest steps: - name: Checkout code uses: actions/checkout@v2 - name: Setup Node uses: actions/setup-node@v2 with: node-version: '24' - name: Install run: npm ci - name: Lint run: npm run lint - name: Build run: npx dt-app build - name: Deploy run: npx dt-app deploy --skip-build
`
.gitlab-ci.yml
`tsx
default: image: node:24stages: - install - lint - build - deployinstall: stage: install script: - npm ci artifacts: paths: - node_modules/lint: stage: lint script: - npm run lintbuild: stage: build script: - npx dt-app build artifacts: paths: - .dt-app - distdeploy: stage: deploy script: - npx dt-app deploy --skip-build
`

NoteEvery time you modify the `app.config.json` file, you must increase the version number in the file before re-deploying the app.If you don't increase the version number, you need to uninstall the current deployed version.

### Uninstall the app

- Ensure your user or the OAuth token used on the CI/CD pipeline has the `app-engine:apps:delete` permission.

- Run the following command in your terminal:

`tsx
npx dt-app uninstall
`

---

## dynatrace-intelligence/forecast-with-dynatrace-intelligence

`/develop/guides/dynatrace-intelligence/forecast-with-dynatrace-intelligence/`

- Dynatrace Intelligence
- Forecast with Dynatrace Intelligence

## Forecast with Dynatrace Intelligence

- How-to guide
- 5-min readNote"Dynatrace Intelligence" is the umbrella term for all AI in Dynatrace, including generative, agentic, causal, and predictive AI. It replaces "Davis AI" and "Davis CoPilot" and expands upon their capabilities. The terms "Davis" and "CoPilot" persist in certain locations, including APIs, Swagger, scopes, and Grail. These references are still relevant for Dynatrace Intelligence.
The latest Dynatrace platform provides general-purpose AI/ML services covering various functionalities. In this guide, you'll learn the intricacies of using the Dynatrace predictive and causal AI platform service from your Dynatrace® Apps.

### Get available analyzers

Before getting started, one of the main questions to answer is which data analyzers are available for you to use. To see the available analyzers, you have two options:

Check out the `/analyzers` endpoint in the . It's the easiest way of accessing every option of the different endpoints.

Use the Dynatrace data analyzers SDK in your app:

`tsx
import { analyzersClient } from '@dynatrace-sdk/client-davis-analyzers';const { analyzers, totalCount, nextPageKey } = await analyzersClient.queryAnalyzers({ filter: "name contains 'statistic'", addFields: 'baseAnalyzer, type, input',});
`

TipThis operation requires the scope `davis:analyzers:read`. Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

Once you've chosen the analyzer that best fits your use case, you need to understand its requirements. The next section describes how to do that.

### Analyzers input and output

All Dynatrace data analyzers have a basic set of input parameters, like `timeframe` or `logVerbosity`. Additionally, each analyzer needs a specific set of input parameters unique to that analyzer. There are a couple ways to get this information:

Using the .

Use the SDK to get the analyzer definition:

`tsx
const analyzer = await analyzersClient.getAnalyzer({ analyzerName: 'dt.statistics.GenericForecastAnalyzer',});
`

TipThis operation requires the scope `davis:analyzers:read`. Read more about scopes in this guide.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

The output of each analyzer can be very different as well. You need to query the analyzer definition using one of the two methods above to get the output definition.

### Time series forecast analysis

At this point, we know which analyzer we want to use and we understand its input parameters and its output definition. Now, we get to use it. Let's look at a complete example of how you would use the `dt.statistics.GenericForecastAnalyzer` analyzer to get a forecast of any time series metric.

#### Execute analyzer

TipThis operation requires the scope `davis:analyzers:execute`. Read more about scopes in this guide.
Let's begin by creating a function that will request the forecast analysis:

loadForecast.ts
`tsx
import { analyzersClient } from '@dynatrace-sdk/client-davis-analyzers';export const loadForecast = async (query: string) => { const analyzerName = 'dt.statistics.GenericForecastAnalyzer'; const response = await analyzersClient.executeAnalyzer({ analyzerName, body: { timeSeriesData: { expression: query, }, }, }); // ...};
`

NoteDepending on the chosen analyzer and the analyzer input, additional scopes might be required, for example, `storage:buckets:read` and `storage:metrics:read` to enable the analyzer to read time series data from Grail™.
This function receives a DQL query as a parameter and triggers an async forecast analysis on the results of running said query via the `executeAnalyzer` function from the `analyzersClient`. If the analysis takes more than two seconds to finish, the response will contain a `requestToken` that will allow you to poll until the results are available.

#### Poll analyzer execution

Let's create a new `pollExecution` function to handle the polling logic.

pollExecution.ts
`tsx
import { AnalyzerResult, analyzersClient } from '@dynatrace-sdk/client-davis-analyzers';export const pollExecution = async (analyzerName: string, requestToken: string): PromiseAnalyzerResult> => { const MAX_ATTEMPTS = 10; const INTERVAL_MS = 1000; let attempts = 0; while (attempts MAX_ATTEMPTS) { await new Promise((resolve) => setTimeout(resolve, INTERVAL_MS)); const { result } = await analyzersClient.pollAnalyzerExecution({ analyzerName, requestToken, }); if (result.executionStatus === 'COMPLETED') { return result; } if (result.executionStatus === 'ABORTED') { throw new Error('The analyzer execution was aborted'); } attempts++; } const cancelResponse = await analyzersClient.cancelAnalyzerExecution({ analyzerName, requestToken, }); if (cancelResponse && cancelResponse.result.executionStatus === 'COMPLETED') { return cancelResponse.result; } throw new Error('Max polling retries reached');};
`

Aside from the simple polling implementation, we've introduced two new functions:

- `pollAnalyzerExecution`: This function allows you to check the analysis execution status with the analyzer name and the request token you got in the initial request.

- `cancelAnalyzerExecution`: Once we've reached the max polling attempts, we recommend canceling the analysis execution. If the analysis finishes between the last poll and the cancellation, this function will return the analysis results. Otherwise, the response will be `undefined`.

#### Handle analyzer output

We can now use `pollExecution` in our main function and extract the forecasting information as a `TimeseriesBand` from the analysis output:

loadForecast.ts
`tsx
import { analyzersClient } from '@dynatrace-sdk/client-davis-analyzers';import { convertToTimeseriesBand, TimeseriesBand } from '@dynatrace/strato-components/charts';import { pollExecution } from './pollExecution';export const loadForecast = async (query: string): PromiseTimeseriesBand> => { const analyzerName = 'dt.statistics.GenericForecastAnalyzer'; const response = await analyzersClient.executeAnalyzer({ analyzerName, body: { timeSeriesData: { expression: query, }, }, }); const analysisResult = response.requestToken ? await pollExecution(analyzerName, response.requestToken) : response.result; if (analysisResult.executionStatus === 'COMPLETED') { const analyzerOutput = analysisResult.output[0]; const timeseriesBandData = convertToTimeseriesBand( analyzerOutput.timeSeriesDataWithPredictions.records[0], analyzerOutput.timeSeriesDataWithPredictions.types[0], ); if (timeseriesBandData) { return timeseriesBandData.timeseriesBand; } throw new Error('Unexpected error'); } throw new Error('The analyzer execution was aborted');};
`

Your `loadForecast` function is now ready. You can provide any time series DQL query to this function, and it will handle the forecast analysis and return it in `TimeseriesBand` format, which you can use to visualize it.

TipYou can learn more about visualizing a `TimeseriesBand` from the `TimeseriesChart` reference page.

### Troubleshooting

A data analyzer execution can fail for different reasons. If it does fail, the response will contain a log array that you can use to figure out why the analysis was unsuccessful. For instance, if the provided query doesn't return enough data points, the response will look something like this:

`tsx
{ "result": { "resultId": "4e1a8a1efd560193", "resultStatus": "FAILED", "executionStatus": "COMPLETED", "input": { ... }, "logs": [ { "level": "WARNING", "message": "More historical data is required to generate a reliable forecast. Increase the timeframe or adapt the resolution to include a minimum of 14 non-NaN observations.", "analyzerName": "dt.statistics.GenericForecastAnalyzer" }, { "level": "SEVERE", "message": "The analysis of the data was not successful.", "analyzerName": "dt.statistics.GenericForecastAnalyzer" } ], "output": [] }}
`

### Related links

- Visit the

- Learn more about the Dynatrace Intelligence service

- Learn more about Forecast analysis

---

## guides

`/develop/guides/`

## Guides

- 1-min read

###

#### Access platform APIs from outside
Call platform APIs and app functions from outside Dynatrace.How-to guide

#### App functions
Learn about app functions for the app backend.Explanation

#### Automate dependency updates
Automatically update Dynatrace app dependencies with Renovate.How-to guide

#### Code optimization
Introduction to code optimization for Dynatrace appsConcept

#### Data
Introduction to the types of storage available for your Dynatrace appExplanation

#### Deploy your app
Deploy your Dynatrace application.How-to guide

#### Keyboard shortcuts
Access the reference library of Dynatrace keyboard shortcuts.Reference

#### Navigation
Get an overview of navigation patterns, deep linking, and interoperability in Dynatrace Apps.

#### Privacy
Learn about privacy by design for Dynatrace Apps.Explanation

#### Reuse code within your app
Learn to reuse code in your app.How-to guide

#### Security
Understand security-related topics for developing Dynatrace Apps.Explanation

#### Support dark and light themes
Learn how to implement dark and light themes in your Dynatrace App.How-to guide

#### Workflows
Basic concepts of worflows in Dynatrace, which let you automatically act on monitoring dataExplanation

---

## keyboard-shortcuts

`/develop/guides/keyboard-shortcuts/`

- Keyboard shortcuts

## Keyboard shortcuts

- 1-min readKeyboard shortcuts are a powerful tool for saving time with user interfaces primarily designed for mouse and touch input. As an app developer, you can list your app's shortcuts for users with the available modifiers and keys listed below.

All available keywords that you can use as `keyBindings` are based on Key values for keyboard events.

#### Before you begin coding

- For best practices, see Plan keyboard shortcuts for your app.

- For step-by-step instructions, see Display keyboard shortcuts in your app.

#### Available Modifiers

- `Alt`

- `AltGraph`

- `CapsLock`

- `Control`

- `Meta`

- `Windows`

- `Command`

- `NumLock`

- `ScrollLock`

- `Shift`

#### Available Keys

- `ArrowLeft`, `ArrowUp`, `ArrowRight`, `ArrowDown`

- `Tab`

- `Dead`

- `Backspace`

- `Enter`

- `Escape`

- `ContextMenu`

- `Insert`, `Home`, `Delete`, `End`

- `PageUp`, `PageDown`

- `Pause`

- `PrintScreen`

- `Space`

- `F1` to `F12`

- `a` to `z` (lowercase)

- `0` to `9`

- `~`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `()`, `_`, `-`, `=`

- `{`, `}`, `[`, `]`, `:`, `;`, `'`, `"`, `,`, `.`, `/`, , `?`, `+`

---

## keyboard-shortcuts/display-app-keyboard-shortcuts

`/develop/guides/keyboard-shortcuts/display-app-keyboard-shortcuts/`

- Keyboard shortcuts
- Display keyboard shortcuts

## Display keyboard shortcuts in your app

- How-to guide
- 2-min readIn this guide, you'll learn how to display keyboard shortcuts to users of your app.

### Before you begin

Read the guidance in Plan keyboard shortcuts for your app.

### 1. Create the key binding

A shortcut or `keyBinding` consists of modifiers and a key. It can have a single key and any number of modifiers. Some examples are `Control+k`, `Shift+/`, and `Control+Shift+m`.

First, create a `keyBinding` for your app based on actual shortcuts.

### 2. Add the shortcuts in the app configuration

Now, you need to add the shortcuts in the app configuration file. In the following example, you're adding a new config section, `uiCommands`, that defines all the shortcuts for your app:

app.config.json
`tsx
{ "environmentUrl": "", "app": { "id": "", "name": "", "version": "0.0.0", "description": "", "scopes": [], "uiCommands": { "categories": [ { "id": "general.category", "name": "General", "commands": [ { "id": "open.search", "description": "Open global search dialog", "keyBindings": { "macos": ["Command+k"], "other": ["Control+k"] } }, { "id": "open.keyboard", "description": "Open keyboard keyBindings dialog", "keyBindings": ["Shift+/"] } ] } ] } }}
`

In the example, you have the following:

- You have created a category named General using the `categories` key.

- You created commands using the `commands` key and specified `id`, `description`, and `keyBindings` for each command.

- You have commands with separate key bindings for MacOS.

NoteYou need to restart the development server each time you change app configuration to see the updates.

### 3. Verify the shortcuts

To verify the shortcuts, open your app in the browser and press `?`. You'll get a modal with available keyboard shortcuts in your and all active apps, along with platform-wide shortcuts.

NoteIn this guide, you only learned to display your app's keyboard shortcuts. You're not creating them.

### Related topics

- Keyboard shortcuts

---

## keyboard-shortcuts/plan-keyboard-shortcuts

`/develop/guides/keyboard-shortcuts/plan-keyboard-shortcuts/`

- Keyboard shortcuts
- Plan keyboard shortcuts

## Plan keyboard shortcuts for your app

- Explanation
- 4-min readKeyboard shortcuts let users save time when performing common actions. They turn power-user workflows into muscle memory and make Dynatrace apps fully operable without a mouse. They are also a WCAG requirement, ensuring every feature is accessible from the keyboard alone.

This guide helps you plan when to add new shortcuts, how to align them across apps, and where to surface them so users can discover them. You will also learn about platform guidance and how to track adoption in Dynatrace dashboards.

### Identify user journeys that benefit from shortcuts

Start by mapping the repeat-heavy tasks in your app. High-frequency paths include filtering a table, stepping through log lines, or toggling chart legends. Also, consider flow breakers, which are interactions that force users to leave the keyboard, such as opening a context menu or expanding a panel.

Ask yourself: "If I had to do this 50 times an hour, would I still want to use the mouse?" If that feels inefficient or frustrating, a shortcut could save time and effort.

#### Avoid shortcuts for

- Deep-link functions used only once per session

- Destructive actions requiring confirmation

- Mobile views, where shortcut indicators are typically hidden to keep the UI clear on smaller screens

### Choosing and aligning shortcut patterns

Consistency across apps is critical. Users should not have to learn different keys for the same action in each Dynatrace app.

#### Reuse the baseline set

- Universal shortcuts like Copy (`Ctrl/Cmd+C`), Paste (`Ctrl/Cmd+V`), Undo (`Ctrl/Cmd+Z`), and Search (`Ctrl/Cmd+F`) should behave as users expect. Do not override them.

#### Follow platform modifiers

- On macOS, use `⌘` instead of `Ctrl`, per Apple HIG conventions.

- On Windows/Linux, use `Ctrl` and follow patterns like `Alt`, `F6`, `Ctrl+Tab`, and arrow keys, per Microsoft Fluent guidance.

#### Reserve keys for global patterns

- For example:

- `Ctrl/⌘+K` for the command palette (`open.search`)

- `Shift+/` or `?` to open the keyboard-shortcuts overlay (`open.keyboard`)

- `Ctrl/⌘+F` for in-context search

- Use the `keyBindings` schema to declare both macOS and Windows/Linux variants so each OS displays the correct label.

### Surfacing shortcuts in the UI

Shortcuts should be easy to discover and use. Consider these methods for surfacing them:

#### Tooltips

- Provide contextual, low-noise hints next to icons or buttons.

- Ensure tooltips are visible on focus (for keyboard users) as well as hover.

#### Menu hints

- Display shortcuts in dropdown or kebab menus, aligning them right-justified to improve readability.

- Refer to the Keyboard Shortcuts Design Guide for additional best practices.

#### Global cheat-sheet modal

- Offer a complete, searchable reference (e.g., `Shift+/` or `?`).

- Keep it up-to-date automatically via uiCommands.

#### Command palette (`Ctrl/⌘+K`)

- Use the palette for long-tail actions and display matching shortcuts in the results list.

#### Onboarding tips

- Introduce new users to critical shortcuts sparingly.

### Related topics

- Keyboard shortcuts

---

## navigation

`/develop/guides/navigation/`

- Navigation

## Navigation in Dynatrace Apps

- 1-min readNavigation is a key part of building Dynatrace Apps that are easy to use, share, and integrate. This section covers best practices and platform guidance for:

- URL sharing and navigation, so users can bookmark and share specific app states.

- Using Intents to enable cross-app navigation and interoperability.

- Other navigation patterns and techniques for a seamless user experience.

###

#### Intents
Use intents, the cross-app communication mechanisms in Dynatrace.Explanation

#### Page tokens
Use page tokens to access app routes in your app.How-to guide

#### URL sharing and navigation
Create shareable URLs and support navigation in Dynatrace Apps.

---

## navigation/intents

`/develop/guides/navigation/intents/`

- Navigation
- Intents

## Intents

- Explanation
- 1-min readWe use the intents mechanism to extend an app's functionality. An intent is a message object you define in an app that allows you to pass the user flow from one app to another.

Discover more about how to send, receive, and debug intents in Dynatrace apps. Plus, explore relevant use cases and examples on this topic.

###

#### About intents
Learn how intents enable context-aware cross-app navigation in Dynatrace, including explicit intents, add-ons, and the Open with dialog.Explanation

#### Debug intents
Debug your intents using AppShell methods.Concept

#### Receive intents
Receive intents with data that trigger actions in your app.How-to guide

#### Send intents
Send intents from your app to a receiving app.How-to guide

---

## navigation/intents/about-intents

`/develop/guides/navigation/intents/about-intents/`

- Navigation
- Intents
- About intents

## About intents

- Explanation
- 7-min readIntents are the platform mechanism for context-aware cross-app navigation. When a user interacts with a resource—such as an entity, a metric, or a DQL query—and wants to do something with it in another app, an intent carries the relevant context from the source app to the target app through the AppShell.

Every Dynatrace app runs inside an `iframe` hosted by the AppShell. Regular links can navigate between apps, but they can't carry structured context with them. Intents solve this: they let your app pass data—entity IDs, timeframes, queries—to another app in a way the platform can coordinate, so the target app knows what to show.

### How to deliver an intent

Intents reach users through different mechanisms, ordered by specificity. Choosing the right one determines whether users land where they need to go or get stuck picking from a list.

#### Explicit intents

Use an explicit intent when your app knows exactly where to send the user. The user clicks, the target app opens with all context applied. No dialog, no choices.

This is the most common pattern. It powers primary actions in intent menus and the left side of the `IntentButton` split button, the primary action such as View in Hosts or Open in Notebooks.

When to use—the target app and action are obvious for the resource type. You're connecting a host entity to the Hosts app, a trace ID to Distributed Traces, a DQL query to Notebooks. The 80/20 case.

How it works—your app calls `sendIntent()` with a `recommendedAppId` and `recommendedIntentId`, or uses the with those options set. The AppShell skips the Open with... dialog and opens the target app directly.

`tsx
IntentButton payload={{ 'dt.entity.host': 'HOST-F66B242CD3A5E38E' }} options={{ recommendedAppId: 'dynatrace.classic.hosts', recommendedIntentId: 'view-host', }}> View in HostsIntentButton>
`

TipDo not hardcode your own entity-to-app mappings. Use the platform's recommended intents mapping to determine which target app and intent ID to use for a given resource type. This keeps navigation consistent across the platform.

#### Open with... dialog (fallback)

The Open with... dialog is the fallback that surfaces every app capable of handling the current intent payload. It appears when no explicit intent is configured or when the user deliberately wants to see all options.

When it appears:

- Your app calls `sendIntent()` without specifying a `recommendedAppId`.

- The user clicks the three-dot menu on an `IntentButton` and selects the Open with... option.

- The `recommendedAppId` doesn't exist or can't handle the payload.

What to know:

- Always provide this as a fallback. Do not suppress it.

- In the `IntentButton` split button, the Open with... option sits at the bottom of the three-dot menu, after explicit intents and add-ons.

- The label must be exactly `Open with...` with no variations.

### The IntentButton

The `IntentButton` is a split button from the Strato Design System that implements all three mechanisms in one component. The left side triggers the primary explicit intent directly, for example, View in Hosts. The right side opens a menu with additional explicit intents, add-ons, and Open with... as the last option.

Use `IntentButton` for straightforward cases. Use `sendIntent()` from `@dynatrace-sdk/navigation` when you need more control over the trigger. For example, responding to a table row click or a custom interaction.

### Recommended intents

Without central coordination, each app builds its own mapping from resource types to target apps. This creates inconsistency: clicking a host ID in one app opens the Hosts app, while clicking the same ID in another opens something different.

Recommended intents solve this with a centrally managed mapping from resource types to recommended target apps. Instead of hardcoding `recommendedAppId: 'dynatrace.classic.hosts'` in your source code, you query the recommended intents list to get the right target for `dt.entity.host`.

This ensures users always land in the same destination for the same resource type, regardless of which app they started from.

### How intents work under the hood

#### Lifecycle

Source app sends an intent—your app calls `sendIntent(payload, options)` or renders an . The communication uses the `window.postMessage` API to reach the AppShell.

AppShell resolves the target—if a `recommendedAppId` and `recommendedIntentId` are provided and valid, the AppShell opens that app directly. Otherwise, it finds all installed apps whose intent declarations match the payload properties and shows the "Open with..." dialog.

AppShell launches the target app—the target app opens in an iframe (full page for navigation intents, modal for add-ons). The intent payload is passed as URL query arguments.

Target app handles the intent—the target app calls `getIntent()` to read the payload and perform the requested action.

#### Intent matching

The AppShell matches an intent payload against every installed app's intent declarations in `app.config.json`. A match occurs when an app declares intent properties that the source app's payload satisfies:

- If the target declares `dt.entity.host` as `required: true`, the source must include `dt.entity.host` in the payload.

- Extra properties in the payload that the target does not declare are stripped before delivery.

- Use `keyProperties` in `sendIntent()` to narrow matching when your payload contains multiple properties.

#### Payload structure

An intent payload is a set of key-value pairs carrying the context to share:

`tsx
import { IntentPayload } from '@dynatrace-sdk/navigation';const intent: IntentPayload = { 'dt.entity.host': 'HOST-F66B242CD3A5E38E', 'dt.timeframe': { from: 'now-2h', to: 'now' },};
`

Common payload properties include entity IDs (`dt.entity.*`), DQL queries (`dt.query`), and timeframes (`dt.timeframe`). The target app defines which properties it accepts and requires in its intent declaration.

#### Limitations

- One-way payload delivery—the initial intent payload is passed via URL query arguments when the target app loads. For two-way communication, use intents-with-response, where the target add-on can pass data back asynchronously.

- Keep payloads concise—while the previous URL length limitation has been fixed, it's still best practice to pass identifiers and queries rather than large data blobs.

### Security context

Every Dynatrace app runs inside its own cross-origin iframe in the AppShell. API calls from any app, whether it opened via a regular intent or as a modal add-on, run under that app's security context, not the calling app's. Each app uses its own identity, OAuth scopes, and permissions.

Cross-origin iFrames comply with the AppShell's Content Security Policy rules.

### Context sharing

When a target app opens through an intent, it can access:

- Platform context shared between all apps: timeframe, segment, tenant info

- Intent payload—the specific data passed by the source app via the intent

- The target app does not have access to the source app's internal state beyond what is in the intent payload.

This applies equally to full-page navigation intents and modal add-ons.

### Intents as public APIs

Intents behave like public APIs. An app's intent types define its public contract. Consuming apps can rely on a specific intent type always accepting the same payload shape.

- Intent types have owners, just like API owners own API types.

- The intent type name and its required properties form a stable interface.

- Breaking changes to an intent's required properties are breaking API changes and require a deprecation process to phase out safely.

### Choose the right mechanism

 |
 | Scenario | Use | Why
 | User clicks a host entity and should open in the relevant app | Recommended intent | Resolve the target app dynamically, do not hardcode the destination
 | App needs to support a resource type it cannot predict upfront | Open with... | Let the platform's matching find the right targets

### Intent naming guidelines

Every intent has two user-facing identifiers, which affect discoverability and clarity:

- The intent ID—which is the key in `app.config`

- The description—shown on hover in the intent menu

#### Intent IDs

The intent ID is the key you declare in your app configuration under `app.intents`. It should be short, lowercase, and describe the action your app performs.

Use `kebab-case` for new intent IDs:

 |
 | Do | Don't
 | `view-host` | `ViewHost`
 | `share-chart` | `shareChart`
 | `create-alert` | `alert`
 | `view-host-v2` | `view_host_deprecated`
Some older intents use `snake_case` as in `view_host` or `view_service`. Both formats work, but `kebab-case` is the preferred convention for new intents.

Follow these rules:

- Use lowercase letters, underscores, and hyphens only. No spaces, no camelCase.

- Start with a verb that describes the action. For example, `view`, `create`, `edit`, `share`, `add`, or `analyze`.

- Don't include the app name. The intent ID should describe the action, not the destination. The platform maps actions to apps.

- Don't include `deprecated`, `new`, or `old` in the intent ID. Use a `-v2` suffix for versioned replacements.

- Keep it short. The ID appears in URLs and API calls.

#### Descriptions

The `description` field is a short sentence that appears as the label in the intent context menu and in the Open with... dialog. It tells the user what will happen.

Follow this format: `[action verb] + [object]`. See the following table:

 |
 | Good | Bad | Why
 | "View the host" | "Host" | Names the destination, not the action
 | "Add to dashboard" | "Dashboard" | Names the destination, not the action
 | "Analyze query results" | "Notebooks" | Users choose by action, not app name
 | "Create alert" | "Alerting" | Gerund or category name, not an action
The description should complete the sentence `This will...`. If `This will Host` doesn't make sense, rewrite it.

### Next steps

- Send intents—define payloads and trigger intents from your app

- Receive intents—declare intent types and handle incoming payloads

- Debug intents—troubleshoot intent matching and delivery

---

## navigation/intents/debug-intents

`/develop/guides/navigation/intents/debug-intents/`

- Navigation
- Intents
- Debug intents

## Debug intents

- Concept
- 1-min readWhen intents don't behave as expected, you can diagnose the problem with browser console methods and common troubleshooting patterns.

### Browser console methods

The AppShell exposes two global methods for debugging intents from the browser's developer tools.

#### Prerequisites

- Open your browser's developer tools by pressing F12 or `Ctrl+Shift+I` in Windows/Linux and `Cmd+Option+I` in Mac.

- Set the JavaScript context to top, not the app's iFrame. This is important because the AppShell methods are only available in the top-level context.

#### `sendIntent` method

Use this method to test the receiving side of your app without building the sending UI first. The global `sendIntent` method has the same functionality as the SDK method.

Use it to manually trigger an intent from the console and test how the AppShell resolves it:

`tsx
// Test if your intent payload opens the right targetsendIntent({ 'dt.entity.host': 'HOST-F66B242CD3A5E38E' });// Test with explicit target to bypass the dialogsendIntent( { 'dt.entity.host': 'HOST-F66B242CD3A5E38E' }, { recommendedAppId: 'dynatrace.classic.hosts', recommendedIntentId: 'view-host', },);
`

#### `lastIntent` variable

Use it to verify that the source app sent the payload you expected. If the payload is missing properties or has unexpected values, the issue is on the sending side. The `lastIntent` variable holds a reference to the most recently sent intent in your browser window:

`tsx
lastIntent;// -> { intentPayload: { 'dt.entity.host': 'HOST-F66B242CD3A5E38E' } }
`

### Troubleshoot common problems

#### No matching app

Nothing appears in the Open with... dialog. The AppShell found no installed app whose intent declarations match the payload properties.

Check the following:

- Is the target app installed?—the app must be installed in the environment. Check the Hub.

- Do the required properties match?—the target app's intent declaration must have `required: true` for at least one property that the source app includes in the payload. Open the Intent Explorer and compare.

- Is the property name exact?—property names are case-sensitive. `dt.entity.Host` is not `dt.entity.host`.

- Is the schema type correct?—if the target declares `"schema": { "type": "string" }` but the source sends an object, the match fails.

#### App matches unintended payloads

Your app's intent declaration is too broad, so it matches payloads you didn't intend.

Check the following:

- Are your required properties specific enough?—if your intent only requires `dt.query`, which is a very common property, your app matches almost every intent that includes a query. Add more required properties to narrow the match.

- Is this a self-intent?—your app may appear in its own Open with... standalone dialog when you send an intent with properties your own app also handles. This is expected behavior. Use `keyProperties` in `sendIntent()` to narrow matching.

#### Intent opens the wrong app

When using recommended intents, the `recommendedAppId` or `recommendedIntentId` may be wrong.

Check the following:

- Verify the recommended intent mapping—look up the correct app and intent ID for your resource type in the recommended intents list.

- Fallback behavior—if the `recommendedAppId` does not exist or cannot handle the payload, the AppShell falls back to the Open with... dialog. This is by design, not a bug.

#### Target app receives incomplete properties

The AppShell strips payload properties that the target app does not declare in its intent configuration.

Check the following:

- Declare all properties you need—in your `app.config.json`, every property your app needs to read must be listed in the intent's `properties` object. Undeclared properties are silently removed.

- Use `lastIntent` on the target side to see the full payload as received.

#### Add-on modal doesn't open

The intent opened the target app in a new page instead of a modal overlay.

Check the following:

- Is `visualMode: "modal"` set?—the target app's intent declaration in the `app.config.json` file must include `"visualMode": "modal"` for the intent to render as an add-on. You can verify this in the Intent Explorer's Intent Properties panel.

- Is the add-on triggered from within another add-on?—currently, when an add-on triggers another add-on intent, the calling add-on closes and the new one opens. This is a known limitation. The calling context is lost.

#### Intent payload is too large

This was a known issue where the AppShell encoded intent payloads as URL query arguments, and very large payloads caused rendering errors. This has been fixed.

If you still encounter payload size issues, keep payloads concise as a best practice: pass identifiers (entity IDs, query strings) rather than large data objects. If you need to share a large dataset, pass a reference (for example, a document ID) and let the target app fetch the data.

### Next steps

- About intents: Overview of the three intent mechanisms

- Send intents: Define payloads and trigger intents

- Receive intents: Declare intent types and handle incoming payloads

---

## navigation/intents/receive-intents

`/develop/guides/navigation/intents/receive-intents/`

- Navigation
- Intents
- Receive intents

## Receive intents

- How-to guide
- 4-min readYou can allow other apps to send data to your Dynatrace App. An app can receive an intent with a payload that you can use to perform an action. For example:

- Pin the result of a DQL query on a dashboard

- Set up an alert on a metric from a DQL query result

- Show details of an app (based on its `appId`)

To receive an intent, you need to do the following:

### Declare the intents

An app can handle multiple intents that you declare in your app configuration file inside the `app.intents` property. You define an intent using an object where the key of the object is intentId. It consists of the following properties:

- description: A short statement describing the action. It appears in the Open with... dialog.

- properties: An object where you can define every payload property and its corresponding data type. Every payload property is defined using the key of this object, and the corresponding data type is defined with an object with the following properties:

- required: A boolean defining whether a property is mandatory.

- schema: A JSON Schema object describing the shape of the property.

NoteIf you want your intent declaration to be matched in the Open with... flow, you need to add one required property at least. This prevents overly broad matches.If you only use explicit intents—which target a specific app and `intentId`—you can exclusively declare optional properties to support flexible cross-app navigation with dynamic payloads.
Here is an example of an app configuration with intent declarations:

app.config.json
`tsx
{ "environmentUrl": "", "app": { "id": "", "name": "", "version": "0.0.0", "description": "", "scopes": [], "intents": { "view_host": { "description": "View the host", "properties": { "dt.entity.host": { "required": true, "schema": { "type": "string" } } } }, "view_query": { "description": "View query", "properties": { "dt.query": { "required": true, "schema": { "type": "string" } } } } } }}
`

### Receive intent payload

After you declare the type of intents your app can handle, the next step is to receive an intent in your app. You can achieve this using the `getIntent` method from the `@dynatrace-sdk/navigation` package.

NoteTo use intents, you need to install the `@dynatrace-sdk/navigation` npm package in your project.
Here is an example of using `getIntent` with React's `useEffect`:

`tsx
import React, { useEffect, useState } from 'react';import { Code, Paragraph } from '@dynatrace/strato-components/typography';import { getIntent, IntentPayload } from '@dynatrace-sdk/navigation';export const YourComponent = () => { const [intentPayload, setIntentPayload] = useStateIntentPayload>(); useEffect(() => { const intent = getIntent(); if (intent) { setIntentPayload(intent.getPayload()); } }, []); return ( > {intentPayload && ( Paragraph> Received Intent Payload Code>{JSON.stringify(intentPayload)}/Code>. /Paragraph> )} /> );};
`

Things to know about the `getIntent` method:

- The `getIntent` method returns an object of `Intent` type.

- You can call the `getIntent` method anywhere in your Dynatrace App. For example, in `App.tsx`, a component, a custom hook, react context, and elsewhere.

CautionIf your app has routing configured, you need to create a route `/intent/:intentId` in your app to handle the intent using the `getIntent` method. The AppShell opens this route and passes the intent object synchronously. Your app won't receive the intent if this route doesn't exist.

#### Handle multiple intents

Each type of intent has a unique ID. If your app handles multiple intents, you can target a specific intent using that ID.

Here is an example of handling two different intents using the `getId` method:

`tsx
import { useEffect } from 'react';import { getIntent } from '@dynatrace-sdk/navigation';export const AnotherComponent = () => { useEffect(() => { const intent = getIntent(); if (intent?.getId() === 'share_chart') { // for example: shareChart(intent.context); } if (intent?.getId() === 'view_query') { // for example: viewQueryInTable(intent.context); } }, []); // … jsx and the rest of the code};
`

In this example, if `intentId` is `share_chart`, the call is to a hypothetical method named shareChart. However, if `intentId` is `view_query`, the call is to a hypothetical method named viewQueryInTable. This strategy lets you perform different actions with different intents.

---

## navigation/intents/send-intents

`/develop/guides/navigation/intents/send-intents/`

- Navigation
- Intents
- Send intents

## Send intents

- How-to guide
- 3-min readIntents provide a way to extend your Dynatrace app's functionality. Part of that process is to send intents from your app to the receiving app. You might want to send an intent for several reasons, such as:

- Pin a chart to a dashboard

- View details of an app in the Dynatrace Hub

When you send an intent, the AppShell displays an Open with dialog to let you choose the app that will receive the intent.

This guide shows you how to define and trigger a send intent from your app. Before you start, familiarize yourself with the intents mechanism and its processes.

Time to complete: 10 minutes

### 1. Define the intent

First, you need to define the intent payload. An intent payload is a set of key-value pairs that contains information you want to share.

Define the intent payload using the `IntentPayload` type from `@dynatrace-sdk/navigation` as follows:

`tsx
import { IntentPayload } from '@dynatrace-sdk/navigation';// Intent payload definitionconst intent: IntentPayload = { 'dt.query': 'fetch logs', 'custom.type': { foo: 'bar' },};
`

### 2. Trigger the intent

You can trigger the intent from your app in one of three ways, using the:

- option

- `sendIntent` method

- `getIntentLink` method

#### The option

Use the for straightforward use cases where you want to trigger a declarative intent.

Execute the from `@dynatrace/strato-components/buttons` as follows:

ui/app/App.tsx
`tsx
import React from 'react';import { IntentButton } from '@dynatrace/strato-components/buttons';export const App = () => { return ( IntentButton payload={{ 'dt.query': 'fetch logs' }} options={{ recommendedAppId: 'dynatrace.notebooks', recommendedIntentId: 'view-query', }} > Edit in Notebooks IntentButton> );};
`

#### The `sendIntent` method

Use the `sendIntent` method if you need more control than the provides to trigger an intent from the `@dynatrace-sdk/navigation` programmatically. The `sendIntent` method takes an `intentPayload` and optional `sendIntentOptions` parameter.

Send an intent with the `dt.query` property using the `sendIntent` method as follows:

`tsx
import { sendIntent, IntentPayload } from '@dynatrace-sdk/navigation';const payload: IntentPayload = { 'dt.query': 'fetch logs',};sendIntent(payload);
`

##### Open app without showing the Open with dialog

It's possible to bypass the Open with dialog and open the app directly.

`tsx
import { sendIntent } from '@dynatrace-sdk/navigation';sendIntent( { 'dt.query': 'fetch logs' }, { recommendedAppId: 'dynatrace.notebooks', recommendedIntentId: 'view-query', },);
`

NoteIf you provide a non-existent `recommendedAppId` or `recommendedIntentId`, the AppShell will display the Open with dialog box, allowing you to select a different app.

##### Mark properties as required when matching the intent

When an app sends a complex intent payload, the Open with dialog shows every app capable of handling at least one of the payload properties.
It's possible to narrow the list by providing property names that must be matched as `keyProperties`.

`tsx
import { sendIntent } from '@dynatrace-sdk/navigation';const complexRowData = { 'dt.entity.host': '', 'dt.entity.process_group': '', 'dt.entity.process_group_instance': '', 'span_id': '', 'trace_id': '',};sendIntent(complexRowData, { keyProperties: ['trace_id'],});
`

#### The `getIntentLink` method

Use the `getIntentLink` method to create a static URL link that users can copy, share, and bookmark in their browser. The `getIntentLink` method takes an `intentPayload` and optional `appId` and `intentId` parameters.

Create a static URL link using the `getIntentLink` method from `@dynatrace-sdk/navigation` as shown below. This example shows how an app renders a URL using `getIntentLink`.

ui/app/components/YourComponent.tsx
`tsx
import React from 'react';import { getIntentLink } from '@dynatrace-sdk/navigation';import { Link } from '@dynatrace/strato-components/typography';export const YourComponent = () => { const intentLink = getIntentLink({ 'dt.query': 'fetch logs' }); return ( Link href={intentLink} target="_blank"> Intent Link Link> );};
`

NoteIf you provide a non-existent `appId`, the AppShell will display the Open with dialog box, allowing you to select a different app. Provide an existing `appId` and `intentId` to bypass the Open with dialog and open the app directly.
Now, you have integrated the user flow from your app to other Dynatrace Apps by sending an intent.

### Learn more

If you want to learn more about extending your Dynatrace app using intents, check out the Receive and Debug intent pages.

---

## navigation/page-tokens

`/develop/guides/navigation/page-tokens/`

- Navigation
- Page tokens

## Page tokens

- How-to guide
- 3-min readApp routes that can be accessed from other apps should be registered via page tokens and considered as a public API of the app.
They should stay consistent across app versions and be independent of the internal app routing schema to avoid breaking existing links in other apps.

This is where page tokens come into place. They allow you to provide static, consistent, and externally accessible links to specific routes within your app.

By using page tokens, you can keep your app interfaces consistent independently of your internal route changes.
This can be particularly useful when linking to static content, for example a guide, an article or some documentation.

Page tokens allow you to define static path segments for routes in your Dynatrace App. You can ensure that external links to specific routes won't break if your internal route structure changes by providing page tokens. This guide will teach you how to specify page tokens for your app routes.

### Register page token for a route

Within your app configuration file, you can specify page tokens for your routes.
The `app` property includes an optional property called `pageTokens`. In the following example you can see an example of how such a configuration might look:

app.config.json
`tsx
{ "environmentUrl": "", "app": { "id": "", "name": "", "version": "0.0.0", "description": "", "scopes": [], "pageTokens": { "documentation": "/about", "appchangelog": "/changelog" } }}
`

This allows you to use the `documentation` page token to link to the `/about` route from outside of your app. If you need to change the route name in the future, you only need to change the documentation `pageToken` parameter. The static link that uses the `documentation` page token will still be consistent.

### Link to page token

There are two primary options for creating a link to a page token. You can either use the `AppLink` component or one of two functions from the `@dynatrace-sdk/navigation` package.

#### AppLink component

The `@dynatrace/strato-components` package provides the `AppLink` component to create page token links.
You only have to provide the `appId` and the corresponding `pageToken` as properties to have a link rendered in your UI:

ui/app/Component.tsx
`tsx
import React from 'react';import { AppLink } from '@dynatrace/strato-components/navigation';export const Component = () => { return ( AppLink appId="app.id" pageToken="documentation"> Documentation AppLink> );};
`

#### @dynatrace-sdk/navigation functions

Another option is to use the `@dynatrace-sdk/navigation` package directly. It provides two convenient functions that make use of page token links:

- `openApp()`

- `getAppLink()`

Both of these functions accept an app id (required) and a page token (optional) as parameters.

The `openApp()` function opens a specific page token. You can, for example, use this as an onClickHandler function:

`tsx
Button onClick={() => openApp('app.id', 'documentation')}>Open DocumentationButton>
`

The `getAppLink()` function returns a static link, which you can copy, share, bookmark or open in a new tab:

`tsx
getAppLink('app.id', 'documentation');
`

For the provided example, the function would return the following link:

`tsx
https://abc12345.apps.dynatrace.com/ui/openApp/app.id?pageToken=documentation
`

---

## navigation/url-sharing

`/develop/guides/navigation/url-sharing/`

- Navigation
- URL sharing and navigation

## URL sharing and navigation

- 7-min readBuilding Dynatrace apps requires careful consideration of how users navigate, share, and collaborate around data. Two fundamental web platform features, URLs and the browser back button, play a critical role in creating intuitive user experiences. This guide outlines best practices for implementing URL-based state management and browser history handling in Dynatrace applications.

### Why URLs matter in Dynatrace solutions

URLs are more than just addresses—they're a fundamental part of the user interface. As Scott Hanselman famously stated, "URLs are UI." In Dynatrace contexts, where teams collaborate around incidents, performance issues, and system behavior, shareable URLs become essential collaboration tools.

Consider a typical scenario: A DevOps engineer discovers a performance anomaly in a dashboard filtered to a specific service, time range, and metric. They need to share this exact view with their team. Without proper URL state management, they'd need to write instructions like "Go to the dashboard, select Service X, set the time range to last 4 hours, and filter by error rate." With well-designed URLs, they can simply share a link.

### The core principle: Bidirectional state synchronization

The W3C's guidance on web architecture emphasizes that URLs should represent the state of a resource. For modern web applications, this means establishing bidirectional data flow between your application state and the URL:

- When the URL changes (via navigation, back button, or direct access), the UI state updates accordingly.

- When the UI state changes (via user interaction), the URL updates to reflect the new state.

This synchronization keeps URLs as the single source of truth for shareable application states.

### What should go in the URL?

#### States worth sharing

Include UI states that make sense for users to share or bookmark.

In Dynatrace apps, this typically includes:

- Time ranges: Absolute timestamps or relative timeframes (e.g., "last 15 minutes").

- Entity selections: Specific hosts, services, applications, or processes being monitored.

- Filter criteria: Status filters, tag filters, management zones.

- View configurations: Selected metrics, chart types, grouping options, table configurations.

- Navigation context: Active tab, expanded sections, selected dashboard.

Example URL structure:

`tsx
/dashboards/service-overview? service=payment-api& timeframe=2h& metric=response-time& environment=production& view=chart
`

#### States to exclude

Not everything belongs in the URL. According to best practices for URL design, avoid including:

- Transient UI states: Hover states, tooltip visibility, loading indicators, foldouts, expanded accordions, etc.

- Sensitive information: User credentials, personally identifiable information (PII).

- Session-specific data: Temporary states that are not meaningful outside the current session.

### Browser history API best practices

The browser history API allows you to manage the user's navigation history seamlessly. Use the `history.pushState()` method to add a new entry to the history stack when the URL changes due to user interactions, such as filtering or navigating to a different view.

NoteFor any automatic redirection, use the history API's `replaceState` method instead of `pushState`. It ensures a clean and usable history stack, preventing issues with navigation through history.While this is most commonly relevant for initial redirects (for example, from the app's root location to the default view), it also applies to redirects that occur later in the app's lifecycle.

#### Key recommendations

- Use `pushState` for significant state changes, like switching dashboards or applying filters.

- Use `replaceState` for minor updates, such as adjusting relative timeframes, to avoid cluttering the history stack.

### Back button UX patterns

The back button is one of the most frequently used navigational elements in modern browsers. It is crucial to ensure that the back button behaves as users expect.

In Dynatrace apps, this means pushing new history entries whenever a significant UI change occurs, such as switching between dashboards or applying filters. This ensures that users can navigate back to their previous state without confusion.

### Scroll position management

Scroll position is another critical aspect of navigation UX that directly impacts how users interact with the back button. Modern browsers automatically restore scroll positions when users navigate through history, but this default behavior doesn't always align with user expectations in dynamic web applications.

#### Understanding scroll restoration

The History API provides the `scrollRestoration` property, which allows you to control how browsers handle scroll position when navigating through history. This property accepts two values:

- `auto` (default): The browser automatically restores the scroll position to where the user was when they left the page.

- `manual`: You take control of scroll behavior and must handle scroll position restoration yourself.

#### When to use automatic scroll restoration

For most Dynatrace apps, the default `auto` behavior works well. Use automatic scroll restoration when:

- Users navigate between distinct pages or views (for example, from a dashboard list to a specific dashboard).

- Content loads synchronously and the page structure remains stable.

- Users expect to return to their previous position when using the back button.

Example Dynatrace scenarios:

- Navigating from a list of hosts to a specific host detail page.

- Switching between different sections in Settings.

- Browsing through problem lists or log entries.

#### When to use manual scroll restoration

Set `scrollRestoration` to `manual` when you need custom control over scroll behavior. This is necessary when:

- Your app performs page transitions or animations that conflict with automatic scroll restoration.

- Content loads asynchronously and the page height changes dynamically.

- You're implementing infinite scroll or virtualized lists.

- The same URL can display different content based on application state.

Example Dynatrace scenarios:

- Dashboards with dynamically loaded tiles that affect page height.

- Metric charts that load data asynchronously.

- Entity lists with lazy loading or infinite scroll.

- Views with expandable sections that change the page layout.

#### Implementing manual scroll restoration

When you set scroll restoration to manual, you're responsible for storing and restoring scroll positions. You can store scroll position data in the history state when using `pushState()`:

Best practices for manual scroll restoration:

- Store scroll position with history entries: Capture the current scroll position before navigation and store it using `history.pushState()` or `history.replaceState()`.

- Restore on popstate events: Listen for popstate events and restore the scroll position from the stored state.

- Handle async content: Wait for dynamic content to load before restoring scroll position to avoid incorrect positioning.

- Consider scroll regions: Don't forget about scrollable containers within your page—not just the main document scroll.

#### Scroll position and URL state

Generally, you should not include scroll position in the URL query parameters. Scroll position is ephemeral navigation state, not shareable application state. When someone shares a URL, they want to share the content and filters, not their specific scroll position.

Exception: In rare cases where scroll position represents meaningful content location (such as a specific log entry in a long list), consider using anchor links or dedicated parameters that identify the content item rather than a pixel position.

#### Testing scroll behavior

When implementing scroll management in your Dynatrace app, test these scenarios:

- Navigate forward and back through multiple pages.

- Use the back button after scrolling partway through a long page.

- Navigate back to pages with dynamically loaded content.

- Test on different screen sizes and resolutions.

- Verify behavior with both keyboard and mouse navigation.

### Dedicated share feature

If your application requires complex URL handling, such as adjusting relative timeframes or managing long URLs, consider implementing a dedicated share feature. This feature can save the application state in a more manageable format and provide users with a shortened URL that can be easily shared.

### Conclusion

By implementing these guidelines, Dynatrace apps can offer a more intuitive user experience, enabling seamless navigation and effective collaboration among users. Shareable URLs, proper back button functionality, and scroll position management are essential components of any well-designed web application.

---

## privacy

`/develop/guides/privacy/`

- Privacy

## Privacy by design

- Explanation
- 1-min readPrivacy is paramount in the development of Dynatrace Apps. At Dynatrace, responsible data processing is at the core of our business. Thus, protecting personally identifiable information (PII) is a key priority.

Dynatrace enables its customers to have complete control of their data, and, through configurable privacy features, they can determine what data to share with Dynatrace.

When developing Dynatrace Apps, implement privacy by design and by default to support customers in maximizing the value of Dynatrace while complying with data protection requirements. It is essential to respect the customer’s preferences and take reasonable steps to protect sensitive data collected in the app.

To guide you through the different privacy requirements, you should consider three core questions:

- Does your app process and collect PII?

- Is the PII relevant and necessary for the app's core functionalities?

- Does a retention period apply to the PII ingested in the app?

###

#### Identify PII
Basic concepts of Personally Identifiable InformationExplanation

#### Limit storage time
Requirements to comply with storage limitations for PIIHow-to guide

#### Minimize data
Guidelines to minimize the amount of personally identifiable information processed by a Dynatrace appHow-to guide

---

## privacy/identify-pii

`/develop/guides/privacy/identify-pii/`

- Privacy
- Identify PII

## Identify PII

- Explanation
- 2-min readPersonally Identifiable Information (PII), also called Personal Data or Personal Information, means every piece of information that relates to a natural person (or an individual), referred to as a "data subject" in data protection terms.

The scope of the definition is broad as it includes directly identifying data (for example, first and last name). And indirectly identifying data with several independent data elements (for example, telephone number, license plate, terminal identifier, etc.).

For example, when relating to natural persons, the following data is personal data:

- Surname, first name, pseudonym, date of birth

- photos, sound recordings of voices

- fixed or mobile telephone number, postal address, email address

- IP address, the computer connection identifier, or cookie identifier

- Fingerprint, palm or venous network of the hand, retinal print

- License plate number, social security number, ID number

- Application usage data, comments, etc.

Any operation on PII constitutes processing under data protection law and must, therefore, meet the applicable requirements (for example, accessing, manipulating, storing, and transferring PII are all processing activities that need to comply with data protection law).

You should implement privacy by design and consider if you have a justification for processing PII even if your app never stores it but proxies it or queries it from elsewhere.

### Anonymization and pseudonymization

Anonymizing personal data is an irreversible process that makes identifying individuals within data sets impossible. Anonymous data doesn't contain any PII and, therefore, falls outside the scope of data protection law.

You need to decide whether to anonymize data and the anonymization technique on a case-by-case basis according to different contexts of use. By default, you should never consider a raw dataset anonymous. However, having implemented an appropriate anonymization process, a developer can collaborate with third parties, and you can keep the data indefinitely.

Whereas pseudonymization data relating to an individual can no longer be attributed without more information, for example, to pseudonymize PII, you replace personal identifiers with random numbers or codes in a dataset. Unlike anonymization, pseudonymization can be a reversible process.

Despite reducing risks, differently from anonymized data, pseudonymized data is considered PII and therefore is subject to data protection law!

To better understand the difference between anonymization and pseudonymization, consider these examples:

- Anonymization

- Data Masking (+ data deletion)

- Randomization

- Aggregation (+ identifiers deletion)

- Generalization (+ identifiers deletion)

- Pseudonymization

- Data Masking (+ masked data is kept)

- Encryption

- Hashing (+ table is kept)

- Tokenization

---

## privacy/limit-storage-time

`/develop/guides/privacy/limit-storage-time/`

- Privacy
- Limit storage time

## Limit storage time

- How-to guide
- 1-min readPersonal Identifiable Information (PII) can't be stored for an indefinite period. You need to define the retention period in line with the purposes of the processing. After the data has been used for its given purpose, it should be deleted or anonymous.

### Steps to comply with storage limitation

- Implement retention periods in line with the Dynatrace offering

- Offer configurable settings to select specific retention periods

- Implement a process to comply with an individual request for the erasure of specific PII

To support customers in complying with the principle of storage limitation, Dynatrace automatically deletes data older than the configured retention periods and also provides adaptive data retention to increase or decrease data retention time periodically. As customers rely on their selected retention periods, consider implementing configurable options in the app to ensure that data isn't stored longer than the defined period.

---

## privacy/minimize-data

`/develop/guides/privacy/minimize-data/`

- Privacy
- Minimize data

## Minimize data

- How-to guide
- 1-min readTo comply with the principle of data minimization, you need to ensure that the Personal Identifiable Information (PII) that your app processing is:

- Relevant: you should collect only PII necessary for the specified purposes.

- Adequate: you have enough data to fulfill those purposes properly.

- Limited to what's necessary: you periodically review the stored data and delete anything unnecessary.

Dynatrace enables its customers to comply with data minimization requirements through built-in mechanisms, such as data masking rules. You need to consider whether customers need similar data masking rules in your app and, if relevant, offer settings that allow the customer to disable access to sensitive information.

### Tips on how to minimize data collection in Dynatrace Apps

- If specific PII isn't needed to offer the core functionality of the app, don't collect it

- The app should use the minimum amount of customer data required to carry out a given task

- Offer settings to disable access to specific data types

- Minimize the amount of data collected in the log data

---

## reuse-code

`/develop/guides/reuse-code/`

- Reuse code

## Reuse code within your app

- How-to guide
- 3-min readTypeScript/JavaScript allows you to share code between multiple files using `export` and `import` statements. If a file has a statement with these keywords, it's a JavaScript module. You can share variables, classes, functions, or objects from a JavaScript module.

Your Dynatrace app can use the same techniques to share code between different parts of the app and app functions.

### Export

To use code from another module, first you need to export the code from the original module using the `export` statement. In the example below, you have a module named `moduleA` with some exported members:

moduleA.ts
`tsx
export const fruits = ['apple', 'orange', 'banana', 'pineapple', 'blueberry'];export function login() { // Placeholder function for demonstration purposes}export const player = { id: 1, name: 'John Doe', age: 22,};// Animal class isn't be available outsideclass Animal {}
`

Alternatively, you can export everything in a single statement at the end of the file:

`tsx
export { fruits, login, player };
`

#### Export with alias

If you would like to rename a member while exporting it. You can do so using the `as` keyword:

`tsx
export { fruits, login, player as tennisPlayer };
`

### Import

After you have exported the members, you can import them into the other modules using the import statement. Use the `import` keyword, followed by the members you want to import in curly brackets, and then the location of the module relative to the current file as shown:

`tsx
import { fruits, login, player } from './moduleA';
`

#### Import with alias

In cases where you have a naming conflict because two module shares an export with the same name. Importing them will create a name collision. To solve this, you can rename the import using the `as` keyword:

`tsx
import { fruits } from './moduleA';import { fruits as summerFruits } from './moduleB';
`

#### Import all exported members

To import all the exported members, you can do so without individually naming them like this:

`tsx
import * as MyModule from './moduleA';
`

Then you can access the members using dot notation:

`tsx
console.log(MyModule.fruits); // ['apple', 'orange', 'banana', 'pineapple', 'blueberry'];
`

### Example: Share code between app functions

Let's imagine you have a function `validateStringInput`, checking if the payload sent to your function is a `String` as you would expect.
As this functionality is needed in multiple app functions, it can be re-used in numerous of your app functions.
This example shows two example functions: `getAdress.ts` and `getZipCode.ts`. In both functions, you have to validate that your input is a string.

First, you need to export the `validateStringInput` function within function `getAdress.ts`:

api/getAdress.function.ts
`tsx
export function validateStringInput(payload) { if (typeof payload === 'string' && payload != '') { return; } throw new Error(`Input is not a valid string!`);}export default async function (zipCode: string): Promiseunknown> { validateStringInput(zipCode); const city = fetch('https://api.getmyadress.com/api/zipCode/?zipCode=' + zipCode).then((res) => res.json()); return city;}
`

Now you can import and use that function in your app function `getZipCode.ts` like this:

api/getZipCode.function.ts
`tsx
import { validateStringInput } from './getAdress';export default async function (city: string) { validateStringInput(city); const zipCode = fetch('https://api.getmyadress.com/api/city/?city=' + city).then( (res) => res.json() as Promiseunknown>, ); return zipCode;}
`

By importing functions like shown above, you can easily re-use functionality between your app functions.

---

## security

`/develop/guides/security/`

- Security

## Security

- Explanation
- 1-min readWhen developing Dynatrace Apps you should consider all kind of security aspects from the very beginning. This section provides you with guides to make sure your app is not affected by security vulnerabilites, it is only using a minimal set of permissions and secrets are handled correctly.

###

#### Add permission scopes to use Dynatrace APIs
Add permission scopes to your Dynatrace App configuration.How-to guide

#### Configure CSP rules
Information about Content Security Policy (CSP) rules within Dynatrace AppsReference

#### Manage secrets
Best practices to manage secrets in Dynatrace Apps for accessing external servicesHow-to guide

#### Manage dependencies for third-party libraries
Best practices for using third-party librariesExplanation

#### Query user permissions
Query user permissions in your Dynatrace App.How-to guide

---

## security/add-permission-scopes-to-use-dynatrace-apis

`/develop/guides/security/add-permission-scopes-to-use-dynatrace-apis/`

- Security
- Add permission scopes

## Add permission scopes to use Dynatrace APIs

- How-to guide
- 2-min readRequests to the Dynatrace API need authorization via OAuth. When you consume these APIs in your app, directly or via the provided SDK packages, the platform takes care of the authorization for you. During the usage of an app, the user's permissions are used for authorization. During development, they're the developer's permissions, respectively.

The fact that the user's permissions are used for authorization could lead to potential security problems, as an app could misuse the user's permissions and perform malicious activity. Therefore, the Dynatrace platform requires an app to provide all the needed permissions within the app configuration file. When executing an app, app permissions are intersected with user permissions to adhere to the principle of least privilege.

Making this list of required permissions transparent to Dynatrace users and administrators allows them to decide if a particular app is safe to run in their environment. Having specific permissions defined in the app configuration file doesn't necessarily mean that the app uses it.

### Find the required scopes

You can find all scopes for every exposed function of Dynatrace SDK packages on the corresponding reference page. Additionally, you can find a complete list of available scopes on the IAM service reference page.

### Add the required scopes

Once you have figured out the needed scopes, add them to your app configuration file:

app.config.json
`tsx
{ "environmentUrl": "", "app": { "id": "", "name": "", "version": "0.0.0", "description": "", "scopes": [ { "name": "storage:events:read", "comment": "allows to query events from Grail" }, { "name": "state:app-states:read", "comment": "allows to read app state" } ] }}
`

CautionAfter changing the scopes in the app configuration file, you must restart the local development server to apply the changes.

---

## security/configure-csp-rules

`/develop/guides/security/configure-csp-rules/`

- Security
- Configure CSP rules

## Configure CSP rules

- 2-min readContent Security Policy (CSP) is a mechanism by browsers and web servers that restricts resources that are allowed to be loaded. This limits an app's capabilities within the browser and mitigates certain types of vulnerabilities. For example, a Content Security Policy can ensure that data can't be leaked to third-party services as it prevents external network connections. For more information on Content Security Policies, visit MDN's article on Content Security Policy.

By default, the Dynatrace platform only defines a small set of CSP rules. You can configure your app's custom CSP rules if you need to access more sources from your app—such as custom fonts and custom UI widgets from non-platform domains, etc. Requesting these exceptions via the app configuration file ensures transparency and helps users understand the consequences of installing apps in their environment.

### Configurable CSP rule exceptions

Because of security restrictions, you can't configure every available CSP rule for your app. You can extend the following directives:

 |
 | Name | Purpose | Allowed values
 | `font-src` | Applying custom fonts to the app. |
- `https://my.domain.com` (only https is allowed, no trailing slash)
- `'data:'`
- `'sha*-*'`
 | `img-src` | Loading custom images from outside of the platform |
- `https://my.domain.com` (only https is allowed, no trailing slash)
- `'data:'`
- `'blob:'`
- `'sha*-*'`
 | `media-src` | Loading media files (videos, audio) |
- `https://my.domain.com` (only https is allowed, no trailing slash)
- `'sha*-*'`
 | `script-src` | Loading custom scripts from outside of the platform |
- `https://my.domain.com` (only https is allowed, no trailing slash)
- `'sha*-*'`
 | `style-src` | Loading custom styles from outside of the platform |
- `https://my.domain.com` (only https is allowed, no trailing slash)
- `'unsafe-inline'`
- `'sha*-*'`

### Where to configure custom CSP rules

You can configure custom rules within the app configuration file. Within the `app` property, you can define your CSP rule exceptions.
In the following example, we add two CSP rules to allow images and fonts to load from domains outside the platform.

app.config.json
`tsx
{ "environmentUrl": "", "app": { "id": "", "name": "", "version": "0.0.0", "description": "", "scopes": [], "csp": { "img-src": [ { "value": "https://awesome-cdn.net", "comment": "allows to load images from awesome CDN" } ], "font-src": [ { "value": "https://font-paradise.com", "comment": "allows to load fonts from font paradise" } ] } }}
`

### Limitations

You can't configure the connect-src directive for your app. That means you can't fetch resources from external domains. To do so, create an app function and fetch external data. To learn more, read the How to create an app function guide.

NoteThe unsafe-eval directive is forbidden for all CSP rule exceptions.

---

## security/manage-secrets

`/develop/guides/security/manage-secrets/`

- Security
- Manage secrets

## Manage secrets

- How-to guide
- 3-min read

### How to handle secrets within the Dynatrace platform

Whenever Dynatrace Apps or functions need to access services outside the Dynatrace platform, secrets are likely required to authenticate these service interactions. Many services require API tokens, OAuth clients, or secrets within webhook URLs to authenticate their users.

Your app is never to contain these secrets, and there are several reasons for that:

- People with access to the app bundle or a function, for example, in Notebooks, can see the secret in clear text and misuse them.

- Your app bundles that have secrets can't be easily updated. You need to update the whole app to exchange a secret.

To help users keep secrets secure and easy to handle, Dynatrace offers the Credential Vault service and a corresponding SDK, which stores secrets, credentials, certificates, etc.

With the help of the SDK, you can easily retrieve your credentials in your app. There are four types of credentials, each with a corresponding interface in the SDK:

 |
 | Secret type | Interface
 | Certificate | CredentialsDetailsCertificateResponseElement
 | Public certificate | CredentialsDetailsCertificateResponseElement
 | Token | CredentialsDetailsTokenResponseElement
 | Username and password | CredentialsDetailsUsernamePasswordResponseElement
When retrieving credentials in your app, you need to use the corresponding interface according to your secret type, like this:

`tsx
import { credentialVaultClient, CredentialsDetailsTokenResponseElement,} from '@dynatrace-sdk/client-classic-environment-v2';const tokenCredentials: CredentialsDetailsTokenResponseElement = await credentialVaultClient.getCredentialsDetails({ id: 'CREDENTIALS_VAULT-xxxxxxxxxxxxxxxx', });if (tokenCredentials.token) { // use token}
`

TipThis operation requires the scope `environment-api:credentials:read`. Read more about scopes in this guide.
TipEnsure to use the `AppEngine` scope for your credentials.
NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.

### Best practices to handle secrets

#### Storage of secrets in the credential vault

Storing secrets outside places specifically designed for that purpose is discouraged. For the Dynatrace platform, use the Credential Vault and don't hard-code credentials within apps, Dashboards, Notebooks, or similar.

#### Apply the principle of least privilege

Each user, token, and OAuth client should only be assigned the minimum level of access required to perform their duties. As a result, your secrets' permissions will only be accessible when used in conjunction with the corresponding task they're to perform. Following this principle, you can reduce the potential impact if secrets leak.

#### Don't reuse secrets

It would be best if you don't reuse secrets. We recommended creating a set of secrets for a single action—for example, in a workflow—where you can change secrets easily without dependencies on multiple services that might break by revoking a single certificate.

#### Rotate secrets

Try to rotate any secrets periodically. This will ensure that people who had access to secrets in the past can't access the system after they change roles or leave the company.

#### Review and share secrets

Try to review secrets and their sharing status periodically. Is a secret still in use, or can it be removed? Secrets that aren't stored anywhere can't be compromised. Ask yourself if all persons who can access a secret still require access. From a security point of view, less is more when it comes to sharing secrets.

---

## security/manage-third-party-library-dependencies

`/develop/guides/security/manage-third-party-library-dependencies/`

- Security
- Manage dependencies

## Manage dependencies for third-party libraries

- Explanation
- 2-min read

### Third-party dependency management

Developers usually rely on third-party software libraries and frameworks to save time and not have to reinvent the wheel. Typically, most of the running code is third-party, not your app code. The upside of velocity comes with the downside of potential security pitfalls. Libraries can (and often do) contain known security problems, or, in the worst case, a library can be deliberately compromised by a malicious actor.

Vulnerable or malicious code in a JavaScript library can fully control the user session the app is running in—that's why you need to keep an eye on the security of third-party dependencies.

#### Best practices for third-party dependency security

A few practices substantially lower the likelihood of something going wrong with your dependencies in terms of security.

- Keep the list of dependencies small: Even though there might be a library for the function you're about to implement, you should be sure you need it. Every single dependency you pull in increases the attack surface on your app. A few negative examples are the use of libraries like `leftpad`, `trim`, and `is-even`, even though these are simple functions.

- Choose your libraries wisely: If the library has only one contributor, and the last commit happened years ago, likely, it won't be well maintained in the future. So chances are high that security bugs don't get fixed and that the library is prone to repository hijacking. Look for libraries with many contributors, frequent updates, security documentation, and a solid security track record.

- Update regularly, even in the absence of known vulnerabilities: The longer you wait for a major version upgrade of your library, the harder it will get. Make sure to pay down such technical debts regularly by frequent library updates, even though there is no urgent need. It will decrease the likelihood of severe vulnerabilities in your dependencies.

- Regularly scan your dependencies for known vulnerabilities: Even if you update often, new known vulnerabilities might still pop up from time to time in the versions you use. Regularly scan your libraries for any known security problems and act accordingly.

---

## security/query-user-permissions

`/develop/guides/security/query-user-permissions/`

- Security
- Query user permissions

## Query user permissions

- How-to guide
- 2-min readEvery app configuration file must declare the IAM scopes needed to access the used Dynatrace APIs. For more information, visit Add permission scopes to use Dynatrace APIs. In addition, a user must be granted the respective scopes by an IAM policy so that the app can execute any Dynatrace API request on a user's behalf. You can find out which scope a function of a Dyntrace SDK needs on the reference page.

If a user lacks the IAM scope necessary for accessing a Dynatrace SDK function the app calls, that request will fail with a `403` error code. To avoid this, you can ensure that the app determines if a user has the necessary IAM scopes before it calls an SDK function. The client-platform-management-service SDK provides the `effectivePermissionsClient` for that purpose.

### Install the SDK

First, in your app's folder, you need to install the required SDK via the terminal as follows:

`tsx
npm i @dynatrace-sdk/client-platform-management-service
`

### Resolve a user's permissions

You can issue one or many permission requests with a call to `resolveEffectivePermissions` provided by the package's effectivePermissionsClient.

Optionally, you can provide a `context` object where you give the values for any conditions for the respective permission. The response object has a corresponding array of objects that have a `granted` field with the following possible values:

- `true`: The user generally has permission independent of any conditions.

- `condition`: The user has permission, only given certain conditions, and the provided `context` hasn't been enough to resolve them.

- `false`: The user doesn't have the permission.

TipBased on the result, an app could decide to show or hide a UI element like a button, which would trigger an SDK call, for example, hiding a "Create" button if it's known that the user doesn't have permission.
As an example, a user has the following permissions using a group membership where the following IAM policy is assigned:

`tsx
ALLOW storage:logs:read; ALLOW storage:metrics:read where storage:metric.key startsWith "builtin:synthetic";
tsx
import { effectivePermissionsClient } from '@dynatrace-sdk/client-platform-management-service';const result = await effectivePermissionsClient.resolveEffectivePermissions({ body: { permissions: [ { permission: 'storage:logs:read', context: [ { key: 'storage:k8s.cluster.name', value: 'mycluster', }, ], }, { permission: 'app-engine:edge-connects:write', }, { permission: 'storage:metrics:read', }, { permission: 'storage:metrics:read', context: [ { key: 'storage:metric.key', value: 'builtin:synthetic.http.availability.location.total', }, ], }, ], },});// result[0].granted === "true"// result[1].granted === "false"// result[2].granted === "condition"// result[3].granted === "true"
`

The example shows that the first result returned "true" because the policy even allows `storage:logs:read` without any conditions.
The second result is "false" because the user's policy doesn't allow `app-engine:edge-connects:write`. The third is "condition" because the user only has `storage:metrics:read` under conditions but provides no context. The fourth example provides explicitly that condition so that a definite "true" can be returned.

TipYou can query app settings permissions using the `client-app-settings-v2` SDK or the `useEffectivePermissionsV2` React hook.

---

## support-dark-light-themes

`/develop/guides/support-dark-light-themes/`

- Support dark and light themes

## Support dark and light themes

- How-to guide
- 1-min readDynatrace platform allows switching between light and dark themes. Strato components support it out of the box. If you create custom components or use custom resources, you can add light and dark theme support for them.

### Custom component

You can use Strato design tokens to support theming when you create custom components. Instead of writing hard-coded CSS values like colors, or radius, you can import design tokens from `@dynatrace/strato-design-tokens` and use them instead of hard-coded values. It will ensure that when a user switches the theme, colors will adapt accordingly. Look at a custom card component and see the styling of the `div` element.

ui/app/Card.tsx
`tsx
import React from 'react';import Colors from '@dynatrace/strato-design-tokens/colors';export const Card = ({ href, name }: { href: string; name: string }) => { return ( div style={{ background: Colors.Background.Surface.Default, }} > a href={href}>{name}a> div> );};
`

### Custom resource

You use the `useCurrentTheme` hook from the `@dynatrace/strato-components` library to a custom behavior based on the user's theme. This hook returns a `string` value that is `light` or `dark` depending on the selected theme. The following example shows how to show different images based on the user's theme:

ui/app/App.tsx
`tsx
import React from 'react';import { useCurrentTheme } from '@dynatrace/strato-components/core';export const App = () => { const theme = useCurrentTheme(); return ( > { theme === 'light' ? ( img src={'./assets/background.png'}>img> ) : ( img src={'./assets/background_dark.png'}>img> ) } > );};
`

---

## visualize-data-in-apps/create-logs-viewer

`/develop/guides/visualize-data-in-apps/create-logs-viewer/`

- Visualize data in apps
- Create logs viewer

## Create logs viewer

- How-to guide
- 4-min readIn this guide, you'll learn how to create simple visualizations to gather insights from your log data.

### The LogStatusDistribution component

In the `LogStatusDistribution` component, we'll visualize the log status distribution over time in a bar chart. We'll use DQL to fetch the logs data via the `useDql` hook and the `TimeseriesChart` component for the visualization, with a handy predefined log status color palette.

The DQL query is straightforward. Using the `makeTimeseries` command, we can convert the raw log records to time series. We need to also convert the DQL result to the appropriate type for the `TimeseriesChart` using the `convertToTimeseries` function. As we know, DQL doesn't guarantee any specific order in the results, so if we want a consistent and semantically valid visualization, we need to sort the time series data according to the status severity.

ui/app/components/LogStatusDistribution.tsx
`tsx
import React from 'react';import { TypedQueryResult, useDql } from '@dynatrace-sdk/react-hooks';import { Flex } from '@dynatrace/strato-components/layouts';import { ProgressCircle } from '@dynatrace/strato-components/content';import { Heading } from '@dynatrace/strato-components/typography';import { convertToTimeseries, TimeseriesChart, type TimeseriesWithDimensions,} from '@dynatrace/strato-components/charts';import { Surface } from '@dynatrace/strato-components/layouts';const LOG_STATUS_QUERY = `fetch logs| makeTimeseries count(), by:{status}, interval:5m`;const getSeriesName = (series: TimeseriesWithDimensions) => { return Array.isArray(series.name) ? series.name[0] : series.name;};const buildTimeseries = (result: TypedQueryResult) => { const timeseries = convertToTimeseries(result.records, result.types, undefined, result.metadata); const order = ['ERROR', 'WARN', 'INFO', 'NONE']; timeseries.sort((a, b) => order.indexOf(getSeriesName(a)) - order.indexOf(getSeriesName(b))); return timeseries;};export const LogStatusDistribution = () => { const logSeries = useDql({ query: LOG_STATUS_QUERY, }); return ( Surface> {logSeries.isLoading && ProgressCircle />} {logSeries.data && ( Flex flexDirection="column" gap={24}> Heading level={3}>Log record distributionHeading> TimeseriesChart colorPalette="log-status" data={buildTimeseries(logSeries.data)} variant="bar" /> Flex> )} Surface> );};
`

TipThis operation requires the following scopes:
- `storage:buckets:read`
- `storage:logs:read`Read more about scopes in this guide.

### The LogRecords component

The `LogRecords` component consists of a table with the latest logs generated in our environment. Similar to how we did it in the `LogStatusDistribution` component, we'll use DQL and the `useDql` hook, but we'll use the `DataTable` component for the visualization.

The DQL part is relatively simple. We use the `fields` command to retrieve only those values that interest us. Then we `sort` them by timestamp. The `DataTable` component understands the DQL response format in this case, so no conversion is needed.

The `DataTable` component is highly customizable. For our use case, we'll configure different colors for the log status using thresholds and color tokens to give instant visual feedback and communicate the severity. We'll also add a toolbar with useful actions, the ability to sort the table, and pagination.

ui/app/components/LogRecords.tsx
`tsx
import React from 'react';import { useDql } from '@dynatrace-sdk/react-hooks';import { ResultRecord } from '@dynatrace-sdk/client-query';import { ProgressCircle } from '@dynatrace/strato-components/content';import { Heading } from '@dynatrace/strato-components/typography';import { DataTable, DataTableColumnDef } from '@dynatrace/strato-components/tables';import { Surface } from '@dynatrace/strato-components/layouts';import Colors from '@dynatrace/strato-design-tokens/colors';const LOG_RECORDS_QUERY = `fetch logs| fields timestamp, status, content| sort timestamp desc`;const columns: DataTableColumnDefResultRecord>[] = [ { header: 'Timestamp', id: 'timestamp', accessor: 'timestamp', width: 'content', columnType: 'date', }, { header: 'Status', id: 'status', accessor: 'status', width: 'content', thresholds: [ { value: 'INFO', comparator: 'equal-to', color: Colors.Charts.Logstatus.Info.Default, }, { value: 'WARN', comparator: 'equal-to', color: Colors.Charts.Logstatus.Warning.Default, }, { value: 'ERROR', comparator: 'equal-to', color: Colors.Charts.Logstatus.Error.Default, }, ], }, { header: 'Content', id: 'content', accessor: 'content', },];export const LogRecords = () => { const logRecords = useDql({ query: LOG_RECORDS_QUERY, }); return ( Surface> {logRecords.isLoading && ProgressCircle />} {logRecords.data && ( > Heading level={3}>Most recent {logRecords.data.records.length} log recordsHeading> DataTable sortable defaultSortBy={[{ id: 'timestamp', desc: true }]} data={logRecords.data.records} columns={columns} lineWrap fullWidth > DataTable.Toolbar> DataTable.DownloadData /> DataTable.LineWrap /> DataTable.Toolbar> DataTable.Pagination defaultPageSize={20} /> DataTable> > )} Surface> );};
`

### Putting it together

The last piece of the puzzle is using these components somewhere. We can simply instantiate them in the `App` component, and we're done.

ui/app/App.tsx
`tsx
import React from 'react';import { Heading } from '@dynatrace/strato-components/typography';import { Flex } from '@dynatrace/strato-components/layouts';import { Page } from '@dynatrace/strato-components/layouts';import { AppHeader } from '@dynatrace/strato-components/layouts';import { LogStatusDistribution } from './components/LogStatusDistribution';import { LogRecords } from './components/LogRecords';export const App = () => { return ( Page> Page.Header> AppHeader /> Page.Header> Page.Main> Flex padding={16} flexDirection="column"> Heading level={2}>Logs ViewerHeading> LogStatusDistribution /> LogRecords /> Flex> Page.Main> Page> );};
`

### Summary

Just like that, we've created a basic Logs Viewer app in no time. We hope you found this guide helpful and got the inspiration to build more Dynatrace Apps.

---

## visualize-data-in-apps/prepare-histogram-data

`/develop/guides/visualize-data-in-apps/prepare-histogram-data/`

- Visualize data in apps
- Prepare histogram data

## Prepare histogram data

- How-to guide
- 5-min readHave you wondered how to prepare data so you can use it in a HistogramChart component? If you're unsure how to query the correct type of data and transform it correctly, this guide will help you.

### Get the data

A histogram chart visualizes the distribution in a numerical data set. For this guide, you'll query data from Grail on Discover Dynatrace using `useDql` react hook and use business events with credit card data.

You'll use the range function to help structure the query data. The function takes in some numerical data and an interval and returns a `start` and an `end` value for each range, as follows:

ui/app/components/HistogramPage.tsx
`tsx
import React from 'react';import { useDql } from '@dynatrace-sdk/react-hooks';export const HistogramPage = () => { const queryResult = useDql({ query: `fetch bizevents | filter isNotNull(amount) and isNotNull(cardType) | summarize count = count(), by:{cardType, range = range(amount, 100)}`, });};
`

TipThis operation requires the scope `storage:bizevents:read`. Read more about scopes in this guide.
Now that you've got the data, the next step is to convert the data to pass it to the component.

### Convert the queried data

The HistogramChart component expects `HistogramSeries[]` as data prop. A `HistogramSeries` object contains `HistogramBin[]` and name property. The `HistogramBin` object consists of `value`, `start`, and `end`. The `start` and `end` properties correspond with the start and end values from the query result. In the code below, you extract these values from the query result and construct a `HistogramSeries[]` that you can pass to the component, as follows:

ui/app/components/HistogramPage.tsx
`tsx
import React from 'react';import { useDql } from '@dynatrace-sdk/react-hooks';import { QueryResult } from '@dynatrace-sdk/client-query';import { HistogramSeries } from '@dynatrace/strato-components/charts';const convertQueryResult = (data: QueryResult): HistogramSeries[] => { const result = new Mapstring, HistogramSeries>(); for (const record of data.records) { if (!record) continue; const creditCard = record['cardType'] as string; const amount = Number(record['count']); const range = record['range']; if (!range) continue; const start = Number(range['start']); const end = Number(range['end']); let series = result.get(creditCard); if (!series) { series = { name: creditCard, bins: [] }; result.set(creditCard, series); } series.bins.push({ from: start, to: end, value: amount }); } return Array.from(result.values());};export const HistogramPage = () => { const queryResult = useDql({ query: `fetch bizevents | filter isNotNull(amount) and isNotNull(cardType) | summarize count = count(), by:{cardType, range = range(amount, 100)}`, });};
`

### Display the data in the component

Now that you've queried and converted the data, the next step is to make it visible in the UI. As shown in the code below, you create a new component for our chart and import the necessary components. Then, you pass the function with the data as its argument to the HistogramChart component, as follows:

ui/app/components/HistogramPage.tsx
`tsx
import React from 'react';import { TypedQueryResult, useDql } from '@dynatrace-sdk/react-hooks';import { Heading } from '@dynatrace/strato-components/typography';import { ProgressCircle } from '@dynatrace/strato-components/content';import { HistogramChart, HistogramSeries } from '@dynatrace/strato-components/charts';import { Surface } from '@dynatrace/strato-components/layouts';import { formatCurrency } from '@dynatrace-sdk/units';const convertQueryResult = (data: TypedQueryResult): HistogramSeries[] => { const result = new Mapstring, HistogramSeries>(); for (const record of data.records) { if (!record) continue; const creditCard = record['cardType'] as string; const amount = Number(record['count']); const range = record['range']; if (!range) continue; const start = Number(range['start']); const end = Number(range['end']); let series = result.get(creditCard); if (!series) { series = { name: creditCard, bins: [] }; result.set(creditCard, series); } series.bins.push({ from: start, to: end, value: amount }); } return Array.from(result.values());};export const HistogramPage = () => { const queryResult = useDql({ query: `fetch bizevents | filter isNotNull(amount) and isNotNull(cardType) | summarize count = count(), by:{cardType, range = range(amount, 100)}`, }); return ( Surface> Heading level={2}>Distribution of paymentsHeading> {queryResult.isLoading && ProgressCircle />} {queryResult.data && ( HistogramChart data={convertQueryResult(queryResult.data)}> HistogramChart.XAxis formatter={(value) => formatCurrency(value, 'USD')} /> HistogramChart.YAxis label="Number of payments" /> HistogramChart> )} Surface> );};
`

### Summary

In this guide, you queried numerical data from Grail and then transformed it into a form that the `HistogramChart` component accepts. Finally, you displayed the data in a histogram chart.

Here's the complete code with all the pieces put together:

Full code exampleui/app/components/HistogramPage.tsx
`tsx
import React from 'react';import { TypedQueryResult, useDql } from '@dynatrace-sdk/react-hooks';import { Heading } from '@dynatrace/strato-components/typography';import { ProgressCircle } from '@dynatrace/strato-components/content';import { HistogramChart, HistogramSeries } from '@dynatrace/strato-components/charts';import { Surface } from '@dynatrace/strato-components/layouts';import { formatCurrency } from '@dynatrace-sdk/units';const convertQueryResult = (data: TypedQueryResult): HistogramSeries[] => { const result = new Mapstring, HistogramSeries>(); for (const record of data.records) { if (!record) continue; const creditCard = record['cardType'] as string; const amount = Number(record['count']); const range = record['range']; if (!range) continue; const start = Number(range['start']); const end = Number(range['end']); let series = result.get(creditCard); if (!series) { series = { name: creditCard, bins: [] }; result.set(creditCard, series); } series.bins.push({ from: start, to: end, value: amount }); } return Array.from(result.values());};export const HistogramPage = () => { const queryResult = useDql({ query: `fetch bizevents | filter isNotNull(amount) and isNotNull(cardType) | summarize count = count(), by:{cardType, range = range(amount, 100)}`, }); return ( Surface> Heading level={2}>Distribution of paymentsHeading> {queryResult.isLoading && ProgressCircle />} {queryResult.data && ( HistogramChart data={convertQueryResult(queryResult.data)}> HistogramChart.XAxis formatter={(value) => formatCurrency(value, 'USD')} /> HistogramChart.YAxis label="Number of payments" /> HistogramChart> )} Surface> );};
`

---

## visualize-data-in-apps/query-and-visualize-grail-data

`/develop/guides/visualize-data-in-apps/query-and-visualize-grail-data/`

- Visualize data in apps
- Query and visualize Grail data

## Query and visualize Grail data

- How-to guide
- 2-min readThe Strato Design System offers multiple out-of-the-box components to visualize time-series data. This guide walks you through the steps to query data via Dynatrace Query Language (DQL) and display it in a chart. If you're interested, you can skip ahead and check out the code example at the end of this page.

TipRead more about DQL

#### 1. Import DQL query hook

Import the `useDql` hook from the `@dynatrace-sdk/react-hooks` package in your React component.

`tsx
import { useDql } from '@dynatrace-sdk/react-hooks';
`

TipAlternatively, you can use the `queryExecutionClient` from the `@dynatrace-sdk/client-query` package. To learn more, visit Storage – Query Service.

#### 2. Define and execute your query

Define the query you want to execute in your component body. In this example, you'll query logs and chart the count of records over time:

`tsx
import { useDql } from '@dynatrace-sdk/react-hooks';export const App = () => { const query = 'fetch logs | makeTimeseries count()'; const result = useDql({ query, });};
`

#### 3. Add imports to visualize result

Visualize the result using the `convertToTimeseries` function and the `TimeseriesChart` component. First, add the following imports:

`tsx
import { convertToTimeseries, TimeseriesChart } from '@dynatrace/strato-components/charts';
`

#### 4. Visualize result

The data structure of the DQL result is incompatible with the charting components out of the box. That's why Strato provides the `convertToTimeseries` function, which makes the result compatible with the `TimeseriesChart` component. Add the following snippet in the return statement to visualize the data. Make sure the chart renders only if the result variable is defined.

`tsx
{ result?.data && TimeseriesChart variant="bar" data={convertToTimeseries(result.data.records, result.data.types)} />;}
`

The `convertToTimeseries` function takes two parameters: the records from the DQL result and the field types. Once converted into a time series, you can use the result to render the `TimeseriesChart`.

#### Full code example

ui/app/App.tsx
`tsx
import React from 'react';import { useDql } from '@dynatrace-sdk/react-hooks';import { convertToTimeseries, TimeseriesChart } from '@dynatrace/strato-components/charts';export const App = () => { const query = 'fetch logs | makeTimeseries count()'; const result = useDql({ query, }); return ( result?.data && TimeseriesChart variant="bar" data={convertToTimeseries(result.data.records, result.data.types)} /> );};
`

TipThis operation requires the following scopes:
- `storage:buckets:read`
- `storage:logs:read`Read more about scopes in this guide.

### Related topics

- Learn React

- Learn TypeScript

---

## visualize-data-in-apps/visualize-events

`/develop/guides/visualize-data-in-apps/visualize-events/`

- Visualize data in apps
- Visualize events

## Visualize events

- How-to guide
- 3-min readIn this guide, you'll learn how to visualize multiple metrics and add annotations to the chart based on host events.

### Annotations component

In the `Annotations` component, we'll visualize the CPU and memory used by a specific host. On top of that, we'll add chart annotations with events from the same host. We'll use DQL to fetch the CPU, memory, and events data via the `useDql` hook. Finally, we'll use the `TimeseriesChart` component for the visualization.

The DQL queries for CPU and memory usage use the DQL `timeseries` command. After we have the results, we need to convert them to the appropriate type for the `TimeseriesChart` using the `convertToTimeseries` function. Additionally, we'll merge both converted outputs to have one time series for each metric.

For the events, the DQL query uses the record type `events` and filters by `event.kind`, so we only get what interests us. Similarly to the earlier queries, we need to convert the results to the appropriate type for the `TimeseriesChart.Annotations` component.

Note"Davis" is the former brand name for Dynatrace AI, now called "Dynatrace Intelligence." Legacy strings and files may still use "Davis" and these references remain valid.
ui/app/components/Annotations.tsx
`tsx
import React from 'react';import { Flex } from '@dynatrace/strato-components/layouts';import { ProgressCircle } from '@dynatrace/strato-components/content';import { convertToTimeseries, TimeseriesAnnotations, TimeseriesAnnotationsMarkerProps, TimeseriesChart,} from '@dynatrace/strato-components/charts';import { Surface } from '@dynatrace/strato-components/layouts';import Colors from '@dynatrace/strato-design-tokens/colors';import { ResultRecord } from '@dynatrace-sdk/client-query';import { TypedQueryResult, useDql } from '@dynatrace-sdk/react-hooks';type EventAnnotation = TimeseriesAnnotationsMarkerProps & { eventId: string; color: string;};const hostId = 'HOST-ED51E6E3ECA7BA67';const from = 'now() - 3d';const EVENTS_QUERY = `fetch events, from: ${from}| filter event.kind == "DAVIS_EVENT"| filter dt.entity.host == "${hostId}"| sort timestamp desc| summarize { event.name = takeFirst(event.name), event.description = takeFirst(event.description), event.start = takeFirst(event.start), event.end = takeFirst(event.end), event.status = takeFirst(event.status) }, by:{event.id}`;const HOST_CPU_QUERY = `timeseries from: ${from}, \`CPU Usage\` = avg(dt.host.cpu.usage), filter:dt.entity.host == "${hostId}"`;const HOST_RAM_QUERY = `timeseries from: ${from}, \`RAM Usage \` = avg(dt.host.memory.usage), filter:dt.entity.host == "${hostId}"`;const buildAnnotations = (data: TypedQueryResult): EventAnnotation[] => data.records .filter((record) => record !== null) .map((event: ResultRecord) => { const rawStart = event['event.start'] as string; const rawEnd = event['event.end'] as string | undefined; const start = new Date(rawStart); const end = rawEnd ? new Date(rawEnd) : start; const color = event['event.status'] === 'ACTIVE' ? Colors.Charts.Loglevel.Warning.Default : Colors.Charts.Loglevel.Debug.Default; return { start, end, color, title: event['event.name'] as string, description: event['event.description'] as string, eventId: event['event.id'] as string, }; });const buildTimeseries = (...queryResults: (TypedQueryResult | undefined)[]) => queryResults.flatMap((res) => (res ? convertToTimeseries(res.records, res.types, undefined, res.metadata) : []));export const Annotations = () => { const hostCpuSeries = useDql({ query: HOST_CPU_QUERY, enrich: 'metric-metadata', }); const hostRamSeries = useDql({ query: HOST_RAM_QUERY, enrich: 'metric-metadata', }); const events = useDql({ query: EVENTS_QUERY }); const isLoading = hostCpuSeries.isLoading || hostRamSeries.isLoading || events.isLoading; return ( Flex flexDirection="column" padding={32}> Surface> {isLoading && ProgressCircle />} {hostCpuSeries.data && hostRamSeries.data && ( TimeseriesChart data={buildTimeseries(hostCpuSeries.data, hostRamSeries.data)}> {events.data && events.data.records.length > 0 && ( TimeseriesChart.Annotations> TimeseriesAnnotations.Track> {buildAnnotations(events.data).map((event) => ( TimeseriesAnnotations.Marker key={event.eventId} {...event} /> ))} TimeseriesAnnotations.Track> TimeseriesChart.Annotations> )} TimeseriesChart> )} Surface> Flex> );};
`

TipThis operation requires the following scopes:
- `storage:buckets:read`
- `storage:events:read`
- `storage:metrics:read`Read more about scopes in this guide.

### Summary

With these few lines of code, we've created a useful visualization in very little time. We hope you found this guide helpful and got the inspiration to build more Dynatrace Apps.

---

## workflows

`/develop/guides/workflows/`

- Workflows

## Workflows

- Explanation
- 3-min readWorkflows are a powerful tool that lets you automatically act on monitoring data. Create workflows that generate scheduled reports, notify you about detected issues, or even mitigate them immediately.

This section provides you with guides on how you can leverage Workflows when developing custom apps.

TipTo learn more about how to use Workflows, visit Dynatrace Documentation.

### Custom action

A workflow consists of a directed acyclic graph of tasks that defines their invocation sequence. Each task invokes an action with given inputs and might return a result. Dynatrace provides a set of built-in actions, such as JavaScript or HTTP request, and the possibility to create custom actions to extend the platform.

An action consists of the following:

- A widget that allows users to define the input as a static value or expression, called widgets. The task input the user configures via the widget is stored in the workflow.

- A Dynatrace app function invoked with the task input by the AutomationEngine at runtime. The AutomationEngine resolves expressions before it invokes the action.

- An action typically connects to a third party system. Information related to this connection (URL, credentials, etc.) is a specific type of input that defines its schema and can be managed separately. The user can pick it up in the widget and resolve it in the action app function so the connection can be established.

#### Action widget

The widget is a react app. The UI part of the action allows the user to configure and parameterize a task within a workflow. For example, the built-in `HTTP request` action lets users specify parameters like HTTP method, URL address, payload, and headers. You can build this input form to suit your action as a developer.

Users can either provide static values or use expressions to reference the results of the earlier steps as task inputs. Find more information about expressions in the user documentation expression reference.
To properly support the user in configuring inputs, there are specific Automation action UI components (@dynatrace/automation-action-components) we highly recommend to use for widget implementation. Those support expression auto-completion, input expand mode, etc.

The App Toolkit will set up your widget for communication with the Workflows, thus ensuring task input values are populated, and Automation action component features work.

#### Action app function

App functions implement the actual logic of an action. When implementing your desired business logic, be aware of the following app function limitations.

The AutomationEngine invokes the action app function while processing tasks and their actions. Any expression used in a task input is resolved at runtime of the workflow. Looking at a task in the execution monitor of Workflows shows all resolved inputs as provided to the function invocation by the AutomationEngine.

If your Custom Action requires a connection (app setting) the related schema must have the following properties:

- MultiObject property must be set to true

- Name property must be apply unique constraint

- Ordered property must be set to false

Use the generated sample as a template for customizations.

###

#### Automate app function runs
Run app functions automatically through the Workflows app.How-to guide

#### Create a custom Workflow action
Create custom workflow actions to integrate third-party systems into your workflows.How-to guide

#### Test custom actions
Test your custom workflow actions within Dynatrace Apps.How-to guide

#### Use intents for Workflows
Use intents provided by the Workflows app.How-to guide

---

## workflows/automate-app-function-runs

`/develop/guides/workflows/automate-app-function-runs/`

- Workflows
- Automate app function runs

## Automate app function runs

- How-to guide
- 1-min readTo run a function automatically based on predefined conditions, use the Workflows app. There are numerous reasons why you might want to run a function automatically, for example:

- To fetch data from external systems and write time series

- To sync an app state with an external system

### Solution

In the Workflows app, create a workflow with the trigger of your choice and a task of type `Run Javascript` to call the function:

api/workflow-example.function.ts
`tsx
export default async function () { const response = await fetch('/apps/my.demo.app/api/query-external-data'); if (!response.ok) { const responseText = await response.text(); throw new Error(`Request failed with status ${response.status}. Response text: ${responseText}`); }}
`

The URL follows the same pattern as for calls from the app UI. In this example, `my.demo.app` is the ID of the app and `query-external-data` is the name of the function.

---

## workflows/create-custom-action

`/develop/guides/workflows/create-custom-action/`

- Workflows
- Create a custom action

## Create a custom Workflow action

- How-to guide
- 6-min readYou can extend Workflows via custom actions. In a custom action, you implement your integration with any third-party system that allows the user to communicate with other systems. Users can then add your custom action as a task to their workflows. This guide explains how to create a custom action.

In this guide, you'll create a custom action named greeter that:

- Accepts a name and a connection as an input.

- Returns a greeting message using the name given as the input and logs the message in Workflows.

- Shows how to retrieve the connection as an app settings object by its ID.

### Create an action

A custom action is part of a Dynatrace app. To create an action, run the following command in the root directory of your app within the terminal:

`tsx
npx dt-app action create greeter
`

The command will generate an action named greeter in the `/actions` directory with some default files and register the action in the app config. When you run `dt-app deploy`, it will detect the action on the filesystem and deploy it as part of the whole app artifact, regardless of whether the action is registered in the app config.

If you develop an app that only consists of actions and doesn't provide a UI,
consider hiding your app in the launcher by setting `app.hidden` to `true`
in your `app.config.json`.

#### Update Jest config

The earlier command also generates Jest files to test your action. If you use Jest for testing your Dynatrace app, you can update your `jest.config.js` file in the root directory as follows:

jest.config.js
`tsx
module.exports = { projects: ['/actions/jest.action.config.js', '/actions/jest.widget.config.js'],};
`

#### Run the action in a workflow

Now that you have updated the app configuration and have all the files, you can deploy the app to run it in a workflow using the following command in the terminal:

`tsx
npx dt-app deploy
`

After deployment, do the following:

- Open Workflows and create a new workflow.

- Then, add a task and select the Greeter task from the list.

- Save the workflow and run it.

By running a workflow, you'll end up in the execution monitor. Within there, you can see not only execution details but also the input sent to your action and the result produced by your action. This information is in the respective `Detail`, `Input`, and `Result` tabs. You can find the logs in the dedicated log section at the bottom of the page.

NoteTo find the details about building and monitoring workflows, visit Introduction to workflows
 |
 | Input Tab | Result Tab
 | |
Congratulations. You ran a task successfully with your custom action.

### Widget interface

The App Toolkit generates a default widget interface for you after you execute the `npx dt-app action create` command. For the greeter action, you'll find this default widget UI in `/actions/greeter.widget.tsx`. It has two UI elements:

- Connection: It's an `AutomationConnectionPicker` component that lets you pick an app setting. The user defines this app setting, which contains information to connect to an external system. It's then sent to the action logic as the `connectionId` property.

- Name: It's an input element where the user can insert their name. It's also sent to the action logic as a `name` property.

CautionThe input produced by the widget is the payload for the action app function. The app function implementing the action defines its contract by the input it consumes. Changing it has an impact on any existing workflow. You need to ensure that your action app function does support legacy and newer payloads if you make changes.
The same is true for your action's return value (the return value of the action app function).
This code will result in the following widget UI:

NoteWhile developing locally, you can mock the connection picker value (`My Connection`). Go to local development section for app settings to learn more.

### Action logic

The App Toolkit generates a default action logic in the `/actions` directory. This default code handles the `connectionId` and the `name` payload sent by the widget interface. You can find the file at `/actions.greeter.actions.ts`. This file is an app function explicitly for the greeter action.

It's essential to understand the following things:

- The input from the widget interface is available as the `payload` property.

- The app function's return value becomes the output of the action.

#### Get app settings

If you look at the code in the file, you'll find that you can get the app settings using `getAppSettingsObjectByObjectId` from `@dynatrace-sdk/client-app-settings-v2` as follows:

`tsx
const connectionObject = await appSettingsObjectsClient.getAppSettingsObjectByObjectId({ objectId: payload.connectionId,});
`

NoteTo use `await` in React components, you need to wrap the asynchronous invocation in an `async` function. Read more about it in this guide.
It'll give you access to the URL and the token required to access the external system through `connectionObject.value.url` and `connectionObject.value.token`, respectively. You can use them to access the external system in your app function.

The `generate action` command automatically includes the `settings:objects:read` scope in your app config, which is essential for operating the `getAppSettingsObjectByObjectId` function. There's no need for manual scope addition, as the command ensures your app has correct permissions for accessing settings objects.

It's essential to understand that there are different types of fields in settings. Especially for any credentials like `token`, the `"type": "secret"` should be used.

#### Log messages

You can log messages for the end user using the `userLogger` function exported by `@dynatrace-sdk/automation-action-utils` as follows:

`tsx
userLogger.info(`Hello ${payload.name}! Have a great day!`);
`

These logs will appear in the task's logs in the Workflow for every execution.

NoteThe log size is limited to 1 MB.

### Debug the action

Workflows offer a dev-helper tool that helps you debug action widgets.

You can access the dev helper via the links displayed by the `dt-app` on your terminal after executing the `npx dt-app dev` command.

NoteThe total size of a custom workflow action's result and log data must not exceed 6 MB. A larger response will cause the action to fail.

### Show sample results

You can show a sample result for your action. Users can look at this sample and figure out what the action output would look like.

The App Toolkit creates a `greeter.sample-result.json` file in the `/assets` directory for our greeter action. Open this file and add the sample JSON result.

### End an action early

If you want to exit from your action at any point, you can use the `UnsuccessfulActionError` error class from `@dynatrace-sdk/automation-action-utils/actions` as follows:

`tsx
throw new UnsuccessfulActionError('A message why the action failed');
`

This will result in the action's failure with the given message.

### Validate expression values

For actions with an input that's some sort of syntax for a third party system (for example, a Kubernetes manifest, an SQL query, or similar), you want to protect your action from injection attacks. You can, therefore, control the values against which to evaluate an expression. To prevent any unwanted input, specify an `expressionValidation` in your action manifest to validate the expression value against a pattern.

For example, the app evaluates any expression in the `name` field against uppercase letters.

`tsx
// Excerpt of app.config.json{ ... "actions": [ { "name": "greeter", "title": "Greeter", "expressionValidation": {"name": {"pattern": "[A-Z]+"}} } ]}
`

A violation such a validation at runtime shall fail the task.

### Summary

You learned how to create a custom action with the action widget UI and action function to implement its functionality. For further information about the Workflows and AutomationEngine, have a look at the user documentation.

### Related topics

- Store app settings

- App settings service

---

## workflows/test-custom-actions

`/develop/guides/workflows/test-custom-actions/`

- Workflows
- Test custom actions

## Test custom actions

- How-to guide
- 13-min readAfter you've created your custom Workflow Action, you'll likely want to test it. This guide describes best practices and recommended approaches to properly test your app functions and widgets that implement the custom action.

### Approach custom action tests

Run app functions unit and integration tests in your terminal or IDE with mocked dependencies. For end-to-end tests, use AutomationEngine via the Workflows API.

For widgets, follow Dynatrace Apps testing guide for unit tests and use the `dev-helper` for end-to-end tests.

### Test an app function

Refer to the Dynatrace Apps testing guide on how to write tests for app functions.

#### Write unit and integration tests

The app function testing guide emphasizes testing the business logic of functions. We recommend focusing on testing individual function invocations and simulating dependencies and requests. This approach allows isolated testing of core functionality to ensure proper behavior. By simplifying the testing environment and abstracting away external dependencies, you can effectively evaluate if your app functions work as expected.

#### Write E2E tests

NoteYour test workflow will use the actions currently installed in the target environment. During the setup, deploy and ensure that the action version you expect to test is correct.
If your custom action uses the settings schema for connection details, also ensure that:

- You've created settings schemas.

- Connections objects exist.

The E2E testing guide emphasizes testing the interaction between your application and third-party systems. Verifying seamless integration with these systems is essential to avoid regressions.

We recommend creating your test scenarios as workflows using a Workflows API. Run these workflows and inspect the results of their execution. The testing process shouldn't involve any user interface interactions.

By utilizing the Workflows API, you can simulate various scenarios and test the interactions and behavior of your app function with Dynatrace or third party systems. Analyzing the workflow execution results will help you identify any issues or regressions of your app functions.

What you should test:

- Single invocations with different parameters for test scenarios.

- Several app functions tested together; those are scenarios where the input of the subsequent app function invocations depends on the results of the previous one.

- E2E tests are the only place where you should use Jinja expressions. All other tests should avoid the syntax. AutomationEngine resolves them to static values, which your actions later use as inputs.

NoteIn some test cases, you may expect an app function that implements an action to fail intentionally, such as receiving an HTTP 403 response from a request. In such situations, we recommend creating an intermediate placeholder task with a custom start condition to validate if the previous task failed as expected.This approach allows you to verify the desired behavior explicitly and ensures that the initial tasks, based on their expected outcome, trigger subsequent tasks. By incorporating these intermediate checks, you can effectively test and validate how your app handles failure scenarios.

##### Example

The example below shows a TypeScript script that leverages the Automation SDK to create and run a workflow. The script also checks for the final state of the workflow execution.

The workflow consists of three tasks in a sequence:

- Make a Jira issue.

- Comment on the Jira issue.

- Transfer the issue to a different state.

NoteUsing the Workflow API, you can use any programming language and tools for such tests. To access its visual documentation, navigate to `https:///platform/swagger-ui/index.html?urls.primaryName=Automation`Remember to replace with your environmental URL address in the link above.
action-e2e.spec.ts
`tsx
import { workflowsClient, ExecutionState, executionsClient } from '@dynatrace-sdk/client-automation';const workflow = await workflowsClient.createWorkflow({ body: { title: '[e2e] Test Jira actions', tasks: { create_issue: { name: 'create_issue', input: { project: { id: '18890', }, issueType: { id: '2', }, description: 'New issue', connectionId: 'vu9U3hXa3q0AAAABAB1hcHA6ZHluYXRyYWNlLmppcmE6Y29ubmVjdGlvbgAGdGVuYW50AAZ0ZW5hbnQAJGI4MjU2NDI1LTM5YWEtM2ZlMi05NzgzLTlkOGE1ZmQ0MWFkY77vVN4V2t6t', }, action: 'dynatrace.jira:jira-create-issue', position: { x: 0, y: 1, }, }, comment_on_issue: { name: 'comment_on_issue', input: { comment: 'Updating with relevant details', issueID: '{{ result("create_issue").id }}', connectionId: 'vu9U3hXa3q0AAAABAB1hcHA6ZHluYXRyYWNlLmppcmE6Y29ubmVjdGlvbgAGdGVuYW50AAZ0ZW5hbnQAJGI4MjU2NDI1LTM5YWEtM2ZlMi05NzgzLTlkOGE1ZmQ0MWFkY77vVN4V2t6t', }, action: 'dynatrace.jira:jira-add-comment', position: { x: 0, y: 2, }, conditions: { states: { create_issue: 'OK', }, }, description: 'Comment on a Jira issue', predecessors: ['create_issue'], }, transition_issue: { name: 'transition_issue', input: { project: '18890', issue: '{{ result("create_issue") }}', issueType: '2', connectionId: 'vu9U3hXa3q0AAAABAB1hcHA6ZHluYXRyYWNlLmppcmE6Y29ubmVjdGlvbgAGdGVuYW50AAZ0ZW5hbnQAJGI4MjU2NDI1LTM5YWEtM2ZlMi05NzgzLTlkOGE1ZmQ0MWFkY77vVN4V2t6t', targetStatus: '11415', }, action: 'dynatrace.jira:jira-transition-issue', position: { x: 0, y: 3, }, conditions: { states: { comment_on_issue: 'OK', }, }, predecessors: ['comment_on_issue'], }, }, },});// Utility function to block the script execution for `ms` milliseconds.const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));const POLL_INTERVAL = 5 * 1000; // 5 secondslet execution = await workflowsClient.runWorkflow({ id: workflow.id as string, body: {} });// Poll the execution state until it's finished.while (execution.state === ExecutionState.Idle || execution.state === ExecutionState.Running) { execution = await executionsClient.getExecution({ id: execution.id as string }); await sleep(POLL_INTERVAL);}if (execution.state !== ExecutionState.Success) { console.error('E2E tests failed'); process.exit(1);}
`

### Test a widget

You don't need to test any Strato Design System components. You can rely on them; developers have tested them adequately.

#### Write UI integration tests

Visit the Dynatrace Apps testing guide to learn how to write unit tests for your UI.
Focus on testing the functionality of a single component in isolation by simulating how your end users will use it.

#### Write E2E tests

Test your widget only by performing actions you could expect real users to make. The test framework allows initializing a widget with or without the initial value, such as an existing or new task configuration. More details are in the example below.

You don't need to worry about embedding your widget into the Workflows or how it persists the widget value. Workflows take care of this for you.

The tests you write must add value to your widget, verify the widget's state, and show that:

- Your components interact as expected; for example, there are interdependencies between widget UI components.

- Your widget compiles and renders all fields. Ensure that there are no breaking changes in dependencies.

- The widget produces the output you would expect.

It's important not to test the app function or its business logic. Therefore, don't use `Run Action` from the dev-helper view. You can test app functions using specific app function tests. In these E2E tests, we focus on widgets only.

##### Examples

These examples test the `Greeter` widget created in the custom Workflows action section.

Let's begin by setting up E2E tests for Dynatrace Apps. In addition to the required environment variables, add `WIDGET_URL`, which refers to the URL address where your custom action runs. It could either be the action's local URL displayed by the App Toolkit or the URL of the deployed widget.

NoteYou can retrieve the base URL of a deployed action using the visual documentation by navigating to: `https:///platform/swagger-ui/index.html?urls.primaryName=AppEngine%20-%20Registry#/AppEngine%20-%20Registry%20-%20Apps/getApp`Provide your application ID on this page, add `isolatedUri` to the `add-fields` parameter, and execute the request. In the response, look for the `isolatedUri` object. Under this object, you'll find the `widgetUrl`. Finally, append your action widget's specific path, for example, `/actions/greeter`, to the `widgetUrl` while making sure you preserve any query parameters that may be present in the `widgetUrl` e.g. `https:///actions/greeter?`.Ensure you replace the placeholder with the actual URL address of your environment.
Once you've configured the tests, you can change the `setup` method in the `setup.ts` file. This change will allow the `setup` method to accept a URL parameter. When you provide a URL address, the test will navigate to this location just before it starts. Providing a URL eliminates the need to switch between iframes during the test.

e2e/setup.ts
`tsx
export async function setup( controller: TestController, navigateTo?: string): Promisevoid> { await controller.maximizeWindow(); await controller.useRole(role); if (navigateTo) { await controller.navigateTo(navigateTo); } ... const iframeSelector = Selector("iframe", { timeout: 60_000 }); await controller.switchToIframe(iframeSelector);}
`

Additionally, add the following content:

e2e/setup.ts
`tsx
export const DEV_HELPER_URL = `${process.env.ENVIRONMENT_URL}/ui/apps/dynatrace.automations/dev-helper?src=${process.env.WIDGET_URL}`;export const WIDGET_STATE_STORAGE_KEY = 'dev-helper-widget-state';
`

- The `DEV_HELPER_URL` represents the URL address to the dev-helper, which includes a query parameter `src` pointing to the widget URL. Refer to the debugging custom action documentation for more detailed information on accessing dev-helper.

- The `WIDGET_STATE_STORAGE_KEY` is the key used in the `localStorage` of the dev-helper to store the widget state.

NoteBe aware that your custom action may not be installed in an environment where the E2E tests run. This circumstance could lead to an error page indicating that the provided app doesn't exist. However, the test setup will redirect you to the dev-helper within a few seconds.

###### Test an empty widget

Let's create the initial test that guarantees the persistence of provided values in the widget state.

e2e/tests/greeter-empty.spec.ts
`tsx
import { ClientFunction, Selector } from 'testcafe';import { DEV_HELPER_URL, WIDGET_STATE_STORAGE_KEY, setup } from '../setup';// Client function to run custom-code on the client side.// https://testcafe.io/documentation/402832/guides/basic-guides/client-functionsconst getLocalStorageItem = ClientFunction((key: string) => window.localStorage.getItem(key));fixture('Empty widget').beforeEach(async (t) => { await setup(t, DEV_HELPER_URL); await t.switchToIframe(Selector('iframe#widget', { timeout: 10_000 }));});test('Fill empty widget form', async (t) => { const nameInput = Selector('[data-testid="base-code-editor-content"]'); // Fill widgets inputs await t.typeText(nameInput, 'John Sr.'); // Assert inputs values await t.expect(nameInput.innerText).eql('John Sr.'); // Switch to dev-helper app iframe await t.switchToMainWindow().switchToIframe(Selector('iframe')); // Assert widget state await t.expect(getLocalStorageItem(WIDGET_STATE_STORAGE_KEY)).eql(JSON.stringify({ name: 'John Sr.' }));});
`

Let's review the most crucial parts of the test:

- We set up the test and navigate to the dev-helper. Then, we switch to the context of the widget iframe.
NoteTo make it convenient, you can always find the iframe of any widget within the dev-helper by the ID `widget`.

- We provide value to the widget input.

- We switch to the dev-helper iframe, retrieve the widget state, and verify that it matches the expected value, which acts as a contract. The AutomationEngine will use it during the execution of the action upon saving a workflow.

###### Test a widget with an initial value

The following test shows how to pass the initial value via the URL query parameters.

e2e/tests/greeter-with-initial-value.spec.ts
`tsx
import { ClientFunction, Selector } from 'testcafe';import { DEV_HELPER_URL, WIDGET_STATE_STORAGE_KEY, setup } from '../setup';// Client function to run custom-code on the client side.// https://testcafe.io/documentation/402832/guides/basic-guides/client-functionsconst getLocalStorageItem = ClientFunction((key: string) => window.localStorage.getItem(key));fixture('Widget with initial value').beforeEach(async (t) => { const initialValue = { name: 'Mark' }; const uriEncodedInitialValue = encodeURIComponent(JSON.stringify(initialValue)); await setup(t, `${DEV_HELPER_URL}&initialValue=${uriEncodedInitialValue}`); await t.switchToIframe(Selector('iframe#widget', { timeout: 10_000 }));});test('Validate initial values and make changes', async (t) => { const nameInput = Selector('[data-testid="base-code-editor-content"]'); // Verify that the widget holds the correct value await t.expect(nameInput.innerText).eql('Mark'); // Make changes await t.typeText(nameInput, 'Ann Marie', { replace: true }); // Switch to dev-helper app iframe await t.switchToMainWindow().switchToIframe(Selector('iframe')); // Assert widget state await t.expect(getLocalStorageItem(WIDGET_STATE_STORAGE_KEY)).eql(JSON.stringify({ name: 'Ann Marie' }));});
`

Let's understand what's happening in the test:

- We set up the test and navigated to the dev-helper. This time, we include an extra query parameter called initialValue. It should hold the URI-encoded value of the initial value for your widget. The dev-helper passes this value to the widget during its initial rendering. Finally, switch to the context of the widget iframe.

- We ensure the widget holds the correct initial value.

- After making changes, the remaining part of the test ensures that the widget state aligns with our expectations.

##### Add optional test improvements

Avoid repetitions for more extensive test scenarios while looking for page elements or simulating user actions. To do so, we'll create Page Models. For further details, refer to the testcafe documentation.

Create a file, `e2e/page-models/dev-helper.ts`, with the following content.

e2e/page-models/dev-helper.ts
`tsx
import { Selector, t } from 'testcafe';class DevHelper { widgetIframe: Selector; constructor() { this.widgetIframe = Selector('iframe#widget', { timeout: 10_000 }); } async switchToDevHelper() { await t.switchToMainWindow().switchToIframe(Selector('iframe')); } async switchToWidgetIframe() { await t.switchToIframe(this.widgetIframe); }}export default new DevHelper();
`

- The `widgetIframe` selector targets the widget iframe.

- The `switchToDevHelper` action provides a convenient method to switch to the dev-helper iframe. Such action is practical, for example, when you need to access and read the widget state from the `localStorage`.

- The `switchToWidgetIframe` action offers a convenient way to switch to the widget iframe and interact with it.

As a next step, create a `Greeter` page model in `e2e/page-models/greeter.ts`.

e2e/page-models/greeter.ts
`tsx
import { Selector, t } from 'testcafe';class Greeter { nameInput: Selector; constructor() { this.nameInput = Selector('[data-testid="base-code-editor-content"]'); } async typeName(name: string) { await t .expect(this.nameInput.exists) .ok('name input is not visible') .typeText(this.nameInput, name, { replace: true }); }}export default new Greeter();
`

To ease the step of getting widget state, you can create the following file `e2e/utils.ts` and add content:

e2e/utils.ts
`tsx
import { ClientFunction } from 'testcafe';import DevHelper from './page-models/dev-helper';import { WIDGET_STATE_STORAGE_KEY } from './setup';export const getLocalStorageItem = ClientFunction((key: string) => window.localStorage.getItem(key));export const getWidgetState = async (): PromiseRecordstring, unknown>> => { await DevHelper.switchToDevHelper(); const widgetStateRaw: string | null = await getLocalStorageItem(WIDGET_STATE_STORAGE_KEY); if (!widgetStateRaw) return {}; try { return JSON.parse(widgetStateRaw); } catch (e) { console.warn('Failed to read widget state due to', e); return {}; }};export const encodeInitialValue = (value: Recordstring, unknown>): string => encodeURIComponent(JSON.stringify(value));
`

The `getWidgetState` gets the widget state as an object from the `localStorage`, and the `encodeInitialValue "utility function helps to translate the object value to URI encoded string.

Below, you can find updated tests that use Page Models objects and actions.

##### Test an empty widget

e2e/tests/greeter-empty.spec.ts
`tsx
import DevHelper from '../page-models/dev-helper';import Greeter from '../page-models/greeter';import { setup, DEV_HELPER_URL } from '../setup';import { getWidgetState } from '../utils';fixture('Empty widget').beforeEach(async (t) => { await setup(t, DEV_HELPER_URL); await DevHelper.switchToWidgetIframe();});test('Fill empty widget form', async (t) => { // fill widget input await Greeter.typeName('John Sr.'); // assert inputs values await t.expect(Greeter.nameInput.innerText).eql('John Sr.'); // assert widget state await t.expect(await getWidgetState()).eql({ name: 'John Sr.' });});
`

##### Test a widget with an initial value

e2e/tests/greeter-with-initial-value.spec.ts
`tsx
import DevHelper from '../page-models/dev-helper';import Greeter from '../page-models/greeter';import { DEV_HELPER_URL, setup } from '../setup';import { encodeInitialValue, getWidgetState } from '../utils';fixture('Widget with initial value').beforeEach(async (t) => { const initialValue = { name: 'Mark' }; await setup(t, `${DEV_HELPER_URL}&initialValue=${encodeInitialValue(initialValue)}`); await DevHelper.switchToWidgetIframe();});test('Validate initial values and make changes', async (t) => { // verify that the widget value has been populated correctly await t.expect(Greeter.nameInput.innerText).eql('Mark'); // make changes await Greeter.typeName('Ann Marie'); // assert widget state await t.expect(await getWidgetState()).eql({ name: 'Ann Marie' });});
`

NoteWhen using TestCafe with a headless browser like Chrome Headless to test your custom actions, you may get the following error:
`tsx
JS ERROR | Cannot read properties of null (reading 'hammerhead|shadow-ui-element')
`
Disable TestCafe's native automation mode to solve this issue by following the instructions on TestCafe's website

### Related topics

- Create a custom Workflow action

---

## workflows/use-intents

`/develop/guides/workflows/use-intents/`

- Workflows
- Use intents for Workflows

## Use intents for Workflows

- How-to guide
- 6-min readWorkflows provide the following intents:

- Create a new workflow: an intent to create a workflow and, optionally, an associated trigger

- Create a new workflow from template by id: an intent to create a workflow from a template by providing the document ID of the template

- Create a new workflow from template: an intent to create a workflow from a template providing interactive guidance for app requirements and task connections configuration

- View workflow: an intent that opens an existing workflow in the editor by a given ID

- Search workflows: an intent to search for workflows, thus opening the list of workflows for given filter criteria

- Automate DQL Query: an intent to create a new workflow with a single Execute DQL Query task and fill the task with the passed DQL query

- Automate code: an intent to create a new workflow with a single Run JavaScript task and fill the task with the passed code snippet

### Create a new workflow

Do you have data in your app that should serve as a workflow starting point, for example, a daily report? You can use intents to guide the user from your app to a new workflow.

#### Define the intent

An intent to create a workflow requires at least the following mandatory properties:

`tsx
{ "title": "Workflow from intent", "tasks": {}}
`

Here is an example of an intent for a workflow with two sequential tasks and an interval-based trigger:

`tsx
{ "title": "Workflow from intent", "tasks": { "task1": { "name": "task1", "action": "dynatrace.automations:run-javascript", "input": { "script": "export default async function () { \n console.log('Hello world.')\n}" }, "position": { "x": 0, "y": 1 } }, "task2": { "name": "task2", "action": "dynatrace.automations:http-function", "input": { "url": "https://www.dynatrace.com/contact/", "method": "GET" }, "position": { "x": 0, "y": 2 }, "predecessors": ["task1"] } }, "trigger": { "schedule": { "trigger": { "type": "interval", "intervalMinutes": 25 } } }}
`

#### Intent payload details

A workflow can consist of a list of `tasks`. Each task has the following properties:

- `action`: one of the actions which are made available by apps

- `input`: action parameters depending on the `action`

- `position`: the position of the task in the graph

- `predecessors`: an optional list of predecessor tasks

An optional `trigger` can be provided to define how the workflow is executed. It can specify either a `schedule` or an `eventTrigger`. If omitted, an on-demand trigger is assumed.

`schedule` can be one of the following types:

- cron: `{ "type": "cron", "cron": "0 * * * *" }`

- interval: `{ "type": "interval", "intervalMinutes": 30 }`

- time: `{ "type": "time", "time": "09:00" }`

`eventTrigger` can be one of the following types::

event:

`tsx
{ "triggerConfiguration": { "type": "event", "value": { "query": "..." } }}
`

davis-problem:

`tsx
{ "triggerConfiguration": { "type": "davis-problem", "value": { "onProblemClose": false, "categories": { "monitoringUnavailable": true, "availability": true, "error": true, "slowdown": true, "resource": true, "custom": true, "info": true } } }}
`

davis-event:

`tsx
{ "triggerConfiguration": { "type": "davis-event", "value": { "onProblemClose": false, "types": ["APPLICATION_ERROR_RATE_INCREASED"] } }}
`

Note"Davis" is the former brand name for Dynatrace AI, now called "Dynatrace Intelligence." Legacy strings and files may still use "Davis" and these references remain valid.

### Create a new workflow from a template by ID

An exported workflow is an exact copy of a workflow. To import it into another environment, you'll need to adjust details such as the owner, actor, connections, and more. Using a workflow template makes it easier to transport a workflow from one environment to another.

Workflow templates are environment-agnostic representations of workflows, enriched with information about required apps and connections. Dependencies for specific versions of required apps are evaluated, and links to the Dynatrace Hub make installation simple. Connections for action types are listed and can be configured for the workflow. All steps are optional, allowing users to skip them if needed.

If you want users to have interactive guidance when configuring a workflow, use intents based on workflow templates instead of workflows.

This specific intent references a workflow template by its document ID and optionally allows further input values to tweak the selected workflow template.

#### Define the intent

Below is an example of an intent referencing a workflow template document:

`tsx
{ "workflowTemplateId": "dynatrace.slack.davis-problem-notification"}
`

#### Intent payload details

- `workflowTemplateId`: The document ID as a string. This is typically your app name concatenated with a period (`.`) and the document name, as provided in the app manifest that ships the template. (Required)

- `inputs`: A list of input objects. Each object contains:

- `targets` A list of target properties specified as JSON Path strings in dot notation (e.g., `path.to.prop.foo`, `path.to.prop.bar`, etc.).

- `value`: The value to set for the specified targets.

Note: Values for task properties that hold connection IDs will always be set to the connection selected by the user in the "Create workflow from template" wizard in the Workflows app, no matter the inputs configuration.

### Create a new workflow from template

For an explanaition about workflow vs workflow template please see the description of the intent Create a new workflow from template by id -

We always recommend to use Create a new workflow from template by id over this intent, unless you encounter a limitation where you cant ship the template with your app. Please also mind the length restriction of an URL and therefore an intent, which effects the size of the workflow template you can provide.

#### Define the intent

Here is an example of an intent for a workflow with two sequential tasks and an interval-based trigger:

`tsx
{ "metadata": { "dependencies": { "apps": [ { "id": "dynatrace.automations", "version": "^1.0.0" }, { "id": "dynatrace.slack", "version": "^1.2.0" } ] }, "inputs": [ { "type": "connection", "schema": "app:dynatrace.slack:connection", "targets": ["tasks.send_message.connection"] } ] }, "workflow": { "title": "Workflow from intent", "tasks": { "send_message": { "name": "send_message", "description": "Send a message to a Slack workspace", "action": "dynatrace.slack:slack-send-message", "input": { "message": "", "reaction": [], "connection": "", "workflowID": "{{ execution().workflow.id }}", "executionID": "{{ execution().id }}", "executionDate": "{{ execution().started_at }}", "appendToThread": false, "selectedRequestType": 0, "attachmentToggleValue": "none" }, "position": { "x": 0, "y": 1 } }, "run_javascript": { "name": "run_javascript", "description": "Build a custom task running js Code", "action": "dynatrace.automations:run-javascript", "input": { "script": "export default async function () { \n console.log('Hello world.')\n}" }, "position": { "x": 0, "y": 2 }, "predecessors": ["send_message"] } }, "trigger": { "schedule": { "trigger": { "type": "interval", "intervalMinutes": 25 } } } }}
`

#### Intent payload details

- `metadata` contains app dependencies and connection configuration information (required).

- `dependencies` contains app dependencies.

- `apps` is a list of required apps as objects consisting of app `id` and `version`. `version` supports npm style semver version range syntax.

- `inputs` declares a set of input definitions for workflow task input configuration the user provides on import. It consists of `type` (the only supported type, for now, is "connection"), type-specific attributes (`schema` as fully qualified settings schema id for connection type), and `targets` as a list of JSON path style (dot notation) qualifiers to specify the task inputs to update with the connection id value from the wizard.

- `workflow` is similar to the workflow definition described in `Create a new workflow` section above but deliberately omits actor and owner information to allow environment-agnostic creation (required).

### View workflow

An intent that opens an existing workflow in the editor by a given ID.

#### Define the intent

`tsx
{ "dynatrace.workflows.id": "00000000-0000-0000-0000-000000000000"}
`

#### Intent payload details

You need to provide only one property, either `dynatrace.workflows.id` or `workflow.id`.

- `dynatrace.workflows.id`: the UUID of the workflow

- `workflow.id`: the UUID of the workflow

### Search workflows

An intent to search for workflows, thus opening the list of workflows for given filter criteria.

#### Define the intent

`tsx
{ "dt.searchQuery": { "search": "My workflow", "owner": "00000000-0000-0000-0000-000000000000", "triggerType": "Manual" }}
`

#### Intent payload details

- `dt.searchQuery`: object (required)

- `search`: filter by a search string

- `owner`: filter by the owner of the workflow

- `triggerType`: filter by the trigger type. Available options are `Manual`, `Schedule`, and `Event`.

### Automate DQL Query

Using `dt.query` in the intent payload, you can create a new workflow with a single Execute DQL Query task that will execute the passed query.

#### Define the intent

`tsx
{ "dt.query": "fetch logs\n| limit 100"}
`

#### Intent payload details

- `dt.query`: the DQL query (required)

### Automate code

Using `dt.code` in the intent payload, you can create a new workflow with a single Run JavaScript task to execute the passed code.

#### Define the intent

`tsx
{ "dt.code": "export default async function () {\n return \"Hello, world!\";\n}"}
`

#### Intent payload details

- `dt.code`: the code snippet (required)

### Related topics

- Send intents
