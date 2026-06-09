# Tables

Strato design-system components in the **Tables** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## DataTable

`/design/components/tables/DataTable/`

The `DataTable` is a component for building tables which organize information
into rows and columns.

### Import

`tsx
import { DataTable } from '@dynatrace/strato-components/tables';
`

### Demo

Data and column memoizationMake sure to memoize the `data` and `columns` props passed to the `DataTable`
and use the `useMemo` hook so the props don't change on each render cycle.

### Columns

Table size limitThe `DataTable` supports a maximum of 10,000 columns (including built-in
columns) due to CSS Grid layout constraints. This aligns with
W3C CSS Grid Layout Module
recommendations. Exceeding this limit may cause rendering issues in browsers
such as Firefox.

#### Define column types

You can assign a predefined type to every column. Available types: `text`,
`datetime`, `bit`, `number`, `long`, `currency`, `log-content`, `sparkline`,
`meterbar`, `markdown`, and `gantt`. Column values render and sort according to
their predefined types.

By default, columns of type `text` automatically detect and render links. To
disable this feature, set the `detectLinks` prop in the column `config` to
`false`. If you use a custom cell renderer, you can also apply the `detectLinks`
function.

You can use the `customComponentMappings` config to override the default
rendering behavior of `markdown` columns.

NoteWhen setting the column type to `log-content`, only the first 1,000 characters
are highlighted to optimize performance for datasets of any size. In addition,
log lines are truncated after 1,000 characters. This limit can be changed via
the `truncationLimit` property in the column config. Note that any trailing
whitespaces are removed after truncation.
NoteIf the column type is set to `datetime`, nanosecond precision is only supported
when the input includes sub-second time information, such as
`hh:mm:ss.sssssssss`. This typically includes the ISO 8601 strings with
fractional seconds. In all other cases, the precision is limited to milliseconds
due to the constraints of the JavaScript `Date` type.

#### Column sizing

To set default column widths, use `defaultColumnSizing` as a `DataTable` prop.
This property requires an object that maps column IDs to their respective widths
in pixels.

#### Control column sizing

To activate the column resizing feature in `DataTable`, you must include the
`resizable` property within the table configuration. This property acts as a
flag that allows the user to adjust column widths.

You can track the changes to column widths during resizing events with the
`onColumnSizingChange` and `columnSizing` properties. The callback triggered
upon resizing delivers data for the current widths of all columns. This
information can be used to record and maintain the dimensions of resized
columns. For instance, as demonstrated here, whenever the email column is
resized, it reverts to a default width of 300px.

NoteAs soon as a resizing event starts, all columns with a fraction width or no
defined width will be locked to their current width.

#### Control column width behavior

The `DataTable` lets you control column width behavior in different ways:

Fixed width in pixels: You can set a fixed width for the column by specifying
the exact number of pixels. For example, `width: 100` would set the column to
100 pixels wide.

Minimum and maximum width constraints: You can specify `minWidth` and
`maxWidth` in the exact number of pixels to set width boundaries for a column.
`maxWidth` will not work on fraction widths, to avoid circular width
calculations.

Flexible width in fractions: You can set a flexible width for the column using
a fractional unit. This is done by specifying the width as a fraction, like
`width: '1fr'`. This approach allows the column to take up a proportion of the
available space, adjusting dynamically based on the total space available and
the fractional values assigned to other columns. For instance, if you have two
columns and set their widths to `width: '1fr'` and `width: '2fr'`, the second
column will be twice as wide as the first one.

Fit to content: To make a column's width automatically adjust to fit the
content of its cells, set the column's `width` property to `content`.

Shared leftover space: If you want certain columns to share the leftover space
among themselves set the option to a fraction value for those columns. See the
example in
allow certain columns to occupy the remaining space.

`auto` will hand over control about the column size to the browsers grid
layout and follows the layout engine and specification of the browser.
Reference
MDN grid documentation
for details.

You can also set a maximum width for the column when using either of the
previous two options by configuring it like this:
`{type: 'auto' | 'content', maxWidth: 100}`. Here, `maxWidth` specifies the
maximum width in pixels.

##### Allow specific columns to occupy remaining space

Your `DataTable` may have columns that are more important than others. Between
these columns, you can spread the remaining space within the table by providing
a fraction width like `1fr` for the columns. In the example below the columns
`Memory Total` and `Timestamp` occupy each one fraction of the remaining space,
and the `Price` column takes up two fractions.

#### Accessors

Accessors specify how to retrieve column data from your data structure. Accessor
strings that contain dots allow you to retrieve nested data. If the actual
property key contains a dot, you can escape an accessor by enclosing the string
in square brackets. It is also possible to specify an accessor function that
returns the value you want to extract. See the code below for examples of each.

#### Define header groups

It is possible to define header groups by providing a nested array of columns
via the `columns` property in the column definition. Currently, a header group
can only contain columns and not another nested header group.

#### Customize column header

To customize the column header, simply use the `header` property within the
column definition. Assign a function to this property that returns a customized
JSX element.

You can also use the optional `label` property for accessibility and for
elements such as column settings. If the `label` isn't defined, the column's
`id` will be used as a fallback.

As with cells, to maintain the default header styling, you must wrap each return
statement with the `DataTable.DefaultHeader` element. The
`DataTable.DefaultHeader` also supports `className` and `style` props, allowing
further customization of the header appearance.

CautionAvoid placing interactive elements within a custom-rendered header if column
actions are already configured for the same column. Since a column header with
column actions already includes a button element, adding additional interactive
elements inside may result in unexpected behavior.

#### Configure column visibility

The column visibility feature allows you to specify which columns should be
visible and which should be hidden. Use the `defaultColumnVisibility` prop to
define the column visibility state. Provide an object with the respective column
IDs as keys and boolean values indicating their visibility. A value of `true`
means the column is visible, while `false` means it is hidden. By default, all
columns are visible.

#### Column visibility UI elements

To allow the user to show and hide columns, you need to configure the
corresponding UI elements in the table. Column visibility can be controlled
through either the `DataTable.Toolbar` or the `DataTable.ColumnActions`.

Use the `DataTable.VisibilitySettings` component inside the toolbar, to render a
trigger for the column settings and enable the visibility settings. To let users
hide a column via the column actions, include the `TableActionsMenu.HideColumn`
as a menu item.

To prevent a specific column from being hidden, set the `disableColumnHiding`
prop to `true` in the column definition. For header groups, the group itself
cannot be hidden if at least one of its child columns has `disableColumnHiding`
prop set to `true`.

#### Control column visibility

To control column visibility, use the `columnVisibility` prop to provide the
visibility state, along with the `onColumnVisibilityChange` callback which
allows you to react to visibility changes.

#### Reset column visibility

Column visibility can be reset to default original value using the column
settings overlay trigger in toolbar. A custom reset state can be set using the
`resetColumnVisibility` prop in `DataTable.VisibilitySettings` component, which
allows the column visibility state to be set to the provided reset state. In
uncontrolled, the column visibility resets to `defaultColumnVisibility` prop
state if present or original visibility state. This ensures that the columns can
be easily reverted to their default visibility state whenever needed. Reset
button is disabled when the current state is the same as the default state.

#### Open column settings programmatically

You can open the column settings programmatically using the
`openColumnSettings()` function. By default, the settings modal is opened with
the same options (column visibility, column order and/or column pinning
settings) as specified in the `DataTable.Toolbar`. However, you can override
these options via the function's parameters. This is particularly useful if the
data table is used without its built-in toolbar.

#### Configure column order

To enable column ordering, set the `columnOrdering` prop to `true`.

For uncontrolled, you can optionally use `defaultColumnOrder` to define the
initial column order, by providing an array of all column IDs in the desired
order. If you don't specify any order, the initial order is inferred from the
column definition.

The defined column order should include all columns and ensure that child
columns with the same parent are not separated. To avoid invalid configurations,
the passed column order is validated and corrected if necessary. The following
issues will be resolved:

- duplicate column IDs

- column IDs that don't exist in the column definition

- missing column IDs

- column IDs within the same group that are not adjacent

When column ordering is enabled, column headers will be draggable. To move a
column to another position hold down the mouse on the column header and then
release it when you have moved it to its destination. This is also possible
using touch (press, hold and release).

#### Column order UI elements

In addition to drag and drop, the column order can be adjusted using
corresponding UI elements in the table. You can control the column order through
either the `DataTable.Toolbar` or the `DataTable.ColumnActions`.

Use the `DataTable.ColumnOrderSettings` component within the toolbar to render a
trigger for the column settings and enable the column order settings. To allow
users to move a column via the column actions, include the
`TableActionsMenu.ColumnOrder` as a menu item.

#### Control column order

To control column order, use the `columnOrder` prop to provide the desired
order, along with the `onColumnOrderChange` callback which allows you to react
to changes in the column order.

#### Reset column order

Column order can be reset to default original value using column settings
overlay trigger inside the toolbar. A custom reset state can be set using the
`resetColumnOrder` prop can be set in `DataTable.ColumnOrderSettings` component,
which allows the column order state to be set to the provided reset state. In
uncontrolled, the column order resets to `defaultColumnOrder` prop value if
present or original order. This ensures that the columns can be easily reverted
to their default order whenever needed. Reset button is disabled when the
current state is the same as the default state.

#### Configure pinned columns

Column pinning enables individual columns to remain pinned to the left or right
edge of the table, improving visibility for important data. To enable column
pinning, set the `columnPinning` prop to true.

Default pinned columnsThe built-in columns for drag and drop row ordering,
row selection,
expandable rows, and
row actions are always pinned by default and cannot be
unpinned, regardless of whether column pinning is enabled.
For uncontrolled usage, you can use `defaultPinnedColumns` to define the initial
pinned state. This prop accepts an object with two optional properties:

- `left`: An array of child column IDs to pin to the left side.

- `right`: An array of child column IDs to pin to the right side.

LimitationsWhile ordering is supported for unpinned columns,
pinned columns cannot be re-ordered.

#### Column pinning UI elements

Column pinning can be configured through the table's UI. To enable users to pin
and unpin columns via the column actions menu, use `DataTable.ColumnActions` and
include `TableActionsMenu.ColumnPinning` as a menu item.

