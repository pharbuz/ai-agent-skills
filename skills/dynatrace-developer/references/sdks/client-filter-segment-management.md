# @dynatrace-sdk/client-filter-segment-management

Source: <https://developer.dynatrace.com/develop/sdks/client-filter-segment-management/v1/> (latest: `client-filter-segment-management/v1`).

## client-filter-segment-management/v1

`/develop/sdks/client-filter-segment-management/v1/`

- SDK for TypeScript
- Grail Storage Filter-Segments
- V1

## Grail Filter Segments API
Filter-Segment Management for Grail.

Slice, dice and contextualize your data to make it easier to find, understand and work with.

 @dynatrace-sdk/client-filter-segment-management v1.8.1 

`tsx
npm install @dynatrace-sdk/client-filter-segment-management
`

### filterSegmentsClient

`tsx
import { filterSegmentsClient } from '@dynatrace-sdk/client-filter-segment-management';
`

#### createFilterSegment

filterSegmentsClient.createFilterSegment(config): PromiseDetailedFilterSegment>Create a new filter-segment.Create a new segment and define data.Required scopes:

- `storage:filter-segments:write`

- `storage:filter-segments:share` if `isPublic` is set to `true`

#### New Filter-Segment
Provide a name and an optional description for the filter-segment.

##### Variables
Create variables to apply in your filter-segment data filters

##### Includes (Segment data)
Include all data that should be accessible when applying the filter-segment

##### IsPublic (Visibility)

- `false`: The filter-segment is private and only visible to the owner

- `true`: The filter-segment is visible to everyone in the environment

##### Parameters
 |
 | Name | Type
 | config.body*required | NewFilterSegment

##### Returns
 |
 | Return type | Status code | Description
 | DetailedFilterSegment | 201 | Filter-segment successfully created.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Filter-segment Bad Request. | unauthorized | missing permissionsCode example
`tsx
import { filterSegmentsClient } from "@dynatrace-sdk/client-filter-segment-management";const data = await filterSegmentsClient.createFilterSegment( { body: { name: "dev_environment", description: "only includes data of the dev environment", variables: { type: "query", value: "fetch logs | limit 1", }, isPublic: false, includes: [ { filter: '{"type":"Group","range":{"from":0,"to":19},"logicalOperator":"AND","explicit":false,"children":[{"type":"Statement","range":{"from":0,"to":19},"key":{"type":"Key","textValue":"content","value":"content","range":{"from":0,"to":7}},"operator":{"type":"ComparisonOperator","textValue":"=","value":"=","range":{"from":8,"to":9}},"value":{"type":"String","textValue":"\\"[debug]\\"","value":"[debug]","range":{"from":10,"to":19},"isEscaped":true}}]}', dataObject: "logs", }, { filter: '{"type":"Group","range":{"from":0,"to":18},"logicalOperator":"AND","explicit":false,"children":[{"type":"Statement","range":{"from":0,"to":18},"key":{"type":"Key","textValue":"content","value":"content","range":{"from":0,"to":7}},"operator":{"type":"ComparisonOperator","textValue":"=","value":"=","range":{"from":8,"to":9}},"value":{"type":"String","textValue":"\\"[info]\\"","value":"[info]","range":{"from":10,"to":18},"isEscaped":true}}]}', dataObject: "events", }, ], }, },);
`

#### deleteFilterSegment

filterSegmentsClient.deleteFilterSegment(config): PromiseDelete a filter-segment.Remove the filter-segment from the environment for all users.Required scopes:

- `storage:filter-segments:delete`

##### Parameters
 |
 | Name | Type | Description
 | config.filterSegmentUid*required | string | UID of the filter-segment

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | Filter-segment successfully deleted.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissions | Not found: the server cannot find the requested filter-segment.Code example
`tsx
import { filterSegmentsClient } from "@dynatrace-sdk/client-filter-segment-management";const data = await filterSegmentsClient.deleteFilterSegment( { filterSegmentUid: "D82a1jdA23a" },);
`

