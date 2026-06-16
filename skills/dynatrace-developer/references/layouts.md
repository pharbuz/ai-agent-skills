# Layouts

Strato design-system components in the **Layouts** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## AppHeader

`/design/components/layouts/AppHeader/`

The AppHeader component is a responsive header with navigation and action items.

### Import

`tsx
import { AppHeader } from '@dynatrace/strato-components/layouts';
`

### Use cases

By itself, the `AppHeader` displays the configured application icon and name as
anchor tag, which links to the root of the application.

Note`AppHeader.NavItems`, `AppHeader.NavItem` and `AppHeader.AppNavLink` have been
renamed for better discoverability.The old names still work like before and can be used interchangeably.
Read more.

#### App navigation

If your app has several high-level features to explore data or personas with
different user goals, levels of knowledge, or access, use `AppHeader.Navigation`
to segment the flows. It will collapse into a menu, if there isn't enough space
in the AppHeader.

```tsx
import { NavLink, Link as RouterLink } from 'react-router';

import { Button } from '@dynatrace/strato-components/buttons';
import { AppHeader, HelpMenu } from '@dynatrace/strato-components/layouts';
import { Tooltip } from '@dynatrace/strato-components/overlays';
import { SettingIcon } from '@dynatrace/strato-icons';

const Navigation = () => {
  return (
    <AppHeader>
      <AppHeader.Navigation>
        <AppHeader.Logo />
        <AppHeader.NavigationItem href="#" isSelected>
          First tab
        </AppHeader.NavigationItem>
        <AppHeader.NavigationItem href="#" disabled isSelected>
          Second tab
        </AppHeader.NavigationItem>
        <AppHeader.NavigationItem href="#" disabled>
          Third tab
        </AppHeader.NavigationItem>
        <AppHeader.NavigationItem to="#" as={NavLink}>
          Fourth tab
        </AppHeader.NavigationItem>
        <AppHeader.NavigationItem to="/#?something" as={RouterLink}>
          Fifth tab
        </AppHeader.NavigationItem>
      </AppHeader.Navigation>
      <AppHeader.Menus>
        <Tooltip text="Settings">
          <Button onClick={() => undefined}>
            <Button.Prefix>
              <SettingIcon />
            </Button.Prefix>
          </Button>
        </Tooltip>
        <HelpMenu
          entries={{
            whatsNew: 'default',
            keyboardShortcuts: 'default',
            playground: 'default',
            about: 'default',
          }}
        />
      </AppHeader.Menus>
    </AppHeader>
  );
};
```

```tsx
import { NavLink, Link as RouterLink } from 'react-router';

import { Button } from '@dynatrace/strato-components/buttons';
import { AppHeader, HelpMenu } from '@dynatrace/strato-components/layouts';
import { Tooltip } from '@dynatrace/strato-components/overlays';
import { SettingIcon } from '@dynatrace/strato-icons';

const Navigation = () => {
  return (
    <AppHeader>
      <AppHeader.Navigation>
        <AppHeader.Logo />
        <AppHeader.NavigationItem href="#" isSelected>
          First tab
        </AppHeader.NavigationItem>
        <AppHeader.NavigationItem href="#" disabled isSelected>
          Second tab
        </AppHeader.NavigationItem>
        <AppHeader.NavigationItem href="#" disabled>
          Third tab
        </AppHeader.NavigationItem>
        <AppHeader.NavigationItem to="#" as={NavLink}>
          Fourth tab
        </AppHeader.NavigationItem>
        <AppHeader.NavigationItem to="/#?something" as={RouterLink}>
          Fifth tab
        </AppHeader.NavigationItem>
      </AppHeader.Navigation>
      <AppHeader.Menus>
        <Tooltip text="Settings">
          <Button onClick={() => undefined}>
            <Button.Prefix>
              <SettingIcon />
            </Button.Prefix>
          </Button>
        </Tooltip>
        <HelpMenu
          entries={{
            whatsNew: 'default',
            keyboardShortcuts: 'default',
            playground: 'default',
            about: 'default',
          }}
        />
      </AppHeader.Menus>
    </AppHeader>
  );
};
```


##### Setting active styles on `NavigationItem`

Set `isSelected` on `AppHeader.NavigationItem` to apply the correct styles.

##### Usage with routing libraries

By default, navigation items and the logo link are rendered as
tags. You can use the `as` prop on `AppHeader.Logo` and
`AppHeader.NavigationItem`s to customize which component is rendered. If you
want to use a routing library like `react-router-dom` you can set
`as={NavLink}`.

`react-router-dom`s `NavLink` automatically adds an `active` css class, so you
don't need to set `isSelected` manually.

```tsx
<AppHeader>
  <AppHeader.Navigation>
    <AppHeader.Logo as={RouterLink} to="#" />
    <AppHeader.NavigationItem as={RouterLink} to="#" isSelected={false}>
      First tab
    </AppHeader.NavigationItem>
    <AppHeader.NavigationItem as={NavLink} to="#">
      Second tab
    </AppHeader.NavigationItem>
  </AppHeader.Navigation>
  <AppHeader.Menus>
    <Tooltip text="Settings">
      <Button onClick={() => undefined}>
        <Button.Prefix>
          <SettingIcon />
        </Button.Prefix>
      </Button>
    </Tooltip>
    <HelpMenu
      entries={{
        whatsNew: 'default',
        keyboardShortcuts: 'default',
        playground: 'default',
        about: 'default',
      }}
    />
  </AppHeader.Menus>
</AppHeader>
```

```tsx
<AppHeader>
  <AppHeader.Navigation>
    <AppHeader.Logo as={RouterLink} to="#" />
    <AppHeader.NavigationItem as={RouterLink} to="#" isSelected={false}>
      First tab
    </AppHeader.NavigationItem>
    <AppHeader.NavigationItem as={NavLink} to="#">
      Second tab
    </AppHeader.NavigationItem>
  </AppHeader.Navigation>
  <AppHeader.Menus>
    <Tooltip text="Settings">
      <Button onClick={() => undefined}>
        <Button.Prefix>
          <SettingIcon />
        </Button.Prefix>
      </Button>
    </Tooltip>
    <HelpMenu
      entries={{
        whatsNew: 'default',
        keyboardShortcuts: 'default',
        playground: 'default',
        about: 'default',
      }}
    />
  </AppHeader.Menus>
</AppHeader>
```


##### Customize the app Logo

The `AppHeader.Logo` component allows you to customize the logos link, text and
icon. It needs to be placed inside `AppHeader.Navigation`.

##### Indicate the release phase of an app

Use the `releasePhase` prop on `AppHeader.Logo` to communicate the release phase
of your app to users. Setting `releasePhase="preview"` displays a "Preview" chip
next to the app name.

#### Use `AppHeader.ActionItems` for app-wide actions

If your app needs to have one or a maximum of two actions always visible on any
page, consider using `AppHeader.ActionItems`.

#### Provide a settings and HelpMenu button

To provide an app-specific help menu for users to find additional help and
information, render the `HelpMenu` component within `AppHeader.Menus`.
Optionally, you can also supply a custom settings button next to the `HelpMenu`.

You can read more about the `HelpMenu` in the
`HelpMenu` docs.Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- App navigation
- Use `AppHeader.ActionItems` for app-wide actions
- Provide a settings and HelpMenu button

### Props

The AppHeader component is a responsive header with navigation and action items.

#### AppHeaderProps
extends`, , , , `

### AppHeader.Logo

You can use the `AppHeader.Logo` component to render a customizable link that
navigates to your app's home page.

#### AppHeaderLogoProps

##### Signature:
`declare type AppHeaderLogoProps = ;`

### AppHeader.AppIcon

You can use the `AppHeader.AppIcon` component to render the icon used for the
app on the platform.

#### AppIconProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `src?` | | | The path to the app icon. If not specified, the icon from the app registry is retrieved automatically.
 | `alt?` | | | The alternative text representation for the image when it's not loaded. If not specified, the app name is used.

### AppHeader.Navigation

You can use the `AppHeader.Navigation` component to render a group of
navigational items (`AppHeader.NavigationItem`s).

Prop Table did not receive data

### AppHeader.NavigationItem

You can use the `AppHeader.NavigationItem` component to render a navigational
item inside the `AppHeader.Navigation` group.

#### AppHeaderNavigationItemProps

##### Signature:
`export declare type AppHeaderNavigationItemProps = ;`

### AppHeader.ActionItems

You can use the `AppHeader.ActionItems` component to render either
`ActionButton`s or a group of `ActionButton`s.

#### AppHeaderActionItemsProps
extends`, , `

### AppHeader.ActionItemGroup

You can use the `AppHeader.ActionItemGroup` component to render a group of
action items.

#### GroupProps
extends`, , `

### AppHeader.ActionButton

You can use the `AppHeader.ActionButton` component to render a button inside the
action items section or inside a group of action buttons.

#### AppHeaderActionButtonProps

##### Signature:
`export declare type AppHeaderActionButtonProps = ;`Still have questions?Find answers in the Dynatrace Community
- AppHeader.Logo
- AppHeader.AppIcon
- AppHeader.Navigation
- AppHeader.NavigationItem
- AppHeader.ActionItems
- AppHeader.ActionItemGroup
- AppHeader.ActionButton

---

## Container

`/design/components/layouts/Container/`

Containers can be used to group content that is related. Additionally, they
emphasize and highlight your grouped content.

### Import

`tsx
import { Container } from '@dynatrace/strato-components/layouts';
`

### Use cases

#### Change the Container variant

Use the `variant` prop to create the different contextual container variants.
When no `variant` is specified, it is set to `default`.

#### Change the Container color

By default, the container has the color `neutral`. You should always consider
the meaning behind the colors when changing this.

#### Polymorph the Container component

By default, the container component is rendered as a standard `div` element. For
layouting purposes, the component can be polymorphed to any other component.
This can be used, for example, to create a Flex layout inside a container
component.

#### Add layout styles to the Container component

The container component has a default padding of 16px. This can be changed by
setting any padding prop on the container. Similarly, the container also accepts
any CSS margin and layout props, such as width or height.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change the Container variant
- Change the Container color
- Polymorph the Container component
- Add layout styles to the Container component

### Props

Containers can be used to group content that is related. Additionally, they
emphasize and highlight your grouped content.

#### ContainerProps

##### Signature:
`export declare type ContainerProps = ;`

#### ContainerOwnProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `variant?` | | | | | `'default'` | The visual style of the container.
 | `color?` | | | | | | `'neutral'` | The color of the container. This should be chosen based on the context
the container is used in.

