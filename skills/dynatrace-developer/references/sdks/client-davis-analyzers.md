# @dynatrace-sdk/client-davis-analyzers

Source: <https://developer.dynatrace.com/develop/sdks/client-davis-analyzers/v1/> (latest: `client-davis-analyzers/v1`).

## client-davis-analyzers/v1

`/develop/sdks/client-davis-analyzers/v1/`

- SDK for TypeScript
- Davis® AI - Predictive and Causal
- V1

## Davis® AI - Predictive and Causal
Note"Dynatrace Intelligence" is the umbrella term for all AI in Dynatrace, including generative, agentic, causal, and predictive AI. It replaces "Davis AI" and "Davis CoPilot" and expands upon their capabilities. The terms "Davis" and "CoPilot" persist in certain locations, including APIs, Swagger, scopes, and Grail. These references are still relevant for Dynatrace Intelligence.
This SDK allows you to interact with Dynatrace Intelligence predictive and causal AI for customized AI/ML analysis.

Refer to the service documentation to get familiar with the key concepts.

 @dynatrace-sdk/client-davis-analyzers v1.10.0 

`tsx
npm install @dynatrace-sdk/client-davis-analyzers
`

### analyzersClient

`tsx
import { analyzersClient } from '@dynatrace-sdk/client-davis-analyzers';
`

#### cancelAnalyzerExecution

analyzersClient.cancelAnalyzerExecution(config): PromiseAnalyzerCancelResult>Stop a started analyzer execution.Required scope: davis:analyzers:executeUse the request token that was returned when starting an analyzer execution to cancel it.

##### Parameters
 |
 | Name | Type | Description
 | config.analyzerName*required | string | The name of the analyzer.
 | config.requestToken*required | string | The request token is returned when starting a long-running analyzer execution. It can be used to do follow-up operations like polling and cancelling.

##### Returns
 |
 | Return type | Status code | Description
 | AnalyzerCancelResult | 200 | The current analyzer execution status and an optional partial result.
 | void | 202 | The cancel request was accepted and is being processed.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | Invalid or malformed request. | Insufficient permissions. | No analyzer available with the requested name. | The analyzer result with the request token has already been consumed or its time-to-live (TTL) has been reached. The result is not available anymore. | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.cancelAnalyzerExecution({ analyzerName: "...", requestToken: "RHluYXRyYWNlMjAyMw==",});
`

#### executeAnalyzer

analyzersClient.executeAnalyzer(config): PromiseAnalyzerExecuteResult>Execute an analyzer with the given input.Required scope: davis:analyzers:executeThe analyzer execution is started asynchronously.
If the result is not available after the specified timeout, a request token is returned
to poll for the result. Otherwise, the final result is directly available and no request token is returned.Depending on the chosen analyzer and the analyzer input, additional scopes might be required, e.g.
`storage:buckets:read` and `storage:metrics:read` to enable the analyzer to read time series data from Grail™.

##### Parameters
 |
 | Name | Type | Description
 | config.analyzerName*required | string | The name of the analyzer.
 | config.body*required | AnalyzerInput |
 | config.enablePreview | boolean | Indicates if analyzer results should preview already created outputs while the analyzer is still running.

 Set to false if only the final result is needed.
 | config.timeoutSeconds | number | The amount of seconds to wait for the response to be returned.

 The timeout controls how long the client is willing to wait, while the analyzer execution continues running until it has finished or is cancelled.

##### Returns
 |
 | Return type | Status code | Description
 | AnalyzerExecuteResult | 200 | The final analyzer result and execution status.
 | AnalyzerExecuteResult | 202 | The current analyzer execution status and a request token and time-to-live (TTL) to continue polling the result with.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | Invalid or malformed request. | Insufficient permissions. | No analyzer available with the requested name. | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.executeAnalyzer({ analyzerName: "...", body: { timeSeriesData: { expression: "timeseries avg(dt.host.cpu.usage)", }, forecastHorizon: 10, },});
`

#### getAnalyzer

analyzersClient.getAnalyzer(config): PromiseAnalyzerDefinitionDetails>Get the analyzer definition for an analyzer.Required scope: davis:analyzers:readAll available meta-information for the analyzer is returned.

##### Parameters
 |
 | Name | Type | Description
 | config.analyzerName*required | string | The name of the analyzer.

##### Returns
 |
 | Return type | Status code | Description
 | AnalyzerDefinitionDetails | 200 | The definition of the requested analyzer.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | Invalid or malformed request. | Insufficient permissions. | No analyzer available with the requested name. | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.getAnalyzer({ analyzerName: "...",});