#### getFilterSegment

filterSegmentsClient.getFilterSegment(config): PromiseDetailedFilterSegment>Get filter-segment by UID.Get filter-segment by its UID.Required scopes:

- `storage:filter-segments:read`

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | null | Array | Add additional fields.
 | config.filterSegmentUid*required | string | UID of the filter-segment

##### Returns
 |
 | Return type | Status code | Description
 | DetailedFilterSegment | 200 | Filter-segment successfully retrieved.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissions | Not found: the server cannot find the requested filter-segment.Code example
`tsx
import { filterSegmentsClient } from "@dynatrace-sdk/client-filter-segment-management";const data = await filterSegmentsClient.getFilterSegment({ filterSegmentUid: "D82a1jdA23a",});
`

#### getFilterSegments

filterSegmentsClient.getFilterSegments(config): PromiseFilterSegments>Get all filter-segments.Returns all filter-segments.
If details like description are not needed then consider using the `:lean` endpoint.Required scopes:

- `storage:filter-segments:read`

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | null | Array | Add additional fields.

##### Returns
 |
 | Return type | Status code | Description
 | FilterSegments | 200 | Filter-segments successfully retrieved.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissionsCode example
`tsx
import { filterSegmentsClient } from "@dynatrace-sdk/client-filter-segment-management";const data = await filterSegmentsClient.getFilterSegments();
`

#### getFilterSegmentsEntityModel

filterSegmentsClient.getFilterSegmentsEntityModel(config): PromiseFilterSegmentNamespaceDto>Get filter-segment-entity-model.Returns the filter-segment-entity-model.Required scopes:

- `storage:filter-segments:read`

##### Returns
 |
 | Return type | Status code | Description
 | FilterSegmentNamespaceDto | 200 | Filter-segments-entity-model successfully retrieved.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissionsCode example
`tsx
import { filterSegmentsClient } from "@dynatrace-sdk/client-filter-segment-management";const data = await filterSegmentsClient.getFilterSegmentsEntityModel();
`

#### getLeanFilterSegments

filterSegmentsClient.getLeanFilterSegments(config): PromiseLeanFilterSegments>Get all filter-segments in a minimal/lean form.Returns all filter-segments in a minimal representational form. This endpoint saves resources
and as a result quicker response times can be expected over the more detailed get-all
endpoint.Required scopes:

- `storage:filter-segments:read`

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | null | Array | Add additional fields.

##### Returns
 |
 | Return type | Status code | Description
 | LeanFilterSegments | 200 | Filter-segments successfully retrieved.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissionsCode example
`tsx
import { filterSegmentsClient } from "@dynatrace-sdk/client-filter-segment-management";const data = await filterSegmentsClient.getLeanFilterSegments();
`

#### partiallyUpdateFilterSegment

filterSegmentsClient.partiallyUpdateFilterSegment(config): PromisePartially update a filter-segment.Update one or more fields of a filter-segment.Required scopes:

- `storage:filter-segments:write`

- `storage:filter-segments:share` to change `isPublic` to `true`
Following fields can be updated:

- `name`

- `description`

- `isPublic`

- `variables`*

- `includes`*
* If given the value will be overridden.Fields not given will be ignored.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | PartialUpdateFilterSegment |
 | config.filterSegmentUid*required | string | UID of the filter-segment
 | config.optimisticLockingVersion*required | number | version which should be updated. used for optimistic locking.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Filter-segment successfully updated.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissions | Not found: the server cannot find the requested filter-segment.Code example
`tsx
import { filterSegmentsClient } from "@dynatrace-sdk/client-filter-segment-management";const data = await filterSegmentsClient.partiallyUpdateFilterSegment({ filterSegmentUid: "D82a1jdA23a", optimisticLockingVersion: 1, body: { description: "only includes data of the development environment", }, });
`

#### updateFilterSegment

