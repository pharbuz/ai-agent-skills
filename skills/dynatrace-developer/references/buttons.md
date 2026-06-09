# Buttons

Strato design-system components in the **Buttons** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## Button

`/design/components/buttons/Button/`

Buttons let users trigger actions or events with a single click, or by pressing
`Enter` or `Space` while the button has focus.

### Import

`tsx
import { Button } from '@dynatrace/strato-components/buttons';
`

### Demo

### Add label and icons

Buttons can consist of a label, a prefix icon, and a suffix icon. Buttons should
always use a label unless the icon displayed is universally understood and
accessible. If a button uses only an icon, it should be placed in the prefix or
suffix slot and have an `aria-label` applied.

It's advised to only use the `aria-label` if the button has no readable content,
like when it only has an icon. In that case, the `aria-label` needs to be used
to make the item accessible.

### Change variant

Use the `variant` prop to create the different contextual button variants. When
no `variant` is specified, it's set to `default`.

### Change color

By default, the button has the color `neutral`. You should always consider the
meaning behind the colors when changing this.

### Disable

The `disabled` prop disables a button, applying the native
`disabled`
attribute to the `button` element.

To make the button more accessible, use
`aria-disabled`
instead. This doesn't apply the disabled attribute to the native button. The
`aria-disabled` attribute only semantically disables the button, but it's still
focusable, clickable, and registered events will still be triggered. This
enables visually impaired users to focus the button and have it announced by a
screen reader. You need to handle events yourself to prevent triggering
unintended actions when the button is `aria-disabled`.

To provide more information about why the button is disabled, add an
`aria-label` or `aria-describedby` attribute.

Try to use disabled buttons as rarely as possible, especially in forms. Disabled
buttons provide little feedback, making it hard to know why they aren't usable.
Instead, let the users submit the form, but prevent the submission and provide
appropriate error messages.

To provide a visual indicator of why the button is disabled, we recommend adding
additional content next to the button, as in the example above, but you can also
use a tooltip.

### Change width

The button is as wide as its content by default. When the prop is set to `full`,
it takes the width of its parent container. The `width` prop also supports any
CSS width value.

### Change size

The size of the button can be changed with the `size` prop. It supports two
different sizes, `default` and `condensed`.

### Change text alignment

By default, the text content is centered inside a button. The alignment can be
changed by setting the `textAlign` prop to `start`. This only affects the button
if its width is set to any value bigger than the button content.

### Set loading state

You can set the `Button` state to loading by adding the prop `loading`. By
default, it's set to `false`, so the button contents are shown. If `true`, it
shows an indeterminate `ProgressCircle`, styled depending on the `color` and
`variant` props. You also can't interact with the button, which acts as disabled
while `loading` is `true` and doesn't fire any trigger events.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Add label and icons
- Change variant
- Change color
- Disable
- Change width
- Change size
- Change text alignment
- Set loading state

### Props

Buttons let users trigger actions or events with a single click, or by pressing
`Enter` or `Space` while the button has focus.

#### ButtonProps

##### Signature:
`export declare type ButtonProps = ;`

#### ButtonOwnProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `disabled?` | | `false` | If a button is disabled e.g. it cannot be interacted with.
 | `variant?` | | | | `'default'` | Different variants have different styles.
 | `type?` | | | | `'button'` | The HTML button type.
 | `onClick?` | | | Called when the button is interacted with.
 | `width?` | | | .. | `'content'` | The width of the button.
 | `color?` | | | | | | `'neutral'` | The color of the button. This should be chosen based on the context
the button is used in.
 | `textAlign?` | | | `'center'` | Controls the text alignment inside the button. Only affects the button
if the width is not set to 'content'.
 | `size?` | | | `'default'` | The size of the button.
 | `loading?` | | `false` | The current loading state of the button. If true, a loading icon is shown and the button is disabled.

### Button.Label

You can use the `Button.Label` component to render any custom label. If you pass
a text-based label, overflowing text would get truncated. If you don't use the
`Label` component and just add your label as the `Button` child, it gets added
internally.

