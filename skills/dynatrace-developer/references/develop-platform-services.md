# Develop — Platform services

Scraped from <https://developer.dynatrace.com/develop/>. Each section is one doc page (its path is shown) with the prose and code captured.

## core-concepts

`/develop/platform-services/core-concepts/`

- Core concepts

## Core concepts

- 1-min read

###

#### About platform services
Learn methods to interact with platform services.Explanation

#### API versions
Understand the versioning of Dynatrace platform service APIs.Reference

#### Authentication
Details about the structure of Dynatrace platform service APIs permissionsReference

#### Error handling
Description of the platform service APIs HTTP error codes and error responsesReference

#### Filtering and sorting
Details about filtering and sorting strategies through APIsReference

#### Locking strategies
Information about using optimistic locking to protect your resources in versionsExplanation

---

## core-concepts/about-platform-services

`/develop/platform-services/core-concepts/about-platform-services/`

- Core concepts
- About platform services

## About platform services

- Explanation
- 2-min readThe Dynatrace platform provides a collection of so-called platform services where each has its specific area of responsibility. You can access platform services in different ways. Platform services are individually versioned and offer RESTful APIs via HTTP requests. JSON is the message format for all platform service API calls.

### URL structure

The general URL structure of the Dynatrace platform API looks like this:

`tsx
/platform////
`

- The environment-specific domain name `.apps.dynatrace.com` defines the URL.

- is the customer environment's unique identifier.

- `platform` is the mandatory root path for all platform services.

- is the mandatory name of the platform service. A may prepend the to group platform services that belong together.

- is the current platform service version in this format: `v`.

- is the path within the platform service.

#### Example

### Swagger UI

All Dynatrace platform services are accessible via the Swagger UI on this path:

`tsx
.apps.dynatrace.com/platform/swagger-ui/index.html
`

### SDK

App developers typically don't directly interact with the platform service APIs and instead use the Dynatrace SDK for TypeScript.
We build a Dynatrace SDK package to match a certain platform service API version exactly. The package's metadata documents the exact API version that the package represents.

All platform service SDK packages follow this naming schema:

`tsx
client---v
` and correspond with the URL structure of the platform service that the package represents.
 is the API version and is only set if more than one major version of the same service is available.

NoteThe API version isn't the same as the package build version. Developers might rebuild a package without changing the API version it represents (for example, to include bug fixes or other improvements in
the SDK implementation without affecting the API it represents).

#### Example

---

## core-concepts/api-versions

`/develop/platform-services/core-concepts/api-versions/`

- Core concepts
- API versions

## API versions

- 2-min readAll Dynatrace platform service APIs are semantically versioned with this format:

`tsx
..
`

NoteOnly the Major version is visible on the service URL path and the SDK name.

### Backward compatibility

Semantic versioning defines that the major version must only be changed when incompatible changes are applied to the API.

Therefore, any Dynatrace platform service API must support backward compatibility:

- `Major` version updates (x.*.*) represent a breaking change. Any major update results in a new service version being provided parallel to the existing version.

- `Minor` version updates (*.x.*) represent a backward compatible change in the API (for example., a new field is added to a response, or a new query parameter is introduced). Extensions of an existing API are generally not considered a breaking change.

- `Patch` version updates (*.*.x) represent any changes that don't affect the functionality or structure of the API (for example, additional examples or documentation in the API Spec file).

Backward compatibility policy: When we change the API by tagging the update `Minor` or `Patch`, the changes will be non-breaking. It includes:

- Addition of optional request parameters: API might include new optional properties to the requests. It means clients don't need to handle them. However, they can utilize them if needed.

- Addition of response parameters: API responses may include additional properties in the JSON body. You should design your clients to either process or ignore these properties while considering compatibility.

- Enum constants in response: We might add new constants to existing enums. You should handle these new constants in your clients in a way that maintains application stability.

### Deprecation & sunsetting

Eventually, a platform service version will reach its end of life and Dynatrace decides to remove it.

All Dynatrace APIs about to be removed go through two phases - Deprecation and Sunsetting.

- Deprecation means that the service version is no longer recommended for use, even though it's still fully operational.

- Sunsetting means that the service version will be shut down, meaning that at the announced time, the service version will no longer be available.

NoteServices marked as deprecated, or sunset are still fully functional and supported by Dynatrace.

#### Deprecation

A deprecated service has all operations marked with the deprecated field in the Swagger UI documentation of the service.
All REST responses of a deprecated service contain the deprecation header with the value 'true'.

#### Sunsetting

A sunset service contains the sunset date in the Swagger UI documentation of the service.
All REST responses of a sunset service contain a sunset header with the sunset date.

---

## core-concepts/authentication

`/develop/platform-services/core-concepts/authentication/`

- Core concepts
- Authentication

## Authentication

- 1-min readAll Dynatrace platform service APIs use the OAuth2.0 Client Credentials Flow for authentication.

NoteFor further details, visit Access platform APIs from outside.

### API permissions

Dynatrace platform service APIs control user access with a policy-based permission system.
The Dynatrace IAM (Identity and access management) system allows you to define policies that grant actions of users on resources.
Each platform service API requires permission (or scope) to be granted to the user executing a request on the API.

All permissions follow this naming schema:

`tsx
::
`

- , and correspond to the entries described in the general URL structure.

- defines the action associated with the permission (for example, execute, read, write, etc.).

#### Example

You can find a full list of available scopes on the IAM service reference page.

---

## core-concepts/error-handling

`/develop/platform-services/core-concepts/error-handling/`

- Core concepts
- Error handling

## Error handling

- 6-min read

### Standard HTTP error codes

All platform service APIs mainly (but not only) use these HTTP status codes.
Additional status or standard codes are used differently and documented in the respective service's Swagger UI.

 |
 | Error Status Code | Description
 | 400 - Bad Request | The request syntax was corrupt. It's also the default fallback code to transport an application-level error if no specific error code is available (for example, the request was valid, but the application logic refused to execute it due to some application restriction like a quota).
 | 401 - Unauthorized | The request was rejected because the client needs to be authenticated first.
 | 403 - Forbidden | The request was rejected because the (authenticated) client didn't have the necessary permissions. See Errors for the details in the error response.
 | 404 - Not Found | The requested resource wasn't found (it never existed).
 | 409 - Conflict | The write operation failed because the "optimistic locking" strategy detected a conflict.
 | 410 - Gone | The requested resource wasn't found, although it existed some time ago.
 | 429 - Too Many Requests | The client sent too many requests at a certain time.
 | 500 - Internal Server Error | Unspecified server error (typically caused by internal problems like exceptions).
 | 501 - Not Implemented | The API doesn't support the operation.
 | 503 - Service Unavailable | Service is temporary unavailable.

### Errors

Error responses are always returned in an error envelope like this:

`tsx
{ "error": { "code": "error code", "message": "error message" }}
`

- `code` is set to the HTTP response code or an API-specific error code documented in the service APIs Swagger UI.

- `message` is a brief description of the error that occurred

You can add additional details about each error in a details field. This section conveys additional information about the error, for example, which query parameter violated a precondition. The `details` field contains fields to describe the error further.

