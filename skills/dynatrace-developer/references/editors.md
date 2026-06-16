# Editors

Strato design-system components in the **Editors** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## CodeEditor

`/design/components/editors/CodeEditor/`

The `CodeEditor` provides a text input field that is specifically designed for
editing code. It further offers properties to configure e.g. syntax
highlighting, spell checks or line wrapping. Once the editor is focused via the
keyboard, the user must press "Enter" to start editing and "Escape" to quit
editing and return to the keyboard navigation flow.

### Import

`tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';
`

### Demo

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';

const Basic = () => {
  return <CodeEditor value="const text = 'hello world!'" />;
};
```

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';

const Basic = () => {
  return <CodeEditor value="const text = 'hello world!'" />;
};
```


### Set language

To enable syntax highlighting, specify the desired language with the `language`
property.

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';

const Language = () => {
  return <CodeEditor language="ts" value="const text = 'hello world!'" />;
};
```

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';

const Language = () => {
  return <CodeEditor language="ts" value="const text = 'hello world!'" />;
};
```


### Disable editing

To disable editing of the content, use the `readOnly` property.

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';

const ReadOnly = () => {
  return (
    <CodeEditor language="ts" value="const text = 'hello world!'" readOnly />
  );
};
```

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';

const ReadOnly = () => {
  return (
    <CodeEditor language="ts" value="const text = 'hello world!'" readOnly />
  );
};
```


### Enable line wrap

To enable line wrap as soon as the content overflows, use the `lineWrap`
property.

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';
import { Flex } from '@dynatrace/strato-components/layouts';

const LineWrap = () => {
  return (
    <Flex flexDirection="row">
      <Flex maxWidth="50%" flexItem>
        <CodeEditor
          language="json"
          value='{
  "alert_settings": [
    {
      "alert_id": "custom_connections_alert",
      "event_type": "AVAILABILITY_EVENT",
      "event_name": "No connections!",
      "description": "The {metricname} of {severity} is {alert_condition} the threshold of {threshold}"
    }
  ]
}'
          lineWrap
        />
      </Flex>
      <Flex maxWidth="50%" flexItem>
        <CodeEditor
          language="json"
          value='{
  "alert_settings": [
    {
      "alert_id": "custom_connections_alert",
      "event_type": "AVAILABILITY_EVENT",
      "event_name": "No connections!",
      "description": "The {metricname} of {severity} is {alert_condition} the threshold of {threshold}"
    }
  ]
}'
        />
      </Flex>
    </Flex>
  );
};
```

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';
import { Flex } from '@dynatrace/strato-components/layouts';

const LineWrap = () => {
  return (
    <Flex flexDirection="row">
      <Flex maxWidth="50%" flexItem>
        <CodeEditor
          language="json"
          value='{
  "alert_settings": [
    {
      "alert_id": "custom_connections_alert",
      "event_type": "AVAILABILITY_EVENT",
      "event_name": "No connections!",
      "description": "The {metricname} of {severity} is {alert_condition} the threshold of {threshold}"
    }
  ]
}'
          lineWrap
        />
      </Flex>
      <Flex maxWidth="50%" flexItem>
        <CodeEditor
          language="json"
          value='{
  "alert_settings": [
    {
      "alert_id": "custom_connections_alert",
      "event_type": "AVAILABILITY_EVENT",
      "event_name": "No connections!",
      "description": "The {metricname} of {severity} is {alert_condition} the threshold of {threshold}"
    }
  ]
}'
        />
      </Flex>
    </Flex>
  );
};
```


### Expand to full height

To expand the `CodeEditor` to the full available height of its parent, use the
`fullHeight` property. If you want the `CodeEditor` to respect the min-height
and max-height of the parent, use a flex container.

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';
import { Flex } from '@dynatrace/strato-components/layouts';

const FullHeight = () => {
  return (
    <Flex height={100}>
      <CodeEditor
        language="ts"
        value="const text = 'hello world!'"
        fullHeight
      />
    </Flex>
  );
};
```

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';
import { Flex } from '@dynatrace/strato-components/layouts';

const FullHeight = () => {
  return (
    <Flex height={100}>
      <CodeEditor
        language="ts"
        value="const text = 'hello world!'"
        fullHeight
      />
    </Flex>
  );
};
```


### Add default folding

To provide default folding at specific character positions in the `CodeEditor`,
use the `defaultFolding` property that accepts an array of positions.

