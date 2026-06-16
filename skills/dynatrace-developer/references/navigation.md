# Navigation

Strato design-system components in the **Navigation** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## AppLink

`/design/components/navigation/AppLink/`

`AppLink` renders a link that points to the specified application.

OverviewProperties

### Import

`tsx
import { AppLink } from '@dynatrace/strato-components/navigation';
`

### Use cases

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases

### Props

`AppLink` renders a link that points to the specified application.

OverviewProperties

#### AppLinkProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `appId` | | | The ID of the app to which the link points.
 | `pageToken?` | | | ID of the app page to be launched.
 | `onClick?` | (event: ) => | | Function to handle click events on the AppLink.Still have questions?Find answers in the Dynatrace Community

---

## Breadcrumbs

`/design/components/navigation/Breadcrumbs/`

The `Breadcrumbs` component can be used to indicate the location and hierarchy
of the current page. It also allows users to easily navigate back to a higher
level in the hierarchy.

### Import

`tsx
import { Breadcrumbs } from '@dynatrace/strato-components/navigation';
`

### Use cases

#### Disable an item

The `disabled` prop disables a `Breadcrumbs.Item`, making it unclickable.

```tsx
import { Breadcrumbs } from '@dynatrace/strato-components/navigation';

const DisabledItem = () => {
  return (
    <Breadcrumbs>
      <Breadcrumbs.Item href="#">Home</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#">Level 1</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#">Level 2</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#">Level 3</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#">Level 4</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#" disabled>
        Level 5
      </Breadcrumbs.Item>
    </Breadcrumbs>
  );
};
```

```tsx
import { Breadcrumbs } from '@dynatrace/strato-components/navigation';

const DisabledItem = () => {
  return (
    <Breadcrumbs>
      <Breadcrumbs.Item href="#">Home</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#">Level 1</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#">Level 2</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#">Level 3</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#">Level 4</Breadcrumbs.Item>
      <Breadcrumbs.Item href="#" disabled>
        Level 5
      </Breadcrumbs.Item>
    </Breadcrumbs>
  );
};
```


#### Use the Breadcrumbs with React Router

The `Breadcrumbs.Item` is a polymorphic component and can also be used as a
React Router link.

#### Use the Breadcrumbs inside a Flex component

When using the Breadcrumbs component inside a Flex component, make sure to set
`flexGrow` and `minWidth` as shown in the example. Otherwise, the responsive
collapsing and resize behavior won't work as the available space can't be
calculated correctly.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Disable an item
- Use the Breadcrumbs with React Router
- Use the Breadcrumbs inside a Flex component

### Props

The `Breadcrumbs` component can be used to indicate the location and hierarchy
of the current page. It also allows users to easily navigate back to a higher
level in the hierarchy.

#### BreadcrumbsProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `children?` | | | Elements to be displayed as Breadcrumbs.

### Breadcrumbs.Item

You can use the `Breadcrumbs.Item` component to render an item inside the
`Breadcrumbs` menu, as shown above.

#### BreadcrumbsItemProps

##### Signature:
`export declare type BreadcrumbsItemProps = ;`Still have questions?Find answers in the Dynatrace Community
- Breadcrumbs.Item

---

## Menu

`/design/components/navigation/Menu/`

The `Menu` component displays the list of action items that are revealed when
the user clicks on the trigger element.

### Import

`tsx
import { Menu } from '@dynatrace/strato-components/navigation';
`

### Demo

```tsx
import { useNavigate } from 'react-router';

import { HelpMenu } from '@dynatrace/strato-components/layouts';

const Basic = () => {
  const navigate = useNavigate();

  return (
    <HelpMenu
      entries={{
        whatsNew: 'default',
        getStarted: {
          onSelect: () => undefined,
        },
        documentation: [
          {
            label: 'Dynatrace Hub',
            href: 'link/to/hub',
            onSelect: () => {
              // side effect code can be executed to track behavioral events
            },
          },
          {
            label: 'Onboarding wizard',
            onSelect: () => {
              navigate('/onboarding');
            },
          },
        ],
        keyboardShortcuts: {
          href: 'https://developer.dynatrace.com/',
        },
        playground: 'default',
        feedback: { onSelect: () => undefined },
        about: 'default',
      }}
    />
  );
};
```

