# @dynatrace-sdk/client-query

Source: <https://developer.dynatrace.com/develop/sdks/client-query/v1/> (latest: `client-query/v1`).

> Truncated — this SDK's auto-generated reference is large. Key exports/usage are below; see the full reference at the URL above.

## client-query/v1

`/develop/sdks/client-query/v1/`

- SDK for TypeScript
- DQL Query
- V1

## Grail DQL Query API
Exposes an API to fetch records stored in Grail

 @dynatrace-sdk/client-query v1.26.0 

`tsx
npm install @dynatrace-sdk/client-query
`

### queryAssistanceClient

`tsx
import { queryAssistanceClient } from '@dynatrace-sdk/client-query';
`

#### queryAutocomplete

queryAssistanceClient.queryAutocomplete(config): PromiseAutocompleteResponse>Get a structured list of suggestions for the query at the given position.For information about the required permissions see the Bucket and table permissions in Grail documentation.

### Overview
We provide a list of suggestions that may be used after the cursor position. The following queries will all provide the
same results:

- `query: "f"`

- `query: "f", cursorPosition:1`

- `query: "fetch ", cursorPosition:1`
Available fields: |
 | Field | Description
 | suggestions | a list of suggestions. Each item is a separate possible suggestion, despite they might have the same outputs.
 | optional | whether the suggestion is optional. If `true`, the query until the cursor position might work. If `false`, the query is definitely incomplete or invalid if cut at the cursor position.Fields in the `suggestions` |
 | Field | Description
 | suggestion | a string representing the whole suggestion. This information could also be derived from the parts.
 | alreadyTypedCharacters | how many characters of this suggestion have already been typed (and will be overridden by the suggestion).
 | parts | a list of semantically enriched information on what are the parts of a suggestion.Fields in `parts` |
 | Field | Description
 | suggestion | a string representing the current part of the suggestion.
 | type | current types: SPACE, PIPE, COMMAND (may be extended)The `type` helps to treat specific parts of the suggestion different to others; either by a different visualization,
a link to docs, etc.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | AutocompleteRequest |
 | config.dtClientContext | string | The dt-client-context header is an optional string parameter used for monitoring purposes. When included in a request, it helps retrieve information about the execution of the query. It shouldn't hold sensitive information.

##### Returns
 |
 | Return type | Description
 | PromiseAutocompleteResponse> | A list of structured autocomplete suggestions.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Bad Request - The caller submitted an invalid request (e.g., mandatory parameters missing).
 | Unauthorized | Unauthorized. The request lacks valid authentication credentials. Happens when the authentication token is missing or invalid.
 | InsufficientPermission | Insufficient permissions.
 | TenantNotFound | Not Found - Returned when the tenant is inactive or not found.
 | MethodNotAllowed | Method not allowed. The HTTP method is not supported for this endpoint.
 | UnsupportedMediaType | Unsupported media type. The request content type is not supported.
 | InternalServerError | An internal server error has occurred.
 | ServiceUnavailable | Service Unavailable - The grail instance is either shutting down or busy.
 | GatewayTimeout | Gateway timeout. The service did not respond in time.Code example
`tsx
import { queryAssistanceClient } from "@dynatrace-sdk/client-query";const data = await queryAssistanceClient.queryAutocomplete({ body: { query: 'fetch events | filter event.type == "davis" AND davis.status != "CLOSED" | fields timestamp, davis.title, davis.underMaintenance, davis.status | sort timestamp | limit 10', },});
`

#### queryParse

queryAssistanceClient.queryParse(config): PromiseDQLNode>Get a structured tree of the canonical form of the query.For information about the required permissions see the Bucket and table permissions in Grail documentation.

### Overview
Returns the parsed query as a tree, containing the structure of the canonical query. Tree-nodes can contain references to
the token position where they originate from. This may help to provide hover effects, show canonical forms, mark
optional items, and more.

### Details
The query tree consists of nodes that contain different additional information (everything optional):

