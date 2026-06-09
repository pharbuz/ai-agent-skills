# @dynatrace-sdk/client-bucket-management

Source: <https://developer.dynatrace.com/develop/sdks/client-bucket-management/v3/> (latest: `client-bucket-management/v3`).

## client-bucket-management/v3

`/develop/sdks/client-bucket-management/v3/`

- SDK for TypeScript
- Grail - Storage Management
- V3

## Grail Storage Management API
This API allows you to manage storage for Grail. Data is organizied in buckets. To get familiar
with the data model within Grail check the Grail data model documentation.

### Access Management

### Entpoint permissions

There are 4 permissions that are enabling the management of the Grail bucket storage. More about
Grail storage permissions can be read in the documentation.

`storage:bucket-definitions:read`

`storage:bucket-definitions:write`

`storage:bucket-definitions:delete`

`storage:bucket-definitions:truncate`

### Storage Object Modification

### Optimistic Locking Version

Operations which modify buckets use mandatory optimistic locking.
When such operations are executed, the user must provide the version upon which they operate.
The version can be found in the JSON within the response of
GET bucket definitions or GET bucket definition.

If the document version in the service doesn't match, because the document has been modified in
the meantime, then the operation gets rejected.

### Storage Object creation

Creating a custom storage bucket can have benefits in terms of data management.
Read more about custom buckets.

Bucket creation can take up to 1 minute.

To create a new custom Grail bucket with Storage Management you need to specify:

- A unique bucket name

- It has to be between 3-100 characters long and start with a letter.

- The bucket name can only contain

- lowercase alphanumeric characters [ a - z ]

- underscores [ _ ] and

- hyphens [ - ].

- Bucket name can not start with

- default_

- dt_.

The bucket name can't be edited or changed at a later time.

Display name. You can use this field to describe your bucket.

Retention period in days between 1 day - 3657 days (10 years).

 @dynatrace-sdk/client-bucket-management v3.7.1 

`tsx
npm install @dynatrace-sdk/client-bucket-management
`

### bucketDefinitionsClient

`tsx
import { bucketDefinitionsClient } from '@dynatrace-sdk/client-bucket-management';
`

#### createBucket

bucketDefinitionsClient.createBucket(config): PromiseBucket>Create a new bucketCreate a new custom bucket.Bucket creation can take up to 1 minute.Required permission: `storage:bucket-definitions:write`To create a new custom Grail bucket with Storage Management you need to specify the following values:

### Allowed JSON values

bucketName defines the name of the bucket. The bucket name can't be edited or changed
at a later time.

must be unique

has to be between 3-100 characters long and has to start with a letter

can only contain

lowercase alphanumeric characters [ a - z ]

underscores [ _ ] and

hyphens [ - ].

must not start with

default_

dt_

table name of the table this bucket is assigned to. Currently allowed
one of [logs, events, bizevents, spans, security.events, user.sessions, user.events].

retentionDays describes the data retention period in days between 1 day - 3657 days (10
years + 1 week).

displayName Optional field that can be used to describe the bucket. Length of the field
is limited to 200 characters.

bucketClass Optional field that can be used to specify the bucket class.
Allowed values are `live` and `historic`. If not specified, the bucket class will be set to `live` by default.

##### Parameters
 |
 | Name | Type
 | config.body*required | CreateBucket

##### Returns
 |
 | Return type | Status code | Description
 | Bucket | 201 | Successfully created bucket definition

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissions | Bucket already existsCode example
`tsx
import { bucketDefinitionsClient } from "@dynatrace-sdk/client-bucket-management";const data = await bucketDefinitionsClient.createBucket({ body: { bucketName: "custom_logs", table: "logs", displayName: "Custom logs bucket", retentionDays: 35, includedQueryLimitDays: 0, },});
`

#### deleteBucket

bucketDefinitionsClient.deleteBucket(config): PromiseBucket>Delete a bucket

