# @dynatrace-sdk/client-hub

Source: <https://developer.dynatrace.com/develop/sdks/client-hub/v2/> (latest: `client-hub/v2`).

## client-hub/v2

`/develop/sdks/client-hub/v2/`

- SDK for TypeScript
- Hub
- V2

## Hub
The Hub API provides catalog content, such as Dynatrace Apps, Extensions, and Technologies, in the context of the current environment.

 @dynatrace-sdk/client-hub v2.0.0 

`tsx
npm install @dynatrace-sdk/client-hub
`

### appsClient

`tsx
import { appsClient } from '@dynatrace-sdk/client-hub';
`

#### getAppDetails

appsClient.getAppDetails(config): PromiseDetail>Provides detailed information about an appRequired scope: hub:catalog:read

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | A list of fields that are added to the default set of fields.
 | config.id*required | string |

##### Returns
 |
 | Return type | Status code | Description
 | Detail | 200 | Detailed information about an app

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { appsClient } from "@dynatrace-sdk/client-hub";const data = await appsClient.getAppDetails({ id: "..." });
`

#### getAppOverviewList

appsClient.getAppOverviewList(config): PromiseOverviewsList>List overview information of all appsRequired scope: hub:catalog:read

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | A list of fields that are added to the default set of fields.
 | config.onlyCompatible | boolean | Filters apps and their releases to exclude incompatible instances. If true or missing the resulting releases will have compatibility of COMPATIBLE or UNKNOWN.

##### Returns
 |
 | Return type | Status code | Description
 | OverviewsList | 200 | A list of overview information

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { appsClient } from "@dynatrace-sdk/client-hub";const data = await appsClient.getAppOverviewList();
`

#### getAppReleases

appsClient.getAppReleases(config): PromiseReleasesList>Provides a list of releases published for an app, including revoked releasesRequired scope: hub:catalog:read

##### Parameters
 |
 | Name | Type
 | config.addFields | Array
 | config.id*required | string

##### Returns
 |
 | Return type | Status code | Description
 | ReleasesList | 200 | A list of releases

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { appsClient } from "@dynatrace-sdk/client-hub";const data = await appsClient.getAppReleases({ id: "..." });
`

### categoriesClient

`tsx
import { categoriesClient } from '@dynatrace-sdk/client-hub';
`

#### getCategories

categoriesClient.getCategories(config): PromiseCategories>List Hub categories, including the IDs of the associated items and their content blocks if anyRequired scope: hub:catalog:read

##### Returns
 |
 | Return type | Status code | Description
 | Categories | 200 | The categories

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { categoriesClient } from "@dynatrace-sdk/client-hub";const data = await categoriesClient.getCategories();
`

### extensionsClient

`tsx
import { extensionsClient } from '@dynatrace-sdk/client-hub';
`

#### getExtensionDetails

extensionsClient.getExtensionDetails(config): PromiseDetail>Provides detailed information about an extensionRequired scope: hub:catalog:read

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | A list of fields that are added to the default set of fields.
 | config.id*required | string |

##### Returns
 |
 | Return type | Status code | Description
 | Detail | 200 | Detailed information about an extension

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { extensionsClient } from "@dynatrace-sdk/client-hub";const data = await extensionsClient.getExtensionDetails({ id: "...",});
`

#### getExtensionOverviewList

extensionsClient.getExtensionOverviewList(config): PromiseOverviewsList>List overview information of all extensionsRequired scope: hub:catalog:read

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | A list of fields that are added to the default set of fields.
 | config.onlyCompatible | boolean | A flag to reduce the list to only include compatible extensions with their latest compatible version.

##### Returns
 |
 | Return type | Status code | Description
 | OverviewsList | 200 | A list of overview information

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { extensionsClient } from "@dynatrace-sdk/client-hub";const data = await extensionsClient.getExtensionOverviewList();
`

#### getExtensionReleases

