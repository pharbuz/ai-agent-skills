# Notifications

Strato design-system components in the **Notifications** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## NotificationSettings

`/design/components/notifications/NotificationSettings/`

NotificationSettings component

OverviewProperties

### Import

`tsx
import { NotificationSettings } from '@dynatrace/strato-components/notifications';
`

### Use cases

For reference on what notification types and resources can be configured, please
refer to the notification sdk.

#### Use resource notifications

```tsx
import { NotificationSettings } from '@dynatrace/strato-components/notifications';

const BasicResource = () => {
  return (
    <NotificationSettings
      type="resource"
      config={{
        resourceId: '996d8d4b-a7c8-4471-bbc0-88ffdd31b030',
        notificationType: 'event-query',
      }}
    />
  );
};
```

```tsx
import { NotificationSettings } from '@dynatrace/strato-components/notifications';

const BasicResource = () => {
  return (
    <NotificationSettings
      type="resource"
      config={{
        resourceId: '996d8d4b-a7c8-4471-bbc0-88ffdd31b030',
        notificationType: 'event-query',
      }}
    />
  );
};
```


#### Customize the message content

Use the children slot of the `NotificationSettings` component to customize the
content above the button. The

#### Using the NotificationSettings in a Menu

To use the NotificationSettings within a `Menu` item, we provide a custom hook
that will automatically connect a configured modal with a menu item.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Use resource notifications
- Customize the message content
- Using the NotificationSettings in a Menu

### Props

NotificationSettings component

OverviewProperties

#### NotificationSettingsProps

##### Signature:
`export declare type NotificationSettingsProps = & & & & & & & {
 /**
 * Either a or a render function that gets passed certain values
 * from the currently configured notification */
 children?: (({ , , , , , }: {
 : ;
 : ;
 : ;
 : ;
 : ;
 }) => ) | ;
};`

#### NotificationSettingsConfig

##### Signature:
`export declare type NotificationSettingsConfig = | ;`

#### NotificationSettingsEventNotification
 |
 | Name | Type | Default | Description
 | `type` | | | Defines the type of the notifcation that should be subscribed to.
 | `config` | | | Configuration for a event notification. Uses the `@dynatrace-sdk/client-notification-v2`.

#### NotificationSettingsResourceNotification
 |
 | Name | Type | Default | Description
 | `type` | | | Defines the type of the notifcation that should be subscribed to.
 | `config` | | | Configuration for a resource notification. Uses the `@dynatrace-sdk/client-notification-v2`.

#### UseNotificationSettingsMenuItemProps

##### Signature:
`export declare type UseNotificationSettingsMenuItemProps = & {
 /** Either a or a render function that gets passed certain values from the currenlty configured notification */
 content?: (({ , , , , , }: {
 : ;
 : ;
 : ;
 : ;
 : ;
 }) => ) | ;
};`Still have questions?Find answers in the Dynatrace Community

---

## Toast

`/design/components/notifications/Toast/`

Use Toast to show users live, time-sensitive messages about system status
changes. Toast variants for four different kinds of messages are provided.

### Import

`tsx
import { ToastContainer, ToastOptions, dismissAllToasts, dismissToast, showToast,} from '@dynatrace/strato-components/notifications';
`

### Use cases

Add `ToastContainer` to your App.tsx to make it available everywhere. All toasts
will be rendered into this container. Only a single ToastContainer is rendered
at a time, even if multiple containers are provided.

#### Configure the Toast type

The `Toast` type can be configured by setting the `type` prop in the
`ToastOptions`. There are four types, each with a different purpose, appearance,
and lifespan:

- `info`: Closes automatically after 8 seconds; ARIA role `status` (default
type)

- `success`: Closes automatically after 8 seconds; ARIA role `status`

- `warning`: The user must close it; ARIA role `status`

- `critical`: The user must close it; ARIA role `alert`

The lifespan and ARIA role can be configured regardless of `type`.

#### Configure the lifespan

Use the `lifespan` option to define a time limit in milliseconds or set it to
`infinite` to display the toast until closed by the user. From an accessibility
perspective, automatic time limits can be problematic. Therefore don't limit the
lifespan of toasts that contain critical information.

#### Configure the role

Use the `role` option to configure the ARIA role set on the toast's body. The
available roles are `status`, `log` and `alert`. Please ensure that the correct
role attribute is assigned, as it is crucial for proper accessibility handling.

