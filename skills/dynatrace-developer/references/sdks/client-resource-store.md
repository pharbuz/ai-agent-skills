# @dynatrace-sdk/client-resource-store

Source: <https://developer.dynatrace.com/develop/sdks/client-resource-store/v1/> (latest: `client-resource-store/v1`).

## client-resource-store/v1

`/develop/sdks/client-resource-store/v1/`

- SDK for TypeScript
- Grail - Resource Store
- V1

## Grail - Resource Store
Documentation of the Dynatrace Resource Store API for Grail.
To read about use cases and examples, see
Dynatrace Documentation

 @dynatrace-sdk/client-resource-store v1.0.0 

`tsx
npm install @dynatrace-sdk/client-resource-store
`

### lookupDataClient

`tsx
import { lookupDataClient } from '@dynatrace-sdk/client-resource-store';
`

#### delete

lookupDataClient.delete(config): PromiseDelete file.

## Delete file
Delete a file from the Grail Resource Store.ATTENTION - This operation is irreversible.The request body needs to contain the request parameters (see below) in JSON format.

### Request parameters

- `filePath` (required) - The fully qualified file path of the file. Example: * /lookups/mydata*.

### Permissions
Required permissions: `storage:files:delete`

##### Parameters
 |
 | Name | Type
 | config.body*required | ResourceDeleteRequest

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | The requested file has been deleted successfully.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Bad request for deleting the file. | Unauthorized. | Access forbidden. | The file does not exist. | Internal Server Error | Client Error | Server ErrorCode example
`tsx
import { lookupDataClient } from "@dynatrace-sdk/client-resource-store";const data = await lookupDataClient.delete({ body: { filePath: "/lookups/mydata" },});
`

#### upload

lookupDataClient.upload(config): PromiseResourceUploadResponse>Upload lookup data

## Upload lookup data
Upload lookup data and store it as a new tabular file in the Grail Resource Store or replace an existing one.
The request body needs to be submitted as `multipart/form-data` with the following parts:

- request: containing the request parameters (see below) in JSON format

- content: containing the lookup data in text format
The uploaded data is parsed using the
Dynatrace Pattern Language (DPL).
For examples, see the Dynatrace Documentation.

### Request parameters

- `filePath` (required) - The fully qualified file path of the tabular file to store the
lookup
data in Grail. Example: /lookups/mydata. The following constraints apply:

- must only contain alphanumeric characters `[a-zA-Z0-9]`, `-`, `_`, `.`, `/`

- must start with `/lookups`

- must end with `[a-zA-Z0-9]`

- must contain at least two `/` characters

- between any two consecutive `/` characters there must be at least one `[a-zA-Z0-9]` character

- can be up to 500 characters long

- `overwrite` - If false and the file already exists, the upload fails. Set to true to allow
overwriting existing files. Default: false

- `displayName` - An optional name for the file. The length is limited to 500 characters.

- `description` - An optional description for the file. The length is limited to 500 characters.

- `parsePattern` (required) - The DPL pattern to parse the uploaded data. Every pattern match
produces a record. Example: `LD:id ',' LD:value`.

- `skippedRecords` - The number of initial records to discard. Can be used to skip header rows.
Default: 0

- `lookupField` (required) - The name of the lookup field whose value identifies a record in
the lookup data. The uniqueness of the values is ensured by deduplicating records during
upload, if necessary.

- `timezone` - The timezone for parsing time and date fields. The list of valid input values
matches that of the IANA Time Zone Database (TZDB). Example: UTC.

- `locale` - The locale for parsing locale-specific day and month names. The input values take the
ISO-639 Language code with an optional ISO-3166 country code appended to it with an underscore.
Example: en_US.

- `autoFlatten` - Set to true to extract nested fields to the root level when the specified DPL
pattern results in a single record-type field. Default: true

### Permissions
Required permissions: `storage:files:write`

##### Parameters
 |
 | Name | Type
 | config.body*required | ResourceUploadRequestEnvelope