#### General Fields
 |
 | Field | Mandatory | Description
 | tokenPosition | no | optional. If present, it represents the position within the query string where the node refers to.
 | isOptional | no | whether this node could be left out and the result would still be the same query (semantically).

##### tokenPosition
contains `start` (inclusive) and `end` (inclusive), both contain `index` (0 based; fur substrings), `line`
and `column` (both 1-based; for readability).

- If `tokenPosition` is present, it always contains start and end with all fields

- If `tokenPosition` is not present, there might still be nested nodes that do contain a position

- If `start == end`, the position refers to a single character

- If `start > end`, we know for sure that something was inserted.
We can always check whether the canonical representation of a node matches the text in the tokenPosition to see whether
something was inserted, removed, or changed.

##### isOptional
only present if it is true.Optional nodes can e.g. be optional braces that make a query more readable, but are not necessary. This could be used to
enter ghost braces and implicit functions in the user's input field; maybe with different formatting
(using the tokenPosition of sibling nodes we can also check whether the user wrote these or not).

#### Advanced Token Types
each node is of one of following types and may contain more fields:

- Terminal Node

- ContainerNode

- Alternative Node

##### Terminal Node
can be identified by checking whether `canonicalString` is present |
 | Field | Mandatory | Description
 | type | yes | the type of the terminal node - do not confuse with the type of container nodes
 | canonicalString | yes | the canonical string representation. Concatenating the canonicalString of all nested terminal nodes provides the canonical form of the query.
 | isMandatoryOnUserOrder | no | may only be present if (`type="BRACE_OPEN"` or `type="BRACE_CLOSE"`) and `isOptional=true`. For usage see section Special node type: PARAMETERS

###### Current types of terminal nodes (list might grow):

- SPACE

- LINEBREAK

- INDENT

- PIPE

- DOT

- COLON

- COMMA

- BRACE_OPEN

- BRACE_CLOSE

- BRACKET_OPEN

- BRACKET_CLOSE

- PARENTHESIS_OPEN

- PARENTHESIS_CLOSE

- QUOTE

- SLASH

- BOOLEAN_TRUE

- BOOLEAN_FALSE

- NULL

- COMMAND_NAME

- PARAMETER_KEY

- PARAMETER_VALUE_SCOPE

- FUNCTION_NAME

- OPERATOR

- TRAVERSAL_OPERATOR

- TRAVERSAL_RELATION_NAME

- TRAVERSAL_HOP_COUNT

- SIMPLE_IDENTIFIER

- NUMBER

- STRING

- TIME_UNIT

- TIMESTAMP_VALUE

- METRIC_KEY

- VARIABLE

##### ContainerNode
can be identified by checking whether `children` is present |
 | Field | Mandatory | Description
 | type | yes | the type of the container node - do not confuse with the type of terminal nodes
 | children | yes | the children for the node. might be of any type

###### Current types of container nodes (list might grow):

- QUERY

- EXECUTION_BLOCK

- COMMAND

- COMMAND_SEPARATOR

- PARAMETER_WITH_KEY

- GROUP

- PARAMETERS - check examples further down

- PARAMETER_NAMING

- PARAMETER_SEPARATOR

- FUNCTION

- FUNCTION_PART - check examples further down

- EXPRESSION

- IDENTIFIER

- SOURCE_ID

- DURATION

- TIMESTAMP

- TIMEFRAME

- TRAVERSAL_PATH

- TRAVERSAL_STEP

###### Special node type: PARAMETERS
can contain children representing the parameters. Every second child is of type PARAMETER_SEPARATOR.You may reorder the children based on their tokenPosition to get the user order. However, in this case,
you need to consider `isMandatoryOnUserOrder` to determine whether the grouping braces are mandatory or not.