extensionsClient.getExtensionReleases(config): PromiseReleasesList>Provides a list of releases published for an extension, including revoked releasesRequired scope: hub:catalog:read

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | A list of fields that are added to the default set of fields.
 | config.id*required | string |

##### Returns
 |
 | Return type | Status code | Description
 | ReleasesList | 200 | A list of releases

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { extensionsClient } from "@dynatrace-sdk/client-hub";const data = await extensionsClient.getExtensionReleases({ id: "...",});
`

### technologiesClient

`tsx
import { technologiesClient } from '@dynatrace-sdk/client-hub';
`

#### getTechnologyDetails

technologiesClient.getTechnologyDetails(config): PromiseDetail>Provides detailed information about a technologyRequired scope: hub:catalog:read

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | A list of fields that are added to the default set of fields.
 | config.id*required | string |

##### Returns
 |
 | Return type | Status code | Description
 | Detail | 200 | Detailed information about a technology

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { technologiesClient } from "@dynatrace-sdk/client-hub";const data = await technologiesClient.getTechnologyDetails({ id: "...",});
`

#### getTechnologyOverviewList

technologiesClient.getTechnologyOverviewList(config): PromiseOverviewsList>List overview information of all technologiesRequired scope: hub:catalog:read

##### Parameters
 |
 | Name | Type | Description
 | config.addFields | Array | A list of fields that are added to the default set of fields.
 | config.onlyCompatible | boolean | A flag to reduce the list to only include compatible technologies.

##### Returns
 |
 | Return type | Status code | Description
 | OverviewsList | 200 | A list of overview information

##### Throws
 |
 | Error Type | Error Message
 | ErrorResponse | An error occurredCode example
`tsx
import { technologiesClient } from "@dynatrace-sdk/client-hub";const data = await technologiesClient.getTechnologyOverviewList();
`

### Types

#### AssetCount

 |
 | Name | Type
 | total*required | number

#### Author

 |
 | Name | Type
 | icon | string
 | name*required | string
 | salesEmail | string
 | salesLink | string
 | supportEmail | string
 | supportLink | string

#### Categories

 |
 | Name | Type
 | categories*required | ArrayCategory>

#### Category

An item category in the Hub

 |
 | Name | Type | Description
 | id*required | string | The category's ID
 | itemIds*required | Arraystring> | The IDs of the items associated with this category
 | page*required | CategoryPage |
 | subgroup*required | string | Groups categories to related subpages

#### CategoryPage

 |
 | Name | Type | Description
 | content*required | ArrayCategoryPageContent> |
 | description*required | string | The customer facing description of this page
 | shortTitle*required | string | A shorter version of the customer facing title of the page
 | title*required | string | The customer facing title of the page

#### CategoryPageContent

 |
 | Name | Type | Description
 | blocks | ArrayCategoryPageContentBlock> | The blocks of the items associated with this category
 | contentType*required | "section" | "curated_content_block" | "content_block_group" | "browse_all_block" | The type of content
 | description*required | string | The customer facing description of the content
 | itemIds | Arraystring> | The IDs of the items associated with this category
 | title*required | string | The customer facing title of the content

#### CategoryPageContentBlock

 |
 | Name | Type | Default
 | description | string | `""`
 | href*required | string |
 | hrefText | string |
 | image*required | string |
 | title*required | string |

#### ConstraintViolation

Contains information about a constraint violation caused by invalid input.

 |
 | Name | Type | Description
 | message*required | string | The constraint violation description message
 | path | string | The path of the parameter that caused the constraint violation

#### ContentCount

 |
 | Name | Type
 | actions | AssetCount
 | documents | DocumentCount
 | settings | AssetCount

#### Dependency

 |
 | Name | Type | Description
 | name*required | string | The name of the required dependency
 | version*required | string | SemVer2 version of the required dependency

#### Detail