```tsx
import { useNavigate } from 'react-router';

import { HelpMenu } from '@dynatrace/strato-components/layouts';

const Basic = () => {
  const navigate = useNavigate();

  return (
    <HelpMenu
      entries={{
        whatsNew: 'default',
        getStarted: {
          onSelect: () => undefined,
        },
        documentation: [
          {
            label: 'Dynatrace Hub',
            href: 'link/to/hub',
            onSelect: () => {
              // side effect code can be executed to track behavioral events
            },
          },
          {
            label: 'Onboarding wizard',
            onSelect: () => {
              navigate('/onboarding');
            },
          },
        ],
        keyboardShortcuts: {
          href: 'https://developer.dynatrace.com/',
        },
        playground: 'default',
        feedback: { onSelect: () => undefined },
        about: 'default',
      }}
    />
  );
};
```


### Default open menu

You can control whether the menu is open when the component is loaded.

### Groups and icons

You can organize menu items into logical groups. Always label groups properly,
either by using the `Menu.Label` and `aria-labelledby`, or by setting an
`aria-label` directly on the group. Optionally, you can add icons using
`Menu.Prefix` or `Menu.Suffix`.

### Tooltips

This example shows how to add tooltips to menu items.

### Nested menus

You can create nested menus by using `Menu` as a child of `Menu.Item`. This
allows you to create multi-level navigation structures.

### Content alignment

The `alignment` prop lets you position the menu content relative to the trigger.

### Intents

Use `Menu.Intent` to add intents.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Default open menu
- Groups and icons
- Tooltips
- Nested menus
- Content alignment
- Intents

### Props

The `Menu` component displays the list of action items that are revealed when
the user clicks on the trigger element.

#### MenuProps
extends`, , ` |
 | Name | Type | Default | Description
 | `defaultOpen?` | | `false` | The open state of the dropdown menu when it is initially rendered. Use when
you do not need to control its open state.
 | `open?` | | | The controlled open state of the dropdown menu. Must be used in conjunction
with onOpenChange.
 | `onOpenChange?` | (isOpen: ) => | | Event handler called when the open state of the dropdown menu changes.
 | `modal?` | | `true` | The modality of the dialog.
When set to true, interaction with outside elements will be disabled and
only dialog content will be visible to screen readers.

### Menu.Trigger

Use the `Menu.Trigger` to wrap the element that should open the menu.

#### MenuTriggerProps
extends`, `

### Menu.Content

Use the `Menu.Content` subcomponent to provide the contents of the menu, such as
menu items, links, sub menus, etc.

#### MenuContentProps
extends`, , ` |
 | Name | Type | Default | Description
 | `side?` | | | | | `'bottom'` | The preferred side where the menu content should be rendered relative to the
trigger element. This value may be ignored if collisions occur.
This prop is ignored within submenus.
 | `alignment?` | | | | `'start'` | The horizontal position where the menu content should be rendered relative
to the trigger element. This value may be ignored if collisions occur
or when `side` is set to `'right'` or `'left'`.
This prop is ignored within submenus.
 | `onCloseAutoFocus?` | (event: ) => | | Event handler called when focus moves to the trigger after closing.
It can be prevented by calling event.preventDefault.
 | `avoidCollisions?` | | `true` | When true, overrides the side and align preferences to prevent collisions
with boundary edges.
 | `collisionBoundary?` | | | | | Additional elements can be provided to be included in the boundary check for menu.
By default this is the viewport.

### Menu.Intent

Use `Menu.Intent` to render a menu item that sends an intent.

#### MenuIntentProps

##### Signature:
`export declare type MenuIntentProps = | ;`

### Menu.Item

Provide the individual menu items using the `Menu.Item` subcomponent. To specify
what happens when a `Menu.Item` is selected, the `onSelect` callback needs to be
defined.

#### MenuItemProps

##### Signature:
`export declare type MenuItemProps = ;`

#### MenuItemOwnProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `disabled?` | | | Whether the menu item is disabled.
If `true`, it prevents the user from interacting with the item and the item
being focused.
 | `textValue?` | | | Optional text used for typeahead purposes. By default, the typeahead
behavior will use the `.textContent` of the item. Use this when the content
is complex, or you have non-textual content inside.
 | `onSelect` | | | Event handler called when the user selects an item (via mouse or keyboard).
Calling `event.preventDefault()` in this handler prevents the dropdown menu
from closing when selecting that item.

### Menu.ItemTooltip

`Menu.ItemTooltip` can be added as a child to a `Menu.Item` to provide
additional information when you hover or focus on the item.

#### MenuItemTooltipProps

##### Signature:
`export declare type MenuItemTooltipProps = & ;`

### Menu.Prefix

Use the `Menu.Prefix` to add an icon on the left side of a `Menu.Item`.

#### MenuPrefixProps
extends`, , , , `

### Menu.Suffix