#### SpacingProps
 |
 | Name | Type | Default | Description
 | `padding?` | | | Defines CSS padding property
 | `p?` | | | Defines CSS padding property
 | `paddingX?` | | | Defines CSS x padding property
 | `px?` | | | Defines CSS x padding property
 | `paddingY?` | | | Defines CSS y padding property
 | `py?` | | | Defines CSS y padding property
 | `paddingTop?` | | | Defines CSS top padding property
 | `pt?` | | | Defines CSS top padding property
 | `paddingRight?` | | | Defines CSS right padding property
 | `pr?` | | | Defines CSS right padding property
 | `paddingBottom?` | | | Defines CSS bottom padding property
 | `pb?` | | | Defines CSS bottom padding property
 | `paddingLeft?` | | | Defines CSS left padding property
 | `pl?` | | | Defines CSS left padding property
 | `margin?` | | | Defines CSS margin property
 | `m?` | | | Defines CSS margin property
 | `marginX?` | | | Defines CSS x margin property
 | `mx?` | | | Defines CSS x margin property
 | `marginY?` | | | Defines CSS y margin property
 | `my?` | | | Definesy CSS margin property
 | `marginTop?` | | | Defines CSS top margin property
 | `mt?` | | | Defines CSS top margin property
 | `marginRight?` | | | Defines CSS right margin property
 | `mr?` | | | Defines CSS right margin property
 | `marginBottom?` | | | Defines CSS bottom margin property
 | `mb?` | | | Defines bottom margin property
 | `marginLeft?` | | | Defines CSS left margin property
 | `ml?` | | | Defines CSS left margin property

#### LayoutSizeProps
 |
 | Name | Type | Default | Description
 | `width?` | [] | | CSS width property
 | `minWidth?` | [] | | CSS min width property
 | `maxWidth?` | [] | | CSS max width property
 | `height?` | [] | | CSS height property
 | `minHeight?` | [] | | CSS min height property
 | `maxHeight?` | [] | | CSS max height propertyStill have questions?Find answers in the Dynatrace Community

---

## Divider

`/design/components/layouts/Divider/`

The `Divider` component visually separates groups of content.

OverviewProperties

### Import

`tsx
import { Divider } from '@dynatrace/strato-components/layouts';
`

### Use cases

#### Change the orientation

A vertical `Divider` creates a toolbar-like separation of two content sections.
The `orientation` prop lets you control whether the divider should be `vertical`
or `horizontal`.

#### Change the variant

Use the `variant` prop to create the different contextual divider variants.

#### Change the color

Use the `color` prop to change the color of the dividing line according to your
context.

#### Use it without flex styles

The `flexItem` prop allows you to control whether flex styles are applied for
the `Divider`. Flex styles are enabled by default, ensuring the automatic
application of the right styles for usage within a flex layout.

When using the `Divider` outside of a flex layout, you can set the `flexItem`
prop to `false`. In this case, you need to wrap the `Divider` in a block-level
HTML element and set the desired dimension on that element.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change the orientation
- Change the variant
- Change the color
- Use it without flex styles

### Props

The `Divider` component visually separates groups of content.

OverviewProperties

#### DividerProps
extends`, , ` |
 | Name | Type | Default | Description
 | `orientation?` | | | `'horizontal'` | Orientation of the Divider component.
 | `as?` | | | `'div'` | Control the HTML tag used for rendering the Divider.
 | `flexItem?` | | `true` | Indicate whether the Divider is used inside a Flex component to apply the right styling.
If set to false, make sure to have an explicit width/height style set on a parent HTML tag.
 | `color?` | | | | | | `'neutral'` | The color of the Divider.
 | `variant?` | | | `'default'` | The visual style of the Divider.Still have questions?Find answers in the Dynatrace Community

---

## Flex

`/design/components/layouts/Flex/`

The `Flex` component can be used to layout its children with Flexbox. The
component can be customized with flexbox props.

More information about
Flexbox.

OverviewProperties

### Import

`tsx
import { Flex } from '@dynatrace/strato-components/layouts';
`

### Use cases

#### Flex props

In the example below the `flexDirection` prop is used. The same approach can be
used for other flexbox properties.

```tsx
import { Flex, Container } from '@dynatrace/strato-components/layouts';

const FlexDirection = () => {
  return (
    <Flex flexDirection="row" width="100%">
      <Container>Box 1</Container>
      <Container>Box 2</Container>
      <Container>Box 3</Container>
    </Flex>
  );
};
```

```tsx
import { Flex, Container } from '@dynatrace/strato-components/layouts';

const FlexDirection = () => {
  return (
    <Flex flexDirection="row" width="100%">
      <Container>Box 1</Container>
      <Container>Box 2</Container>
      <Container>Box 3</Container>
    </Flex>
  );
};
```


#### Flex item

The prop `flexItem` can be set on any Flex component to mark it as a child of
another Flex component. When a Flex component is set to `flexItem`, properties
for flexbox items can be used on that component.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Flex props
- Flex item

```tsx
import { Flex, Container } from '@dynatrace/strato-components/layouts';

const FlexItem = () => {
  return (
    <Flex flexDirection="row" width="100%">
      <Container>Box 1</Container>
      <Flex flexItem flexGrow={2}>
        <Container>Box 2</Container>
      </Flex>
      <Container>Box 3</Container>
    </Flex>
  );
};
```

```tsx
import { Flex, Container } from '@dynatrace/strato-components/layouts';

const FlexItem = () => {
  return (
    <Flex flexDirection="row" width="100%">
      <Container>Box 1</Container>
      <Flex flexItem flexGrow={2}>
        <Container>Box 2</Container>
      </Flex>
      <Container>Box 3</Container>
    </Flex>
  );
};
```


### Props

The `Flex` component can be used to layout its children with Flexbox. The
component can be customized with flexbox props.

More information about
Flexbox.

OverviewProperties

#### FlexProps

##### Signature:
`export declare type FlexProps = ;`

#### FlexOwnProps

##### Signature:
`export declare type FlexOwnProps = & & & & & ;`

#### FlexStyleProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `order?` | [] | | Defines order
 | `flexGrow?` | [] | | Defines flex grow
 | `flexShrink?` | [] | | Defines flex shrink
 | `flexBasis?` | [] | | Defines flex basis
 | `flex?` | [] | | Defines flex
 | `flexDirection?` | [] | | Defines flex direction
 | `flexWrap?` | [] | | Defines flex wrap
 | `flexFlow?` | [] | | Defines flex flow
 | `gridColumnStart?` | [] | | Defines grid column start
 | `gridColumnEnd?` | [] | | Defines grid column end
 | `gridRowStart?` | [] | | Defines grid row start
 | `gridRowEnd?` | [] | | Defines grid row end
 | `gridColumn?` | [] | | Defines grid column
 | `gridRow?` | [] | | Defines grid row
 | `gridArea?` | [] | | Defines grid area

#### GridFlexPositionProps
 |
 | Name | Type | Default | Description
 | `justifySelf?` | | | justify self positions
 | `alignSelf?` | | | align self positions
 | `placeSelf?` | | | place self positions
 | `justifyItems?` | | | justify items positions
 | `alignItems?` | | | align items positions
 | `placeItems?` | | | place items positions
 | `justifyContent?` | | | justify content positions
 | `alignContent?` | | | align content positions
 | `placeContent?` | | | place content positions

#### GapProps
 |
 | Name | Type | Default | Description
 | `gap?` | | | Defines gap
 | `rowGap?` | | | Defines row gap
 | `columnGap?` | | | Defines column gap

#### LayoutSizeProps
 |
 | Name | Type | Default | Description
 | `width?` | [] | | CSS width property
 | `minWidth?` | [] | | CSS min width property
 | `maxWidth?` | [] | | CSS max width property
 | `height?` | [] | | CSS height property
 | `minHeight?` | [] | | CSS min height property
 | `maxHeight?` | [] | | CSS max height property

#### SpacingProps
 |
 | Name | Type | Default | Description
 | `padding?` | | | Defines CSS padding property
 | `p?` | | | Defines CSS padding property
 | `paddingX?` | | | Defines CSS x padding property
 | `px?` | | | Defines CSS x padding property
 | `paddingY?` | | | Defines CSS y padding property
 | `py?` | | | Defines CSS y padding property
 | `paddingTop?` | | | Defines CSS top padding property
 | `pt?` | | | Defines CSS top padding property
 | `paddingRight?` | | | Defines CSS right padding property
 | `pr?` | | | Defines CSS right padding property
 | `paddingBottom?` | | | Defines CSS bottom padding property
 | `pb?` | | | Defines CSS bottom padding property
 | `paddingLeft?` | | | Defines CSS left padding property
 | `pl?` | | | Defines CSS left padding property
 | `margin?` | | | Defines CSS margin property
 | `m?` | | | Defines CSS margin property
 | `marginX?` | | | Defines CSS x margin property
 | `mx?` | | | Defines CSS x margin property
 | `marginY?` | | | Defines CSS y margin property
 | `my?` | | | Definesy CSS margin property
 | `marginTop?` | | | Defines CSS top margin property
 | `mt?` | | | Defines CSS top margin property
 | `marginRight?` | | | Defines CSS right margin property
 | `mr?` | | | Defines CSS right margin property
 | `marginBottom?` | | | Defines CSS bottom margin property
 | `mb?` | | | Defines bottom margin property
 | `marginLeft?` | | | Defines CSS left margin property
 | `ml?` | | | Defines CSS left margin property

#### FlexItemStyleProps
 |
 | Name | Type | Default | Description
 | `flexItem?` | | | Determines whether this is a flex item.
If true, display: 'flex' style will not be added.Still have questions?Find answers in the Dynatrace Community

---

## Grid

`/design/components/layouts/Grid/`

The `Grid` component can be used to layout its children with the help of CSS
Grid. The component can be customized with CSS grid props.

More information about
CSS Grid.

OverviewProperties

### Import

`tsx
import { Grid } from '@dynatrace/strato-components/layouts';
`

### Use cases

#### Grid props

In the example below the `gridTemplateColumns` prop is used. The same approach
can be used for other CSS grid properties.

```tsx
import { Grid, Container } from '@dynatrace/strato-components/layouts';

const Basic = () => {
  return (
    <Grid gridTemplateColumns="repeat(3, 1fr)">
      <Container>Box 1</Container>
      <Container>Box 2</Container>
      <Container>Box 3</Container>
    </Grid>
  );
};
```

```tsx
import { Grid, Container } from '@dynatrace/strato-components/layouts';

const Basic = () => {
  return (
    <Grid gridTemplateColumns="repeat(3, 1fr)">
      <Container>Box 1</Container>
      <Container>Box 2</Container>
      <Container>Box 3</Container>
    </Grid>
  );
};
```