These are commonly used fields in the `details` object:

- `errorRef` is a uuid string (see rfc-4122) and represents a reference of the error into e.g., the log file of the service.

- `traceId` is a string containing a 32-character hex integer value.

- `errorCode` is a string value representing more detailed error information than the HTTP response code alone.

- `constraintViolations` is an array of ConstraintViolation objects.

- A ConstraintViolation contains information about an input parameter (path, query, or request body) that violated some validation rule of the service API and caused the error.

- `ConstraintViolation` always contains a field `message` describing the error.

- `ConstraintViolation` may contain a separate field, `parameterLocation`, which describes the general location of the violating parameter (query parameter, request body, etc.)

- `ConstraintViolation` may contain a separate field, `path`, which refers to the violating parameter within the `parameterLocation`.

- `ConstraintViolation` may contain additional fields further describing the error.

- `missingScopes` must be set if the API returns a 403 - Forbidden response.

- `missingScopes` is an array of strings containing a complete list of missing IAM scopes necessary to execute the request successfully.

#### Examples

Following are some examples of error responses.

- Error response with `details` object.

`tsx
{ "error": { "code": 400, "message": "Constraints violated.", "details": { "errorRef": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6", "traceId": "99633483d17779d7c81141f50dbc2a49", "errorCode": "InvalidPaginationToken", "constraintViolations": [ { "path": "detectionRules[0].filterConfig.pattern", "message": "may not be null", "parameterLocation": "PAYLOAD_BODY" } ] } }}
`

- Error response with `missingScopes`.

`tsx
{ "error": { "code": 403, "message": "Insufficient permissions.", "details": { "missingScopes": ["document:documents:read", "state:app-states:write"] } }}
`

### Warnings

Sometimes a response may contain warning information although the request was successful. It may happen when some data in the request payload was missing and replaced with default values.

Warnings are optional, but if a response contains warnings, they're returned as the first field in the response body, named `warnings`.
It includes an array of potential warning objects. Each warning object has at least a string `message` field with the warning message.

A `details` field may add additional details about each warning.
This section conveys additional information about the warning, for example, which query parameter violated a precondition. The `details` may contain any fields to describe the warning further.

These are commonly used fields in the `details` object:

- `warningRef` is a uuid string (see rfc-4122) and represents a reference of the warning into e.g., the log file of the service.

- `traceId` is a string containing a 32-character hex integer value.

- `constraintViolations` is an array of `ConstraintViolation` objects.

- A ConstraintViolation contains information about an input parameter (path, query, or request body) that violated some validation rule of the service API and caused the warning.

- `ConstraintViolation` always contains a field `message` describing the warning.

- `ConstraintViolation` may contain a separate field, `parameterLocation`, which describes the general location of the violating parameter (query parameter, request body, etc.)

- `ConstraintViolation` may contain a separate field `path` that refers to the violating parameter within the `parameterLocation`.

- `ConstraintViolation` may contain additional fields further describing the warning.

#### Example

`tsx
{ "warnings": [ { "message": "caffeine saturation is low", "details": { "warningRef": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6", "traceId": "99633483d17779d7c81141f50dbc2a49", "constraintViolations": [ { "path": "dynatrace.employee", "message": "Caffeine is getting low! Grab a cappuccino in the Dynatrace cafeteria!", "parameterLocation": "DYNATRACE_OFFICE" } ] } } ], "items": [ { "latestSchemaVersion": "1.4.2", "schemaId": "builtin:anomaly.infrastructure", "displayName": "Anomaly Detection for Infrastructure" } ], "totalCount": 1}
`

### Rate limiting (throttling)

Services may decide to reject request execution if it's overloaded or to guarantee fair request execution distribution across multiple customer environments.

If a service throttles a request it returns:

- HTTP 429 - Too Many Requests if the throttling was caused by the client.

- HTTP 503 - Service Unavailable if the service is generally overloaded or is unable to determine if overloading is caused by client.

In both cases the service sets the `retry-after` header with the number of seconds to wait until the next retry. The error response also includes the time until the next retry in the field `retryAfterSeconds` in seconds.

It may also include details about the violated constraint in the field `details`.

#### Example

`tsx
{ "error": { "code": 503, "message": "service is overloaded", "retryAfterSeconds": 3, "details": "service is busy, good luck next time!" }}
`

---

## core-concepts/filtering-sorting

`/develop/platform-services/core-concepts/filtering-sorting/`

- Core concepts
- Filtering and sorting

## Filtering and sorting

- 5-min read

### Introduction

One common feature most services provide is the ability to return a list of resources through an API. These resources can be filtered and sorted based on various criteria.

Let's consider the examples of the App Engine Registry and Documents APIs. The `/apps` endpoint enables you to retrieve a list of all installed applications, while the `/documents` endpoint returns a list of all available documents, as shown below:

By utilizing the filtering and sorting options provided by these APIs, you can easily narrow your search and retrieve only the relevant information to your needs.

### Sorting

You can use the query parameter `sort` to sort the list. The `sort` parameter requires a single field name or a comma-separated list of field names defining the sorting order. The order of the field names in the list is left to right, meaning that the first field name is the primary sorting criteria, followed by the second, and then next fields.

By default, the sorting order is ascending. However, you can change this by prefixing the field name with a minus sign, `-`. It will sort the list in descending order based on that particular field. It's important to note that string comparison for sorting is case-insensitive.

Look at the following API call:

`tsx
GET …/problems?sort=status,-startTime,relevance
`

The API will sort the result items by ascending `status` first, then by descending `startTime`, and finally ascending `relevance`.

### Filtering

You can use the query parameter `filter` if the API supports filtering. By default, the filter expression can reference any field in the listed resource. However, some services may restrict the fields that you can filter.

The filtered result is always a list regardless of the number of entries. If the result is empty, it's still considered a successful execution of the API with an HTTP 200 - Ok response code.

#### Construct filter expression

To construct a filter expression, use a set of field-level expressions combined with boolean operators. The boolean operators supported are `or`, `and`, and `not`.

You can also use parentheses to group expressions. If you don't use parentheses, the standard boolean operator precedence is applied, with `and` taking precedence over `or`.

The general form of the field-level expression is . Let's understand them:

- is the field name you want to filter.

- is an operator that specifies how the field should be in comparison to the specified value.

- is the value against which the field is compared. Depending on the filtered field type, the value can be a string, date/time, number, or boolean.

#### Datatypes and operators

Following is the list of data types supported in the filter expression along with the operators:

 |
 | Datatype | Supported operators | Representation
 | number (short, int, long, float, double) | `=`, `!=`, , `>=`, `in` |
- Integers: decimal and hexadecimal (with leading `0x`)
- Floating Point: scientific notation with optional exponent `e` or `E`
 | String | `=`, `!=`, `contains`, `starts-with`, `ends-with`, `in` |
