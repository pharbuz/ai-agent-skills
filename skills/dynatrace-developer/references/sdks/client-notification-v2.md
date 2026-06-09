# @dynatrace-sdk/client-notification-v2

Source: <https://developer.dynatrace.com/develop/sdks/client-notification-v2/> (latest: `client-notification-v2`).

## client-notification-v2

`/develop/sdks/client-notification-v2/`

- SDK for TypeScript
- Notification v2

## Notification v2
Manage resource/event notifications with the Notification Service API.

 @dynatrace-sdk/client-notification-v2 v1.1.2 Latest (V1)

`tsx
npm install @dynatrace-sdk/client-notification-v2
`

### eventNotificationsClient

`tsx
import { eventNotificationsClient } from '@dynatrace-sdk/client-notification-v2';
`

#### createEventNotification

eventNotificationsClient.createEventNotification(config): PromiseEventNotification>Required scope: notification:notifications:write

##### Parameters
 |
 | Name | Type
 | config.body*required | EventNotificationRequest

##### Returns
 |
 | Return type | Status code | Description
 | EventNotification | 201 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { eventNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await eventNotificationsClient.createEventNotification({ body: { resourceId: "...", notificationType: "...", triggerConfiguration: { type: "event", value: { query: "..." }, }, }, });
`

#### deleteEventNotification

eventNotificationsClient.deleteEventNotification(config): PromiseRequired scope: notification:notifications:write

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
import { eventNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await eventNotificationsClient.deleteEventNotification({ id: "...", });
`

#### getEventNotification

eventNotificationsClient.getEventNotification(config): PromiseEventNotification>Required scope: notification:notifications:read

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this self notification.

##### Returns
 |
 | Return type | Status code | Description
 | EventNotification | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { eventNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await eventNotificationsClient.getEventNotification({ id: "...", });
`

#### getEventNotifications

eventNotificationsClient.getEventNotifications(config): PromisePaginatedEventNotificationList>Required scope: notification:notifications:read

##### Parameters
 |
 | Name | Type | Description
 | config.appId | string | Application id associated with the notification. Optional, by default automatically inferred from the request header. Only relevant for manual testing purposes via swagger.
 | config.limit | number | Number of results to return per page.
 | config.notificationType | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | config.offset | number | The initial index from which to return the results.
 | config.ordering | string | Which field to use when ordering the results.
 | config.owner | string |
 | config.resourceId | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.
 | config.search | string | A search term.

##### Returns
 |
 | Return type | Status code | Description
 | PaginatedEventNotificationList | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { eventNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await eventNotificationsClient.getEventNotifications();
`

#### patchEventNotification

eventNotificationsClient.patchEventNotification(config): PromiseEventNotification>Required scope: notification:notifications:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | EventNotificationUpdate |
 | config.id*required | string | A UUID string identifying this self notification.

##### Returns
 |
 | Return type | Status code | Description
 | EventNotification | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { eventNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await eventNotificationsClient.patchEventNotification({ id: "...", body: { triggerConfiguration: { type: "event", value: { query: "..." }, }, }, });
`

#### updateEventNotification

eventNotificationsClient.updateEventNotification(config): PromiseEventNotification>Required scope: notification:notifications:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | EventNotificationUpdate |
 | config.id*required | string | A UUID string identifying this self notification.

##### Returns
 |
 | Return type | Status code | Description
 | EventNotification | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { eventNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await eventNotificationsClient.updateEventNotification({ id: "...", body: { triggerConfiguration: { type: "event", value: { query: "..." }, }, }, });
`

### resourceNotificationsClient

`tsx
import { resourceNotificationsClient } from '@dynatrace-sdk/client-notification-v2';
`

#### createResourceNotification

resourceNotificationsClient.createResourceNotification(config): PromiseResourceNotification>Required scope: notification:notifications:write

##### Parameters
 |
 | Name | Type
 | config.body*required | ResourceNotificationRequest

##### Returns
 |
 | Return type | Status code | Description
 | ResourceNotification | 201 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { resourceNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await resourceNotificationsClient.createResourceNotification( { body: { notificationType: "...", resourceId: "..." }, }, );
`

#### deleteResourceNotification

resourceNotificationsClient.deleteResourceNotification(config): PromiseRequired scope: notification:notifications:write

##### Parameters
 |
 | Name | Type | Description
 | config.appId | string | Application id associated with the notification. Optional, by default automatically inferred from the request header. Only relevant for manual testing purposes via swagger.
 | config.id*required | string | A UUID string identifying this resource notification.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { resourceNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await resourceNotificationsClient.deleteResourceNotification( { id: "..." }, );
`

#### deleteResourceNotificationByTypeAndResource

resourceNotificationsClient.deleteResourceNotificationByTypeAndResource(config): PromiseRequired scope: notification:notifications:write

##### Parameters
 |
 | Name | Type | Description
 | config.appId | string | Application id associated with the notification. Optional, by default automatically inferred from the request header. Only relevant for manual testing purposes via swagger.
 | config.notificationType*required | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | config.resourceId*required | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { resourceNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await resourceNotificationsClient.deleteResourceNotificationByTypeAndResource( { notificationType: "...", resourceId: "..." }, );
`

#### getResourceNotification

resourceNotificationsClient.getResourceNotification(config): PromiseResourceNotification>Required scope: notification:notifications:read

##### Parameters
 |
 | Name | Type | Description
 | config.appId | string | Application id associated with the notification. Optional, by default automatically inferred from the request header. Only relevant for manual testing purposes via swagger.
 | config.id*required | string | A UUID string identifying this resource notification.

##### Returns
 |
 | Return type | Status code | Description
 | ResourceNotification | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { resourceNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await resourceNotificationsClient.getResourceNotification( { id: "..." }, );
`

#### getResourceNotifications

resourceNotificationsClient.getResourceNotifications(config): PromisePaginatedResourceNotificationList>Required scope: notification:notifications:read

##### Parameters
 |
 | Name | Type | Description
 | config.appId | string | Application id associated with the notification. Optional, by default automatically inferred from the request header. Only relevant for manual testing purposes via swagger.
 | config.limit | number | Number of results to return per page.
 | config.notificationType | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | config.offset | number | The initial index from which to return the results.
 | config.ordering | string | Which field to use when ordering the results.
 | config.resourceId | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.
 | config.search | string | A search term.

##### Returns
 |
 | Return type | Status code | Description
 | PaginatedResourceNotificationList | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { resourceNotificationsClient } from "@dynatrace-sdk/client-notification-v2";const data = await resourceNotificationsClient.getResourceNotifications();
`

### Types

#### DavisEventConfig

 |
 | Name | Type | Description
 | customFilter | null | string | Additional DQL matcher expression to further filter events to match.
 | entityTags | null | EntityTags |
 | entityTagsMatch | "all" | "any" |
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
 | Name | Type | Description
 | code*required | number |
 | details | ErrorDetails | Error response details according to API Guidelines
 | message*required | string |

#### ErrorDetails

Error response details according to API Guidelines

 |
 | Name | Type
 | errorCode | null | string
 | errorRef | null | string

#### ErrorEnvelope

 |
 | Name | Type
 | error*required | Error

#### EventNotification

 |
 | Name | Type | Description
 | appId | string | App id for registered notification. Optional, by default automatically inferred from the request. Only relevant for manual testing purposes via swagger.
 | id*required | string |
 | input | EventNotificationInput | Input object consisting of subject and content. Supports automation expressions https://dt-url.net/workflows-expression-reference and markdown syntax. A template provided with an app ({notification_type}.notification-template.json) will take precedence over the input provided here.
 | modificationInfo*required | ModificationInfo |
 | notificationType*required | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | owner*required | string |
 | resourceId*required | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.
 | title | string |
 | triggerConfiguration*required | EventTriggerConfig |

#### EventNotificationInput

 |
 | Name | Type
 | content | null | string
 | subject | null | string

#### EventNotificationRequest

 |
 | Name | Type | Description
 | appId | string | App id for registered notification. Optional, by default automatically inferred from the request. Only relevant for manual testing purposes via swagger.
 | id | string |
 | input | EventNotificationInput | Input object consisting of subject and content. Supports automation expressions https://dt-url.net/workflows-expression-reference and markdown syntax. A template provided with an app ({notification_type}.notification-template.json) will take precedence over the input provided here.
 | notificationType*required | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | resourceId*required | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.
 | title | string |
 | triggerConfiguration*required | EventTriggerConfig |

#### EventNotificationUpdate

 |
 | Name | Type | Description
 | appId | string | App id for registered notification. Optional, by default automatically inferred from the request. Only relevant for manual testing purposes via swagger.
 | input | EventNotificationInput | Input object consisting of subject and content. Supports automation expressions https://dt-url.net/workflows-expression-reference and markdown syntax. A template provided with an app ({notification_type}.notification-template.json) will take precedence over the input provided here.
 | notificationType | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | resourceId | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.
 | title | string |
 | triggerConfiguration | EventTriggerConfig |

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

#### PaginatedEventNotificationList

 |
 | Name | Type
 | count*required | number
 | results*required | ArrayEventNotification>

#### PaginatedResourceNotificationList

 |
 | Name | Type
 | count*required | number
 | results*required | ArrayResourceNotification>

#### ResourceNotification

 |
 | Name | Type | Description
 | appId | null | string | App id for registered notification. Optional, by default automatically inferred from the request. Only relevant for manual testing purposes via swagger.
 | id*required | string |
 | modificationInfo*required | ModificationInfo |
 | notificationType*required | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | owningUser*required | string |
 | resourceId*required | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.

#### ResourceNotificationRequest

 |
 | Name | Type | Description
 | appId | null | string | App id for registered notification. Optional, by default automatically inferred from the request. Only relevant for manual testing purposes via swagger.
 | id | string |
 | notificationType*required | string | String that defines the type of a notification in context of an app. Allows to differentiate between multiple types of notifications in context of one app.
 | resourceId*required | string | Unique identifier of resource to notify on. Used to determine if there is a notification registered for a resource in context of the app and notification type for a user.

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