#### Grid item

The prop `gridItem` can be set on any `Grid` component to mark it as a child of
another `Grid` component. When a `Grid` component is set to `gridItem`,
properties for CSS grid items can be used on that component.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Grid props
- Grid item

```tsx
import { Grid, Container } from '@dynatrace/strato-components/layouts';

const GridItem = () => {
  return (
    <Grid
      width="100%"
      gap={20}
      gridTemplateColumns="repeat(2, 1fr)"
      gridTemplateAreas="'one one' 'A B' 'C D'"
    >
      <Grid gridItem gridArea="one">
        <Container>Grid Header</Container>
      </Grid>
      <Grid gridItem key="A" gridArea="A">
        <Container>A</Container>
      </Grid>
      <Grid gridItem key="B" gridArea="B">
        <Container>B</Container>
      </Grid>
      <Grid gridItem key="C" gridArea="C">
        <Container>C</Container>
      </Grid>
      <Grid gridItem key="D" gridArea="D">
        <Container>D</Container>
      </Grid>
    </Grid>
  );
};
```

```tsx
import { Grid, Container } from '@dynatrace/strato-components/layouts';

const GridItem = () => {
  return (
    <Grid
      width="100%"
      gap={20}
      gridTemplateColumns="repeat(2, 1fr)"
      gridTemplateAreas="'one one' 'A B' 'C D'"
    >
      <Grid gridItem gridArea="one">
        <Container>Grid Header</Container>
      </Grid>
      <Grid gridItem key="A" gridArea="A">
        <Container>A</Container>
      </Grid>
      <Grid gridItem key="B" gridArea="B">
        <Container>B</Container>
      </Grid>
      <Grid gridItem key="C" gridArea="C">
        <Container>C</Container>
      </Grid>
      <Grid gridItem key="D" gridArea="D">
        <Container>D</Container>
      </Grid>
    </Grid>
  );
};
```


### Props

The `Grid` component can be used to layout its children with the help of CSS
Grid. The component can be customized with CSS grid props.

More information about
CSS Grid.

OverviewProperties

#### GridProps

##### Signature:
`export declare type GridProps = ;`

#### GridOwnProps

##### Signature:
`export declare type GridOwnProps = & & & & & ;`

#### GridFlexPositionProps
 |
 | Name | Type | Default | Description
 | `justifySelf?` | | | justify self positions
 | `alignSelf?` | | | align self positions
 | `placeSelf?` | | | place self positions
 | `justifyItems?` | | | justify items positions
 | `alignItems?` | | | align items positions
 | `placeItems?` | | | place items positions
 | `justifyContent?` | | | justify content positions
 | `alignContent?` | | | align content positions
 | `placeContent?` | | | place content positions

#### GapProps
 |
 | Name | Type | Default | Description
 | `gap?` | | | Defines gap
 | `rowGap?` | | | Defines row gap
 | `columnGap?` | | | Defines column gap

#### LayoutSizeProps
 |
 | Name | Type | Default | Description
 | `width?` | [] | | CSS width property
 | `minWidth?` | [] | | CSS min width property
 | `maxWidth?` | [] | | CSS max width property
 | `height?` | [] | | CSS height property
 | `minHeight?` | [] | | CSS min height property
 | `maxHeight?` | [] | | CSS max height property

#### SpacingProps
 |
 | Name | Type | Default | Description
 | `padding?` | | | Defines CSS padding property
 | `p?` | | | Defines CSS padding property
 | `paddingX?` | | | Defines CSS x padding property
 | `px?` | | | Defines CSS x padding property
 | `paddingY?` | | | Defines CSS y padding property
 | `py?` | | | Defines CSS y padding property
 | `paddingTop?` | | | Defines CSS top padding property
 | `pt?` | | | Defines CSS top padding property
 | `paddingRight?` | | | Defines CSS right padding property
 | `pr?` | | | Defines CSS right padding property
 | `paddingBottom?` | | | Defines CSS bottom padding property
 | `pb?` | | | Defines CSS bottom padding property
 | `paddingLeft?` | | | Defines CSS left padding property
 | `pl?` | | | Defines CSS left padding property
 | `margin?` | | | Defines CSS margin property
 | `m?` | | | Defines CSS margin property
 | `marginX?` | | | Defines CSS x margin property
 | `mx?` | | | Defines CSS x margin property
 | `marginY?` | | | Defines CSS y margin property
 | `my?` | | | Definesy CSS margin property
 | `marginTop?` | | | Defines CSS top margin property
 | `mt?` | | | Defines CSS top margin property
 | `marginRight?` | | | Defines CSS right margin property
 | `mr?` | | | Defines CSS right margin property
 | `marginBottom?` | | | Defines CSS bottom margin property
 | `mb?` | | | Defines bottom margin property
 | `marginLeft?` | | | Defines CSS left margin property
 | `ml?` | | | Defines CSS left margin property

#### GridItemStyleProps
 |
 | Name | Type | Default | Description
 | `gridItem?` | | | Determines whether this is a grid item.
If true, display: 'grid' style will not be added.

#### GridStyleProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `order?` | [] | | Defines order
 | `flexGrow?` | [] | | Defines flex grow
 | `flexShrink?` | [] | | Defines flex shrink
 | `flexBasis?` | [] | | Defines flex basis
 | `flex?` | [] | | Defines flex
 | `gridTemplateColumns?` | [] | | Defines grid template columns
 | `gridTemplateRows?` | [] | | Defines grid template rows
 | `gridTemplateAreas?` | [] | | Defines grid template areas
 | `gridTemplate?` | [] | | Defines grid template
 | `gridAutoColumns?` | [] | | Defines grid auto columns
 | `gridAutoRows?` | [] | | Defines grid auto rows
 | `gridAutoFlow?` | [] | | Defines grid auto flow
 | `grid?` | [] | | Defines grid
 | `gridColumnStart?` | [] | | Defines grid column start
 | `gridColumnEnd?` | [] | | Defines grid column end
 | `gridRowStart?` | [] | | Defines grid row start
 | `gridRowEnd?` | [] | | Defines grid row end
 | `gridColumn?` | [] | | Defines grid column
 | `gridRow?` | [] | | Defines grid row
 | `gridArea?` | [] | | Defines grid areaStill have questions?Find answers in the Dynatrace Community

---

## HelpMenu

`/design/components/layouts/HelpMenu/`

A prebuilt menu as entrypoint for app specific help links and actions.

OverviewProperties

### Import

`tsx
import { HelpMenu } from '@dynatrace/strato-components/layouts';
`

### Use cases

The `HelpMenu` is a batteries-included, prebuilt menu with commonly used
entries.

#### Defaults

Some entries provide `'default'` as possible value, which will enable default
behavior when clicking the entry. Some entries use
intents so you need to have
your app configured correctly so `appId` and `appVersion` are set.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Defaults

```tsx
import { HelpMenu } from '@dynatrace/strato-components/layouts';

const Defaults = () => {
  return (
    <HelpMenu
      entries={{
        whatsNew: 'default',
        keyboardShortcuts: 'default',
        playground: 'default',
        about: 'default',
      }}
    />
  );
};
```

```tsx
import { HelpMenu } from '@dynatrace/strato-components/layouts';

const Defaults = () => {
  return (
    <HelpMenu
      entries={{
        whatsNew: 'default',
        keyboardShortcuts: 'default',
        playground: 'default',
        about: 'default',
      }}
    />
  );
};
```


### Props

A prebuilt menu as entrypoint for app specific help links and actions.

OverviewProperties

#### HelpMenuProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `entries` | {
 whatsNew?: | | ;
 getStarted?: | | ;
 documentation?: | | ;
 keyboardShortcuts?: | | ;
 playground?: | | ;
 feedback?: | | ;
 about?: | | ;
 } | |
 | `onOpenChange?` | (isOpen: ) => | | Still have questions?Find answers in the Dynatrace Community

---

## InputGroup

`/design/components/layouts/InputGroup/`

The `InputGroup` component is the outermost layout component of a field
component (for example `TextInput`), providing support for grouping.

### Import

`tsx
import { InputGroup } from '@dynatrace/strato-components/layouts';
`

### Use cases

The `InputGroup` component provides a way to visually group multiple components.
Supported components include:

- Button

- Select

- TextInput

- DateTimePicker

- TimeframeSelector

- Menu

#### Classname

To group components that are not directly supported, you can use the classname
`inputGroupClassName`.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Classname

```tsx
import {
  Flex,
  Container,
  InputGroup,
  inputGroupClassName,
} from '@dynatrace/strato-components/layouts';

const Classname = () => {
  return (
    <Flex flexDirection="column">
      <InputGroup>
        <Container>Container without classname</Container>
        <Container>Container without classname</Container>
      </InputGroup>
      <InputGroup>
        <Container className={inputGroupClassName}>
          Container with classname
        </Container>
        <Container className={inputGroupClassName}>
          Container with classname
        </Container>
      </InputGroup>
    </Flex>
  );
};
```

```tsx
import {
  Flex,
  Container,
  InputGroup,
  inputGroupClassName,
} from '@dynatrace/strato-components/layouts';

const Classname = () => {
  return (
    <Flex flexDirection="column">
      <InputGroup>
        <Container>Container without classname</Container>
        <Container>Container without classname</Container>
      </InputGroup>
      <InputGroup>
        <Container className={inputGroupClassName}>
          Container with classname
        </Container>
        <Container className={inputGroupClassName}>
          Container with classname
        </Container>
      </InputGroup>
    </Flex>
  );
};
```


### Props

The `InputGroup` component is the outermost layout component of a field
component (for example `TextInput`), providing support for grouping.

#### InputGroupProps
extends`, , , , `Still have questions?Find answers in the Dynatrace Community

---

## Page

`/design/components/layouts/Page/`

The `Page` component provides the basic layout for your app with slots for a
header, sidebar, main content, and a detail view. The `Main` slot is the only
slot that is mandatory for rendering the `Page`; every other slot is optional.

Check out the UI and design guidelines
for more information on how to structure your app using the page.

### Import

`tsx
import { Page } from '@dynatrace/strato-components/layouts';
`

### Use cases

#### Integrated controls

The page can show integrated controls to dismiss and close the `Sidebar` panel,
without you having to manually add buttons to your content sections. You can
enable this feature by setting the `integratedControls` prop on the `Sidebar`
component. Integrated controls show when hovering the `Sidebar` panel or when
the panel is dismissed.

