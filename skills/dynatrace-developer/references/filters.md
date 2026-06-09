# Filters

Strato design-system components in the **Filters** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## FilterBar

`/design/components/filters/FilterBar/`

FilterBar helps users easily filter datasets using one or more filter criteria.
A range of form elements can be added as filter controls.

### Import

`tsx
import { FilterBar } from '@dynatrace/strato-components/filters';
`

### Demo

`FilterBar` is designed for filtering with multiple controls. This example shows
a `FilterBar` with a `TextInput`, a single `Select`, a multi-select `Select`,
and a `TimeframeSelector`. See Usage for best practices.

### Give items unique names

The name provided to the `FilterBar.Item` must be unique to initialize the
`defaultValue` correctly. This is true even if the item is rendered
conditionally. If the same `name` is used for two items, React will map the
`name` of the new item to the old `defaultValue`.

`tsx
{conditionalFilter ? ( ) : ( )}
`

### Filter text

Use the `SearchInput` within the `FilterBar` for searching accross fields (e.g.,
multiple columns). Only one `SearchInput` should be used per `FilterBar`. Use
the `TextInput` for targeted, text-based filtering (e.g., for one specific
column). This allows users to narrow down results by entering keywords or
phrases.

### Reset filter values

This example shows how to reset filter item values in controlled scenarios. The
`FilterBar.ResetButton` depends on an `onClick` hander to reset the filter
values. Therefore, the reset button can only be used with controlled `FilterBar`
components.

### Prefill additional filters

If you know the most likely value for an additional, or secondary, filter, you
can help users by setting it as the `defaultValue`.

The user can override the `defaultValue`, but if the filter is removed and
reapplied, it will revert to the `defaultValue`.

To make the changed value persist, the `value` property should be used instead.
In this way, the changed value is saved, even if the filter is removed. (The
`value` is no longer considered for the filtering.)

### Render filtered data in a table

Connect `FilterBar` with `DataTable` with the `useFilteredData` hook. To filter
the data in the table, pass the unfiltered data as the first argument to the
hook. The `useFilteredData` hook returns the `filteredData` that must be passed
to the table's `data` prop along with the `onChange` handler which can be
plugged into the `onFilterChange` callback.

By default, the filter name must match the column name. If a custom filter logic
is required, provide a filter function as the second argument. This example
shows a custom filter function that searches for a match in every column of a
row.

### Persist sorting of filtered data

When using the `useFilteredData` hook to filter table data, the table must
re-render each time the `filteredData` changes, which also resets the sorting.
To keep the sorting, use the `sortBy` and `onSortChange` props along with
`enableDefaultSort`.

### Filter sub-row data

The `useFilteredData` hook can also handle filtering of table data with
sub-rows.

By default, on the matching paths, the sibling rows are also displayed for easy
comparison. In other words, when a child matches, other children at the same
level are also included (on all levels of the matching path). Control this
behavior using the `subrowMatchingBehavior` parameter, to include or exclude
those sibling rows.

For nodes which match, all of their sub-rows are included irrespective of
`subrowMatchingBehavior`.

The return value `expandedRowIds` provides all the IDs of ancestors of matching
nodes. Feed those values to `openSubRows` of the `DataTable` to ensure matching
nodes are visible.

### Pin and unpin optional filters

Important filters should always be visible. However, you can allow users to hide
uncommon, optional filters in the 'Add filter' dropdown. Pass the configuration
object `defaultPinnedState` to the `FilterBar` to set filter states, as follows:

`pinned` items are always visible and can't be unpinned or hidden by the user.

`pinned-optional` items are visible initially, but the user can unpin and hide
them in the dropdown.

`optional` items aren't visible initially, but the user can access them from
the dropdown and pin them. When a filter item is pinned, it's automatically
focused.

Filter items that aren't configured will default to `pinned`.

Dropdown items use the text content of the label, stripping away all other
content. Be sure to add an aria-label or name for each pinned-optional and
optional filter, as these are required for the dropdown. If there's no text
content, the `aria-label` or the `name` will be used as a fallback.

### Control pinned state

To control the pinned state of filter items, pass the pinned state configuration
to the `pinnedState` prop. To handle changes in the 'Add filter' dropdown,
provide a callback to the `onPinnedStateChange` prop. The callback triggers
whenever different items are selected, receiving the suggested pinned state and
a list of item names.

### Use custom component

To use a custom component as a `FilterBar.Item`, use the React
forwardRef. Forward the ref to
the wrapper element and add the following contract props:

`value` if the component is controlled. The `onChange` callback is also
required.

`defaultValue` if the component is uncontrolled. The ref is required to focus
or open items from additional filters in the dropdown. This means that you
must also use the imperative handle in your component to expose the ref of
your input element.

Be sure to add an `aria-label` or `name` for each custom component. If there's
no text content, the `aria-label` or `name` will be used as a fallback.

### Related

#### Patterns