To render a trigger for the column settings and enable column pinning settings,
use the `DataTable.ColumnPinningSettings` component inside the
`DataTable.Toolbar`.

#### Control column pinning

To control column pinning, use the `pinnedColumns` prop to specify which columns
should be pinned to the left or right. To handle updates, provide an
`onPinnedColumnsChange` callback to respond to changes in the pinned column
state.

#### Customize the label of the column settings trigger

Adding the `DataTable.ColumnSettingsTrigger` component inside
`DataTable.Toolbar` in combination with `DataTable.VisibilitySettings`,
`DataTable.ColumnOrderSettings`, or `DataTable.ColumnPinningSettings` allows you
to configure a custom text that will be displayed as the trigger label for the
column settings.

### Rows

#### Enable interactive rows

To activate interactive rows in `DataTable`, you must configure the
`interactiveRows` prop on the table. This will make the entire row highlightable
and selectable by the user. A row can be activated either by clicking on it or
focusing it.

##### Disable auto-activation for interactive rows

By default, interactive rows are automatically activated when they are focused
using the keyboard. However, if you want to disable automatic activation, you
can do so by setting `interactiveRows={{ autoActivate: false }}`. This allows
you to activate a specific row by pressing the `Enter` key.

##### Configure links for interactive rows

To enable navigation from interactive rows, use the `link` prop within the
`interactiveRows` prop. `link` accepts a function that receives the row's data
and returns a URL. When a row is clicked or activated via the `Enter` key, the
user will be directed to the specified URL.

#### Control interactive rows

When you want to control which row is currently activated, you use the
`activeRow` prop. This prop allows you to specify which row should be marked as
active at any given time. To make this dynamic, you can also provide a handler
function for the `onActiveRowChange` callback. The rows themselves are
identified by the `rowId`, which can be customized as well. For details on how
to do this, reference the control row IDs section.

NoteIn addition to the `interactiveRows` prop, it is advised to debounce the row
activation when auto-activation is enabled. This allows you to specify by how
many milliseconds the activation of a row should be delayed for better
performance. By default, the row is immediately activated.

#### Provide sub-rows

The `DataTable` component offers the capability to include sub-rows.

Enable sub-rows - To activate this functionality, the `subRows` prop must be
defined. This prop accepts either a boolean value, which activates the
default sub-row view, or an object configuration.

Provide sub-rows data - Simply define the respective sub-row data by adding
the `subRows` property to the parent row's data definition. The specified
sub-rows must have the same data structure as the parent rows and can be
nested over multiple levels.

Use the `defaultOpenSubRows` prop to specify sub-rows that are already open upon
initial rendering. The `onOpenSubRowsChange` handler allows you to react to
changes in the currently open sub-rows.

The `defaultOpenSubrows`/`openSubRows` expects the id of the row (unless
otherwise specified, this is the array index of the data) along with a boolean
whether or not it's opened. Nested sub-rows are separated with a dot by default,
so '0.0' would be the first row's first sub-row. For details on how to customize
row IDs, reference the control row IDs section.

NoteThe column containing the sub-row indicator should always be left aligned.

#### Configure sub-rows

To further configure sub-rows, you can pass a configuration object to the
`subRows` prop, using the following options:

`accessor`—Provides a custom `accessor` that retrieves the
corresponding sub-rows for each row from the data.

`subRowColumnId`—Specifies the ID of the column in which to inject the
sub-row indicator. By default, this is the first visible column.

`disableSubRow`—Accepts a function that evaluates whether or not to
disable the sub-row trigger for a given row.

#### Control sub-rows

To control the state of the open sub-rows, provide the desired rows using the
`openSubRows` prop along with a handler for the `onOpenSubRowsChange` callback.

#### Enable expandable rows

Expandable rows allow you to add additional data to a row. This information is
only visible when the row is expanded.

The default state of each row can be controlled using the `defaultExpandedRows`
prop on the `DataTable.ExpandableRow` slot child. To control each row over the
lifetime of the table use the `expandedRows` property and the
`onExpandedRowsChange` callback.

In this example, every second row is disabled for demo purposes.

#### Enable row selection

To activate row selection in `DataTable`, you must configure the
`selectableRows` prop on the table. Assigning a boolean value to this prop will
add a checkbox in the first column across all rows, enabling selection
functionality. Alternatively, `selectableRows` can be defined as an object,
allowing for further customization through the following options:

`disableRowSelection` - Accepts a function that takes the row's data as input
and returns a boolean value. If it returns `true`, the row will be
non-selectable; if `false`, the row will be selectable.

`selectAllBehavior` - A string value that specifies whether the Select
all action applies to only the currently visible rows on the page or to all
rows within the table.

`limit` - A positive integer that sets the maximum number of selectable rows.

NoteIf a `limit` is specified, rows will still be de-selectable even when
`disableRowSelection` is enabled. This prevents inconsistent states where the
selection `limit` is reached but all selected rows are disabled, making it
impossible to adjust the selection.
To set up rows that should be selected as soon as your table loads, you need to
use a prop `defaultSelectedRows`. This option should be assigned an object that
specifies which rows are selected. Each row is identified by its id, and the
selection state is indicated by a boolean value (`true` for selected, `false`
for not selected). To ensure correct selection behavior when updating table data
dynamically (e.g., adding or removing rows), make sure to provide
unique row IDs.

It is possible to select or deselect multiple rows at once by first clicking on
a start row, then holding the `Shift` key while clicking on an end row.

#### Control row selection

When you want to control which rows are selected, you use the `selectedRows`
prop. This prop allows you to specify which rows should be considered selected
at any given time. To make this dynamic, so that it can change in response to
user actions, you also provide a handler function for the `onRowSelectionChange`
callback.

Here's how it works:

- `selectedRows` prop: This is where you pass an object that represents the
currently selected rows. Each row is identified by its id, and the selection
state is indicated by a boolean value (`true` for selected, `false` for not
selected).

- `onRowSelectionChange` callback: This function is called whenever the
selection changes, such as when a user clicks on a row checkbox. The callback
function receives information about the new set of selected rows. By using
these two together, you can maintain the selection state outside of the
component, giving you full control over the behavior of the selection.

#### Control row IDs

Features like row selection, sub-rows and row interactivity by default use a row
id based on the index of the data that is passed. This can be problematic when
you want to persist any of the states while the data itself changes. For this
usecase you are able to change how rows are identified by providing a `rowId`
function on the `DataTable`. When providing a custom row id function, for sub
row identification, the row IDs will be separated by `↳` character.

#### Configure row order

To enable row ordering, set the `rowOrdering` prop to `true`. Note that if you
are providing your own row IDs you need to specify the `rowId` prop.

For uncontrolled, you can optionally use `defaultRowOrder` to define the initial
row order, by providing an array of all row IDs in the desired order. If you
don't specify any order, the initial order is inferred from the order in `data`.

To enable drag and drop row ordering, you can pass a configuration object to the
`rowOrdering` prop with the option `enableDragAndDrop` set to `true`.
Additionally, the option `disableRowDragAndDrop` accepts a function that takes
the row's data as input and returns a boolean value. If `true` is returned, drag
and drop will be disabled for the row, otherwise it is enabled.

Additionally, the `lockDisabledRows` option ensures that rows with disabled drag
and drop remain fixed in place when sorted to the start or end of the table.
Consequently, other rows cannot be dropped above or below these locked rows. If
set to `true`, the rows are locked when sorted to the start or end of the table.
Optionally, `lockDisabledRows` can be set to `'start'` or `'end'` if rows should
be locked solely at the start or at the end.

When drag and drop is enabled, a drag handle for every row will be rendered in
the first column. To move a row to another position hold down the mouse on the
drag handle and then release it when you have moved it to its destination. This
is also possible using touch (press, hold and release).

Alternatively, using the keyboard use the tab key to focus the drag handle and
then press the spacebar once. Use the up and down arrow keys to move the row to
its destination and then press the spacebar again to release it. To cancel press
escape.

If you are using row ordering with pagination and modifying the `data`, you
should set `autoResetPageIndex` to `false` to prevent the pagination jumping
back to the first page. If you are only modifying the `rowOrder` then there is
no need.

#### Control row ordering

For controlled, the `rowOrder` prop holds the order of the rows. This is an
ordered set of string IDs of the rows. It's up to you to use the
`onRowOrderChange` event to update row order and optionally update the original
data as you see fit.

##### Order rows with disabled drag and drop

To facilitate disabling of drag and drop functionality for certain rows, we
provide the `useLockedRowOrder` hook. This hook disables drag and drop
functionality for the specified rows and locks them at the start or the end of
the table. It takes an object with the following options:

- `initialRowOrder` - An ordered set of row IDs representing the initial row
order.

- `lockedRows` - A set of row IDs for which drag and drop is disabled and should
be sorted.

- `position` - The position where the rows with disabled drag and drop should be
grouped. Use `'start'` to position the rows at the start of the table and
`'end'` to group them at the end. By default, the rows are positioned at the
start.

#### Highlight rows

You have the option to highlight an entire row. The thresholds for row
highlighting can be configured at the table level using the `rowThresholds`
prop. This prop accepts the same options as the cell threshold with the addition
of a `type`. However, it also allows you to specify which cell value should be
used for the row threshold by defining an accessor or id.

You can add either a single rule or multiple rules to the threshold definition.
If you choose to use multiple rules, you can define different thresholds for
different cell values within a row. However, regardless of which threshold is
met, the same color will be applied to the entire row.

The `type` determines how the highlighted row will be visually marked. The
`pill` type accepts a `color` and shows a marker on the start of the row. The
`hightlight` type accepts `color` and `backgroundColor` and changes the
textcolor and background color of all cells in a row.

#### Define custom comparator

You can define a custom `comparator` function to evaluate the `threshold` using
your own logic. This function should return a `boolean`. If it returns `true`,
the `threshold` is applied; if `false`, it's not. The function receives the row
data as input. Please note that this custom `comparator` function will not be
serialized for sharing via
intents.

### Cells

#### Format cell data

You can format the cell data via the column definition, by specifying the column
property `formatter`. For configuration, use the corresponding options from
'@dynatrace-sdk/units', i.e. `FormatOptions` for numbers, `FormatDateOptions`
for dates, and `DataTableCellFormatterCurrencyOptions` for currencies.

