# @dynatrace-sdk/react-hooks

Source: <https://developer.dynatrace.com/develop/sdks/react-hooks/> (latest: `react-hooks`).

> Truncated — this SDK's auto-generated reference is large. Key exports/usage are below; see the full reference at the URL above.

## react-hooks

`/develop/sdks/react-hooks/`

- SDK for TypeScript
- React hooks

## React hooks
 @dynatrace-sdk/react-hooks v1.12.1 Latest (V1)

`tsx
npm install @dynatrace-sdk/react-hooks
`

#### Why should I use this package?

This package simplifies interactions with Grail, documents, and app states in React by encapsulating complex state management. It offers easy-to-use hooks that integrate seamlessly with client packages, enhancing developer productivity and usability in React applications.

#### Simplified data querying from Grail

Traditionally, querying data in Dynatrace involves using the client-query package and managing complex React state. The `useDql` hook in this package streamlines this process. The following example showcases how to fetch data with a DQL query:

`tsx
const { data, error, isLoading } = useDql('fetch logs');
`

This hook is fully compatible with the parameters used in the `queryExecute` function of the `@dynatrace-sdk/client-query` package.

For instance, to limit the number of results returned:

`tsx
const { data, error, isLoading, refetch } = useDql( { query: 'fetch logs', maxResultRecords: 2000, });
`

You can delay the execution of the query until a user clicks on a button by passing additional query options to the hook:

`tsx
const { data, error, isLoading, refetch } = useDql('fetch logs', { enabled: false });function onClickQuery() { refetch();}
`

You should add appropriate scopes to your app's configuration based on the query type. For more details, refer to the Bucket and table permissions in Grail documentation.

#### Interacting with documents and app states

Beyond DQL queries, our hooks facilitate interactions with documents and app state. They allow control over immediate or deferred query execution.

`tsx
const { data, error, isLoading } = useDocument({ id: documentId }, { autoFetch: true });
`

For creating, updating, or deleting documents or app state, an explicit execute call is necessary:

`tsx
const { data, execute, error } = useCreateDocument();function onClickCreateDocument() { execute(DOCUMENT_DATA);}
`

Depending on your interaction type, add these scopes to your app configuration:

 |
 | Function | Scope
 | Document read | document:documents:read
 | Document write/update | document:documents:write
 | Document delete | document:documents:delete
 | State read | state:app-states:read
 | State write | state:app-states:write
 | State delete | state:app-states:delete
 | User state read | state:user-app-states:read
 | User state write | state:user-app-states:write
 | User state delete | state:user-app-states:delete

#### Simplified Use of Davis® Analyzers

Leveraging Davis® analyzers traditionally involves complex state management and polling logic, alongside the `@dynatrace-sdk/client-davis-analyzers` package. The `useAnalyzer` hook in this package makes this process much more straightforward:

`tsx
const { data, error, isLoading } = useAnalyzer({ analyzerName: 'dt.statistics.GenericForecastAnalyzer', body: { timeSeriesData: { expression: query, }, },});
`

This hook supports all the parameters available in the executeAnalyzer method from the `@dynatrace-sdk/client-davis-analyzers` package.

To defer the execution of the analyzer until a user action, like a button click, configure the hook with additional options:

`tsx
const { data, error, isLoading, refetch } = useAnalyzer({ analyzerName: 'dt.statistics.GenericForecastAnalyzer', body: { timeSeriesData: { expression: query, }, }, { autoFetch: false, autoFetchOnUpdate: true, }});function onExecuteAnalyzer() { refetch();}
`

In your app's configuration, include the necessary scope:

 |
 | Function | Scope
 | Use analyzer | davis:analyzers:execute

#### App functions

The useAppFunction hook is the simplest way to call app functions. As the other hooks in this package, it provides state handling for loading and error states:

`tsx
const { data, error, isLoading } = useAppFunction({ name: 'functionName', data: 'data' });
`

Sometimes you want to delay the execution of the app function until a user clicks on a button. This can be achieved by passing additional options to the hook:

`tsx
const { data, error, isLoading, refetch } = useAppFunction({ name: 'functionName', data: 'data' }, { autoFetch: false, autoFetchOnUpdate: false });function onClick() { refetch();}
`

### Hooks

#### useAccessorPermissionsV2