## ATTENTION - This operation is irreversible
Delete can be used to delete a bucket. This operation will remove the content of a given bucket and then delete the bucket itself.Delete is an asynchronous task. Runtime will depend on the amount of data that has to be removed.The status of this operation can be tracked via the status field within the [GET bucket definitions]
(#operations-Bucket_Definitions-getDefinitions)
or GET bucket definition.
Status will show deleting as long as data will be drained and finally the bucket will be deleted. Afterwards the bucket will cease to exist.Operation can be executed on all types of buckets except buckets where bucketName starts with dt_ or default_.Before a bucket is deleted, checks are performed to verify that the bucket is not in use.Required permission: `storage:bucket-definitions:delete`

##### Parameters
 |
 | Name | Type | Description
 | config.bucketName*required | string | Bucket name to delete.

##### Returns
 |
 | Return type | Status code | Description
 | Bucket | 202 | accepted delete bucket

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | Forbidden | bucket not found | The operation cannot proceed due to a conflict.Code example
`tsx
import { bucketDefinitionsClient } from "@dynatrace-sdk/client-bucket-management";const data = await bucketDefinitionsClient.deleteBucket({ bucketName: "...",});
`

#### getDefinition

bucketDefinitionsClient.getDefinition(config): PromiseBucket>Get bucket definition by nameGet a bucket definition by name.Newly created buckets aren't shown immediately, this can take up to one minute.Required permission: `storage:bucket-definitions:read`

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | add-fields: Define additional fields added to the response.

 Depending on the field this may result in longer response times:

- `records` - Request number of records stored in a bucket.
- `estimatedUncompressedBytes` - Request estimated uncompressed size of a bucket.
- `estimatedUncompressedBytesQueryIncluded` - Request estimated uncompressed size of query-included data in a bucket.
- `estimatedUncompressedBytesOnDemand` - Request estimated uncompressed size of on-demand data in a bucket. Note: Hold down STRG on Windows/Linux or Command on Mac to select multiple values in the box below.
 | config.bucketName*required | string | Bucket name to get definition for.

##### Returns
 |
 | Return type | Status code | Description
 | Bucket | 200 | Successfully retrieved bucket definition.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissions | Bucket with provided name was not found.Code example
`tsx
import { bucketDefinitionsClient } from "@dynatrace-sdk/client-bucket-management";const data = await bucketDefinitionsClient.getDefinition({ bucketName: "...",});
`

#### getDefinitions

bucketDefinitionsClient.getDefinitions(config): PromiseBuckets>Get all bucket definitionsGet all bucket definitions.Newly created buckets aren't shown immediately, this can take up to one minute.Required permission: `storage:bucket-definitions:read`

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | add-fields: Define additional fields added to the response.

 Depending on the field this may result in longer response times:

- `records` - Request number of records stored in a bucket.
- `estimatedUncompressedBytes` - Request estimated uncompressed size of a bucket.
- `estimatedUncompressedBytesQueryIncluded` - Request estimated uncompressed size of query-included data in a bucket.
- `estimatedUncompressedBytesOnDemand` - Request estimated uncompressed size of on-demand data in a bucket. Note: Hold down STRG on Windows/Linux or Command on Mac to select multiple values in the box below.

##### Returns
 |
 | Return type | Status code | Description
 | Buckets | 200 | Successfully retrieved all bucket definitions

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissionsCode example
`tsx
import { bucketDefinitionsClient } from "@dynatrace-sdk/client-bucket-management";const data = await bucketDefinitionsClient.getDefinitions();
`

#### truncateBucket

bucketDefinitionsClient.truncateBucket(config): PromiseTruncate a bucket

## ATTENTION - This operation is irreversibly
Truncate can be used to empty a bucket. This operation will remove the content of a given bucket.Truncate is an asyncronous task. Runtime will depend on the amount of data that has to be removed.Operation can be executed on all types of buckets.Required permission: `storage:bucket-definitions:truncate`

##### Parameters
 |
 | Name | Type | Description
 | config.bucketName*required | string | Bucket name to truncate.

##### Returns
 |
 | Return type | Status code | Description
 | void | 202 | Accepted truncate bucket

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | Forbidden | Bucket not found | Server not readyCode example
`tsx
import { bucketDefinitionsClient } from "@dynatrace-sdk/client-bucket-management";const data = await bucketDefinitionsClient.truncateBucket({ bucketName: "...",});
`

#### updateBucket

bucketDefinitionsClient.updateBucket(config): PromiseUpdate a bucketUpdate a bucket definition.The following fields can be changed:

- displayName can be used to describe your bucket (up to 200 characters)

- retentionDays defines how long the data in the bucket will be retained
Warning: changing the retention days will also apply to existing records. Shortening the retention period could result in data deletion.Add the field(s) to be updated to the request body.Required permission: `storage:bucket-definitions:write`

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | UpdateBucket |
 | config.bucketName*required | string | Bucket name to update
 | config.optimisticLockingVersion*required | number | optimistic-locking-version defines the base version that this update applies to. You can get the current version of a bucket definition by checking the version field in the JSON response of GET bucket definitions or GET bucket definition.

 ATTENTION: this optimistic-locking-version and the version value in the JSON body must match.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Successfully updated bucket definition
 | void | 202 | Accepted update bucket definition

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | Forbidden | Bucket with provided name was not found | Attempt to update an old version or an operation is currently in progress that prevents current modifications (creating, deleting, updating)Code example
`tsx
import { bucketDefinitionsClient } from "@dynatrace-sdk/client-bucket-management";const data = await bucketDefinitionsClient.updateBucket({ bucketName: "...", optimisticLockingVersion: 10, body: { bucketName: "custom_logs", table: "logs", displayName: "Custom logs bucket (updated)", status: "active", retentionDays: 10, includedQueryLimitDays: 0, version: 1, },});
`

#### updateBucketPartially

bucketDefinitionsClient.updateBucketPartially(config): PromiseUpdate a bucket partiallyUpdate a bucket definition.There are to fields that can be changed

- displayName can be used to describe your bucket (up to 200 characters)

- retentionDays defines the period in days
Warning: changing the retention days will also apply to existing records. Shortening the
retention period could result in data deletion.Add the field(s) to be updated to the request body.Required permission: `storage:bucket-definitions:write`

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | PartialUpdateBucket |
 | config.bucketName*required | string | Bucket name to update.
 | config.optimisticLockingVersion*required | number | optimistic-locking-version defines the base version that this update applies to. You can get the current version of a bucket definition by checking the version field in the JSON response of GET bucket definitions or GET bucket definition.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Successfully updated bucket definition
 | void | 202 | Accepted update bucket definition

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | Forbidden | Bucket with provided name was not found | Attempt to update an old version or an operation is currently in progress that prevents current modifications (creating, deleting, updating)Code example
`tsx
import { bucketDefinitionsClient } from "@dynatrace-sdk/client-bucket-management";const data = await bucketDefinitionsClient.updateBucketPartially({ bucketName: "...", optimisticLockingVersion: 10, body: { displayName: "Custom logs bucket (updated)", retentionDays: 10, includedQueryLimitDays: 0, }, });
`

### Types

#### Bucket

 |
 | Name | Type | Description
 | bucketClass | null | "live" | "historic" | The class of the bucket. Read-only after creation.
 | bucketName*required | string | The unique identifier of the bucket within the tenant.
Pattern: `([a-z])([a-z0-9])([a-z0-9_-])+`
 | displayName | null | string | Descriptive name of the bucket. No restriction regarding unique naming or valid characters.
 | estimatedUncompressedBytes | null | number | Estimated uncompressed size of the bucket in bytes.
 | estimatedUncompressedBytesOnDemand | null | number | Estimated uncompressed size of on-demand data in the bucket in bytes.
 | estimatedUncompressedBytesQueryIncluded | null | number | Estimated uncompressed size of query-included data in the bucket in bytes.
 | includedQueryLimitDays*required | number | The period in days in which queries from the bucket are included in the pricing model.
 | metricInterval | null | "PT1S" | "PT5S" | "PT10S" | "PT1M" | "PT5M" | "PT15M" | "PT1H" | Interval of aggregated metric data. Only applies to metric buckets.
 | records | null | number | Amount of records in the bucket.
 | retentionDays*required | number | The retention period in days of the data in the bucket.
 | status*required | "creating" | "active" | "updating" | "deleting" | The current status of the bucket, depending on bucket lifecycle.
 | table*required | string | Name of the table the bucket is assigned to.
 | updatable*required | boolean | A flag indicating whether a bucket can be updated or not.
 | version*required | number | Optimistic locking version. Update requests define with this on which version the data updated is based on. This must match with the version stored, otherwise the update will fail due to concurrent modification.

#### Buckets

 |
 | Name | Type
 | buckets*required | ArrayBucket>

#### CreateBucket

 |
 | Name | Type | Description
 | bucketClass | null | "live" | "historic" | Classification of the bucket. Determines the ingest mode. Allowed values: live, historic. Defaults to live if not specified. Historic buckets are only supported for table 'logs'.
 | bucketName*required | string | The unique identifier of the bucket within the tenant.
Pattern: `([a-z])([a-z0-9])([a-z0-9_-])+`
 | displayName | null | string | Descriptive name of the bucket. No restriction regarding unique naming or valid characters.
 | includedQueryLimitDays | null | number | The period in days in which queries from the bucket are included in the pricing model.
 | includedQueryLimitDaysOrDefault | number |
 | metricInterval | null | "PT1M" | "PT5M" | "PT15M" | "PT1H" | Interval of aggregated metric data. Only applies to metric buckets.
 | retentionDays*required | null | number | The retention period in days of the data in the bucket.
 | retentionDaysOrDefault | number |
 | table*required | string | Name of the table the bucket is assigned to. One of [logs, events, bizevents, spans, security.events, user.sessions, user.events]

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

#### PartialUpdateBucket

 |
 | Name | Type | Description
 | displayName | null | string | Descriptive name of the bucket. No restriction regarding unique naming or valid characters.
 | includedQueryLimitDays | null | number | The period in days in which queries from the bucket are included in the pricing model.
 | retentionDays | null | number | The retention period in days of the data in the bucket. Important note: the new retention days will also apply to existing records. Shortening the retention period could result in data deletion!

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

#### UpdateBucket

 |
 | Name | Type | Description
 | bucketClass | null | "live" | "historic" | The class of the bucket. Read-only after creation.
 | bucketName*required | string | The unique identifier of the bucket within the tenant.
Pattern: `([a-z])([a-z0-9])([a-z0-9_-])+`
 | displayName | null | string | Descriptive name of the bucket. No restriction regarding unique naming or valid characters.
 | includedQueryLimitDays | null | number | The period in days in which queries from the bucket are included in the pricing model.
 | includedQueryLimitDaysOrDefault | number |
 | metricInterval | null | "PT1M" | "PT5M" | "PT15M" | "PT1H" | Metric interval for metric buckets. Will be ignored for other buckets.
 | retentionDays | null | number | The retention period in days of the data in the bucket. Important note: the new retention days will also apply to existing records. Shortening the retention period could result in data deletion!
 | retentionDaysOrDefault | number |
 | status*required | "creating" | "active" | "updating" | "deleting" | The current status of the bucket, depending on bucket lifecycle.
 | table*required | string | Name of the table the bucket is assigned to.
 | version | null | number | Optimistic locking version. Update requests define with this on which version the data updated is based on. This must match with the version stored, otherwise the update will fail due to concurrent modification.
 | versionOrDefault | number |

### Enums

#### BucketBucketClass

⚠️ Deprecated
Use literal values.

The class of the bucket. Read-only after creation.

##### Enum keys
`Historic` | `Live`

#### BucketMetricInterval

⚠️ Deprecated
Use literal values.

Interval of aggregated metric data. Only applies to metric buckets.

##### Enum keys
`Pt10S` | `Pt15M` | `Pt1H` | `Pt1M` | `Pt1S` | `Pt5M` | `Pt5S`

#### BucketStatus

⚠️ Deprecated
Use literal values.

The current status of the bucket, depending on bucket lifecycle.

##### Enum keys
`Active` | `Creating` | `Deleting` | `Updating`

#### CreateBucketBucketClass

⚠️ Deprecated
Use literal values.

Classification of the bucket. Determines the ingest mode.
Allowed values: live, historic. Defaults to live if not specified.
Historic buckets are only supported for table 'logs'.

##### Enum keys
`Historic` | `Live`

#### CreateBucketMetricInterval

⚠️ Deprecated
Use literal values.

Interval of aggregated metric data. Only applies to metric buckets.

##### Enum keys
`Pt15M` | `Pt1H` | `Pt1M` | `Pt5M`

#### GetDefinitionQueryAddFieldsItem

⚠️ Deprecated
Use literal values.

##### Enum keys
`EstimatedUncompressedBytes` | `EstimatedUncompressedBytesOnDemand` | `EstimatedUncompressedBytesQueryIncluded` | `Records`

#### GetDefinitionsQueryAddFieldsItem

⚠️ Deprecated
Use literal values.

##### Enum keys
`EstimatedUncompressedBytes` | `EstimatedUncompressedBytesOnDemand` | `EstimatedUncompressedBytesQueryIncluded` | `Records`

#### UpdateBucketBucketClass

⚠️ Deprecated
Use literal values.

The class of the bucket. Read-only after creation.

##### Enum keys
`Historic` | `Live`

#### UpdateBucketMetricInterval

⚠️ Deprecated
Use literal values.

Metric interval for metric buckets. Will be ignored for other buckets.

##### Enum keys
`Pt15M` | `Pt1H` | `Pt1M` | `Pt5M`

#### UpdateBucketStatus

⚠️ Deprecated
Use literal values.

The current status of the bucket, depending on bucket lifecycle.

##### Enum keys
`Active` | `Creating` | `Deleting` | `Updating`