- Single quotes only: 'Hello World!'
- Special characters (for example, the quotes) are preceded with `\`
- exact operators `=` and `!=` are case sensitive
- inexact operators `contains`, `starts-with`, and `ends-with` are case insensitive
 | Boolean | `=`, `!=` | Comparison with constants `true` or `false` only
 | Date/Time | `=`, `!=`, , `>=`, `in` | As ISO 8601 compliant string in one of the following formats:
- `yyyy-MM-ddThh:mm:ss[+/-]hh:mm` (e.g. `2007-12-03T10:15:30+01:00`)
- `yyyy-MM-ddThh:mm:ss` (e.g. `2007-12-03T10:15:30`)
- `yyyy-MM-dd` (e.g. `2007-12-03`)
- `hh:mm:ss` (e.g. `10:15:30`)
 | Array | `contains`, `is-empty` |
- `contains`: Comparison with elements contained in the array, for example, 'Hello World!' for an array of strings.
- `is-empty`: Check if array is empty.

##### The 'in' operator

You can use it to compare for equality within a constant list of possible values, which is provided by the `in` operator.

Assuming `name` being of datatype String, instead of writing

`tsx
name = '123' or name = '456' or name = '789'
`

you can write

`tsx
name in('123','456','789')
`

The operator is supported for all datatypes except for booleans. You can only use the list constant on the right side of the `in` operator; you can't use it like a field of datatype `list`.

Thus, this expression is invalid:

`tsx
('123','456','789') contains ‘123’
`

#### Examples

`tsx
GET /clients?filter=age=30GET /clients?filter=firstName='Konrad' and lastName='Zuse'GET /documents?filter=owner='user1' and lastModified>='2022-02-06T11:00:00Z'GET /tenants?filter=tenantUuid starts-with 'abc' and not(deleted=false or active=true)GET /caches?filter=cacheHitRateGET /locations?filter=distance>=1.0E4GET /apps?filter=resourceStatus.subResourceTypes contains 'FUNCTIONS'
`

### Field filtering and partial results

Some services may return only a subset of all available fields of a resource by default, also known as a partial result. This can be beneficial in certain scenarios to avoid expensive background operations and unnecessary network bandwidth usage.

If an API supports partial results, it accepts a query parameter `add-fields` to include missing fields in the default response.

Field filtering is only supported in the APIs that list or get a resource.

#### Things to remember

- `add-fields` accept a comma-separated list of field names that are added to the default set of fields.

- Duplicate fields in the list result in an error.

- Adding fields already in the default response is considered redundant and ignored.

- Referencing unknown fields results in an error.

- A dot separates nested field names.

#### Example

In the following example, you're fetching a list of entities. The result includes default fields.

`tsx
GET /entities
tsx
{ "totalCount": 72, "nextPageKey": "…", "entities": [ { "entityId": "HOST-0004DD30F142D18C" } ]}
`

In the following example, you're using `add-fields` to add `lastSeenTms` and `properties.bitness` in addition to the default result, which you can see in the result below:

`tsx
GET /entities?add-fields=lastSeenTms,properties.bitness
tsx
{ "totalCount": 72, "nextPageKey": "…", "entities": [ { "entityId": "HOST-0004DD30F142D18C", "lastSeenTms": 1615991063257, "properties": { "bitness": "64" } } ]}
`

---

## core-concepts/locking-strategies

`/develop/platform-services/core-concepts/locking-strategies/`

- Core concepts
- Locking strategies

## Locking strategies

- Explanation
- 2-min read

### Introduction

Multiple users manipulating the same resource simultaneously typically leads to a conflict of interest. Without locking or validation, the order of the write operations defines who finally wins and whose changes are lost. This is the last writer wins strategy, the default strategy used in the Dynatrace platform API.

### Optimistic locking

You can use optimistic locking strategy as an alternative to the default.

Optimistic Locking assigns a version to the protected resource as a field named `version`. The format of the version depends on the service and can be a simple ever-increasing counter, a hash, or a decimal or hash encoding.

When a resource is protected by optimistic locking, all writing operations accept an `optimistic-locking-version` query parameter which contains the numeric representation of the original version from which the written content was taken. That allows the API to check if the current version of the resource is still the one on which the write operation is based and reject the request if it's not.

In the case of a conflict, the API will respond with a 409 - Conflict status code. The only situation where a missing `optimistic-locking-version` parameter is accepted on a writing operation is when no conflict can occur, such as when creating a new resource or deleting a resource.

#### Example

This example shows how you can update a document protected by optimistic locking.
You first need to retrieve the current version by calling the `/documents/` endpoint.

`tsx
GET /documents/6239bf48-ce6d-4e06-8694-bd3c2b235d63
tsx
{ "id": "6239bf48-ce6d-4e06-8694-bd3c2b235d63", "name": "document name", "type": "notebook", "version": "2e9565ea", "owner": "441664f0-23c9-40ef-b344-18c02c23d789"}
`

To update the document you have to pass the `version` returned by the request above as the `optimistic-locking-version` query parameter:

`tsx
PUT /documents/6239bf48-ce6d-4e06-8694-bd3c2b235d63?optimistic-locking-version=2e9565ea
`

A subsequent call to the `/documents/` endpoint returns a new `version` value:

`tsx
GET /documents/6239bf48-ce6d-4e06-8694-bd3c2b235d63
tsx
{ "id": "6239bf48-ce6d-4e06-8694-bd3c2b235d63", "name": "updated document name", "type": "notebook", "version": "456efa90", "owner": "441664f0-23c9-40ef-b344-18c02c23d789"}
`

---

## platform-services

`/develop/platform-services/`

## Platform services

- Explanation
- 1-min readDynatrace provides a collection of platform services, each with a specific area of responsibility. In this section, you can learn key concepts and understand how each platform service works.

###

#### Core concepts
Understand core Dynatrace platform concepts, including API versioning, authentication, error handling, filtering, sorting, and more.Reference

#### Services
Learn about available services for the Dynatrace platform, including services for Dynatrace Intelligence, Grail, app settings, metadata, and more.Reference

---

## services

`/develop/platform-services/services/`

- Services

## Services

- 1-min read

###

#### AppEngine
Basic concepts to understand when working with AppEngineExplanation

#### App settings service
Manage app settingsExplanation

#### AutomationEngine
Introduction to AutomationEngine, which manages workflows and runs their executionsExplanation

#### Classic environment service
Information about a service that mirrors most Dynatrace APIs so you can use them inside AppEngine and AutomationEngineExplanation

#### Dynatrace Intelligence service
Basic concepts to learn to use AI and ML capabilities in the Dynatrace platformExplanation

#### Document service
Information about storing all types of data; typically, self-contained data produced and maintained by appsExplanation

#### Grail service
Reference of the Grail query API, which lets you store and query dataExplanation

#### Notification service
Basic concepts and limitations of email notifications in your appExplanation

#### Platform management service
Information about retrieving license and settings information in a Dynatrace environmentExplanation

#### State service
Information about a key-value storage service that an app can use to store internal states, only available in their corresponding appsExplanation

---

## services/app-engine

`/develop/platform-services/services/app-engine/`

- Services
- AppEngine

## AppEngine

- Explanation
- 3-min readDynatrace AppEngine is responsible for installing Dynatrace Apps and their lifecycle.
It also provides APIs to execute JavaScript code inside the Dynatrace JavaScript runtime, with low-latency access to Grail and the platform APIs. Code for the JavaScript runtime is either part of the app bundle or dynamically sent in the request body.

### Concepts

You need to know the following concepts to work with the AppEngine.

#### App bundles

AppEngine installs apps by uploading the app bundle—a ZIP file containing the built app code, app metadata, static resources, settings, and functions. The App Toolkit (`dt-app`) is the preferred tool for creating app bundles.

#### Registry

The registry is mainly responsible for installing, retrieving, updating, and uninstalling apps.

It performs a basic confidence check before installation and returns an error if it finds any constraint violations, such as the app bundle being too large. If the confidence check ends successfully, the asynchronous app installation process starts. You can check the app installation process by calling the `/apps/` endpoint. Installing an app is a relatively quick process that should finish within a few minutes.

Uninstalling an app is also an asynchronous process. AppEngine might take a few minutes to remove the app.

#### Function executor

The function executor is an API that allows you to execute code (that you haven't bundled with apps) inside Dynatrace AppEngine.

#### Dynatrace JavaScript runtime

In addition to code executed in the browser, you can provide back-end code using Dynatrace app functions powered by the Dynatrace JavaScript runtime. The runtime executes app functions and code sent to the function executor (for example, within Notebooks and Workflows). Follow the Dynatrace app development tutorial or read more in the app functions reference to start with app functions. Read more about all available APIs in the Dynatrace JavaScript runtime in the JavaScript runtime reference.

Code inside the runtime runs sandboxed, and communication with resources outside the Dynatrace platform is restricted. Code inside the Dynatrace JavaScript runtime may use the fetch function to execute HTTP requests to external and platform service APIs. If the `resource` parameter of the fetch function is a relative path, the request can interact with Dynatrace platform services. In that case, the Dynatrace platform handles the authentication and routing to the right environment for you.

#### Outbound connections from functions

By default, you can't access external hosts from the Dynatrace runtime. To learn more about managing the list of allowed hosts, read Allow outbound connections.

#### EdgeConnect

To forward HTTP requests from the Dynatrace JavaScript runtime to your private network, you need to:

- Run an EdgeConnect container in your private network.

- Use the to configure the host patterns of all HTTP requests that should be routed to that EdgeConnect container.

To learn more about EdgeConnect, read the deployment instructions.

### Related links

- App functions

- JavaScript runtime

- Allow outbound connections

---

## services/app-settings-service

`/develop/platform-services/services/app-settings-service/`

- Services
- App settings service

## App settings service

- Explanation
- 1-min readApp settings allows users to store app configuration settings in a centralized location, so that all app users can retrieve the information via the SDK. For example, you can provide a configuration to access an external system.

The app can consume the settings data via the App Settings SDK.

### Concepts

You need to know the following concepts to work with the app settings service.

#### Schemas

Schemas define the structure and constraints of the data stored in app settings.
You can define any number of schemas and bundle them with your app.

#### Effective values

The SDK allows the app to get effective values for the defined schemas.
Effective values fall back to the default values defined in the schema if no stored values are available.
That way, as an app developer, you can provide the sensible default settings without needing the user to configure them first.

#### Secrets handling

App settings allow you to define secret properties to store sensitive information like access tokens. The autogenerated UI will mask the properties with the type `secret`. However, you can get the actual values inside an app function.

#### Local development

For easier development, the App Settings SDK provides a plugin for the App Toolkit that enables you to provide mock data right out of your development environment and manipulate settings without deploying the app. To learn more, look at Local development.

### Related links

- How to store app settings

---

## services/automation-engine

`/develop/platform-services/services/automation-engine/`

- Services
- AutomationEngine

## AutomationEngine

- Explanation
- 1-min readThe AutomationEngine is the backend of Dynatrace Workflows. It manages workflows and runs their executions.

### Concepts

For details about workflow definitions and their behavior refer to the user documentation.

### Related links

- Automation SDK

- User documentation

---

## services/classic-environment-service

`/develop/platform-services/services/classic-environment-service/`

- Services
- Classic environment service

## Classic environment service

- Explanation
- 2-min readThe classic environment service is a convenience service that mirrors most APIs already available in your existing Dynatrace environment. The service allows you to use these APIs inside AppEngine and AutomationEngine, enabling you to use the full power of Dynatrace in your apps and workflows.

The classic service only covers a subset of your Dynatrace environment's API since most functionality is available via the platform services. Use our platform services and Grail as the preferred option to access data inside Dynatrace and only fall back to the classic services if necessary.

### Concepts

You need to know the following concepts to work with the classic environment service.

#### Authentication and access control

The classic endpoints are authorized via OAuth and enforce the user's permissions in the backend. The environment role-based permissions are mapped onto the existing endpoints to make the environment endpoints consumable in a user context for app development. When using these APIs in apps and workflows, the whole OAuth layer is abstracted by the runtime and SDK so that you can focus on the problem and don't have to care about authentication and authorization.

#### Access classic endpoints with role-based permissions

As described above, OAuth enforces the user's role-based permissions to access classic API endpoints. For app developers, every endpoint has dedicated requirements regarding the permissions that the user needs in order to access it via the app. You can find the details of every method in the Classic Environment V2 reference.

The following example lists the required information to get an auto-update configuration for an ActiveGate:

- Method: `activeGatesAutoUpdateConfigurationClient.getAutoUpdateConfigById()`

- Description: Gets the configuration of auto-update for the specified ActiveGate

- OAuth scope for manifest: `environment-api:activegates:read`

- Required user permission: `environment:roles:manage-settings`

- Management zone permission: No

For this method, the user must be able to manage the environment's settings.

#### Audit REST API calls

With AppEngine and Grail, we can monitor the full API spectrum and provide detailed API access logs as part of our audit logs on Grail. Since AppEngine exposes the classic environment service, you can also use the API logs for this service.

### Related links

- Classic SDK v1

- Classic SDK v2

- Ingest data

---

## services/document-service

`/develop/platform-services/services/document-service/`

- Services
- Document service

## Document service

- Explanation
- 3-min readThe document service provides storage for all types of data. The primary use case for document service is to store user-centric, self-contained data typically produced and maintained by apps.

### Concepts

You need to know the following concepts to work with the document service.

#### Document

Every document consists of metadata and content. The metadata contains information such as the document name and timestamps, which you can use to filter and sort your documents.

Following are some essential things to remember about documents:

- The document service generates a unique ID for each document and doesn't rely on the document's name for identification. Therefore, document names don't have to be unique.

- The content of documents isn't indexed. Therefore, you can't search the contents of a document.

- You must ensure that the content for each document doesn't exceed the maximum size.

NoteThe document service is entirely agnostic of the content and the content type.

#### Ownership

The user who creates a document becomes the owner of that document. The owner has permission to share and delete the document. Only the owner can access the document unless the owner shares it with others.

#### Admin access

Users with elevated privileges may request admin access and act with the same permissions as a document's owner. An admin has permission to access and modify documents created by any user of the same environment.

#### Sharing documents

By default, only the document owner can share a document. However, the owner can allow everyone with the Can edit permission to also share the document through the Allow editors to share toggle.
The document owner can grant either read-only or read-write access to the document for other users. Document service also prevents accidental overwriting due to collaboration using optimistic locking

There are three ways to share documents:

- Access for all (view-only): A document's owner can grant read-only access to the document to all users of the same environment.

- Access per user or group: A document's owner can grant access to the document to all users of the same environment. Each user must opt in individually.

- Access via shared link: A document's owner can grant specific users or groups access to a document.

NoteAll apps can access a document, even when the owner is restricting access to the document.

#### Restore deleted documents

Deleting a document moves it into the trash and makes it inaccessible. The document service will automatically delete documents in the trash after some time. Alternatively, users can manually delete a document from the trash if they don't want to wait for the automatic deletion.
Users can restore a document from the trash, making it accessible and sparing it from permanent deletion.

#### Restore previous document states

Users can create snapshots of documents. Subsequent updates to the document don't affect these snapshots.
Users can also restore a snapshot later if needed. This action resets the document to its state when the user made the snapshot.

NoteRestoring a snapshot affects only the document's content. It doesn't change access-related data like the document's shares or ownership.
Creating snapshots is rate-limited per user and document. The document service will delete snapshots automatically after some time. Each document allows for a maximum number of snapshots.

#### Data consistency

The document service guarantees eventual consistency.

### Related links

- Document SDK

- Basic document usage

---

## services/dynatrace-intelligence-service

`/develop/platform-services/services/dynatrace-intelligence-service/`

- Services
- Dynatrace Intelligence service

## Dynatrace Intelligence service

- Explanation
- 4-min readThe Dynatrace Intelligence predictive and causal AI platform service delivers a comprehensive suite of AI/ML and core statistical capabilities, seamlessly integrated into the Dynatrace platform. These essential predictive and causal analysis functions help app developers effectively address various use cases, including time series forecasting, learning anomaly detection models for time series data, and automated monitoring of metric behavior changes and anomalies.

App developers gain direct and streamlined access to all AI/ML functionalities when using Dynatrace Intelligence capabilities. This direct integration allows developers to apply these capabilities within apps, workflows, or Dynatrace functions, optimizing the efficiency and effectiveness of development processes.

Note"Dynatrace Intelligence" is the umbrella term for all AI in Dynatrace, including generative, agentic, causal, and predictive AI. It replaces "Davis AI" and "Davis CoPilot" and expands upon their capabilities. The terms "Davis" and "CoPilot" persist in certain locations, including APIs, Swagger, scopes, and Grail. These references are still relevant for Dynatrace Intelligence.

### Concepts

You need to know the following concepts to work with the Dynatrace Intelligence service.

#### Analyzer definitions

Every analyzer has a static definition, which describes its capabilities. The definition consists of the following parts: general metadata, input, and output definition.

The general metadata section contains essential information about the analyzer, such as its name, displayName, and description. An analyzer's name is fully qualified and guaranteed not to change in the future.

Input and output definitions share a standard schema describing how the input and output of a specific analyzer are structured. You can retrieve the exact structure of the input and output objects for a particular analyzer from the `analyzers//json-schema/input` or the `analyzers//json-schema/output` endpoints.