##### Returns
 |
 | Return type | Status code | Description
 | ResourceUploadResponse | 200 | The requested table has been saved successfully.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Bad request for uploading the lookup data. | Unauthorized. | Access forbidden. | Conflict because the requested table already exists and `override` parameter was set to false. | The uploaded file or the JSON request were too large. | Too many concurrent requests. | Internal Server Error | Client Error | Server ErrorCode example
`tsx
import { lookupDataClient } from "@dynatrace-sdk/client-resource-store";const data = await lookupDataClient.upload({ body: { content: "...", request: { filePath: "/lookups/mydata", lookupField: "id", parsePattern: "LD:id ',' LD:value", }, },});
`

#### uploadToTestPattern

lookupDataClient.uploadToTestPattern(config): PromiseResourceTestPatternResponse>Test parsing lookup data without storing the result in the Grail Resource Store.

## Test parsing lookup data
Test parsing lookup data without storing the result in the Grail Resource Store.
The request body needs to be submitted as `multipart/form-data` with the following parts:

- request: containing the request parameters (see below) in JSON format

- content: containing the lookup data in text format
The uploaded data is parsed using the
Dynatrace Pattern Language (DPL).
For examples, see the Dynatrace Documentation.

### Request parameters

- `parsePattern` (required) - The DPL pattern to parse the uploaded data. Every pattern match
produces a record. Example: `LD:id ',' LD:value`.

- `skippedRecords` - The number of initial records to discard. Can be used to skip header rows.
Default: 0

- `lookupField` - The name of the lookup field whose value identifies a record in
the lookup data. The uniqueness of the values is ensured by deduplicating records during
upload, if necessary.

- `timezone` - The timezone for parsing time and date fields. The list of valid input values
matches that of the IANA Time Zone Database (TZDB). Example: UTC.

- `locale` - The locale for parsing locale-specific day and month names. The input values take the
ISO-639 Language code with an optional ISO-3166 country code appended to it with an underscore.
Example: en_US.

- `autoFlatten` - Set to true to extract nested fields to the root level when the specified DPL
pattern results in a single record-type field. Default: true

### Permissions
Required permissions: `storage:files:write`

##### Parameters
 |
 | Name | Type
 | config.body*required | ResourceTestPatternRequestEnvelope

##### Returns
 |
 | Return type | Status code | Description
 | ResourceTestPatternResponse | 200 | The result of applying the pattern to the uploaded file. The schema for the `records` and `types` is the same as in the DQL Query API.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Bad request for uploading the lookup data. | Unauthorized. | Access forbidden. | The uploaded file or the JSON request were too large. | Too many concurrent requests. | Internal Server Error | Client Error | Server ErrorCode example
`tsx
import { lookupDataClient } from "@dynatrace-sdk/client-resource-store";const data = await lookupDataClient.uploadToTestPattern({ body: { content: "...", request: { parsePattern: "LD:id ',' LD:value" }, },});
`

### Types

#### CustomValidationErrorInfo

 |
 | Name | Type
 | message*required | string

#### ErrorEnvelope

 |
 | Name | Type
 | error | ExceptionalReturn

#### ErrorInfo

 |
 | Name | Type
 | message*required | string

#### ExceptionalReturn

 |
 | Name | Type
 | code | number
 | errorDetails*required | ArrayCustomValidationErrorInfo | InvalidAuditEventsErrorInfo | MediaTypeErrorInfo | ParameterErrorInfo | ProxyErrorInfo | QueryFrontendRawErrorInfo | RequestBodyErrorInfo>
 | message*required | string

#### InvalidAuditEventsErrorInfo

 |
 | Name | Type
 | invalidAuditEventIndices*required | Arraynumber>
 | invalidEventIndices | Arraynumber>
 | message*required | string

#### MediaTypeErrorInfo

 |
 | Name | Type
 | message*required | string
 | supportedMediaTypes*required | Arraystring>

#### ParameterErrorInfo

 |
 | Name | Type
 | message*required | string
 | parameterDescriptor*required | string

#### ProxyErrorInfo

 |
 | Name | Type
 | message*required | string

#### QueryFrontendRawErrorInfo

 |
 | Name | Type
 | message*required | string
 | rawQueryFrontendResponse*required | string