```tsx
import { useState } from 'react';

import { CodeEditor } from '@dynatrace/strato-components/editors';

const Folding = () => {
  const [value] = useState(
    "/**\n * Example\n */\nfunction helloWorld() {\n  const message = 'hello world';\n  return message + '!';\n}\n\nconst hello = helloWorld();\nconsole.log(hello);"
  );

  return <CodeEditor language="js" value={value} defaultFolding={[22]} />;
};
```

```tsx
import { useState } from 'react';

import { CodeEditor } from '@dynatrace/strato-components/editors';

const Folding = () => {
  const [value] = useState(
    "/**\n * Example\n */\nfunction helloWorld() {\n  const message = 'hello world';\n  return message + '!';\n}\n\nconst hello = helloWorld();\nconsole.log(hello);"
  );

  return <CodeEditor language="js" value={value} defaultFolding={[22]} />;
};
```


### Change size

The CodeEditor component offers a `size` prop with `default` and `condensed`
options. The `condensed` option enables a more compact code display by
optimizing space, while the prop defaults to `default` for a regular view.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Set language
- Disable editing
- Enable line wrap
- Expand to full height
- Add default folding
- Change size

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';

const Size = () => {
  const content = `
    /**
     * Example
     */
    function helloWorld() {
      const message = 'hello world';
      return message + '!';
    }

    const hello = helloWorld();
    console.log(hello);
    `;

  return <CodeEditor language="js" value={content} size="condensed" />;
};
```

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';

const Size = () => {
  const content = `
    /**
     * Example
     */
    function helloWorld() {
      const message = 'hello world';
      return message + '!';
    }

    const hello = helloWorld();
    console.log(hello);
    `;

  return <CodeEditor language="js" value={content} size="condensed" />;
};
```


### Props

The `CodeEditor` provides a text input field that is specifically designed for
editing code. It further offers properties to configure e.g. syntax
highlighting, spell checks or line wrapping. Once the editor is focused via the
keyboard, the user must press "Enter" to start editing and "Escape" to quit
editing and return to the keyboard navigation flow.

#### CodeEditorProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `language?` | | | | | | | | | `'other'` | The language for syntax highlighting and autocompletion.
 | `id?` | | | The ID for the DOM element.
 | `value?` | | `''` | The contents of the editor.
 | `onChange?` | (value: ) => | | Callback that is called when the value in the editor changes.
 | `placeholder?` | | | Displayed initially in the editor when there is no other content.
 | `spellCheck?` | | `false` | Whether spellcheck should be enabled.
 | `fullHeight?` | | `false` | If set to true, the code editor uses the full height available in its parent.
 | `defaultFolding?` | [] | | The start indices (character position) that should be folded initially in uncontrolled scenarios.
 | `folding?` | [] | | The start indices (character position) that should be folded initially in controlled scenarios.
 | `onFoldingChange?` | (values: []) => | | Callback that is called when folding changes.
 | `readOnly?` | | `false` | Whether the input is readonly.
 | `lineWrap?` | | `false` | Whether long lines should be wrapped.
 | `onBlur?` | (e: ) => | | Callback that is called when the editor loses focus.
 | `onFocus?` | (e: ) => | | Callback that is called when the editor receives focus.
 | `gutterConfiguration?` | | | Provides the gutter configuration to display a marker next to the fold gutter.
 | `size?` | | | `'default'` | Editor layout size, 'default' for standard spacing and 'condensed' for reduced font-size, padding and margins.
 | `required?` | | `false` | If set to true, `aria-required` will be set to true on the input element.Still have questions?Find answers in the Dynatrace Community

---

## DQLEditor

`/design/components/editors/DQLEditor/`

The `DQLEditor` is specifically designed for editing DQL queries. It further
offers syntax highlighting and autocomplete functionality specific to the
Dynatrace Query Language. Once the editor is focused via the keyboard, the user
must press "Enter" to start editing and "Escape" to quit editing and return to
the keyboard navigation flow.

### Import

`tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';
`

### Demo

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';

const Basic = () => {
  return <DQLEditor value="fetch metrics | limit 100" />;
};
```

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';

const Basic = () => {
  return <DQLEditor value="fetch metrics | limit 100" />;
};
```


### Disable editing

To disable editing of the content, use the `readOnly` property.

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';

const ReadOnly = () => {
  return <DQLEditor value="fetch metrics | limit 100" readOnly />;
};
```

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';

const ReadOnly = () => {
  return <DQLEditor value="fetch metrics | limit 100" readOnly />;
};
```


### Enable linewrap

To enable linewrap as soon as the content overflows, use the `linewrap`
property.

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';
import { Flex } from '@dynatrace/strato-components/layouts';