FilteringStill have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Give items unique names
- Filter text
- Reset filter values
- Prefill additional filters
- Render filtered data in a table
- Persist sorting of filtered data
- Filter sub-row data
- Pin and unpin optional filters
- Control pinned state
- Use custom component
- Related
- Patterns

### Props

FilterBar helps users easily filter datasets using one or more filter criteria.
A range of form elements can be added as filter controls.

#### FilterBarProps

##### Signature:
`export declare type FilterBarProps = ( | ) & ;`

### FilterBar.Item

You can use the `FilterBar.Item` component to render an item inside the
`FilterBar`, as shown above.

#### FilterBarItemProps
extends`, , ` |
 | Name | Type | Default | Description
 | `name` | | | A unique identifier for this sub-filter (must only be unique for this filter). In case custom labels are used without text children, this is displayed on the MoreMenu trigger instead.
 | `label` | | | Description text of this sub-filter. If you use a custom label without text children, the name will be displayed on the MoreMenu instead.
 | `children` | <> | | Only one element, is expected here.
 | `showLabel?` | | | Defines if the label is shown for the filter item. If set specifically, it also overwrites the general configuration set with the showLabels prop on the FilterBar for one item.

### FilterBar.ResetButton

You can use the `FilterBar.ResetButton` component to render a button that resets
all filters, as shown above.

#### ResetButtonProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `onClick` | () => | | Handler that is called when the ResetButton is clicked.Still have questions?Find answers in the Dynatrace Community
- FilterBar.Item
- FilterBar.ResetButton

---

## FilterField

`/design/components/filters/FilterField/`

`FilterField` is an advanced, text-based filtering component. It supports
complex data filtering with intuitive filter field syntax and auto-suggestions.

### Import

`tsx
import { FilterField } from '@dynatrace/strato-components/filters';
`

### Demo

`FilterField` uses a simple and intuitive
filter field syntax.
When the user begins to type, a dropdown with suggestions for the next key,
value, or operator appears. See Usage for best practices to
implement the component.

### Validate user input

To validate user input, set restrictions for keys, comparison operators, and
values using the `validatorMap` property. `FilterField` will highlight errors
and show appropriate suggestions in the suggestions overlay as long as the
`autoSuggestions` property of the `FilterField` is set to `true`.

### Define valid keys

You can define a list of keys in the `validatorMap` property to be interpreted
as valid. For any keys that aren't in the list, `FilterField` will show an
error. By setting the `exhaustive` property of `validatorMap` to `false`, users
can enter any key without triggering an error.

### Define key types

You can set one or multiple types for `FilterField` keys and thus restrict the
list of comparison operators and values that will be accepted. Set the
`valueType` property on a `FilterFieldKeySuggestionConfig` in the
`keyPredicates` array. The type must be set for each key individually. The type
can't be set for all keys globally.

To overwrite the type restriction of a comparison operator, set the allowed
comparison operators for that key.