`

#### getAnalyzerDocumentation

analyzersClient.getAnalyzerDocumentation(config): PromiseGet the documentation for an analyzer.Required scope: davis:analyzers:readA documentation may provide further information and context for a given analyzer.
Not all analyzers provide documentation.The documentation is returned as Markdown.

##### Parameters
 |
 | Name | Type | Description
 | config.analyzerName*required | string | The name of the analyzer.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | The documentation of the requested analyzer.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | Invalid or malformed request. | Insufficient permissions. | No analyzer available with the requested name. | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.getAnalyzerDocumentation( { analyzerName: "..." },);
`

#### getJsonSchemaForInput

analyzersClient.getJsonSchemaForInput(config): Promisestring | any>>Get the JSON schema for an analyzer input.Required scope: davis:analyzers:readThe JSON schema defines a standardized declaration of the input structure,
providing well-defined input documentation that is both human- and machine-readable.

##### Parameters
 |
 | Name | Type | Description
 | config.analyzerName*required | string | The name of the analyzer.
 | config.config | "DEFAULT" | "LLM" | The configuration for the JSON schema generation.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | The JSON input schema of the requested analyzer.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | Invalid or malformed request. | Insufficient permissions. | No analyzer available with the requested name. | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.getJsonSchemaForInput({ analyzerName: "...",});
`

#### getJsonSchemaForResult

analyzersClient.getJsonSchemaForResult(config): Promisestring | any>>Get the JSON schema for an analyzer result.Required scope: davis:analyzers:readThe JSON schema defines a standardized declaration of the output structure,
providing well-defined output documentation that is both human- and machine-readable.

##### Parameters
 |
 | Name | Type | Description
 | config.analyzerName*required | string | The name of the analyzer.
 | config.config | "DEFAULT" | "LLM" | The configuration for the JSON schema generation.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | The JSON result schema of the requested analyzer.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | Invalid or malformed request. | Insufficient permissions. | No analyzer available with the requested name. | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.getJsonSchemaForResult({ analyzerName: "...",});
`

#### pollAnalyzerExecution

analyzersClient.pollAnalyzerExecution(config): PromiseAnalyzerPollResult>Poll for the result of a started analyzer execution.Required scope: davis:analyzers:executeUse the request token returned when starting an analyzer execution to poll for a result.The `executionStatus` of the result indicates if the analyzer execution is already completed.
While the status is `RUNNING`, wait and poll for the result again in subsequent calls.

##### Parameters
 |
 | Name | Type | Description
 | config.analyzerName*required | string | The name of the analyzer.
 | config.requestToken*required | string | The request token is returned when starting a long-running analyzer execution. It can be used to do follow-up operations like polling and cancelling.
 | config.timeoutSeconds | number | The amount of seconds to wait for the response to be returned.

 The timeout controls how long the client is willing to wait, while the analyzer execution continues running until it has finished or is cancelled.

##### Returns
 |
 | Return type | Status code | Description
 | AnalyzerPollResult | 200 | The current analyzer execution status and an optional partial result.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | Invalid or malformed request. | Insufficient permissions. | No analyzer available with the requested name. | The analyzer result with the request token has already been consumed or its time-to-live (TTL) has been reached. The result is not available anymore. | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.pollAnalyzerExecution({ analyzerName: "...", requestToken: "RHluYXRyYWNlMjAyMw==",});
`

#### queryAnalyzers

analyzersClient.queryAnalyzers(config): PromiseAnalyzerQueryResult>Query all available analyzer definitions.Required scope: davis:analyzers:readThe analyzer definition contains meta-information about an analyzer, including its input and output structure:

- The `input` definition specifies which fields the analyzer accepts, some of which may be required.

- The `output` definition specifies how the returned analyzer result is structured.

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | string | Specify which meta-information to fetch in addition to the default fields `name`, `displayName` and `description`.

 Valid values are:

- `analyzerCall`
- `baseAnalyzer`
- `category`
- `input`
- `labels`
- `output`
- `type` Any other field will result in a HTTP 400 response.
 | config.filter | string | Use the `filter` parameter to only fetch a subset of analyzer definitions.

 When using the operators `=`and `!=`, filtering is case sensitive.

 The following operators are supported:

- `=`
- `!=`
- `contains`
- `starts-with`
- `ends-with`
- `and`
- `or` Parenthesis and the `not` operator are currently not supported.

 The following fields are valid filtering parameters:

- `baseAnalyzer`
- `description`
- `displayName`
- `labels`
- `name`
- `type` Any other field will result in a HTTP 400 response.
 | config.pageKey | string | The cursor for the page of results. Find it in the `nextPageKey` field of the previous response.

 If the `page-key` parameter is used, no other query parameters must be provided.

 If not provided, the first page is always returned.
 | config.pageSize | number | The amount of returned analyzer definitions in a single response payload. By default, 50 is used. The maximum is 200.

##### Returns
 |
 | Return type | Status code | Description
 | AnalyzerQueryResult | 200 | All available analyzer definitions.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | Insufficient permissions. | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.queryAnalyzers();
`

