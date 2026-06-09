# @dynatrace-sdk/client-notification

Source: <https://developer.dynatrace.com/develop/sdks/client-notification/> (latest: `client-notification`).

## client-notification

`/develop/sdks/client-notification/`

- SDK for TypeScript
- Notification

## Notification
Manage self notifications with the Notification Service API. This is deprecated, use event notifications provided in the Notification Service v2 API instead.

 @dynatrace-sdk/client-notification v2.3.3 Latest (V2)

`tsx
npm install @dynatrace-sdk/client-notification
`

### selfNotificationsClient

`tsx
import { selfNotificationsClient } from '@dynatrace-sdk/client-notification';
`

#### createSelfNotification

⚠️ Deprecated

selfNotificationsClient.createSelfNotification(config): PromiseSelfNotification>Required scope: notification:self-notifications:write

##### Parameters
 |
 | Name | Type
 | config.body*required | SelfNotificationCreate

##### Returns
 |
 | Return type | Status code | Description
 | SelfNotification | 201 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { selfNotificationsClient } from "@dynatrace-sdk/client-notification";const data = await selfNotificationsClient.createSelfNotification({ body: { resourceId: "...", notificationType: "...", triggerConfiguration: { type: "event", value: { query: "..." }, }, }, });
`

#### deleteSelfNotification

⚠️ Deprecated

selfNotificationsClient.deleteSelfNotification(config): PromiseRequired scope: notification:self-notifications:write

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this self notification.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { selfNotificationsClient } from "@dynatrace-sdk/client-notification";const data = await selfNotificationsClient.deleteSelfNotification({ id: "...", });
`

#### getSelfNotification

⚠️ Deprecated

selfNotificationsClient.getSelfNotification(config): PromiseSelfNotification>Required scope: notification:self-notifications:read

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this self notification.

##### Returns
 |
 | Return type | Status code | Description
 | SelfNotification | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { selfNotificationsClient } from "@dynatrace-sdk/client-notification";const data = await selfNotificationsClient.getSelfNotification({ id: "...", });
`

#### getSelfNotifications

⚠️ Deprecated

selfNotificationsClient.getSelfNotifications(config): PromisePaginatedSelfNotificationList>Required scope: notification:self-notifications:read

##### Parameters
 |
 | Name | Type | Description
 | config.appId | string |
 | config.limit | number | Number of results to return per page.
 | config.notificationType | string |
 | config.offset | number | The initial index from which to return the results.
 | config.ordering | string | Which field to use when ordering the results.
 | config.owner | string |
 | config.resourceId | string |
 | config.search | string | A search term.

##### Returns
 |
 | Return type | Status code | Description
 | PaginatedSelfNotificationList | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { selfNotificationsClient } from "@dynatrace-sdk/client-notification";const data = await selfNotificationsClient.getSelfNotifications();
`

#### patchSelfNotification

⚠️ Deprecated

selfNotificationsClient.patchSelfNotification(config): PromiseSelfNotification>Required scope: notification:self-notifications:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | SelfNotificationUpdate |
 | config.id*required | string | A UUID string identifying this self notification.

##### Returns
 |
 | Return type | Status code | Description
 | SelfNotification | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { selfNotificationsClient } from "@dynatrace-sdk/client-notification";const data = await selfNotificationsClient.patchSelfNotification({ id: "...", body: { triggerConfiguration: { type: "event", value: { query: "..." }, }, }, });
`

#### updateSelfNotification

⚠️ Deprecated

selfNotificationsClient.updateSelfNotification(config): PromiseSelfNotification>Required scope: notification:self-notifications:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | SelfNotificationUpdate |
 | config.id*required | string | A UUID string identifying this self notification.

##### Returns
 |
 | Return type | Status code | Description
 | SelfNotification | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { selfNotificationsClient } from "@dynatrace-sdk/client-notification";const data = await selfNotificationsClient.updateSelfNotification({ id: "...", body: { triggerConfiguration: { type: "event", value: { query: "..." }, }, }, });
`

### Types

#### DavisEventConfig

 |
 | Name | Type | Description
 | customFilter | null | string | Additional DQL matcher expression to further filter events to match.
 | entityTags | null | EntityTags |
 | entityTagsMatch | "all" | "any" |
 | maintenanceWindowTriggerBehavior | "always" | "inside" | "outside" | default: `"always"`
 | names | null | ArrayDavisEventName> |
 | onProblemClose | boolean | Trigger on Davis event open only or also on close. default: `false`
 | typesDEPRECATED | null | Arraystring> |

#### DavisEventName

 |
 | Name | Type | Description
 | match*required | "equals" | "contains" | Davis event name must equal or contain the string provided.
 | name*required | string |

#### DavisEventTriggerConfig

 |
 | Name | Type
 | type*required | "davis-event"
 | value*required | DavisEventConfig

