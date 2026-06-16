# Typography

Strato design-system components in the **Typography** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## Blockquote

`/design/components/typography/Blockquote/`

The `Blockquote` component wraps longer text blocks and indicates that the
passage is quoted from another source.

OverviewProperties

### Import

`tsx
import { Blockquote } from '@dynatrace/strato-components/typography';
`

### Use cases

#### Provide a source

Use the optional `cite` prop to reference the source of the quotation by
providing a URL pointing to the original text or further explanation.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Provide a source

```tsx
import { Blockquote } from '@dynatrace/strato-components/typography';

const Cite = () => {
  return (
    <Blockquote cite="https://www.dynatrace.com/support/help/setup-and-configuration/dynatrace-oneagent/">
      OneAgent gives you all the operational and business performance metrics
      you need, from the frontend to the backend and everything in between—cloud
      instances, hosts, network health, processes, and services.
    </Blockquote>
  );
};
```


### Props

The `Blockquote` component wraps longer text blocks and indicates that the
passage is quoted from another source.

OverviewProperties

#### BlockquoteProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `cite?` | | | A URL that designates a source document or message for the information quoted.
This attribute is intended to point to information explaining the context for the quoted content.Still have questions?Find answers in the Dynatrace Community

---

## Code

`/design/components/typography/Code/`

Use the `Code` component to display snippets of code inline. If you want to
display a block of code, use the
`CodeSnippet`
component instead.

OverviewProperties

### Import

`tsx
import { Code } from '@dynatrace/strato-components/typography';
`

### Use cases

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases

### Props

Use the `Code` component to display snippets of code inline. If you want to
display a block of code, use the
`CodeSnippet`
component instead.

OverviewProperties

#### CodeProps
extends`, , , , , `Still have questions?Find answers in the Dynatrace Community

---

## Emphasis

`/design/components/typography/Emphasis/`

The `Emphasis` component adds visual and semantic emphasis to stressed or
essential content.

OverviewProperties

### Import

`tsx
import { Emphasis } from '@dynatrace/strato-components/typography';
`

### Use cases

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases

### Props

The `Emphasis` component adds visual and semantic emphasis to stressed or
essential content.

OverviewProperties

#### EmphasisProps
extends`, , , , , `Still have questions?Find answers in the Dynatrace Community

---

## ExternalLink

`/design/components/typography/ExternalLink/`

Use the `ExternalLink` component to link to external resources (i.e., outside
the current environment). To link to any internal resources, use the
`Link`
component instead.

### Import

`tsx
import { ExternalLink } from '@dynatrace/strato-components/typography';
`

### Use cases

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases

### Props

Use the `ExternalLink` component to link to external resources (i.e., outside
the current environment). To link to any internal resources, use the
`Link`
component instead.

#### ExternalLinkProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `href` | | | The href used for the link.
 | `onClick?` | | | Callback handler called on click.Still have questions?Find answers in the Dynatrace Community

---

## Heading

`/design/components/typography/Heading/`

Use the `Heading` to render semantic HTML heading elements (`h1`, `h2`, etc.).
The component allows you to independently define both the visual and the
semantic level of the heading.

OverviewProperties

### Import

`tsx
import { Heading } from '@dynatrace/strato-components/typography';
`

### Use cases

#### Set the visual level

To change the visual level of the `Heading` component, set the `level` property.
The visual level and the semantic level will match if not set explicitly. The
default value is `1`, which renders an `h1` tag with the highest visual
importance.

#### Polymorph to an HTML tag

Use the `as` prop to polymorph the `Heading` to the desired HTML tag
(`h1`-`h6`), which sets the semantic level independently of the visual level.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Set the visual level
- Polymorph to an HTML tag

### Props

Use the `Heading` to render semantic HTML heading elements (`h1`, `h2`, etc.).
The component allows you to independently define both the visual and the
semantic level of the heading.

OverviewProperties

#### HeadingProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `level?` | 1 | 2 | 3 | 4 | 5 | 6 | `1` | The visual level of the heading.
 | `as?` | | | | | | | `'h1'` | The polymorphed HTML tag that determines the semantic level of the heading.Still have questions?Find answers in the Dynatrace Community

---

## Highlight

`/design/components/typography/Highlight/`

Use the `Highlight` component to highlight one or more substrings within a text.

OverviewProperties

### Import

`tsx
import { Highlight } from '@dynatrace/strato-components/typography';
`

### Use cases

Render the appropriate text as children of the `Highlight` component and pass
the substring you want to highlight to the `term` prop.

#### Highlight multiple terms

To highlight multiple terms within the same `Highlight` component, pass the
substrings you want to highlight as an array to the `term` prop.

#### Enable case sensitivity

Use the `caseSensitive` prop to determine whether the search for the specified
terms should be case-sensitive.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Highlight multiple terms
- Enable case sensitivity

### Props

Use the `Highlight` component to highlight one or more substrings within a text.

OverviewProperties

#### HighlightProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `term` | | [] | | Either a substring or an array of multiple different substrings that
should be highlighted in the projected content.
Every occurrence of the string(s) is highlighted accordingly.
 | `caseSensitive?` | | `false` | Property that determines whether the highlighting search is case-sensitive.
If set to `true`, the component searches for case sensitive occurrences.Still have questions?Find answers in the Dynatrace Community

---

## Link

`/design/components/typography/Link/`

Use the `Link` component to link to any internal resources. For external
resources (i.e., outside the current environment), use the
`ExternalLink`
component instead.

### LinkImport

`tsx
import { Link } from '@dynatrace/strato-components/typography';
`

### Use cases

#### Polymorph the Link component

When linking to an internal resource, the `Link` component typically needs to be
polymorphed into a component from a routing library, such as the Link component
from the `react-router-dom` package, so that the respective API can be used.

To polymorph the `Link` component, pass the desired element to the `as` property
and provide the corresponding props.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- LinkImport
- Use cases
- Polymorph the Link component

### Props

Use the `Link` component to link to any internal resources. For external
resources (i.e., outside the current environment), use the
`ExternalLink`
component instead.

#### LinkProps

##### Signature:
`export declare type LinkProps = ;`Still have questions?Find answers in the Dynatrace Community

---

## List

`/design/components/typography/List/`

The `List` component groups a set of related content in a list and can be
arbitrarily nested. List items are preceded by either a consecutive number (for
ordered lists) or a bullet point (for unordered lists).

OverviewProperties

### Import

`tsx
import { List } from '@dynatrace/strato-components/typography';
`

### Use cases

#### Change the list type

By default, lists are unordered. To create an ordered list, you can set the
`ordered` prop. For ordered lists, it is also possible to specify the start
value of the first item in the list using the `start` prop.

#### Create nested lists

To create a nested list, simply place another `List` component as a child of the
`List` component it belongs to.

#### Change font and text style

Use the `fontStyle` and `textStyle` props to change the visual style of the used
font.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change the list type
- Create nested lists
- Change font and text style

```tsx
import { List, Text } from '@dynatrace/strato-components/typography';

const FontTextStyle = () => {
  return (
    <List fontStyle="code" textStyle="base-emphasized">
      <Text>Item 1</Text>
      <Text>Item 2</Text>
      <Text>Item 3</Text>
    </List>
  );
};
```

```tsx
import { List, Text } from '@dynatrace/strato-components/typography';

const FontTextStyle = () => {
  return (
    <List fontStyle="code" textStyle="base-emphasized">
      <Text>Item 1</Text>
      <Text>Item 2</Text>
      <Text>Item 3</Text>
    </List>
  );
};
```


### Props

The `List` component groups a set of related content in a list and can be
arbitrarily nested. List items are preceded by either a consecutive number (for
ordered lists) or a bullet point (for unordered lists).

OverviewProperties

#### ListProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `ordered?` | | `false` | Whether the List is ordered or not. This changes whether numbers or bullets are used.
 | `textStyle?` | | | | | `'base'` | Sets the text style for the List.
 | `fontStyle?` | | | `'text'` | Sets the text style for the List.
 | `start?` | | `1` | Sets the starting number of the first item in an ordered list.
The value is always treated as an integer (floor).Still have questions?Find answers in the Dynatrace Community

---

## Paragraph

`/design/components/typography/Paragraph/`

The `Paragraph` component displays a block of text with the default text style
and supports text truncation.

OverviewProperties

### Import

`tsx
import { Paragraph } from '@dynatrace/strato-components/typography';
`

### Use cases

#### Combine with other typography components

All typography components like `Strong`, `Strikethrough` or `Text` can be used
within a `Paragraph`.

```tsx
import {
  Emphasis,
  Paragraph,
  Strikethrough,
  Strong,
  Text,
} from '@dynatrace/strato-components/typography';

const Styled = () => {
  return (
    <Paragraph>
      <Strong>Dynatrace OneAgent</Strong> automatically monitors all process
      groups detected in your environment (processes running during OneAgent
      installation must be restarted{' '}
      <Strikethrough>to initiate monitoring</Strikethrough>).
      <Text as="p">
        OneAgent additionally provides <Emphasis>deep monitoring</Emphasis> for
        all processes that it can monitor at the request.
      </Text>
    </Paragraph>
  );
};
```

```tsx
import {
  Emphasis,
  Paragraph,
  Strikethrough,
  Strong,
  Text,
} from '@dynatrace/strato-components/typography';

const Styled = () => {
  return (
    <Paragraph>
      <Strong>Dynatrace OneAgent</Strong> automatically monitors all process
      groups detected in your environment (processes running during OneAgent
      installation must be restarted{' '}
      <Strikethrough>to initiate monitoring</Strikethrough>).
      <Text as="p">
        OneAgent additionally provides <Emphasis>deep monitoring</Emphasis> for
        all processes that it can monitor at the request.
      </Text>
    </Paragraph>
  );
};
```


#### Limit the number of lines