#### Analyzer execution

##### Flow

To execute an analyzer for the first time, we recommend the following request flow:

Query all analyzers: You should query all the available analyzers and choose among them using the endpoint.

Query a specific analyzer: Query a particular definition of an analyzer to see which functional scope and parameters the selected analyzer supports using the endpoint.

Query schema: Query the input and result schema of the analyzer using the and endpoint. The response is a JSON schema for the analyzer you're interested in.

Execute the data analyzer: Use the endpoint to execute a data analyzer. The Dynatrace Intelligence service executes analyzers asynchronously and returns a synchronous result within the defined wait period.

##### Execution logs

An analyzer provides execution logs if the execution fails or if additional information about the result is available. Before the Dynatrace Intelligence service executes an analyzer, it performs preliminary checks, such as input validations. If these checks fail, the analyzer is not executed and the service returns an error.

If the input matches the input definition, the request will always produce a consumable, successful result.

However, it can still happen that some analysis inside the analyzer fails for other reasons. In such cases, the analyzer provides execution logs pointing toward the problem.

Execution logs have a specific level, indicating the severity of the issue for the given analyzer. These levels can be filtered when executing an analyzer.

##### Example

The `dt.statistics.GenericForecastAnalyzer` produces a forecast for a given time series and is an excellent tool for predicting business metrics.