const LineWrap = () => {
  return (
    <Flex flexDirection="row">
      <Flex maxWidth="50%" flexItem>
        <DQLEditor
          value="fetch logs
    | summarize count(), alias:`Total number of logs`, by:{bin(timestamp, 1m)}"
          lineWrap
        />
      </Flex>
      <Flex maxWidth="50%" flexItem>
        <DQLEditor
          value="fetch logs
    | summarize count(), alias:`Total number of logs`, by:{bin(timestamp, 1m)}"
        />
      </Flex>
    </Flex>
  );
};
```

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';
import { Flex } from '@dynatrace/strato-components/layouts';

const LineWrap = () => {
  return (
    <Flex flexDirection="row">
      <Flex maxWidth="50%" flexItem>
        <DQLEditor
          value="fetch logs
    | summarize count(), alias:`Total number of logs`, by:{bin(timestamp, 1m)}"
          lineWrap
        />
      </Flex>
      <Flex maxWidth="50%" flexItem>
        <DQLEditor
          value="fetch logs
    | summarize count(), alias:`Total number of logs`, by:{bin(timestamp, 1m)}"
        />
      </Flex>
    </Flex>
  );
};
```


### Expand to full height

To expand the `DQLEditor` to the full available height of its parent, use the
`fullHeight` property. If you want the `DQLEditor` to respect the min-height and
max-height of the parent, use a flex container.

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';
import { Flex } from '@dynatrace/strato-components/layouts';

const FullHeight = () => {
  return (
    <Flex height={100}>
      <DQLEditor value="fetch metrics | limit 100" fullHeight />
    </Flex>
  );
};
```

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';
import { Flex } from '@dynatrace/strato-components/layouts';

const FullHeight = () => {
  return (
    <Flex height={100}>
      <DQLEditor value="fetch metrics | limit 100" fullHeight />
    </Flex>
  );
};
```


### Query autocomplete

The `DQLEditor` supports autocomplete functionality to assist with writing DQL
queries more efficiently. Autocomplete suggestions appear automatically as you
type, or can be manually triggered using `Ctrl+Space`.

NoteIn the following example, the autocomplete suggestions are limited for
demonstration purposes. In a real-world environment, the suggestions will be
more comprehensive, depending on the query context.
CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Disable editing
- Enable linewrap
- Expand to full height
- Query autocomplete

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';

const Autocomplete = () => {
  return <DQLEditor />;
};
```

```tsx
import { DQLEditor } from '@dynatrace/strato-components/editors';

const Autocomplete = () => {
  return <DQLEditor />;
};
```


### Props

The `DQLEditor` is specifically designed for editing DQL queries. It further
offers syntax highlighting and autocomplete functionality specific to the
Dynatrace Query Language. Once the editor is focused via the keyboard, the user
must press "Enter" to start editing and "Escape" to quit editing and return to
the keyboard navigation flow.

#### DQLEditorProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `id?` | | | The ID for the DOM element.
 | `'data-testid'?` | | `'dql-editor'` | Test id used for matching the editor container.
 | `value?` | | `''` | The value (i.e. contents) of the editor.
 | `onChange?` | (value: ) => | | Handler that is called when the value changes.
 | `placeholder?` | | | Displayed initially in the editor when there is no other content.
 | `spellCheck?` | | `false` | Whether spellcheck should be enabled.
 | `fullHeight?` | | `false` | If set to true, the DQL editor uses the full height available in its parent.
 | `defaultFolding?` | [] | | The start indices (character position) that should be folded initially in uncontrolled scenarios.
 | `folding?` | [] | | The start indices (character position) that should be folded initially in controlled scenarios.
 | `onFoldingChange?` | (values: []) => | | Callback that is called when folding changes.
 | `readOnly?` | | `false` | Whether the input is readonly
 | `lineWrap?` | | `false` | Whether long lines should be wrapped.
 | `onBlur?` | (e: ) => | | Callback that is called when the editor loses focus.
 | `onFocus?` | (e: ) => | | Callback that is called when the editor receives focus.
 | `onValidationStart?` | () => | | Callback fired when DQL validation starts.
This can be used for setting a status that validation is in progress.
 | `onValidationEnd?` | (validityInfo: []) => | | Callback fired when DQL validation ends.
This can be used for resetting a status that validation is in progress and to get the validation result.
 | `onValidityChange?` | (validityInfo: []) => | | Callback fired when new diagnostic information is available.
This can be used to get the validation result from outside the editor.
 | `size?` | | | `'default'` | Editor layout size, 'default' for standard spacing and 'condensed' for reduced font-size, padding and margins.
 | `required?` | | `false` | If set to true, `aria-required` will be set to true on the input element.Still have questions?Find answers in the Dynatrace Community

---