Datetime columns also accept the shorthands `date`, `time`, or `datetime` as a
`formatter` value to conveniently show only the date portion, only the time
portion, or both.

#### Customize cell rendering

To customize the cell rendering, pass the corresponding function to the `cell`
prop in the column definition. If you want to maintain default cell styling, you
need to wrap each return statement with `DataTable.DefaultCell` element. Also,
`DataTable.DefaultCell` supports `className` and `style` props, allowing further
customization of the cell appearance.

Within the function passed to the cell property, you can access the cell's
`value`, `rowIndex`, `rowData` and `rowId`. Additionally, the `isLineWrapped`
prop provides the current line wrap state of the column in which the cell is
rendered.

Moreover, a `format`, a `formatLogContent` and a `detectLinks` function are
available:

- `format` - Allows you to apply the `formatter` options that have been
configured for that cell (either via the column definition or via the
columnType).

- `formatLogContent` - Formats the given text as a log output.

- `detectLinks` - Automatically detects links in the given text and renders them
as such using the `ExternalLink` component.

#### Highlight cells

Cells can be highlighted in different colors depending on the specified
threshold. In the column definition, you can configure the threshold for every
column. You can specify `value`, `comparator`, `color`, `backgroundColor`, and
`accessor`. The `color` will be applied to the cell text and `backgroundColor`
to the cell background. The `accessor` prop can also be used for providing
custom accessor for the cell value that can be used for threshold calculations.

If the column cell value passed is a string (text), the threshold comparator can
be set with either an `equal-to` or `not-equal-to` operator. On the other hand,
if your value is a number, you can use one of the following operators:

- `greater-than`

- `less-than`

- `greater-than-or-equal-to`

- `less-than-or-equal-to`

- `equal-to`

- `not-equal-to`

If the value of the `cell` is an object, the `thresholdaccessor` could return
a specific attribute within the object, such as a `number` or `string`. This
allows for more complex threshold calculations based on specific attributes of
object values.

NoteWhen multiple thresholds are applicable (evaluate to true) the final valid
threshold has priority. Also, if both row and column thresholds apply to a cell,
the column threshold takes precedence over the row threshold.

### Layout and format

#### Customize visual representation

The `variant` prop allows you to customize the appearance of the `DataTable` by
setting the configuration options available in `DataTableProps['variant']`.

##### Row density

The `rowDensity` option adds spacing around the content within a row. By
default, `rowDensity` is set to `default`, which represents a medium spacing. If
the option is set to `condensed`, the spacing becomes minimal while
`comfortable` represents the maximum spacing.

##### Row separation

The `rowSeparation` option determines how rows should be separated visually. By
default, `rowSeparation` is set to `horizontalDividers` which adds lines between
the rows. `zebraStripes` additionally provides alternate row coloring. By
setting `rowSeparation` to `none`, the rows are not separated visually.

##### Vertical dividers

The `verticalDividers` option determines whether columns should be separated
visually. By default, `false` is set which does not separate the columns within
a `DataTable`. If `verticalDividers` is set to `true`, lines are added between
the columns.

##### Borders

The `contained` option provides a border for the `DataTable`. By default,
`contained` is set to `true` to display the border. If `false` is set, no border
is added.

##### Hide header

You can customize the `DataTable`'s appearance to hide the entire header, by
setting `headers: 'hidden'`.

If you choose to hide the header, please note that the ability to sort columns
by header, as well as any actions that could be triggered with column headers,
won't be available.

##### Vertical alignment

Use the `verticalAlignment` option to configure the vertical alignment of the
cell content. The alignment options are `top`, `center`, and `bottom`. It is
also possible to configure the vertical alignment for header and body cells
separately. By default, all cell content is top-aligned.

#### Enable full width

By default, the `DataTable` is set to automatically expand and occupy the full
width of its parent element. However, this behavior changes when the table is
placed within a flex container. In such cases, if you wish to ensure that the
table maintains full width, you can include the `fullWidth` prop when using the
`DataTable` component.

When this value is not set, it will grow as needed based on the number of
columns and their width.

#### Enable full height

By default, the `DataTable` grows as needed based on the number of rows. When
placed inside a container, the table's height can be the same as its parent or
smaller depending on how many rows would be visible inside the parent container.
If you wish to ensure that the table always occupies the full height of its
parent element, you can include the `fullHeight` prop when using the `DataTable`
component.

NoteKeep in mind that the `fullHeight` prop should be applied carefully. Setting
`fullHeight` on the table that is placed inside a container that takes up the
height of the page can lead to serious performance issues. It is therefore
advisable to use the prop in combination with a well-defined container height.

#### Fonts

The `DataTable` allows for the customization of font styles across the entire
table or within individual columns. This can be achieved by configuring it in
the table variant options or the column definition.

#### Text alignment

If no column type is set, text within the cell is left-aligned by default. To
explicitly change the default alignment, use the `alignment` property in the
column definition.

#### Enable line wrap

The `DataTable` component offers flexible options for managing the line wrapping
of cell content within your table. Here’s how you can control it:

Global line wrapping configuration - To activate line wrapping across all
columns, set the `defaultLineWrap` or `lineWrap` property to true.

Column-specific line wrapping - If you prefer to enable or disable line
wrapping for certain columns, pass an object to the `defaultLineWrap`
property. Use column IDs as keys and set their values to true (to enable) or
false (to disable).

User-Controlled Line Wrapping - Toggle via column actions: Incorporate
`TableActionsMenu.LineWrap` into your table to allow users to switch line
wrapping on or off for specific columns through the column actions menu.

User-Controlled Line Wrapping (entire table) - Toggle via a
`DataTable.Toolbar` action: Incorporate `DataTable.LineWrap` into you tables
`DataTable.Toolbar` component to allow users to switch line wrapping on or off
for all columns.

##### Props for line wrap control

The `DataTable` also provides properties to manage line wrapping state:

- `defaultLineWrap`- Defines the initial state of line wrapping when the table
loads.

- `lineWrap` - Sets the line wrapping state.

- `onLineWrapChange` - A callback function that triggers when the line wrapping
state changes.

NoteThe `DataTable` uses column virtualization to optimize performance. With line
wrap enabled, row heights might change while scrolling horizontally as wrapped
content becomes visible.

#### Export configuration

The `DataTable`'s configuration can be exported at any time for various
purposes, such as sharing the configuration with other applications
through an intent. The
current configuration can be retrieved by creating and assigning a `ref` to the
corresponding `ref` property of the `DataTable`, and then calling
`ref.getConfig()` function.

NoteWhen the `getConfig` function is invoked, a snapshot of the serialized
configuration is returned. As such, it will not change if the `DataTable`'s
configuration is subsequently modified. It is recommended to ensure that you
apply all your required configurations to the `DataTable` before calling this
function.

#### Import configuration

The configuration provider for the `DataTable` accepts a JSON object and also
accepts a `string` as input for importing a serialized configuration. When a
string is provided, it is internally parsed and applied as the `DataTable`
configuration.

NoteIf the configuration provided does not match the properties of the `DataTable`
configuration, any unknown properties will be ignored. Additionally, if required
properties are not provided, or the given config is invalid, default values will
be applied.
NoteWe do not support dynamically changing default values, as doing so goes against
their intended purpose. Therefore, changing the values of `defaultPageSize` or
`defaultPageIndex` in the configuration for pagination will not update the
corresponding props in the `DataTable`. If you need to set default values, it is
recommended to ensure that you always do that before importing the
configuration.
NoteDue to potential version mismatches in `DataTable` packages used in different
applications, importing a configuration from another application may produce an
unintended outcome and not result in a perfect match.

### Navigation

#### Enable pagination

To enable pagination add the `DataTable.Pagination` component to your table.

#### Change page size

The default page size options are 10, 20, 50, 100, 250, 500 and 1000. To
customize these options, use the `pageSizeOptions` prop, which allows you to
pass the desired page sizes as an array. Please ensure that the passed (default)
page size aligns with the defined options. The table will not sanitize page
sizes that do not exist in the options.

#### Control pagination

It is also possible to control the page size and the page index using the
`pageSize` and the `pageIndex` props together with the `onPageSizeChange` and
the `onPageIndexChange` callbacks.

#### Use server-side pagination

In addition to the regular client-side pagination, it is also possible to use
server-side pagination. For server-side pagination, pass the data for the
respective page to the table and update the `enablePrevPage` and
`enableNextPage` flags accordingly. Upon navigating to another page or changing
the page size the corresponding callbacks as well as the `onPageChange`
callbacks provide the updated values, allowing you to retrieve the corresponding
data.

By default, the server-side pagination does not display the indicator for which
page out of the total number of pages is currently shown, i.e. "Page 1 of 30",
in the bottom right corner. This is because the total number of rows is unknown
since only the data for the respective page is passed. However, adding the
`totalRowsCount` prop enables this information to be displayed as well.

#### Scroll to a given row

The `DataTableRef` provides the `scrollToRow` method, which enables programmatic
scrolling to a specific row in the table, identified by its `rowId`. If
pagination is enabled, the table first navigates to that page if necesssary.

You can configure the `scrollToRow` method to align the target row to the
`start`, `center`, or `end` of the table's visible area by passing the desired
alignment as a second argument. If no alignment is specified, the default
alignment is `start`.

If the target row is a sub-row, the parent row must be expanded beforehand.
Otherwise, the sub-row will not be accessible for scrolling.

### States

#### Loading state

Use the `loading` prop to display a loading indicator. This can be used for the
initial load where columns and data are not yet available, when waiting for data
to be fetched or when performing actions such as moving to the next page. The
loading indicator will adjust accordingly depending on whether columns and data
are already loaded.

##### Initial table load

##### Load data

#### Customize empty state

The `DataTable.EmptyState` component allows you to configure a custom empty
state that will be displayed if no data or no columns are available.

### Actions and intents

#### Configure column actions

The column actions are represented by a button in a column header that opens a
drop-down menu. Within the menu, you can include various functionalities
allowing end users to perform actions related to the columns.

The drop-down menu also appears on right-click, providing additional access to
defined cell or column actions. This feature adds a layer of functionality,
allowing users to access more options directly from the table.

To configure column actions you need to define the `DataTable.ColumnActions`
slot component.