#### Configure the position

Use the `position` option to configure the placement of the `Toast` component.
By default, toasts are positioned at `bottom-left`, but this can be changed to
`bottom-center` or `bottom-right`.

#### Custom ID for the Toast

You can configure a unique `id` for the `Toast`. Using the `id` option, you can
control the behavior of individual toast notifications. Also, by assigning a
unique `id` to a toast, you can prevent duplicate messages from being shown with
the same toast `id`.

#### Multiple toasts

You can display multiple toasts simultaneously. A maximum of five toasts can be
displayed on the page at once. Additional toasts will be queued and appear when
one of the first five toasts is closed.

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import {
  ToastContainer,
  showToast,
  type ToastOptions,
} from '@dynatrace/strato-components/notifications';

const MultipleToasts = () => {
  const handleMultipleToast = () => {
    const options: Record<number, ToastOptions> = {
      0: { type: 'info', title: 'Info' },
      1: { type: 'warning', title: 'Warning!' },
      2: { type: 'critical', title: 'Error!' },
    };

    showToast({
      ...options[0],
      lifespan: 4000,
      message: 'This is a place to add an optional detail text to the Toast.',
    });
    showToast({
      ...options[1],
      lifespan: 4000,
      message: 'This is a place to add an optional detail text to the Toast.',
    });
    showToast({
      ...options[2],
      lifespan: 4000,
      message: 'This is a place to add an optional detail text to the Toast.',
    });
  };

  return (
    <>
      <ToastContainer />
      <Button onClick={handleMultipleToast} variant="emphasized">
        Show multiple toasts
      </Button>
    </>
  );
};
```

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import {
  ToastContainer,
  showToast,
  type ToastOptions,
} from '@dynatrace/strato-components/notifications';

const MultipleToasts = () => {
  const handleMultipleToast = () => {
    const options: Record<number, ToastOptions> = {
      0: { type: 'info', title: 'Info' },
      1: { type: 'warning', title: 'Warning!' },
      2: { type: 'critical', title: 'Error!' },
    };

    showToast({
      ...options[0],
      lifespan: 4000,
      message: 'This is a place to add an optional detail text to the Toast.',
    });
    showToast({
      ...options[1],
      lifespan: 4000,
      message: 'This is a place to add an optional detail text to the Toast.',
    });
    showToast({
      ...options[2],
      lifespan: 4000,
      message: 'This is a place to add an optional detail text to the Toast.',
    });
  };

  return (
    <>
      <ToastContainer />
      <Button onClick={handleMultipleToast} variant="emphasized">
        Show multiple toasts
      </Button>
    </>
  );
};
```


#### Add actions inside the toast

The `actions` option allows you to pass custom actions to the `Toast`. The
actions will be appended at the bottom. Only use a `Button` or `Link` as an
action element.

#### Dismiss toasts programmatically

Use the `dismissToast` and `dismissAllToasts` functions to close toasts
programmatically. To close a single toast with the `dismissToast` function,
simply pass the ID returned by the `showToast` function as an argument.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Configure the Toast type
- Configure the lifespan
- Configure the role
- Configure the position
- Custom ID for the Toast
- Multiple toasts
- Add actions inside the toast
- Dismiss toasts programmatically

### Props

Use Toast to show users live, time-sensitive messages about system status
changes. Toast variants for four different kinds of messages are provided.

#### ToastOptions
extends`, , , , ` |
 | Name | Type | Default | Description
 | `id?` | | | | A unique id for the toast. Using this toast id consumer can control
the behavior of individual toast notifications. Toast messages with same
id will only be shown once.
 | `title` | | | Title displayed in the toast notification.
 | `type?` | | | | | `'info'` | Type of the notification. Also indicates the color and icon.
 | `message?` | | . | | Message displayed in the toast notification.
 | `lifespan?` | | | `info and success: 8000, critical and warning: 'infinite'` | The Toast notification will automatically close after a certain period of
time given in milliseconds. If 'infinite' is provided, the user must close the toast.
 | `actions?` | . | | Optional actions passed to the toast element, appended on the bottom left.
Should only be used to either add a Button or a Link.
 | `role?` | | | | `info, success and warning: 'status', critical: 'alert'` | Live region roles
 | `position?` | | | | `'bottom-left'` | Position of toastStill have questions?Find answers in the Dynatrace Community

---