###### Example
For the query `SORT a, {direction:"descending", b}`, the canonical form is:`SORT a, {b, direction:"descending"}`This is the order, in which the parameters are returned in the query tree.
Parameters are {a} and {{b} and {direction:"descending"}}. In this case, the braces are optional.`SORT a, {b, direction:"descending"}` is equivalent to `SORT a, b, direction:"descending"`However, if you reorder the children by tokenPosition, the braces are not optional, because`SORT a, direction:"descending", b` is interpreted as `SORT {a, direction:"descending"}, b`So, if the children in PARAMETERS are re-ordered by tokenPosition, braces (or in general: TerminalNodes)
are only optional if `isOptional && !isMandatoryOnUserOrder`.

###### Special node type: FUNCTION_PART
A container node of type `FUNCTION` may contain nodes of type `FUNCTION_PART`.If those `FUNCTION_PART`s are marked as optional, this means you have to either include all or none of these
optional function parts.Example:`filter anyMatch(a.b == 1, input:a)`The optional function parts are `anyMatch(` and `, input:a)`. If you leave out both, the command will still work:
`filter a.b == 1` and return the same result. Using one of these optional function parts and removing the other will lead
to an invalid query.

##### Alternative Node
can be identified by checking whether `alternatives` is present |
 | Field | Mandatory | Description
 | alternatives | yes | Type: MapWhen displaying the query, pick one option. You may use the other options for hovering, replacing, and more.

###### Current values of AlternativeType (list might grow):

- CANONICAL: This node is the one we will use for our canonical form

- USER: An alternative that is also valid, but not canonical; and this version was picked by the user.

- INFO: only if the canonical version is not present
Examples:

- `CANONICAL` is not present, `USER` is present: user's nodes are optional, but not canonical (usually optional nodes
are still canonical)

- `CANONICAL` is present, `USER` is not present: same as if the canonical node was optional. If this happens, it is
likely that there is also an `INFO` node

- `CANONICAL` is present, `USER` is present: there are different alternatives

- `INFO` is present: usually if `CANONICAL` is not present (e.g. the parameter key for `FILTER a == 1`), there is an info node
for `FILTER condition:a == 1`. This `condition:` was neither written by the user nor is it canonical; but it might be
used to help the user understand what this parameter means.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | ParseRequest |
 | config.dtClientContext | string | The dt-client-context header is an optional string parameter used for monitoring purposes. When included in a request, it helps retrieve information about the execution of the query. It shouldn't hold sensitive information.

##### Returns
 |
 | Return type | Description
 | PromiseDQLNode> | A node containing more nodes, a node offering different (semantically equivalent) versions of the query parts, or a terminal node that shows the canonical form.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | The supplied request is wrong. Either the query itself or other parameters are wrong.
 | Unauthorized | Unauthorized. The request lacks valid authentication credentials. Happens when the authentication token is missing or invalid.
 | InsufficientPermission | Insufficient permissions.
 | MethodNotAllowed | Method not allowed. The HTTP method is not supported for this endpoint.
 | UnsupportedMediaType | Unsupported media type. The request content type is not supported.
 | InternalServerError | An internal server error has occurred.
 | ServiceUnavailable | Service Unavailable - The grail instance is either shutting down or busy.
 | GatewayTimeout | Gateway timeout. The service did not respond in time.Code example
`tsx
import { queryAssistanceClient } from "@dynatrace-sdk/client-query";const data = await queryAssistanceClient.queryParse({ body: { query: 'fetch events | filter event.type == "davis" AND davis.status != "CLOSED" | fields timestamp, davis.title, davis.underMaintenance, davis.status | sort timestamp | limit 10', },});
`

#### queryVerify

queryAssistanceClient.queryVerify(config): PromiseVerifyResponse>Verifies a query without executing it.For information about the required permissions see the Bucket and table permissions in Grail documentation.

### Overview
Verifies the supplied query string and other query parameters for lack of any errors, but without actually
submitting the query for execution.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | VerifyRequest |
 | config.dtClientContext | string | The dt-client-context header is an optional string parameter used for monitoring purposes. When included in a request, it helps retrieve information about the execution of the query. It shouldn't hold sensitive information.