useAccessorPermissionsV2(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Load accessor permissions.

##### Parameters
 |
 | Name | Type | Description
 | params*required | AccessorPermissionsParamsV2 | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useAllUsersPermissionsV2

useAllUsersPermissionsV2(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Load all-users permissions.

##### Parameters
 |
 | Name | Type | Description
 | params*required | LoadAllUsersPermissionsParamsV2 | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useAnalyzer

useAnalyzer(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Execute an analyzer with the given data.

##### Parameters
 |
 | Name | Type | Description
 | params*required | AnalyzerParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useAppFunction

useAppFunction(params,options?): { cancel, data, error, isError, isLoading, isSuccess, refetch, status }Call specified app function by name.

##### Parameters
 |
 | Name | Type | Description
 | params*required | AppFunctionParams | App function params.
 | options | HookOptions | Additional options for the react hook.

#### useAppState

useAppState(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Gets app state

##### Parameters
 |
 | Name | Type | Description
 | params*required | AppStateParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useAppStates

useAppStates(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }List app states

##### Parameters
 |
 | Name | Type | Description
 | params*required | AppStatesParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useCreateDocument

useCreateDocument(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Create a new document.

#### useCreatePermissionsV2

useCreatePermissionsV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Create a new permissions.

#### useCreateSettings

⚠️ Deprecated
Use V2 instead.

useCreateSettings(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Create a new setting.

#### useCreateSettingsV2

useCreateSettingsV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Create a new setting.

#### useDeleteAccessorPermissionsV2

useDeleteAccessorPermissionsV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Delete the accessor permissions

#### useDeleteAllUsersPermissionsV2

useDeleteAllUsersPermissionsV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Delete the all-users permissions

#### useDeleteAppState

useDeleteAppState(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Deletes app state

#### useDeleteAppStates

useDeleteAppStates(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Delete all app states

#### useDeleteDocument

useDeleteDocument(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Delete the document

#### useDeleteSettings

⚠️ Deprecated
Use V2 instead.

useDeleteSettings(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Delete the setting

#### useDeleteSettingsV2

useDeleteSettingsV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Delete the setting

#### useDeleteUserAppState

useDeleteUserAppState(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Delete user app state

#### useDeleteUserAppStates

useDeleteUserAppStates(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Delete all user app states

#### useDocument

useDocument(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Retrieve metadata and content for documents.

##### Parameters
 |
 | Name | Type | Description
 | params*required | DocumentParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useDocumentMetaData

useDocumentMetaData(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Retrieve document metadata.

##### Parameters
 |
 | Name | Type | Description
 | params*required | DocumentMetaDataParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useDownloadDocument

useDownloadDocument(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Download document content

##### Parameters
 |
 | Name | Type | Description
 | params*required | DownloadDocumentParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useDql

useDql(query,options?): UseDqlResultReact hook for executing DQL (Dynatrace Query Language) queries against Grail.Use this hook to run DQL queries in React components and manage query state with less boilerplate.
It returns query data, loading and error state, and functions to cancel or rerun the query.

- By default, queries that are in-flight are cancelled when the browser tab
loses focus. Set `runInBackground: true` to keep them running.

- Results are cached for 60 seconds by default (`staleTime`). Calling `refetch`
while data is still fresh returns the cached result; use `forceRefetch` to
bypass the cache.

- The hook automatically retries on HTTP 429 (Too Many Requests) responses
using the `retryAfterSeconds` header when available, falling back to exponential
back-off.

- When `enablePreview` is set on the query params, intermediate partial results
are exposed via `data` while the query is still running.

##### Parameters
 |
 | Name | Type | Description
 | query*required | string | DqlQueryParams | A DQL query string, or a DqlQueryParams object for full control over execution parameters (timezone, timeframe, locale, etc.). Parameters provided here are merged with any values from a parent DqlQueryParamsProvider, with per-call values taking precedence.
 | options | UseDqlOptions | Optional configuration for the hook behavior.

##### Returns
 |
 | Return type | Description
 | UseDqlResult | Returns the query result, loading and error state, progress information, and functions to cancel or rerun the query.Basic usage
`tsx
function HostList() { const { data, isLoading, error } = useDql( 'fetch dt.entity.host | fields entity.name, state' ); if (isLoading) return span>Loading...span>; if (error) return span>Error: {error.message}span>; return ( ul> {data?.records.map((host) => ( li key={host['entity.name']}>{host['entity.name']}li> ))} ul> );}
`
Typed records
`tsx
interface MyRecord { state: string;}const { data } = useDqlMyRecord>( 'fetch dt.entity.host | fields state');// data?.records is typed as MyRecord[]
`
Advanced query parameters
`tsx
const result = useDql({ query: 'fetch logs | sort timestamp desc | limit 100', defaultTimeframeStart: 'now()-2h', defaultTimeframeEnd: 'now()', timezone: 'Europe/Berlin', locale: 'en_US', enablePreview: true,});
`
Shared query parameters via context
`tsx
DqlQueryParamsProvider defaultTimeframeStart="now()-1h" defaultTimeframeEnd="now()"> HostList /> LogViewer />DqlQueryParamsProvider>
`
Cancellation and refetching
`tsx
const { cancel, refetch, forceRefetch } = useDql('fetch logs');// Cancel the in-flight queryawait cancel();// Refetch only if data is staleawait refetch();// Force a fresh fetch regardless of stale timeawait forceRefetch();
`
Tracking progress
`tsx
const { data, state, progress } = useDql('fetch logs | summarize count()');if (state === 'RUNNING') { return ProgressBar value={progress} />;}
`

#### useDqlQuery

⚠️ Deprecated
Use `useDql` hook instead.

useDqlQuery(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Use this hook to execute a DQL query.

##### Parameters
 |
 | Name | Type | Description
 | paramsDEPRECATED*required | QueryParams | Query and enrich options that will be executed.
 | optionsDEPRECATED | HookOptions | Additional options for the react hook.

##### Returns
 |
 | Description
 | The state of the query, including the result and functions to refetch or cancel the query.

#### useEffectivePermissions

⚠️ Deprecated
Use V2 instead.

useEffectivePermissions(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Retrieve effective settings permissions for the calling user.

##### Parameters
 |
 | Name | Type | Description
 | paramsDEPRECATED*required | Omit | Parameters for the client sdk call.
 | optionsDEPRECATED | HookOptions | Additional options for the react hook.

#### useEffectivePermissionsV2

useEffectivePermissionsV2(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Retrieve effective settings permissions for the calling user.

##### Parameters
 |
 | Name | Type | Description
 | params*required | Omit | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useGrailFields

useGrailFields(options): UseGrailFieldsResultFetches Grail fields from both autocomplete and DSS query sources
and exposes standard React Query status flags.

##### Parameters
 |
 | Name | Type
 | options*required | UseGrailFieldsOptions

##### Returns
 |
 | Return type | Description
 | UseGrailFieldsResult | The raw query data (or the value returned by `select`), plus React Query state flags (`isLoading`, `isError`, `isSuccess`, `errors`, `refetch`, `cancel`).Basic usage:
`tsx
const { data, isLoading } = useGrailFields({ autocompleteQueryOptions: { query: 'fetch logs' }, dssQueryOptions: { dataObject: 'logs' },});// data.autocompleteData, data.dssData
`
With select transform:
`tsx
const { data } = useGrailFields({ autocompleteQueryOptions: { query: 'fetch logs' }, dssQueryOptions: { dataObject: 'logs' }, select: ({ autocompleteData }) => autocompleteData?.suggestions?.map((s) => s.suggestion ?? '') ?? [],});
`

#### useListDocuments

useListDocuments(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }List all documents accessible to you.

##### Parameters
 |
 | Name | Type | Description
 | params*required | undefined | ListDocumentsParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### usePermissionsV2

usePermissionsV2(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Load permissions.

##### Parameters
 |
 | Name | Type | Description
 | params*required | PermissionsParamsV2 | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useSetAppState

useSetAppState(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Updates app state

#### useSetUserAppState

useSetUserAppState(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Updates user app state

#### useSettings

⚠️ Deprecated
Use V2 instead.

useSettings(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Retrieve metadata and content for settings.

##### Parameters
 |
 | Name | Type | Description
 | paramsDEPRECATED*required | SettingsParams | Parameters for the client sdk call.
 | optionsDEPRECATED | HookOptions | Additional options for the react hook.

#### useSettingsObjects

⚠️ Deprecated
Use V2 instead.

useSettingsObjects(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Retrieve metadata and content for settings.

##### Parameters
 |
 | Name | Type | Description
 | paramsDEPRECATED*required | SettingsObjectParams | Parameters for the client sdk call.
 | optionsDEPRECATED | HookOptions | Additional options for the react hook.

#### useSettingsObjectsV2

useSettingsObjectsV2(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Retrieve metadata and content for settings.

##### Parameters
 |
 | Name | Type | Description
 | params*required | SettingsObjectParamsV2 | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useSettingsV2

useSettingsV2(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Retrieve metadata and content for settings.

##### Parameters
 |
 | Name | Type | Description
 | params*required | SettingsParamsV2 | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useTransferOwnershipV2

useTransferOwnershipV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Transfer ownership.

#### useUpdateAccessorPermissionsV2

useUpdateAccessorPermissionsV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Update accessor permissions.

#### useUpdateAllUsersPermissionsV2

useUpdateAllUsersPermissionsV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Update all-users permissions.

#### useUpdateDocument

useUpdateDocument(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Update metadata and content.

#### useUpdateDocumentMetadata

useUpdateDocumentMetadata(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Update document metadata

#### useUpdateSettings

⚠️ Deprecated
Use V2 instead.

useUpdateSettings(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Update metadata and content.

#### useUpdateSettingsV2

useUpdateSettingsV2(): { data, error, errorDetails, execute, isError, isLoading, isSuccess, status }Update metadata and content.

#### useUser

useUser(uuid,options): UseUserResultReact hook for fetching a single user by UUID.Internally batches multiple concurrent `useUser` calls into a single bulk
POST request to the IAM API, deduplicating UUIDs and chunking into batches
of ≤100 to avoid silent truncation.

##### Parameters
 |
 | Name | Type | Description
 | uuid*required | undefined | string | The user UUID to fetch, or `undefined` to disable the query.
 | options*required | UseUserOptions | Additional options for the hook.

##### Returns
 |
 | Description
 | The user data, loading state, and error information.Code example
`tsx
const { data: user, isLoading, error } = useUser('user-uuid-123');
`

#### useUserAppState

useUserAppState(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }Get user app state

##### Parameters
 |
 | Name | Type | Description
 | params*required | UserAppStateParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useUserAppStates

useUserAppStates(params,options?): { cancel, data, error, errorDetails, isError, isLoading, isSuccess, refetch, status }List user app states

##### Parameters
 |
 | Name | Type | Description
 | params*required | UserAppStatesParams | Parameters for the client sdk call.
 | options | HookOptions | Additional options for the react hook.

#### useUsers

useUsers(uuids,options): UseUsersResultReact hook for fetching multiple users by their UUIDs.Internally batches all UUID lookups into chunked bulk POST requests
to the IAM API (≤100 UUIDs per chunk), with per-UUID caching.

##### Parameters
 |
 | Name | Type | Description
 | uuids*required | Arraystring> | Array of user UUIDs to fetch.
 | options*required | UseUserOptions | Additional options for the hook.

##### Returns
 |
 | Description
 | Aggregated result with a Map of UUID→user data and loading states.Code example
`tsx
const { data, users, isLoading } = useUsers(['uuid-1', 'uuid-2', 'uuid-3']);
`

### Components

#### DqlQueryParamsProvider

Provider component for Dql query params context to use with the `useDql` hook.

##### Parameters
 |
 | Name | Type
 | props*required | DqlQueryParamsContextProps

### Functions

#### UseUsersProvider

UseUsersProvider(props): ReactElementany | string | JSXElementConstructorany>>Provider component for configuring the `useUser` and `useUsers` hooks.

##### Parameters
 |
 | Name | Type
 | props*required | UseUsersConfigCode example
`tsx
UseUsersProvider levelType="account" levelId="abc-123"> MyTable />/UseUsersProvider>
`

#### getGrailFieldsQueryOptions

getGrailFieldsQueryOptions(autocompleteOptions,dssOptions): GrailFieldsQueryOptionsCreates combined query options for both autocomplete and DSS queries used in useGrailFields.
This allows consumers to prefetch both queries in parallel.

##### Parameters
 |
 | Name | Type | Description
 | autocompleteOptions*required | AutocompleteQueryOptions | Options for the autocomplete query.
 | dssOptions*required | DssQueryOptions | Options for the DSS query.

##### Returns
 |
 | Description
 | An object containing query options for both autocomplete and DSS queries.Code example
`tsx
const queryClient = useQueryClient();const { autocomplete, dss } = getGrailFieldsQueryOptions( { query: 'fetch logs' }, { dataObject: 'logs' },);await Promise.all([ queryClient.prefetchQuery(autocomplete), queryClient.prefetchQuery(dss),]);
`

### Constants

#### DqlQueryParamsContext

Context storing Dql query params.
ContextDqlQueryParamsContextProps>

### Types

#### AnalyzerHookOptions

##### Properties

 |
 | Name | Type | Description
 | autoFetchDEPRECATED*required | boolean | If set to true, the hook will execute the query immediately. If set to false, the query only executes when calling refetch.
 | autoFetchOnUpdateDEPRECATED*required | boolean | If set to true, the hook will execute the query on a component update. If set to false, it is not executed on update.
 | onErrorDEPRECATED | (error: Error) => void |

#### AutocompleteQueryOptions

Options for the autocomplete query passed to useGrailFields.

##### Properties

 |
 | Name | Type | Description
 | enabled | boolean | Whether the query is enabled.
 | query*required | string | The DQL query string used to derive autocomplete field suggestions.
 | retry | number | boolean | Number of retries or boolean to indicate whether to retry on failure.
 | staleTime | number | Time in milliseconds before the query is considered stale.

#### DqlQueryParams

Parameters for query execution.

##### Properties

 |
 | Name | Type | Description
 | defaultSamplingRatio | number | Default sampling ratio. By default no sampling is applied. No upper limit but will be normalized to a power of 10 less than or equal to 100000.
 | defaultScanLimitGbytes | number | Default scan limit. Can be overridden in DQL. Default value is configured on application level (see documentation of FETCH command). No upper limit. Use -1 for no limit.
 | defaultTimeframeEnd | string | The query timeframe 'end' timestamp in ISO-8601 or RFC3339 format. If the timeframe 'start' parameter is missing, the whole timeframe is ignored. Note that if a timeframe is specified within the query string (query) then it has precedence over this query request parameter.
 | defaultTimeframeStart | string | The query timeframe 'start' timestamp in ISO-8601 or RFC3339 format. If the timeframe 'end' parameter is missing, the whole timeframe is ignored. Note that if a timeframe is specified within the query string (query) then it has precedence over this query request parameter.
 | dtClientContext | string | The dt-client-context header is an optional string parameter used for monitoring purposes. When included in a request, it helps retrieve information about the execution of the query. It shouldn't hold sensitive information.
 | enablePreview | boolean | Request preview results. If a preview is available within the requestTimeoutMilliseconds, then it will be returned as part of the response.
 | enforceQueryConsumptionLimit | boolean | (DEPRECATED use body parameter 'enforceQueryConsumptionLimit' instead) If set, query consumption limit will be enforced.
 | enrich | string | If set additional data will be available in the metadata section.
 | fetchTimeoutSeconds | number | The time limit for fetching data. Soft limit as further data processing can happen. No upper limit in API but application level default and maximum fetch timeout also applies.
 | filterSegments | FilterSegments | Represents a collection of filter segments.
 | includeContributions | boolean | Indicates whether bucket contribution information should be included in the query response metadata. When set to true, the response will contain details about how each bucket contributed to the query result.
 | includeTypes | boolean | Parameter to exclude the type information from the query result. In case not specified, the type information will be included.
 | locale | string | The query locale. If none specified, then a language/country neutral locale is chosen. The input values take the ISO-639 Language code with an optional ISO-3166 country code appended to it with an underscore. For instance, both values are valid 'en' or 'en_US'.
 | maxResultBytes | number | The maximum number of serialized result bytes. Applies to records only and is a soft limit, i.e. the last record that exceeds the limit will be included in the response completely. No upper limit, no default value.
 | maxResultRecords | number | The maximum number of returned query result records. No upper limit.
 | query*required | string | The full query string.
 | queryOptions | QueryOptions | Query options enhance query functionality for Dynatrace internal services.
 | requestTimeoutMilliseconds | number | The maximum time the response will be delayed to wait for a result. (This excludes the sending time and time spent in any services between the query-frontend and the client.) If the query finishes within the specified timeout, the query result is returned. Otherwise, the requestToken is returned, allowing polling for the result.
 | timezone | string | The query timezone. If none is specified, UTC is used as fallback. The list of valid input values matches that of the IANA Time Zone Database (TZDB). It accepts values in their canonical names like 'Europe/Paris', the abbreviated version like CET or the UTC offset format like '+01:00'

#### DqlQueryParamsContextProps

##### Properties

 |
 | Name | Type | Description
 | defaultSamplingRatio | number | Default sampling ratio. By default no sampling is applied. No upper limit but will be normalized to a power of 10 less than or equal to 100000.
 | defaultScanLimitGbytes | number | Default scan limit. Can be overridden in DQL. Default value is configured on application level (see documentation of FETCH command). No upper limit. Use -1 for no limit.