filterSegmentsClient.updateFilterSegment(config): PromiseUpdate a filter-segment. All fields will be overwritten (also undefined or null fields).Update one or more fields of a filter-segment.Required scopes:

- `storage:filter-segments:write`

- `storage:filter-segments:share` to change `isPublic` to `true`
Following fields can be updated:

- `name`

- `description`

- `isPublic`

- `variables`*

- `includes`*
* Values of the fields will be overridden or removed if not given.Provide all other fields with unchanged values.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | UpdateFilterSegment |
 | config.filterSegmentUid*required | string | UID of the filter-segment
 | config.optimisticLockingVersion*required | number | version which should be updated. used for optimistic locking.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Filter-segment successfully updated.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | bad request | unauthorized | missing permissions | Not found: the server cannot find the requested filter-segment.Code example
`tsx
import { filterSegmentsClient } from "@dynatrace-sdk/client-filter-segment-management";const data = await filterSegmentsClient.updateFilterSegment( { filterSegmentUid: "D82a1jdA23a", optimisticLockingVersion: 1, body: { uid: "D82a1jdA23a", name: "dev_environment", description: "only includes data of the development environment", variables: { type: "query", value: "fetch logs | limit 1", }, isPublic: false, owner: "john.doe", includes: [ { filter: '{"type":"Group","range":{"from":0,"to":19},"logicalOperator":"AND","explicit":false,"children":[{"type":"Statement","range":{"from":0,"to":19},"key":{"type":"Key","textValue":"content","value":"content","range":{"from":0,"to":7}},"operator":{"type":"ComparisonOperator","textValue":"=","value":"=","range":{"from":8,"to":9}},"value":{"type":"String","textValue":"\\"[debug]\\"","value":"[debug]","range":{"from":10,"to":19},"isEscaped":true}}]}', dataObject: "logs", }, { filter: '{"type":"Group","range":{"from":0,"to":18},"logicalOperator":"AND","explicit":false,"children":[{"type":"Statement","range":{"from":0,"to":18},"key":{"type":"Key","textValue":"content","value":"content","range":{"from":0,"to":7}},"operator":{"type":"ComparisonOperator","textValue":"=","value":"=","range":{"from":8,"to":9}},"value":{"type":"String","textValue":"\\"[info]\\"","value":"[info]","range":{"from":10,"to":18},"isEscaped":true}}]}', dataObject: "events", }, ], }, },);
`

### Types

#### CustomValidationErrorInfo

 |
 | Name | Type
 | message*required | string

#### DetailedFilterSegment

 |
 | Name | Type | Description
 | allowedOperations | null | Array | Defines the allowed operations of the current user.
 | description | null | string | Description of the filter-segment.
 | externalId | null | string | Optional unique identifier of the filter-segment. Used for Dynatrace Configuration as Code
 | includes | null | ArrayInclude> | List of includes of the filter-segment.
 | isPublic | boolean | Indicates if the filter-segment is publicly accessible within the tenant.
 | isReadyMade | null | boolean | Indicates if the segment is ready-made.
 | name*required | string | Name of the filter-segment.
 | owner*required | string | Defines the owner of the filter-segment.
 | uid*required | string | Unique identifier of the filter-segment.
 | variables | null | FilterSegmentVariables | Variables of the filter-segment.
 | version | number | Used for optimistic locking. Update requests define with this on which version the data updated is based on. This must match with the version stored, otherwise the update will fail due to concurrent modification.

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

#### FilterSegment

List of filter-segments.

 |
 | Name | Type | Description
 | allowedOperations | null | Array | Defines the allowed operations of the current user.
 | description | null | string | Description of the filter-segment.
 | externalId | null | string | Optional unique identifier of the filter-segment. Used for Dynatrace Configuration as Code
 | isPublic | boolean | Indicates if the filter-segment is publicly accessible within the tenant.
 | isReadyMade | null | boolean | Indicates if the segment is ready-made.
 | name*required | string | Name of the filter-segment.
 | owner*required | string | Defines the owner of the filter-segment.
 | uid*required | string | Unique identifier of the filter-segment.
 | variables | null | FilterSegmentVariables | Variables of the filter-segment.
 | version | number | Used for optimistic locking. Update requests define with this on which version the data updated is based on. This must match with the version stored, otherwise the update will fail due to concurrent modification.