Given the following input:

`tsx
{ "timeSeriesData": "timeseries avg(dt.host.cpu.usage)"}
`

This analyzer returns the forecast predictions for the given time series:

`tsx
{ "result": { "resultId": "b433d5b1e3125ff3", "resultStatus": "SUCCESSFUL", "executionStatus": "COMPLETED", "input": { "generalParameters": { "timeframe": "unknown-unknown", "logVerbosity": "WARNING", "resolveDimensionalQueryData": false }, "forecastHorizon": 10, "timeSeriesData": { "expression": "timeseries avg(dt.host.cpu.usage)" }, "coverageProbability": 0.9, "nPaths": 200 }, "output": [ { "timeSeriesDataWithPredictions": { "records": [ { "dt.davis.forecast:lower": [ 20.302533297777046, 20.30119956974749, 20.299826093391346, 20.298413637147934, 20.296962988044072, 20.295474948510375, 20.293950333306114, 20.29238996657088, 20.290794679018166, 20.289165305282822 ], "dt.davis.forecast:upper": [ 20.531565739653274, 20.5316575385106, 20.53178908569177, 20.531959612757507, 20.532168332681056, 20.53241444303185, 20.532697129050682, 20.53301556659801, 20.533368924960413, 20.53375636950308 ], "dt.davis.forecast:point": [ 20.4170495226752, 20.416428558113733, 20.41580759355227, 20.415186628990803, 20.414565664429336, 20.41394469986787, 20.413323735306403, 20.412702770744936, 20.412081806183473, 20.411460841622006 ], "interval": "60000000000", "timeframe": { "end": "2023-04-03T05:42Z", "start": "2023-04-03T05:32Z" }, "dt.davis.internal.dataName": "avg(dt.host.cpu.usage)" } ], "types": [ { "indexRange": [0, 0], "mappings": { "dt.davis.forecast:lower": { "type": "array", "types": [ { "indexRange": [0, 9], "mappings": { "element": { "type": "double" } } } ] }, "timeframe": { "type": "timeframe" }, "dt.davis.forecast:upper": { "type": "array", "types": [ { "indexRange": [0, 9], "mappings": { "element": { "type": "double" } } } ] }, "dt.davis.forecast:point": { "type": "array", "types": [ { "indexRange": [0, 9], "mappings": { "element": { "type": "double" } } } ] }, "interval": { "type": "duration" }, "dt.davis.internal.dataName": { "type": "string" } } } ] }, "forecastQualityAssessment": "valid", "analysisStatus": "OK", "analyzedTimeSeriesQuery": { "expression": "timeseries avg(dt.host.cpu.usage)", "timeframe": { "startTime": "2023-04-03T03:31:32.718Z", "endTime": "2023-04-03T05:31:32.718Z" } } } ] }}
`

### Related links

---

## services/grail-service

