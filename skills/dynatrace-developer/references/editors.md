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

### Set language

To enable syntax highlighting, specify the desired language with the `language`
property.

### Disable editing

To disable editing of the content, use the `readOnly` property.

### Enable line wrap

To enable line wrap as soon as the content overflows, use the `lineWrap`
property.

### Expand to full height

To expand the `CodeEditor` to the full available height of its parent, use the
`fullHeight` property. If you want the `CodeEditor` to respect the min-height
and max-height of the parent, use a flex container.

### Add default folding

To provide default folding at specific character positions in the `CodeEditor`,
use the `defaultFolding` property that accepts an array of positions.

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

### Disable editing

To disable editing of the content, use the `readOnly` property.

### Enable linewrap

To enable linewrap as soon as the content overflows, use the `linewrap`
property.

### Expand to full height

To expand the `DQLEditor` to the full available height of its parent, use the
`fullHeight` property. If you want the `DQLEditor` to respect the min-height and
max-height of the parent, use a flex container.

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