#### FilterSegmentNamespaceDto

 |
 | Name | Type | Description
 | allowedFilterOperations | ArrayFilterSegmentPushDownFilterableDto> | Allowed filter operations.
 | name*required | string | Name of the namespace.
 | types | ArrayFilterSegmentTypeDto> | Types of the namespace.

#### FilterSegmentPropertyDto

 |
 | Name | Type
 | name | string
 | type | string

#### FilterSegmentPushDownFilterableDto

Allowed filter operations.

 |
 | Name | Type
 | filterName | string
 | supportedAttributes | Arraystring>

#### FilterSegmentRelationshipDto

 |
 | Name | Type
 | name | string
 | target | string

#### FilterSegmentTypeDto

Types of the namespace.

 |
 | Name | Type
 | displayName | string
 | filtersEntitiesOnly | boolean
 | fromTypes | ArrayFilterSegmentRelationshipDto>
 | name | string
 | properties | ArrayFilterSegmentPropertyDto>
 | relatedTargetEntityOnly | boolean
 | restrictedParentProperties | Arraystring>

#### FilterSegmentVariables

Variables of the filter-segment.

 |
 | Name | Type | Description
 | type*required | string | Type of the variable.
 | value*required | string | Value of the variable.

#### FilterSegments

 |
 | Name | Type | Description
 | filterSegments*required | ArrayFilterSegment> | List of filter-segments.

#### Include

List of includes of the filter-segment.

 |
 | Name | Type | Description
 | applyTo | null | Arraystring> | [Experimental] The tables that the entity-filter will be applied to.
 | dataObject*required | string | The data object that the filter will be applied to. Use '_all_data_object' to apply it to all dataObjects.
 | filter*required | string | Data will be filtered by this value. Field names must only contain letters, numbers and underscores, otherwise they need to be escaped using quotes(`).
 | relationship | null | Relationship | [Experimental] The relationship of an include which has to be be specified when the data object is an entity view.

#### InvalidAuditEventsErrorInfo

 |
 | Name | Type
 | invalidAuditEventIndices*required | Arraynumber>
 | invalidEventIndices | Arraynumber>
 | message*required | string

#### LeanFilterSegment

List of filter-segments.

 |
 | Name | Type | Description
 | allowedOperations | null | Array | Defines the allowed operations of the current user.
 | externalId | null | string | Optional unique identifier of the filter-segment. Used for Dynatrace Configuration as Code
 | isPublic | boolean | Indicates if the filter-segment is publicly accessible within the tenant.
 | isReadyMade | null | boolean | Indicates if the segment is ready-made.
 | name*required | string | Name of the filter-segment.
 | owner | null | string | Defines the owner of the filter-segment.
 | uid*required | string | Unique identifier of the filter-segment.
 | variables | null | FilterSegmentVariables | Variables of the filter-segment.

#### LeanFilterSegments

 |
 | Name | Type | Description
 | filterSegments*required | ArrayLeanFilterSegment> | List of filter-segments.

#### MediaTypeErrorInfo

 |
 | Name | Type
 | message*required | string
 | supportedMediaTypes*required | Arraystring>

#### NewFilterSegment

 |
 | Name | Type | Description
 | description | null | string | Description of the filter-segment.
 | externalId | null | string | Optional unique identifier of the filter-segment. Used for Dynatrace Configuration as Code
 | includes | null | ArrayNewInclude> | List of includes of the filter-segment.
 | isPublic*required | boolean | Indicates if the filter-segment is publicly accessible within the tenant.
 | name*required | string | Name of the filter-segment.
 | variables | null | FilterSegmentVariables | Variables of the filter-segment.

#### NewInclude

List of includes of the filter-segment.

 |
 | Name | Type | Description
 | applyTo | null | Arraystring> | [Experimental] The tables that the entity-filter will be applied to.
 | dataObject*required | string | The data object that the filter will be applied to. Use '_all_data_object' to apply it to all dataObjects.
 | filter*required | string | Data will be filtered by this value. Field names must only contain letters, numbers and underscores, otherwise they need to be escaped using quotes(`).
 | relationship | null | NewRelationship | [Experimental] The relationship of an include which has to be be specified when the data object is an entity view.