`/develop/platform-services/services/grail-service/`

- Services
- Grail service

## Grail service

- Explanation
- 8-min readGrail provides APIs to store and query data, including but not limited to events, logs, and metrics.

### Concepts

You need to know the following concepts to work with Grail.

#### Grail Query API

The Grail Query API is the entry point for querying data stored in Grail.

You can query data in Grail using the . To write queries, you use Dynatrace Query Language (DQL).

There are two types of operations the Grail Query API offers:

- Query execution lets the client start queries, cancel a running query, and fetch query results.

- Language services support writing DQL queries and provide syntax information.

#### Query execution

The Grail Query API executes queries asynchronously via REST.

The final result is guaranteed to be available for one minute after the query has finished, so we strongly recommend a polling interval of less than one minute.

Query start: You start a DQL query by sending an `HTTP POST` request. The query and all corresponding parameters are part of the request body in the JSON. For the following requests, you need to include the `request-token` as a query parameter to reference the started query.

Polling and long polling: You can use `request-token` to poll queries. The response to a polling request contains the query's status.

- Long polling: When starting a query and polling operation, you can specify a `request-timeout`. If the final result or a preview is available before the specified timeout, the API returns the response; otherwise, it returns the state of the query.

Preview: You can enable previews within the initial request. The following polling responses will contain new previews if they're available. A new preview will always be whole, not as a delta to any previous preview.

Cancel: You can cancel a query using the `request-token` from the response to the initial request. If the query has finished, you'll get the final result as a response to the cancellation request. If the query is still being executed, Grail will stop execution and discard the result.

Metadata: The API returns metadata in addition to the query result. Some metadata types are always part of the response, while you must explicitly request others by setting the `enrich` parameter to specify the list of the requested metadata types.

The API provides the following metadata types:

 |
 | Metadata | Description
 | `grail` | The Grail metadata is always added and gives meta-information about the query execution.
 | `metrics` | You can request metric metadata by adding the `?enrich=metric-metadata` parameter to `/query:execute` and `/query:poll` requests. Suppose the query result has metric keys (for example, `dt.host.disk.free` ). In that case, the response will include an additional metadata section called `metrics` with information about those metrics, such as their units and display names.

Endpoints: These are the endpoints for starting queries and fetching the current status, including the final result and query cancellation.

 |
 | Endpoint | Description
 | `/query:execute` | Starts a Grail query.
 | `/query:poll` | Retrieves the query status and the final result from Grail.
 | `/query:cancel` | If the query has finished: returns the result. If the query has not finished: cancels the query and discards the result.

#### Grail language services

The language services support you in writing DQL queries.

Endpoints:

 |
 | Endpoint | Description
 | `/query:verify` | Checks a DQL query without executing it and returns a response with error messages if the query is invalid.
 | `/query:parse` | Creates a tree of the query's canonical form. Nodes contain references to the related token positions in the DQL query string. It can be used for hover effects, marking optional items, displaying canonical forms, and more.
 | `/query:autocomplete` | Creates a list of suggestions for the query at the given cursor position.

#### Filter segments

Filter segments allow you to segment data in Grail, enhancing data analytics and troubleshooting by providing the necessary focus. They use query-time filtering to limit the results of consumer queries to selected segments.

To create a filter segment, follow the steps outlined in the documentation. Once you have created a filter segment and obtained its ID, you can use it in your queries.

If the request defines multiple segments, they will be combined using the `AND` boolean operator, and the Grail data will be filtered accordingly. The values defined in the request will replace the variables used in the filter segments.

#### Permissions

To query data stored in Grail, you need to define permissions using Dynatrace's IAM policies. A typical IAM permission follows this structure:

`tsx
ALLOW WHERE (AND ...)
`

- `ALLOW`—grants the specified action (e.g., `storage:buckets:read`).

- `WHERE`—specifies the conditions under which the action is allowed.

- —represents a field or attribute being evaluated (e.g., `storage:bucket-name`).

- —defines how the condition is compared to the value (e.g., =, IN, STARTSWITH).

- —the value being compared (e.g., `"default_logs"`).

- `AND`/`OR`—combines multiple conditions logically

##### Supported operators

The operators available depend on the specific permission type or condition you use. These are all the available operators:

`=`—checks whether the condition equals the specified value. For example:

`tsx
ALLOW storage:logs:read WHERE storage:bucket-name = "default_logs"
`

`IN`—checks whether the condition matches any value in a list. For example:

`tsx
ALLOW storage:buckets:read WHERE storage:bucket-name IN ("default_logs", "default_metrics")
`

`STARTSWITH`—checks whether the condition starts with the specified value. For example:

`tsx
ALLOW storage:logs:read WHERE storage:bucket-name STARTSWITH "default"
`

`!=`—checks whether the condition does not equal the specified value. For example:

`tsx
ALLOW storage:logs:read WHERE storage:bucket-name != "restricted_logs"
`

`NOT IN`—checks whether the condition does not match any value in a list. For example:

`tsx
ALLOW storage:buckets:read WHERE storage:bucket-name NOT IN ("restricted_logs", "sensitive_logs")
`

`NOT STARTSWITH`—checks whether the condition does not start with the specified value. For example:

`tsx
ALLOW storage:logs:read WHERE storage:bucket-name NOT STARTSWITH "restricted"
`

`MATCH`—checks whether the condition matches a specific pattern. For example:

`tsx
ALLOW storage:logs:read WHERE storage:bucket-name MATCH ("default-*", "security_logs")
`

##### Permission types

You need to have the correct permissions to query data stored in Grail. Grail stores records in Grail buckets and assigns each bucket to a table.

Bucket permissions: A typical bucket read permission looks like this: `ALLOW storage:buckets:read;`. Adding this permission grants access to all buckets. You need table permissions in addition to this to access Grail data. Without proper table permissions, it won't be accessible.

Bucket permissions can also be conditional, depending on which buckets you want to make accessible. The following conditional permission give access to buckets with the names `default_logs` and `default_metrics`.

`tsx
ALLOW storage:buckets:read WHERE storage:bucket-name IN ("default_logs", "default_metrics");
`

Conditions support the following operators: `=`, `IN`, `STARTSWITH`, `!=`, `NOT IN`, `NOT STARTSWITH` and `MATCH`.

Table permissions: Grail has pre-defined tables whose permissions you can define as follows, for example:

- `ALLOW storage:metrics:read;`,

- `ALLOW storage:logs:read;`,

- `ALLOW storage:events:read;`,

- `ALLOW storage:system:read;`,

- and so on.

These permissions grant access to the table. In order to read the data stored in the buckets, you also need to add bucket permissions.
A few tables have unrestricted access and don't need bucket or table permissions, such as `dt.system.data_objects`.

Record-level permissions: You can restrict table permissions at the record level by adding conditions to certain predefined fields. Adding conditions restricts access to only the records that satisfy the condition.

The following record-level permission grants access to only those records in the metrics table that have the metric key `dt.host.cpu.load`.

`tsx
ALLOW storage:metrics:read WHERE storage:metric.key = "dt.host.cpu.load";
`

Conditions support the following operators: `=`, `IN`, `STARTSWITH` and `MATCH`.