#### RequestBodyErrorInfo

 |
 | Name | Type
 | bodyDescriptor*required | string
 | message*required | string

#### ResourceDeleteRequest

Request Details

 |
 | Name | Type | Description
 | filePath*required | string | The fully qualified file path of the tabular file to store the lookup data in Grail.

#### ResourceTestPatternRequest

The JSON metadata for the test pattern request.

 |
 | Name | Type | Description
 | autoFlatten | boolean | Set to true to extract nested fields to the root level when the specified DPL pattern results in a single record-type field. default: `true`
 | locale | string | The locale for parsing locale-specific day and month names. The input values take the ISO-639 Language code with an optional ISO-3166 country code appended to it with an underscore.
 | lookupField | string | The name of the lookup field whose value identifies a record in the lookup data.The uniqueness of the values is ensured by deduplicating records during upload, if necessary.
 | parsePattern*required | string | The DPL pattern to parse the uploaded data. Every pattern match produces a record.
 | skippedRecords | number | The number of initial records to discard. Can be used to skip header rows. default: `0`
 | timezone | string | The timezone for parsing time and date fields. The list of valid input values matches that of the IANA Time Zone Database (TZDB).

#### ResourceTestPatternRequestEnvelope

Multipart request containing JSON metadata and file content.

 |
 | Name | Type | Description
 | content*required | Binary |
 | request*required | ResourceTestPatternRequest | The JSON metadata for the test pattern request.

#### ResourceTestPatternResponse

The result of applying the pattern to the uploaded file.

 |
 | Name | Type | Description
 | numberOfRecords | number | The total number of records in the uploaded file that match the provided pattern.
 | records | ArrayResourceTestPatternResponseRecordsItem> | List of records that result from applying the pattern to the uploaded file. If there are more than 100 records, this list contains only the first 100.
 | types | ArrayResourceTestPatternResponseTypesItem> | The data types for the result records.

#### ResourceTestPatternResponseRecordsItem

List of records that result from applying the pattern to the uploaded file. If there are more than 100 records, this list contains only the first 100.

type: Record>

#### ResourceTestPatternResponseTypesItem

The data types for the result records.

type: Record>

#### ResourceUploadRequest

The JSON metadata for the upload request.

 |
 | Name | Type | Description
 | autoFlatten | boolean | Set to true to extract nested fields to the root level when the specified DPL pattern results in a single record-type field. default: `true`
 | description | string | An optional description for the file.
 | displayName | string | An optional name for the file.
 | filePath*required | string | The fully qualified file path of the tabular file to store the lookup data in Grail.
 | locale | string | The locale for parsing locale-specific day and month names. The input values take the ISO-639 Language code with an optional ISO-3166 country code appended to it with an underscore.
 | lookupField*required | string | The name of the lookup field whose value identifies a record in the lookup data.The uniqueness of the values is ensured by deduplicating records during upload, if necessary.
 | overwrite | boolean | If false and the file already exists, the upload fails. Set to true to allow overwriting existing files. default: `false`
 | parsePattern*required | string | The DPL pattern to parse the uploaded data. Every pattern match produces a record.
 | skippedRecords | number | The number of initial records to discard. Can be used to skip header rows. default: `0`
 | timezone | string | The timezone for parsing time and date fields. The list of valid input values matches that of the IANA Time Zone Database (TZDB).

#### ResourceUploadRequestEnvelope

Multipart request containing JSON metadata and file content.

 |
 | Name | Type | Description
 | content*required | Binary |
 | request*required | ResourceUploadRequest | The JSON metadata for the upload request.

#### ResourceUploadResponse

 |
 | Name | Type | Description
 | discardedDuplicates*required | number | The number of records that were discarded because their lookup field was not unique.
 | fileSize*required | number | The size of the tabular file in the resource store, in bytes.
 | patternMatches*required | number | The number of records in the uploaded file that match the parse pattern.
 | records*required | number | The number of records in the final lookup data.
 | skippedRecords*required | number | The number of records that were skipped, based on the skippedRecords parameter in the request.
 | uploadedBytes*required | number | The number of bytes that were sent in the request content.