Available types and their comparison operators are:

 |
 | Type | Comparison operators
 | `Any` | `equals`, `not-equals`, `less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `in`, `not in`, `exists`, `not-exists`
 | `Boolean` | `equals`, `not-equals`, `exists`, `not-exists`
 | `Duration` | `equals`, `not-equals`, `less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `in`, `not in`, `exists`, `not-exists`
 | `Number` | `equals`, `not-equals`, `less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `in`, `not in`, `exists`, `not-exists`
 | `String` | `equals`, `not-equals`, `in`, `not in`, `exists`, `not-exists`, `starts-with`, `not-starts-with`, `ends-with`, `not-ends-with`, `contains`, `not-contains`

### Define values for keys

For any key in the `validatorMap` property, you can define a list of values that
are valid by passing an array to the `valuePredicate`. `FilterField` will return
an error for any value that isn't on the list.

If, in addition to a list of values, you pass a key type as a `valuePredicate`,
`FilterField` will accept any value that is in the list and of that key type.

### Additional and custom types

In addition to the built-in types (`Number`, `String`, `Boolean`, `Duration`,
`JSONPath`, `IPAddress`, `UID`, `Timestamp`, `SmartscapeId`), you can register
custom types using the `customTypes` prop. Custom types let you define
domain-specific validation logic and can be referenced in the `validatorMap`
just like built-in types by using `{ type: 'CustomTypeName' }` in the
`valuePredicate`.

Each custom type requires a validation function that returns `true` when a value
is valid for that type. Optionally, you can provide an icon to display in the
suggestions overlay.

### Suggestion Ordering

By default, key and value suggestions from the `validatorMap` are sorted
alphabetically for string values, numerically in ascending order for numbers,
and by unit order (smallest to largest, e.g. `ns`, `ms`, `s`, `m`, `h`) then
numerically within the same unit for durations. When the user types, suggestions
are reordered by match relevance: exact matches appear first, followed by
starts-with, and then contains or ends-with matches. Within each relevance tier,
alphabetical or ascending order is preserved.

To preserve the original order defined in `keyPredicates` and `valuePredicate`,
set `sortSuggestions: false` on the `validatorMap`. Relevance-based sorting when
the user is typing remains active regardless of this setting.

### Suggest full statements when typing values

Complete filter statements (key, operator, value) can be suggested automatically
based on typed input. This allows users to type a value like `error` and
immediately see suggestions like `status = error` without needing to know the
key name first.

To enable this feature, add `suggestStatementOnValueMatch` to the key predicate
in your `validatorMap`. The property accepts either:

- `true` — Enables statement suggestions for all values defined in the
`valuePredicate` array (suggestions are displayed for exact matches,
starts-with, ends-with, and contains matches)

- A function — A custom match function that receives the current token and
returns `true` if a statement suggestion should be shown

Statement suggestions always use the `=` (equals) comparison operator. If
multiple keys have the same value configured, suggestions for all matching keys
will be shown.

### Define fallback keys for free-text search

The `fallbackKey` property allows you to define commonly used keys that generate
suggestions using the currently typed token as the value. This is useful when
you want users to search within specific fields without knowing the exact key
name.

To enable this feature, add `fallbackKey` to the key predicate in your
`validatorMap`. The property accepts either:

- `true` — Generates statement suggestions using the `matches-phrase` (`~`)
operator

- An array of comparison operators — Generates one statement suggestion for each
specified operator

When a user starts typing in an empty `FilterField`, suggestions like
`content ~ typed-value` are shown, allowing quick searches in common fields.

The difference to `suggestStatementOnValueMatch` is that `fallbackKey` uses the
currently typed token as the value regardless of whether it matches predefined
values, while `suggestStatementOnValueMatch` only suggests statements when the
typed value matches values defined in the `valuePredicate`.

### Add display labels and descriptions to suggestions

You can enrich key and value suggestions from the `validatorMap` with a
`displayValue` (a human-readable label shown instead of the raw value) and
`details` (a secondary description). Both are optional and only affect the
suggestion overlay — they have no effect on validation or the applied filter
value.

For keys — add `displayValue` and `details` directly to the
`FilterFieldKeySuggestionConfig` object in `keyPredicates`.

For values — replace string, number, boolean, or duration entries in
`valuePredicate` with a `FilterFieldRichValuePredicate` object. Set `value` to
the actual filter value that gets applied. `displayValue` and `details` are
optional.

### Group key suggestions

Key suggestions from the `validatorMap` can be organized into labeled groups
using `FilterFieldKeySuggestionGroupConfig` objects in the `keyPredicates`
array.

The `keyPredicates` property accepts an array of key names (strings),
`FilterFieldKeySuggestionConfig` objects, or
`FilterFieldKeySuggestionGroupConfig` objects. The array format is required to
use key suggestion groups.

### Group value suggestions

Value suggestions for a key can be organized into labeled groups by replacing
string or number entries in `valuePredicate` with
`FilterFieldValueSuggestionGroupConfig` objects.

### Specify validation logic

To validate a value according to a particular logic, pass a validator function
to the `valuePredicate`. This allows you to write a custom error message in case
of an error. You can also use this approach to check whether a value follows a
particular pattern.

Make sure to pass only pure or cached functions and avoid calling
`convertStringToFilterFieldTree` in combination with a `validatorMap` inside of
the validator function, as this may cause infinite loops.

### Define comparison operators

The `validatorMap` property lets you define a list of comparison operators
globally (for all keys) or individually (per key). For any comparison operator
that isn't defined in the list, `FilterField` will show an error.

If you define comparison operators globally, be aware that the key types may
also narrow down the list of allowed comparison operators. If you define
comparison operators specifically for a key, they will overwrite restrictions
set by the type of the key.

### Work with syntax tree

`FilterField` provides a tokenized version of the entered value and groups
statements that are connected by the same logical operator. As the logical `AND`
takes precedence over the logical `OR`, the statements `a = 1 b = 2 OR c = 3`
will be grouped as follows:

Each statement is represented by a node holding the key, operator, and value of
the statement, provided as properties of the statement node. Depending on the
type of value and operator used, additional information (e.g. `starts-with`,
`contains`) is provided in the syntax tree.

If there is an error in the syntax, a node with type `Error` is included in the
syntax tree and the accompanying `isValid` flag is set to `false`.

#### Explicit logical operator nodes

Explicit logical operators are included in the syntax tree so it can be
converted back into a string without losing information. The logical operator
needed to evaluate a group of statements is included on the `Group` node. Ignore
logical operators in the `children` array of groups.

#### Convert string to syntax tree

Use the `convertStringToFilterFieldTree` utility to convert a string into a
`FilterTree`. Setting the value programmatically doesn't trigger the `onChange`
callback. Use the provided utility function for the converted syntax tree and
filter data.

#### Convert syntax tree to string

Use the `convertFilterFieldTreeToString` utility to convert a syntax tree to a
string.

CautionWe can't guarantee that converting a string to a tree and back yields the exact
same result. The `value` of every node (except for `Error` nodes) doesn't
contain escape characters (both wrapping doublequotes and backslashes). Hence,
the simple value `foo` may be written `"foo"`, `\f\o\o`, or using any other
combination of escape characters. With the `textValue` of tree nodes being
optional for the conversion util input, it is impossible to re-build the exact
same string as the original input for certain trees unless the `textValue` is
included.
This example demonstrates the conversion from string to tree, and back:

### Customize comparison operator suggestions

With the `autoSuggestions` prop set to true, relevant operator suggestions are
added automatically. To customize the suggestions, omit `autoSuggestions` and
use the returned `autoSuggestions` in the `onSuggest` callback. The `onSuggest`
callback provides the information you need to determine which suggestions to
show.

### Escape characters in suggestions

`FilterField` uses `space` as a delimiter between keys, comparison operators,
values, and statements. Learn the
filter field syntax.

To avoid invalid syntax when suggestions are applied, use the `value` prop and
the children of the `FilterField.Suggestion` component. The `value` is used to
apply the suggestion, while the `children` are used to render the suggestion in
the overlay.

In general, the following characters need to be escaped, either by wrapping the
whole value in double quotes, or by using a `\` to escape single characters:

- Asterisk

- , Comma

- () Parentheses

- ! Exclamation

- Angles

- = Equals

- " Quote

- $ Dollar sign

- : Colon

- [] Brackets

- ~ Tilde

When the insertion strategy for suggestions is set to `replace-token`, the
applied value is automatically escaped, if needed.

The following examples are also valid for keys:

- Exact match of comparison operator

- `foo = \=`

- `foo = \