Use the `AND` operator to join multiple conditions.

`tsx
ALLOW storage:logs:read WHERE storage:log.source STARTSWITH "/var/log" AND storage:host.name IN ("host1", "host2");
`

If a table has many associated statements, they're they're processed with the logical `OR`. The following set of conditional table permissions grant access to those records in the `events` table that have
an event type of `PROCESS_RESTART` OR an event kind of `DAVIS_EVENT`.

`tsx
ALLOW storage:events:read WHERE storage:event.type = "PROCESS_RESTART";ALLOW storage:events:read WHERE storage:event.kind = "DAVIS_EVENT";
`

Unconditional table permissions override conditional table permissions on the same table. The following set of permissions grants access to all records in the `events` table:

`tsx
ALLOW storage:events:read WHERE storage:event.type = "PROCESS_RESTART";ALLOW storage:events:read;
`

As with table permissions, you must combine them with bucket permissions to access data stored in the buckets.

Bucket scope permissions: You can combine bucket- and record-level permissions to grant access to specific records only if they're located in the designated buckets.

The following permissions will provide access to all logs in the `unrestricted_logs` bucket and only specific records in the `restricted_logs` bucket:

`tsx
ALLOW storage:buckets:read;ALLOW storage:logs:read WHERE storage:bucket-name = "unrestricted_logs";ALLOW storage:logs:read WHERE storage:bucket-name = "restricted_logs" AND storage:dt.security_context = "TeamA";
`

A `storage:bucket-name` condition on table- or record-level permissions will work only if the user has access to the specified bucket.
The following permissions won't provide any access to logs because the user has no access to the `unrestricted_logs` or `restricted_logs` buckets, resulting in an empty query result:

`tsx
ALLOW storage:buckets:read WHERE storage:bucket-name STARTSWITH "default"ALLOW storage:logs:read WHERE storage:bucket-name = "unrestricted_logs";ALLOW storage:logs:read WHERE storage:bucket-name = "restricted_logs" AND storage:dt.security_context = "TeamA";
`

Conditions support the following operators on `storage:bucket-name`: `=`, `IN`, `STARTSWITH`, `!=`, `NOT IN`, `NOT STARTSWITH` AND `MATCH`.

Fieldset: A fieldset is a collection of fields with a unique name. You define them on a bucket, table, or environment scope.
There are two predefined fieldsets for the spans table: `builtin-request-attributes-spans` and `builtin-sensitive-spans`.
Likewise, there is one for the tables `user.events` and `user.sessions`: `builtin-sensitive-user-events-and-sessions`.

The fields in `builtin-request-attributes-spans` are dynamically generated through request attributes.
The fields in `builtin-sensitive-spans` and `builtin-sensitive-user-events-and-sessions` are static:

`builtin-sensitive-spans`

- `client.ip`

- `db.connection_string`

- `http.request.header.referer`

- `http.request.header.proxy-authorization`

- `http.request.header.authorization`

- `http.request.header.api-key`

- `http.request.header.x-xsrf-token`

- `url.full`

- `url.query`

- `db.query.parameters`

`builtin-sensitive-user-events-and-sessions`

- `client.ip`

- `dt.rum.user_tag`

- `geo.location.latitude`

- `geo.location.longitude`

- `user.identifier`

You can create custom fieldsets to hide fields containing sensitive data via the
.

Fieldset permissions: A typical fieldset read permission looks like `ALLOW storage:fieldsets:read;`. Adding this permission grants access to all sensitive fields.

Fieldset permissions can also be conditional based on the buckets and tables where access to sensitive fields is required.

The following conditional permission gives access to sensitive fields on buckets with the name `default_spans` and `sensitive_spans`.

`tsx
ALLOW storage:fieldsets:read WHERE storage:bucket-name IN ("default_spans", "sensitive_spans");
`

The following conditional permission gives access to sensitive fields on the `spans` table.

`tsx
ALLOW storage:fieldsets:read WHERE storage:table-name = "spans";
`

The following conditional permission gives access to sensitive fields with the fieldset named `builtin-sensitive-spans`.

`tsx
ALLOW storage:fieldsets:read WHERE storage:fieldset-name = "builtin-sensitive-spans";
`

If a field is defined in multiple fieldsets and you don't have permission for all of them, you won't have access to that field.

Currently, conditions support the following operators: `=`, `IN`, `STARTSWITH`, `!=`, `NOT IN`, `NOT STARTSWITH` and `MATCH`.

Endpoints:

 |
 | Endpoint | Permission Handling
 | `/query:execute` | Requires bucket and table permissions.
 | `/query:poll` | Permissions to execute the request apply. Only the user that started the query can poll.
 | `/query:cancel` | Permissions to execute the request apply. Only the user that started the query can cancel.
 | `/query:verify` | Requires table permissions.
 | `/query:parse` | Requires table permissions.
 | `/query:autocomplete` | Requires bucket and table permissions.

### Related links

- Dynatrace Query Language documentation

- Manage user permissions with IAM policies

- Bucket and table permissions in Grail

- Allowed conditions on the bucket and table permissions

- Field permissions

---

## services/notification-service

`/develop/platform-services/services/notification-service/`

- Services
- Notification service

## Notification service

- Explanation
- 3-min readThe notification service manages notification configurations. You can use it to allow your users to register email notifications in your app. Events related to a resource your app presents or any event recognized in the Dynatrace platform may trigger these notifications.

### Concepts

You need to know the following concepts to work with the notification service.

#### Notifications

Notifications are emails sent to a user, triggered by an event. A notification configuration defines which event triggers a notification related to a resource of your domain and how this notificaiton looks like.

#### Notification configurations

A notification is sent based on a notification configuration.

A notification configuration is defined via the notification service API and the notification template as a static asset in your app. The default approach to registering/unregistering a notification configuration is to use the NotifyButton the Strato design system offers. You can use the notifications-client-v2 SDK to customize the behavior to your needs.

While all notification configurations are about events and the resource they are about, there are two types of notification configurations, resource and event notification configurations.

##### Resource notifications

A resource notification configuration is streamlined to cover notifcations that are always triggered by the same events and only differ in the resource selection (e.g. a document change, a workflow change, an app release, ...). This is also the main use case for notifications.

- A resource ID that identifies the relevant resource. Together with the notification type, you can use this to look up a notification configuration.

- The notification type that associates the notification template with the notification configuration.

- The base query and resource_attribute the notification service shall use to build the trigger configuration.

- The notification template defines the email's subject and body text.

###### Resource notification template example

`tsx
event_type: dt.system.eventsbase_query: event.provider == "AUTOMATION_ENGINE" AND event.type == "WORKFLOW_DELETED"resource_attribute: dt.automation_engine.workflow.idsubject: Workflow "{{ event()["dt.automation_engine.workflow.title"] }} has been deletedcontent: Workflow "{{ (workflow_title) }}" ({{ (event()["dt.automation_engine.workflow.id"]) }}) was deleted by {{ user(event()["user.id"])["name"] }}.
`

Properties available for `event()` depend on the events matching your notification trigger configuration.

##### Event notifications