Meta data of the latest version of this item.

 |
 | Name | Type | Description
 | author | Author |
 | comingSoon*required | boolean |
 | contentCount | ContentCount |
 | createdTime | Date | The time this Hub item was originally created.
 | currentRelease | Release |
 | description*required | string |
 | detailSections*required | ArrayDetailSection> |
 | hasDetailSection*required | boolean | Whether the details of this item contain one or more detail content sections.
 | hubItemId | string | The Hub item id, aka. slug.
 | icon | string |
 | id*required | string | The id is only unique within a specific type.
 | keywords*required | Arraystring> |
 | links | ArrayLink> |
 | name*required | string |
 | relatedItems | ArrayOverview> |
 | releaseTime | Date | The time this latest version of the item was released.
 | resourceContext | ResourceContext |
 | type*required | "APP" | "CLASSIC_APP" | "EXTENSION_2" | "TECHNOLOGY" |
 | version | string | The latest version of this item.

#### DetailSection

Can be either a Markdown or Gallery section. Only one of the respective properties is returned (`markdown`, or `gallery`).

 |
 | Name | Type
 | gallery | GallerySection
 | markdown | MarkdownSection
 | sourceId*required | string

#### DocumentCount

 |
 | Name | Type
 | total*required | number
 | types | DocumentCountTypes

#### DocumentCountTypes

type: Record

#### Error

Standard error response

 |
 | Name | Type | Description
 | code*required | number | The error code (HTTP response)
 | details | ErrorDetails | Optional details of the error
 | message*required | string | The error code (HTTP response)

#### ErrorDetails

Optional details of the error

 |
 | Name | Type | Description
 | constraintViolations | ArrayConstraintViolation> | A list of constraint violations of input parameters (path, query, request body)

#### ErrorEnvelope

 |
 | Name | Type | Description
 | error*required | Error | Standard error response

#### ExtensionMetadata

 |
 | Name | Type
 | extensionContents | any
 | featureSets | Arraystring>
 | featureSetsDetails | Recordstring | any>

#### GalleryImage

 |
 | Name | Type | Description
 | alt | string | Descriptive text of what the image expresses
 | caption | string |
 | resolutions | GalleryImageResolutions |
 | src*required | string |
 | title | string |

#### GalleryImageResolutions

type: Record

#### GallerySection

 |
 | Name | Type
 | images*required | ArrayGalleryImage>
 | title*required | string

#### Link

 |
 | Name | Type | Description
 | appId | string |
 | pageToken | string |
 | target | string |
 | type*required | "DOCUMENTATION" | "MARKETING" | "ACTIVATION" | "REPOSITORY" | Links can be of the following types:

- `DOCUMENTATION` - Technical documentation
- `MARKETING` - Promotion material
- `ACTIVATION` - Location within the product to configure the item
- `REPOSITORY` - Source code repository

#### Manifest

 |
 | Name | Type | Default
 | actions | any |
 | contentCount | ContentCount |
 | csp | any |
 | dependencies*required | ArrayDependency> |
 | documents | any |
 | hidden*required | boolean | `false`
 | intents | any |
 | pageTokens | any |
 | scopes | ArrayManifestScope> |
 | settings | any |

#### ManifestScope

 |
 | Name | Type
 | comment*required | string
 | name*required | string

#### MarkdownSection

 |
 | Name | Type
 | markdown*required | string
 | title*required | string
Meta data of the latest version of this item.

 |
 | Name | Type | Description
 | author | Author |
 | comingSoon*required | boolean |
 | contentCount | ContentCount |
 | createdTime | Date | The time this Hub item was originally created.
 | description*required | string |
 | hasDetailSection*required | boolean | Whether the details of this item contain one or more detail content sections.
 | hubItemId | string | The Hub item id, aka. slug.
 | icon | string |
 | id*required | string | The id is only unique within a specific type.
 | keywords*required | Arraystring> |
 | links | ArrayLink> |
 | name*required | string |
 | releaseTime | Date | The time this latest version of the item was released.
 | resourceContext | ResourceContext |
 | type*required | "APP" | "CLASSIC_APP" | "EXTENSION_2" | "TECHNOLOGY" |
 | version | string | The latest version of this item.