Use the `Menu.Suffix` to add an icon on the right side of a `Menu.Item`.

#### MenuSuffixProps
extends`, , , `

### Menu.Link

Use the `Menu.Link` subcomponent to display links inside the menu.

#### MenuLinkProps

##### Signature:
`export declare type MenuLinkProps = ;`

### Menu.Group

Use the `Menu.Group` subcomponent to group multiple items in the menu content.

#### MenuGroupProps
extends`, , , `

### Menu.Label

`Menu.Label` allows you to add a descriptive label inside the menu content. The
rendered label is not focusable via the arrow keys.

#### MenuLabelProps
extends`, , `

### Menu.Sub

The `Menu.Sub` component allows you to add a submenu.

#### MenuSubProps
extends |
 | Name | Type | Default | Description
 | `defaultOpen?` | | | The open state of the dropdown menu when it is initially rendered. Use when
you do not need to control its open state.
 | `open?` | | | The controlled open state of the dropdown menu. Must be used in conjunction
with onOpenChange.
 | `onOpenChange?` | (isOpen: ) => | | Event handler called when the open state of the dropdown menu changes.

### Menu.SubTrigger

Use the `Menu.SubTrigger` to wrap the element that should open the submenu.

#### MenuSubTriggerProps
extends`, ` |
 | Name | Type | Default | Description
 | `disabled?` | | | Whether the menu trigger item is disabled.
If true, it prevents the user from interacting with the item.
 | `textValue?` | | | Optional text used for typeahead purposes. By default, the typeahead
behavior will use the .textContent of the item. Use this when the content
is complex, or you have non-textual content inside.

### Menu.SubContent

Use the `Menu.SubContent` component to provide the contents of the submenu.

#### MenuSubContentProps

##### Signature:
`export declare type MenuSubContentProps = ;`Still have questions?Find answers in the Dynatrace Community
- Menu.Trigger
- Menu.Content
- Menu.Intent
- Menu.Item
- Menu.ItemTooltip
- Menu.Prefix
- Menu.Suffix
- Menu.Link
- Menu.Group
- Menu.Label
- Menu.Sub
- Menu.SubTrigger
- Menu.SubContent

---

## Tabs

`/design/components/navigation/Tabs/`

Tabs organize related content by grouping similar information into views or tab
panels that are displayed one at a time.

### Import

`tsx
import { Tab, Tabs } from '@dynatrace/strato-components/navigation';
`

### Use cases

#### Use icons in tabs

By using `prefixIcon` you can add icons to each tab.

#### Disable tab

The disabled prop allows you to disable specific tabs. In the example below, the
third tab is disabled.

#### Default open tab

Allows you to open a specific tab when the component is loaded. In the example
below, the third tab is open when component is loaded.

```tsx
import { Flex } from '@dynatrace/strato-components/layouts';
import { Tab, Tabs } from '@dynatrace/strato-components/navigation';
import { Text } from '@dynatrace/strato-components/typography';

const DefaultOpen = () => {
  return (
    <Tabs defaultIndex={2}>
      <Tab title="Digital Experience">
        <Flex flexDirection="column">
          <Text>
            Improve user experiences with best-in-class digital experience
            monitoring. Ensure every application is available, functional, fast,
            and efficient across every channel including mobile, web, IoT, and
            APIs.
          </Text>
        </Flex>
      </Tab>
      <Tab title="Business Analytics">
        <Flex flexDirection="column">
          <Text>
            Drive better business outcomes across web, mobile, and IoT channels
            through digital application analytics that deliver real-time
            visibility into business KPIs and improve IT and business
            collaboration.
          </Text>
        </Flex>
      </Tab>
      <Tab title="Cloud Automation">
        <Flex flexDirection="column">
          <Text>
            Empower DevOps platform engineers, SREs, and Development teams to
            deliver higher quality software faster and more securely.
          </Text>
        </Flex>
      </Tab>
    </Tabs>
  );
};
```

```tsx
import { Flex } from '@dynatrace/strato-components/layouts';
import { Tab, Tabs } from '@dynatrace/strato-components/navigation';
import { Text } from '@dynatrace/strato-components/typography';

const DefaultOpen = () => {
  return (
    <Tabs defaultIndex={2}>
      <Tab title="Digital Experience">
        <Flex flexDirection="column">
          <Text>
            Improve user experiences with best-in-class digital experience
            monitoring. Ensure every application is available, functional, fast,
            and efficient across every channel including mobile, web, IoT, and
            APIs.
          </Text>
        </Flex>
      </Tab>
      <Tab title="Business Analytics">
        <Flex flexDirection="column">
          <Text>
            Drive better business outcomes across web, mobile, and IoT channels
            through digital application analytics that deliver real-time
            visibility into business KPIs and improve IT and business
            collaboration.
          </Text>
        </Flex>
      </Tab>
      <Tab title="Cloud Automation">
        <Flex flexDirection="column">
          <Text>
            Empower DevOps platform engineers, SREs, and Development teams to
            deliver higher quality software faster and more securely.
          </Text>
        </Flex>
      </Tab>
    </Tabs>
  );
};
```