#### validateAnalyzerExecution

analyzersClient.validateAnalyzerExecution(config): PromiseAnalyzerValidationResult>Validate the provided input for an analyzer execution.Required scope: davis:analyzers:executeProvide the same input that is planned to be used for an analyzer execution to have it validated without
executing the analyzer.

##### Parameters
 |
 | Name | Type | Description
 | config.analyzerName*required | string | The name of the analyzer.
 | config.body*required | AnalyzerInput |

##### Returns
 |
 | Return type | Status code | Description
 | AnalyzerValidationResult | 200 | The validation result for the requested analyzer execution.

##### Throws
 |
 | Error Type | Error Message
 | AnalyzerErrorEnvelopeError | No analyzer available with the requested name. | Insufficient permissions. | Not found | Client error. | Internal server error.Code example
`tsx
import { analyzersClient } from "@dynatrace-sdk/client-davis-analyzers";const data = await analyzersClient.validateAnalyzerExecution({ analyzerName: "...", body: {}, });
`

### Types

#### AnalyzerCancelResult

Result of cancelling the analyzer execution. Only returned if the result completes while cancelling.

 |
 | Name | Type | Description
 | requestToken | string | The request token is returned when starting a long-running analyzer execution. It can be used to do follow-up operations like polling and cancelling.
 | result*required | AnalyzerResult |
 | ttlInSeconds | number | Time-to-live until the result is not available anymore.

#### AnalyzerCategory

The category of an analyzer used to logically group different analyzers.

 |
 | Name | Type
 | displayName*required | string

#### AnalyzerData

The map of actual data matching the input and output definition of the analyzer.

type: Record

#### AnalyzerDefinition

The definition of the analyzer. It describes which input and output data the analyzer accepts
and produces when being executed.

 |
 | Name | Type | Description
 | baseAnalyzer | string | The analyzer name that the current analyzer is based on. All input and output parameters are inherited. Additional parameters may be present in the current analyzer.
 | category | AnalyzerCategory | The category of an analyzer used to logically group different analyzers.
 | description | string | Detailed description of the analyzers' functionality. Get the documentation of the analyzer for more information.
 | displayName*required | string |
 | input | ArrayParameterDefinition> |
 | labels | Arraystring> | A list of string-based labels to group and mark different analyzers.
 | name*required | string | The uniquely identifying name of the analyzer.
 | output | ArrayParameterDefinition> |
 | type | "IMPLEMENTED" | "INTERFACE" | The type of the analyzer.

- IMPLEMENTED: Analyzers which have an implementation and can be executed.
- INTERFACE: Just an interface to be implemented or extended by other analyzer definitions.

#### AnalyzerDefinitionDetails

The definition of the analyzer. It describes which input and output data the analyzer accepts
and produces when being executed.

 |
 | Name | Type | Description
 | baseAnalyzer | string | The analyzer name that the current analyzer is based on. All input and output parameters are inherited. Additional parameters may be present in the current analyzer.
 | category | AnalyzerCategory | The category of an analyzer used to logically group different analyzers.
 | description | string | Detailed description of the analyzers' functionality. Get the documentation of the analyzer for more information.
 | displayName*required | string |
 | input | ArrayParameterDefinition> |
 | labels | Arraystring> | A list of string-based labels to group and mark different analyzers.
 | name*required | string | The uniquely identifying name of the analyzer.
 | output | ArrayParameterDefinition> |
 | type | "IMPLEMENTED" | "INTERFACE" | The type of the analyzer.

- IMPLEMENTED: Analyzers which have an implementation and can be executed.
- INTERFACE: Just an interface to be implemented or extended by other analyzer definitions.

#### AnalyzerDimensionalData