#### OverviewsList

A list of item meta data. Per default contains only compatible items, but can be controlled using the onlyCompatible flag.

 |
 | Name | Type
 | items*required | ArrayOverview>

#### Release

 |
 | Name | Type | Description
 | compatible*required | "COMPATIBLE" | "INCOMPATIBLE" | "UNKNOWN" |
 | contentCount | ContentCount |
 | extensionDocuments | any |
 | extensionMetadata | ExtensionMetadata |
 | manifest | Manifest |
 | publicationTime*required | Date |
 | releaseNotes | string | Markdown content describing this release.
 | revocation | Revocation | The existence of this object marks a release as being revoked. It contains information on why this is the case.
 | version*required | string | A semantic versioning 2.0 conform version.

#### ReleasesList

 |
 | Name | Type
 | releases*required | ArrayRelease>

#### ResourceContext

 |
 | Name | Type
 | operations | Array

#### Revocation

The existence of this object marks a release as being revoked. It contains information on why this is the case.

 |
 | Name | Type
 | description | string
 | reason*required | "SECURITY_ISSUE" | "FAULTY_RELEASE" | "DEPRECATED"
 | severity | "LOW" | "MEDIUM" | "HIGH"

### Enums

#### CategoryPageContentContentType

⚠️ Deprecated
Use literal values.

The type of content

##### Enum keys
`BrowseAllBlock` | `ContentBlockGroup` | `CuratedContentBlock` | `Section`

#### Compatibility

⚠️ Deprecated
Use literal values.

##### Enum keys
`Compatible` | `Incompatible` | `Unknown`

#### ItemType

⚠️ Deprecated
Use literal values.

##### Enum keys
`App` | `ClassicApp` | `Extension_2` | `Technology`

#### LinkType

⚠️ Deprecated
Use literal values.

Links can be of the following types:

- `DOCUMENTATION` - Technical documentation

- `MARKETING` - Promotion material

- `ACTIVATION` - Location within the product to configure the item

- `REPOSITORY` - Source code repository

##### Enum keys
`Activation` | `Documentation` | `Marketing` | `Repository`

#### OptionalAppDetailField

⚠️ Deprecated
Use literal values.

##### Enum keys
`ContentCount` | `HubItemId` | `Manifest` | `ResourceContext`

#### OptionalAppOverviewField

⚠️ Deprecated
Use literal values.

##### Enum keys
`ContentCount` | `HubItemId` | `ResourceContext`

#### OptionalAppReleaseField

⚠️ Deprecated
Use literal values.

##### Enum keys
`ContentCount` | `Manifest`

#### OptionalExtensionDetailField

⚠️ Deprecated
Use literal values.

##### Enum keys
`ContentCount` | `ExtensionDocuments` | `ExtensionMetadata` | `HubItemId`

#### OptionalExtensionOverviewField

⚠️ Deprecated
Use literal values.

##### Enum keys
`ContentCount` | `HubItemId`

#### OptionalExtensionReleaseField

⚠️ Deprecated
Use literal values.

##### Enum keys
`ContentCount` | `ExtensionDocuments` | `ExtensionMetadata`

#### OptionalTechnologyDetailField

⚠️ Deprecated
Use literal values.

##### Enum keys
`HubItemId`

#### OptionalTechnologyOverviewField

⚠️ Deprecated
Use literal values.

##### Enum keys
`HubItemId`

#### ResourceContextOperationsItem

⚠️ Deprecated
Use literal values.

##### Enum keys
`Install`

#### RevocationReason

⚠️ Deprecated
Use literal values.

##### Enum keys
`Deprecated` | `FaultyRelease` | `SecurityIssue`

#### RevocationSeverity

⚠️ Deprecated
Use literal values.

##### Enum keys
`High` | `Low` | `Medium`