##### Returns
 |
 | Return type | Description
 | PromiseVerifyResponse> | Supplied query and parameters were verified.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | The supplied request is wrong. Either the query itself or other parameters are wrong.
 | Unauthorized | Unauthorized. The request lacks valid authentication credentials. Happens when the authentication token is missing or invalid.
 | InsufficientPermission | Insufficient permissions.
 | MethodNotAllowed | Method not allowed. The HTTP method is not supported for this endpoint.
 | UnsupportedMediaType | Unsupported media type. The request content type is not supported.
 | InternalServerError | An internal server error has occurred.
 | ServiceUnavailable | Service Unavailable - The grail instance is either shutting down or busy.
 | GatewayTimeout | Gateway timeout. The service did not respond in time.Code example
`tsx
import { queryAssistanceClient } from "@dynatrace-sdk/client-query";const data = await queryAssistanceClient.queryVerify({ body: { query: 'fetch events | filter event.type == "davis" AND davis.status != "CLOSED" | fields timestamp, davis.title, davis.underMaintenance, davis.status | sort timestamp | limit 10', },});
`

### queryExecutionClient

`tsx
import { queryExecutionClient } from '@dynatrace-sdk/client-query';
`

#### queryCancel

queryExecutionClient.queryCancel(config): PromiseQueryPollResponse>Cancels the query and returns the result if the query was already finished, otherwise discards it.For information about the required permissions see the Bucket and table permissions in Grail documentation.

#### Overview:
Cancels a running Grail query and returns a list of records if the query already finished.

#### The response format:
If the query was already finished, a response body including the result will be returned. Otherwise the response will contain no body.The result has three main sections:

- the 'records' section contains the individual records, where each record consists of a set of fields and their corresponding values.

- the 'types' section describes the corresponding data types that a record field has.

- the 'metadata' section contains information about the query like 'analysisTimeframe', 'timezone' or 'locale'.
Every record has an implicit 'index' according to the position in the 'records' JSON array.
The types section has a list of 1..N possible type 'buckets'. Each such bucket has an 'indexRange' which indicates which
records will find their field types in which bucket. The index range has two values start & end and can be thought of as [startIndex, endIndex).A field part of a record with index 'i' will find its corresponding field type by first locating the bucket that satisfies:
`tsx
startIndex
`
Once the bucket is found the 'mappings' object has an entry for all the fields that are part of that record with index 'i'.Since enforcement of a particular schema is absent at ingestion time, it is possible to have records that share the same
field name but their values are of a different type. This phenomenon will hence forth be named as a "collision".
When a collision does occur, we will create a new type 'bucket' that will have a different index range where
the new record field types will be placed.
It is guaranteed that every field of every record will have a corresponding type.
Clients should always take the included types into account when consuming records!

##### Parameters
 |
 | Name | Type | Description
 | config.dtClientContext | string | The dt-client-context header is an optional string parameter used for monitoring purposes. When included in a request, it helps retrieve information about the execution of the query. It shouldn't hold sensitive information.
 | config.enrich | string | If set additional data will be available in the metadata section.
 | config.requestToken*required | string | The request-token of the query.

##### Returns
 |
 | Return type | Description
 | PromiseQueryPollResponse | void> | The query already finished.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | The supplied request is wrong. Either the query itself or other parameters are wrong.
 | Unauthorized | Unauthorized. The request lacks valid authentication credentials. Happens when the authentication token is missing or invalid.
 | InsufficientPermission | Insufficient permissions.
 | QueryNotFound | Not Found - The query with the given ID does not exist for this tenant.
 | MethodNotAllowed | Method not allowed. The HTTP method is not supported for this endpoint.
 | QueryGone | The query for the given request-token is not available anymore.
 | UnsupportedMediaType | Unsupported media type. The request content type is not supported.
 | TooManyRequests | Too Many Requests - There were too many queries in the queue.
 | InternalServerError | An internal server error has occurred.
 | ServiceUnavailable | Service Unavailable - The grail instance is either shutting down or busy.
 | GatewayTimeout | Gateway timeout. The service did not respond in time.Code example