#### DavisProblemCategories

 |
 | Name | Type | Default
 | availability | boolean | `false`
 | custom | boolean | `false`
 | error | boolean | `false`
 | info | boolean | `false`
 | monitoringUnavailable | boolean | `false`
 | resource | boolean | `false`
 | slowdown | boolean | `false`

#### DavisProblemConfig

 |
 | Name | Type | Description
 | categories*required | DavisProblemCategories |
 | customFilter | null | string | Additional DQL matcher expression to further filter events to match.
 | entityTags | null | EntityTags |
 | entityTagsMatch | "all" | "any" |
 | onProblemClose | boolean | Trigger on Davis problem open only or also on close. default: `false`

#### DavisProblemTriggerConfig

 |
 | Name | Type
 | type*required | "davis-problem"
 | value*required | DavisProblemConfig

#### EntityTags

Entity tags to match by key and (optional) values. For example {"foo": [], "bar": ["a", "b", "c"]}

type: Record

#### Error

 |
 | Name | Type
 | code*required | number
 | details | ErrorDetails
 | message*required | string

#### ErrorDetails

 |
 | Name | Type
 | errorCode | string
 | errorRef | string

#### ErrorEnvelope

 |
 | Name | Type
 | error*required | Error

#### EventQuery

 |
 | Name | Type | Description
 | eventType | "events" | "bizevents" | "dt.system.events" | "security.events" | Grail event type.
 | query*required | string | DQL matcher expression defining which events to match.

#### EventQueryTriggerConfig

 |
 | Name | Type
 | type*required | "event"
 | value*required | EventQuery

#### ModificationInfo

 |
 | Name | Type
 | createdBy*required | null | string
 | createdTime*required | Date
 | lastModifiedBy*required | null | string
 | lastModifiedTime*required | Date

#### PaginatedSelfNotificationList

 |
 | Name | Type
 | count*required | number
 | results*required | ArraySelfNotification>

#### SelfNotification

 |
 | Name | Type | Description
 | appId | string | App id for registered notification. Optional, by default automatically inferred from the request. Only relevant for manual testing purposes via swagger.
 | id*required | string |
 | input | SelfNotificationInput | Input object consisting of subject and content. Supports automation expressions https://dt-url.net/workflows-expression-reference and markdown syntax. A template provided with an app ({notification_type}.notification-template.json) will take precedence over the input provided here.
 | modificationInfo*required | ModificationInfo |
 | notificationType*required | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | owner*required | string |
 | resourceId*required | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.
 | title | string |
 | triggerConfiguration*required | EventTriggerConfig |

#### SelfNotificationCreate

 |
 | Name | Type | Description
 | appId | string | App id for registered notification. Optional, by default automatically inferred from the request. Only relevant for manual testing purposes via swagger.
 | id | string |
 | input | SelfNotificationInput | Input object consisting of subject and content. Supports automation expressions https://dt-url.net/workflows-expression-reference and markdown syntax. A template provided with an app ({notification_type}.notification-template.json) will take precedence over the input provided here.
 | notificationType*required | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | resourceId*required | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.
 | title | string |
 | triggerConfiguration*required | EventTriggerConfig |

#### SelfNotificationInput

 |
 | Name | Type
 | content | null | string
 | subject | null | string

#### SelfNotificationUpdate

 |
 | Name | Type | Description
 | appId | string | App id for registered notification. Optional, by default automatically inferred from the request. Only relevant for manual testing purposes via swagger.
 | input | SelfNotificationInput | Input object consisting of subject and content. Supports automation expressions https://dt-url.net/workflows-expression-reference and markdown syntax. A template provided with an app ({notification_type}.notification-template.json) will take precedence over the input provided here.
 | notificationType | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | resourceId | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.
 | title | string |
 | triggerConfiguration | EventTriggerConfig |

#### EventTriggerConfig

type: EventQueryTriggerConfig | DavisProblemTriggerConfig | DavisEventTriggerConfig

### Enums

#### DavisEventNameMatch

⚠️ Deprecated
Use literal values.

Davis event name must equal or contain the string provided.

##### Enum keys
`Contains` | `Equals`

#### DavisEventTriggerConfigType

⚠️ Deprecated
Use literal values.

##### Enum keys
`DavisEvent`

#### DavisProblemTriggerConfigType

⚠️ Deprecated
Use literal values.

##### Enum keys
`DavisProblem`

#### EntityTagsMatch

⚠️ Deprecated
Use literal values.

Event must match all or any of the entity tags.

##### Enum keys
`All` | `Any`

#### EventQueryTriggerConfigType

⚠️ Deprecated
Use literal values.

##### Enum keys
`Event`

#### EventType

⚠️ Deprecated
Use literal values.

Grail event type.

##### Enum keys
`Bizevents` | `DtSystemEvents` | `Events` | `SecurityEvents`

#### MaintenanceWindowTriggerBehaviorType

⚠️ Deprecated
Use literal values.

Specifies when to trigger based on maintenance window status.

##### Enum keys
`Always` | `Inside` | `Outside`