- `foo = ">"`

- `foo = "!="`

- Starts with / ends with operator in value

- `foo = *"ba*r"` (ends with `ba*r`)

- `foo = ba\*r*` (starts with `ba*r`)

- `foo = *"ba*r"*` (contains `ba*r`)

- Space in value

- `foo = "b a r"`

- `foo = b\ ar`

#### Programmatically escape suggestion values

The `escapeFilterFieldSuggestion` utility allows you to escape suggestion
values. This is the same function applied internally by the `FilterField`,
making it ideal for verifying that manually escaped values match the expected
format.

### Group suggestions

If there are many suggestions that fit into different categories, you can use
`FilterField.SuggestionGroup` to separate them visually. Use the
`FilterField.SuggestionGroupLabel` to add short labels above the groups.

### Load suggestions async

To load suggestions async and display a loading state in the suggestions
overlay, set the `loading` prop on `FilterField.Suggestions`.

### Limit suggestions shown

To limit the number of default suggestions rendered, provide the
`defaultSuggestionsCount` config. You can set limits for an empty and a filled
`FilterField`.

If the suggestions exceed the limit, a show more / less button will be rendered
to expand / collapse the remaining suggestions.

### Persist recent and pinned filters

To enhance user experience and streamline workflows, `FilterField` supports
persisting recent and pinned filters across sessions. This feature stores
user-defined filters in the Dynatrace platform's `userAppState`, allowing users
to quickly reapply commonly used filters.

To enable this feature, set the `filterNamespace` prop on the `FilterField`
component. This string value acts as a unique identifier for the storage scope.
Filters are persisted per user and namespace, ensuring isolation between
different use cases or components under the keys
`strato-FilterField-pinnedFilters-{filterNameSpace}` and
`strato-FilterField-recentFilters-{filterNameSpace}`.

CautionIf your application uses namespaced recent and pinned filters that are no longer
relevant or supported, it is your responsibility to explicitly clean them up in
the application code. The system does not automatically remove unused namespaces
from the userAppState.

### Use the FilterField in a form

The user can submit a filter statement using `Enter` or `Ctrl / Cmd + Enter`.
This triggers the `onFilter` callback, which provides the string representation
of the value, the syntax tree, and its validity state. Clearing the
`FilterField` also triggers the `onFilter` callback.

`FilterField` can be displayed in a form. By default, the form shows a set of
error messages based on the entered value, rendered as tooltips. Use the
`FormField` to make the error state visible and add an error message beneath the
`FilterField`. Learn about using the `FormField`
here.

To provide the same functionality for pointer users, add a dedicated button next
to the `FilterField`, as outlined in Usage.

### Variables

Variables are a default feature of every `FilterField`. Any value starting with
`$` is automatically interpreted as a variable and returned as type `Variable`
in the value node.

Use the `validatorMap` to allow only specific variables or variable patterns.

### Enable matches phrase (~)

To enable matches phrase comparison operators (`~` and `!~`), provide a
`validatorMap` with `matches-phrase` or `not-matches-phrase` in the list of
allowed operators. You can enable comparison operators globally, for all keys at
once, or for individual keys. Matches phrase comparison operators are compatible
with keys of the type `Any` and `String`, or any type that you list as an
allowed comparison operator for a key.

For details on mapping `matches-phrase` and `not-matches-phrase` to a DQL
command, and when to use different comparison operators, see the documentation
on translation to DQL.