Within the `DataTable.ColumnActions` slot there's a function that receives the
current column's details, enabling customization of the column's actions. The
function should return a `TableActionsMenu` object, which defines user actions
for the cell. It should also include the `TableActionsMenu.Item` slot component
to represent a single action item.

This is similar to the `TableActionsMenu.Link` component, which renders a
defined link element as a menu action item. You can assign an `onSelect` event
as a property of this component. This will execute the specified action upon
user interaction.

Additionally, you can use the `TableActionsMenu.Prefix` slot to place an icon on
the left side of the action item, while the `TableActionsMenu.Suffix` slot lets
you place an icon on the right.

For cross-app navigation, the `TableActionsMenu.Intent` slot component can be
used to define an intent item. See the section
Configure intents to learn more.

Use the predefined `TableActionsMenu.CopyItem` slot component to let users copy
column values to the clipboard. To group items semantically within the menu, use
`TableActionsMenu.Group` and `TableActionsMenu.Label`. See the
documentation for more information about
grouping items in menus.

The user action menu supports multi-level menus, allowing you to configure
sub-menus using the slots `TableActionsMenu.SubMenu`,
`TableActionsMenu.SubContent`, and `TableActionsMenu.SubTrigger`.

To configure actions for a particular column, its ID must be provided to the
`column` property. Omit the `DataTable.ColumnActions` column ID to make default
actions apply to any columns without explicitly configured column actions.

#### Configure row actions

Configuring row actions in a `DataTable` involves adding an action column to the
far right of the table. This column should contain buttons, menus, or links that
allow users to perform actions specific to each row.

To set up row actions in the table you need to locate `DataTable.RowActions`
slot component as a `DataTable` child. This component takes a function that
receives the current row’s data as well as some meta information about the
tables layout as its parameters. This allows you to access and manipulate the
data for that specific row. The function needs to return a `ReactNode` that
defines the user actions for the row. Most likely you want to add some primary
actions as buttons and secondary actions into a menu.

#### Configure selected row actions

The `DataTable.SelectedRowsActions` component provides an additional slot where
you can perform actions simultaneously on one or more selected rows. Actions
passed to this slot are placed right above the table header and are shown only
when at least one row is selected. If table actions exist, they are hidden when
the selected rows actions menu is active.

#### Configure cell actions

The cell actions are represented by a button in a table cell that opens a
drop-down menu. Within the menu, you can include various functionalities
allowing end users to perform actions related to the cells.

The cells within the `DataTable` allow custom interactive elements, allowing you
to include links or other actionable elements within cells with cell actions
defined.

To configure cell actions you must define the `DataTable.CellActions` slot
component. There's a function within the `DataTable.CellActions` tag that
returns a `TableActionsMenu` object that defines the user actions for the cell.
It should also include the `TableActionsMenu.Item` slot component to represent a
single action item, similar to the `TableActionsMenu.Link` component, which
renders a defined link element as a menu action item.

You can assign an `onSelect` event as a property of this component to execute
the specified action upon user interaction. Additionally, the
`TableActionsMenu.Prefix` and `TableActionsMenu.Suffix` properties can be
applied to the item to add an icon on the left or right side of the action
trigger element.

For cross-app navigation, the `TableActionsMenu.Intent` slot component can be
used to define an intent item. See the section
Configure intents to learn more.

To enable users to copy cell values to the clipboard, use the predefined
`TableActionsMenu.CopyItem` slot component.

To group items semantically within the menu, use `TableActionsMenu.Group` and
`TableActionsMenu.Label`. For more information about menu groups and labels,
refer to the documentation. The user action
menu supports multi-level menus, allowing you to configure sub-menus using the
slots `TableActionsMenu.SubMenu`, `TableActionsMenu.SubContent`, and
`TableActionsMenu.SubTrigger`.

To assign actions to cells in a specific column, you must specify the unique
identifier (ID) of the column. This ID is used as the value for the `column`
property within the `DataTable.CellActions` configuration. It tells the
`DataTable` which column to associate the actions with. Omit the column ID to
have default actions apply to any columns without explicitly configured actions.

#### Configure table actions

The `DataTable.TableActions` component provides an additional slot where you can
place custom actions that affect the entire table. Actions passed to this slot
are placed right above the table header.

#### Download data

The `DataTable.Toolbar` has an item `DownloadData` which enables the downloading
of the table data. Depending on your table configuration, you can choose between
downloading all data, downloading the current page and only downloading the
selected rows. Only visible columns are included when downloading data. To
exclude specific columns, provide an array of column IDs to the `excludeColumns`
prop in the `DownloadData` slot of the toolbar.

NoteColumns with `sparkline` column type are always excluded from the downloaded
data, as sparkline visualizations cannot be meaningfully represented in CSV
format.
NoteCSV data is generated in the browser. For very large tables (with many rows or
large cell content), exporting all rows may slow down the browser or even cause
it to crash. In such cases, prefer exporting only individual pages or selected
rows.
If the table has sub-rows, an additional column `index` is
added to the downloaded table data, indicating the row's indentation level. For
example, the first row has index `1`, its first sub-row has index `1.1` and so
on. Sub-rows are included in the downloaded table data regardless of whether
they are currently open or closed. When downloading the current page, all
sub-rows of the rows on that page are included, even if some sub-rows are
actually rendered on following pages.

When downloading, double quotes are escaped and if the text has commas, new
lines, double quotes, tabs or carriage returns, the entire line is enclosed in
double quotes. In addition, values starting with `=`, `+`, `-`, `@`, `\t` and
`\r` are escaped with a single quote to mitigate CSV injection. Also note that
if you have custom cells you can provide a `toString` function on the data
object for customized download output.

The `DataTable.DownloadData` slot also provides the `onDownloadData` callback
that fires once data has been downloaded. The callback's `subset` parameter
indicates whether all data, the current page, or the selected rows were
downloaded. The `excludedColumns` parameter indicates which specified columns
were excluded from the download.

The preferred way is to use the toolbar item as above but if you have some good
reason not to use the toolbar you can create your own download trigger which
programmatically calls `downloadData()` with one of the parameters `'all'`,
`'page'`, or `'selected'`. You can also exclude specific columns by providing an
array of column IDs to the `excludeColumns` parameter.

#### Enable sorting

By using the `sortable` flag, you can enable sorting for the entire table.
Additionally, you have the option to disable sorting on a per-column basis by
configuring the `disableSorting` property in the column definition. For
`meterbar` columns, sorting is disabled by default and
can be enabled explicitly by setting `disableSorting` to `false`. Please note
that sorting is not supported for
`MultiMeterBarChart`s.

By default, the first sorting direction is ascending. If you want to change
that, you can configure the `sortDescFirst` flag for the individual column.
There is also a possibility to invert the sorting logic. Setting `sortInverted`
to `true` means the underlying sorting direction will be inverted, but the UI
will not change. This could be useful, for example, when a lower score is
better. Values like `null` and `undefined` will be sorted with lower priority
and will always appear at the end of the list.

Columns can be sorted by clicking directly on the header, even on header cells
with column actions defined. Sorting indicators and column action indicators are
shown on hover or on sorted columns, which allow for header cells to be less
cluttered, allowing to focus on the header's content.

Multiple columns can be sorted at the same time. To enable this, hold the
`Shift` key while clicking on the headers of the columns you want to sort by.
The sorting indicators will show the sorting priority, with the primary sorting
column showing a `1`, the secondary sorting column showing a `2`, and so on.

Sorting controls are also available in the column actions menu for any column
with sorting enabled.

#### Sort programmatically

Control sorting programmatically by setting the `sortBy` prop, passing an array
with column IDs and sorting directions. Use the `onSortByChange` callback to
monitor and manipulate sorting changes within the `DataTable`. If you want to
sort your data before it is passed to the table, you need to disable built-in
sorting by setting `sortable={{ manualSorting: true }}`. This is particularly
useful for server-side sorting. To initially sort tables without controlling
their state, use `defaultSortBy`.

#### Define sortAccessor

Define a custom `sortAccessor` in the column definition to sort by a different
value than the one returned by the accessor. For example, if the accessor
returns an object, you can set the sortAccessor to return a number or string
field within the object.

#### Define custom sortType

You can specify a `sortType` in the column definition to control sorting
behavior more precisely. The built-in options are
`'text' | 'textCaseSensitive' | 'number' | 'datetime'`. However, for more
advanced scenarios, you can pass a function as well. This is particularly useful
for compound data, where a column displays multiple or combined data entries.
When using a custom `sortType` function, you may also need to define a custom
sortAccessor in your column definition. For details, see:
Define a sortAccessor.

In the example below, a column displays both CPU usage (as a percentage) and
memory usage (in GB). The custom sorting function prioritizes higher CPU usage
and resolves ties by considering higher memory usage.

#### Configure intents

An intent is a message object that enables users to pass the user flow from one
app to another. It is possible to perform actions such as viewing data in
another application. You can read more about intents in the
Intents docs.

The `DataTable` supports intents within the following slot components:

`DataTable.CellActions` and `DataTable.ColumnActions`: Use the
`TableActionsMenu.Intent` slot within the `TableActionsMenu`. For custom
icons, use the `TableActionsMenu.Prefix` slot within
`TableActionsMenu.Intent`.

`DataTable.RowActions`: Provide a `Menu` component containing the
`Menu.Intent` slot. For custom icons, place the `Menu.Prefix` slot within
`Menu.Intent`.

`DataTable.Toolbar`: Use the `DataTable.Intent` slot to configure intents.
Optionally, set a custom icon by passing the desired icon to the `icon` prop.

Intents can be configured using the following options:

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: ID of the application that will be launched to handle
the intent.

- `recommendedIntentId`: ID of the action that is passed to the application.

- `responseProperties`: Array of properties to be included in the response.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

#### Configure intents in toolbar

The `DataTable.Toolbar` accepts `DataTable.Intent` slot components, offering a
menu with the specified intents for cross-app navigation. See the
Configure intents section to learn more about the
configuration of intents in the `DataTable`.

### Charts in tables

#### Gantt chart

To visualize column data with a Gantt chart, set the columnType to `gantt`. The
Gantt column definition also accepts a `config` prop in the format
`DataTableGanttColumnConfig`, which allows configuration of the following
options:

- `min`: Axis configuration for the minimum value (`MinScaleBoundary`).

- `max`: Axis configuration for the maximum value (`MaxScaleBoundary`).

- `xAxisType`: Whether the axis type is `numerical` or `time`.

- `nameAccessor`: String accessor for the segment's name, which is displayed in
the tooltip.

- `colorAccessor`: String accessor for the segment's color.

- `colorPalette`: The palette that contains the segment color mapping.

- `showBackground`: Whether gaps between segments should receive a background.

- `tooltipActions`: Actions that should be displayed with the default tooltip.
The function provides the `segment`, `row` and `parent` data as parameters.

- `tooltip`: Custom tooltip implementation. The function provides the `segment`,
`row` and `parent` data as parameters.

- `formatter`: Formatter options from the `@dynatrace-sdk/units` package.

- `annotationsHeader`: Configuration for displaying annotations in the header
above the x-axis. See the `GanttAnnotationsHeaderConfig` type for details.

The data for the Gantt chart must contain the Gantt segment data in this format:
`{ start: number; end?: number; }`. Each row can display one or more Gantt
segments. If multiple segments should be displayed, you can pass an array of
segment data. The segment data can also contain further properties to configure
color or name, for example, if the corresponding accessor is specified in the
`config`.

##### Annotations

Unlike other annotation-supporting charts where annotations are composed via
slot components, Gantt annotations are configured entirely via the
`annotationsHeader` prop (type `GanttAnnotationsHeaderConfig`) on the column
`config`. They render in the Gantt header above the x-axis.

Note that the annotation data must be of the same type as the Gantt data
(`numerical` or `time`). If `min` is set to `data-min`, or `max` is set to
`data-max`, the values from the annotation data are also considered when
determining the axis boundaries.

`GanttAnnotationsHeaderConfig` accepts the following options:

- `tracks` (`GanttAnnotationsTrackConfig[]`): The annotation tracks. See below.

- `tooltip`: Custom tooltip shown when hovering over a marker.

- `tooltipActions`: Actions menu handler for the default tooltip.

- `height`: Fixed height for the annotations header area. If not set, the height
is determined by the content.

- `textOverflow` / `truncateMode`: Control text overflow and truncation of
marker labels.

- `loading`: Displays a loading state in the annotations header.

- `emptyState` / `errorState`: Custom templates for empty and error states.

Tracks are configured as an array of `GanttAnnotationsTrackConfig` objects. Each
track groups related markers and extends `AnnotationsTrackProps` with two
Gantt-specific additions:

- `markers` (`GanttAnnotationsMarkerProps[]`): The markers for the track. Each
marker extends `AnnotationsMarkerProps` with an optional `indicatorsDisplay`
prop.

- `indicatorsDisplay` (`auto` / `always` / `never`): Controls the visibility of
annotation indicators. Setting this on a track applies to all its markers, but
a marker-level `indicatorsDisplay` takes precedence when specified.

Annotation indicators are small visual markers rendered inside each Gantt
cell that correspond to the annotation positions in the header. They help users
correlate cell data with annotations. `indicatorsDisplay` controls their
visibility:

- `auto`: Indicators appear when hovering over the corresponding annotation in
the header. Default behavior.

- `always`: Indicators are always shown, regardless of hover state.

- `never`: Indicators are never shown.

#### MeterBarChart

You can visualize numerical data within the `DataTable` by using the
MeterBarChart.
Follow these steps to render a `MeterBarChart` in the table:

- Set `columnType` to `meterbar` in the column definition.

- Use the `accessor` property to specify the value data to process.

The MeterBarChart in the `DataTable` column can be further customized through
the column definition. You can configure its appearance by using the `config`
prop, which includes the following options:

- `color` (string): Specifies the color of the `MeterBarChart`.

- `min` (number): Sets the minimum value for the `MeterBarChart`.

- `max` (number): Sets the maximum value for the `MeterBarChart`.

- `showTooltip` (boolean): Controls whether tooltips are displayed.

- `formatter` (formatter function or format option): Formats the value displayed
in the tooltip.

- `thresholds` (array of objects
`{name: string, value: number, color: string, showIndicator?: boolean}`):
Defines threshold values and associated colors.

#### MultiMeterBarChart

To add a
MultiMeterBarChart
to the `DataTable`, follow the steps described in the section on
displaying a MeterBarChart in a table.

Set the `columnType` to `meterbar` in the column definition and use the
`accessor` property to specify the value data to process. Instead of providing a
single numerical value, as for `MeterBarChart`, with `MultiMeterBarChart` you
can provide an array of value objects. Each value object should have the
following structure: `{name: string, value: number, color: string}` as data.

As with the `MeterBarChart`, you can fine-tune the appearance of the
`MultiMeterBarChart` by using the `colorPalette` property to set a custom color
pattern.

When data is provided as value array objects, the `color` and `thresholds` props
in `config` are ignored.

#### Sparkline chart

To pass timeseries data to the `DataTable` and visualize it with a `Sparkline`
chart, set the column's `columnType` to `sparkline` and use the column's
`accessor` to point to the timeseries data that you want to process.

The Sparkline chart in the `DataTable` can be further configured via the column
definition. You can set its color and variant by adding
`config: {color: string, variant: 'line' | 'area' | 'bar'}`. The default
configuration of sparkline is
`config: {color: 'categorical', variant: 'line', showContextValues: false}`.
Additionally, x‑axis boundaries can be configured by setting
`config: { xAxis: { min: 'auto' | 'data-min' | number | Date, max: 'auto' | 'data-max' | number | Date } }`.
Similarly, y‑axis boundaries and scale can be configured by setting
`config: { yAxis: { min: number | 'data-min', max: number | 'data-max', scale: 'linear' | 'log' } }`.
More details on the configuration options can be found here in the
`Sparkline`
documentation.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Columns
- Define column types
- Column sizing
- Control column sizing
- Control column width behavior
- Accessors
- Define header groups
- Customize column header
- Configure column visibility
- Column visibility UI elements
- Control column visibility
- Reset column visibility
- Open column settings programmatically
- Configure column order
- Column order UI elements
- Control column order
- Reset column order
- Configure pinned columns
- Column pinning UI elements
- Control column pinning
- Customize the label of the column settings trigger
- Rows
- Enable interactive rows
- Control interactive rows
- Provide sub-rows
- Configure sub-rows
- Control sub-rows
- Enable expandable rows
- Enable row selection
- Control row selection
- Control row IDs
- Configure row order
- Control row ordering
- Highlight rows
- Define custom comparator
- Cells
- Format cell data
- Customize cell rendering
- Highlight cells
- Layout and format
- Customize visual representation
- Enable full width
- Enable full height
- Fonts
- Text alignment
- Enable line wrap
- Export configuration
- Import configuration
- Enable pagination
- Change page size
- Control pagination
- Use server-side pagination
- Scroll to a given row
- States
- Loading state
- Customize empty state
- Actions and intents
- Configure column actions
- Configure row actions
- Configure selected row actions
- Configure cell actions
- Configure table actions
- Download data
- Enable sorting
- Sort programmatically
- Define sortAccessor
- Define custom sortType
- Configure intents
- Configure intents in toolbar
- Charts in tables
- Gantt chart
- MeterBarChart
- MultiMeterBarChart
- Sparkline chart

### Props

The `DataTable` is a component for building tables which organize information
into rows and columns.

#### DataTableProps

##### Signature:
`export declare type DataTableProps = <> & & & & & & & & & <> & <> & <> & <> & & <> & <> & & & & & ;`

#### DataTableBaseProps
extends |
 | Name | Type | Default | Description
 | `data` | [] | | Data given to the DataTable. Needs to be memoized in order to ensure
performant update cycles.
 | `columns` | <>[] | | Column definition given to the DataTable. Needs to be memoized in order
to ensure performant update cycles.
 | `fullWidth?` | | `false` | Enables DataTable to use the full width of its container.
 | `fullHeight?` | | `false` | Enables DataTable to use the full height of its container.

#### DataTableLineWrapBaseProps
 |
 | Name | Type | Default | Description
 | `onLineWrapChange?` | (lineWrap: ) => | | Callback that is called when the lineWrap state of the table or any column is changed.

#### DataTableLineWrapUncontrolledProps
extends |
 | Name | Type | Default | Description
 | `defaultLineWrap?` | | | Lets you set lineWrap state initially of the entire table or individual columns.
`boolean` values will affect the whole table, whereas `Record` values will let you assign
lineWraps to individual columns.

#### DataTableLineWrapControlledProps
extends |
 | Name | Type | Default | Description
 | `lineWrap?` | | | Lets you control the lineWrap state of the entire table or individual columns.
`boolean` values will affect the whole table, whereas `Record` values will let you assign
lineWraps to individual columns.

#### DataTableColumnFontStyleProps

##### Signature:
`export declare type DataTableColumnFontStyleProps = | ;`

#### DataTableVisualVariantProps
 |
 | Name | Type | Default | Description
 | `variant?` | {
 /**
 * rowSeparation can be set to which will provide lines between rows or
 * can be set to which will provide alternate row coloring.
 * @defaultValue
 */
 rowSeparation?: | | ;
 /**
 * If true provides vertical lines between the columns.
 * @defaultValue false
 */
 verticalDividers?: ;
 /**
 * If true provides a border for the table.
 * @defaultValue true
 */
 contained?: ;
 /**
 * rowDensity adds spacing around the content inside the row
 * with minimal space for , maximum spacing for and
 * being medium spacing.
 * @defaultValue
 */
 rowDensity?: | | ;
 /**
 * fontStyle, sets the font style for the entire data table.
 * This does not overwrite fontStyle set at the lower level, like columns etc.
 * @defaultValue
 */
 fontStyle?: | ;
 /**
 * headers defines if the header rows of the table should be rendered or not.
 * @defaultValue
 */
 headers?: | ;
 /**
 * Determines the vertical alignment for all table cells.
 * If header and body cells should have a different vertical alignment, they can be configured separately.
 * @defaultValue
 */
 verticalAlignment?: | | | {
 header: | | ;
 body: | | ;
 };
 } | |

#### DataTableLoadingStateProps
 |
 | Name | Type | Default | Description
 | `loading?` | | `false` | Displays a loading indicator while the table's columns and/or data are being loaded.