A list of resolved dimensional data.

 |
 | Name | Type | Description
 | query*required | DimensionQuery | A query for dimensional data such as timeseries, entities, or logs.
 | type*required | "entityId" | "timeseriesArray" | The type of the dimensional query.
 | value*required | AnalyzerDimensionalDataValue | The resolved value of the dimensional query.

#### AnalyzerError

The error that is returned for unsuccessful responses.

 |
 | Name | Type | Description
 | code*required | number | The HTTP status code of the error.
 | details | AnalyzerErrorDetails |
 | message*required | string |

#### AnalyzerErrorDetails

 |
 | Name | Type
 | constraintViolations | ArrayConstraintViolation>

#### AnalyzerErrorEnvelope

 |
 | Name | Type | Description
 | error | AnalyzerError | The error that is returned for unsuccessful responses.

#### AnalyzerExecuteResult

Result of the analyzer execution.

 |
 | Name | Type | Description
 | requestToken | string | The request token is returned when starting a long-running analyzer execution. It can be used to do follow-up operations like polling and cancelling.
 | result*required | AnalyzerResult |
 | ttlInSeconds | number | Time-to-live until the result is not available anymore.

#### AnalyzerExecutionLog

 |
 | Name | Type | Description
 | level*required | "TRACING" | "INFO" | "WARNING" | "SEVERE" | Determines the severity of the log.
 | message*required | string |
 | path | string | A path pointing to the source of the error in the input. The format of the path follows the JSON path specification.

#### AnalyzerGeneralParameters

Parameters that are present in all analyzer input parameter definitions.

 |
 | Name | Type | Default
 | logVerbosity | "TRACING" | "INFO" | "WARNING" | "SEVERE" | `"WARNING"`
 | resolveDimensionalQueryData | boolean | `false`
 | timeframe | Timeframe |

#### AnalyzerInput

The input is specific to an analyzer. Get the definition of the analyzer to retrieve the required input structure.

 |
 | Name | Type | Description
 | generalParameters | AnalyzerGeneralParameters | Parameters that are present in all analyzer input parameter definitions.

#### AnalyzerOutput

The output is specific to an analyzer. Get the definition of the analyzer to retrieve the required output structure.

 |
 | Name | Type | Description
 | system | AnalyzerOutputSystemParameters | Parameters that are present in all analyzer output parameter definitions.

#### AnalyzerOutputLog

 |
 | Name | Type
 | level*required | "TRACING" | "INFO" | "WARNING"
 | message*required | string

#### AnalyzerOutputSystemParameters

Parameters that are present in all analyzer output parameter definitions.

 |
 | Name | Type
 | logs | ArrayAnalyzerOutputLog>

#### AnalyzerPollResult

Result of polling the analyzer execution.

 |
 | Name | Type | Description
 | requestToken | string | The request token is returned when starting a long-running analyzer execution. It can be used to do follow-up operations like polling and cancelling.
 | result*required | AnalyzerResult |
 | ttlInSeconds | number | Time-to-live until the result is not available anymore.

#### AnalyzerQueryResult

The list of available analyzers.

 |
 | Name | Type | Description
 | analyzers*required | ArrayAnalyzerDefinition> |
 | nextPageKey | string | The key that should be used to do follow-up requests, fetching the remaining analyzers. If the last page is reached or all analyzers are already listed, this field is omitted.
 | totalCount*required | number | The total amount of analyzers available opposed to the current page size.

#### AnalyzerResult

 |
 | Name | Type | Description
 | data | ArrayAnalyzerDimensionalData> |
 | executionStatus*required | "RUNNING" | "ABORTED" | "COMPLETED" |
 | input*required | AnalyzerInput | The input is specific to an analyzer. Get the definition of the analyzer to retrieve the required input structure.
 | logs | ArrayAnalyzerExecutionLog> |
 | output*required | ArrayAnalyzerOutput> |
 | resultId*required | string | The uniquely identifying ID of the result. Used for logging.
 | resultStatus*required | "SUCCESSFUL" | "SUCCESSFUL_WITH_WARNINGS" | "FAILED" |

#### AnalyzerValidationResult

The result of the dry-execution of the analyzer.

 |
 | Name | Type | Description
 | details | AnalyzerErrorDetails |
 | valid*required | boolean | Whether the analyzer can be successfully executed with the given input data.

#### ConstraintViolation