### Enable search (* ~)

To enable the search operator (`* ~`), set `searchConversion: true` in the
`parserConfig` prop. While the matches phrase comparison operator is used to
search in a specific field, the search operator is used to look for matches in
the whole record.

For details on mapping `search` to a DQL command, and when to use different
comparison operators, see the documentation on
translation to DQL.

### Enable JSONPath filtering

JSONPath filtering lets users target nested JSON data using JSONPath
expressions. To enable JSONPath filtering, set `jsonPathConversion: true` in the
`parserConfig` prop and add `{ type: 'JSONPath' }` to the `valuePredicate` array
in your validator map. You can combine JSONPath with other types, such as
`{type: Number}` or specific values, for flexible filtering. When combined, the
filter key appears twice in the suggestions: once with `$.` notation for
JSONPath, and once without for the expected type.

### Change insertion strategy

`FilterField` uses
filter field syntax
to parse the user's input and transform it into tokens. Each token represents a
filter key, value, comparison operator, or logical operator.

By default, applying a suggestion replaces the token that the cursor is
currently positioned on with the value of the suggestion. Use the
`insertionStrategy` prop to alter the behavior.

The following replacement strategies are supported:

 |
 | Strategy | Behavior
 | `replace-token` (default) | Replace the token at the cursor position.
 | `replace-statement` | Replace the whole statement at the cursor position.
 | `replace-all` | Replace the whole filter.
 | `insert` | Insert at the cursor position without any replacements.

### React to pasted content

To react to pasted content, implement an `onSuggest` callback and check whether
`pastedContent` is included in the provided suggestion types. When it is, you
can offer suggestions based on the pasted content, optionally using insertion
strategies like `replace-statement` or `replace-all` to turn the raw pasted
content into a full statement.

### Map FilterField syntax to DQL

To ensure predictable and consistent behavior for end users, map FilterField
syntax to
Dynatrace Query Language (DQL)
using these equivalents:

 |
 | FilterField syntax | DQL equivalent
 | `=` | `matchesValue(key, "value")`
 | `!=` | `not matchesValue(key, "value")`
 | | `>`
 | `>=` | `>=`
 | `= *` | `isNotNull()`
 | `!= *` | `isNull()`
 | `AND` | `and`
 | `OR` | `or`
 | `in` | `matchesValue(key, array("value1", "value2"))`
 | `not in` | `not matchesValue(key, array("value1", "value2"))`
 | `*value` | `matchesValue(key, "*value")`
 | `value*` | `matchesValue(key, "value*")`
 | `*value*` | `matchesValue(key, "*value*")`
 | `~` | `matchesPhrase(key, "*value*")`
 | `!~` | `not matchesPhrase(key, "*value*")`
 | `* ~` | `search "value"`

### Related

#### Patterns

- Filtering

#### Documentation

- Filter field

- Filtering and sorting
Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Validate user input
- Define valid keys
- Define key types
- Define values for keys
- Additional and custom types
- Suggestion Ordering
- Suggest full statements when typing values
- Define fallback keys for free-text search
- Add display labels and descriptions to suggestions
- Group key suggestions
- Group value suggestions
- Specify validation logic
- Define comparison operators
- Work with syntax tree
- Explicit logical operator nodes
- Convert string to syntax tree
- Convert syntax tree to string
- Customize comparison operator suggestions
- Escape characters in suggestions
- Programmatically escape suggestion values
- Group suggestions
- Load suggestions async
- Limit suggestions shown
- Persist recent and pinned filters
- Use the FilterField in a form
- Variables
- Enable matches phrase (~)
- Enable search (* ~)
- Enable JSONPath filtering
- Change insertion strategy
- React to pasted content
- Map FilterField syntax to DQL
- Related
- Patterns
- Documentation

### Props

`FilterField` is an advanced, text-based filtering component. It supports
complex data filtering with intuitive filter field syntax and auto-suggestions.

#### FilterFieldProps