`tsx
import { queryExecutionClient } from "@dynatrace-sdk/client-query";const data = await queryExecutionClient.queryCancel({ requestToken: "...",});
`

#### queryExecute

queryExecutionClient.queryExecute(config): PromiseQueryStartResponse>Starts a Grail query.For information about the required permissions see the Bucket and table permissions in Grail documentation.

#### Overview:
Executes a query and returns a list of records.For details about the query language see the Dynatrace Query Language documentation.

#### The response format:
The json response will contain the state of the started query. If the query succeeded, the result will be included. Otherwise the response will contain a request token to reference the query in future polling requests.The result has two main sections:

- The 'records' section contains the individual records, where each record consists of a set of fields and their corresponding values.

- The 'types' section describes the corresponding data types that a record field has.
Every record has an implicit 'index' according to the position in the 'records' JSON array.
The types section has a list of 1..N possible type 'buckets'. Each such bucket has an 'indexRange' which indicates which
records will find their field types in which bucket. The index range has two values start & end and can be thought of as [startIndex, endIndex).A field part of a record with index 'i' will find its corresponding field type by first locating the bucket that satisfies:
`tsx
startIndex
`
Once the bucket is found the 'mappings' object has an entry for all the fields that are part of that record with index 'i'.Since enforcement of a particular schema is absent at ingestion time, it is possible to have records that share the same
field name but their values are of a different type. This phenomenon will hence forth be named as a "collision".
When a collision does occur, we will create a new type 'bucket' that will have a different index range where
the new record field types will be placed.
It is guaranteed that every field of every record will have a corresponding type.
Clients should always take the included types into account when consuming records!

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | ExecuteRequest |
 | config.dtClientContext | string | The dt-client-context header is an optional string parameter used for monitoring purposes. When included in a request, it helps retrieve information about the execution of the query. It shouldn't hold sensitive information.
 | config.enrich | string | If set additional data will be available in the metadata section.

##### Returns
 |
 | Return type | Description
 | PromiseQueryStartResponse> | The final status and results of the supplied query if it finished within a supplied requestTimeoutMilliseconds. | The status of the query to start.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | The supplied request is wrong. Either the query itself or other parameters are wrong.
 | Unauthorized | Unauthorized. The request lacks valid authentication credentials. Happens when the authentication token is missing or invalid.
 | InsufficientPermission | Insufficient permissions.
 | TenantNotFound | Not Found - Returned when the tenant is inactive or not found.
 | MethodNotAllowed | Method not allowed. The HTTP method is not supported for this endpoint.
 | Conflict | Conflict - The supplied queryId already exists and is currently running.
 | UnsupportedMediaType | Unsupported media type. The request content type is not supported.
 | TooManyRequests | Too Many Requests - There were too many queries in the queue.
 | InternalServerError | An internal server error has occurred.
 | ServiceUnavailable | Service Unavailable - The grail instance is either shutting down or busy.
 | GatewayTimeout | Gateway timeout. The service did not respond in time.Code example
`tsx
import { queryExecutionClient } from "@dynatrace-sdk/client-query";const data = await queryExecutionClient.queryExecute({ body: { query: 'fetch events | filter event.type == "davis" AND davis.status != "CLOSED" | fields timestamp, davis.title, davis.underMaintenance, davis.status | sort timestamp | limit 10', },});
`

#### queryPoll

queryExecutionClient.queryPoll(config): PromiseQueryPollResponse>Retrieves query status and final result from Grail.For information about the required permissions see the Bucket and table permissions in Grail documentation.

#### Overview:
Polls the status of a Grail query. Returns the status of the query, including the result if the query finished.

#### The response format:
The json response will contain the state of the query. If the query succeeded, the result will be included.The result has two main sections:

- The 'records' section contains the individual records, where each record consists of a set of fields and their corresponding values.