A constraint violation indicating why an error has occurred.

 |
 | Name | Type | Description
 | level*required | "TRACING" | "INFO" | "WARNING" | "SEVERE" | Determines the severity of the log.
 | message*required | string |
 | path | string | A path pointing to the source of the error in the input. The format of the path follows the JSON path specification.

#### EnumerationElement

An object that has a fixed set of possible values differentiated by the `key` property.

 |
 | Name | Type
 | description*required | string
 | displayName*required | string
 | key*required | string

#### ParameterDefinition

The definition for a single parameter, describing its name and other meta information.

 |
 | Name | Type | Description
 | advanced | boolean | If true, this parameter is considered to be for advanced usage.
 | array*required | boolean | Whether this parameter can have an array of values. Passing a single, non-array value is also allowed.
 | defaultValue | any | The default value used when the parameter is omitted.
 | description | string |
 | displayName*required | string |
 | enumerationValues | ArrayEnumerationElement> |
 | extendedType | string | Provides extended type information for this parameter. This allows additional semantics that can be utilized by analyzer consumers.
 | fields | ArrayParameterDefinition> | Given the parameter is of type `structure` this property contains the sub-definition of the parameter.
 | maxSize | number | The maximum number of elements if the parameter is an array.
 | name*required | string |
 | optional*required | boolean | Whether this parameter can be omitted when executing the analyzer.
 | type*required | "string" | "number" | "boolean" | "timeseriesArray" | "analyzerStructure" | "dimensionQuery" | "enumeration" | "integer" | "timeframe" | "timeseriesQuery" | "timestamp" | The type of the parameter, indicating the format of the value to be provided.
 | valueConstraints | ParameterDefinitionValueConstraints | Defines value constraints for string or number parameters. Not applicable to other parameter types.

#### Timeframe

 |
 | Name | Type | Description
 | endTime | string | Specify the end time in either absolute or relative format. For absolute format, use the ISO 8601 format (yyyy-MM-ddTHH:mm:ssZ). For relative format, use 'now' for the current time or apply an offset with the available units: 's' for seconds, 'm' for minutes, 'h' for hours, and 'd' for days. For example, use 'now-2h' or '-2h' for a relative offset of 2 hours. If not specified, defaults to now.
 | startTime*required | string | Specify the start time in either absolute or relative format. For absolute format, use the ISO 8601 format (yyyy-MM-ddTHH:mm:ssZ). For relative format, use 'now' for the current time or apply an offset with the available units: 's' for seconds, 'm' for minutes, 'h' for hours, and 'd' for days. For example, use 'now-2h' or '-2h' for a relative offset of 2 hours.

#### DimensionQuery

A query for dimensional data such as timeseries, entities, or logs.

type: string | object

### Enums

#### AnalyzerDefinitionType

⚠️ Deprecated
Use literal values.

The type of the analyzer.

- IMPLEMENTED: Analyzers which have an implementation and can be executed.

- INTERFACE: Just an interface to be implemented or extended by other analyzer definitions.

##### Enum keys
`Implemented` | `Interface`

#### AnalyzerDimensionalDataType

⚠️ Deprecated
Use literal values.

The type of the dimensional query.

##### Enum keys
`EntityId` | `TimeseriesArray`

#### AnalyzerExecutionLogLevel

⚠️ Deprecated
Use literal values.

Determines the severity of the log.

##### Enum keys
`Info` | `Severe` | `Tracing` | `Warning`

#### AnalyzerOutputLogLevel

⚠️ Deprecated
Use literal values.

##### Enum keys
`Info` | `Tracing` | `Warning`

#### AnalyzerResultExecutionStatus

⚠️ Deprecated
Use literal values.

##### Enum keys
`Aborted` | `Completed` | `Running`

#### AnalyzerResultResultStatus

⚠️ Deprecated
Use literal values.

##### Enum keys
`Failed` | `Successful` | `SuccessfulWithWarnings`

#### JsonSchemaConfig

⚠️ Deprecated
Use literal values.

The configuration for the JSON schema generation:

- `DEFAULT` - Use the standard JSON schema generation (recommended for most clients).

- `LLM` - Generate a schema optimized for LLM consumption.

##### Enum keys
`Default` | `Llm`

#### ParameterDefinitionType

⚠️ Deprecated
Use literal values.

The type of the parameter, indicating the format of the value to be provided.

##### Enum keys
`AnalyzerStructure` | `Boolean` | `DimensionQuery` | `Enumeration` | `Integer` | `Number` | `String` | `Timeframe` | `TimeseriesArray` | `TimeseriesQuery` | `Timestamp`