##### Signature:
`export declare type FilterFieldProps = > & {
 /**
 * Placeholder text displayed when the filter field is empty.
 * @defaultValue
 */
 placeholder?: ;
 /**
 * Whether the automatically determined suggestions (logical / comparison operators) should be shown.
 * If set to true, the suggestions will automatically be added to the suggestions overlay.
 * @defaultValue false
 */
 autoSuggestions?: ;
 /**
 * The of default suggestions rendered before showing a button.
 * Set to -1 to always render all the available suggestions.
 * You can specify different counts for when the input is empty and when the user has typed something.
 * @defaultValue \{ empty: 5, filled: 10 \}
 */
 defaultSuggestionsCount?: {
 empty?: ;
 filled?: ;
 } | ;
 /**
 * Callback triggered when the suggestions may need to be updated.
 * @defaultValue
 */
 onSuggest?: ;
 /**
 * Callback triggered when the user submits the currently entered filter for filtering.
 * @defaultValue
 */
 onFilter?: (filterState: {
 /** The current value of the filter field. */
 value: ;
 /** Syntax tree of the current value. */
 syntaxTree: ;
 /** Whether the current value is valid. */
 isValid: ;
 }) => ;
 /**
 * Custom types to restrict allowed values in the validator map.
 * Keys are type names that can be used in the validatorMap, values are validation functions.
 * @example
 * `tsx
 *
 * `
 */
 customTypes?: ;
 /** Validators to restrict allowed keys and their operators. */
 validatorMap?: ;
 /** Config to enable new nodes in the . */
 parserConfig?: {
 /**
 * Whether search operators are enabled in the filter field. If set to false,
 * they will be marked as error and returned accordingly in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the SearchOperator node will be returned by default
 */
 searchConversion?: ;
 /**
 * Whether a key will be converted to a JSONPath node if a JSONPath is entered in the FilterField.
 * If set to false, they will be marked as error and returned accordingly in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the jsonPathConversion will be enabled by default
 */
 jsonPathConversion?: ;
 /**
 * Whether a value will be converted to an IPAddress node if an IPAddress is entered in the FilterField.
 * If set to false, they will be returned as a node in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the ipAddressConversion will be enabled by default
 */
 ipAddressConversion?: ;
 /**
 * Whether a value will be converted to a UID node if a UID is entered in the FilterField.
 * If set to false, they will be returned as a node in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the uidConversion will be enabled by default
 */
 uidConversion?: ;
 /**
 * Whether a value will be converted to a Timestamp node if a Timestamp is entered in the FilterField.
 * If set to false, they will be returned as a node in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the timestampConversion will be enabled by default
 */
 timestampConversion?: ;
 /**
 * Whether a value will be converted to a SmartscapeId node if a SmartscapeId is entered in the FilterField.
 * If set to false, they will be returned as a node in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the smartscapeIdConversion will be enabled by default
 */
 smartscapeIdConversion?: ;
 };
 /**
 * Namespace identifying the used key for the recent and saved filters storage.
 * Defaults currently to and will default to with the next breaking change.
 * Set the value to if you want to opt out of the recent and saved filters api.
 * @defaultValue
 *
 */
 filterNamespace?: | ;
}>;`

### FilterField.Suggestions

The `FilterField.Suggestions` component to render a list of suggestions is
optional, but can be used to set options specific to the suggestions.

#### FilterFieldSuggestionsProps

##### Signature:
`export declare type FilterFieldSuggestionsProps = & & & & {
 /** Whether the suggestions are loading. If true, a loading indicator is shown and otherwise the suggestions are shown. */
 loading?: ;
};`

### FilterField.Suggestion

Use the `FilterField.Suggestion` component for each suggestion list entry.

#### FilterFieldSuggestionProps

##### Signature:
`export declare type Props = ;`

### FilterField.SuggestionDetails

Use the `FilterField.SuggestionDetails` component inside a
`FilterField.Suggestion` to provide additional information.

#### FilterFieldSuggestionDetailsProps

##### Signature:
`export declare type FilterFieldSuggestionDetailsProps = & & & ;`

### FilterField.SuggestionGroup

Use the `FilterField.SuggestionGroup` to add separators between groups of
related suggestions.

#### FilterFieldSuggestionGroupProps

##### Signature:
`export declare type Props = ;`

### FilterField.SuggestionGroupLabel

To label a set of grouped suggestions, use the
`FilterField.SuggestionGroupLabel` component.

#### FilterFieldSuggestionGroupLabelProps

##### Signature:
`export declare type FilterFieldSuggestionGroupLabelProps = & & & & ;`Still have questions?Find answers in the Dynatrace Community
- FilterField.Suggestions
- FilterField.Suggestion
- FilterField.SuggestionDetails
- FilterField.SuggestionGroup
- FilterField.SuggestionGroupLabel

---

## SegmentSelector

`/design/components/filters/SegmentSelector/`

`SegmentSelector` is a top-level filter component that filters data by segments,
setting the scope for additional filters.

### Import

`tsx
import { SegmentSelector } from '@dynatrace/strato-components/filters';
`

### Demo

`SegmentSelector` lets users filter data from specific datasets called
Segments. The
`useSegments` hook provides access to the selected values. See
Usage for best practices.

### Set the scope

Use the `SegmentsProvider` to restrict the scope of one or more
`SegmentSelector` components. This will apply only those segments within a given
scope and ignore any globally-set segments.

The `SegmentsProvider` accepts default segments as well and filters out any
faulty segments. If the default selection should apply to all `SegmentsSelector`
components, place the `SegmentsProvider` at a high level. For example, right
after the `AppRoot`.

### Configure segments programmatically

The `useSegments` hook provides the following helper functions to
programmatically configure selected segments:

 |
 | Function | Description
 | `addSegment` | Adds one segment to the selection. If the segment is unavailable, it won't be added to the selection.
 | `removeSegment` | Removes one segment from the selection.
 | `removeAllSegments` | Removes all segments from the selection.
 | `setSegments` | Overrides all currently applied segments. Similarly to `addSegment`, `setSegments` checks the availability of each segment.

