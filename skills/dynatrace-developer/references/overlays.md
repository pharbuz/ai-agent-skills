# Overlays

Strato design-system components in the **Overlays** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## Modal

`/design/components/overlays/Modal/`

The `Modal` component lets you show important, additional content in an overlay.

The overlay is always centered on the page and covers the on-screen content
until the user closes it.

The `Modal` must have a trigger that controls the open status of the modal. The
`useOverlayWithTrigger` hook provides the corresponding props.

It's also essential to add at least one focusable element inside the `Modal` so
that it's keyboard accessible. If no focusable element is available, the focus
will be given to the document when opening the modal.

### Import

`tsx
import { Modal } from '@dynatrace/strato-components/overlays';
`

### Use Cases

#### Control size of modal

Use the `size` prop of the modal to change its size. The default value is
`medium`.

#### Control dismissible state of modal

Allows you to control the dismissible state of your modal.

#### Nest modals

You can place different content or additional modals inside a modal. If a modal
within the modal (a nested modal) is triggered, the focus is switched to the
nested modal and the first modal loses focus and is treated like a background
element.

#### Handle the focus if the trigger is removed when opening

If you're using a trigger that is removed from the DOM when the modal is opened,
you have to take care of some parts of the focus handling to ensure that proper
keyboard navigation is still possible. When the trigger is removed, you may have
to prevent the trigger from moving the focus away from the modal and move it
back to an element on your page after dismissing the modal. Check out the
following example to see how this could work when using a `Menu.Item` as trigger
for the modal.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use Cases
- Control size of modal
- Control dismissible state of modal
- Nest modals
- Handle the focus if the trigger is removed when opening

### Props

The `Modal` component lets you show important, additional content in an overlay.

#### ModalProps
extends`, , ` |
 | Name | Type | Default | Description
 | `title` | | | | Title of the modal, which is shown in the header section.
 | `footer?` | | | Footer section of the modal, where customized content can be added.

#### BaseModalProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `show?` | | `false` | Controls when the modal is shown.
 | `size?` | | `'medium'` | Sets the size of the modal.
 | `onDismiss?` | () => | | Handler function that is called when the modal is closed.
 | `dismissible?` | | `true` | Determines if you can click the backdrop to dismiss the modal.
If true, pressing "ESC" also dismisses the modal.Still have questions?Find answers in the Dynatrace Community

---

## Overlay

`/design/components/overlays/Overlay/`

The `Overlay` component allows you to show additional content when the user
clicks on a particular element in the UI. The `Overlay` is placed at the border
of its trigger element. To define a UI element as a trigger, use the
`useOverlayWithTrigger` hook. The Overlay only exists in a controlled manner, so
the `isOpen` prop must be updated by the developer.

OverviewProperties

### Import

`tsx
import { Overlay } from '@dynatrace/strato-components/overlays';
`

### UseCases

#### Control appearance

Use `placement` in the overlayProps to set the overlay's position relative to
its trigger element. To influence the space between the trigger element and the
overlay, change the `offset`.

Set the widthStrategy to control the width of the overlay. Values can be min and
max in pixels, 'content' or 'trigger'.

#### Trap focus

If you want to trap the focus inside the overlay, you can use the `trapFocus`
option of the `useOverlayWithTrigger` hook. Note that the focus will be trapped,
regardless of any focusable children being present in the overlay. If you don't
have focusable children in the overlay, make sure not to trap the focus so
keyboard users can still dismiss the overlay and continue navigating the page.

#### Dynamic content

If you have dynamic content in the overlay that is changing from including
focusable children at first to no more focusable children being present in the
end, you need to make sure to also handle trapping the focus accordingly. As
long as you include focusable children, you can have the focus trapped in the
overlay. As soon as there are no more focusable children in the overlay, you
must not trap the focus anymore to avoid keyboard traps.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- UseCases
- Control appearance
- Trap focus
- Dynamic content

### Props

The `Overlay` component allows you to show additional content when the user
clicks on a particular element in the UI. The `Overlay` is placed at the border
of its trigger element. To define a UI element as a trigger, use the
`useOverlayWithTrigger` hook. The Overlay only exists in a controlled manner, so
the `isOpen` prop must be updated by the developer.

OverviewProperties

#### OverlayComponentProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `isOpen` | [][] | | Whether the overlay is open.
 | `overlayProps?` | [] | | Properties for connecting the overlay to the overlay trigger.
Includes styles and accessibility attributes.
 | `overlayContainerProps?` | [] | | Properties to pass to the overlay container.Still have questions?Find answers in the Dynatrace Community

---

## Sheet

`/design/components/overlays/Sheet/`

The `Sheet` component allows you to show additional content in an overlay of
your application. It is essential to add at least one focusable element inside
the `Sheet` to be keyboard accessible. If none is available the focus will be
lost and given to the `window.document` when opening the sheet.

The developer is responsible for the sheet's visibility via the `show` prop.
This prop must be updated to false in the `onDismiss` callback to ensure
keyboard accessibility.

OverviewProperties

### Import

`tsx
import { Sheet } from '@dynatrace/strato-components/overlays';
`

### Use cases

#### Custom dismiss functionality

The `onDismiss` prop allows you to define a custom dismiss functionality. That
is triggered when closing the sheet with escape.

#### Accessibility

If there is no title prop, you need to add either an `aria-label` or
`aria-labelledby` prop to ensure accessibility.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Custom dismiss functionality
- Accessibility

### Props

The `Sheet` component allows you to show additional content in an overlay of
your application. It is essential to add at least one focusable element inside
the `Sheet` to be keyboard accessible. If none is available the focus will be
lost and given to the `window.document` when opening the sheet.

The developer is responsible for the sheet's visibility via the `show` prop.
This prop must be updated to false in the `onDismiss` callback to ensure
keyboard accessibility.

OverviewProperties

#### SheetProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `title?` | | | The title which is displayed at the top of the sheet.
 | `show?` | | `false` | Toggles the visibility of the sheet component.
 | `topoffset?` | | `28` | The offset to the top of the App which should not be covered.
 | `actions?` | | | Actions will be rendered to the top right, next to the title.
They usually contain buttons like 'Apply' or 'Cancel'.
 | `onDismiss?` | () => | | Handler that is only called if the sheet is closed with the Escape key.Still have questions?Find answers in the Dynatrace Community

---

## Tooltip

`/design/components/overlays/Tooltip/`

Use the `Tooltip` component to display extra information when users hover on a
trigger element.

### Import

`tsx
import { Tooltip } from '@dynatrace/strato-components/overlays';
`

### Demo

The `Tooltip` component shows brief, helpful information when users hover on a
trigger. The trigger element must be interactive. See Usage for
best practices.

### Placement

Use the `placement` prop to set the position of the tooltip relative to the
trigger element. The default placement is at the top.

### Accessibility

The content of the tooltip isn't accessible to screen readers by default. If the
trigger doesn't include a label, it's only an icon for example, and there isn't
an `aria-label`, you must link the tooltip text to the trigger.

Pass an `id` property to the tooltip itself and add an `aria-describedby` or an
`aria-labelledby` property to the trigger and reference the `id`.

In choosing which property to use, consider that a label describes the thing
itself (Example: Edit button), whereas a description describes an action or
purpose (Example: Allows you to change the title and text of the document).

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Placement
- Accessibility

### Props

Use the `Tooltip` component to display extra information when users hover on a
trigger element.

#### TooltipProps
extends |
 | Name | Type | Default | Description
 | `text` | | | Text displayed in the tooltip component.

#### TooltipBaseProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `children` | | | Single child of the tooltip considered to trigger the tooltip element.
 | `disabled?` | | `false` | Defines if the tooltip is disabled or not.
 | `placement?` | | | | | | | | | | | | | `'top'` | Placement of the tooltip relative to its trigger element.
 | `defaultOpen?` | | `false` | Defines if the tooltip should be open initially when used uncontrolled.
 | `open?` | | | Defines if the tooltip is open / closed in a controlled component. In
this case, you need to react to `onOpenChange` yourself in order
to open and close the tooltip.
 | `delay?` | | | `'default'` | Defines the type of delay which is used for the tooltip.
 | `onOpenChange?` | (isOpen: ) => | | Callback fired when the tooltip opens.
 | `fallbackPlacements?` | | | Array of placements to be used as fallback if the tooltip doesn't fit at the specified placement.Still have questions?Find answers in the Dynatrace Community

---