Event notifications are for use cases where event selection is part of the user's input in the use case. For example, to notify about problem-type events, as filtered by the user. There is an associated resource, such as a filter id, for looking up the notification configuration. The app owner is responsible for managing the event filter and related event notification configuration.

- A resource ID that identifies the relevant resource. Together with the notification type, you can use this to look up a notification configuration.

- The notification type that associates the notification template with the notification configuration.

- The trigger configuration defines which event(s) trigger a notification.

- The notification template defines the email's subject and body text.

Any notification configuration is always implicitly associated with the user who clicked the NotifyButton and the app where the request originated.

##### Event notification template example

An event notification template is similar to the resource notification template but omits everything but `subject` and `content`

#### Resource ID

The resource ID identifies which resource the notification is about (for example, an app ID for app update notifications, or a workflow ID for workflow change notifications). Together with the notification type, you can use the resource ID to determine whether there is a notification configuration for the user and app.

#### Notification type

The notification type is a string that allows users to differentiate between multiple types of notifications in the context of one app. It can associate a notification with a template, see Notification template.

#### Notification template

The notification template defines the properties of a notification configuration that the notification service resolves (e.g. subject and body of the email to send). For details please check resource and event notification configurations above.

The notification service expects a JSON or YAML file in your app's static asset folder. The filename must follow the convention `{notification_type}.notification.json|yaml` and can be either in JSON or YAML format.

The service supports Markdown syntax to format the content in the notification body.

The subject and body may contain expressions to define the content dynamically, for example, by referencing attributes of the triggering event. The expressions are a subset of the expressions supported by the AutomationEngine:

- `environment()`

- `event()`

- `now()`

- `timedelta()`

Additionally the following expressions are supported for notification configurations:

`owner()` - returns the uuid of the owner of the notification configuration ie. the user who created the notification configuration. This allows for example to avoid sending notifications to the owner by using the expression in the base query of a resoure notification (e.g. workflow change event only if the owner is not the editor of the change)
Example:

`tsx
{{ owner() }}# results incfb56028-f1b6-4819-8567-308cec8d9173
`

`user(userId)` - returns human readable user information for a given uuid of a user.
Example:

`tsx
{{ user("cfb56028-f1b6-4819-8567-308cec8d9173") }}# results in{ "id": "cfb56028-f1b6-4819-8567-308cec8d9173", "email": "jane.doe@sample.com", "name": "Jane Doe", "displayName": "Jane Doe (jane.doe@sample.com)"}
`

`problem_link()` - returns URL to a Davis problem in the Problems app.
Example:

`tsx
{{ problem_link() }}# results in"https://xyz12345.apps.dynatrace.com/ui/apps/dynatrace.davis.problems/problem/20d01063-14d7-4b99-aef1-77e92962fb7f"
`

For details, refer to the AutomationEngine expression reference.

#### Trigger configuration

The trigger configuration defines which events trigger sending an email to the user. Check out the notification-client SDK and .

#### Notify button

The Strato Design System offers a NotifyButton that allows users to register and unregister a self-notification. Look at the component documentation for details.

### Limitations

- The notification service limits the number of emails sent to a user to

- 30 per user per app per hour for event notifications

- 10 per user per app per resource per hour for resource notifications
An email notifies the user when they hit this limitation.

- The number or notification configurations are limited to

- 60 per user per app for resource notifications

- 30 per user per app for event notifications

### Related links

- (deprecated)

---

## services/platform-management-service

`/develop/platform-services/services/platform-management-service/`

- Services
- Platform management service

## Platform management service

- Explanation
- 2-min readThe Platform Management Service (PMS) can retrieve license and settings information in a Dynatrace environment.

### Concepts

You need to know the following concepts to work with the PMS.

#### License

Every environment has some information related to the license. This license API includes the following:

- `trial`: A boolean value that tells whether an environment is a trial environment.

- `platformSubscription`: A boolean that tells whether an environment has an enabled Dynatrace Platform Subscription (DPS) license.

#### License settings

Every environment has license-related settings represented by a list of key and value pairs available at `/environment/license/settings`.

#### Environment

Technical information about the environment is provided, such as:

- `environmentId`: the actual environment ID corresponding to the canonical URL of `.apps.dynatrace.com`

- `createTime`: timestamp in ISO 8601 of when the environment was created.

#### Environment settings

Every environment has some settings that include the following:

- `chatEnabled`: A boolean that tells if the chat feature is active for the environment.

- `countryCode`: An ISO3166-1 alpha-2 two letter country code. For further details, visit Wikipedia.

#### Environment effective permissions

Environment effective permissions provide information on whether the calling user has specific IAM permissions (or scopes) for the environment as listed in the IAM service reference page.

As explained in Authentication, access to Dynatrace API endpoints is only allowed if the calling user is granted the corresponding scope using some policy and group assignment.
You can use the `effective-permissions` endpoint or the corresponding SDK method to check a user's permissions before calling the endpoint guarded by that scope. For more information, visit the Query user permissions guide and learn how to use the SDK.

TipYou can query app settings permissions using the `client-app-settings-v2` SDK or the `useEffectivePermissionsV2` React hook.

### Related links

- Typescript SDK

- Query user permissions

---

## services/state-service

`/develop/platform-services/services/state-service/`

- Services
- State service

## State service

- Explanation
- 3-min readThe state service provides a key-value storage for your app to store internal states.

It can store essential data needed for the app's functioning in its context. Data access is configurable: either to all users or confined to a specific user's context.
These states are only accessible from their respective apps and can't be accessed using a different app or ad-hoc functions.

If the data set is extensive (see Limitations) or multiple users need to collaborate on the data, the document service may be a better fit.

### Concepts

You need to know the following concepts to work with the state service.

#### User app states

You can use user app states to store information that is relevant only to a specific user and app context. For example, the configurable state of components that are used in your app. User app states persist across that user's sessions and devices.

#### App states

CautionBe aware that all app users can read app states. If your use case allows for a user-scoped state, best practice is to use the the user app state.
App states are accessible to all users; therefore, you can share specific states essential to the app's context. For example, you can create a workflow that fetches third-party data into your app function. Your app stores this information in its app state. All users of your app can then access this data.

There are also use cases for writing an app state in browser code. For example, the app can allow the user to share some meta information (that is only relevant in the context of this app) with other users.

#### Limitations

Generic key-value-based state storage, where the key and value are simple strings, allows you to manage the state design according to your app's specific needs.

For example, instead of using multiple small chunks of state, you can use one more significantly larger state as an alternative. The limits the app must abide by for either case are listed below.

- User app states: The sum of all user app state values for a single user must not exceed 1 MB per app. User app state keys must not exceed 200 characters.

- App states: A single app state value must not exceed 10 MB. The sum of all app state values for a single app must not exceed 50 MB. An app state key must not exceed 200 characters.

Any operation violating these limits will result in an error. You can delete states to avoid imminent quota violations.

#### Reset states

Administrators (users with the policy "AppEngine - Admin") can clear all app states and user app states of an app in the by selecting the Reset state context menu entry. In addition, any user can also trigger the clearance of their user app states.

### Related links

- Typescript SDK

- How to store app and user states