### Show private and outdated segments

Users can share private segments with other users, for example, through a link.
If the recipient removes a private segment from their view, it will not be
visible to them any longer. However, they can access the private segment once
more by re-opening the link.

Outdated segments remain visible in the segments array but are marked as
`unavailable`.

### Customize trigger

`SegmentSelector` comes with a default trigger to ensure a consistent user
experience. In exceptional cases, if necessary, it's possible to override the
default trigger.

Props are automatically applied with the custom trigger we provide to ensure
correct semantics. The `SegmentSelector.CustomTrigger` accepts a render function
with two objects as arguments:

- The first object provides access to the default `displayValue` and the
`isLoading` state.

- The second object provides all the trigger props necessary for the trigger
button to function.

If you override the default trigger, make sure to spread the props to the
trigger element to tie interactions back to the `SegmentSelector`. This enables
you to customize the trigger component, while leveraging the internal logic of
the `SegmentSelector` component.

### Related

#### Patterns

- Filtering

#### Documentation

- Segments
Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Set the scope
- Configure segments programmatically
- Show private and outdated segments
- Customize trigger
- Related
- Patterns
- Documentation

### Props

`SegmentSelector` is a top-level filter component that filters data by segments,
setting the scope for additional filters.

#### SegmentSelectorProps

##### Signature:
`export declare type SegmentSelectorProps = & & & & & & & {
 /**
 * Configures the style of the trigger.
 * @defaultValue 'default
 */
 variant?: | ;
 /** Callback that is triggered when the open state of the SegmentSelector's overlay changes its open state. */
 onOpenChange?: (isOpen: ) => ;
};`

#### useSegments

#### useSegments

##### Signature:
`export declare const useSegments: () => {
 segments: FilterSegment[];
 addSegment: (segment: FilterSegment) => Promise;
 removeSegment: (id?: | ) => ;
 removeAllSegments: () => ;
 setSegments: (segments: FilterSegment[], force?: ) => Promise<>;
};`

#### SegmentSelector.CustomTrigger

#### SegmentSelectorCustomTriggerProps

##### Signature:
`export declare type SegmentSelectorCustomTriggerProps = & & & {
 /** Elements to be displayed in the CustomTrigger. */
 children: | ((customTriggerProps: {
 displayValue: ;
 isLoading: ;
 }, props: ( & & (>> & )) | ) => );
};`Still have questions?Find answers in the Dynatrace Community
- useSegments
- SegmentSelector.CustomTrigger

---

## TimeframeSelector

`/design/components/filters/TimeframeSelector/`

`TimeframeSelector` is a filtering component that lets users choose from preset
timeframes or add unique "from" and "to" time values of their own.

### Import

`tsx
import { TimeframeSelector } from '@dynatrace/strato-components/filters';
`

### Demo

`TimeframeSelector` takes its information from the user's Dynatrace user
settings. The timezone setting determines the timezone offset in
`TimeframeSelector`, while the region setting determines its display format.
Both the timezone and the region can be set independently. If either is set to
"use browser default," `TimeframeSelector` will fall back to the user's browser
settings for that value. The value passed to the `onChange` is converted back to
an ISO string or passed as an expression. See Usage for best
practices.

### Control state

`TimeframeSelector` can be controlled, meaning that you can handle the selection
state. To do so, use the `onChange` prop to provide a handler to be called when
the internal state changes. You must assign the value from the state to the
`TimeframeSelector` by setting the `value` prop.

### Set initial values

When you create the state for controlling `TimeframeSelector`, you can pass a
`Timeframe` to pre-fill the `from` and `to` inputs. To make a pre-filled value
the default or preset selection, initialize the state with an expression
matching the preset.

### Customize presets

Use `TimeframeSelector.Presets` to customize presets and show any timeframe
inside the overlay. Default presets are exported, so you can either add to the
list of default items or override them entirely.

The preset list can display up to ten items. If an invalid preset item is added,
it won't be rendered and a console.warn will be called, with details to help you
resolve the issue.

### Enable timeframe reset

This component provides a button to 'Reset timeframe', giving users the option
to clear a selected timeframe. To display this button, the `clearable` prop must
be set to true.

### Set display precision

Change the default display precision of minutes by setting the `precision` prop
to either seconds or milliseconds. This also sets the precision of the inputs
shown in the overlay or the returned ISOStrings from the `onChange`.

### Set min and max values

The default `min` and `max` values for `TimeframeSelector` follow the current
Grail limitations for timeframes. You can define a custom min and max range by
setting the `min` and `max` props to valid `isoString` dates or expressions. Use
`FormField` and `FormFieldMessages` to provide users with helpful error
messages.

### Validate user input