Setting the optional `maxLines` property limits the text in the `Paragraph` to
the given number of lines. When the text exceeds the set limit, it is truncated,
and an ellipsis is displayed to indicate the truncation.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Combine with other typography components
- Limit the number of lines

### Props

The `Paragraph` component displays a block of text with the default text style
and supports text truncation.

OverviewProperties

#### ParagraphProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `maxLines?` | | | Limits the text to the given number of lines and adds ellipsis if the text would need more lines.Still have questions?Find answers in the Dynatrace Community

---

## Strikethrough

`/design/components/typography/Strikethrough/`

The `Strikethrough` component renders text with a line through it. Use it to
represent things that are no longer relevant or accurate.

OverviewProperties

### Import

`tsx
import { Strikethrough } from '@dynatrace/strato-components/typography';
`

### Use cases

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases

### Props

The `Strikethrough` component renders text with a line through it. Use it to
represent things that are no longer relevant or accurate.

OverviewProperties

#### StrikethroughProps
extends`, , , , , `Still have questions?Find answers in the Dynatrace Community

---

## Strong

`/design/components/typography/Strong/`

Use the `Strong` component to render text in bold type to emphasize it.

OverviewProperties

### Import

`tsx
import { Strong } from '@dynatrace/strato-components/typography';
`

### Use cases

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases

### Props

Use the `Strong` component to render text in bold type to emphasize it.

OverviewProperties

#### StrongProps
extends`, , , , , `Still have questions?Find answers in the Dynatrace Community

---

## Text

`/design/components/typography/Text/`

Use the `Text` component for text that is rendered without any semantic markup.

OverviewProperties

### Import

`tsx
import { Text } from '@dynatrace/strato-components/typography';
`

### Use cases

#### Change font and text style

Setting the optional `textStyle` and `fontStyle` properties allows for changing
the style of the rendered text. While `textStyle` determines font weight and
size, `fontStyle` defines whether variable-width font for regular text or
monospace font for code examples is used.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change font and text style

### Props

Use the `Text` component for text that is rendered without any semantic markup.

OverviewProperties

#### TextProps

##### Signature:
`export declare type TextProps = ;`

#### TextOwnProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `textStyle?` | | | | | | Sets the text style. Variants include "base", "base-emphasized", etc.
 | `fontStyle?` | | | | Sets the font style. Can either be "text" or "code"Still have questions?Find answers in the Dynatrace Community

---

## TextEllipsis

`/design/components/typography/TextEllipsis/`

Use the `TextEllipsis` component to truncate text and show an ellipsis whenever
there is insufficient space to render the entire text. While some of our Strato
components provide ellipsis out of the box, you need to take care of this
yourself when writing your own components.

OverviewProperties

### Import

`tsx
import { TextEllipsis } from '@dynatrace/strato-components/typography';
`

### Use cases

#### Variants

Depending on the value set for the `truncationMode` prop, the `TextEllipsis`
component can truncate text at the `start`, `middle`, or `end`. It is important
to note that `start` and `end` truncation rely on the CSS `text-overflow`
ellipsis, making them more performant than the `middle` ellipsis.

```tsx
import { TextEllipsis } from '@dynatrace/strato-components/typography';

const Variants = () => {
  const text = '1 synthetic event, every 1 hour, 1/1 location unavailable';

  return (
    <div style={{ width: 200 }}>
      <TextEllipsis truncationMode="start">{text}</TextEllipsis>
      <TextEllipsis truncationMode="middle">{text}</TextEllipsis>
      <TextEllipsis truncationMode="end">{text}</TextEllipsis>
    </div>
  );
};
```

```tsx
import { TextEllipsis } from '@dynatrace/strato-components/typography';

const Variants = () => {
  const text = '1 synthetic event, every 1 hour, 1/1 location unavailable';

  return (
    <div style={{ width: 200 }}>
      <TextEllipsis truncationMode="start">{text}</TextEllipsis>
      <TextEllipsis truncationMode="middle">{text}</TextEllipsis>
      <TextEllipsis truncationMode="end">{text}</TextEllipsis>
    </div>
  );
};
```


#### Show tooltip when text overflows

To let users access the full text when it gets truncated, wrap `TextEllipsis`
inside a `Tooltip` and use the
`onTextOverflow` callback to enable the tooltip only when the text is actually
overflowing.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Variants
- Show tooltip when text overflows

### Props

Use the `TextEllipsis` component to truncate text and show an ellipsis whenever
there is insufficient space to render the entire text. While some of our Strato
components provide ellipsis out of the box, you need to take care of this
yourself when writing your own components.

OverviewProperties

#### TextEllipsisProps
extends`<>, , , , , ` |
 | Name | Type | Default | Description
 | `children` | | | The children (as text) passed to the component.
 | `truncationMode?` | | `'end'` | The mode used for truncating the text, either at the start, in the middle or at the end.
 | `onTextOverflow?` | (ellipsized: ) => | | Gets called when text needs to get truncated due to lack of horizontal space.Still have questions?Find answers in the Dynatrace Community

---