```tsx
<Page>
  <Page.Header>
    <AppHeader>
      <AppHeader.Navigation>
        <AppHeader.Logo appName="MyApp" />
      </AppHeader.Navigation>
    </AppHeader>
  </Page.Header>
  <Page.Sidebar integratedControls>
    <TitleBar>
      <TitleBar.Title>Sidebar</TitleBar.Title>
      <TitleBar.Subtitle>e.g. for navigation</TitleBar.Subtitle>
    </TitleBar>
  </Page.Sidebar>
  <Page.Main style={{ display: 'flex', flexDirection: 'column' }}>
    <TitleBar>
      <TitleBar.Title>Main</TitleBar.Title>
      <TitleBar.Subtitle>
        Place your main content in this area
      </TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton target="details" />
      </TitleBar.Action>
    </TitleBar>
    <Placeholder />
  </Page.Main>
  <Page.DetailView style={{ display: 'flex', flexDirection: 'column' }}>
    <TitleBar>
      <TitleBar.Title>Settings</TitleBar.Title>
      <TitleBar.Subtitle>
        For content related to the main area
      </TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton />
      </TitleBar.Action>
    </TitleBar>
    <Placeholder />
  </Page.DetailView>
</Page>
```

```tsx
<Page>
  <Page.Header>
    <AppHeader>
      <AppHeader.Navigation>
        <AppHeader.Logo appName="MyApp" />
      </AppHeader.Navigation>
    </AppHeader>
  </Page.Header>
  <Page.Sidebar integratedControls>
    <TitleBar>
      <TitleBar.Title>Sidebar</TitleBar.Title>
      <TitleBar.Subtitle>e.g. for navigation</TitleBar.Subtitle>
    </TitleBar>
  </Page.Sidebar>
  <Page.Main style={{ display: 'flex', flexDirection: 'column' }}>
    <TitleBar>
      <TitleBar.Title>Main</TitleBar.Title>
      <TitleBar.Subtitle>
        Place your main content in this area
      </TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton target="details" />
      </TitleBar.Action>
    </TitleBar>
    <Placeholder />
  </Page.Main>
  <Page.DetailView style={{ display: 'flex', flexDirection: 'column' }}>
    <TitleBar>
      <TitleBar.Title>Settings</TitleBar.Title>
      <TitleBar.Subtitle>
        For content related to the main area
      </TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton />
      </TitleBar.Action>
    </TitleBar>
    <Placeholder />
  </Page.DetailView>
</Page>
```


#### Define responsive layouts

The page handles different screen sizes internally. On smaller screens, a drawer
is used for `Sidebar` and `DetailView` instead of rendering them next to the
`Main` panel. You can configure the breakpoints to determine when to switch to
the drawer.

Default breakpoints:

- `DetailView`: tablet

- `Sidebar`: mobile

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  NumberInputV2 as NumberInput,
} from '@dynatrace/strato-components/forms';
import {
  AppHeader,
  Page,
  TitleBar,
} from '@dynatrace/strato-components/layouts';
import Borders from '@dynatrace/strato-design-tokens/borders';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';
import {
  CloseSidebarIcon,
  OpenSidebarIcon,
  SettingIcon,
  XmarkIcon,
} from '@dynatrace/strato-icons';

const MobileConfig = () => {
  const [isDetailViewDismissed, setIsDetailViewDismissed] =
    useState<boolean>(false);
  const [isSidebarDismissed, setIsSidebarDismissed] = useState<boolean>(false);
  const [breakpoint, setBreakpoint] = useState<number | null>(920);

  return (
    <Page>
      <Page.Header>
        <AppHeader>
          <AppHeader.Navigation>
            <AppHeader.NavigationItem href="/">Home</AppHeader.NavigationItem>
            <AppHeader.NavigationItem href="/">
              Dashboards
            </AppHeader.NavigationItem>
            <AppHeader.NavigationItem href="/">
              Notebooks
            </AppHeader.NavigationItem>
          </AppHeader.Navigation>
        </AppHeader>
      </Page.Header>
      <Page.Sidebar
        dismissed={isSidebarDismissed}
        onDismissChange={(state) => {
          setIsSidebarDismissed(state);
        }}
      >
        <TitleBar>
          <TitleBar.Title>Sidebar</TitleBar.Title>
          <TitleBar.Subtitle>e.g. for navigation</TitleBar.Subtitle>
          <TitleBar.Action>
            <Button
              onClick={() => setIsSidebarDismissed(true)}
              aria-label="Close sidebar"
            >
              <Button.Prefix>
                <XmarkIcon />
              </Button.Prefix>
            </Button>
          </TitleBar.Action>
        </TitleBar>
      </Page.Sidebar>
      <Page.Main style={{ display: 'flex', flexDirection: 'column' }}>
        <TitleBar>
          <TitleBar.Prefix>
            <Button
              onClick={() => setIsSidebarDismissed(!isSidebarDismissed)}
              aria-label={`${isSidebarDismissed ? 'Open' : 'Close'} sidebar`}
            >
              <Button.Suffix>
                {isSidebarDismissed ? (
                  <OpenSidebarIcon />
                ) : (
                  <CloseSidebarIcon />
                )}
              </Button.Suffix>
            </Button>
          </TitleBar.Prefix>
          <TitleBar.Title>Main</TitleBar.Title>
          <TitleBar.Subtitle>
            Place your main content in this area
          </TitleBar.Subtitle>
          <TitleBar.Action>
            <Button
              onClick={() => setIsDetailViewDismissed(!isDetailViewDismissed)}
              aria-label={`${
                isDetailViewDismissed ? 'Open' : 'Close'
              } settings`}
            >
              <Button.Prefix>
                <SettingIcon />
              </Button.Prefix>
            </Button>
          </TitleBar.Action>
        </TitleBar>
        <div
          style={{
            width: '100%',
            height: '100%',
            marginTop: Spacings.Size24,
            borderRadius: Borders.Radius.Container.Default,
            backgroundColor: Colors.Background.Container.Neutral.Default,
          }}
        />
      </Page.Main>
      <Page.DetailView
        onDismissChange={(state) => {
          setIsDetailViewDismissed(state);
        }}
        dismissed={isDetailViewDismissed}
        breakpoint={breakpoint || 920}
        style={{ display: 'flex', flexDirection: 'column' }}
      >
        <TitleBar>
          <TitleBar.Title>Settings</TitleBar.Title>
          <TitleBar.Subtitle>
            Change the breakpoint to a screen size smaller than the current
            screen to see the Drawer (initially closed).
          </TitleBar.Subtitle>
          <TitleBar.Action>
            <Button
              onClick={() => setIsDetailViewDismissed(true)}
              aria-label="Close details"
            >
              <Button.Prefix>
                <XmarkIcon />
              </Button.Prefix>
            </Button>
          </TitleBar.Action>
        </TitleBar>
        <FormField>
          <Label>
            Change the breakpoint of the detail view, 0 means no mobile layout
            will be used.
          </Label>
          <NumberInput
            aria-label="define breakpoint"
            value={breakpoint}
            onChange={setBreakpoint}
          />
        </FormField>
      </Page.DetailView>
    </Page>
  );
};
```

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  NumberInputV2 as NumberInput,
} from '@dynatrace/strato-components/forms';
import {
  AppHeader,
  Page,
  TitleBar,
} from '@dynatrace/strato-components/layouts';
import Borders from '@dynatrace/strato-design-tokens/borders';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';
import {
  CloseSidebarIcon,
  OpenSidebarIcon,
  SettingIcon,
  XmarkIcon,
} from '@dynatrace/strato-icons';

const MobileConfig = () => {
  const [isDetailViewDismissed, setIsDetailViewDismissed] =
    useState<boolean>(false);
  const [isSidebarDismissed, setIsSidebarDismissed] = useState<boolean>(false);
  const [breakpoint, setBreakpoint] = useState<number | null>(920);

  return (
    <Page>
      <Page.Header>
        <AppHeader>
          <AppHeader.Navigation>
            <AppHeader.NavigationItem href="/">Home</AppHeader.NavigationItem>
            <AppHeader.NavigationItem href="/">
              Dashboards
            </AppHeader.NavigationItem>
            <AppHeader.NavigationItem href="/">
              Notebooks
            </AppHeader.NavigationItem>
          </AppHeader.Navigation>
        </AppHeader>
      </Page.Header>
      <Page.Sidebar
        dismissed={isSidebarDismissed}
        onDismissChange={(state) => {
          setIsSidebarDismissed(state);
        }}
      >
        <TitleBar>
          <TitleBar.Title>Sidebar</TitleBar.Title>
          <TitleBar.Subtitle>e.g. for navigation</TitleBar.Subtitle>
          <TitleBar.Action>
            <Button
              onClick={() => setIsSidebarDismissed(true)}
              aria-label="Close sidebar"
            >
              <Button.Prefix>
                <XmarkIcon />
              </Button.Prefix>
            </Button>
          </TitleBar.Action>
        </TitleBar>
      </Page.Sidebar>
      <Page.Main style={{ display: 'flex', flexDirection: 'column' }}>
        <TitleBar>
          <TitleBar.Prefix>
            <Button
              onClick={() => setIsSidebarDismissed(!isSidebarDismissed)}
              aria-label={`${isSidebarDismissed ? 'Open' : 'Close'} sidebar`}
            >
              <Button.Suffix>
                {isSidebarDismissed ? (
                  <OpenSidebarIcon />
                ) : (
                  <CloseSidebarIcon />
                )}
              </Button.Suffix>
            </Button>
          </TitleBar.Prefix>
          <TitleBar.Title>Main</TitleBar.Title>
          <TitleBar.Subtitle>
            Place your main content in this area
          </TitleBar.Subtitle>
          <TitleBar.Action>
            <Button
              onClick={() => setIsDetailViewDismissed(!isDetailViewDismissed)}
              aria-label={`${
                isDetailViewDismissed ? 'Open' : 'Close'
              } settings`}
            >
              <Button.Prefix>
                <SettingIcon />
              </Button.Prefix>
            </Button>
          </TitleBar.Action>
        </TitleBar>
        <div
          style={{
            width: '100%',
            height: '100%',
            marginTop: Spacings.Size24,
            borderRadius: Borders.Radius.Container.Default,
            backgroundColor: Colors.Background.Container.Neutral.Default,
          }}
        />
      </Page.Main>
      <Page.DetailView
        onDismissChange={(state) => {
          setIsDetailViewDismissed(state);
        }}
        dismissed={isDetailViewDismissed}
        breakpoint={breakpoint || 920}
        style={{ display: 'flex', flexDirection: 'column' }}
      >
        <TitleBar>
          <TitleBar.Title>Settings</TitleBar.Title>
          <TitleBar.Subtitle>
            Change the breakpoint to a screen size smaller than the current
            screen to see the Drawer (initially closed).
          </TitleBar.Subtitle>
          <TitleBar.Action>
            <Button
              onClick={() => setIsDetailViewDismissed(true)}
              aria-label="Close details"
            >
              <Button.Prefix>
                <XmarkIcon />
              </Button.Prefix>
            </Button>
          </TitleBar.Action>
        </TitleBar>
        <FormField>
          <Label>
            Change the breakpoint of the detail view, 0 means no mobile layout
            will be used.
          </Label>
          <NumberInput
            aria-label="define breakpoint"
            value={breakpoint}
            onChange={setBreakpoint}
          />
        </FormField>
      </Page.DetailView>
    </Page>
  );
};
```