#### Control the state

#### Change the panel overflow

The `panelOverflow` prop allows you to enable/disable vertical scrolling when
the content would overflow the tab panel.

#### Keep Tabs mounted

By default, when the `Tab` content is not visible to the user, it will also be
removed from the DOM to prevent unwanted component updates on hidden elements.
If you want to keep the `Tab`s content in the DOM to preserve the state, you can
set the `keepMounted` prop on the component.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Use icons in tabs
- Disable tab
- Default open tab
- Control the state
- Change the panel overflow
- Keep Tabs mounted

```tsx
import { Flex } from '@dynatrace/strato-components/layouts';
import { Tab, Tabs } from '@dynatrace/strato-components/navigation';

const KeepMounted = () => {
  return (
    <Tabs>
      <Tab title="Infrastructure Monitoring">
        <Flex flexDirection="column">
          Get automatic and intelligent observability across cloud and hybrid
          environments with continuous auto-discovery of hosts, VMs, serverless,
          cloud services, containers and Kubernetes, network, devices, logs,
          events and more - all in context, with precise, AI-powered answers.
        </Flex>
      </Tab>
      <Tab title="Applications &amp; Microservices" keepMounted>
        <Flex flexDirection="column">
          Get best-in-class APM from the category leader. Automatic and
          intelligent observability at scale for cloud native workloads and
          enterprise apps helps you ensure end-to-end hybrid cloud distributed
          tracing, optimize service performance, innovate faster, collaborate
          efficiently, and deliver more value with less effort.
        </Flex>
      </Tab>
    </Tabs>
  );
};
```

```tsx
import { Flex } from '@dynatrace/strato-components/layouts';
import { Tab, Tabs } from '@dynatrace/strato-components/navigation';

const KeepMounted = () => {
  return (
    <Tabs>
      <Tab title="Infrastructure Monitoring">
        <Flex flexDirection="column">
          Get automatic and intelligent observability across cloud and hybrid
          environments with continuous auto-discovery of hosts, VMs, serverless,
          cloud services, containers and Kubernetes, network, devices, logs,
          events and more - all in context, with precise, AI-powered answers.
        </Flex>
      </Tab>
      <Tab title="Applications &amp; Microservices" keepMounted>
        <Flex flexDirection="column">
          Get best-in-class APM from the category leader. Automatic and
          intelligent observability at scale for cloud native workloads and
          enterprise apps helps you ensure end-to-end hybrid cloud distributed
          tracing, optimize service performance, innovate faster, collaborate
          efficiently, and deliver more value with less effort.
        </Flex>
      </Tab>
    </Tabs>
  );
};
```


### Props

Tabs organize related content by grouping similar information into views or tab
panels that are displayed one at a time.

#### TabsProps

##### Signature:
`export declare type TabsProps = & ( | );`

#### TabsBaseProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `disabled?` | | `false` | Whether the whole tab group is disabled.
 | `id?` | | | The element's unique identifier. See MDN.
 | `children` | | | The collection of tabs to display.
 | `panelOverflow?` | | | | The overflow behavior of the tab panel.

#### TabsControlledProps
 |
 | Name | Type | Default | Description
 | `selectedIndex` | | | The index of the selected tab.
 | `onChange` | (selectedIndex: ) => | | Handler that is called when the selected tab changes.

#### TabsUncontrolledProps
 |
 | Name | Type | Default | Description
 | `defaultIndex?` | | | The default index of the selected tab.

#### Tab

Use the `Tab` component to specify the content and title for a single tab.

#### TabProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `children` | | | Rendered contents of the option.
 | `disabled?` | | `false` | Whether the tab should be disabled.
If true, the tab cannot be clicked and its tab panel does not render any content.
 | `title` | | | The text shown on the tab. This must be unique.
 | `prefixIcon?` | | | The prefix icon shown in front of the tab text.
 | `keepMounted?` | | `false` | Defines if the tabs content will be kept in the DOM, even if the content
is not shown to the user.Still have questions?Find answers in the Dynatrace Community
- Tab

---