- The 'types' section describes the corresponding data types that a record field has.
Every record has an implicit 'index' according to the position in the 'records' JSON array.
The types section has a list of 1..N possible type 'buckets'. Each such bucket has an 'indexRange' which indicates which
records will find their field types in which bucket. The index range has two values start & end and can be thought of as [startIndex, endIndex).A field part of a record with index 'i' will find its corresponding field type by first locating the bucket that satisfies:
`tsx
startIndex
`
Once the bucket is found the 'mappings' object has an entry for all the fields that are part of that record with index 'i'.Since enforcement of a particular schema is absent at ingestion time, it is possible to have records that share the same
field name but their values are of a different type. This phenomenon will hence forth be named as a "collision".
When a collision does occur, we will create a new type 'bucket' that will have a different index range where
the new record field types will be placed.
It is guaranteed that every field of every record will have a corresponding type.
Clients should always take the included types into account when consuming records!

##### Parameters
 |
 | Name | Type | Description
 | config.dtClientContext | string | The dt-client-context header is an optional string parameter used for monitoring purposes. When included in a request, it helps retrieve information about the execution of the query. It shouldn't hold sensitive information.
 | config.enrich | string | If set additional data will be available in the metadata section.
 | config.requestTimeoutMilliseconds | number | Time the response is allowed to be delayed for either a preview or the final result to become available. No default value (immediate response).
 | config.requestToken*required | string | The request-token of the query.

##### Returns
 |
 | Return type | Description
 | PromiseQueryPollResponse> | The current status and results of the supplied query.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | The supplied request is wrong. Either the query itself or other parameters are wrong.
 | Unauthorized | Unauthorized. The request lacks valid authentication credentials. Happens when the authentication token is missing or invalid.
 | InsufficientPermission | Insufficient permissions.
 | QueryNotFound | Not Found - The query with the given ID does not exist for this tenant.
 | MethodNotAllowed | Method not allowed. The HTTP method is not supported for this endpoint.
 | QueryGone | The query for the given request-token is not available anymore.
 | UnsupportedMediaType | Unsupported media type. The request content type is not supported.
 | TooManyRequests | Too Many Requests - There were too many queries in the queue.
 | InternalServerError | An internal server error has occurred.
 | ServiceUnavailable | Service Unavailable - The grail instance is either shutting down or busy.
 | GatewayTimeout | Gateway timeout. The service did not respond in time.Code example
`tsx
import { queryExecutionClient } from "@dynatrace-sdk/client-query";const data = await queryExecutionClient.queryPoll({ requestToken: "...",});
`

### Types

#### AutocompleteRequest

 |
 | Name | Type | Description
 | cursorPosition | number | No upper limit but must be lower than length of query. No default value.
 | enforceQueryConsumptionLimit | boolean | Boolean to indicate if the query consumption limit should be enforced
 | locale | string | The query locale. If none specified, then a language/country neutral locale is chosen. The input values take the ISO-639 Language code with an optional ISO-3166 country code appended to it with an underscore. For instance, both values are valid 'en' or 'en_US'.
 | maxDataSuggestions | number | Limit the number of data suggestions, such as field names. No upper limit. No default value.
 | query*required | string | The full query string.
 | queryOptions | QueryOptions | Query options enhance query functionality for Dynatrace internal services.
 | timezone | string | The query timezone. If none is specified, UTC is used as fallback. The list of valid input values matches that of the IANA Time Zone Database (TZDB). It accepts values in their canonical names like 'Europe/Paris', the abbreviated version like CET or the UTC offset format like '+01:00'

#### AutocompleteResponse

The response of the autocomplete call.

 |
 | Name | Type | Description
 | optional*required | boolean | True if the suggestions are optional.
 | suggestedTtlSeconds | number | Suggested duration in seconds, for how long the response may be cached and reused by the client. It is derived from the volatility of the suggestions on the server (if the suggestions are static, how long the server will cache the volatile suggestions, ...). If not provided, then the result may be cached for long time. Value below 1 means that the result should not be cached.
 | suggestions*required | ArrayAutocompleteSuggestion> | The list of suggestions.

#### AutocompleteSuggestion

Single suggestion for completion of the query.