#### Controlling panel state

Use the `dismissed` prop and `onDismissChange` callback of the panels to control
the panel state yourself. The `onDismissChange` is called every time a different
dismiss state is suggested with two arguments:

- The expected state

- The reason for the change

There are currently four possible reasons for such a change:

- The viewport width exceeds the breakpoint ('above breakpoint')

- The viewport width is larger than the breakpoint ('below breakpoint')

- The drawer was dismissed by user interaction, either pressing `Escape`
('escape') or clicking on the backdrop ('backdrop')

- The drawer was opened by clicking on the panel hint when using
`integratedControls` ('panel hint')

#### Set minimum panel width

To avoid panels shrinking below a certain value, you can set the `minWidth`.

If you provide a `minWidth` bigger than the `preferredWidth`, the minimum
width overrides the preferred width.

If the combined minimum width of all panels exceeds the viewport width, the
page will have a horizontal scrollbar. Make sure to provide reasonable
breakpoints (see the define responsive layouts section) if you want to avoid
having a horizontal scroll.

#### Save & restore panel sizes

Panel sizes are automatically retained when dismissing and reopening panels.

To restore the panel sizes over full page reloads or navigation, you can utilize
e.g. the `localStorage`. Resize the panels in the page below and use the buttons
to toggle between pages or reload the page to see this in effect.

#### Using the page with react-router

We recommend using `react-router-dom` as the routing library.

The basic concept is to render content based on the matching routes. For
example, you have a set of cards in your main panel. When clicking on a card,
the current route is updated and the `DetailView` content changes accordingly.

##### One page per route

The easiest solution for rendering different pages in your app is to use one
page for each route. This way, you can choose which compounds to use per route
and configure each page separately.

```tsx
import { useState } from 'react';
import { Route, Link as RouterLink, Routes } from 'react-router';

import { AppHeader, Page } from '@dynatrace/strato-components/layouts';

const CommonHeader = () => (
  <Page.Header>
    <AppHeader>
      <AppHeader.Navigation>
        <AppHeader.Logo
          as={RouterLink}
          to="/layouts/page/PagePerRoute/stories/"
          appName="Home"
        />
        <AppHeader.NavigationItem
          as={RouterLink}
          to="/layouts/page/PagePerRoute/stories/page1"
        >
          Workflows
        </AppHeader.NavigationItem>
      </AppHeader.Navigation>
    </AppHeader>
  </Page.Header>
);

const PagePerRoute = () => {
  const [sidebarDismissed, setSidebarDismissed] = useState(false);

  return (
    <Routes>
      <Route
        index
        element={
          <Page>
            <CommonHeader />
            <Page.Main>Main</Page.Main>
          </Page>
        }
      />
      <Route
        path="/page1"
        element={
          <Page>
            <CommonHeader />
            <Page.Sidebar
              dismissed={sidebarDismissed}
              onDismissChange={() => null}
            >
              <Page.PanelControlButton
                onClick={() => setSidebarDismissed(true)}
              />
              Sidebar
            </Page.Sidebar>
            <Page.Main>Main</Page.Main>
          </Page>
        }
      />
    </Routes>
  );
};
```

```tsx
import { useState } from 'react';
import { Route, Link as RouterLink, Routes } from 'react-router';

import { AppHeader, Page } from '@dynatrace/strato-components/layouts';

const CommonHeader = () => (
  <Page.Header>
    <AppHeader>
      <AppHeader.Navigation>
        <AppHeader.Logo
          as={RouterLink}
          to="/layouts/page/PagePerRoute/stories/"
          appName="Home"
        />
        <AppHeader.NavigationItem
          as={RouterLink}
          to="/layouts/page/PagePerRoute/stories/page1"
        >
          Workflows
        </AppHeader.NavigationItem>
      </AppHeader.Navigation>
    </AppHeader>
  </Page.Header>
);

const PagePerRoute = () => {
  const [sidebarDismissed, setSidebarDismissed] = useState(false);

  return (
    <Routes>
      <Route
        index
        element={
          <Page>
            <CommonHeader />
            <Page.Main>Main</Page.Main>
          </Page>
        }
      />
      <Route
        path="/page1"
        element={
          <Page>
            <CommonHeader />
            <Page.Sidebar
              dismissed={sidebarDismissed}
              onDismissChange={() => null}
            >
              <Page.PanelControlButton
                onClick={() => setSidebarDismissed(true)}
              />
              Sidebar
            </Page.Sidebar>
            <Page.Main>Main</Page.Main>
          </Page>
        }
      />
    </Routes>
  );
};
```


##### Nested layouts

The page's compounds can be nested inside other components. This enables you to
create different layouts by nesting routes and rendering different parts of the
page depending on the current route.

Note: The wrapping components of `Sidebar`, `Main`, or `DetailView` must not
render an actual wrapper in the DOM. This would break the page layout. You can
only use components that output the compounds directly, as the `Fragment` or
react-router-dom's `Outlet`.

```tsx
import { useState } from 'react';
import {
  Outlet,
  Route,
  Link as RouterLink,
  Routes,
  useParams,
} from 'react-router';

import { Flex, AppHeader, Page } from '@dynatrace/strato-components/layouts';
import { Link } from '@dynatrace/strato-components/typography';

const RootLayout = () => {
  return (
    <Page>
      <Page.Header>
        <AppHeader>
          <AppHeader.Navigation>
            <AppHeader.Logo as={RouterLink} to="./" appName="Home" />
            <AppHeader.NavigationItem as={RouterLink} to="./workflows">
              Workflows
            </AppHeader.NavigationItem>
          </AppHeader.Navigation>
        </AppHeader>
      </Page.Header>
      <Outlet />
    </Page>
  );
};
const Index = () => <Page.Main>Intro</Page.Main>;
const WorkflowsHome = () => {
  const [sidebarDismissed, setSidebarDismissed] = useState(false);
  return (
    <>
      <Page.Sidebar dismissed={sidebarDismissed} onDismissChange={() => null}>
        <Page.PanelControlButton
          target="sidebar"
          onClick={() => setSidebarDismissed(true)}
        />
        <Flex flexDirection="column">
          Sidebar
          <Link as={RouterLink} to="./workflow1">
            workflow1
          </Link>
          <Link as={RouterLink} to="./workflow2">
            workflow2
          </Link>
        </Flex>
      </Page.Sidebar>
      <Outlet />
    </>
  );
};
const WorkflowsIntro = () => <Page.Main>Workflows intro</Page.Main>;
const WorkflowTasks = () => {
  const { workflow } = useParams();
  return (
    <>
      <Page.Main>
        <Flex flexDirection="column">
          Tasks for workflow {workflow}
          <Link as={RouterLink} to="./task1">
            {workflow} - task1
          </Link>
          <Link as={RouterLink} to="./task2">
            {workflow} - task2
          </Link>
        </Flex>
      </Page.Main>
      <Outlet />
    </>
  );
};
const TaskDetails = () => {
  const { task } = useParams();
  const [detailViewDismissed, setDetailViewDismissed] = useState(false);
  return (
    <Page.DetailView
      dismissed={detailViewDismissed}
      onDismissChange={() => null}
    >
      <Page.PanelControlButton onClick={() => setDetailViewDismissed(true)} />
      Details for task {task}
    </Page.DetailView>
  );
};

const NestedRouterOutlets = () => {
  return (
    <Routes>
      <Route element={<RootLayout />}>
        <Route index element={<Index />} />
        <Route path="workflows" element={<WorkflowsHome />}>
          <Route index element={<WorkflowsIntro />} />
          <Route path=":workflow" element={<WorkflowTasks />}>
            <Route path=":task" element={<TaskDetails />} />
          </Route>
        </Route>
      </Route>
    </Routes>
  );
};
```

```tsx
import { useState } from 'react';
import {
  Outlet,
  Route,
  Link as RouterLink,
  Routes,
  useParams,
} from 'react-router';

import { Flex, AppHeader, Page } from '@dynatrace/strato-components/layouts';
import { Link } from '@dynatrace/strato-components/typography';

const RootLayout = () => {
  return (
    <Page>
      <Page.Header>
        <AppHeader>
          <AppHeader.Navigation>
            <AppHeader.Logo as={RouterLink} to="./" appName="Home" />
            <AppHeader.NavigationItem as={RouterLink} to="./workflows">
              Workflows
            </AppHeader.NavigationItem>
          </AppHeader.Navigation>
        </AppHeader>
      </Page.Header>
      <Outlet />
    </Page>
  );
};
const Index = () => <Page.Main>Intro</Page.Main>;
const WorkflowsHome = () => {
  const [sidebarDismissed, setSidebarDismissed] = useState(false);
  return (
    <>
      <Page.Sidebar dismissed={sidebarDismissed} onDismissChange={() => null}>
        <Page.PanelControlButton
          target="sidebar"
          onClick={() => setSidebarDismissed(true)}
        />
        <Flex flexDirection="column">
          Sidebar
          <Link as={RouterLink} to="./workflow1">
            workflow1
          </Link>
          <Link as={RouterLink} to="./workflow2">
            workflow2
          </Link>
        </Flex>
      </Page.Sidebar>
      <Outlet />
    </>
  );
};
const WorkflowsIntro = () => <Page.Main>Workflows intro</Page.Main>;
const WorkflowTasks = () => {
  const { workflow } = useParams();
  return (
    <>
      <Page.Main>
        <Flex flexDirection="column">
          Tasks for workflow {workflow}
          <Link as={RouterLink} to="./task1">
            {workflow} - task1
          </Link>
          <Link as={RouterLink} to="./task2">
            {workflow} - task2
          </Link>
        </Flex>
      </Page.Main>
      <Outlet />
    </>
  );
};
const TaskDetails = () => {
  const { task } = useParams();
  const [detailViewDismissed, setDetailViewDismissed] = useState(false);
  return (
    <Page.DetailView
      dismissed={detailViewDismissed}
      onDismissChange={() => null}
    >
      <Page.PanelControlButton onClick={() => setDetailViewDismissed(true)} />
      Details for task {task}
    </Page.DetailView>
  );
};

const NestedRouterOutlets = () => {
  return (
    <Routes>
      <Route element={<RootLayout />}>
        <Route index element={<Index />} />
        <Route path="workflows" element={<WorkflowsHome />}>
          <Route index element={<WorkflowsIntro />} />
          <Route path=":workflow" element={<WorkflowTasks />}>
            <Route path=":task" element={<TaskDetails />} />
          </Route>
        </Route>
      </Route>
    </Routes>
  );
};
```