This example shows how to validate user input in `TimeframeSelector` using the
`react-hook-form` package, which handles error messages. To connect the form
with `TimeframeSelector`, register the field with the custom error message and
use the `useForm` hook from `react-hook-form`.

### Add custom trigger

`TimeframeSelector` comes with a default trigger for consistent user experience.
In exceptional cases, if it's necessary, you may override the default trigger.
Make sure to communicate whether a timeframe is selected and, if so, the
timeframe itself.

Props are applied automatically to the `TimeframeSelector.CustomTrigger` to
ensure correct semantics. Ideally, use a button as the outermost HTML element
inside the custom trigger.

### Show custom placeholder

Use the `TimeframeSelector.Trigger` and the `placeholder` prop to show a
placeholder for the trigger button. If no option is selected, the `placeholder`
value is shown by default. Notice that the `clearable` prop is used here to
enable empty selection.

### Render custom trigger

We also provide a render function for the `TimeframeSelector.CustomTrigger`,
giving you access to the `displayValue` that the TimeframeSelector would have
applied. This enables you to understand the internal logic of the component
before you customize it. When using a render function here, make sure to spread
the props to the trigger element so the interactions tie back to the
`TimeframeSelector`.

### Enable stepper

When a timeframe is selected, backward and forward arrows are shown next to the
`TimeframeSelector` trigger. Clicking an arrow shifts the timeframe by its
current duration. Set the `stepper` prop to `false` to disable the stepper if
desired.

NoteThe `onChange` callback is debounced by 300 ms, so rapidly clicking the
arrows will only trigger a single `onChange` call once the user stops clicking.
The trigger value updates immediately for responsive UI feedback.

### Related

#### Patterns

- Filtering

#### Documentation

- Timeframe selector
Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Control state
- Set initial values
- Customize presets
- Enable timeframe reset
- Set display precision
- Set min and max values
- Validate user input
- Add custom trigger
- Show custom placeholder
- Render custom trigger
- Enable stepper
- Related
- Patterns
- Documentation

### Props

`TimeframeSelector` is a filtering component that lets users choose from preset
timeframes or add unique "from" and "to" time values of their own.

#### TimeframeSelectorProps

##### Signature:
`export declare type SelectorProps = | <> | , (value: | ) => > & & & & & & {
 /**
 * Shows the button if set to true.
 * @defaultValue false
 * @deprecated The `clearable` prop is deprecated in favor of the new clear button directly located in the input.
 */
 clearable?: ;
 /**
 * The ISODatetime of the earliest datetime that can be configured.
 * @defaultValue '1677-09-21T00:12:43.145224192Z'
 */
 min?: ;
 /**
 * The ISODatetime of the latest datetime that can be configured.
 * @defaultValue '2262-04-11T23:47:16.854775807Z'
 */
 max?: ;
 /**
 * The precision of the time shown in the display value.
 * @defaultValue
 */
 precision?: | | ;
 /**
 * Whether the Stepper is shown.
 * @defaultValue true
 */
 stepper?: ;
};`

#### TimeframeSelector presets components

##### TimeframeSelector.Presets

The `TimeframeSelector.Presets` component is used to render the list of preset
items shown in the overlay.

#### TimeframeSelectorPresetsProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `children?` | | | Children shown inside the presets list. A default list of presets is shown if no children are set.

##### TimeframeSelector.PresetItem

The `TimeframeSelector.PresetItem` component is used to render a preset item to
the list of presets shown in the overlay. This needs to be used inside the
`TimeframeSelector.Presets` component.

#### TimeframeSelectorPresetItemProps
extends`<>, , , , ` |
 | Name | Type | Default | Description
 | `value` | {
 /** Start of the time frame. */
 from: ;
 /** End of the time frame. */
 to: ;
 } | | The value of the timeframe preset.

#### TimeframeSelector trigger components

##### TimeframeSelector.Trigger

The `TimeframeSelector.Trigger` component is used to render the trigger that
opens or closes the overlay.

#### TimeframeSelectorTriggerProps

##### Signature:
`export declare type TimeframeSelectorTriggerProps = & & & & & {
 /**
 * The placeholder text displayed in the TimeframeSelector.Trigger.
 */
 placeholder?: ;
};`

##### TimeframeSelector.DisplayValue

#### TimeframeSelectorDisplayValueProps

##### Signature:
`export declare type TimeframeSelectorDisplayValueProps = & {
 children?: | ((customTriggerProps: {
 displayValue: ;
 }) => );
};`

##### TimeframeSelector.CustomTrigger

#### TimeframeSelectorCustomTriggerProps

##### Signature:
`export declare type TimeframeSelectorCustomTriggerProps = & & & & {
 /** Elements to be displayed in the CustomTrigger. */
 children: | | ((customTriggerProps: {
 displayValue: ;
 isInvalid: ;
 hint: ;
 }, props: ( & & & (>> & )) | ) => );
};`Still have questions?Find answers in the Dynatrace Community
- TimeframeSelector presets components
- TimeframeSelector trigger components

---