#### DataTableColumnSizingBaseProps
 |
 | Name | Type | Default | Description
 | `resizable?` | | `false` | Enables resizable columns for the table.
 | `onColumnSizingChange?` | (newSizes: ) => | | Callback that triggers when a user finishes resizing a column.

#### DataTableColumnSizingControlledProps
extends |
 | Name | Type | Default | Description
 | `columnSizing?` | | | ColumnSizing state that lets you set the individual column sizes in a controlled scenario.

#### DataTableColumnSizingUncontrolledProps
extends |
 | Name | Type | Default | Description
 | `defaultColumnSizing?` | | | ColumnSizing state that lets you set the individual column sizes in a uncontrolled scenario.

#### DataTableSortingBaseProps
 |
 | Name | Type | Default | Description
 | `sortable?` | | {
 /**
 * When set to true, the table will assume that the data provided by the consumer is already sorted,
 * and will not apply sorting to it.
 */
 manualSort?: ;
 } | `false` | Enables sorting for all columns which do not have it explicitly
disabled with the `disableSorting` prop on the column entry.
 | `onSortByChange?` | (columnSorting: []) => | | Callback triggered when sorting of the column is changed.

#### DataTableSortingControlledProps
extends |
 | Name | Type | Default | Description
 | `sortBy?` | [] | | Controlled property to define the columns the DataTable is sorted by.

#### DataTableSortingUncontrolledProps
extends |
 | Name | Type | Default | Description
 | `defaultSortBy?` | [] | | Uncontrolled property to define the columns the DataTable is sorted by.

#### DataTableColumnVisibilityBaseProps
 |
 | Name | Type | Default | Description
 | `onColumnVisibilityChange?` | (columnVisibility: ) => | | Callback that is called when the ColumnVisibility state of any column is changed.

#### DataTableColumnVisibilityControlledProps
extends |
 | Name | Type | Default | Description
 | `columnVisibility?` | | | Lets you control the ColumnVisibility state of the individual columns.

#### DataTableColumnVisibilityUncontrolledProps
extends |
 | Name | Type | Default | Description
 | `defaultColumnVisibility?` | | | Lets you set the initial ColumnVisibility state of the individual columns.

#### DataTableColumnOrderBaseProps
 |
 | Name | Type | Default | Description
 | `columnOrdering?` | | | Enables column ordering functionality in the table.
 | `onColumnOrderChange?` | (columnOrder: [], trigger: | ) => | | Callback that is called when the column order of any column is changed.
It provides the changed column order along with the underlying trigger that indicates
if the change was triggered by a user interaction or internally.

#### DataTableColumnOrderControlledProps
extends |
 | Name | Type | Default | Description
 | `columnOrder?` | [] | | Lets you control the column order of the individual columns.

#### DataTableColumnOrderUncontrolledProps
extends |
 | Name | Type | Default | Description
 | `defaultColumnOrder?` | [] | | Lets you set the initial column order of the individual columns.

#### DataTableRowOrderBaseProps
 |
 | Name | Type | Default | Description
 | `rowOrdering?` | | {
 /**
 * When enabled, a drag handle is be rendered in the first column for every row.
 */
 enableDragAndDrop?: ;
 /**
 * Allows to disable the dragging of certain rows.
 */
 disableRowDragAndDrop?: (row: ) => ;
 /**
 * Locks rows with disabled drag and drop in place if they are sorted to the start or end of the table.
 */
 lockDisabledRows?: | | ;
 } | `false` | Enables row ordering.
 | `onRowOrderChange?` | (rowOrder: []) => | | Callback triggered when row order is changed.

#### DataTableRowOrderControlledProps
extends`<>` |
 | Name | Type | Default | Description
 | `rowOrder?` | [] | | Ordered set of row ids.

#### DataTableRowOrderUncontrolledProps
extends`<>` |
 | Name | Type | Default | Description
 | `defaultRowOrder?` | [] | | Ordered set of row ids.

#### DataTableRowSelectionBaseProps
 |
 | Name | Type | Default | Description
 | `selectableRows?` | | {
 /**
 * Allows to disable the selection of certain rows.
 */
 disableRowSelection?: (row: ) => ;
 /**
 * Allows to configure if the select all will only select
 * the current page or the entire.
 * @defaultValue
 */
 selectAllBehavior?: | ;
 /**
 * Allows to set a limit on how m items are allowed
 * to be selected. Limit needs to be a positive integer.
 */
 limit?: ;
 } | `false` | Enables row selection. Either accepts a boolean to enable the
row selection on the entire table or a config object.
The config object accepts a function that will get the row data as
the parameter and should return true or false if the row should be
selectable or not. In the config object, the 'select all' behavior
can also be configured and a selection 'limit' can also be set.

Note: For the case where this prop is a config object, it needs
to be memoized, to avoid updates if it is identical. Same as for all
for other props with type object.
 | `onRowSelectionChange?` | (selectedRows: ) => | | Callback triggered when selection is changed.

#### DataTableRowSelectionControlledProps
extends`<>` |
 | Name | Type | Default | Description
 | `selectedRows?` | | | Controlled property to define the selected rows.

#### DataTableRowSelectionUncontrolledProps
extends`<>` |
 | Name | Type | Default | Description
 | `defaultSelectedRows?` | | | Controlled property to define the selected rows.

#### DataTableThresholdProps
 |
 | Name | Type | Default | Description
 | `rowThresholds?` | <>[] | | Configures the thresholds used for the rows highlighting.

#### DataTableSubRowsBaseProps
 |
 | Name | Type | Default | Description
 | `subRows?` | | {
 accessor?: // With a keyof we would have type safety for the objects first level and would be able to suggest and ensure that the key given actually exists in the given row data. To support pathed accessors like 'some.nested' we need to fall back to a .
 | ((row: ) => [] | );
 /**
 * Allows to specify a columnId that the subRow indicator will be injected to.
 * By default, this will be the first visible column provided by the columns prop.
 */
 subRowColumnId?: ;
 /**
 * Allows to specify a function that will evalute if a specific subRows trigger in a row
 * should be disabled.
 */
 disableSubRow?: (row: ) => ;
 } | `false` |
 | `onOpenSubRowsChange?` | (openSubRows: ) => | | Callback triggered when open subrows change.

#### DataTableSubRowsControlledProps
extends`<>` |
 | Name | Type | Default | Description
 | `openSubRows?` | true | | | Currently open sub rows in a controlled scenario.

#### DataTableSubRowsUncontrolledProps
extends`<>` |
 | Name | Type | Default | Description
 | `defaultOpenSubRows?` | true | | | Initially open sub rows in an uncontrolled scenario.

#### DataTableRowInteractivityBaseProps
 |
 | Name | Type | Default | Description
 | `interactiveRows?` | | {
 /**
 * The `autoActivate` setting controls whether a focused row immediately activates it,
 * making stepping through interactive rows with a keyboard more accessible.
 * @defaultValue true
 */
 autoActivate?: ;
 /**
 * Defines a link for an interactive row, enabling navigation to another view or page.
 * @deprecated Please use onActiveRowChange instead.
 */
 link?: (row: ) => ;
 } | `false` | Enables row interactivity.
 | `onActiveRowChange?` | (activeRow: | , event?: ) => | | Callback triggered when active row is changed.

#### DataTableRowInteractivityControlledProps
extends`<>` |
 | Name | Type | Default | Description
 | `activeRow?` | | | | Lets you control the active row.

#### DataTableRowInteractivityUncontrolledProps
extends`<>` |
 | Name | Type | Default | Description
 | `defaultActiveRow?` | | | | Lets you set the initially active row.

#### DataTableDownloadSlotProps
 |
 | Name | Type | Default | Description
 | `excludeColumns?` | [] | | Array of column IDs that can optionally be excluded from the download.
 | `onDownloadData?` | (subset: | | , excludedColumns?: []) => | | Called when table data was downloaded via the toolbar, or programmatically when the slot is configured.

#### DataTableRowIdentification
 |
 | Name | Type | Default | Description
 | `rowId?` | (row: ) => | | Enables identification of rows independent of their index in the array.

### DataTable.Pagination

Use `DataTable.Pagination` to enable pagination.

#### DataTablePaginationBaseProps
extends`, ` |
 | Name | Type | Default | Description
 | `id?` | | | The element's unique identifier. See MDN.
 | `pageSizeOptions?` | [] | `[10, 20, 50, 100, 250, 500, 1000]` | Page size options to be displayed in the page size select.
 | `autoResetPageIndex?` | | `true` | Allows opting out of automatic page index reset when new data is being set.
Be aware that if you turn off `autoResetPageIndex`, you may need to add logic
to handle resetting the pageIndex yourself.
 | `onPageIndexChange?` | (pageIndex: , trigger: | ) => | | Called when the page index changes. Provides the changed page index along with the underlying trigger.
 | `onPageSizeChange?` | (pageSize: ) => | | Handler that is called when the page size changes.

#### DataTablePaginationPageIndexUncontrolledProps
extends |
 | Name | Type | Default | Description
 | `defaultPageIndex?` | | `0` | Initial page index in an uncontrolled scenario.

#### DataTablePaginationPageIndexControlledProps
extends |
 | Name | Type | Default | Description
 | `pageIndex` | | | Current page index in a controlled scenario.

#### DataTablePaginationPageSizeUncontrolledProps
extends |
 | Name | Type | Default | Description
 | `defaultPageSize?` | | `100` | Default number of rows per page (uncontrolled).

#### DataTablePaginationPageSizeControlledProps
extends |
 | Name | Type | Default | Description
 | `pageSize` | | | Number of rows per page (controlled)

#### DataTablePaginationClientSideProps
extends

#### DataTablePaginationServerSideProps
extends |
 | Name | Type | Default | Description
 | `enablePreviousPage` | | | Whether the previous page is available (if not, the go to previous page button should be disabled).
 | `enableNextPage` | | | Whether the next page is available (if not, the go to next page button should be disabled).
 | `totalRowsCount?` | | | The total number of rows.
Will be used to determine the total number of pages to display the indicator "Page X of Y" for server-side pagination.

### DataTable.ColumnActions

Use `DataTable.ColumnActions` to specify user actions for the table columns.