#### Scroll behavior

Each of the panels of the page will be a scroll container if the content
overflows. If you switch from an already scrolled panel to another scrollable
content in the same panel, the browser will remember the old scroll position.
You may want to reset the scroll position and start at the top of the scroll
container again. To do so, we're exposing a reference to the container element
of each panel that you can leverage to reset the scroll position when changing
the content.

```tsx
import { useEffect, useRef, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { Flex, Page, TitleBar } from '@dynatrace/strato-components/layouts';
import Borders from '@dynatrace/strato-design-tokens/borders';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';

const ScrollToTop = () => {
  const [togglePageContent, setTogglePageContent] = useState(false);
  const [toggleScroll, setToggleScroll] = useState(false);
  const mainRef = useRef<HTMLDivElement | null>(null);
  useEffect(() => {
    if (toggleScroll && mainRef.current) {
      mainRef.current.scrollTop = 0;
    }
  }, [toggleScroll, togglePageContent]);

  return (
    <Page>
      <Page.Header>
        <Flex>
          <Button
            onClick={() => {
              setTogglePageContent(!togglePageContent);
            }}
          >
            Toggle content
          </Button>
          <Button
            onClick={() => {
              setToggleScroll(!toggleScroll);
            }}
          >
            Toggle scroll behavior
          </Button>
        </Flex>
      </Page.Header>
      <Page.Main ref={mainRef}>
        <TitleBar>
          <TitleBar.Title>Main</TitleBar.Title>
          <TitleBar.Subtitle>
            Place your main content in this area
          </TitleBar.Subtitle>
        </TitleBar>
        <div
          style={{
            width: '100%',
            height: togglePageContent ? '3000px' : '1500px',
            marginTop: Spacings.Size24,
            borderRadius: Borders.Radius.Container.Default,
            background: `linear-gradient(${
              togglePageContent
                ? `${Colors.Background.Container.Neutral.Default}, ${Colors.Background.Container.Neutral.Emphasized}`
                : `${Colors.Background.Container.Success.Default}, ${Colors.Background.Container.Success.Emphasized}`
            })`,
          }}
        />
      </Page.Main>
    </Page>
  );
};
```

```tsx
import { useEffect, useRef, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { Flex, Page, TitleBar } from '@dynatrace/strato-components/layouts';
import Borders from '@dynatrace/strato-design-tokens/borders';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';

const ScrollToTop = () => {
  const [togglePageContent, setTogglePageContent] = useState(false);
  const [toggleScroll, setToggleScroll] = useState(false);
  const mainRef = useRef<HTMLDivElement | null>(null);
  useEffect(() => {
    if (toggleScroll && mainRef.current) {
      mainRef.current.scrollTop = 0;
    }
  }, [toggleScroll, togglePageContent]);

  return (
    <Page>
      <Page.Header>
        <Flex>
          <Button
            onClick={() => {
              setTogglePageContent(!togglePageContent);
            }}
          >
            Toggle content
          </Button>
          <Button
            onClick={() => {
              setToggleScroll(!toggleScroll);
            }}
          >
            Toggle scroll behavior
          </Button>
        </Flex>
      </Page.Header>
      <Page.Main ref={mainRef}>
        <TitleBar>
          <TitleBar.Title>Main</TitleBar.Title>
          <TitleBar.Subtitle>
            Place your main content in this area
          </TitleBar.Subtitle>
        </TitleBar>
        <div
          style={{
            width: '100%',
            height: togglePageContent ? '3000px' : '1500px',
            marginTop: Spacings.Size24,
            borderRadius: Borders.Radius.Container.Default,
            background: `linear-gradient(${
              togglePageContent
                ? `${Colors.Background.Container.Neutral.Default}, ${Colors.Background.Container.Neutral.Emphasized}`
                : `${Colors.Background.Container.Success.Default}, ${Colors.Background.Container.Success.Emphasized}`
            })`,
          }}
        />
      </Page.Main>
    </Page>
  );
};
```


#### Keep Sidebar / DetailView panel mounted

By default, when the `Page.Sidebar` or `Page.DetailView` content is not visible
to the user, it will also be removed from the DOM to prevent unwanted component
updates on hidden elements. If you want to keep the content in the DOM to
preserve the state, you can set the `keepMounted` prop on the component.

Known limitationThe `keepMounted` approach we are using currently doesn't work with e.g.
`react-router-dom` and `Outlet`s nested in the panels, because the rendered
react nodes end up in a different position in the react tree, losing the
original context. For now, if you need to keep more complex components mounted,
you have to implement it in your app.
CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Integrated controls
- Define responsive layouts
- Controlling panel state
- Set minimum panel width
- Save & restore panel sizes
- Using the page with react-router
- Scroll behavior
- Keep Sidebar / DetailView panel mounted

```tsx
<Page>
  <Page.Header>
    <AppHeader>
      <AppHeader.Navigation>
        <AppHeader.Logo appName="MyApp" />
      </AppHeader.Navigation>
    </AppHeader>
  </Page.Header>
  <Page.Sidebar keepMounted>
    <TitleBar>
      <TitleBar.Title>Sidebar</TitleBar.Title>
      <TitleBar.Subtitle>e.g. for navigation</TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton />
      </TitleBar.Action>
    </TitleBar>
  </Page.Sidebar>
  <Page.Main style={{ display: 'flex', flexDirection: 'column' }}>
    <TitleBar>
      <TitleBar.Prefix>
        <Page.PanelControlButton target="sidebar" />
      </TitleBar.Prefix>
      <TitleBar.Title>Main</TitleBar.Title>
      <TitleBar.Subtitle>
        Place your main content in this area
      </TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton />
      </TitleBar.Action>
    </TitleBar>
    <Placeholder />
  </Page.Main>
  <Page.DetailView style={{ display: 'flex', flexDirection: 'column' }}>
    <TitleBar>
      <TitleBar.Title>Settings</TitleBar.Title>
      <TitleBar.Subtitle>
        For content related to the main area
      </TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton />
      </TitleBar.Action>
    </TitleBar>
    <Placeholder />
  </Page.DetailView>
</Page>
```

```tsx
<Page>
  <Page.Header>
    <AppHeader>
      <AppHeader.Navigation>
        <AppHeader.Logo appName="MyApp" />
      </AppHeader.Navigation>
    </AppHeader>
  </Page.Header>
  <Page.Sidebar keepMounted>
    <TitleBar>
      <TitleBar.Title>Sidebar</TitleBar.Title>
      <TitleBar.Subtitle>e.g. for navigation</TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton />
      </TitleBar.Action>
    </TitleBar>
  </Page.Sidebar>
  <Page.Main style={{ display: 'flex', flexDirection: 'column' }}>
    <TitleBar>
      <TitleBar.Prefix>
        <Page.PanelControlButton target="sidebar" />
      </TitleBar.Prefix>
      <TitleBar.Title>Main</TitleBar.Title>
      <TitleBar.Subtitle>
        Place your main content in this area
      </TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton />
      </TitleBar.Action>
    </TitleBar>
    <Placeholder />
  </Page.Main>
  <Page.DetailView style={{ display: 'flex', flexDirection: 'column' }}>
    <TitleBar>
      <TitleBar.Title>Settings</TitleBar.Title>
      <TitleBar.Subtitle>
        For content related to the main area
      </TitleBar.Subtitle>
      <TitleBar.Action>
        <Page.PanelControlButton />
      </TitleBar.Action>
    </TitleBar>
    <Placeholder />
  </Page.DetailView>
</Page>
```


### Props

The `Page` component provides the basic layout for your app with slots for a
header, sidebar, main content, and a detail view. The `Main` slot is the only
slot that is mandatory for rendering the `Page`; every other slot is optional.

Check out the UI and design guidelines
for more information on how to structure your app using the page.

#### PageProps
extends`, , keyof >, , , , ` |
 | Name | Type | Default | Description
 | `disableAnimations?` | | `false` | Whether animations should be disabled.
If true or 'prefers-reduced-motion' is set to 'reduce', no animations are applied.

### Page.Header

The `Page.Header` is rendered at the very top of the page. Take a look at the
UI and design guidelines for information
on which components we recommend to use in the header.

#### HeaderProps
extends`, , keyof >, , `

### Page.Sidebar

The `Page.Sidebar` is the first slot of the page you can use to display content.
Take a look at the
UI and design guidelines for information
on which content we recommend to use in the sidebar.

#### SidebarProps

##### Signature:
`export declare type SidebarProps = | ;`

### Page.Main

You should use the `Page.Main` compound to display the main content of your
application. Take a look at the
UI and design guidelines for information
on which content we recommend to use in the main view.

#### MainProps
extends`, , , , keyof >` |
 | Name | Type | Default | Description
 | `minWidth?` | | `320` | The minimum width of the main panel in pixels.

### Page.DetailView

The `Page.DetailView` can be leveraged to provide additional information related
to the main content. Take a look at the
UI and design guidelines for information
on which content we recommend to use in the detail view.

#### DetailViewProps

##### Signature:
`export declare type DetailViewProps = | ;`

### Page.PanelControlButton

The `Page.PanelControlButton` updates the dismissed state of an uncontrolled
panel. The button automatically renders the correct icons depending on the panel
state.

#### PanelControlButtonProps
extends`, | | >` |
 | Name | Type | Default | Description
 | `action?` | | | | | The action triggered by the button.
 | `target?` | | | | The target panel controlled by the button.Still have questions?Find answers in the Dynatrace Community
- Page.Header
- Page.Sidebar
- Page.Main
- Page.DetailView
- Page.PanelControlButton

---

## PageLayout

`/design/components/layouts/PageLayout/`

The `PageLayout` component provides the basic layout for your app with slots for
a header, sidebar, main content, and a details panel.

Slot components (`Header`, `Sidebar`, `Content`, `Details`) can appear anywhere
in the React subtree - inside , , or any wrapper
component. They portal their children into stable DOM positions owned by
`PageLayout`.

Experimental`PageLayout` is still experimental. Be aware that the API is subject to change.
See
Strato versioning
for details.
Migration guide

### Import

`tsx
import { PageLayout } from '@dynatrace/strato-components/layouts';
`

### Defaults