#### ButtonLabelProps
extends`, , ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the Button Label slot.

### Button.Prefix

You can use the `Button.Prefix` component to render content (e.g. an icon) right
before the button label, as shown above.

#### ButtonPrefixProps
extends`, , ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the Button Prefix slot.

### Button.Suffix

You can use the `Button.Suffix` component to render content (e.g. an icon) right
after the button label, as shown above.

#### ButtonSuffixProps
extends`, , ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the Button Suffix slot.Still have questions?Find answers in the Dynatrace Community
- Button.Label
- Button.Prefix
- Button.Suffix

---

## IntentButton

`/design/components/buttons/IntentButton/`

The `IntentButton` is a dedicated component for sending
intents.
The `IntentButton` only works within the AppShell context.

OverviewProperties

### Import

`tsx
import { IntentButton } from '@dynatrace/strato-components/buttons';
`

### Use cases

The `IntentButton` component consists of a button label with a prefix icon, and
a dropdown menu.

### Display intents in a menu

Use the `IntentButton.Item` compound component to automatically display
additional intents in a menu. The main intent is the primary action on the root
component, the , itself.

### Add payload to "Open with..."

The `IntentButton` include an "Open with..." menu item as a default. "Open
with..." opens an overlay listing suitable apps for users to choose from. To
customize the `payload` prop (information that you want to share with the apps)
use the `IntentButton.OpenWith` compound component. The label and icon for the
"Open with..." menu item cannot be changed.

### Intent with response

The `IntentButton` supports intents that return data from intent actions. To
receive a response, you must provide both the `onResponse` and the
`responseProperties` prop. The `responseProperties` prop defines which
properties the source app expects in the response; `onResponse` is the callback
that handles the returned values.

### Three dot menu

This menu is rendered by default and includes a fallback "Open with..." entry
for cases where specific intents or apps are unavailable. You can hide the menu
using the `showMenu` prop, but keep in mind you can't be sure if there isn't a
different action your user wants to take.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Display intents in a menu
- Add payload to "Open with..."
- Intent with response
- Three dot menu

### Props

The `IntentButton` is a dedicated component for sending
intents.
The `IntentButton` only works within the AppShell context.

OverviewProperties

#### IntentButtonProps

##### Signature:
`export declare type IntentButtonProps = & & & {
 /**
 * Enable the three dot menu for additional intents.
 * This menu includes a fallback "Open with..." entry for cases where specific intents are unavailable.
 * @defaultValue true
 */
 showMenu?: ;
};`

#### ButtonOwnProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `disabled?` | | `false` | If a button is disabled e.g. it cannot be interacted with.
 | `variant?` | | | | `'default'` | Different variants have different styles.
 | `type?` | | | | `'button'` | The HTML button type.
 | `onClick?` | | | Called when the button is interacted with.
 | `width?` | | | .. | `'content'` | The width of the button.
 | `color?` | | | | | | `'neutral'` | The color of the button. This should be chosen based on the context
the button is used in.
 | `textAlign?` | | | `'center'` | Controls the text alignment inside the button. Only affects the button
if the width is not set to 'content'.
 | `size?` | | | `'default'` | The size of the button.
 | `loading?` | | `false` | The current loading state of the button. If true, a loading icon is shown and the button is disabled.

#### IntentWithoutResponseProps
extends |
 | Name | Type | Default | Description
 | `options` | <> | |

#### IntentWithResponseProps
extends |
 | Name | Type | Default | Description
 | `options` | <> | |
 | `onResponse` | (response: | ) => | |

### IntentButton components

#### IntentButton.Item

Has the same properties as the `IntentButton` component and can also use the
`IntentButton.Icon` component.

#### IntentButtonProps

##### Signature:
`export declare type IntentButtonProps = & & & {
 /**
 * Enable the three dot menu for additional intents.
 * This menu includes a fallback "Open with..." entry for cases where specific intents are unavailable.
 * @defaultValue true
 */
 showMenu?: ;
};`

#### IntentButton.Icon

Use it to render an icon inside the `IntentButton` component or the
`IntentButton.Item` component.

Prop Table did not receive data

#### IntentButton.OpenWith

The `OpenWith` component renders an `IntentMenu` with a default label that can't
be changed. Pass the `payload` prop for the intent.

#### OpenWithProps

##### Signature:
`export declare type OpenWithProps = & ;`Still have questions?Find answers in the Dynatrace Community
- IntentButton components
- IntentButton.Item
- IntentButton.Icon
- IntentButton.OpenWith

---

## NotifyButton

`/design/components/buttons/NotifyButton/`

The `NotifyButton` allows users to turn notifications about updates of resources
on or off. Common use cases include notifications about updates of saved
filters, workflows, or entities. Users will be notified via e-mail.

### Import

`tsx
import { NotifyButton } from '@dynatrace/strato-components/buttons';
`

### Use cases

#### Use resource notifications

#### Change the variant

Use the `variant` prop to create the different contextual button variants. When
no `variant` is specified, it's set to `default`.

#### Change the size

Use the `size` prop to change the size of the button. When no `size` is
specified, it's set to `default`.

#### Make the NotifyButton read-only

The `readOnly` prop makes the button read-only, which disables toggling the
overlay. The button is still focusable.

#### Show label

Use the `showLabel` prop to show the "Notifications" translated text next to the
`NotifyButton` icon.

#### Customize the overlay content

Use the `NotifyButton.Content` component to customize the content of the
overlay. Add the `aria-describedby` prop and `id` prop to connect the trigger to
the custom content. In most cases, the heading of the overlay provides the best
description for the trigger, as shown in the example.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Use resource notifications
- Change the variant
- Change the size
- Make the NotifyButton read-only
- Show label
- Customize the overlay content

### Props

The `NotifyButton` allows users to turn notifications about updates of resources
on or off. Common use cases include notifications about updates of saved
filters, workflows, or entities. Users will be notified via e-mail.

#### NotifyButtonProps

##### Signature:
`export declare type NotifyButtonProps = & & & & & & & & & {
 /**
 * Configures the size of the trigger.
 * @defaultValue 'default
 */
 size?: | ;
 /**
 * Configures the variant of the trigger.
 * @defaultValue 'default
 */
 variant?: | ;
 /**
 * Whether the NotifyButton is read-only.
 * @defaultValue false
 */
 readOnly?: ;
 /**
 * Whether the NotifyButton is disabled.
 * @defaultValue false
 */
 disabled?: ;
 /**
 * Whether the label text is shown on the trigger.
 * @defaultValue false
 */
 showLabel?: ;
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

### NotifyButtonContent

The `NotifyButtonContent` component renders custom content inside the
`NotifyButton` overlay.

#### NotifyButtonContentProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `children?` | (({ , , , , , }: {
 : ;
 : ;
 : ;
 : ;
 : ;
 }) => ) | | | Still have questions?Find answers in the Dynatrace Community
- NotifyButtonContent

---

## RunQueryButton

`/design/components/buttons/RunQueryButton/`

This button component is used for running queries. It supports four query
states: idle, loading, success, and error.

OverviewProperties

### Import

`tsx
import { RunQueryButton } from '@dynatrace/strato-components/buttons';
`

### Use cases

#### Change button states

Use the `queryState` prop to transition between the button's states.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change button states

### Props

This button component is used for running queries. It supports four query
states: idle, loading, success, and error.

OverviewProperties

#### RunQueryButtonProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `disabled?` | | `false` | When the run query button is disabled it cannot be interacted with.
 | `queryState?` | | `idle` | The current button state.
 | `onClick?` | | | Callback triggered when the RunQueryButton is interacted with.
 | `cancelable?` | | `true` | Whether the run query button is cancelable, i.e., if the loading
state can be interrupted.Still have questions?Find answers in the Dynatrace Community

---