#### NewRelationship

[Experimental] The relationship of an include which has to be be specified when the data object is an entity view.

 |
 | Name | Type | Description
 | name*required | string | Name of the relationship.
 | target*required | string | Target of the relationship.

#### ParameterErrorInfo

 |
 | Name | Type
 | message*required | string
 | parameterDescriptor*required | string

#### PartialUpdateFilterSegment

 |
 | Name | Type | Description
 | description | null | string | Description of the filter-segment.
 | externalId | null | string | Optional unique identifier of the filter-segment. Used for Dynatrace Configuration as Code
 | includes | null | ArrayNewInclude> | List of includes of the filter-segment.
 | isPublic | null | boolean | Indicates if the filter-segment is publicly accessible within the tenant.
 | name | null | string | Name of the filter-segment.
 | variables | null | FilterSegmentVariables | Variables of the filter-segment.

#### ProxyErrorInfo

 |
 | Name | Type
 | message*required | string

#### QueryFrontendRawErrorInfo

 |
 | Name | Type
 | message*required | string
 | rawQueryFrontendResponse*required | string

#### Relationship

[Experimental] The relationship of an include which has to be be specified when the data object is an entity view.

 |
 | Name | Type | Description
 | name*required | string | Name of the relationship.
 | target*required | string | Target of the relationship.

#### RequestBodyErrorInfo

 |
 | Name | Type
 | bodyDescriptor*required | string
 | message*required | string

#### UpdateFilterSegment

 |
 | Name | Type | Description
 | description | null | string | Description of the filter-segment.
 | externalId | null | string | Optional unique identifier of the filter-segment. Used for Dynatrace Configuration as Code
 | includes | null | ArrayNewInclude> | List of includes of the filter-segment.
 | isPublic*required | boolean | Indicates if the filter-segment is publicly accessible within the tenant.
 | name*required | string | Name of the filter-segment.
 | owner*required | string | Defines the owner of the filter-segment.
 | uid*required | string | Unique identifier of the filter-segment.
 | variables | null | FilterSegmentVariables | Variables of the filter-segment.

### Enums

#### DetailedFilterSegmentAllowedOperationsItem

⚠️ Deprecated
Use literal values.

Defines the allowed operations of the current user.

##### Enum keys
`Delete` | `Read` | `Share` | `Write`

#### FilterSegmentAllowedOperationsItem

⚠️ Deprecated
Use literal values.

Defines the allowed operations of the current user.

##### Enum keys
`Delete` | `Read` | `Share` | `Write`

#### GetFilterSegmentQueryAddFieldsItem

⚠️ Deprecated
Use literal values.

##### Enum keys
`Externalid` | `Includes` | `Resourcecontext` | `Variables`

#### GetFilterSegmentsQueryAddFieldsItem

⚠️ Deprecated
Use literal values.

##### Enum keys
`Externalid` | `Resourcecontext` | `Variables`

#### GetLeanFilterSegmentsQueryAddFieldsItem

⚠️ Deprecated
Use literal values.

##### Enum keys
`Externalid` | `Owner` | `Resourcecontext` | `Variables`

#### LeanFilterSegmentAllowedOperationsItem

⚠️ Deprecated
Use literal values.

Defines the allowed operations of the current user.

##### Enum keys
`Delete` | `Read` | `Share` | `Write`