All panels work without configuration. The defaults below are applied when you
do not set a prop explicitly.

 |
 | Slot | `minWidth` | `maxWidth` | `defaultWidth` | `defaultLayout` | `breakpoint`
 | `PageLayout.Sidebar` | `200` | `'50%'` | `'15%'` | n/a | `960`
 | `PageLayout.Details` | `320` | `'50%'` | `'25%'` | `'split'` | `600`

### Demo

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  AppHeader,
  Flex,
  HelpMenu,
  PageLayout,
} from '@dynatrace/strato-components/layouts';
import { Menu } from '@dynatrace/strato-components/navigation';
import { Heading } from '@dynatrace/strato-components/typography';
import Borders from '@dynatrace/strato-design-tokens/borders';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';
import { DotMenuIcon } from '@dynatrace/strato-icons';

const Placeholder = () => (
  <div
    style={{
      width: '100%',
      flex: 1,
      marginTop: Spacings.Size24,
      borderRadius: Borders.Radius.Container.Default,
      backgroundColor: Colors.Background.Container.Neutral.Default,
    }}
  />
);

const Basic = () => {
  const [isDetailsCollapsed, setIsDetailsCollapsed] = useState(false);

  return (
    <PageLayout style={{ height: '600px' }}>
      <PageLayout.Header>
        <AppHeader>
          <AppHeader.Navigation>
            <AppHeader.NavigationItem href="#">
              NavItem
            </AppHeader.NavigationItem>
            <AppHeader.NavigationItem href="#" isSelected>
              NavItem
            </AppHeader.NavigationItem>
          </AppHeader.Navigation>
          <AppHeader.Menus>
            <HelpMenu
              entries={{
                whatsNew: 'default',
                playground: 'default',
                about: 'default',
              }}
            />
          </AppHeader.Menus>
        </AppHeader>
      </PageLayout.Header>
      <PageLayout.Sidebar>
        <Flex flexDirection="column">
          <Heading level={3}>Sidebar</Heading>
          <Placeholder />
        </Flex>
      </PageLayout.Sidebar>
      <PageLayout.Content>
        <Flex flexDirection="column">
          <Heading level={2}>Content</Heading>
          <Button
            variant="emphasized"
            onClick={() => setIsDetailsCollapsed(false)}
          >
            Show Details
          </Button>
          <Placeholder />
        </Flex>
      </PageLayout.Content>
      <PageLayout.Details
        collapsed={isDetailsCollapsed}
        onCollapsedChange={setIsDetailsCollapsed}
      >
        <Flex flexDirection="column">
          <Flex alignItems="baseline" justifyContent="space-between">
            <Heading level={3}>Details</Heading>
            <PageLayout.Details.ControlBar>
              <Menu>
                <Menu.Trigger>
                  <Button aria-label="More actions">
                    <Button.Prefix>
                      <DotMenuIcon />
                    </Button.Prefix>
                  </Button>
                </Menu.Trigger>
                <Menu.Content>
                  <Menu.Item onSelect={() => undefined}>Edit</Menu.Item>
                  <Menu.Item onSelect={() => undefined}>Download</Menu.Item>
                  <Menu.Item onSelect={() => undefined}>Bookmark</Menu.Item>
                  <Menu.Item onSelect={() => undefined}>Share</Menu.Item>
                </Menu.Content>
              </Menu>
            </PageLayout.Details.ControlBar>
          </Flex>
          <Placeholder />
        </Flex>
      </PageLayout.Details>
    </PageLayout>
  );
};
```

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  AppHeader,
  Flex,
  HelpMenu,
  PageLayout,
} from '@dynatrace/strato-components/layouts';
import { Menu } from '@dynatrace/strato-components/navigation';
import { Heading } from '@dynatrace/strato-components/typography';
import Borders from '@dynatrace/strato-design-tokens/borders';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';
import { DotMenuIcon } from '@dynatrace/strato-icons';

const Placeholder = () => (
  <div
    style={{
      width: '100%',
      flex: 1,
      marginTop: Spacings.Size24,
      borderRadius: Borders.Radius.Container.Default,
      backgroundColor: Colors.Background.Container.Neutral.Default,
    }}
  />
);

const Basic = () => {
  const [isDetailsCollapsed, setIsDetailsCollapsed] = useState(false);

  return (
    <PageLayout style={{ height: '600px' }}>
      <PageLayout.Header>
        <AppHeader>
          <AppHeader.Navigation>
            <AppHeader.NavigationItem href="#">
              NavItem
            </AppHeader.NavigationItem>
            <AppHeader.NavigationItem href="#" isSelected>
              NavItem
            </AppHeader.NavigationItem>
          </AppHeader.Navigation>
          <AppHeader.Menus>
            <HelpMenu
              entries={{
                whatsNew: 'default',
                playground: 'default',
                about: 'default',
              }}
            />
          </AppHeader.Menus>
        </AppHeader>
      </PageLayout.Header>
      <PageLayout.Sidebar>
        <Flex flexDirection="column">
          <Heading level={3}>Sidebar</Heading>
          <Placeholder />
        </Flex>
      </PageLayout.Sidebar>
      <PageLayout.Content>
        <Flex flexDirection="column">
          <Heading level={2}>Content</Heading>
          <Button
            variant="emphasized"
            onClick={() => setIsDetailsCollapsed(false)}
          >
            Show Details
          </Button>
          <Placeholder />
        </Flex>
      </PageLayout.Content>
      <PageLayout.Details
        collapsed={isDetailsCollapsed}
        onCollapsedChange={setIsDetailsCollapsed}
      >
        <Flex flexDirection="column">
          <Flex alignItems="baseline" justifyContent="space-between">
            <Heading level={3}>Details</Heading>
            <PageLayout.Details.ControlBar>
              <Menu>
                <Menu.Trigger>
                  <Button aria-label="More actions">
                    <Button.Prefix>
                      <DotMenuIcon />
                    </Button.Prefix>
                  </Button>
                </Menu.Trigger>
                <Menu.Content>
                  <Menu.Item onSelect={() => undefined}>Edit</Menu.Item>
                  <Menu.Item onSelect={() => undefined}>Download</Menu.Item>
                  <Menu.Item onSelect={() => undefined}>Bookmark</Menu.Item>
                  <Menu.Item onSelect={() => undefined}>Share</Menu.Item>
                </Menu.Content>
              </Menu>
            </PageLayout.Details.ControlBar>
          </Flex>
          <Placeholder />
        </Flex>
      </PageLayout.Details>
    </PageLayout>
  );
};
```


### Responsive behavior

Below its configured `breakpoint`, a panel collapses into a `Drawer` to preserve
screen space.

#### Layout hierarchy

`PageLayout.Sidebar` and `PageLayout.Details` each have a `breakpoint` prop, but
they measure different widths:

- `PageLayout.Sidebar` - `breakpoint` is measured against the full
`PageLayout` container width.

- `PageLayout.Details` - `breakpoint` is measured against the combined width
of the `Content` + `Details` area, to the right of the sidebar.

This means the two breakpoints fire independently. When the sidebar is expanded,
it consumes page width and shrinks the content+details area. A details panel
with `breakpoint={600}` may collapse to a drawer even when the full page is
wider than 600 px.

The same rule applies to width props: `minWidth`, `maxWidth`, and `defaultWidth`
on `PageLayout.Details` are percentages of the content + details area, not the
full page.

### Preserve content state

Panel content is never unmounted. Component state, scroll positions, and form
input values survive collapse and expand cycles without any configuration. To
reset state on close, do so explicitly in `onCollapsedChange`, or conditionally
render the slot's children.

### Built-in controls

#### Sidebar

Collapse and expand controls are always present in `PageLayout.Sidebar` and
require no configuration. The collapse button appears on hover when the sidebar
is expanded. When collapsed, an expand button takes its place.

#### Details control bar

`PageLayout.Details.ControlBar` is optional. Place it at the top of the details
panel to give users a close button and, above the breakpoint, a layout-mode
toggle. See Control bar in Usage for
placement and customization guidance.

### Disable resizing

Set `resizable={false}` to lock a panel to its configured width and hide the
drag handle. Use this when the panel width is determined by its content rather
than user preference.

### Use with router

Slot components work correctly inside a router , a
boundary, or any other wrapper, including components that conditionally render
or lazy-load their children.

A common pattern is a top-level `PageLayout` with the header and sidebar defined
at the app layout level, and the `Content` and `Details` slots provided by
individual route components:

`tsx
// App layout - defines the persistent layout frameconst AppLayout = () => ( PageLayout> PageLayout.Header> AppHeader>{/* top-level navigation */}AppHeader> PageLayout.Header> PageLayout.Sidebar>{/* sub-navigation */}PageLayout.Sidebar> {/* Route components render their Content/Details slots here */} Outlet /> PageLayout>);// Route component - only provides the slots it ownsconst DashboardRoute = () => ( > PageLayout.Content> DashboardTable /> PageLayout.Content> PageLayout.Details> PageLayout.Details.ControlBar /> DetailsPanel /> PageLayout.Details> >);
`

When a route lazy-loads its content, wrap it in and render a
fallback inside `PageLayout.Content` to keep the layout stable while loading:

`tsx
const LazyDashboard = lazy(() => import('./DashboardRoute'));const AppLayout = () => ( PageLayout> PageLayout.Header>...PageLayout.Header> PageLayout.Sidebar>...PageLayout.Sidebar> Suspense fallback={ PageLayout.Content> ProgressCircle /> PageLayout.Content> } > Outlet /> Suspense> PageLayout>);
`
Still have questions?Find answers in the Dynatrace Community
- Import
- Defaults
- Demo
- Responsive behavior
- Layout hierarchy
- Preserve content state
- Built-in controls
- Sidebar
- Details control bar
- Disable resizing
- Use with router

```tsx
// App layout - defines the persistent layout frame
const AppLayout = () => (
  <PageLayout>
    <PageLayout.Header>
      <AppHeader>{/* top-level navigation */}</AppHeader>
    </PageLayout.Header>
    <PageLayout.Sidebar>{/* sub-navigation */}</PageLayout.Sidebar>
    {/* Route components render their Content/Details slots here */}
    <Outlet />
  </PageLayout>
);

// Route component - only provides the slots it owns
const DashboardRoute = () => (
  <>
    <PageLayout.Content>
      <DashboardTable />
    </PageLayout.Content>
    <PageLayout.Details>
      <PageLayout.Details.ControlBar />
      <DetailsPanel />
    </PageLayout.Details>
  </>
);
```