#### DataTableColumnActionsProps
 |
 | Name | Type | Default | Description
 | `children` | <> | | Content for the column actions.
Should be a `TableActionsMenu` directly or a function returning one.
 | `column?` | | | Column id that the given column actions apply to. If left empty, the given column actions
apply to all columns that allow column actions.

### DataTable.CellActions

Use `DataTable.CellActions` to specify user actions for the table cells.

#### DataTableCellActionsProps
 |
 | Name | Type | Default | Description
 | `children` | <> | | Content for the cell actions.
Should be a `TableActionsMenu` directly or a function returning one.
 | `column?` | | ((columnId: ) => ) | | Column ID that the given cell actions apply to. When a function is provided, it receives a
column ID and must return a boolean whether the action should be applied to that column.
If left empty, the actions apply to all cells in columns that allow cell actions.

### TableActionsMenu

Use the `TableActionsMenu` component for configuring column or cell actions.
This component must be returned by the `DataTable.ColumnActions` or
`DataTable.CellActions` function.

### TableActionsMenu.ColumnOrder

Use `TableActionsMenu.ColumnOrder` inside the `TableActionsMenu` to add a menu
item for changing the order of the columns.

### TableActionsMenu.LineWrap

Use `TableActionsMenu.LineWrap` inside the `TableActionsMenu` to add a menu item
for toggling the line wrap of a table column.

### TableActionsMenu.ColumnFontStyle

Use `TableActionsMenu.ColumnFontStyle` inside the `TableActionsMenu` to add a
menu item for toggling the font style of a table column.

### TableActionsMenu.HideColumn

Use `TableActionsMenu.HideColumn` inside the `TableActionsMenu` to add a menu
item for hiding the respective table column.

### TableActionsMenu.CopyItem

Use `TableActionsMenu.CopyItem` inside the `TableActionsMenu` to add a menu item
for copying the cell content to clipboard.

### TableActionsMenu.Item

In addition to the predefined actions, you can provide a custom user action
using the `TableActionsMenu.Item` subcomponent.

For detailed information about the props check out the
`Menu.Item` props.

### TableActionsMenu.Intent

Use `TableActionsMenu.Intent` to render a table action menu item that sends an
intent.

#### MenuIntentProps

##### Signature:
`export declare type MenuIntentProps = | ;`

### TableActionsMenu.Prefix

Use the `TableActionsMenu.Prefix` to add an icon to the left side of a
`TableActionsMenu.Item`.

For detailed information about the props check out the
`Menu.Prefix` props.

### TableActionsMenu.Suffix

Use the `TableActionsMenu.Suffix` to add an icon to the right side a
`TableActionsMenu.Item`.

For detailed information about the props check out the
`Menu.Suffix` props.

### TableActionsMenu.Group

Use the `TableActionsMenu.Group` to group multiple items in the table actions
menu.

For detailed information about the props check out the
`Menu.Group` props.

### TableActionsMenu.Label

Use the `TableActionsMenu.Label` to add a descriptive label to a table actions
menu group.

For detailed information about the props check out the
`Menu.Label` props.

### DataTable.RowActions

Use `DataTable.RowActions` to specify user actions for the table rows.

#### DataTableRowActionsProps
 |
 | Name | Type | Default | Description
 | `children` | (row: , { , , , }: {
 : | | ;
 : ;
 : ;
 }) => <> | |

### DataTable.SelectedRowsActions

Use `DataTable.SelectedRowsActions` to define actions that will be applied to
the selected rows. These actions will replace the `DataTable.TableActions` when
one or multiple rows are selected.

#### DataTableSelectedRowsActionsProps
extends`, , ` |
 | Name | Type | Default | Description
 | `children` | (rows: {
 rowId: ;
 originalRow: ;
 }[]) => | |

### DataTable.DefaultCell

Custom cell renderer wrapper which automatically deals with applying the correct
cell styles.

### DataTable.EmptyState

Use `DataTable.EmptyState` to configure a custom empty state that will be
displayed if no data is available.

### DataTable.TableActions

Use `DataTable.TableActions` to define general table actions that are positioned
at the top of the `DataTable`.

### DataTable.Toolbar

`DataTable.Toolbar` provides a slot where toolbar components can be added.

### DataTable.VisibilitySettings

Use `DataTable.VisibilitySettings` inside the `DataTable.Toolbar` to render the
trigger for the visibility settings overlay in the toolbar. The overlay allows
the user to control the column visibility for all columns.

Prop Table did not receive data

### DataTable.ColumnOrderSettings

Use `DataTable.ColumnOrderSettings` inside the `DataTable.Toolbar` to render the
trigger for the column order settings overlay in the toolbar. The overlay allows
the user to control the column order for all columns.

#### DataTableColumnOrderSettingsProps
 |
 | Name | Type | Default | Description
 | `resetColumnOrder?` | [] | | Column order reset state that will be used to reset and also to enable/disable 'Reset to default'
in column settings modal.

### DataTable.ColumnSettingsTrigger

Use `DataTable.ColumnSettingsTrigger` inside the `DataTable.Toolbar` to
customize the label of the trigger for the column settings overlay in the
toolbar.

#### DataTableColumnSettingsTriggerProps
extends`, ` |
 | Name | Type | Default | Description
 | `children?` | (params: {
 hiddenColumnCount: ;
 totalColumnCount: ;
 defaultLabel: ;
 }) => | | Custom label to be displayed in the column settings trigger.

### DataTable.DownloadData

Use `DataTable.DownloadData` inside the `DataTable.Toolbar` to enable
downloading of the table data. This component contains a menu with the options
for downloading all data, the current page or the selected row data.

### DataTable.Intent

Use `DataTable.Intent` inside the `DataTable.Toolbar` to add intents to the
toolbar.

#### IntentProps

##### Signature:
`export declare type IntentProps = | ;`

### DataTable.LineWrap

Use `DataTable.LineWrap` inside the `DataTable.Toolbar` to add a button for
toggling the line wrap in the table cells.

### DataTable.SelectionChip

The `DataTable.SelectionChip` indicates how many rows are currently selected.

### DataTable.ExpandableRow

Use `DataTable.ExpandableRow` to define an expandable row template which
provides additional information for each table row.

#### DataTableExpandableRowBaseProps
 |
 | Name | Type | Default | Description
 | `children` | (params: {
 row: ;
 }) => | | Define a render function as the child of this slot selection to
control what is rendered in the expanded row section.
 | `onExpandedRowsChange?` | (expandedRows: ) => | | Callback triggered when the state of the expanded row is changed.
 | `disableExpand?` | (row: ) => | | Allows you to disable individual rows from expanding by returning true from the
passed function.

#### DataTableExpandableRowControlledProps
extends`<>` |
 | Name | Type | Default | Description
 | `expandedRows?` | true | | | Controlled state for the expanded rows of the DataTable.

#### DataTableExpandableRowUncontrolledProps
extends`<>` |
 | Name | Type | Default | Description
 | `defaultExpandedRows?` | true | | | Uncontrolled state for the expanded rows of the DataTable.

### DataTable.ExpandableRowWrapper

Wrapper helper for `DataTable.ExpandableRow` that will automatically sync
specific style properties like row padding for `rowDensity` variant settings.

#### DataTableExpandableRowWrapperProps
extends`, , , <>`

### DataTableRef

#### DataTableRef
 |
 | Name | Type | Default | Description
 | `element` | | | | Root element ref of the component.
 | `getConfig` | () => | | Returns the current config of the DataTable.
 | `downloadData` | (subset: | | , excludeColumns?: []) => | | Downloads all data, the data on the current page or the selected data.
Optionally, columns can be excluded by their IDs.
 | `scrollToRow` | (rowId: , align?: | | ) => | | Scrolls the table to the row with the given `rowId`, aligning the row at the given scroll position.
 | `openColumnSettings` | (columnSettings?: ) => | | Opens the column settings modal.
 | `getDisplayedRowIds` | () => [] | | Returns the row IDs in their current display order, reflecting active sorting and the current page when pagination is enabled.

### DataTableConfig

Current configuration option that can be shared via intents.

#### DataTableConfig
 |
 | Name | Type | Default | Description
 | `pagination?` | {
 defaultPageIndex?: ;
 defaultPageSize?: ;
 } | | Pagination props to initialize pagination.
 | `columnVisibility?` | [] | | For specifying which columns should be visible or hidden.
 | `fullWidth?` | <>[] | `false` | For controlling whether to take up the full parent container width.
 | `fullHeight?` | <>[] | `false` | For controlling whether to take up the full parent container height.
 | `lineWrap?` | [] | `false` | For controlling whether the content of a cell should be line wrapped.
 | `fontStyle?` | [] | `'text'` | For customizing the font style across the table or within individual columns.
 | `resizable?` | [] | `false` | For controlling whether the columns are resizable.
 | `selectableRows?` | <>[] | `undefined` | For controlling whether individual rows can be selected.
 | `rowThresholds?` | <>[] | `[]` | For configuring the highlighting of individual rows.
 | `sortable?` | [] | `false` | For controlling whether the columns are sortable.
 | `variant?` | [] | | For customizing the appearance of the table.

### DataTableColumnDef

Mapping type for the columns prop that can contain either display columns or
group columns.

#### DataTableColumnDef

##### Signature:
`export declare type DataTableColumnDef = | ;`

### DataTableRowData

#### DataTableRowData

##### Signature:
`export declare type DataTableRowData = | object | [];`

### DataTableAlignmentColumnDef

Extension interface to extend the types of the `columnDefinition` from the
TanStack table.

#### DataTableAlignmentColumnDef
 |
 | Name | Type | Default | Description
 | `alignment?` | | | | | Defines the text alignment inside the column cell.

### DataTableSortingColumnDef

Extension interface to extend the types of the `columnDefinition` from the
TanStack table.

#### DataTableSortingColumnDef
 |
 | Name | Type | Default | Description
 | `disableSorting?` | | | Setting to true disables sorting for this column even
if sorting is enabled globally.
 | `sortType?` | | | | | <> | `'text'` | Used to compare two rows of data and order them correctly.
If a function is passed, it must be memoized.
 | `sortDescFirst?` | | | Setting to true means the first sorting direction for
this column will be descending instead of ascending.
 | `sortInverted?` | | | Setting this to true means the underlying sorting
