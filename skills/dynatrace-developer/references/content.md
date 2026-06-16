# Content

Strato design-system components in the **Content** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## Accordion

`/design/components/content/Accordion/`

The `Accordion` component can be used to group information, reveal and hide
content.

### Import

`tsx
import { Accordion } from '@dynatrace/strato-components/content';
`

### Use cases

#### Add a section

You can add a section to the `Accordion` component by using the
`Accordion.Section`, `Accordion.SectionLabel` and `Accordion.SectionContent`
components. When adding a section a unique identifier has to be set using the
`id` prop. This allows to correctly expand and collapse the according sections.

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const MultipleSections = () => {
  return (
    <Accordion>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section2">
        <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section3">
        <Accordion.SectionLabel>Label 3</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const MultipleSections = () => {
  return (
    <Accordion>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section2">
        <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section3">
        <Accordion.SectionLabel>Label 3</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```


#### Interactive header

By default the whole header is interactive and can open and close the
`Accordion.Section`. If set to `false` only the `button` is interactive.

NoteKeep into consideration that, you shouldn't add interactive content to the
`Accordion.SectionLabel` when the entire header is interactive to avoid nesting
interactive elements.

```tsx
import { Accordion } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Interactive = () => (
  <Flex flexDirection="column">
    <Accordion>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Interactive Label</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
    <Accordion interactive={false}>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Interactive Button</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  </Flex>
);
//#endregion
```

```tsx
import { Accordion } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Interactive = () => (
  <Flex flexDirection="column">
    <Accordion>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Interactive Label</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
    <Accordion interactive={false}>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Interactive Button</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  </Flex>
);
//#endregion
```


#### Polymorph the Accordion.Section component

By default, the `Accordion.Section` component is rendered as a standard `div`
element. For layouting purposes, the component can be polymorphed to any other
component. This can be used, for example, to create a `Surface` layout inside an
Accordion component.

#### Change the position of the trigger

The position of the trigger in the `Accordion` is the same for every section. By
default the trigger is at the `end` of a section header. In order to change the
position to the beginning of a section header, you need to set the
`triggerPosition` prop to `start`.

#### Change the color

You can use the `color` prop to style the `Accordion` with a different color.
Setting the color affects the button, label, content, and divider color. If no
`color` is specified, it's set to `neutral`.

You can also use the `color` prop on the `Accordion.Section` to style one
section. If no `color` is specified, the color of the `Accordion` is used.

#### Show and hide dividers

You can use the `showDividers` prop to show or hide dividers. If no
`showDividers` If no `showDividers` is specified, it's set to `true`.

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const ShowDividers = () => (
  <Accordion showDividers={false}>
    <Accordion.Section id="section1">
      <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
      <Accordion.SectionContent>Some content</Accordion.SectionContent>
    </Accordion.Section>
    <Accordion.Section id="section2">
      <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
      <Accordion.SectionContent>Some content</Accordion.SectionContent>
    </Accordion.Section>
  </Accordion>
);
```

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const ShowDividers = () => (
  <Accordion showDividers={false}>
    <Accordion.Section id="section1">
      <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
      <Accordion.SectionContent>Some content</Accordion.SectionContent>
    </Accordion.Section>
    <Accordion.Section id="section2">
      <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
      <Accordion.SectionContent>Some content</Accordion.SectionContent>
    </Accordion.Section>
  </Accordion>
);
```


#### Change the size

You can use the `size` prop to set a smaller or bigger `Accordion` size. If no
`size` is specified, it's set to `default`.

#### Disable sections

In the `Accordion`, you can disable each section individually by adding the
`disabled` prop to the `Accordion.Section` component. With setting a section to
disabled, the `defaultExpanded` prop, which is optionally set on the `Accordion`
component, determines whether it is initially expanded or collapsed. The user
can no longer change the expanded state of the section.

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const DisabledSection = () => {
  return (
    <Accordion>
      <Accordion.Section id="section1" disabled>
        <Accordion.SectionLabel>Label</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const DisabledSection = () => {
  return (
    <Accordion>
      <Accordion.Section id="section1" disabled>
        <Accordion.SectionLabel>Label</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```


#### Expand multiple sections

Use the `multiple` prop to enable expanding multiple sections at the same time.

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const MultipleExpanded = () => {
  return (
    <Accordion multiple>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section2">
        <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section3">
        <Accordion.SectionLabel>Label 3</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const MultipleExpanded = () => {
  return (
    <Accordion multiple>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section2">
        <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section3">
        <Accordion.SectionLabel>Label 3</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```


#### Expand a single section by default

Use the `defaultExpanded` to specify the section that should be initially
expanded. The passed value should be a string or a number depending on the
specified section id.

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const DefaultSingleExpanded = () => {
  return (
    <Accordion defaultExpanded="section3">
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section2">
        <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section3">
        <Accordion.SectionLabel>Label 3</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const DefaultSingleExpanded = () => {
  return (
    <Accordion defaultExpanded="section3">
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section2">
        <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section3">
        <Accordion.SectionLabel>Label 3</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```


#### Expand multiple sections by default

Use the `defaultExpanded` to specify the sections that should be initially
expanded. The passed value should be an array of strings or numbers depending on
the specified section ids.

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const DefaultMultipleExpanded = () => {
  return (
    <Accordion defaultExpanded={['section1', 'section2']} multiple>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section2">
        <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section3">
        <Accordion.SectionLabel>Label 3</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```

```tsx
import { Accordion } from '@dynatrace/strato-components/content';

const DefaultMultipleExpanded = () => {
  return (
    <Accordion defaultExpanded={['section1', 'section2']} multiple>
      <Accordion.Section id="section1">
        <Accordion.SectionLabel>Label 1</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section2">
        <Accordion.SectionLabel>Label 2</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
      <Accordion.Section id="section3">
        <Accordion.SectionLabel>Label 3</Accordion.SectionLabel>
        <Accordion.SectionContent>Some content</Accordion.SectionContent>
      </Accordion.Section>
    </Accordion>
  );
};
```


#### Control the state

You can also handle the state of the `Accordion` component, making it
controlled. In order to do so, you need to set the `expanded` prop to assign the
state value. In addition, you need to use the `onExpandChange` prop to provide a
handler that is called when the state of the `Accordion` changes.

#### Keep SectionContent mounted

By default, when the `Accordion.Section` content is not visible to the user, it
will also be removed from the DOM to prevent unwanted component updates on
hidden elements. If you want to keep the `Accordion.Section`s content in the DOM
to preserve the state, you can set the `keepMounted` prop on the component.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Add a section
- Interactive header
- Polymorph the Accordion.Section component
- Change the position of the trigger
- Change the color
- Show and hide dividers
- Change the size
- Disable sections
- Expand multiple sections
- Expand a single section by default
- Expand multiple sections by default
- Control the state
- Keep SectionContent mounted

### Props

The `Accordion` component can be used to group information, reveal and hide
content.

#### AccordionProps

##### Signature:
`export declare type AccordionProps = <> & (<> | <>);`

#### AccordionOwnProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `multiple?` | | `false` | Determines whether multiple sections can be open at the same time.
 | `triggerPosition?` | | | `'end'` | The position of the trigger that expands and collapses a section.
 | `onExpandChange?` | (value: <>) => | | Callback fired when a section is expanded/collapsed.
 | `interactive?` | | `true` | If the accordion is interactive, the whole header is interactive and can open or close the accordion.
Otherwise, only the button is interactive
 | `color?` | | | | | | `'neutral'` | The color of the accordion.
Setting the color affects the button, label, content and divider color.
 | `size?` | | | `'default'` | The size of the accordion.
 | `showDividers?` | | `true` | Whether a divider is shown between the sections.

#### AccordionControlledProps
 |
 | Name | Type | Default | Description
 | `expanded` | extends true ? : | | Determines which sections are expanded in a controlled scenario.

#### AccordionUncontrolledProps
 |
 | Name | Type | Default | Description
 | `defaultExpanded?` | extends true ? : | `false` | Determines which sections are initially expanded in an uncontrolled scenario.

### Accordion.Section

#### AccordionSectionProps

##### Signature:
`export declare type AccordionSectionProps = , > & ;`Still have questions?Find answers in the Dynatrace Community
- Accordion.Section

---

## AiLoadingIndicator

`/design/components/content/AiLoadingIndicator/`

Use the `AiLoadingIndicator` component to indicate that AI-generated content is
being loaded.

OverviewProperties

### Import

`tsx
import { AiLoadingIndicator } from '@dynatrace/strato-components/content';
`

### Use cases

It's recommended to include the `AiLoadingIndicator.Icon` slot to show the
default icon, which helps users identify AI-generated content.

#### Customize icon

By providing a custom icon in the `AiLoadingIndicator.Icon` slot, you can
override the default icon.

```tsx
import { AiLoadingIndicator } from '@dynatrace/strato-components/content';
import { EducationIcon } from '@dynatrace/strato-icons';

const CustomIcon = () => {
  return (
    <AiLoadingIndicator>
      <AiLoadingIndicator.Icon>
        <EducationIcon />
      </AiLoadingIndicator.Icon>
      Checking sources…
    </AiLoadingIndicator>
  );
};
```


#### Hide icon

You can hide the icon by not including the `AiLoadingIndicator.Icon` slot.

```tsx
import { AiLoadingIndicator } from '@dynatrace/strato-components/content';

const HiddenIcon = () => {
  return <AiLoadingIndicator>Verifying DQL…</AiLoadingIndicator>;
};
```


### Accessibility

The `AiLoadingIndicator` component includes `role="progressbar"` to indicate an
indeterminate loading state to assistive technologies. The icon is marked as
decorative with `aria-hidden="true"`.

For optimal accessibility, wrap the component in a container with
`role="status"` and `aria-live="polite"` to announce loading state changes to
screen readers:

`tsx
div role="status" aria-live="polite"> {isLoading && AiLoadingIndicator>Thinking…AiLoadingIndicator>}div>
`
Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Customize icon
- Hide icon
- Accessibility

```tsx
<div role="status" aria-live="polite">
  {isLoading && <AiLoadingIndicator>Thinking…</AiLoadingIndicator>}
</div>
```


### Props

Use the `AiLoadingIndicator` component to indicate that AI-generated content is
being loaded.

OverviewProperties

#### AiLoadingIndicatorProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `'aria-disabled'?` | [] | | Whether the element and all focusable descendants are disabled.
`aria-disabled="true"` only semantically exposes these elements as being disabled.
 | `children` | | | The label shown in the indicator.
 | `'aria-valuetext'?` | | | The `aria-valuetext` attribute provides a human-readable text alternative for assistive technologies about the loading progress.

### AiLoadingIndicator.Icon

The `AiLoadingIndicator.Icon` slot is used to specify an icon displayed in the
`AiLoadingIndicator`. Defaults to the `AiIcon` if no children are provided.

#### AiLoadingIndicatorIconProps
extends`, , `Still have questions?Find answers in the Dynatrace Community
- AiLoadingIndicator.Icon

---

## AiResponse

`/design/components/content/AiResponse/`

Use the `AiResponse` component to animate AI-generated content.

OverviewProperties

### Import

`tsx
import { AiResponse } from '@dynatrace/strato-components/content';
`

### Use cases

#### Response state

The `responseState` prop controls how the component renders and animates
content:

- `streaming` (default): Use while the AI response is actively being generated.
The component animates each new word as it arrives, giving users a live typing
effect.

- `complete`: Set this once streaming has finished and the full response text
has been passed. The component finishes animating any remaining words that
have not yet been displayed.

- `static`: Use when the full response is available upfront and no animation is
needed. The content is rendered immediately without any animation.

#### Animation state

The `onAnimationStateChange` callback lets you react to the word-by-word
animation. It is called with `true` when the animation starts and with `false`
once the last word of the current content has fully faded in.Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Response state
- Animation state

### Props

Use the `AiResponse` component to animate AI-generated content.

OverviewProperties

#### AiResponseProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `children` | | | The content to be displayed as markdown.
 | `onAnimationStateChange?` | (isAnimating: ) => | | Callback that is called whenever the animation state changes.
 | `responseState?` | | | | `'streaming'` | Controls how the content is rendered and animated.

- `'static'`: Renders the entire response immediately with no animation.

- `'streaming'`: Animates content as it streams in.

- `'complete'`: Indicates streaming has finished and the full content has been passed. The component will finish animating any remaining content and turn off animation.
Still have questions?Find answers in the Dynatrace Community

---

## Avatar

`/design/components/content/Avatar/`

The `Avatar` component can be used as a visual representation of a user.

### Import

`tsx
import { Avatar } from '@dynatrace/strato-components/content';
`

### Use cases

The `Avatar` is a visual representation of a user.

#### Add a label and subtitle

You can add a label and a subtitle to the `Avatar` component by using the
`Avatar.Label` and `Avatar.Subtitle` components.

#### Creating a display label

The Avatar requires an `abbreviation`, which usually are the initials of the
displayed user. When generating this value you should consider that some users
could have more than one firstname or lastname and there could also be team
users that have different naming conventions. In the code sample below, an easy
way to generate the initials from a name is shown. In the future, the
`abbreviation` could be also created by the Avatar component itself or provided
by a user API.

#### Change the size of the Avatar

By default, the size of the `Avatar` is set to `default` and shows two letters
in the `displayValue`. If you need a smaller `Avatar` component you can set the
`size` prop to `small`. Small `Avatar`s only show one letter in the
`displayValue`.

#### Add a tooltip

You can wrap the `Avatar` component in a `Tooltip` component. To make it
accessible for keyboard users you need to add a `tabIndex`. For the alignment of
the tooltip it is necessary that the Avatar is not wrapped in an element that is
larger than the Avatar itself or that additional styles are set on the Avatar to
control the width.

#### Make the Avatar clickable

You can use the `small` size of the `Avatar` inside the `Button.Prefix` slot of
the `Button` component to make it clickable. Additional text can be displayed in
the `Button.Label` slot. If you can't use a wrapping interactive element you can
also polymorph the `Avatar` component itself into an interactive element, such
as a link. Keep in mind that nested interactive elements, such as buttons inside
buttons, are not valid HTML and can cause issues with accessibility. Ensure that
the component is not polymorphed into an interactive element or has a tabIndex
set if you use an interactive wrapper element.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Add a label and subtitle
- Creating a display label
- Change the size of the Avatar
- Add a tooltip
- Make the Avatar clickable

### Props

The `Avatar` component can be used as a visual representation of a user.

#### AvatarProps

##### Signature:
`export declare type AvatarProps = ;`

### Avatar.Label

You can use the `Avatar.Label` component to render the whole text describing the
`Avatar`, as shown above.

#### AvatarLabelProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the Avatar Label slot.

### Avatar.Subtitle

You can use the `Avatar.Subtitle` component to render extra information below
the `Avatar`'s label, as shown above.

#### AvatarSubtitleProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the Avatar Subtitle slot.Still have questions?Find answers in the Dynatrace Community
- Avatar.Label
- Avatar.Subtitle

---

## AvatarGroup

`/design/components/content/AvatarGroup/`

The `Avatar` component can be used as a visual representation of multiple users.

OverviewProperties

### Import

`tsx
import { AvatarGroup } from '@dynatrace/strato-components/content';
`

### Use cases

The `AvatarGroup` is a wrapper that stacks multiple
`Avatar`s together.

#### Add multiple items

The `AvatarGroup` can display a maximum of 5 `AvatarItem`s. If it contains more
than that, the remaining items are collapsed into a menu. The trigger icon shows
the number of menu items.

```tsx
import { AvatarGroup } from '@dynatrace/strato-components/content';

const MultipleItems = () => {
  const USERS = [
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
  ];

  return (
    <AvatarGroup>
      {USERS.map((user, key) => (
        <AvatarGroup.Item
          abbreviation={user.abbreviation}
          tooltipText="Firstname Lastname"
          key={key}
        />
      ))}
    </AvatarGroup>
  );
};
```

```tsx
import { AvatarGroup } from '@dynatrace/strato-components/content';

const MultipleItems = () => {
  const USERS = [
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
    {
      abbreviation: 'FL',
      label: 'Firstname Lastname',
      subtitle: 'firstname.lastname@dynatrace.com',
    },
  ];

  return (
    <AvatarGroup>
      {USERS.map((user, key) => (
        <AvatarGroup.Item
          abbreviation={user.abbreviation}
          tooltipText="Firstname Lastname"
          key={key}
        />
      ))}
    </AvatarGroup>
  );
};
```


#### Polymorph items into links

The `AvatarGroup.Item` is polymorphic, so you can, for example, polymorph it to
an anchor.

```tsx
import { type MouseEvent as ReactMouseEvent } from 'react';

import { AvatarGroup } from '@dynatrace/strato-components/content';

const Polymorph = () => {
  return (
    <AvatarGroup>
      <AvatarGroup.Item
        abbreviation="AE"
        tooltipText="Albert Einstein"
        href="#"
        as="a"
        onClick={(event: ReactMouseEvent) => {
          event.preventDefault();
        }}
      />
      <AvatarGroup.Item
        abbreviation="JK"
        tooltipText="Johannes Kepler"
        href="#"
        as="a"
        onClick={(event: ReactMouseEvent) => {
          event.preventDefault();
        }}
      />
      <AvatarGroup.Item
        abbreviation="FN"
        tooltipText="Friedrich Nietzsche"
        href="#"
        as="a"
        onClick={(event: ReactMouseEvent) => {
          event.preventDefault();
        }}
      />
    </AvatarGroup>
  );
};
```

```tsx
import { type MouseEvent as ReactMouseEvent } from 'react';

import { AvatarGroup } from '@dynatrace/strato-components/content';

const Polymorph = () => {
  return (
    <AvatarGroup>
      <AvatarGroup.Item
        abbreviation="AE"
        tooltipText="Albert Einstein"
        href="#"
        as="a"
        onClick={(event: ReactMouseEvent) => {
          event.preventDefault();
        }}
      />
      <AvatarGroup.Item
        abbreviation="JK"
        tooltipText="Johannes Kepler"
        href="#"
        as="a"
        onClick={(event: ReactMouseEvent) => {
          event.preventDefault();
        }}
      />
      <AvatarGroup.Item
        abbreviation="FN"
        tooltipText="Friedrich Nietzsche"
        href="#"
        as="a"
        onClick={(event: ReactMouseEvent) => {
          event.preventDefault();
        }}
      />
    </AvatarGroup>
  );
};
```


#### Accessibility

You can navigate between `AvatarGroup.Item`s, as well as the menu trigger, with
the left and right arrow keys. A roving focus index is used, so the focus moves
when you use the arrow keys. This means you can tab outside the `AvatarGroup`,
and if you tab back inside the group, the focus is set on the item you
previously navigated to.Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Add multiple items
- Polymorph items into links
- Accessibility

### Props

The `Avatar` component can be used as a visual representation of multiple users.

OverviewProperties

#### AvatarGroupProps

##### Signature:
`export declare type AvatarGroupProps = & & & & & ;`

### AvatarGroup.Item

You can use the `AvatarGroup.Item` component to render an item belonging to the
group of `Avatar`s, as shown above.

#### AvatarGroupItemProps

##### Signature:
`export declare type AvatarGroupItemProps = ;`Still have questions?Find answers in the Dynatrace Community
- AvatarGroup.Item

---

## Chip

`/design/components/content/Chip/`

Use the `Chip` component to present a piece of information in a compact form.

### Import

`tsx
import { Chip } from '@dynatrace/strato-components/content';
`

### Use cases

#### Remove a Chip

You can add a `DeleteButton` to the `Chip` to allow removing it. This comes with
a default 'Delete Chip' translation used for the `aria-label`. If necessary, you
can also override it with a different translation by setting the `aria-label`.

#### Display key-value pairs

The `Chip` can also display key-value pairs. The key is shown before the value
and separated with a `:`.

```tsx
import { Chip } from '@dynatrace/strato-components/content';

const WithKey = () => {
  return (
    <Chip>
      <Chip.Key>App</Chip.Key>
      Product Analytics
    </Chip>
  );
};
```

```tsx
import { Chip } from '@dynatrace/strato-components/content';

const WithKey = () => {
  return (
    <Chip>
      <Chip.Key>App</Chip.Key>
      Product Analytics
    </Chip>
  );
};
```


#### Add a prefix or suffix slot

You can render icons at the beginning and the end of the `Chip` by using the
`Chip.Prefix` and `Chip.Suffix` slots.

#### Change the color

You can use the `color` prop to style the `Chip` with a different color. If no
`color` is specified, it's set to `neutral`.

#### Change the variant

You can use the `variant` prop to create the different variants. If no `variant`
is specified, it's set to `emphasized`.

#### Change the size

You can use the `size` prop to set a smaller or bigger `Chip` size. If no `size`
is specified, it's set to `default`.

#### Change the maximum width

The `Chip` is as wide as its content by default and has a default maximum width
of 250px. You can change that by setting the `maxWidth` prop to a different
value.

#### Disable the Chip

You can use the `disabled` prop to disable the `Chip`. If it's disabled, the
user can no longer interact with it and it has no interactive styles. If no
`disabled` prop is specified, it's set to `false`.

#### Polymorph the Chip

The `Chip` can be polymorphed to a different component, which could be
interactive. So the whole content added inside the Chip other than the
`Chip.DeleteButton` is then polymorphed to the specified component. The
`DeleteButton` is excluded because it's already a button, so if you polymorph
the entire Chip content to a button for example, this would nest interactive
components.

This is also the reason why you shouldn't add an interactive component to the
`Chip.Key` when the entire Chip is interactive. The same applies to the Chip
value, so in case you add an interactive component inside the Chip, you would be
nesting interactive elements.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Remove a Chip
- Display key-value pairs
- Add a prefix or suffix slot
- Change the color
- Change the variant
- Change the size
- Change the maximum width
- Disable the Chip
- Polymorph the Chip

### Props

Use the `Chip` component to present a piece of information in a compact form.

#### ChipProps

##### Signature:
`export declare type ChipProps = ;`

#### ChipOwnProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `color?` | | | | | | `'neutral'` | The color of the component. This should be chosen based on the context
it's used in.
 | `variant?` | | | `'emphasized'` | Variant defining the visual representation of the component.
 | `disabled?` | | `false` | Whether the component is disabled. If true, it cannot be interacted with.
 | `size?` | | | `'default'` | The size of the component.

### Chip.Prefix, Chip.Suffix

#### ChipContentProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the prefix or suffix slot.

### Chip.Key

#### ChipKeyProps

##### Signature:
`export declare type ChipKeyProps = & & ;`

### Chip.DeleteButton

#### ChipDeleteButtonProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `disabled?` | | `false` | If a button is disabled e.g. it cannot be interacted with.
By default, it inherits the disabled prop of the Chip, but can be overwritten.
 | `onClick?` | | | Called when the button is interacted with.Still have questions?Find answers in the Dynatrace Community
- Chip.Prefix, Chip.Suffix
- Chip.Key
- Chip.DeleteButton

---

## ChipGroup

`/design/components/content/ChipGroup/`

Use the `ChipGroup` component to group multiple `Chip`s in an expandable
container.

### Import

`tsx
import { ChipGroup } from '@dynatrace/strato-components/content';
`

### Use cases

#### Show ChipGroup control

You can display a control label at the end of the `ChipGroup`. This label can be
used to expand or collapse the group as needed. To achieve this, add a
`ChipGroup.Control` subcomponent. If the `count` property is set to `true`, the
label displays the number of hidden chips. Note that the control label is shown
only when the available chips do not fit on one line.

```tsx
import { Chip, ChipGroup } from '@dynatrace/strato-components/content';

const names = [
  'Patty O’Furniture',
  'Chris Cross',
  'Allie Gater',
  'Paige Turner',
  'Ferris Wheeler',
  'Al Dente',
  'Sonny Day',
  'Sarah Bellum',
  'Rocky Rhoades',
  'Sal A. Mander',
  'Sheila Blige',
  'Tom A. Toe',
  'Sno White',
  'Wanna Hickey',
  'Willie Waite',
  'Stan Still',
];

const HiddenCounter = () => {
  return (
    <ChipGroup>
      {names.map((name, index) => (
        <Chip key={`key${index}`}>{name}</Chip>
      ))}
      <ChipGroup.Control count />
    </ChipGroup>
  );
};
```

```tsx
import { Chip, ChipGroup } from '@dynatrace/strato-components/content';

const names = [
  'Patty O’Furniture',
  'Chris Cross',
  'Allie Gater',
  'Paige Turner',
  'Ferris Wheeler',
  'Al Dente',
  'Sonny Day',
  'Sarah Bellum',
  'Rocky Rhoades',
  'Sal A. Mander',
  'Sheila Blige',
  'Tom A. Toe',
  'Sno White',
  'Wanna Hickey',
  'Willie Waite',
  'Stan Still',
];

const HiddenCounter = () => {
  return (
    <ChipGroup>
      {names.map((name, index) => (
        <Chip key={`key${index}`}>{name}</Chip>
      ))}
      <ChipGroup.Control count />
    </ChipGroup>
  );
};
```


#### Show custom Chip counter

You can customize the counter within the control label by passing a number to
the `ChipGroup.Controlcount` property. This is useful when the remaining
chips are loaded asynchronously and the total number of chips is already known.
For more advanced use-cases, the `useChipGroupContext` hook provides you with
the amount of `Chip`s currently displayed or hidden.

```tsx
import {
  Chip,
  ChipGroup,
  useChipGroupContext,
} from '@dynatrace/strato-components/content';

const names = [
  'Patty O’Furniture',
  'Chris Cross',
  'Allie Gater',
  'Paige Turner',
  'Ferris Wheeler',
  'Al Dente',
  'Sonny Day',
  'Sarah Bellum',
  'Rocky Rhoades',
  'Sal A. Mander',
  'Sheila Blige',
  'Tom A. Toe',
  'Sno White',
  'Wanna Hickey',
  'Willie Waite',
  'Stan Still',
];
const NR_OF_CHIPS_IN_DB = 42;
const CustomControl = () => {
  const { visibleKeys } = useChipGroupContext();
  return <ChipGroup.Control count={NR_OF_CHIPS_IN_DB - visibleKeys.length} />;
};

const CustomCounter = () => {
  return (
    <ChipGroup>
      {names.map((name, index) => (
        <Chip key={`key${index}`}>{name}</Chip>
      ))}
      <CustomControl />
    </ChipGroup>
  );
};
```

```tsx
import {
  Chip,
  ChipGroup,
  useChipGroupContext,
} from '@dynatrace/strato-components/content';

const names = [
  'Patty O’Furniture',
  'Chris Cross',
  'Allie Gater',
  'Paige Turner',
  'Ferris Wheeler',
  'Al Dente',
  'Sonny Day',
  'Sarah Bellum',
  'Rocky Rhoades',
  'Sal A. Mander',
  'Sheila Blige',
  'Tom A. Toe',
  'Sno White',
  'Wanna Hickey',
  'Willie Waite',
  'Stan Still',
];
const NR_OF_CHIPS_IN_DB = 42;
const CustomControl = () => {
  const { visibleKeys } = useChipGroupContext();
  return <ChipGroup.Control count={NR_OF_CHIPS_IN_DB - visibleKeys.length} />;
};

const CustomCounter = () => {
  return (
    <ChipGroup>
      {names.map((name, index) => (
        <Chip key={`key${index}`}>{name}</Chip>
      ))}
      <CustomControl />
    </ChipGroup>
  );
};
```


#### Custom control label

Configure the content of the control label by passing a child component to the
`ChipGroup.Control`. Additionally, `ChipGroup.HiddenCount` provides the number
of `Chip`s not currently visible.

```tsx
import { useState } from 'react';

import { Chip, ChipGroup } from '@dynatrace/strato-components/content';

const names = [
  'Patty O’Furniture',
  'Chris Cross',
  'Allie Gater',
  'Paige Turner',
  'Ferris Wheeler',
  'Al Dente',
  'Sonny Day',
  'Sarah Bellum',
  'Rocky Rhoades',
  'Sal A. Mander',
  'Sheila Blige',
  'Tom A. Toe',
  'Sno White',
  'Wanna Hickey',
  'Willie Waite',
  'Stan Still',
];

const CustomMoreLabel = () => {
  const [expanded, setExpanded] = useState(false);

  return (
    <ChipGroup expanded={expanded} onExpandedChange={setExpanded}>
      {names.map((name, index) => (
        <Chip key={`key${index}`}>{name}</Chip>
      ))}
      <ChipGroup.Control>
        {expanded ? (
          <>Give me less</>
        ) : (
          <>
            Give me <ChipGroup.HiddenCount /> more
          </>
        )}
      </ChipGroup.Control>
    </ChipGroup>
  );
};
```

```tsx
import { useState } from 'react';

import { Chip, ChipGroup } from '@dynatrace/strato-components/content';

const names = [
  'Patty O’Furniture',
  'Chris Cross',
  'Allie Gater',
  'Paige Turner',
  'Ferris Wheeler',
  'Al Dente',
  'Sonny Day',
  'Sarah Bellum',
  'Rocky Rhoades',
  'Sal A. Mander',
  'Sheila Blige',
  'Tom A. Toe',
  'Sno White',
  'Wanna Hickey',
  'Willie Waite',
  'Stan Still',
];

const CustomMoreLabel = () => {
  const [expanded, setExpanded] = useState(false);

  return (
    <ChipGroup expanded={expanded} onExpandedChange={setExpanded}>
      {names.map((name, index) => (
        <Chip key={`key${index}`}>{name}</Chip>
      ))}
      <ChipGroup.Control>
        {expanded ? (
          <>Give me less</>
        ) : (
          <>
            Give me <ChipGroup.HiddenCount /> more
          </>
        )}
      </ChipGroup.Control>
    </ChipGroup>
  );
};
```


#### Limit visible Chips when collapsed

Set the `maxVisibleChips` property to limit the number of visible chips when the
`ChipGroup` is collapsed, regardless of available space. This is useful when you
want to maintain a consistent initial view with a specific number of chips, even
if more would fit in the container.

```tsx
import { Chip, ChipGroup } from '@dynatrace/strato-components/content';

const names = [
  "Patty O'Furniture",
  'Chris Cross',
  'Allie Gater',
  'Paige Turner',
  'Ferris Wheeler',
  'Al Dente',
  'Sonny Day',
  'Sarah Bellum',
  'Rocky Rhoades',
  'Sal A. Mander',
];

const MaxVisibleChips = () => {
  return (
    <ChipGroup maxVisibleChips={3}>
      {names.map((name, index) => (
        <Chip key={`key${index}`}>{name}</Chip>
      ))}
      <ChipGroup.Control />
    </ChipGroup>
  );
};
```

```tsx
import { Chip, ChipGroup } from '@dynatrace/strato-components/content';

const names = [
  "Patty O'Furniture",
  'Chris Cross',
  'Allie Gater',
  'Paige Turner',
  'Ferris Wheeler',
  'Al Dente',
  'Sonny Day',
  'Sarah Bellum',
  'Rocky Rhoades',
  'Sal A. Mander',
];

const MaxVisibleChips = () => {
  return (
    <ChipGroup maxVisibleChips={3}>
      {names.map((name, index) => (
        <Chip key={`key${index}`}>{name}</Chip>
      ))}
      <ChipGroup.Control />
    </ChipGroup>
  );
};
```


#### Remove Chips in ChipGroup

Combine the `Chip.DeleteButton` subcomponent
to remove specific `Chip`s by clicking on the delete button. Provide an
`onClick` handler to remove the selected chip from the rendered collection.

#### Control the ChipGroup

You can use the `expanded` state of the `ChipGroup` component in a controlled
manner. Set the `expanded` prop to the state value and the `onExpandedChange`
prop to the state update callback.

#### Disable the ChipGroup

Disable the entire `ChipGroup` by setting the `disabled` property to `true`.
This prevents interactions with the `Chip`s while still allowing the group to be
expanded or collapsed.

#### Async loading Chips into the ChipGroup

Implement advanced use cases like asynchronous loading of chips on expand by
providing an `onClick` callback to the `ChipGroup.Control`. Set the `loading`
property of `ChipGroup.Control` to `true` to show a visual loading indicator
while data is being fetched.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Show ChipGroup control
- Show custom Chip counter
- Custom control label
- Limit visible Chips when collapsed
- Remove Chips in ChipGroup
- Control the ChipGroup
- Disable the ChipGroup
- Async loading Chips into the ChipGroup

### Props

Use the `ChipGroup` component to group multiple `Chip`s in an expandable
container.

#### ChipGroupProps

##### Signature:
`export declare type ChipGroupProps = & ( | ) & ;`

#### ChipGroupBaseProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `disabled?` | | `false` | Whether the chip group is disabled.
If set to true, all the chips inside the group are disabled, unless explicitly overridden.
 | `size?` | [] | `default` | The size of the spacing and chips in the group.
All the chips match the size of the group, but can be overridden individually.
 | `onExpandedChange?` | (state: ) => | | Callback triggered when the expanded state changes.
 | `maxVisibleChips?` | | | `'auto'` | Maximum number of chips rendered before the "Show more" control.

If set to 'auto', the chip group automatically determines
how many chips can fit based on the available width.
If a number is provided, it limits the visible chips to that number
when the group is collapsed, regardless of available space.

#### ChipGroupControlledProps
 |
 | Name | Type | Default | Description
 | `expanded?` | | | Whether the chip group is expanded.

#### ChipGroupUncontrolledProps
 |
 | Name | Type | Default | Description
 | `defaultExpanded?` | | | Whether the chip group is expanded by default.

### ChipGroup.Control

#### ChipGroupControlProps
extends`, , ` |
 | Name | Type | Default | Description
 | `display?` | | | `inferred from the`expanded`/`defaultExpanded`prop of the`ChipGroup | Whether to show more chips or collapse chips.
If undefined, the action is inferred.
If no more items are available and all items fit in one line,
the control is automatically hidden unless display is set.
 | `count?` | | | `undefined` | Whether to render `Show more` or `Show x more` by default.
If true, the count is calculated automatically. The count can be overridden
by passing a number.
 | `loading?` | | `false` | Whether the control should show the loading indicator.
 | `onClick?` | <> | | Callback triggered when the control is interacted with.Still have questions?Find answers in the Dynatrace Community
- ChipGroup.Control

---

## CodeSnippet

`/design/components/content/CodeSnippet/`

Use the `CodeSnippet` to display a code block in a read-only context. By
default, the code is formatted but not highlighted.

OverviewProperties

### Import

`tsx
import { CodeSnippet } from '@dynatrace/strato-components/content';
`

### Use cases

#### Change the language

The `CodeSnippet` component offers syntax highlighting for different languages.
To change the language, set the `language` property.

#### Hide line numbers

To disable the line numbers, you can use the boolean prop `showLineNumbers`.

```tsx
import { CodeSnippet } from '@dynatrace/strato-components/content';

const LineNumbers = () => {
  return (
    <CodeSnippet language="typescript" showLineNumbers={false}>
      {`const example = function(name: string) {
  console.log("Hello " + name);
}`}
    </CodeSnippet>
  );
};
```

```tsx
import { CodeSnippet } from '@dynatrace/strato-components/content';

const LineNumbers = () => {
  return (
    <CodeSnippet language="typescript" showLineNumbers={false}>
      {`const example = function(name: string) {
  console.log("Hello " + name);
}`}
    </CodeSnippet>
  );
};
```


#### Limit the snippet height

Use the prop `maxHeight` to enable scrolling for long code blocks. The maximum
height is given in pixels.

#### React to copying

The `onCopy` callback allows you to react to the user copying the code snippet
using the copy button.

```tsx
import { useState } from 'react';

import { CodeSnippet } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const OnCopy = () => {
  const [copyCounter, setCopyCounter] = useState(0);

  return (
    <Flex flexDirection="column" gap={12}>
      <CodeSnippet
        language="typescript"
        onCopy={() => setCopyCounter(copyCounter + 1)}
      >
        {`const example = function(name: string) {
  console.log("Hello " + name);
}`}
      </CodeSnippet>
      Copied {copyCounter} times.
    </Flex>
  );
};
```

```tsx
import { useState } from 'react';

import { CodeSnippet } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const OnCopy = () => {
  const [copyCounter, setCopyCounter] = useState(0);

  return (
    <Flex flexDirection="column" gap={12}>
      <CodeSnippet
        language="typescript"
        onCopy={() => setCopyCounter(copyCounter + 1)}
      >
        {`const example = function(name: string) {
  console.log("Hello " + name);
}`}
      </CodeSnippet>
      Copied {copyCounter} times.
    </Flex>
  );
};
```


#### Wrap long lines

Set the `lineBreaks` prop to automatically wrap lines that exceed the available
width. This is especially useful for log output or other content with long
lines.

```tsx
import { CodeSnippet } from '@dynatrace/strato-components/content';

const LineWrap = () => {
  return (
    <CodeSnippet language="log" lineBreaks>
      {`2025-03-19T12:00:00.000Z - INFO  - Application started successfully on port 8080 with configuration: {"database":"postgres://localhost:5432/mydb","cache":"redis://localhost:6379","logLevel":"info","maxConnections":100}
2025-03-19T12:00:01.000Z - WARN  - High memory usage detected: 85% of available memory is in use. Consider increasing the memory limit or optimizing the application to reduce memory consumption.
2025-03-19T12:00:02.000Z - ERROR - Failed to connect to external service at https://api.example.com/v2/data?query=select+*+from+logs+where+timestamp+>+now()-1h&format=json — retrying in 5 seconds (attempt 3 of 10)`}
    </CodeSnippet>
  );
};
```

```tsx
import { CodeSnippet } from '@dynatrace/strato-components/content';

const LineWrap = () => {
  return (
    <CodeSnippet language="log" lineBreaks>
      {`2025-03-19T12:00:00.000Z - INFO  - Application started successfully on port 8080 with configuration: {"database":"postgres://localhost:5432/mydb","cache":"redis://localhost:6379","logLevel":"info","maxConnections":100}
2025-03-19T12:00:01.000Z - WARN  - High memory usage detected: 85% of available memory is in use. Consider increasing the memory limit or optimizing the application to reduce memory consumption.
2025-03-19T12:00:02.000Z - ERROR - Failed to connect to external service at https://api.example.com/v2/data?query=select+*+from+logs+where+timestamp+>+now()-1h&format=json — retrying in 5 seconds (attempt 3 of 10)`}
    </CodeSnippet>
  );
};
```


#### Add new lines

You can add new lines in the following ways:

- Plain string: Add `\n`

- String concatenation: Add `'\n'`

- Template strings: Preserves any whitespace

- JSX expression: One of the expressions can be `'\n'`

```tsx
import { CodeSnippet } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const LineBreak = () => {
  return (
    <Flex flexDirection="column" gap={12}>
      <CodeSnippet language="json">
        {`function exampleTemplate(name: string) {
  console.log("Hello " + name);
}`}
        {'\n\n'}
        {
          'function exampleString(name: string) {\n  console.log("Hello " + name);\n}'
        }
        {'\n\n'}
        {[
          'function exampleStringConcat(name: string) {',
          '  console.log("Hello " + name);',
          '}',
        ].join('\n')}
      </CodeSnippet>
    </Flex>
  );
};
```

```tsx
import { CodeSnippet } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const LineBreak = () => {
  return (
    <Flex flexDirection="column" gap={12}>
      <CodeSnippet language="json">
        {`function exampleTemplate(name: string) {
  console.log("Hello " + name);
}`}
        {'\n\n'}
        {
          'function exampleString(name: string) {\n  console.log("Hello " + name);\n}'
        }
        {'\n\n'}
        {[
          'function exampleStringConcat(name: string) {',
          '  console.log("Hello " + name);',
          '}',
        ].join('\n')}
      </CodeSnippet>
    </Flex>
  );
};
```


#### Change the size

The CodeSnippet component offers a `size` prop with `default` and `condensed`
options. The `condensed` option enables a more compact code display by
optimizing space, while the prop defaults to `default` for a regular view.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change the language
- Hide line numbers
- Limit the snippet height
- React to copying
- Wrap long lines
- Add new lines
- Change the size

### Props

Use the `CodeSnippet` to display a code block in a read-only context. By
default, the code is formatted but not highlighted.

OverviewProperties

#### CodeSnippetProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `language?` | | | Code language to be used to run highlighting on the given code.
 | `allowCopy?` | | `true` | Whether the copy button should be displayed.
 | `showCopyAction?` | | `true` | Whether the copy button should be displayed.
 | `showLineNumbers?` | | `true` | Whether line numbers should be shown.
 | `maxHeight?` | | | Height of the code container. If this is known in advance, then very long
code snippets will still be able to fit into the container while also
having scrolling enabled. Value is given in px.
 | `lineBreaks?` | | `false` | Whether the content breaks into new lines automatically or not.
 | `onCopy?` | () => | | Callback fired when copy button is clicked and the code snippet was copied.
 | `size?` | | | `'default'` | CodeSnippet layout size, 'default' for standard spacing and 'condensed' for reduced font size, padding and margins.Still have questions?Find answers in the Dynatrace Community

---

## EmptyState

`/design/components/content/EmptyState/`

Use the `EmptyState` component to give feedback to an end-user in case there is
no data available. There are cases where this data is missing, requires special
permission, or has not been yet created, for example.

### Import

`tsx
import { EmptyState } from '@dynatrace/strato-components/content';
`

### Use cases

#### Visual presets

Use the `VisualPreset` slot within the `Visual` slot in order to use predefined
illustrations. Different combinations are possible based on the `context` and
`type` props.

```tsx
<EmptyState size="large">
  <EmptyState.Visual>
    <EmptyState.VisualPreset context="query" type="create-new" />
  </EmptyState.Visual>
  <EmptyState.Title>You have no dashboards</EmptyState.Title>
  <EmptyState.Details>
    Create a new dashboard or import an existing one from a JSON file.
  </EmptyState.Details>
  <EmptyState.Actions>
    <Button color="primary" variant="accent">
      New dashboard
    </Button>
    <Button color="neutral" variant="default">
      Import dashboard
    </Button>
  </EmptyState.Actions>
  <EmptyState.Footer>
    Alternatively, you can have a look at your{' '}
    <ExternalLink href="https://www.dynatrace.com">
      shared dashboards
    </ExternalLink>
  </EmptyState.Footer>
</EmptyState>
```

```tsx
<EmptyState size="large">
  <EmptyState.Visual>
    <EmptyState.VisualPreset context="query" type="create-new" />
  </EmptyState.Visual>
  <EmptyState.Title>You have no dashboards</EmptyState.Title>
  <EmptyState.Details>
    Create a new dashboard or import an existing one from a JSON file.
  </EmptyState.Details>
  <EmptyState.Actions>
    <Button color="primary" variant="accent">
      New dashboard
    </Button>
    <Button color="neutral" variant="default">
      Import dashboard
    </Button>
  </EmptyState.Actions>
  <EmptyState.Footer>
    Alternatively, you can have a look at your{' '}
    <ExternalLink href="https://www.dynatrace.com">
      shared dashboards
    </ExternalLink>
  </EmptyState.Footer>
</EmptyState>
```


#### Size

Use the optional `size` prop, which has a default value, to provide a suitable
variation for your use case. When you set `size` to `large`, the layout is
responsive based on the width of its parent container.

#### Small

```tsx
<EmptyState size="small">
  <EmptyState.Visual>
    <EmptyState.VisualPreset context="query" type="create-new" />
  </EmptyState.Visual>
  <EmptyState.Title>You have no dashboards</EmptyState.Title>
  <EmptyState.Details>
    Create a new dashboard or import an existing one from a JSON file.
  </EmptyState.Details>
  <EmptyState.Actions>
    <Button color="primary" variant="accent">
      New dashboard
    </Button>
    <Button color="neutral" variant="default">
      Import dashboard
    </Button>
  </EmptyState.Actions>
  <EmptyState.Footer>
    Alternatively, you can have a look at your{' '}
    <ExternalLink href="https://www.dynatrace.com">
      shared dashboards
    </ExternalLink>
  </EmptyState.Footer>
</EmptyState>
```

```tsx
<EmptyState size="small">
  <EmptyState.Visual>
    <EmptyState.VisualPreset context="query" type="create-new" />
  </EmptyState.Visual>
  <EmptyState.Title>You have no dashboards</EmptyState.Title>
  <EmptyState.Details>
    Create a new dashboard or import an existing one from a JSON file.
  </EmptyState.Details>
  <EmptyState.Actions>
    <Button color="primary" variant="accent">
      New dashboard
    </Button>
    <Button color="neutral" variant="default">
      Import dashboard
    </Button>
  </EmptyState.Actions>
  <EmptyState.Footer>
    Alternatively, you can have a look at your{' '}
    <ExternalLink href="https://www.dynatrace.com">
      shared dashboards
    </ExternalLink>
  </EmptyState.Footer>
</EmptyState>
```


#### Default

```tsx
<EmptyState>
  <EmptyState.Visual>
    <EmptyState.VisualPreset context="generic" type="something-wrong" />
  </EmptyState.Visual>
  <EmptyState.Title>You have no dashboards</EmptyState.Title>
  <EmptyState.Details>
    Create a new dashboard or import an existing one from a JSON file.
  </EmptyState.Details>
  <EmptyState.Actions>
    <Button color="primary" variant="accent">
      New dashboard
    </Button>
    <Button color="neutral" variant="default">
      Import dashboard
    </Button>
  </EmptyState.Actions>
  <EmptyState.Footer>
    Alternatively, you can have a look at your{' '}
    <ExternalLink href="https://www.dynatrace.com">
      shared dashboards
    </ExternalLink>
  </EmptyState.Footer>
</EmptyState>
```

```tsx
<EmptyState>
  <EmptyState.Visual>
    <EmptyState.VisualPreset context="generic" type="something-wrong" />
  </EmptyState.Visual>
  <EmptyState.Title>You have no dashboards</EmptyState.Title>
  <EmptyState.Details>
    Create a new dashboard or import an existing one from a JSON file.
  </EmptyState.Details>
  <EmptyState.Actions>
    <Button color="primary" variant="accent">
      New dashboard
    </Button>
    <Button color="neutral" variant="default">
      Import dashboard
    </Button>
  </EmptyState.Actions>
  <EmptyState.Footer>
    Alternatively, you can have a look at your{' '}
    <ExternalLink href="https://www.dynatrace.com">
      shared dashboards
    </ExternalLink>
  </EmptyState.Footer>
</EmptyState>
```


#### Large

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Visual presets
- Size
- Small
- Default
- Large

### Props

Use the `EmptyState` component to give feedback to an end-user in case there is
no data available. There are cases where this data is missing, requires special
permission, or has not been yet created, for example.

#### GenericEmptyStateProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `size?` | | | | `'default'` | Size of the empty state component.

#### EmptyState.VisualPreset

#### EmptyStateVisualPresetProps
extends`, ` |
 | Name | Type | Default | Description
 | `context` | | | | | | | The visual context of the illustration.
 | `type` | | | | | | | A visual cue added to the illustration hinting at the reason the state is empty.Still have questions?Find answers in the Dynatrace Community
- EmptyState.VisualPreset

---

## ExpandableText

`/design/components/content/ExpandableText/`

The `ExpandableText` component provides expand and collapse functionality for
inline text.

OverviewProperties

### Import

`tsx
import { ExpandableText } from '@dynatrace/strato-components/content';
`

### Use cases

#### Expand text by default

Use the `defaultExpanded` prop to initially expand the text.

```tsx
import { ExpandableText } from '@dynatrace/strato-components/content';
import { Paragraph } from '@dynatrace/strato-components/typography';

const DefaultExpanded = () => {
  return (
    <Paragraph>
      Dynatrace OneAgent automatically monitors all process groups detected in
      your environment.
      <ExpandableText defaultExpanded>
        A single OneAgent per host is required to collect all relevant
        monitoring data — even if your hosts are deployed within Docker
        containers, microservices architectures, or cloud-based infrastructure.
      </ExpandableText>
    </Paragraph>
  );
};
```

```tsx
import { ExpandableText } from '@dynatrace/strato-components/content';
import { Paragraph } from '@dynatrace/strato-components/typography';

const DefaultExpanded = () => {
  return (
    <Paragraph>
      Dynatrace OneAgent automatically monitors all process groups detected in
      your environment.
      <ExpandableText defaultExpanded>
        A single OneAgent per host is required to collect all relevant
        monitoring data — even if your hosts are deployed within Docker
        containers, microservices architectures, or cloud-based infrastructure.
      </ExpandableText>
    </Paragraph>
  );
};
```


#### Customize the Button

Use the `expandLabel` and `collapseLabel` props to set a custom label for the
expand and collapse buttons respectively.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Expand text by default
- Customize the Button

### Props

The `ExpandableText` component provides expand and collapse functionality for
inline text.

OverviewProperties

#### ExpandableTextProps

##### Signature:
`export declare type ExpandableTextProps = & ( | );`

#### ExpandableTextBaseProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `expandLabel?` | | `'Show more'` | Text shown for expanding the content.
 | `collapseLabel?` | | `'Show less'` | Text shown for collapsing the content.

#### ExpandableTextControlledProps
 |
 | Name | Type | Default | Description
 | `expanded` | | | Determines whether or not the content is expanded in a controlled scenario.
 | `onExpandChange` | (expanded: ) => | | Callback fired when the expanded attribute changes in a controlled scenario.

#### ExpandableTextUncontrolledProps
 |
 | Name | Type | Default | Description
 | `defaultExpanded?` | | `false` | Determines whether or not the content is initially expanded in an uncontrolled scenario.Still have questions?Find answers in the Dynatrace Community

---

## FeatureHighlight

`/design/components/content/FeatureHighlight/`

The `FeatureHighlight` supports the onboarding of new users, as well as the
introduction of new features to existing users. It is positioned next to the
specified reference element and has four optional slots: `Title`, `Visual`,
`Content` and `Actions`.

### Import

`tsx
import { FeatureHighlight } from '@dynatrace/strato-components/content';
`

### Use cases

There is no designated trigger for the `FeatureHighlight`. It can be triggered
using a button, but as the state is entirely controlled by you, it is also
possible to open it e.g. on page load. A small pointer connects the
`FeatureHighlight` to the element it is referring to. To handle the component's
state, provide a value for the `open` prop along with an `onClose` callback.

#### Add a visual

Use the `Visual` slot to add an image or a video. The recommended asset size is
400 x 250px (8:5 aspect ratio). If the provided visual has a different aspect
ratio, it is scaled proportionally to fit the container.

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { FeatureHighlight } from '@dynatrace/strato-components/content';
import { OptionsIcon } from '@dynatrace/strato-icons';

const Visual = () => {
  const [open, setOpen] = useState(true);
  const [buttonRef, setButtonRef] = useState<HTMLButtonElement | null>(null);

  return (
    <>
      <Button
        variant="emphasized"
        onClick={() => setOpen(!open)}
        ref={setButtonRef}
      >
        <Button.Prefix>
          <OptionsIcon />
        </Button.Prefix>
        See Options
      </Button>

      <FeatureHighlight
        open={open}
        onClose={() => setOpen(false)}
        anchor={buttonRef}
      >
        <FeatureHighlight.Title>
          Complex data can be visualized in different ways.
        </FeatureHighlight.Title>
        <FeatureHighlight.Visual>
          <img
            src="https://dt-cdn.net/images/notebooks-visualizations-600-102690101f.webp"
            alt="Notebooks visualization options"
          />
        </FeatureHighlight.Visual>
      </FeatureHighlight>
    </>
  );
};
```

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { FeatureHighlight } from '@dynatrace/strato-components/content';
import { OptionsIcon } from '@dynatrace/strato-icons';

const Visual = () => {
  const [open, setOpen] = useState(true);
  const [buttonRef, setButtonRef] = useState<HTMLButtonElement | null>(null);

  return (
    <>
      <Button
        variant="emphasized"
        onClick={() => setOpen(!open)}
        ref={setButtonRef}
      >
        <Button.Prefix>
          <OptionsIcon />
        </Button.Prefix>
        See Options
      </Button>

      <FeatureHighlight
        open={open}
        onClose={() => setOpen(false)}
        anchor={buttonRef}
      >
        <FeatureHighlight.Title>
          Complex data can be visualized in different ways.
        </FeatureHighlight.Title>
        <FeatureHighlight.Visual>
          <img
            src="https://dt-cdn.net/images/notebooks-visualizations-600-102690101f.webp"
            alt="Notebooks visualization options"
          />
        </FeatureHighlight.Visual>
      </FeatureHighlight>
    </>
  );
};
```


#### Add content

The `Content` slot can be used to provide detailed information, for example text
or a link to an external source. If the `FeatureHighlight` exceeds the screen
height, the content becomes scrollable.

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { FeatureHighlight } from '@dynatrace/strato-components/content';
import { Paragraph } from '@dynatrace/strato-components/typography';
import { OptionsIcon } from '@dynatrace/strato-icons';

const Content = () => {
  const [open, setOpen] = useState(true);
  const [buttonRef, setButtonRef] = useState<HTMLButtonElement | null>(null);

  return (
    <>
      <Button
        variant="emphasized"
        onClick={() => setOpen(!open)}
        ref={setButtonRef}
      >
        <Button.Prefix>
          <OptionsIcon />
        </Button.Prefix>
        See Options
      </Button>

      <FeatureHighlight
        open={open}
        onClose={() => setOpen(false)}
        anchor={buttonRef}
      >
        <FeatureHighlight.Title>
          Complex data can be visualized in different ways.
        </FeatureHighlight.Title>
        <FeatureHighlight.Content>
          <Paragraph>
            The resulting data can be visualized in different way. When you're
            working with complex data, you'll find it useful to see a record
            list, at other times, a chart or graph may be more effective.
          </Paragraph>
        </FeatureHighlight.Content>
      </FeatureHighlight>
    </>
  );
};
```

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { FeatureHighlight } from '@dynatrace/strato-components/content';
import { Paragraph } from '@dynatrace/strato-components/typography';
import { OptionsIcon } from '@dynatrace/strato-icons';

const Content = () => {
  const [open, setOpen] = useState(true);
  const [buttonRef, setButtonRef] = useState<HTMLButtonElement | null>(null);

  return (
    <>
      <Button
        variant="emphasized"
        onClick={() => setOpen(!open)}
        ref={setButtonRef}
      >
        <Button.Prefix>
          <OptionsIcon />
        </Button.Prefix>
        See Options
      </Button>

      <FeatureHighlight
        open={open}
        onClose={() => setOpen(false)}
        anchor={buttonRef}
      >
        <FeatureHighlight.Title>
          Complex data can be visualized in different ways.
        </FeatureHighlight.Title>
        <FeatureHighlight.Content>
          <Paragraph>
            The resulting data can be visualized in different way. When you're
            working with complex data, you'll find it useful to see a record
            list, at other times, a chart or graph may be more effective.
          </Paragraph>
        </FeatureHighlight.Content>
      </FeatureHighlight>
    </>
  );
};
```


#### Add actions

The `Actions` slot should be used to add, for example, links to further
information or buttons to perform additonal operations.

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { FeatureHighlight } from '@dynatrace/strato-components/content';
import {
  ExternalLink,
  Paragraph,
} from '@dynatrace/strato-components/typography';
import { OptionsIcon } from '@dynatrace/strato-icons';

const Actions = () => {
  const [open, setOpen] = useState(true);
  const [buttonRef, setButtonRef] = useState<HTMLButtonElement | null>(null);

  return (
    <>
      <Button
        variant="emphasized"
        onClick={() => setOpen(!open)}
        ref={setButtonRef}
      >
        <Button.Prefix>
          <OptionsIcon />
        </Button.Prefix>
        See Options
      </Button>

      <FeatureHighlight
        open={open}
        onClose={() => setOpen(false)}
        anchor={buttonRef}
      >
        <FeatureHighlight.Title>
          Complex data can be visualized in different ways.
        </FeatureHighlight.Title>
        <FeatureHighlight.Visual>
          <img
            src="https://dt-cdn.net/images/notebooks-visualizations-600-102690101f.webp"
            alt="Notebooks visualization options"
          />
        </FeatureHighlight.Visual>
        <FeatureHighlight.Content>
          <Paragraph>
            The resulting data can be visualized in different way. When you're
            working with complex data, you'll find it useful to see a record
            list, at other times, a chart or graph may be more effective.
          </Paragraph>
        </FeatureHighlight.Content>
        <FeatureHighlight.Actions>
          <ExternalLink href="https://www.dynatrace.com/support/help/observe-and-explore/edit-visualizations">
            Read more
          </ExternalLink>
        </FeatureHighlight.Actions>
      </FeatureHighlight>
    </>
  );
};
```

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { FeatureHighlight } from '@dynatrace/strato-components/content';
import {
  ExternalLink,
  Paragraph,
} from '@dynatrace/strato-components/typography';
import { OptionsIcon } from '@dynatrace/strato-icons';

const Actions = () => {
  const [open, setOpen] = useState(true);
  const [buttonRef, setButtonRef] = useState<HTMLButtonElement | null>(null);

  return (
    <>
      <Button
        variant="emphasized"
        onClick={() => setOpen(!open)}
        ref={setButtonRef}
      >
        <Button.Prefix>
          <OptionsIcon />
        </Button.Prefix>
        See Options
      </Button>

      <FeatureHighlight
        open={open}
        onClose={() => setOpen(false)}
        anchor={buttonRef}
      >
        <FeatureHighlight.Title>
          Complex data can be visualized in different ways.
        </FeatureHighlight.Title>
        <FeatureHighlight.Visual>
          <img
            src="https://dt-cdn.net/images/notebooks-visualizations-600-102690101f.webp"
            alt="Notebooks visualization options"
          />
        </FeatureHighlight.Visual>
        <FeatureHighlight.Content>
          <Paragraph>
            The resulting data can be visualized in different way. When you're
            working with complex data, you'll find it useful to see a record
            list, at other times, a chart or graph may be more effective.
          </Paragraph>
        </FeatureHighlight.Content>
        <FeatureHighlight.Actions>
          <ExternalLink href="https://www.dynatrace.com/support/help/observe-and-explore/edit-visualizations">
            Read more
          </ExternalLink>
        </FeatureHighlight.Actions>
      </FeatureHighlight>
    </>
  );
};
```


#### Change the placement

Use the `placement` property to define the component's position.

Possible placement options:

- right-bottom (default)

- right-middle

- right-top

- left-bottom

- left-middle

- left-top

- top-left

- top-middle

- top-right

- bottom-left

- bottom-middle

- bottom-right

#### Add an aria-label

By default, the `FeatureHighlight` is already correctly labeled with
`aria-labelledby` pointing to the title and `aria-describedby` pointing to the
provided content. Only if both title and content are not defined, an appropriate
`aria-label` should be set.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Add a visual
- Add content
- Add actions
- Change the placement
- Add an aria-label

### Props

The `FeatureHighlight` supports the onboarding of new users, as well as the
introduction of new features to existing users. It is positioned next to the
specified reference element and has four optional slots: `Title`, `Visual`,
`Content` and `Actions`.

#### FeatureHighlightProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `open` | | | Whether the FeatureHighlight is currently shown or not. Has to be controlled by the consumer.
 | `anchor` | | | | The element the popover is referring to (i.e. where the pointer is pointing to).
 | `placement?` | | `'right-bottom'` | Placement of the FeatureHighlight.
 | `onClose` | () => | | Callback fired when closing the FeatureHighlight.

### FeatureHighlight.Title

You can use the `FeatureHighlight.Title` component to render a title for the
`FeatureHighlight` overlay.

#### TitleProps
extends`, , `

### FeatureHighlight.Visual

#### VisualProps
extends`, , `

### FeatureHighlight.Content

#### ContentProps
extends`, , `

### FeatureHighlight.Actions

Prop Table did not receive dataStill have questions?Find answers in the Dynatrace Community
- FeatureHighlight.Title
- FeatureHighlight.Visual
- FeatureHighlight.Content
- FeatureHighlight.Actions

---

## HealthIndicator

`/design/components/content/HealthIndicator/`

The HealthIndicator helps consumers to visualize the status of a resource.

### Import

`tsx
import { HealthIndicator } from '@dynatrace/strato-components/content';
`

### Use cases

#### Change the status and visual

Use the `status` and `visual` prop to create the different contextual indicator
variants. When `HealthIndicator` is used within an accentuated `Container`, it
automatically uses the on accent text color of the color defined on the
`HealthIndicator`.

#### Custom visual representation

Use the `HealthIndicator.Visual` component to customize the visual
representation of the indicator.

```tsx
import { HealthIndicator } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Text } from '@dynatrace/strato-components/typography';
import { ApplicationSecuritySignetIcon } from '@dynatrace/strato-icons';

const CustomShape = (
  <svg
    focusable="false"
    role="img"
    aria-hidden="true"
    fill="currentColor"
    width="12"
    height="12"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 12 12"
  >
    <path d="M5.6107 11C5.55998 10.9999 5.50965 10.9907 5.46198 10.9727C5.37001 10.9377 5.292 10.8717 5.24045 10.7851C5.1889 10.6986 5.16679 10.5966 5.17765 10.4955L5.51447 7.27274H2.93808C2.85861 7.27287 2.78062 7.2505 2.71246 7.20803C2.64431 7.16556 2.58858 7.1046 2.55126 7.0317C2.51393 6.9588 2.49642 6.87671 2.50061 6.79425C2.50479 6.71179 2.53052 6.63207 2.57502 6.56366L6.02624 1.20004C6.08083 1.11611 6.16083 1.05352 6.25355 1.02223C6.34627 0.990937 6.44639 0.992727 6.53802 1.02732C6.62611 1.0613 6.70133 1.12385 6.75253 1.20572C6.80374 1.28759 6.82822 1.38441 6.82234 1.48186L6.48553 4.7273H9.06192C9.14139 4.72718 9.21938 4.74955 9.28754 4.79202C9.35569 4.83448 9.41142 4.89544 9.44874 4.96834C9.48607 5.04124 9.50358 5.12333 9.49939 5.20579C9.49521 5.28826 9.46948 5.36797 9.42498 5.43639L5.97375 10.8C5.93363 10.8617 5.87954 10.9122 5.81623 10.9471C5.75293 10.9819 5.68235 11.0001 5.6107 11Z" />
  </svg>
);

const CustomVisual = () => {
  return (
    <>
      <Flex gap={8} alignItems="center">
        <Flex alignSelf="flex-start">
          <HealthIndicator status="ideal" visual="icon">
            <HealthIndicator.Visual>
              <ApplicationSecuritySignetIcon />
            </HealthIndicator.Visual>
          </HealthIndicator>
        </Flex>
        <Text>
          HealthIndicator custom visual representation as icon with a width and
          height of 20px. The gap between the icon and the text is 8px.
        </Text>
      </Flex>
      <Flex gap={4} alignItems="center">
        <HealthIndicator status="critical" visual="shape">
          <HealthIndicator.Visual>{CustomShape}</HealthIndicator.Visual>
        </HealthIndicator>
        <Text>
          HealthIndicator custom visual representation as shape with a width and
          height of 12px. The gap between the shape and the text is 4px.
        </Text>
      </Flex>
    </>
  );
};
```

```tsx
import { HealthIndicator } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Text } from '@dynatrace/strato-components/typography';
import { ApplicationSecuritySignetIcon } from '@dynatrace/strato-icons';

const CustomShape = (
  <svg
    focusable="false"
    role="img"
    aria-hidden="true"
    fill="currentColor"
    width="12"
    height="12"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 12 12"
  >
    <path d="M5.6107 11C5.55998 10.9999 5.50965 10.9907 5.46198 10.9727C5.37001 10.9377 5.292 10.8717 5.24045 10.7851C5.1889 10.6986 5.16679 10.5966 5.17765 10.4955L5.51447 7.27274H2.93808C2.85861 7.27287 2.78062 7.2505 2.71246 7.20803C2.64431 7.16556 2.58858 7.1046 2.55126 7.0317C2.51393 6.9588 2.49642 6.87671 2.50061 6.79425C2.50479 6.71179 2.53052 6.63207 2.57502 6.56366L6.02624 1.20004C6.08083 1.11611 6.16083 1.05352 6.25355 1.02223C6.34627 0.990937 6.44639 0.992727 6.53802 1.02732C6.62611 1.0613 6.70133 1.12385 6.75253 1.20572C6.80374 1.28759 6.82822 1.38441 6.82234 1.48186L6.48553 4.7273H9.06192C9.14139 4.72718 9.21938 4.74955 9.28754 4.79202C9.35569 4.83448 9.41142 4.89544 9.44874 4.96834C9.48607 5.04124 9.50358 5.12333 9.49939 5.20579C9.49521 5.28826 9.46948 5.36797 9.42498 5.43639L5.97375 10.8C5.93363 10.8617 5.87954 10.9122 5.81623 10.9471C5.75293 10.9819 5.68235 11.0001 5.6107 11Z" />
  </svg>
);

const CustomVisual = () => {
  return (
    <>
      <Flex gap={8} alignItems="center">
        <Flex alignSelf="flex-start">
          <HealthIndicator status="ideal" visual="icon">
            <HealthIndicator.Visual>
              <ApplicationSecuritySignetIcon />
            </HealthIndicator.Visual>
          </HealthIndicator>
        </Flex>
        <Text>
          HealthIndicator custom visual representation as icon with a width and
          height of 20px. The gap between the icon and the text is 8px.
        </Text>
      </Flex>
      <Flex gap={4} alignItems="center">
        <HealthIndicator status="critical" visual="shape">
          <HealthIndicator.Visual>{CustomShape}</HealthIndicator.Visual>
        </HealthIndicator>
        <Text>
          HealthIndicator custom visual representation as shape with a width and
          height of 12px. The gap between the shape and the text is 4px.
        </Text>
      </Flex>
    </>
  );
};
```


#### Label

The `HealthIndicator.Label` component allows you to render custom labels using
both inline and block-level elements.

Note: Be careful when using a different line height than the base line height.
If you use `Heading` or `Text` with a small `textStyle`, ensure you place the
`HealthIndicator` inside the `Heading` or `Text` to maintain proper line
height alignment.

```tsx
import { HealthIndicator } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  Emphasis,
  Heading,
  Link,
  Strong,
  Text,
} from '@dynatrace/strato-components/typography';

const Label = () => {
  return (
    <Flex flexDirection="column">
      {/*String*/}
      <HealthIndicator>
        <HealthIndicator.Label>String label</HealthIndicator.Label>
      </HealthIndicator>
      {/*Mixed with strong and emphasis*/}
      <HealthIndicator>
        <HealthIndicator.Label>
          <Strong>Strong</Strong> or <Emphasis>emphasized</Emphasis> label
        </HealthIndicator.Label>
      </HealthIndicator>
      {/*Link*/}
      <HealthIndicator>
        <HealthIndicator.Label>
          <Link href="#">Link</Link>
        </HealthIndicator.Label>
      </HealthIndicator>
      {/*Heading*/}
      <Heading>
        <HealthIndicator>
          <HealthIndicator.Label>Headline</HealthIndicator.Label>
        </HealthIndicator>
      </Heading>
      {/*Small Text*/}
      <Text textStyle="small">
        <HealthIndicator status="neutral" visual="icon">
          <HealthIndicator.Label>Small text</HealthIndicator.Label>
        </HealthIndicator>
      </Text>
    </Flex>
  );
};
```

```tsx
import { HealthIndicator } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  Emphasis,
  Heading,
  Link,
  Strong,
  Text,
} from '@dynatrace/strato-components/typography';

const Label = () => {
  return (
    <Flex flexDirection="column">
      {/*String*/}
      <HealthIndicator>
        <HealthIndicator.Label>String label</HealthIndicator.Label>
      </HealthIndicator>
      {/*Mixed with strong and emphasis*/}
      <HealthIndicator>
        <HealthIndicator.Label>
          <Strong>Strong</Strong> or <Emphasis>emphasized</Emphasis> label
        </HealthIndicator.Label>
      </HealthIndicator>
      {/*Link*/}
      <HealthIndicator>
        <HealthIndicator.Label>
          <Link href="#">Link</Link>
        </HealthIndicator.Label>
      </HealthIndicator>
      {/*Heading*/}
      <Heading>
        <HealthIndicator>
          <HealthIndicator.Label>Headline</HealthIndicator.Label>
        </HealthIndicator>
      </Heading>
      {/*Small Text*/}
      <Text textStyle="small">
        <HealthIndicator status="neutral" visual="icon">
          <HealthIndicator.Label>Small text</HealthIndicator.Label>
        </HealthIndicator>
      </Text>
    </Flex>
  );
};
```


#### Usage of aria props

Add the `aria-label` prop to the component if it's used without a label.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change the status and visual
- Custom visual representation
- Label
- Usage of aria props

```tsx
import { HealthIndicator } from '@dynatrace/strato-components/content';
import { ApplicationSecuritySignetIcon } from '@dynatrace/strato-icons';

const UsageAria = () => {
  return (
    <HealthIndicator
      status="ideal"
      visual="icon"
      aria-label="Application Security health indicator"
    >
      <HealthIndicator.Visual>
        <ApplicationSecuritySignetIcon />
      </HealthIndicator.Visual>
    </HealthIndicator>
  );
};
```

```tsx
import { HealthIndicator } from '@dynatrace/strato-components/content';
import { ApplicationSecuritySignetIcon } from '@dynatrace/strato-icons';

const UsageAria = () => {
  return (
    <HealthIndicator
      status="ideal"
      visual="icon"
      aria-label="Application Security health indicator"
    >
      <HealthIndicator.Visual>
        <ApplicationSecuritySignetIcon />
      </HealthIndicator.Visual>
    </HealthIndicator>
  );
};
```


### Props

The HealthIndicator helps consumers to visualize the status of a resource.

#### HealthIndicatorProps
extends`, , , , , , , ` |
 | Name | Type | Default | Description
 | `status?` | | | | | | `'neutral'` | The status of the component. This should be chosen based on the context
the indicator is used in.
 | `visual?` | | | `'shape'` | Configures the visual representation of the component, which is a shape by
default.

### HealthIndicator.Visual

You can use the `HealthIndicator.Visual` component to render a custom visual
representation of your `HealthIndicator`.

#### HealthIndicatorVisualProps
extends`, , `

### HealthIndicator.Label

You can use the `HealthIndicator.Label` component to render a label for your
`HealthIndicator`.

#### HealthIndicatorLabelProps
extends`, , `Still have questions?Find answers in the Dynatrace Community
- HealthIndicator.Visual
- HealthIndicator.Label

---

## InformationOverlay

`/design/components/content/InformationOverlay/`

The `InformationOverlay` provides additional information via an overlay, the
position of which can be adjusted. According to the type of information, the
`variant` can be set. The trigger consists of an icon and an optional text. By
default, the `variant` is `neutral` and the overlay is positioned on the bottom.

### Import

`tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';
`

### Demo

Provide context, guidance, feedback, and other helpful information with the
`InformationOverlay` component. See Usage for best practices,
including content guidelines.

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const Basic = () => {
  return (
    <InformationOverlay>
      <InformationOverlay.Trigger />
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const Basic = () => {
  return (
    <InformationOverlay>
      <InformationOverlay.Trigger />
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```


### Add trigger text

Apart from using the default trigger with only an icon, it's possible to specify
additional text for the trigger.

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const TriggerText = () => {
  return (
    <InformationOverlay>
      <InformationOverlay.Trigger>
        Dynatrace Platform
      </InformationOverlay.Trigger>
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const TriggerText = () => {
  return (
    <InformationOverlay>
      <InformationOverlay.Trigger>
        Dynatrace Platform
      </InformationOverlay.Trigger>
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```


### Change trigger icon

Use the `InformationOverlay.Trigger` slot to customize the icon for the trigger.
Wrap the desired icon inside the `InformationOverlay.Icon` slot component.

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';
import { ClockIcon } from '@dynatrace/strato-icons';

const TriggerIcon = () => {
  return (
    <InformationOverlay>
      <InformationOverlay.Trigger>
        <InformationOverlay.Icon>
          <ClockIcon />
        </InformationOverlay.Icon>
      </InformationOverlay.Trigger>
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';
import { ClockIcon } from '@dynatrace/strato-icons';

const TriggerIcon = () => {
  return (
    <InformationOverlay>
      <InformationOverlay.Trigger>
        <InformationOverlay.Icon>
          <ClockIcon />
        </InformationOverlay.Icon>
      </InformationOverlay.Trigger>
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```


### Change color

Use the `color` prop to set the color according to the type of information.
Changing the color also affects the displayed icon.

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex flexDirection="column" alignItems="flex-start">
      <InformationOverlay color="neutral">
        <InformationOverlay.Trigger>Neutral</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          Dynatrace is a software-intelligence monitoring platform that
          simplifies enterprise cloud complexity and accelerates digital
          transformation.
        </InformationOverlay.Content>
      </InformationOverlay>
      <InformationOverlay color="primary">
        <InformationOverlay.Trigger>Primary</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          Dynatrace delivers simplified, automated infrastructure monitoring
          that provides broad visibility across your hosts, VMs, containers,
          network, events, and logs.
        </InformationOverlay.Content>
      </InformationOverlay>
      <InformationOverlay color="success">
        <InformationOverlay.Trigger>Success</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          The 1.255 GA release contains 13 resolved issues (including 1
          vulnerability resolution).
        </InformationOverlay.Content>
      </InformationOverlay>
      <InformationOverlay color="warning">
        <InformationOverlay.Trigger>Warning</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          All your Dynatrace monitoring data will be deleted 60 days following
          the expiration of your license.
        </InformationOverlay.Content>
      </InformationOverlay>
      <InformationOverlay color="critical">
        <InformationOverlay.Trigger>Critical</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          Unauthorized. The token authentication has failed. Check to see if
          your token has the required scopes.
        </InformationOverlay.Content>
      </InformationOverlay>
    </Flex>
  );
};
```

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex flexDirection="column" alignItems="flex-start">
      <InformationOverlay color="neutral">
        <InformationOverlay.Trigger>Neutral</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          Dynatrace is a software-intelligence monitoring platform that
          simplifies enterprise cloud complexity and accelerates digital
          transformation.
        </InformationOverlay.Content>
      </InformationOverlay>
      <InformationOverlay color="primary">
        <InformationOverlay.Trigger>Primary</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          Dynatrace delivers simplified, automated infrastructure monitoring
          that provides broad visibility across your hosts, VMs, containers,
          network, events, and logs.
        </InformationOverlay.Content>
      </InformationOverlay>
      <InformationOverlay color="success">
        <InformationOverlay.Trigger>Success</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          The 1.255 GA release contains 13 resolved issues (including 1
          vulnerability resolution).
        </InformationOverlay.Content>
      </InformationOverlay>
      <InformationOverlay color="warning">
        <InformationOverlay.Trigger>Warning</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          All your Dynatrace monitoring data will be deleted 60 days following
          the expiration of your license.
        </InformationOverlay.Content>
      </InformationOverlay>
      <InformationOverlay color="critical">
        <InformationOverlay.Trigger>Critical</InformationOverlay.Trigger>
        <InformationOverlay.Content>
          Unauthorized. The token authentication has failed. Check to see if
          your token has the required scopes.
        </InformationOverlay.Content>
      </InformationOverlay>
    </Flex>
  );
};
```


### Change overlay placement

Use the `placement` prop to set the preferred position for the overlay if there
is enough space. If the preferred position is not possible, the overlay will be
positioned according to the available space.

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const Placement = () => {
  return (
    <InformationOverlay placement="right">
      <InformationOverlay.Trigger>
        Dynatrace Platform
      </InformationOverlay.Trigger>
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const Placement = () => {
  return (
    <InformationOverlay placement="right">
      <InformationOverlay.Trigger>
        Dynatrace Platform
      </InformationOverlay.Trigger>
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```


### Open overlay by default

Use the `defaultOpen` prop to set the overlay to open in uncontrolled scenarios.

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const DefaultOpen = () => {
  return (
    <InformationOverlay defaultOpen>
      <InformationOverlay.Trigger>
        Dynatrace Platform
      </InformationOverlay.Trigger>
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const DefaultOpen = () => {
  return (
    <InformationOverlay defaultOpen>
      <InformationOverlay.Trigger>
        Dynatrace Platform
      </InformationOverlay.Trigger>
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```


### Add aria-label

Use the `aria-label` prop on the `Trigger` to set a specific `aria-label` on the
trigger button. If the trigger is just an icon without a text label, add an
`aria-label` to help users understand the meaning and functionality.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Add trigger text
- Change trigger icon
- Change color
- Change overlay placement
- Open overlay by default
- Add aria-label

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const AriaLabel = () => {
  return (
    <InformationOverlay>
      <InformationOverlay.Trigger aria-label="Open additional information" />
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```

```tsx
import { InformationOverlay } from '@dynatrace/strato-components/content';

const AriaLabel = () => {
  return (
    <InformationOverlay>
      <InformationOverlay.Trigger aria-label="Open additional information" />
      <InformationOverlay.Content>
        Dynatrace is a software-intelligence monitoring platform that simplifies
        enterprise cloud complexity and accelerates digital transformation.
      </InformationOverlay.Content>
    </InformationOverlay>
  );
};
```


### Props

The `InformationOverlay` provides additional information via an overlay, the
position of which can be adjusted. According to the type of information, the
`variant` can be set. The trigger consists of an icon and an optional text. By
default, the `variant` is `neutral` and the overlay is positioned on the bottom.

#### InformationOverlayProps

##### Signature:
`export declare type InformationOverlayProps = & ( | );`

#### InformationOverlayBaseProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `placement?` | | `'bottom'` | The preferred placement for the overlay if there is enough space. If the preferred placement is not possible, the overlay will be positioned according to the available space.
 | `color?` | | | | | | `'neutral' or a container's color.` | Controls the color of the styling and the trigger icon.

#### InformationOverlayControlledProps
 |
 | Name | Type | Default | Description
 | `open` | | | Determines whether the overlay is open in a controlled scenario.
 | `onOpenChange` | (isOpen: ) => | | Callback fired when the open attribute changes in a controlled scenario.

#### InformationOverlayUncontrolledProps
 |
 | Name | Type | Default | Description
 | `defaultOpen?` | | `false` | Determines whether the overlay is initially opened in an uncontrolled scenario.

#### InformationOverlay.Content

You can use the `InformationOverlay.Content` component to render any content
inside the `InformationOverlay` overlay.

#### InformationContentProps
extends`, `

#### InformationOverlay.Trigger

You can use the `InformationOverlay.Trigger` component to render a custom
trigger for the `InformationOverlay` overlay.

#### InformationOverlayTriggerProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `'aria-label'?` | | | Optional aria-label to provide an additional description for the trigger.Still have questions?Find answers in the Dynatrace Community
- InformationOverlay.Content
- InformationOverlay.Trigger

---

## KeyboardShortcut

`/design/components/content/KeyboardShortcut/`

The `KeyboardShortcut` component visualizes one or multiple keys to communicate
keyboard shortcuts for certain actions. To specify a shortcut, provide the key
sequence in the
aria-keyshortcuts
format.

### Import

`tsx
import { KeyboardShortcut } from '@dynatrace/strato-components/content';
`

### Use cases

A shortcut consists of zero, one or more modifier keys, followed by a
non-modifier key. The keys are joined by a plus sign and there are some rules on
how to write the modifier keys. Aria-keyshortcuts also allows the user to define
alternative key combinations separated with space, however this component only
displays the first one.

#### Disable the component

The KeyboardShortcut component can also be displayed in a disabled state. By
setting the `disabled` attribute, the styling is adjusted accordingly and the
`aria-disabled` attribute is applied to indicate that the shortcut is currently
disabled.

#### Change the variant

Use the `variant` prop to define if the component should be rendered using the
`default` or `minimal` styling.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Disable the component
- Change the variant

### Props

The `KeyboardShortcut` component visualizes one or multiple keys to communicate
keyboard shortcuts for certain actions. To specify a shortcut, provide the key
sequence in the
aria-keyshortcuts
format.

#### KeyboardShortcutProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `keys` | | | The list of keys the component should display, specified in the aria-keyshortcuts format.
 | `variant?` | | | `'default'` | The variant that should be used for styling the keys.
 | `disabled?` | | `'false'` | Whether the component should be rendered in a disabled state.Still have questions?Find answers in the Dynatrace Community

---

## KeyboardShortcutTooltip

`/design/components/content/KeyboardShortcutTooltip/`

Use the `KeyboardShortcutTooltip` component to display a keyboard shortcut
inside a tooltip.

### Import

`tsx
import { KeyboardShortcutTooltip } from '@dynatrace/strato-components/content';
`

### Demo

The component opens when the user hovers over the trigger, which must be an
interactive element, such as a button or input. Use the `keys` prop and the
format shown in
aria-keyshortcuts
to display the shortcut in the tooltip. See Usage for additional
guidance.

### Add label

Use the `text` prop to add an optional label above the keyboard shortcut.

### Place tooltip

Use the `placement` prop to set the position of the tooltip relative to the
trigger element.

### Disable tooltip

To disable the tooltip, set the `disabled` prop. The tooltip won't appear on
hover.

### Disable keyboard shortcut

Set the `shortcutDisabled` prop, to display `KeyboardShortcutTooltip` in a
disabled state. The tooltip with the shortcut will appear on hover, but with
disabled styling.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Add label
- Place tooltip
- Disable tooltip
- Disable keyboard shortcut

### Props

Use the `KeyboardShortcutTooltip` component to display a keyboard shortcut
inside a tooltip.

#### KeyboardShortcutTooltipProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `keys` | | | The list of keys the component should display, specified in the aria-keyshortcuts format.
 | `shortcutDisabled?` | | `'false'` | Whether the component should be rendered in a disabled state.
 | `text?` | | | Text displayed in the tooltip component.

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

## Markdown

`/design/components/content/Markdown/`

The `Markdown` component is a read-only way to display content formatted in
markdown-style.

OverviewProperties

### Import

`tsx
import { Markdown } from '@dynatrace/strato-components/content';
`

### Use cases

#### Customize markdown rendering

Use the `customComponentMappings` prop to override the default rendering
behavior.

`tsx
const customMappings = { h2: ({ children }) => (u>{children}h2>u>)}Markdown customComponentMappings={customMappings}>## TestMarkdown>
`

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Customize markdown rendering

```tsx
import { type PropsWithChildren } from 'react';

import { Markdown } from '@dynatrace/strato-components/content';
import { Heading } from '@dynatrace/strato-components/typography';

const markdownExample = `
For example, we want to provide custom implementation for the \`##\` markdown tag (which is equivalent to \`h2\` HTML tag).

```tsx
import { type PropsWithChildren } from 'react';

import { Markdown } from '@dynatrace/strato-components/content';
import { Heading } from '@dynatrace/strato-components/typography';

const markdownExample = `
For example, we want to provide custom implementation for the \`##\` markdown tag (which is equivalent to \`h2\` HTML tag).

## The custom H2 header (underlined)
`;

const CustomizedRendering = () => {
  const customMapping = {
    h2: ({ children }: PropsWithChildren) => (
      <u>
        <Heading level={2}>{children}</Heading>
      </u>
    ),
  };

  return (
    <Markdown customComponentMappings={customMapping}>
      {markdownExample}
    </Markdown>
  );
};
```


## The custom H2 header (underlined)
`;

const CustomizedRendering = () => {
  const customMapping = {
    h2: ({ children }: PropsWithChildren) => (
      <u>
        <Heading level={2}>{children}</Heading>
      </u>
    ),
  };

  return (
    <Markdown customComponentMappings={customMapping}>
      {markdownExample}
    </Markdown>
  );
};
```


### Props

The `Markdown` component is a read-only way to display content formatted in
markdown-style.

OverviewProperties

#### MarkdownProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `children` | | | The markdown content to render.
 | `customComponentMappings?` | | `undefined` | A map of HTML tags (e.g., `'a'`, `'h1'`) to custom render functions,
allowing you to override the default rendering of specific elements.
 | `onSelectionChange?` | (selection: ) => | | Callback fired whenever the user's text selection within the rendered
markdown changes. Receives a `MarkdownSelection` describing the
selected range expressed as positions in the original markdown source.Still have questions?Find answers in the Dynatrace Community

---

## MessageContainer

`/design/components/content/MessageContainer/`

The `MessageContainer` allows you to communicate statuses prominently. It's
either persistent or dismissible. If needed, provide actions to help users take
the following steps or resolve an issue.

### Import

`tsx
import { MessageContainer } from '@dynatrace/strato-components/content';
`

### Use cases

#### Use different variants

Use the `variant` prop to change the color theme of the `MessageContainer`. Each
`variant` value has a matching default icon, which is based on the
`status and health` design concept, so changing
the `variant` also changes the provided default prefix icon.

```tsx
import { MessageContainer } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex flexDirection="column">
      <MessageContainer>
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a neutral message
        </MessageContainer.Description>
      </MessageContainer>
      <MessageContainer variant="primary">
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a primary message
        </MessageContainer.Description>
      </MessageContainer>
      <MessageContainer variant="success">
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a success message
        </MessageContainer.Description>
      </MessageContainer>
      <MessageContainer variant="warning">
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a warning message
        </MessageContainer.Description>
      </MessageContainer>
      <MessageContainer variant="critical">
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a critical message
        </MessageContainer.Description>
      </MessageContainer>
    </Flex>
  );
};
```

```tsx
import { MessageContainer } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex flexDirection="column">
      <MessageContainer>
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a neutral message
        </MessageContainer.Description>
      </MessageContainer>
      <MessageContainer variant="primary">
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a primary message
        </MessageContainer.Description>
      </MessageContainer>
      <MessageContainer variant="success">
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a success message
        </MessageContainer.Description>
      </MessageContainer>
      <MessageContainer variant="warning">
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a warning message
        </MessageContainer.Description>
      </MessageContainer>
      <MessageContainer variant="critical">
        <MessageContainer.Prefix />
        <MessageContainer.Description>
          This is a critical message
        </MessageContainer.Description>
      </MessageContainer>
    </Flex>
  );
};
```


#### Show a prefix icon

Use to render an icon. You can supply the icon as
child to render a custom prefix icon.

#### Add actions

Certain info messages might prompt your user to perform an action or navigate to
a different location. You can pass `Button`s, `Link`s, or other content as
children to `MessageContainer.Actions`.

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import { MessageContainer } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Actions = () => {
  return (
    <Flex flexDirection="column">
      <MessageContainer variant="primary">
        <MessageContainer.Description>
          This is a message
        </MessageContainer.Description>
        <MessageContainer.Actions>
          <Button variant="emphasized" color="primary">
            Action 1
          </Button>
        </MessageContainer.Actions>
      </MessageContainer>

      <MessageContainer variant="primary">
        <MessageContainer.Prefix />
        <MessageContainer.Title>This is a title</MessageContainer.Title>
        <MessageContainer.Description>
          This is a message providing information to the user with actionable
          insights.
        </MessageContainer.Description>
        <MessageContainer.Actions>
          <Button variant="emphasized" color="critical">
            Action 1
          </Button>
        </MessageContainer.Actions>
      </MessageContainer>
    </Flex>
  );
};
```

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import { MessageContainer } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Actions = () => {
  return (
    <Flex flexDirection="column">
      <MessageContainer variant="primary">
        <MessageContainer.Description>
          This is a message
        </MessageContainer.Description>
        <MessageContainer.Actions>
          <Button variant="emphasized" color="primary">
            Action 1
          </Button>
        </MessageContainer.Actions>
      </MessageContainer>

      <MessageContainer variant="primary">
        <MessageContainer.Prefix />
        <MessageContainer.Title>This is a title</MessageContainer.Title>
        <MessageContainer.Description>
          This is a message providing information to the user with actionable
          insights.
        </MessageContainer.Description>
        <MessageContainer.Actions>
          <Button variant="emphasized" color="critical">
            Action 1
          </Button>
        </MessageContainer.Actions>
      </MessageContainer>
    </Flex>
  );
};
```


#### Make `MessageContainer` dismissible

Pass a callback function to the `onDismiss` prop of `MessageContainer` to
display a close button that calls the provided callback when clicked. You can
combine that with your own state to determine when to show the message.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Use different variants
- Show a prefix icon
- Add actions
- Make `MessageContainer` dismissible

### Props

The `MessageContainer` allows you to communicate statuses prominently. It's
either persistent or dismissible. If needed, provide actions to help users take
the following steps or resolve an issue.

#### MessageContainerProps
extends`, , , , , , , ` |
 | Name | Type | Default | Description
 | `variant?` | | | | | | | Defines the type of the panel.
 | `onDismiss?` | () => | | Handler that is called if the panel gets dismissed.

### MessageContainer.Prefix

The slot for an icon. will render a specific icon
per variant. Users can provide an icon as child, to customize the displayed
icon.

#### MessageContainerPrefixProps
extends`, ` |
 | Name | Type | Default | Description
 | `children?` | | | Elements to be displayed in the prefix slot.

### MessageContainer.Title

The slot to render the title.

#### MessageContainerTitleProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the title slot.

### MessageContainer.Description

The slot to render the description.

#### MessageContainerDescriptionProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the description slot.

### MessageContainer.Actions

The slot to render actions.

#### MessageContainerActionsProps
extends`, ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the actions slot.Still have questions?Find answers in the Dynatrace Community
- MessageContainer.Prefix
- MessageContainer.Title
- MessageContainer.Description
- MessageContainer.Actions

---

## Microguide

`/design/components/content/Microguide/`

The `Microguide` supports the onboarding of new users, as well as the
introduction of new features to existing users. It can have one or multiple
steps, each of which has three optional slots: `Title`, `Visual` and `Content`.

### Import

`tsx
import { Microguide } from '@dynatrace/strato-components/content';
`

### Use cases

There is no designated trigger for the `Microguide`. The guide can be triggered
using a button, but as the state is entirely controlled by you, it is also
possible to open it e.g. on page load. To handle the component's state, provide
a value for the `open` prop along with an `onClose` callback. The `onClose`
callback also includes the current step and whether the Microguide was finished.

To define a single step, wrap the desired content with the `Step` slot. Each
step can have a `Title`, a `Visual` and a `Content` slot, all of which are
optional.

#### Define multiple steps

Use multiple `Step` slots in the desired order to create multiple pages for the
`Microguide`.

To react to the user navigating between steps, use the `onStepChange` callback,
which includes the step that the user is navigating to.

#### Add a visual

Use the `Visual` slot to add an image or a video. The recommended asset size is
400 x 250px (8:5 aspect ratio). If the provided visual has a different aspect
ratio, it is scaled proportionally to fit the container.

#### Add content

The `Content` slot can be used to provide detailed information for a step, such
as text or links to more information. If the microguide exceeds the screen
height, the content becomes scrollable.

#### Change the placement

Use the `placement` property to define the component's position.

Possible placement options:

- bottom-right (default)

- bottom-left

- top-right

- top-left

#### Add an aria-label

By default, the `Microguide` is already correctly labeled with `aria-labelledby`
pointing to the title and `aria-describedby` pointing to the provided content.
Only if both title and content are not defined, an appropriate `aria-label`
should be set.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Define multiple steps
- Add a visual
- Add content
- Change the placement
- Add an aria-label

### Props

The `Microguide` supports the onboarding of new users, as well as the
introduction of new features to existing users. It can have one or multiple
steps, each of which has three optional slots: `Title`, `Visual` and `Content`.

#### MicroguideProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `open` | | | Whether the Microguide is currently shown or not. Has to be controlled by the consumer.
 | `placement?` | | | | | `'bottom-right'` | Placement of the Microguide.
 | `onClose` | (currentStep: , finished: ) => | | Callback fired when closing the Microguide.
Indicates the current step (zero-based) when closing and whether the Microguide was finished (i.e. closed in the last step).
 | `onStepChange?` | (step: ) => | | Callback fired when the user navigates between steps. Indicates the target step (zero-based).

#### Microguide.Step

Prop Table did not receive data

#### Microguide.Content

#### ContentProps
extends`, , `

#### Microguide.Title

You can use the `Microguide.Title` component to render a title for the
`Microguide` overlay.

#### TitleProps
extends`, , `

#### Microguide.Visual

#### VisualProps
extends`, , `Still have questions?Find answers in the Dynatrace Community
- Microguide.Step
- Microguide.Content
- Microguide.Title
- Microguide.Visual

---

## ProgressBar

`/design/components/content/ProgressBar/`

Use the `ProgressBar` component to show your users that a system operation such
as downloading, uploading, or processing is progressing. The `ProgressBar` can
be used to visualize determinate or indeterminate progress.

### Import

`tsx
import { ProgressBar } from '@dynatrace/strato-components/content';
`

### Use cases

#### Indeterminate ProgressBar

If you don't provide numeric values for the `ProgressBar`, it will be
indeterminate and the progress animation will loop continuously.

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';

const Basic = () => {
  return <ProgressBar />;
};
```

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';

const Basic = () => {
  return <ProgressBar />;
};
```


#### Determinate ProgressBar

Assign numeric values to show stages of progression. By default, the numeric
values are percentages. If you don't want to use percentages, you'll need to set
a proper `aria-valuetext` following A11y guidance. The value
is clamped by the `min` and `max` values. These are 0 to 100 by default, as in
this example.

```tsx
import { useEffect, useState } from 'react';

import { ProgressBar } from '@dynatrace/strato-components/content';

const Determinate = () => {
  const [value, setValue] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setValue((prev) => (prev + 5) % 101);
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <ProgressBar value={value} />;
};
```

```tsx
import { useEffect, useState } from 'react';

import { ProgressBar } from '@dynatrace/strato-components/content';

const Determinate = () => {
  const [value, setValue] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setValue((prev) => (prev + 5) % 101);
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <ProgressBar value={value} />;
};
```


#### Set min and max values

You can adjust the progress animation by setting a `min` value, a `max` value,
or both. This example uses 20 as the `min` value and 150 as the `max` value.

```tsx
import { useEffect, useState } from 'react';

import { ProgressBar } from '@dynatrace/strato-components/content';

const MinMax = () => {
  const [value, setValue] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setValue((prev) => (prev + 5) % 101);
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <ProgressBar value={value} min={20} max={150} />;
};
```

```tsx
import { useEffect, useState } from 'react';

import { ProgressBar } from '@dynatrace/strato-components/content';

const MinMax = () => {
  const [value, setValue] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setValue((prev) => (prev + 5) % 101);
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <ProgressBar value={value} min={20} max={150} />;
};
```


#### Add more information

To display more information about the progress, use `ProgressBar` compounds.
`ProgressBar.Label` can be used to describe what's happening (e.g. Downloading,
Uploading, Processing). `ProgressBar.Icon` allows you to add visual icons.
`ProgressBar.Value` displays the progress in numerical values.

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';
import { DownloadIcon } from '@dynatrace/strato-icons';

const Compounds = () => {
  return (
    <ProgressBar value={75}>
      <ProgressBar.Label>Downloading</ProgressBar.Label>
      <ProgressBar.Icon>
        <DownloadIcon />
      </ProgressBar.Icon>
      <ProgressBar.Value>75 / 100 MB</ProgressBar.Value>
    </ProgressBar>
  );
};
```

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';
import { DownloadIcon } from '@dynatrace/strato-icons';

const Compounds = () => {
  return (
    <ProgressBar value={75}>
      <ProgressBar.Label>Downloading</ProgressBar.Label>
      <ProgressBar.Icon>
        <DownloadIcon />
      </ProgressBar.Icon>
      <ProgressBar.Value>75 / 100 MB</ProgressBar.Value>
    </ProgressBar>
  );
};
```


#### Change density

The `ProgressBar` can also be condensed. To enhance the layout, any additional
information can be shown above the `ProgressBar`. If there's insufficient space
to display the entire label or value text, it will be truncated automatically.

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';
import { DownloadIcon } from '@dynatrace/strato-icons';

const Density = () => {
  return (
    <div style={{ maxWidth: '300px' }}>
      <ProgressBar value={75} density="condensed">
        <ProgressBar.Label>
          Very long label that will be truncated in a condensed ProgressBar
        </ProgressBar.Label>
        <ProgressBar.Icon>
          <DownloadIcon />
        </ProgressBar.Icon>
        <ProgressBar.Value>75 / 100 MB</ProgressBar.Value>
      </ProgressBar>
    </div>
  );
};
```

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';
import { DownloadIcon } from '@dynatrace/strato-icons';

const Density = () => {
  return (
    <div style={{ maxWidth: '300px' }}>
      <ProgressBar value={75} density="condensed">
        <ProgressBar.Label>
          Very long label that will be truncated in a condensed ProgressBar
        </ProgressBar.Label>
        <ProgressBar.Icon>
          <DownloadIcon />
        </ProgressBar.Icon>
        <ProgressBar.Value>75 / 100 MB</ProgressBar.Value>
      </ProgressBar>
    </div>
  );
};
```


#### Change color scheme

The `ProgressBar` can be rendered in different colors using the `color` prop.
Color schemes: `neutral`, `primary`, `success`, `warning`, `critical`.

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Color = () => {
  return (
    <Flex flexDirection="column">
      <ProgressBar value={75} color="neutral" />
      <ProgressBar value={75} color="primary" />
      <ProgressBar value={75} color="success" />
      <ProgressBar value={75} color="warning" />
      <ProgressBar value={75} color="critical" />
    </Flex>
  );
};
```

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';
import { Flex } from '@dynatrace/strato-components/layouts';

const Color = () => {
  return (
    <Flex flexDirection="column">
      <ProgressBar value={75} color="neutral" />
      <ProgressBar value={75} color="primary" />
      <ProgressBar value={75} color="success" />
      <ProgressBar value={75} color="warning" />
      <ProgressBar value={75} color="critical" />
    </Flex>
  );
};
```


### Accessibility

#### aria-label

Support usability by adding an `aria-label` to explain the progress that's
represented. This step is particularly important if you aren't using a
`ProgressBar.Label` within the `ProgressBar` compound component.

#### aria-valuetext

If the `value` property of the `ProgressBar` is not a percentage (the default
setting) you must add an
aria-valuetext
to explain what it conveys. Additionally, if it's unclear what meaning the value
of the `ProgressBar` conveys, you can also add the `aria-valuetext`.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Indeterminate ProgressBar
- Determinate ProgressBar
- Set min and max values
- Add more information
- Change density
- Change color scheme
- Accessibility
- aria-label
- aria-valuetext

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';

const A11y = () => {
  return (
    <ProgressBar
      value={4}
      min={1}
      max={5}
      aria-valuetext="Critical Error: 4 out of 5 tasks failed."
      color="critical"
    >
      <ProgressBar.Label>Critical Error</ProgressBar.Label>
      <ProgressBar.Value>4 / 5 tasks failed</ProgressBar.Value>
    </ProgressBar>
  );
};
```

```tsx
import { ProgressBar } from '@dynatrace/strato-components/content';

const A11y = () => {
  return (
    <ProgressBar
      value={4}
      min={1}
      max={5}
      aria-valuetext="Critical Error: 4 out of 5 tasks failed."
      color="critical"
    >
      <ProgressBar.Label>Critical Error</ProgressBar.Label>
      <ProgressBar.Value>4 / 5 tasks failed</ProgressBar.Value>
    </ProgressBar>
  );
};
```


### Props

Use the `ProgressBar` component to show your users that a system operation such
as downloading, uploading, or processing is progressing. The `ProgressBar` can
be used to visualize determinate or indeterminate progress.

#### ProgressBarProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `value?` | | | `'indeterminate'` | The current value.
 | `min?` | | `0` | The minimum allowed value.
 | `max?` | | `100` | The maximum allowed value.
 | `density?` | | | `'default'` | Controls the density of the rendering.
 | `color?` | | | | | | `'primary' or a container's color.` | Controls the color of the progress.
 | `'aria-valuetext'?` | | `the value of the progress as percentage.` | The aria-valuetext attribute defines the human-readable text alternative of aria-valuenow for a range widget.
By default, the value will be given as a percentage. If the value is not a percentage, you should provide aria-valuetext.
https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-valuetext

#### ProgressBar.Label

The label can be used to render any JSX above the `ProgressBar`. If you only use
text inside the label, it will automatically apply a text-ellipsis when using
the `ProgressBar` in condensed mode.

#### ProgressBarLabelProps
extends`, , `

#### ProgressBar.Icon

The icon is rendered at the top right of the `ProgressBar`. It's recommended to
only use icons as children, but you can provide any JSX.

#### ProgressBarIconProps
extends`, , `

#### ProgressBar.Value

The value is rendered underneath the `ProgressBar` and can be utilized to e.g.
show the amount of data already downloaded and the total amount of data.

#### ProgressBarValueProps
extends`, , `Still have questions?Find answers in the Dynatrace Community
- ProgressBar.Label
- ProgressBar.Icon
- ProgressBar.Value

---

## ProgressCircle

`/design/components/content/ProgressCircle/`

The `ProgressCircle` component is used to indicate the progress or completion
status of a task or process.

### Import

`tsx
import { ProgressCircle } from '@dynatrace/strato-components/content';
`

### Use cases

#### Basic ProgressCircle

If you don't provide a value to the `ProgressCircle`, it is indeterminate and
keeps looping the progress animation.

```tsx
import { ProgressCircle } from '@dynatrace/strato-components/content';

const Basic = () => {
  return <ProgressCircle />;
};
```

```tsx
import { ProgressCircle } from '@dynatrace/strato-components/content';

const Basic = () => {
  return <ProgressCircle />;
};
```


#### Determinate ProgressCircle

You can provide a value to animate the progress bar to a given position. By
default, we assume that this numeric value always reflects a percentage. If it
does not reflect a percentage value, a proper `aria-valuetext` needs to be set
see A11y. The value is clamped using the `min` and `max`
value. These are by default `0` to `100`.

```tsx
import { useEffect, useState } from 'react';

import { ProgressCircle } from '@dynatrace/strato-components/content';

const Determinate = () => {
  const [value, setValue] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setValue((prev) => (prev + 5) % 101);
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <ProgressCircle value={value} />;
};
```

```tsx
import { useEffect, useState } from 'react';

import { ProgressCircle } from '@dynatrace/strato-components/content';

const Determinate = () => {
  const [value, setValue] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setValue((prev) => (prev + 5) % 101);
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <ProgressCircle value={value} />;
};
```


#### Set min and max value

You can adjust the progress animation by setting a min value, max value, or
both. This example uses the same value as in the above example, except that the
min and max value are set differently.

```tsx
import { useEffect, useState } from 'react';

import { ProgressCircle } from '@dynatrace/strato-components/content';

const MinMax = () => {
  const [value, setValue] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setValue((prev) => (prev + 5) % 101);
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <ProgressCircle value={value} min={20} max={150} />;
};
```

```tsx
import { useEffect, useState } from 'react';

import { ProgressCircle } from '@dynatrace/strato-components/content';

const MinMax = () => {
  const [value, setValue] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setValue((prev) => (prev + 5) % 101);
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <ProgressCircle value={value} min={20} max={150} />;
};
```


#### Add more information

To display more information about the progress, you can render any JSX inside
the `ProgressCircle`.

```tsx
import { ProgressCircle } from '@dynatrace/strato-components/content';

const Compounds = () => {
  return <ProgressCircle value={75}>Downloading</ProgressCircle>;
};
```

```tsx
import { ProgressCircle } from '@dynatrace/strato-components/content';

const Compounds = () => {
  return <ProgressCircle value={75}>Downloading</ProgressCircle>;
};
```


#### Change the size

The `ProgressCircle` is also available in a smaller version.

#### Change the color scheme

The `ProgressCircle` can be rendered in different colors. You can change the
color scheme using the `color` prop.

### Accessibility

#### aria-label

If there is no string set as `children` inside the `ProgressCircle` you should
add an aria-label to explain what the progress represents.

#### aria-valuetext

If the `value` property of the `ProgressCircle` does not reflect a percentage
you need to provide more meaning for the value of the `ProgressCircle`. In that
case, you should always add an
aria-valuetext.
Additionally, if it is unclear what meaning the value of the `ProgressCircle`
conveys, you can also add the `aria-valuetext`.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Basic ProgressCircle
- Determinate ProgressCircle
- Set min and max value
- Add more information
- Change the size
- Change the color scheme
- Accessibility
- aria-label
- aria-valuetext

```tsx
import { ProgressCircle } from '@dynatrace/strato-components/content';

const A11y = () => {
  return (
    <ProgressCircle
      value={4}
      min={1}
      max={5}
      aria-valuetext="Critical Error: 4 out of 5 tasks failed"
      color="critical"
    >
      Critical Error
    </ProgressCircle>
  );
};
```

```tsx
import { ProgressCircle } from '@dynatrace/strato-components/content';

const A11y = () => {
  return (
    <ProgressCircle
      value={4}
      min={1}
      max={5}
      aria-valuetext="Critical Error: 4 out of 5 tasks failed"
      color="critical"
    >
      Critical Error
    </ProgressCircle>
  );
};
```


### Props

The `ProgressCircle` component is used to indicate the progress or completion
status of a task or process.

#### ProgressCircleProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `value?` | | | `'indeterminate'` | The current value.
 | `min?` | | `0` | The smallest allowed value.
 | `max?` | | `100` | The maximum allowed value.
 | `size?` | | | `'large'` | Controls the size of the rendered progress.
 | `color?` | | | | | | `'primary' or a container's color.` | Controls the color of the progress.
 | `'aria-valuetext'?` | | `the value of the progress as percentage.` | The aria-valuetext attribute defines the human-readable text alternative of aria-valuenow for a range widget.
Default the value as percentage will be provided. If the value is not a percentage please provide the aria-valuetext.
https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-valuetextStill have questions?Find answers in the Dynatrace Community

---

## ReleasePhaseIndicator

`/design/components/content/ReleasePhaseIndicator/`

Use the `ReleasePhaseIndicator` to communicate the release phase of a feature
(Preview, New, Deprecated).

OverviewProperties

### Import

`tsx
import { ReleasePhaseIndicator } from '@dynatrace/strato-components/content';
`

### Demo

Use the `phase` prop to control the shown release phase. The component renders a
condensed `Chip` with a preconfigured color and label.

NoteIf you need to indicate the release phase of an entire app, use the
`releasePhase` prop on the
`AppHeader.Logo`
instead.Still have questions?Find answers in the Dynatrace Community
- Import
- Demo

### Props

Use the `ReleasePhaseIndicator` to communicate the release phase of a feature
(Preview, New, Deprecated).

OverviewProperties

#### ReleasePhaseIndicatorProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `phase` | | | The release phase to display. Determines the chip label and color.Still have questions?Find answers in the Dynatrace Community

---

## Skeleton

`/design/components/content/Skeleton/`

The `Skeleton` component renders a colored block with an animated background,
indicating that something is loading.

### Import

`tsx
import { Skeleton } from '@dynatrace/strato-components/content';
`

### Use cases

#### Basic

In its most basic version, you can use the `Skeleton` as a self-closing tag,
without providing any further props. It will use up whatever space is available
in the parent container.

#### Setting the dimensions

To specify the dimensions of the `Skeleton`, you can provide the `width` and
`height` prop.

#### Changing the variant

The `Skeleton` can be rendered in different variants using the `variant` prop.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Basic
- Setting the dimensions
- Changing the variant

### Props

The `Skeleton` component renders a colored block with an animated background,
indicating that something is loading.

#### SkeletonProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `variant?` | | | `'default'` | Defines the shape of the Skeleton.
 | `width?` | [] | `100%` | Width of the Skeleton placeholder.
 | `height?` | [] | `100%` | Height of the Skeleton placeholder.Still have questions?Find answers in the Dynatrace Community

---

## SkeletonText

`/design/components/content/SkeletonText/`

The `SkeletonText` component renders a specified number of placeholder boxes for
lines of text with an animated background.

### Import

`tsx
import { SkeletonText } from '@dynatrace/strato-components/content';
`

### Use cases

#### Basic

You can use the `SkeletonText` without specifying any props. It will render a
pre-set number of lines and use up the available width in the parent container.

#### Setting the width

The `width` prop can be used to specify the width of the `SkeletonText`.

#### Setting the number of lines

To render a given amount of lines, you can utilize the `lines` prop.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Basic
- Setting the width
- Setting the number of lines

### Props

The `SkeletonText` component renders a specified number of placeholder boxes for
lines of text with an animated background.

#### SkeletonTextProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `width?` | [] | `100%` | Width of the SkeletonText placeholder.
 | `lines?` | | `3` | Number of Lines of the SkeletonText placeholder.Still have questions?Find answers in the Dynatrace Community

---

## TerminologyOverlay

`/design/components/content/TerminologyOverlay/`

Use the `TerminologyOverlay` component to define or explain unusual or technical
terms in the UI.

### Import

`tsx
import { TerminologyOverlay } from '@dynatrace/strato-components/content';
`

### Demo

`TerminologyOverlay` provides an overlay for definitions or explanations of
specific terminology in the UI. The term in the UI is marked by a dotted
underline. When the user clicks on it, an overlay with the explanation opens.
The component consists of at least two elements: a trigger and corresponding
explanation. See Usage for more details.

### Add link

If the definition is complicated, or more information would help users, you can
also include a link to further documentation.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Add link

### Props

Use the `TerminologyOverlay` component to define or explain unusual or technical
terms in the UI.

#### TerminologyOverlayProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `defaultOpen?` | | `false` | Whether the overlay is open by default
 | `children` | | | The component accepts TerminologyOverlay.Trigger, TerminologyOverlay.Description, and TerminologyOverlay.Footer as children.

### TerminologyOverlay.Description

You can use the `TerminologyOverlay.Description` component to render a helpful
description of the terminology item, rendered inside the overlay.

#### TerminologyDescriptionProps
extends`, , , `

### TerminologyOverlay.Trigger

You can use the `TerminologyOverlay.Trigger` component to render the content of
the overlay's trigger.

#### TerminologyOverlayTriggerProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `children` | | | Trigger Overlay button must contain children elements.Still have questions?Find answers in the Dynatrace Community
- TerminologyOverlay.Description
- TerminologyOverlay.Trigger

---