```tsx
// App layout - defines the persistent layout frame
const AppLayout = () => (
  <PageLayout>
    <PageLayout.Header>
      <AppHeader>{/* top-level navigation */}</AppHeader>
    </PageLayout.Header>
    <PageLayout.Sidebar>{/* sub-navigation */}</PageLayout.Sidebar>
    {/* Route components render their Content/Details slots here */}
    <Outlet />
  </PageLayout>
);

// Route component - only provides the slots it owns
const DashboardRoute = () => (
  <>
    <PageLayout.Content>
      <DashboardTable />
    </PageLayout.Content>
    <PageLayout.Details>
      <PageLayout.Details.ControlBar />
      <DetailsPanel />
    </PageLayout.Details>
  </>
);
```


### Props

The `PageLayout` component provides the basic layout for your app with slots for
a header, sidebar, main content, and a details panel.

Slot components (`Header`, `Sidebar`, `Content`, `Details`) can appear anywhere
in the React subtree - inside , , or any wrapper
component. They portal their children into stable DOM positions owned by
`PageLayout`.

Experimental`PageLayout` is still experimental. Be aware that the API is subject to change.
See
Strato versioning
for details.
Migration guide

Prop Table did not receive data

### PageLayout.Header

The `PageLayout.Header` is rendered at the very top of the layout. Use it to
place app-level navigation, titles, or actions that apply to the whole page.

#### PageLayoutHeaderProps
extends`, , , , , `

### PageLayout.Sidebar

The `PageLayout.Sidebar` is the optional left panel. It collapses to a drawer
when the container width drops below the `breakpoint`.

#### PageLayoutSidebarProps
extends`, `

### PageLayout.Content

`PageLayout.Content` is the required main content area. It accepts a `minWidth`
to prevent the content from shrinking below a certain value.

#### PageLayoutContentProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `minWidth?` | | | The minimum width of the content area. Accepts a pixel value or a percentage string.

### PageLayout.Details

The `PageLayout.Details` is the optional right panel. It supports two layout
modes (`split` and `overlay`) in addition to the responsive drawer mode.

#### PageLayoutDetailsProps
extends`, ` |
 | Name | Type | Default | Description
 | `layout?` | | | The current layout mode of the details panel (controlled).
 | `defaultLayout?` | | `'split'` | Default layout mode of the details panel (uncontrolled).
 | `onLayoutChange?` | (value: ) => | | Fired when the layout mode changes or should change.
 | `breakpoint?` | | `600` | Container width in pixels below which the details panel renders as an overlay instead of a split layout.

### PageLayout.Details.ControlBar

`PageLayout.Details.ControlBar` provides the default close and layout-mode
controls. Pass custom actions as children to extend it with panel-specific
buttons.

#### PageLayoutDetailsControlBarProps
extends`, , , , , `Still have questions?Find answers in the Dynatrace Community
- PageLayout.Header
- PageLayout.Sidebar
- PageLayout.Content
- PageLayout.Details
- PageLayout.Details.ControlBar

---

## Surface

`/design/components/layouts/Surface/`

The Surface component is used to structure content on a page.

### Import

`tsx
import { Surface } from '@dynatrace/strato-components/layouts';
`

### Use cases

The Surface component offers different visual styles depending on the elevation
level. By default, the elevation is set to `flat`.

#### Use the selection style

The selection style can be applied with different `color`s, which is set to
`neutral` by default. You should always consider the meaning behind the colors
when changing this. The `color` also defines the color of the focus style that
is applied when a Surface is interactive and is focused.

NoteThe selected border and the box-shadow grow outside of the component's size.
When it is inside a container that hides the overflow, it cuts off the border.
You will need to prevent this with padding or other CSS properties.

#### Make the Surface interactive

In some cases, the surface itself shall be interactive. Most of the time,
polymorphing it into a button or link should be the best way. One caveat is not
to nest other interactive elements inside an already interactive surface since
this leads to a11y implications.

However, the surface is not automatically considered interactive when a
`tabIndex` of 0 is set, in this case the focus styles are applied but no other
interactive styling.

#### Polymorph the Surface component

By default, the Surface component is rendered as a standard `div` element. For
layouting purposes, the component can be polymorphed to any other component.
This can be used, for example, to create a Flex layout inside a Surface
component. You can also polymorph the Surface into an interactive element, such
as a button or link if you want users to interact with the Surface.

#### Add layout styles to the Surface component

The Surface component has a default padding of 24px. This can be changed by
setting any padding prop on the container. Similarly, the container also accepts
any CSS margin and layout props, such as width or height.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Use the selection style
- Make the Surface interactive
- Polymorph the Surface component
- Add layout styles to the Surface component

### Props

The Surface component is used to structure content on a page.

#### SurfaceProps

##### Signature:
`export declare type SurfaceProps = ;`

#### SurfaceOwnProps
extends`, , , , , , , , ` |
 | Name | Type | Default | Description
 | `color?` | | | | | | `'neutral'` | Color of the border when the surface has focus or is selected.
 | `selected?` | | `false` | Defines if the surface is selected and should indicate that state with a border.
 | `dragged?` | | `false` | Indicates if the surface is currently dragged and then applies the corresponding styles.
 | `elevation?` | | | | `'flat'` | Defines the surface's elevation to the background.Still have questions?Find answers in the Dynatrace Community

---

## TitleBar

`/design/components/layouts/TitleBar/`

The TitleBar component can be used for a consistent layout for section titles
and provides layout slots for interactive and navigational elements.

OverviewProperties

### Import

`tsx
import { TitleBar } from '@dynatrace/strato-components/layouts';
`

### Use cases

The `TitleBar` component provides five different slots for layouting the
TitleBar content. We recommend using the Title slot for displaying a title. All
other slots are optional.

#### Use all TitleBar slots

We recommend using the following content for each of the `TitleBar` slots:

- Navigation: `Breadcrumbs`

- Title: String or `Heading`. If a string is provided the recommended styles are
applied automatically.

- Subtitle: String or `Text`. If a string is provided the recommended styles are
applied automatically.

- Prefix: Image, Icon or an Icon Button

- Suffix: One or multiple `Button`s

- Action: Icon Button, e.g. for a closing action

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Use all TitleBar slots

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import {
  Flex,
  Container,
  TitleBar,
} from '@dynatrace/strato-components/layouts';
import { Breadcrumbs } from '@dynatrace/strato-components/navigation';
import {
  FavoriteIcon,
  InformationIcon,
  RefreshIcon,
  UnfavoriteIcon,
  XmarkIcon,
} from '@dynatrace/strato-icons';

const Full = () => {
  return (
    <TitleBar>
      <TitleBar.Navigation>
        <Breadcrumbs>
          <Breadcrumbs.Item href="#">Home</Breadcrumbs.Item>
          <Breadcrumbs.Item href="#">Level 1</Breadcrumbs.Item>
          <Breadcrumbs.Item href="#">Level 2</Breadcrumbs.Item>
        </Breadcrumbs>
      </TitleBar.Navigation>
      <TitleBar.Action>
        <Button variant="default">
          <Button.Prefix>
            <XmarkIcon />
          </Button.Prefix>
        </Button>
      </TitleBar.Action>
      <TitleBar.Prefix>
        <Container as={Flex}>
          <InformationIcon />
        </Container>
      </TitleBar.Prefix>
      <TitleBar.Title>AppName</TitleBar.Title>
      <TitleBar.Subtitle>Some Subtitle</TitleBar.Subtitle>
      <TitleBar.Suffix>
        <Flex gap={4}>
          <Button variant="default">
            <Button.Prefix>
              <UnfavoriteIcon />
            </Button.Prefix>
            Action
          </Button>
          <Button variant="default">
            <Button.Prefix>
              <FavoriteIcon />
            </Button.Prefix>
            Action
          </Button>
          <Button variant="default">
            <Button.Prefix>
              <RefreshIcon />
            </Button.Prefix>
            Action
          </Button>
        </Flex>
      </TitleBar.Suffix>
    </TitleBar>
  );
};
```

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import {
  Flex,
  Container,
  TitleBar,
} from '@dynatrace/strato-components/layouts';
import { Breadcrumbs } from '@dynatrace/strato-components/navigation';
import {
  FavoriteIcon,
  InformationIcon,
  RefreshIcon,
  UnfavoriteIcon,
  XmarkIcon,
} from '@dynatrace/strato-icons';

const Full = () => {
  return (
    <TitleBar>
      <TitleBar.Navigation>
        <Breadcrumbs>
          <Breadcrumbs.Item href="#">Home</Breadcrumbs.Item>
          <Breadcrumbs.Item href="#">Level 1</Breadcrumbs.Item>
          <Breadcrumbs.Item href="#">Level 2</Breadcrumbs.Item>
        </Breadcrumbs>
      </TitleBar.Navigation>
      <TitleBar.Action>
        <Button variant="default">
          <Button.Prefix>
            <XmarkIcon />
          </Button.Prefix>
        </Button>
      </TitleBar.Action>
      <TitleBar.Prefix>
        <Container as={Flex}>
          <InformationIcon />
        </Container>
      </TitleBar.Prefix>
      <TitleBar.Title>AppName</TitleBar.Title>
      <TitleBar.Subtitle>Some Subtitle</TitleBar.Subtitle>
      <TitleBar.Suffix>
        <Flex gap={4}>
          <Button variant="default">
            <Button.Prefix>
              <UnfavoriteIcon />
            </Button.Prefix>
            Action
          </Button>
          <Button variant="default">
            <Button.Prefix>
              <FavoriteIcon />
            </Button.Prefix>
            Action
          </Button>
          <Button variant="default">
            <Button.Prefix>
              <RefreshIcon />
            </Button.Prefix>
            Action
          </Button>
        </Flex>
      </TitleBar.Suffix>
    </TitleBar>
  );
};
```


### Props

The TitleBar component can be used for a consistent layout for section titles
and provides layout slots for interactive and navigational elements.

OverviewProperties

#### TitleBarProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `showDivider?` | | `true` | Whether a divider is displayed after the TitleBar component.

### TitleBar.Navigation

#### TitleBarNavigationProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the TitleBar Navigation slot.

### TitleBar.Action

#### TitleBarActionProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the TitleBar Action slot.

### TitleBar.Prefix

#### TitleBarPrefixProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the TitleBar Prefix slot.

### TitleBar.Suffix

#### TitleBarSuffixProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the TitleBar Suffix slot.

### TitleBar.Subtitle

#### TitleBarSubtitleProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the TitleBar Subtitle slot.

### TitleBar.Title

#### TitleBarTitleProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the TitleBar Title slot.Still have questions?Find answers in the Dynatrace Community
- TitleBar.Navigation
- TitleBar.Action
- TitleBar.Prefix
- TitleBar.Suffix
- TitleBar.Subtitle
- TitleBar.Title

---