direction will be inverted but the UI will not. This
could be useful for example where a lower score is better.
 | `sortAccessor?` | | ((row: ) => ) | | Optional - to be used for providing the value used for sorting.
This enables the value used for sorting to be different from
the value returned by the accessor. For example, if the accessor
returns an object, the sortAccessor may return a number or string
field within the object.

### DataTableColumnSort

Rule for sorting a column.

#### DataTableColumnSort
 |
 | Name | Type | Default | Description
 | `id` | | | Column ID.
 | `desc` | | `false` | Descending sorting direction.

### DataTableThresholdColumnDef

Extension interface to extend the types of the `columnDefinition` from the
TanStack table to support column level thresholds.

#### DataTableThresholdColumnDef
 |
 | Name | Type | Default | Description
 | `thresholds?` | <>[] | | Configures the thresholds used for the cell highlighting.

### DataTableColumnTypesColumnDef

Combined ruleset of column types and their matching configurations.

#### DataTableColumnTypesColumnDef

##### Signature:
`export declare type sColumnDef = {
 columnType: ;
 config?: ;
} | {
 columnType: ;
 config?: ;
} | {
 columnType: ;
 formatter?: | ;
 config?: ;
} | {
 columnType: ;
 formatter?: ;
 config?: ;
} | {
 columnType: ;
 formatter?: ;
 config?: ;
} | {
 columnType?: ;
 formatter?: ;
 config?: ;
} | {
 columnType: ;
 formatter?: , | | | | | >;
 config?: ;
} | {
 columnType: ;
 config?: ;
} | {
 columnType?: ;
 formatter?: ;
 config?: ;
} | {
 columnType: ;
 formatter?: ;
 config?: ;
} | {
 columnType: ;
 formatter?: ;
 config?: ;
};`

### DataTableColumnType

Available column types for the DataTable.

#### DataTableColumnType

##### Signature:
`export declare type DataTableColumnType = | | | | | | | | | | | ;`

### DataTableCellFormatter

DataTable column definition formatter options.

#### DataTableCellFormatter

##### Signature:
`export declare type DataTableCellFormatter = | | | ;`

### DataTableLineWrapState

Defines the shape of the LineWrap state within the TanStack tables state.

#### DataTableLineWrapState

##### Signature:
`export declare type DataTableLineWrapState = | ;`

### DataTableGlobalLineWrapAction

Global line wrap action for the DataTable to be used in the DataTable.Toolbar.

### DataTableColumnFontStyleState

Defines the shape of the FontStyle state within the TanStack tables state.

#### DataTableColumnFontStyleState

##### Signature:
`export declare type DataTableColumnFontStyleState = ;`

### DataTableColumnSizingState

DataTable columnSizing state represented with a columnId key and a pixel size
value.

#### DataTableColumnSizingState

##### Signature:
`export declare type DataTableColumnSizingState = ;`

### DataTableThresholdRule

Threshold configuration that can be applied to highlight something matching the
id.

#### DataTableThresholdRule

##### Signature:
`export declare type DataTableThresholdRule = {
 comparator: | | | | | ;
 value: ;
 /** Accessor or function to pick the value from the rowData that should be compared against. */
 accessor?: | ((row: ) => );
} | {
 /** The operator being used to compare the object value with the threshold value. */
 comparator: | ;
 /** The threshold value to compare the object value to. */
 value: ;
 /** Accessor or function to pick the value from the rowData that should be compared against. */
 accessor?: | ((row: ) => );
} | {
 /** Custom comparator function that is called with the row data. */
 comparator: (rowData: ) => ;
};`

### DataTableRowThreshold

Threshold configuration that can be applied to highlight something matching the
id.

#### DataTableRowThreshold

##### Signature:
`export declare type DataTableRowThreshold = <> | <>;`

### DataTableColumnThreshold

Threshold configuration that can be applied to highlight something matching the
id.

#### DataTableColumnThreshold

##### Signature:
`export declare type DataTableColumnThreshold = <> | <>;`

### DataTableSingleRowThreshold

Threshold configuration that can be applied to highlight something matching the
id.

#### DataTableSingleRowThreshold

##### Signature:
`export declare type DataTableSingleRowThreshold = <> & {
 rules?: ;
} & ({
 type: ;
 color: ;
} | {
 type: ;
 backgroundColor?: ;
 color?: ;
});`

### DataTableCombinedRowThresholds

Threshold configuration that can be applied to highlight something matching the
id.

#### DataTableCombinedRowThresholds

##### Signature:
`export declare type DataTableCombinedRowThresholds = {
 rules: <>[];
} & ({
 type: ;
 color: ;
} | {
 type: ;
 backgroundColor?: ;
 color?: ;
});`

### DataTableColumnVisibilityState

Configuration object for the column visibility state. To define the column
visibility for a column, provide the column ID along with the desired boolean
value.

#### DataTableColumnVisibilityState

##### Signature:
`export declare type DataTableColumnVisibilityState = ;`

### DataTableVisibilityColumnDef

Extension interface to extend the types of the columnDefinition from the
TanStack table.

#### DataTableVisibilityColumnDef
 |
 | Name | Type | Default | Description
 | `disableColumnHiding?` | | | Controls the ability of the given column to toggle it's visibility.
This setting will affect if the column will be hidable in column actions or via
the modal controls of the DataTable toolbar.

### DataTableDownload

DataTable slot definition for the Download action.

#### DataTableDownloadSlotProps
 |
 | Name | Type | Default | Description
 | `excludeColumns?` | [] | | Array of column IDs that can optionally be excluded from the download.
 | `onDownloadData?` | (subset: | | , excludedColumns?: []) => | | Called when table data was downloaded via the toolbar, or programmatically when the slot is configured.Still have questions?Find answers in the Dynatrace Community
- DataTable.Pagination
- DataTable.ColumnActions
- DataTable.CellActions
- TableActionsMenu
- TableActionsMenu.ColumnOrder
- TableActionsMenu.LineWrap
- TableActionsMenu.ColumnFontStyle
- TableActionsMenu.HideColumn
- TableActionsMenu.CopyItem
- TableActionsMenu.Item
- TableActionsMenu.Intent
- TableActionsMenu.Prefix
- TableActionsMenu.Suffix
- TableActionsMenu.Group
- TableActionsMenu.Label
- DataTable.RowActions
- DataTable.SelectedRowsActions
- DataTable.DefaultCell
- DataTable.EmptyState
- DataTable.TableActions
- DataTable.Toolbar
- DataTable.VisibilitySettings
- DataTable.ColumnOrderSettings
- DataTable.ColumnSettingsTrigger
- DataTable.DownloadData
- DataTable.Intent
- DataTable.LineWrap
- DataTable.SelectionChip
- DataTable.ExpandableRow
- DataTable.ExpandableRowWrapper
- DataTableRef
- DataTableConfig
- DataTableColumnDef
- DataTableRowData
- DataTableAlignmentColumnDef
- DataTableSortingColumnDef
- DataTableColumnSort
- DataTableThresholdColumnDef
- DataTableColumnTypesColumnDef
- DataTableColumnType
- DataTableCellFormatter
- DataTableLineWrapState
- DataTableGlobalLineWrapAction
- DataTableColumnFontStyleState
- DataTableColumnSizingState
- DataTableThresholdRule
- DataTableRowThreshold
- DataTableColumnThreshold
- DataTableSingleRowThreshold
- DataTableCombinedRowThresholds
- DataTableColumnVisibilityState
- DataTableVisibilityColumnDef
- DataTableDownload

---

## SimpleTable

`/design/components/tables/SimpleTable/`

The `SimpleTable` component is a simplified version of the `DataTable`. It is
designed to handle small sets of data and markdown representation. It does not
feature sorting, resizing, filtering, or virtualization and behaves like a
native HTML table.

### Import

`tsx
import { SimpleTable } from '@dynatrace/strato-components/tables';
`

### Use Cases

#### Configure text alignment

By default, text within a cell is left-aligned and vertically centered. To
explicitly control the text alignment for a column, set the `alignment` property
in the column definition.

#### Configure the variant

The visual look of the `SimpleTable` can be adjusted using the `variant` prop.
It allows you to configure the font style, a contained border, the row density,
as well as row and column separation.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use Cases
- Configure text alignment
- Configure the variant

### Props

The `SimpleTable` component is a simplified version of the `DataTable`. It is
designed to handle small sets of data and markdown representation. It does not
feature sorting, resizing, filtering, or virtualization and behaves like a
native HTML table.

#### SimpleTableProps

##### Signature:
`export declare type SimpleTableProps = <> & & & & ;`

#### SimpleTableBaseProps
extends |
 | Name | Type | Default | Description
 | `data` | [] | | Data given to the SimpleTable. Needs to be memoized in order to ensure
performant update cycles.
 | `columns` | <>[] | | Column definition given to the SimpleTable. Needs to be memoized in order
to ensure performant update cycles.
 | `variant?` | {
 /**
 * rowSeparation can be set to which will provide lines between rows or
 * can be set to which will provide alternate row coloring.
 * @defaultValue
 */
 rowSeparation?: | | ;
 /**
 * If true provides vertical lines between the columns.
 * @defaultValue false
 */
 verticalDividers?: ;
 /**
 * If true provides a border for the table.
 * @defaultValue true
 */
 contained?: ;
 /**
 * rowDensity adds spacing around the content inside the row
 * with minimal space for , maximum spacing for and
 * being medium spacing.
 * @defaultValue
 */
 rowDensity?: | | ;
 /**
 * fontStyle, sets the font style for the entire data table.
 * This does not overwrite fontStyle set at the lower level, like columns etc.
 * @defaultValue
 */
 fontStyle?: | ;
 } | | Configures the variant on the data table, impacting the visual representation.Still have questions?Find answers in the Dynatrace Community

---

## convertToColumns

`/design/components/tables/convertToColumns/`

The `convertToColumns` function takes a set of Grail field types and converts it
to table columns that can be used in the `DataTable`.

### Import

`tsx
import { convertToColumns } from '@dynatrace/strato-components/tables';
`

### Use cases

Pass an array in the format of `RangedFieldTypes` and receive an array of
columns that can be plugged into the DataTable.

#### Convert query records to table columns

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Convert query records to table columns

---

