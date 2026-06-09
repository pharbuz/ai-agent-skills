# Charts (data visualizations)

Strato design-system components in the **Charts (data visualizations)** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## AnnotationsChart

`/design/data-visualizations/charts/AnnotationsChart/`

The `AnnotationsChart` is a visualization tool designed to highlight significant
events or data points on a timeline or other graph types. It allows you to
annotate specific moments with labels or markers, providing additional context
or insights directly within the chart. This chart can be used standalone or
integrated with other chart types, such `HistogramChart` or `TimeseriesChart`,
to enrich the data presentation by drawing attention to each event.

OverviewProperties

### Import

`tsx
import { AnnotationsChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `AnnotationsChart` consists of at least on track, each containing a
collection of markers. Learn more about the marker's structure
here.

#### Size

By default, the chart will use all the available container size up to the
maximum height required to show all the tracks. This maximum height can be
changed by providing a value in the `height` prop of the `AnnotationsChart`. You
can set any css value to the height and if a number is passed to this prop
without any unit specified, it will be treated as `px`.

Similarly, the chart width can be controlled using the `width` prop. It accepts
CSS units like `"100%"` or `"500px"`, or numeric values which are treated as
pixels. By default, the chart will take `100%` of its container width.

#### AnnotationsChart.Track

Tracks in the AnnotationsChart are horizontal bands that group related markers.
Each track can have a `label`, which is displayed on the left side, and can
represent a specific category of data.

Label width for tracks can be set by `labelWidth` property in AnnotationsChart
component

The track is able to provide prop values for the markers inside of it, like
`color` and `symbol`, which will be used as default values in case they are not
provided on the marker level.

#### AnnotationsChart.Marker

Markers are the individual data points or events within a track, which can
represent a single value or a range. Each marker can have a `title`, `symbol`,
and `description` to provide more context.

When the `symbol` is provided, it will be shown as marker content. As a
fallback, if no `symbol` is provided, the `title` will be chosen as content.

In the case no `symbol` or `title` are provided, no content will be shown.

##### Text Overflow

To deal with text longer than the width of the marker containing it, an option
between 'expand' and 'truncate' could be chosen. When 'expand' is selected the
width of the marker will try to expand to fit all the content within, only
applying an ellipsis when the width in the track is not enough to fit all the
content. When 'truncate' is selected the width of the marker will be respected
and the content will be cropped to fit it. You can specify if this truncation
should be made at the 'start', 'middle' or 'end' of the text with the option
'truncateMode'.

#### AnnotationsChart.Tooltip

It's possible to customize the tooltip by providing a custom HTML template.

To define the template, use a callback handler that receives the relevant marker
data. This data includes both the current hovered marker and any overlapping
markers that are close by, allowing the creation of a detailed and informative
tooltip.

If no tooltip template is provided, then the default tooltip will be shown
instead. Optionally, tooltip can be opted out by setting `hidden` prop to true.

#### User actions

A user action is a creator-defined interaction with a given node in the hive.
Basic interactions include copying the node name and inspecting the underlying
data of it. In order to enable user actions, the `ChartSeriesAction`
subcomponent needs to be appended within the `AnnotationsChart`. More
subcomponents can be added within this component, for instance the
`ChartSeriesAction.Item`, where custom logic can be applied. `Intents` could be
added as part of the series action as well with `ChartSeriesAction.Intent`.

#### Chart states

##### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application.

In case of an error thrown inside the chart, a predefined error message will be
shown.

If you prefer to create your own error screen to preserve styles and information
shown, you can create your own error state presenter.

##### EmptyState

The `EmptyState` subcomponent serves as a fallback when there is no data
available to display in a chart. Its purpose is to provide a user-friendly way
of informing the user about the current situation.

When no data is provided to the chart, a predefined empty state message will be
displayed.

An empty state message can be customized using `AnnotationsChart.ErrorState`
subcomponent.

##### Loading

The `AnnotationsChart` is able to show the default loading indicator by setting
the `loading` prop to `true`.

#### X-axis

The `AnnotationsChart` component provides a `AnnotationsChart.XAxis`
subcomponent to configure chart's X-Axis and scale. The X-Axis is visible by
default. To hide it the `hidden` prop should be set to `true`.

To customize chart's min and max scale values, the `min` and `max` props can be
used. By default, chart's scale min and max are calculated from the data. Be
aware, that customizing the scale values may filter out some markers that are
outside of custom scale range.

##### Numerical x-axis

The numerical x-axis has additional configuration options, like `scale`,
`formatter` and `unit`.

The `scale` option can be used to choose between linear and logarithmic scale.
Take into account that the logarithmic scale just supports positive numbers
(excluding 0), so if negative or zero values are provided, the scale will fall
back to linear.

The `formatter` or `unit` props can be used to customise the formatting of the
x-axis ticks and the tooltip numerical data. If both properties are present, the
`formatter` will take precedence over `unit`.

##### Numbers to time conversion

The `scale` prop offers an additional option that allows for the conversion of
timestamps to dates. By setting the scale to time, all numeric data used in the
markers will be parsed as dates. Consequently, the `min` and `max` props of the
axis can accept both number and date types.

In case some invalid number that can't be converted to date is provided, it will
be filtered out of the original dataset.

#### Multiple chart configuration

Given certain situations it can be helpful to share a common chart configuration
across several `AnnotationsChart` instances. To avoid repeating the same
configuration in all instances, the `AnnotationsChartConfig` provider can be
used. It accepts an object where the keys are either props of the
`AnnotationsChart` component, or the corresponding object representation of each
one of the `AnnotationsChart` subcomponents props. (`AnnotationsChart.XAxis` and
`AnnotationsChart.Tooltip`).

A specific configuration of a `AnnotationsChart` instance will take precedence
over the one specified in the `AnnotationsChartConfig`.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Size
- AnnotationsChart.Track
- AnnotationsChart.Marker
- AnnotationsChart.Tooltip
- User actions
- Chart states
- X-axis
- Multiple chart configuration

### Props

The `AnnotationsChart` is a visualization tool designed to highlight significant
events or data points on a timeline or other graph types. It allows you to
annotate specific moments with labels or markers, providing additional context
or insights directly within the chart. This chart can be used standalone or
integrated with other chart types, such `HistogramChart` or `TimeseriesChart`,
to enrich the data presentation by drawing attention to each event.

OverviewProperties

#### AnnotationsChartProps
extends |
 | Name | Type | Default | Description
 | `labelWidth?` | | `60` | Custom width of the tracks labels.
 | `loading?` | | `false` | Show the loading indicator when truly.
 | `height?` | | | `300px` | The height of the chart. If a number is passed, it will be treated as px.
 | `width?` | | | `"100%"` | The width of the chart. If a number is passed, it will be treated as px.
 | `textOverflow?` | | | Truncate will keep markers width
 | `truncateMode?` | | | Where to truncate the text

#### AnnotationsActionsHandler

##### Signature:
`export declare type AnnotationsActionsHandler = (data?: ) => | ;`

#### AnnotationsActionsPayload
 |
 | Name | Type | Default | Description
 | `start` | | | | Selected marker start
 | `end?` | | | | Selected marker end
 | `title?` | | | Selected marker title
 | `description?` | | | Selected marker description
 | `symbol?` | | | Selected marker symbol

### AnnotationsChart.Track

#### AnnotationsTrackProps
 |
 | Name | Type | Default | Description
 | `color?` | | | Defines the marker background for all the markers inside a track, supporting any valid CSS color.
It will be overridden by any particular marker that has color prop defined.
 | `label?` | | | The track label
 | `symbol?` | | | Defines the marker symbol for all the markers inside a track, which can be a letter, an emoji, an icon or a Unicode character
It will be overridden by any particular marker that has symbol prop defined.
 | `hidden?` | | `false` | Specify whether a track should hide.

### AnnotationsChart.Marker

#### AnnotationsMarkerProps

##### Signature:
`export declare type AnnotationsMarkerProps = & ( | );`

#### BaseMarkerProps
 |
 | Name | Type | Default | Description
 | `title?` | | | The marker title
 | `symbol?` | | | The marker symbol, which can be a letter, an emoji, an icon or a Unicode character
 | `description?` | | | The marker description
 | `color?` | | `Colors.Charts.Categorical.Color01.Default` | The marker background, supporting any valid CSS color
 | `priority?` | | `0` | The priority of the marker, which can be used to specify which marker will be rendered on top of the other, in case of overlapping,
and also will specify the order of the tooltip items in case of having the same range/value.
 | `hidden?` | | `false` | Specify whether a particular marker should hide.

#### TimeMarkerProps
 |
 | Name | Type | Default | Description
 | `start` | | | Starting point of the marker
 | `end?` | | | Ending point of the marker. If not set, the marker will be a timestamp instead of a timeframe

#### NumericalMarkerProps
 |
 | Name | Type | Default | Description
 | `start` | | | Starting point of the marker
 | `end?` | | | Ending point of the marker. If not set, the marker will represent a value instead of a range

### AnnotationsChart.EmptyState

`AnnotationsChart.EmptyState` provides a slot where the Empty state wrapper can
be set.

#### EmptyStateProp
 |
 | Name | Type | Default | Description
 | `children` | | |

### AnnotationsChart.ErrorState

`AnnotationsChart.ErrorState` provides a slot where the Error state wrapper can
be set.

#### ErrorStateProps
 |
 | Name | Type | Default | Description
 | `children` | | ((errorMessage: ) => .) | |

### AnnotationsChart.XAxis

`AnnotationsChart.XAxis` provides a slot to configure the X-Axis of the chart.

#### XAxisProps

##### Signature:
`export declare type XAxisProps = & ( | | );`

#### BaseXAxisProps
 |
 | Name | Type | Default | Description
 | `label?` | | | Defines x-axis label
 | `hidden?` | | `false` | Defines whether x-axis is showed or not

#### TimeXAxisProps
 |
 | Name | Type | Default | Description
 | `min?` | | | Defines minimum time x-axis domain.
As a default, it takes the value from the data
 | `max?` | | | Defines maximum time x-axis domain.
As a default, it takes the value from the data

#### TimestampXAxisProps
 |
 | Name | Type | Default | Description
 | `min?` | | | | Defines minimum numerical x-axis domain.
As a default, it takes the value from the data
 | `max?` | | | | Defines maximum numerical x-axis domain.
As a default, it takes the value from the data
 | `type` | | | If the value is set to time, it enables data casting from timestamps to Date objects

#### NumericalXAxisProps
 |
 | Name | Type | Default | Description
 | `min?` | | | Defines minimum numerical x-axis domain.
As a default, it takes the value from the data
 | `max?` | | | Defines maximum numerical x-axis domain.
As a default, it takes the value from the data
 | `type?` | | | `'linear'` | Defines x-axis scale type. If the value is set to time, it enables data casting from timestamps to Date objects
 | `formatter?` | | | | Defines x-axis tick formatting
 | `unit?` | | | Defines x-axis unit

### AnnotationsChart.Tooltip

`AnnotationsChart.Tooltip` provides a slot to configure the Tooltip of the
chart.

#### AnnotationsTooltipProps
 |
 | Name | Type | Default | Description
 | `hidden?` | | `false` | Defines whether tooltip show be hidden or not
 | `children?` | | | The ChoroplethLayer tooltip handler template

#### AnnotationsTooltipHandler

##### Signature:
`export declare type AnnotationsTooltipHandler = (hoveredMarkers: [], closeMarkers: [][]) => ;`

#### AnnotationsTooltipItem
 |
 | Name | Type | Default | Description
 | `start` | | | | Starting point of the marker
 | `end?` | | | | Ending point of the marker. If not set, the marker will represent a value instead of a range
 | `color` | | | The marker background color
 | `title?` | | | The maker title
 | `description?` | | | The marker description
 | `symbol?` | | | The marker symbolStill have questions?Find answers in the Dynatrace Community
- AnnotationsChart.Track
- AnnotationsChart.Marker
- AnnotationsChart.EmptyState
- AnnotationsChart.ErrorState
- AnnotationsChart.XAxis
- AnnotationsChart.Tooltip

---

## CategoricalBarChart

`/design/data-visualizations/charts/CategoricalBarChart/`

The `CategoricalBarChart` visually displays the frequencies or values of
distinct categories using rectangular bars. Each bar's length or height
corresponds to the quantity or value associated with a specific category, making
it easy to compare the relative differences among categories.

OverviewProperties

### Import

`tsx
import { CategoricalBarChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `CategoricalBarChart` expects a data structure composed of an array of
`categories` with a `value` and an optional `unit` as a string.

- category: Represents the name of the service being measured as a string.

- value: Indicates the quantitative measure associated with the category. The
specified value can either be a number or a key-value pair. In order to render
a single bar for each category, specify a number as the value. When a record
is specified as a key-value pair, each pair will render a bar within a group
in the parent category. The key is used as the name of the dimension for that
bar.

- unit: Specifies the unit of measurement for the value.

`tsx
[ { category: 'Q1', value: { 'R&D': 140000, HR: 40000, Sales: 500000, Support: 400000 }, unit: '$', },];
`

Learn more about the data format here.

#### Size

By default, the chart will use all the available container size up to a maximum
height of 300 pixels and a width of 100% of the container. This maximum height
and width can be changed by providing a value in the `height` and `width` props
of the `CategoricalBarChart`. Both accept a number (treated as pixels) or a CSS
string (e.g., `"500px"`, `"60%"`).

#### Change the layout

The layout prop specifies how bars are drawn within the chart. The `horizontal`
value renders the bar horizontally and the `vertical` option vertically. By
default, the bars are displayed in a `vertical` layout.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the
`CategoricalBarChart`. More subcomponents can be added within this component,
for instance `ChartSeriesAction.Item`, where you can provide a custom action
that will appear in the legend menu. That action can execute any custom logic in
its `onSelect` callback or get disabled via a `disabled` prop. `Intents` could
be added as part of the series action as well with `ChartSeriesAction.Intent`.

#### Change the group mode

When having multiple dimensions for each category, `groupMode` determines how
those dimensions are grouped. The `stacked` option stacks bars on top of each
other, whereas the `grouped` option displays them sequentially (next to one
another). Stacked bars are recommended when the relationship between dimensions
and their contribution to the total matters. Grouped bars are useful for
comparing values between dimensions and categories. This option doesn't have any
effect when there's a single value per category. By default, bars are `stacked`.

#### Change the chart color/s

The `CategoricalBarChart` provides several ways to customize the appearance of
your data:

- Predefined Color Palettes: Choose from a set of built-in color palettes.

- Custom Colors: Define your own color schemes.

- Color Rules: Apply conditional coloring based on data values.

##### Using Color Palettes

The `CategoricalBarChart` accepts a `colorPaletteMode` prop that can be set to
either `single-color` (default) or `multi-color`. In `single-color` mode, all
categories take the first color of the palette, while in `multi-color` mode,
colors are applied to categories by index or by value.

For more details about available palettes and custom colors, see
Chart Coloring.

##### Using Color Rules

For more advanced coloring scenarios, you can use the
`CategoricalBarChart.ColorRule` slot to apply conditional coloring based on your
data values. Here are some examples:

For more details about using color rules, see the
Color Rules
section.

Apart from all these options for providing a color palette, the
`CategoricalBarChart` also offers the ability to override colors for specific
series. When a color override is specified, it takes precedence over the color
that would otherwise be assigned from the color palette. However, it does not
affect the colors assigned to other series. This allows for fine-grained control
over the appearance of individual series within the chart. A color override is
done by category. We should specify the category name we want overridden and
provide the desired color to the `CategoricalBarChart` data using a `color`
prop.

#### Value representation

By default, values within a chart are displayed as is - with their absolute
value (e.g. 3.14 kB). However, this can be changed so that instead of absolute
values, relative values are used. Relative values indicate the proportion that a
given dimension contributes to the sum (100%) of a given category. The
`valueRepresentation` prop can be used to change this behavior. For categories
with only a single dimension, the relative value is based on the maximum value
within the given dimension.

#### Legend customization

The purpose of the legend is to provide additional identifying information for
the chart without needing to interact with it directly.

##### Visibility

The legend for the `CategoricalBarChart` is shown by default in a chart with
more than one dimension per category, and otherwise it is hidden. In order to
hide or show the legend, you need to set the value of `legend.hidden` on the
subcomponent.

##### Legend position

By default, the legend of the `CategoricalBarChart` is positioned automatically
(`{position: "auto"}`). This option prioritizes the legend placement to the
right of the chart area. When the chart width is reduced, the legend is
repositioned beneath the chart area. You can also explicitly set the chart's
legend position to `right` or `bottom` with the position prop.

##### Legend ratio

By default, the legend occupies `25%` of the container width, in the case where
the legend is positioned on the right and `25%` of the container height if the
legend position is on the bottom.

It is possible to override the default legend ratio by setting a custom
percentage value for the ratio prop. The expected value is in the range of
`5-80`. Values out of expected ranges will roll back to the default legend
ratio.

#### Tooltip customization

Tooltips can be used to display additional detailed information about a selected
data point. A tooltip will be shown when hovering the chart at a certain
distance to a datapoint. The tooltip `variant` defines whether the tooltip
should contain data points from all the dimensions within a category (grouped)
or only the closest one (single). By default, the variant is `single`.

#### Truncation Mode

The purpose of truncation is to gracefully handle extra long labels within data
visualization components. By changing the value of this property, you have
control over where truncation is applied within charts. By default, the
truncation is applied to the `middle` of labels with the use of an ellipsis.
Truncation can, however be changed to instead be applied at the `start` or `end`
of data visualization component labels.

#### Axis customization

The category axis is defined as the axis containing the names of the chart's
categories. The value axis contains numeric values. Both will be positioned
either on the x- or y-axis, depending on the selected `layout`. When it's
`horizontal`, the category axis is the x-axis and the value axis is the y-axis,
and when it's `vertical`, vice versa.

##### Category axis

In the category axis, tick labels have a limited space, which depends on the
number of categories and the chart's width. If the tick label is larger than the
available space, it's truncated with ellipsis in the middle. `tickLabelLayout`
can be used to change the orientation of the tick labels to make better use of
the available space. The `label` prop can optionally be used to set the title
for the axis.

The `maxSize` prop defines the maximum growth in pixels of the axis. If the
`maxSize` value is bigger than the space that the axis has to display, the
`maxSize` value will be omitted.

##### Value axis

In the value axis, a `min` and `max` can be used in order to set the extents of
the chart. If no values are specified, these extents will be derived from the
data. When all the values are positive, the `min` is 0 and the `max` will be the
largest value. When all the values are negative, the `min` is the lowest value,
and the `max` is 0. If there are mixed values, the `min` is the lowest value,
and the `max` is the highest value. The `label` prop can optionally be used to
set the title for the axis. The value axis allows one to choose the type of
scale by setting the `scale` property. This property lets you select between two
options: `linear` or `logarithmic` (log). A linear scale distributes values
evenly, making it suitable for data with a consistent rate of change. Meanwhile,
a logarithmic scale distributes values according to a logarithm, making it ideal
for data that spans a wide range or grows exponentially.

#### Formatter

As the `CategoricalBarChart` expects an array of categories with a value and an
optional unit, by default this optional unit will be appended to the specified
value, if it is included. There are two other options in the formatter that
allow for greater customization. The first option enables you to prepend the
unit to the value, while the second option enables you to ignore the original
unit and append a custom string instead. Additionally, there is a custom
formatter option available to allow you to change the input unit to one of your
choice, e.g.: if the input unit is `bits`, you are able to switch and display
the unit as `bytes`, correctly formatted. The formatted value is applied in the
axis ticks, as well as in the tooltip and the axis magnifier. The use cases
below outline each of these scenarios.

#### Thresholds

Thresholds are used to mark meaningful ranges or values on a
`CategoricalBarChart` and they add contextual information to a numerical axis.
There are two variants of thresholds:

- a specific point represented on the value axis and a line across.

- a range - or filled area - represented by a pill on the value axis and a band
across.

##### Point and Range

There is no limit defined for the number of threshold ranges or points that can
be used in a single `CategoricalBarChart`. The threshold will be positioned on
the left axis if the layout is vertical or on the bottom axis if the layout is
horizontal.

##### Points and Ranges on Vertical Layout

##### Points and Ranges on Horizontal Layout

There are three different types of threshold markers:

Range filled, where the value range is defined in order to display the
threshold band. The stroke lines are not drawn unless the pill is hovered.

Range stroke-only variant, where a value range is defined in order to display
the threshold band represented by dashed stroke lines. The stroke lines become
continuous lines when the pill is hovered.

Point, where only one value is required to display the threshold. It's
represented by a dashed line and when the point is hovered the line becomes a
continuous line.

##### Stroke Only Ranges on Vertical Layout

##### Stroke Only Ranges on Horizontal Layout

#### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application. The fallback UI occupies the full
width and height of the chart, ensuring that users are still provided with a
meaningful interface even in the presence of errors.

The `ErrorState` subcomponent offers a versatile feature that enables it to
handle both default and custom error messages. You can provide a custom message
through the `ErrorState` subcomponent, which will then override the default
error message. This flexibility allows developers to tailor error messages to
their specific needs and requirements, ensuring a more personalized and
informative user experience.

The `ErrorState` subcomponent provides the flexibility to format custom error
messages using HTML, which allows for enhanced customization and adaptability in
presenting error information. Furthermore, it is possible to incorporate the
original thrown error within your custom error message, ensuring that users
receive comprehensive and relevant information when an error occurs.

#### EmptyState

The `EmptyState` subcomponent serves as a fallback when there is no data
available to display in a chart. Its purpose is to provide a user-friendly way
of informing the user about the current situation. When there is no data, a
fallback UI is displayed occupying the full width and height of the chart, along
with a default message.

A feature of `EmptyState` is its ability to handle custom messages. It provides
the flexibility to format custom messages using HTML, which allows for enhanced
customization and adaptability in presenting error information.

#### Loading

The `loading` prop is a boolean value that can be passed to the
`CategoricalBarChart` component to control its loading state. When the loading
prop is set to true, the loading indicator appears in the middle of the chart
plot to inform the user that the component is currently fetching or processing
data. When the loading prop is set to false, the component should display its
regular content.

#### Download data as CSV

The `CategoricalBarChart` component supports download data in CSV format using a
toolbar button. To enable this feature, a `CategoricalBarChart.DownloadCSV`
subcomponent must be provided to the `CategoricalBarChart` component. On click
of the download button, raw data will be downloaded as a CSV file.

The CSV file contains the following columns:

- `category` - the name of the category (dimension)

- `value` - the value of the category

- `key` - the name of the second dimension (in case of multiple dimensions)

It's also possible to programmatically trigger the download of the CSV file by
calling the `downloadData` method on the `CategoricalBarChart` instance
reference.

#### Intent options

The `CategoricalBarChart` supports intent options in the toolbar. The intents
appear in the toolbar's dropdown menu, allowing users to perform actions such as
sharing a chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `CategoricalBarChart`, use the
`CategoricalBarChart.Intent` subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrates different intent options in
CategoricalBarChart:

#### Toolbar

The toolbar is where you can download data and use added Intents. It is
displayed by default, but to customize it, you can add the
`CategoricalBarChart.Toolbar` subcomponent, which supports the optional `hidden`
and `placement` props.

##### Behavioral tracking

The `CategoricalBarChart.Toolbar` subcomponent supports behavioral tracking
attributes that are spread onto the toolbar root element. This allows tracking
of toolbar interactions such as menu opens, mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `CategoricalBarChart.Toolbar` to
attach tracking metadata. See `BehaviorTrackingProps` for the full list of
supported attributes.

#### Styling

The `CategoricalBarChart` also accepts custom styling, which can be set using
the props `className` and/or `style` as in a regular html element.Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Size
- Change the layout
- Series actions
- Change the group mode
- Change the chart color/s
- Value representation
- Legend customization
- Tooltip customization
- Truncation Mode
- Axis customization
- Formatter
- Thresholds
- Error state
- EmptyState
- Loading
- Download data as CSV
- Intent options
- Toolbar
- Styling

### Props

The `CategoricalBarChart` visually displays the frequencies or values of
distinct categories using rectangular bars. Each bar's length or height
corresponds to the quantity or value associated with a specific category, making
it easy to compare the relative differences among categories.

OverviewProperties

#### CategoricalBarChartProps
extends`, , ` |
 | Name | Type | Default | Description
 | `data` | [] | | Data object for the categorical bar chart
 | `height?` | | | `300px` | Chart height. When a number is specified, is considered as pixels, otherwise a valid height string is expected.
 | `width?` | | | `100%` | Chart width. When a number is specified, it's treated as pixels,
otherwise a valid width string is expected.
 | `layout?` | | `'vertical'` | Whether the bars are displayed in a 'vertical' or 'horizontal' layout.
 | `groupMode?` | | `'stacked'` | Strategy used for grouping the bars within a category. "stacked" will mount one on top of each other, and "grouped" will place one next to the other
 | `colorPalette?` | | | `"categorical"` | Color palette to be used for the bar category.
 | `valueRepresentation?` | | `"absolute"` | The way values are represented. "absolute" will display the value as it is, and "relative" displays a percentage value considering the other dimensions values within a category.
 | `seriesActions?` | (series: ) => | | Category actions to be shown in the legend and tooltip actions
 | `truncationMode?` | | `'middle'` | Truncation mode to use (start, middle, end)
Applied to all the parts that truncate text.
 | `colorPaletteMode?` | | `"single-color" - each bar gets the same color` | Mode in which bars are colored when single dimension data is shown
 | `loading?` | | `false` | Show the loading indicator when truthy.

### CategoricalBarChart.Legend

To configure the legend, add `CategoricalBarChart.Legend` to the categorical bar
chart.

#### CategoricalBarChartLegendProps

##### Signature:
`export declare type CategoricalBarChart = ;`

### CategoricalBarChart.Tooltip

To configure the tooltip, add `CategoricalBarChart.Tooltip` to the categorical
bar chart.

#### CategoricalBarChartTooltipProps
 |
 | Name | Type | Default | Description
 | `variant` | | | Tooltip variant. 'single' displays only the closest category, and 'grouped' all the category within a category.

### CategoricalBarChart.CategoryAxis

To configure the category axis, add `CategoricalBarChart.CategoryAxis` to the
categorical bar chart.

#### CategoricalBarChartCategoryAxisProps
 |
 | Name | Type | Default | Description
 | `tickLabelLayout?` | | `'horizontal'` | Whether the tick labels are displayed in a 'vertical' or 'horizontal' layout.
 | `label?` | | |
 | `maxSize?` | | | Max size in pixels for the category axis. Size depends on the position this axis is assigned to – left axis will use width, bottom axis will use height.
If there's no enough space for this maxSize, category axis will only take the available space for it.

### CategoricalBarChart.ValueAxis

To configure the value axis, add `CategoricalBarChart.ValueAxis` to the
categorical bar chart.

#### CategoricalBarChartValueAxisProps
 |
 | Name | Type | Default | Description
 | `label?` | | |
 | `min?` | | |
 | `max?` | | |
 | `formatter?` | | | | Handler that is called for every tick value to be formatted.
 | `scale?` | | | The scale of the value axis.

### CategoricalBarChart.ThresholdIndicator

`CategoricalBarChart.ThresholdIndicator` provides a slot for defining
annotations in the chart.

#### CategoricalBarChartThresholdIndicatorProps
 |
 | Name | Type | Default | Description
 | `data` | | | The threshold data to be graphed by the component
 | `color` | | | The unique color picked in HEX, RGB, Color Token or HSL.
 | `strokeOnly?` | | | Whereas to show the ranges filled or only the strokes
 | `label?` | | `"Threshold"` | Label to be shown in the threshold tooltip.

### CategoricalBarChart.EmptyState

`CategoricalBarChart.EmptyState` provides a slot where the Empty state wrapper
can be set.

#### EmptyStateProp
 |
 | Name | Type | Default | Description
 | `children` | | |

### CategoricalBarChart.ErrorState

`CategoricalBarChart.ErrorState` provides a slot where the Error state wrapper
can be set.

#### ErrorStateProps
 |
 | Name | Type | Default | Description
 | `children` | | ((errorMessage: ) => .) | |

### CategoricalBarChart.Intent

`CategoricalBarChart.Intent` provides a slot to set intents that will appear in
the toolbar.

#### IntentProps

##### Signature:
`export declare type IntentProps = | ;`

### CategoricalBarChart.ColorRule

`CategoricalBarChart.ColorRule` provides a slot to apply conditional coloring to
your chart series based on their values or names.

#### ColorRuleProps

##### Signature:
`export declare type ColorRuleProps = {
 valueAccessor?: ;
 comparator: ;
 matchValue: ;
} & ;`

### CategoricalBarChart.toolbar

The `CategoricalBarChart.toolbar` slot allows you to customize or hide the
chart's toolbar.

#### CompactToolbarProps

##### Signature:
`export declare type CompactToolbarProps = & {
 hidden?: ;
 placement?: [];
};`

### CategoricalBarChart.DownloadCSV

The `CategoricalBarChart.DownloadCSV` slot allows users to download the data as
a CSV file.Still have questions?Find answers in the Dynatrace Community
- CategoricalBarChart.Legend
- CategoricalBarChart.Tooltip
- CategoricalBarChart.CategoryAxis
- CategoricalBarChart.ValueAxis
- CategoricalBarChart.ThresholdIndicator
- CategoricalBarChart.EmptyState
- CategoricalBarChart.ErrorState
- CategoricalBarChart.Intent
- CategoricalBarChart.ColorRule
- CategoricalBarChart.toolbar
- CategoricalBarChart.DownloadCSV

---

## ChartColoring

`/design/data-visualizations/charts/ChartColoring/`

- Chart coloring

## Chart coloring

### Predefined Color Palettes

The `colorPalette` prop allows you to set the chart color palette to be used
within the chart (i.e. to color the chart's series). Depending on the selected
color palette, the color is then applied to the series by index or by value.

When utilizing the index-based method, colors are allocated to the series in a
sequential manner. Once the last color in the sequence is reached, the series
will restart from the beginning with the same color sequence. The following
color palettes employ the index-based approach for color assignment:

- `categorical (default)`

- `swamps`

- `fireplace`

- `blue-steel`

- `purple-rain`

All color palettes can be used in reverse order by adding the suffix `-inverted`
to the palette name. For example, `categorical` would become
`categorical-inverted`

#### Color Palette by Index on Timeseries Chart

When employing the value-based approach, colors are automatically allocated to
correspond with the series name. For instance, a series labeled as "Error" would
be associated with the color denoted as "error". The correlation between a
series name and color value is not influenced by letter case, ensuring a
case-insensitive matching process. In cases where a series does not align with
any color palette value, the color assignment is determined based on the index
of the series. The available color palettes and their respective admissible
values are as follows:

- `log-status ( error, warn, info, none )`

- `apdex ( excellent, good, fair, poor, unacceptable )`

- `log-level ( emergency, alert, critical, severe, error, warn, notice, debug, info, none )`

- `vulnerability-risk-level ( critical, high, medium, low )`

- `vulnerability-status ( affected, resolved, muted )`

If you want to use an inverted color palette using the value-based approach, it
will only work in cases where the name does not match a category. In such cases,
the order of the colors in that palette will be inverted.

#### Color Palette by Value on Categorical Bar Chart

### Custom Color Palettes

There is also the option to supply a personalized collection of colors, which
will be subsequently applied to the chart series based on their index. To
accomplish this, you can furnish an array of color strings using the
`colorPalette` prop. The provided color strings can utilize any format supported
by web browsers, including RGB, HSL, HEX, as well as color tokens.

#### Custom Color Palette Value on Donut Chart

### Custom Color Maps

In addition, there is the capability to assign colors that correspond to
specific chart series names. To achieve this, you can provide a map consisting
of series name-color pairs, where the series name acts as the key and the
corresponding color as the value. The provided color strings can utilize any
format supported by web browsers, including RGB, HSL, HEX, as well as color
tokens. To implement this functionality, you can pass the aforementioned map to
the colorPalette prop.

#### Custom Color Palette Value on Pie Chart

### Overriding Series Color with ColorRule

The `ColorRule` component provides a powerful way to apply conditional coloring
to your chart series based on their values or names. This is particularly useful
for highlighting specific data points or applying business logic to your
visualizations.

#### Basic Usage

`ColorRule` can be used as a subcomponent of most of the chart to apply
conditional coloring rules. Each rule consists of:

- `comparator`: The comparison operator to use (e.g., 'equals', 'greater-than',
'starts-with', 'contains', 'matches-phrase')

- `matchValue`: The value to match against

- `color` or `colorPalette`: The color or palette to apply when the rule matches

- `valueAccessor` (optional): The data property to evaluate. When omitted, each
chart uses its own default — typically the primary display value (e.g., the
y-axis value for series charts, the node name for TreeMap). Check each chart's
documentation for its specific default.

#### Example: Color Rules in Action

#### Available Comparators

Numerical comparisons

- `less-than`: Value is strictly less than `matchValue`

- `less-or-equal`: Value is less than or equal to `matchValue`

- `greater-than`: Value is strictly greater than `matchValue`

- `greater-or-equal`: Value is greater than or equal to `matchValue`

Equality comparisons

- `equals`: Exact match

- `not-equals`: Does not match exactly

String comparisons

- `starts-with`: Value starts with the specified string

- `not-starts-with`: Value does not start with the specified string

- `ends-with`: Value ends with the specified string

- `not-ends-with`: Value does not end with the specified string

- `contains`: Value contains the specified string

- `not-contains`: Value does not contain the specified string

- `matches-phrase`: Value matches the specified phrase or pattern

- `not-matches-phrase`: Value does not match the specified phrase or pattern

#### Color Application

- When multiple rules match a series, the last matching rule takes precedence

- If no rules match, the series uses the default color from the chart's color
palette

- You can use either a specific color (hex, rgb, color token) or a color palette

#### Best Practices

- Order your rules from most general to most specific — since the last
matching rule takes precedence, more specific rules should come last

- Use color palettes for consistent theming across related series

- Consider color accessibility when choosing custom colors

- Test with different data sets to ensure rules work as expected

Note: Color rules take precedence over the chart's color palette but can
be overridden by direct color assignments in the data series.

Still have questions?Find answers in the Dynatrace Community
- Predefined Color Palettes
- Color Palette by Index on Timeseries Chart
- Color Palette by Value on Categorical Bar Chart
- Custom Color Palettes
- Custom Color Palette Value on Donut Chart
- Custom Color Maps
- Custom Color Palette Value on Pie Chart
- Overriding Series Color with ColorRule
- Basic Usage
- Example: Color Rules in Action
- Available Comparators
- Color Application
- Best Practices

---

## ChartInteractions

`/design/data-visualizations/charts/ChartInteractions/`

- Chart interactions

## Chart interactions

### Use cases

Chart interactions enable additional possibilities for end users to interact
with the data plotted within the chart area. The interactive options currently
supported within the `TimeseriesChart`, the `HistogramChart` and the `XYChart`
are zoom, pan, and select.

To incorporate these interactions, add the corresponding slot components inside
the chart:

`tsx
TimeseriesChart data={data}> TimeseriesChart.Zoom /> TimeseriesChart.Pan /> TimeseriesChart.Select />TimeseriesChart>
`

For the `XYChart`, every X-axis can opt-in or opt-out for enabling these
interactions by specifying two props: `disableZoom` and `disablePan` (for more
information, see Zoom and Pan).

Chart interactions can be triggered using keyboard shortcuts or by using the
chart toolbar. The toolbar is enabled by default. To customize the toolbar
(e.g., hide it or change its placement), add the toolbar slot to the chart:
, , or
.

#### Explore

The explore functionality is the default mode, and it allows you to inspect the
data within the chart. It allows you to select an area to zoom along the X-axis.
This mode is enabled by default and works in combination with the `Zoom` and
`Select` slots.

You can optionally trigger this mode from the keyboard by pressing `E` while the
chart has focus.

#### Pan

Once a user has zoomed into the plotted data on a chart, panning can optionally
be enabled. Panning allows users to navigate left and right along the X-axis
whilst in a zoomed-in state. To enable this functionality, add the Pan slot to
the chart:

`tsx
TimeseriesChart data={data}> TimeseriesChart.Pan />TimeseriesChart>
`

This interaction is enabled by default in `XYChart`, `TimeseriesChart` and
`HistogramChart`

You can optionally trigger this mode from the keyboard by pressing `P` while the
chart has focus.

Once you have triggered this mode:

- Pressing ← (Left Arrow) will pan to the left. You can also press `Shift`
to increase the speed of pan movement.

- Pressing → (Right Arrow) will pan to the right. You can also press
`Shift` to increase the speed of pan movement.

#### Select

The select functionality allows users to select a specific area in the chart.
Selection can be used to display detailed information about data points inside
the selected area and/or to zoom in to the selected area. The select interaction
is enabled by default for `XYChart`, `TimeseriesChart` and `HistogramChart`. You
can explicitly add it to customize behavior:

Select can be triggered by clicking and dragging on the chart area. To zoom in
on the selected area, press `Enter`.

`tsx
TimeseriesChart data={data}> TimeseriesChart.Select actions={(selectedSeries) => ( ChartSeriesAction> ChartSeriesAction.Item onSelect={() => console.log(selectedSeries)}> Custom action ChartSeriesAction.Item> ChartSeriesAction> )} />TimeseriesChart>
`

Upon selecting an area, the chart will display a tooltip with the selected
area's start and end timestamps, duration of the area, and amount of data points
and series. The tooltip can be dismissed by pressing `Esc`. The selected area
can include custom actions and intents. You can define custom actions using the
`actions` prop on the `Select` slot.

#### Zoom

The zoom functionality allows users to zoom in to the chart's plotted data by a
fixed point along the X-axis. The chart supports zoom in (incremental) and zoom
out (decremental) actions.

To enable zoom interactions, add the Zoom slot to the chart:

`tsx
TimeseriesChart data={data}> TimeseriesChart.Zoom />TimeseriesChart>
`

This interaction is enabled by default.

You can optionally zoom in/out different ways by first focusing the chart:

- Pressing `Cmd` (`Ctrl` in Windows) + the mouse wheel, will generate a zoom
in/out trigger.

- Pressing `Cmd` + ↑ (Up Arrow) will zoom in.

- Pressing `Cmd` + ↓ (Down Arrow) will zoom out.

- Pressing `Cmd` + click will zoom in.

- Pressing `Cmd` + pressing `Shift` + click will zoom out.

- Pressing `Cmd` + clicking and dragging draws a zoom area and zooms in on mouse
up.

#### Reset

Reset will restore the chart to its initial state.

You can optionally trigger this action from the keyboard by pressing `R` while
the chart has focus.

- Double-clicking on any part of the chart will trigger a reset.

The following charts have all interactions enabled (explore, zoom, pan, select
with custom actions).

It's also possible to programmatically trigger all the previously described
interactions by calling their methods on the `TimeseriesChart` instance
reference. The available options are: `exploreMode`, `zoomMode`, `panMode`,
`zoomIn`, `zoomOut` and `reset`.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Use cases
- Explore
- Pan
- Select
- Zoom
- Reset

---

## ChartStates

`/design/data-visualizations/charts/ChartStates/`

- Chart states

## Chart states

### Use cases

#### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application. The fallback UI occupies the full
width and height of the chart, ensuring that users are still provided with a
meaningful interface even in the presence of errors.

The `ErrorState` subcomponent offers a versatile feature that enables it to
handle both default and custom error messages. You can provide a custom message
through the `ErrorState` slot, which will then override the default error
message. This flexibility allows developers to tailor error messages to their
specific needs and requirements, ensuring a more personalized and informative
user experience.

The `ErrorState` subcomponent provides the flexibility to format custom error
messages using HTML, which allows for enhanced customization and adaptability in
presenting error information. Furthermore, it is possible to incorporate the
original thrown error within your custom error message, ensuring that users
receive comprehensive and relevant information when an error occurs.

#### EmptyState

The `EmptyState` subcomponent serves as a fallback when there is no data
available to display in a chart. Its purpose is to provide a user-friendly way
of informing the user about the current situation. When there is no data, a
fallback UI is displayed occupying the full width and height of the chart, along
with a default message.

A feature of `EmptyState` is its ability to handle custom messages. It provides
the flexibility to format custom messages using HTML, which allows for enhanced
customization and adaptability in presenting error information.

#### Loading

The `loading` prop is a boolean value that can be passed to a `Chart` component
to control its loading state. When the loading prop is set to true, the loading
indicator appears in the middle of the chart plot to inform the user that the
component is currently fetching or processing data. When the loading prop is set
to false, the component should display its regular content.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Use cases
- Error state
- EmptyState
- Loading

---

## DonutChart

`/design/data-visualizations/charts/DonutChart/`

The `DonutChart` is a variation of a pie chart with a circular shape and a hole
in the center. It divides the total amount into proportional slices, each
representing a category or value. The key difference is the presence of the
central hole, which allows placing additional information in the available
space.

OverviewProperties

### Import

`tsx
import { DonutChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `DonutChart` expects a data structure composed of an array of `slices` and
an optional `unit` as a string.

Each `slice` of the chart should contain the following attributes:

- Category: The name or label for the slice.

- Value: The numerical value representing the size of the slice.

- Color: An optional color assigned to the slice.

Unit: An optional string representing the unit of measurement for the values.

`tsx
{ slices: [ { category: 'EMEA', value: 66, }, ], unit: '$',}
`

Learn more about the data format here.

#### Change the size of a chart

By default, the chart will use the width and height of the available container
while using a 1:1 aspect ratio. The height of the container is 300 pixels by
default, but both a width and a height specified in pixels can be manually set.
If a number is passed to this prop without any unit specified, it will be
treated as `px`.

#### Labels

By default, slice labels are enabled. In order to hide all the labels in the
chart, add the subcomponent configuration .

Labels that don't fit a specific slice will be automatically hidden independent
of the configuration value setting.

The default values for the labels will be `relative` but you can also set it to
the `absolute` value, using the `valueType` prop

#### Change the chart color/s

The `DonutChart` provides several ways to customize the appearance of your data:

- Predefined Color Palettes: Choose from a set of built-in color palettes.

- Custom Colors: Define your own color schemes.

- Color Rules: Apply conditional coloring based on data values.

##### Using Color Palettes

The `DonutChart` provides a set of predefined color palettes and it also accepts
custom color palettes. See coloring for more
details.

##### Direct Color Assignment

You can directly assign colors to specific slices by including a `color`
property in your data. This takes precedence over the color palette.

##### Using Color Rules

For more advanced coloring scenarios, you can use the `DonutChart.ColorRule`
slot to apply conditional coloring based on your data values. This is
particularly useful for highlighting specific data points or applying business
logic to your visualizations.

Color rules can be applied based on different criteria:

- Value-based rules: Color slices based on their numeric value

- Category-based rules: Color specific categories

- Date-based rules: Color based on date comparisons

- Custom property rules: Color based on any property in your data

For more details about available comparators and options, see the
Color Rules
section.

#### Grouping

The grouping defines a way to aggregate multiple slices into a single one.

The slices are grouped depending on a given `threshold` prop. All the slices
with a value that match the input threshold will be part of the group.

It is possible to specify three different types of thresholds:

- `relative`: The threshold is the relative value of the slices (distribution in
percentage). All values lower than the threshold will be part of the group.

- `absolute`: The threshold is the absolute value of the slices. All values
lower than the threshold will be part of the group.

- `number-of-slices`: The threshold is the ordinal number of the slices. Once
the number of slices specified in the threshold is reached, all the others
will be grouped.

By default, the group name is `Other`. This value can be changed by providing it
in the configuration via the `name` prop.

To configure custom groups, use the subcomponent configuration
. If the group configuration is not provided, the
grouping is relative: 2% as default.

#### Legend customization

The purpose of the legend is to provide additional identifying information for
the chart without needing to interact with it directly.

##### Visibility

The legend for the `DonutChart` will be shown by default, but it can be
optionally hidden by making use of the `hidden` prop on the subcomponent.

##### Legend position

By default, the legend of the `DonutChart` is positioned automatically
(`{position: "auto"}`) to the right if it has space or to the bottom if there's
no right space. It is also possible to customize the chart's legend position by
setting the desired position: `right` or `bottom`.

##### Legend ratio

By default, the legend occupies `75%` of the container width, in the case where
the legend is positioned on the right and `25%` of the container height if the
legend position is on the bottom.

It is possible to override the default legend ratio by setting a custom
percentage value for the ratio prop. The expected value should be in the range
of `5-80`. Values out of expected ranges will roll back to the default legend
ratio.

#### Truncation Mode

The purpose of truncation is to gracefully handle extra long tooltips or legends
within data visualization components. By changing the value of this property,
you have control over where truncation is applied within charts. By default, the
truncation is applied to the `middle` value with the use of an ellipsis.
Truncation can, however be changed to instead be applied at the `start` or `end`
of data visualization component elements.

#### Formatter

As the `DonutChart` expects an array of categories with a value and an optional
unit, by default this optional unit will be appended to the specified value, if
it is included. There are two other options in the formatter that allow for
greater customization. The first option enables you to prepend the unit to the
value, while the second option enables you to ignore the original unit and
append a custom string instead.

Additionally, there is a custom formatter option available to allow you to
change the input unit to one of your choice, e.g.: if the input unit is `bits`,
you are able to switch and display the unit as `bytes`, correctly formatted. The
formatted value will appear in the chart tooltip. The use cases below outline
each of these scenarios.

#### Total value and inner content

The donut chart component provides the possibility to display custom content
within the empty space at its center.

To achieve this, you can utilize the subcomponent. There
are two approaches to passing the content to be rendered. The first option is to
use the subcomponent and insert a basic React Node or JSX template.
Alternatively you can use the function which exposes certain internal
information as a parameters. The parameters of the function provide access to
various details, such as the `absolute value` and `relative value` of the
selected slices, as well as the dimensions of the square area where the element
will be rendered.

#### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application. The fallback UI occupies the full
width and height of the chart, ensuring that users are still provided with a
meaningful interface even in the presence of errors.

#### EmptyState

The `EmptyState` subcomponent serves as a fallback when there is no data
available to display in a chart. Its purpose is to provide a user-friendly way
of informing the user about the current situation. When there is no data, a
fallback UI is displayed occupying the full width and height of the chart, along
with a default message.

#### Loading

The `loading` prop is a boolean value that can be passed to the `DonutChart`
component to control its loading state. When the loading prop is set to true,
the loading indicator appears in the middle of the chart plot to inform the user
that the component is currently fetching or processing data. When the loading
prop is set to false, the component should display its regular content.

#### Toolbar

The toolbar allows you to download data and use added Intents. Displayed by
default, it can be customized by adding the `DonutChart.Toolbar` subcomponent,
which supports the `hidden` and `placement` props.

##### Behavioral tracking

The `DonutChart.Toolbar` subcomponent supports behavioral tracking attributes
that are spread onto the toolbar root element. This allows tracking of toolbar
interactions such as menu opens, mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `DonutChart.Toolbar` to attach
tracking metadata. See `BehaviorTrackingProps` for the full list of supported
attributes.

#### Download data as CSV

The `DonutChart` component allows data to be downloaded in CSV format via a
toolbar button. To enable this feature, add the `DonutChart.DownloadCSV`
subcomponent to the `DonutChart`. Clicking the button will download the raw data
as a CSV file.

The CSV file contains the following columns:

- `category` - the name of the category

- `value` - the value of the category

- `unit` - the unit of the category

It's also possible to programmatically trigger the download of the CSV file by
calling the `downloadData` method on the `DonutChart` instance reference.

#### Intent options

The `DonutChart` supports intent options in the toolbar. The intents appear in
the toolbar's dropdown menu, allowing users to perform actions such as sharing a
chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `DonutChart`, use the `DonutChart.Intent` slot, which
contains different props:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

#### Styling

The `DonutChart` also accepts custom styling, which could be set using the props
`className` and/or `style`, as a regular html element

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change the size of a chart
- Labels
- Change the chart color/s
- Grouping
- Legend customization
- Truncation Mode
- Formatter
- Total value and inner content
- Error state
- EmptyState
- Loading
- Toolbar
- Download data as CSV
- Intent options
- Styling

### Props

The `DonutChart` is a variation of a pie chart with a circular shape and a hole
in the center. It divides the total amount into proportional slices, each
representing a category or value. The key difference is the presence of the
central hole, which allows placing additional information in the available
space.

OverviewProperties

#### DonutChartProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `data` | | | Categorical data of the chart.
 | `width?` | | | `100%` | The width of the chart. A number or a string with accepted CSS units is expected.
 | `height?` | | | `300px.` | The height of the chart. If a number is passed, it will be treated as px.
 | `colorPalette?` | | | `'categorical'.` | Set of Color palette to be used in charts.
 | `formatter?` | | | | Custom Formatter for the chart
 | `truncationMode?` | | `'middle'` | Truncation mode to use (start, middle, end)
Applied to all the parts that truncate text.
 | `seriesActions?` | (slice: ) => | | Exposed callback to display series actions for a slice
 | `loading?` | | `false` | Show the loading indicator when truly.

#### LabelsConfig
 |
 | Name | Type | Default | Description
 | `hidden?` | | `false (all the labels are displayed).` | Hides the slice labels.
 | `valueType?` | | `'relative'` | Display the label with a relative or absolute value.

#### ThresholdConfig
 |
 | Name | Type | Default | Description
 | `type` | | `'relative'.` | Type of the grouping threshold. Can be "relative", "absolute" or "number-of-slices".
 | `value` | | | Value of the group threshold.
Default is dynamically calculated depending on the chart size for relative and absolute. 10 in case of number-of-slices.

#### GroupConfig
 |
 | Name | Type | Default | Description
 | `name?` | | `'Other'.` | Name of the group.
 | `threshold` | | | The threshold for the group.

### DonutChart.Toolbar

`DonutChart.Toolbar` is a slot to hide or to configure the toolbar.

#### BaseToolbarProps
extends`, ` |
 | Name | Type | Default | Description
 | `hidden?` | | `false` | Decides if the toolbar is visible or hiddenStill have questions?Find answers in the Dynatrace Community
- DonutChart.Toolbar

---

## GaugeChart

`/design/data-visualizations/charts/GaugeChart/`

A Gauge Chart is a circular chart that displays information on a numeric scale.
It's great for showing performance metrics or progress towards a goal.

OverviewProperties

### Import

`tsx
import { GaugeChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `GaugeChart` expects a numerical value as an input. This value needs to be
passed to the visualization's `value` prop as a `Number`.

You can also provide custom `min` and `max` props to set the scale of the
`GaugeChart`, and if none are provided, the default `min` will be 0 and `max`
will be 100.

Learn more about the data format here.

#### Object values

The `GaugeChart` accepts object values in addition to numeric values. When
passing an object value, a `valueAccessor` prop needs to be specified to
indicate which field should be used as the gauge's display value.

In the example above, the gauge displays the value from the `value` field, while
ColorRules evaluate against other fields using their own `valueAccessor` prop.
When multiple rules match, the first matching rule takes precedence.

#### Change the chart color/s

The `GaugeChart` provides several ways to customize the appearance of your
gauge:

- Direct Color Assignment: Set a single color for the entire gauge arc.

- Color Rules: Apply conditional coloring based on the gauge's value.

##### Direct Color Assignment

The `GaugeChart` allows you to customize an arc with a custom color. It accepts
a `color` prop that can be set to any valid color string that utilizes a format
supported by web browsers, including RGB, HSL and HEX.

##### Using Color Rules

For more advanced coloring scenarios, you can use the `GaugeChart.ColorRule`
slot to apply conditional coloring based on the gauge's value. This is
particularly useful for creating visual indicators for different value ranges.

Color rules can be applied based on the gauge's value using different
comparators:

- `'greater-than'`

- `'less-than'`

- `'greater-or-equal'`

- `'less-or-equal'`

- `'equals'`

In the example above, we demonstrate several ways to use color rules:

- Basic color rules: Changing colors based on value thresholds

- With default color: Shows how rules override the default color

- Multiple rules: Demonstrates how multiple rules work together

When multiple rules match, the most specific rule (highest `matchValue` for
'greater' comparators, lowest for 'less' comparators) will take precedence.

You can combine color rules with threshold indicators to create clear visual
cues for different value ranges in your gauge charts.

For more details about available comparators and options, see the
Color Rules
section.

#### Customize chart information

There are some subcomponents that can be used on the `GaugeChart` to display
more information about the chart: and
.There are three ways to configure the
 slot:

- No slot is defined: The component does not display any labels.

- Slot is defined without a child component: The component automatically
generates default labels using the `min`, `max`, and `value` props, applying
the specified formatter prop for consistent formatting.

- Slot is defined with a child component: The provided child component is used
directly as the label, and no automatic formatting is applied.

#### Add more context to a GaugeChart

To provide additional context in a GaugeChart, you can enhance it with icons or
emojis using the `prefixIcon` prop. This prop accepts a `ReactNode`, allowing
you to display a symbol—such as an icon, emoji, single character, glyph, or a
Design System icon—before the value. The symbol will appear to the left of the
chart’s value.

#### Sizing

Different sizes can be set on the `GaugeChart` to display the information. By
default, the chart will use all the available container size up to a maximum
height of 300 pixels. This maximum height can be changed by providing a value in
the `height` prop of the `GaugeChart.` If a number is passed to this prop
without any unit specified, it will be treated as `px`. You can also specify the
`width` prop, and it works in the same way.

Resizing the chart will especially affect the `label`. If a `string` is provided
to the `label` slot, both the arc and the strings will grow accordingly.
However, size will not be affected if another type of element is provided as
`label`, but size can be modified manually. The arc will resize either way.

#### Thresholds

Thresholds are used to mark meaningful values on a `GaugeChart`. In order to set
one or multiple thresholds, you can use the
slot. These Thresholds have a `value` prop to define them. You can also
optionally display the threshold indicator via the `showIndicator` prop and
customize their color by using the prop `color`.

#### Add tooltip

The `GaugeChart` has a default Tooltip to display additional information and
will be shown when the user hovers over the segment. You can customize the label
displayed in the tooltip by passing a `name` prop. If no `name` is provided, it
defaults to `"Value"`.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous templates. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the `GaugeChart`.
More subcomponents can be added within this component, for instance
`ChartSeriesAction.Item`, where you can provide a custom action that will appear
in the legend menu. That action can execute any custom logic in its `onSelect`
callback or get disabled via a `disabled` prop. `Intents` could be added as part
of the series action as well with `ChartSeriesAction.Intent`.

#### Intent options

The `GaugeChart` supports intent options in the toolbar. The intents appear in
the toolbar's dropdown menu, allowing users to perform actions such as sharing a
chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `GaugeChart`, use the `GaugeChart.Intent`
subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in GaugeChart:

#### Formatter

The `GaugeChart` has a formatter prop that accepts any function to provide
format to the relevant chart values. One of the uses of this formatter can be to
attach a custom unit or string to the value. The default formatter shows the
value without any format.

Additionally, there is a custom formatter option available that allows you to
change the input unit to one of your choice, e.g.: if the input unit is `bits`,
you are able to switch and display the unit as `bytes`, correctly formatted. The
formatted value will appear in the chart tooltip. The use cases below outline
each of these scenarios.

#### Styling

The `GaugeChart` also accepts custom styling, which could be set using the props
`className` and/or `style`, as a regular html element.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Object values
- Change the chart color/s
- Customize chart information
- Add more context to a GaugeChart
- Sizing
- Thresholds
- Add tooltip
- Series actions
- Intent options
- Formatter
- Styling

### Props

A Gauge Chart is a circular chart that displays information on a numeric scale.
It's great for showing performance metrics or progress towards a goal.

OverviewProperties

#### GaugeChartProps

##### Signature:
`export declare type GaugeChartProps = | ;`Prop Table did not receive dataStill have questions?Find answers in the Dynatrace Community

---

## HistogramChart

`/design/data-visualizations/charts/HistogramChart/`

A `HistogramChart` is a type of graph that represents the distribution of
numerical data. It’s constructed by dividing the entire range of values into a
series of intervals—known as bins and then counting how many values fall into
each interval. The bins are typically of equal size and are adjacent to each
other, with no gaps. Each bin is represented by a bar, where the height of the
bar reflects the frequency or count of data points within that interval

OverviewProperties

### Import

`tsx
import { HistogramChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `HistogramChart` expects a data structure composed of an array of `bins`, a
`name` as a string, an optional `unit` as a string or Unit and optional `color`
as a string.

Each `bin` represents a continuous range of values. A bin is defined by two key
parameters: the range (from and to), which determines its width, and the count
or frequency (value), which determines its height.

`tsx
{ name: 'Series 1', bins: [ { from: 0, to: 10, value: 0, } ] }
`

Learn more about the data format here.

##### Uneven Bin Widths

The `HistogramChart` accommodates uneven bin widths, providing a clearer
representation of the data. Each bin corresponds to a specific range of values
and these ranges can vary from one bin to another.

##### Overlapped and Stacked Bins

In some instances of the `HistogramChart`, when bins are not perfectly aligned
along the x-axis, the resulting bars may overlap. Conversely, if a bar aligns
perfectly, it will be stacked.

ℹ️ If you are interested in how to prepare your data for passing it to the
this article
might

#### Size

By default, the chart will use all the available container size up to a maximum
height of 300 pixels and width of 100%. This height and width can be changed by
providing a value in the `height` and `width` props of the `HistogramChart`. If
a number is passed to these props, it will be treated as `px`. If a string is
passed, it will be treated as a CSS string.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the
`HistogramChart`. More subcomponents can be added within this component, for
instance `ChartSeriesAction.Item`, where you can provide a custom action that
will appear in the legend menu. That action can execute any custom logic in its
`onSelect` callback or get disabled via a `disabled` prop. `Intents` could be
added as part of the series action as well with `ChartSeriesAction.Intent`.

#### Change the chart color/s

The `HistogramChart` provides several ways to customize the appearance of your
data:

- Predefined Color Palettes: Choose from a set of built-in color palettes.

- Custom Colors: Define your own color schemes.

- Color Rules: Apply conditional coloring based on data values.

##### Using Color Palettes

The `HistogramChart` provides a set of predefined color palettes and it also
accepts custom color palettes. See coloring for
more details.

##### Direct Color Assignment

You can directly assign colors to specific series by including a `color`
property in your series data. This takes precedence over the color palette.

##### Using Color Rules

For more advanced coloring scenarios, you can use the `HistogramChart.ColorRule`
slot to apply conditional coloring based on your data values. This is
particularly useful for highlighting specific data points or applying business
logic to your visualizations.

Color rules can be applied based on different criteria:

- Name-based rules: Color series based on their name patterns

- Property-based rules: Color based on specific properties in your series
data

- Value-based rules: Color based on data values

In the example above, we're using several rules:

- Color any series starting with "High" in red

- Color any series starting with "Medium" in yellow

- Color any series starting with "Low" in green

- Color any series with `horizontal.start` set to `true` in purple

For more details about available comparators and options, see the
Color Rules
section.

#### Value representation

By default, values within a chart are displayed as is - with their absolute
value (e.g. 3.14 kB). However, this can be changed so that instead of absolute
values, relative values are used. Relative values indicate the proportion that a
given dimension contributes to the sum (100%) of a given histogram bin. The
`valueRepresentation` prop can be used to change this behavior. For series with
only a single dimension, the relative value is based on the maximum value within
the given series.

#### Legend

The purpose of the legend is to provide additional identifying information for
the chart, without needing to interact with the legend directly.

##### Visibility

The legend of the `HistogramChart` is shown by default. In order to hide or show
the legend, you need to set the value of `legend.hidden` on the subcomponent.

##### Position

By default, the position of the legend of the `HistogramChart` is set
automatically. This option prioritizes the legend placement to the right of the
chart area. When the chart width is reduced, the legend is repositioned to the
area beneath the chart. It is also possible to explicitly set the chart's legend
position to right or bottom with the `position` prop.

##### Legend ratio

By default, the legend occupies `25%` of the container width, in the case where
the legend is positioned on the right and `25%` of the container height if the
legend position is on the bottom.

It is possible to override the default legend ratio by setting a custom
percentage value for the ratio prop. The expected value is in the range of
`5-80`. Values out of expected ranges will roll back to the default legend
ratio.

#### Chart Interactions

The `HistogramChart` provides various interactions (e.g. zoom-x, zoom in, zoom
out, and pan) that can be optionally enabled. See
chart interactions for more details.

#### Axes

To configure the axes of the `HistogramChart`, the `HistogramChart.XAxis` and
`HistogramChart.YAxis` subcomponents can be added. The `label` property sets the
axis label. Axis scale boundaries can be set with the `min` and `max` props.
Both `XAxis` and `YAxis` supports `linear` and `log` scales.

Both `HistogramChart.XAxis` and `HistogramChart.YAxis` subcomponents also
support `data-max` in the `max` property and `data-min` in the `min` property.
These special values allow for granular control over the Y-axis scale
boundaries. By default, the `auto` value is used for both `min` and `max`
properties. The `auto` mode automatically determines both the minimum and
maximum values of the Y-axis scale based on the data in the chart (similar to
`data-min` and `data-max`) and sets the Y-axis baseline to zero.

##### Multiple Y-axes

The `HistogramChart` supports multiple Y-axes. `HistogramChart.YAxis` provides a
`position` property which can be set to either `left` or `right`.

When you specify multiple Y-axes, the chart automatically assigns data series to
Y-axes based on the unique units of the data. The first unique unit is assigned
to the left Y-axis, and the second unique unit to the right Y-axis. Note that
any additional data series with different units from those already used will not
be displayed.

Currently, it's not possible to assign data series to specific Y-axes, nor is it
possible to use the same unit for both Y-axes.

#### Tooltip

Tooltips are used to display additional detailed information about a selected
data point and can be enabled by adding the `HistogramChart.Tooltip`
subcomponent. The tooltip `variant` defines whether the tooltip should contain
data points from all bins (shared) for the selected bin, or just the closest one
(single). The `seriesDisplayMode` prop can be used to define whether the tooltip
should be comprised of a single line of information or multiple lines.

The sequence of the input data in the chart determines the arrangement of the
tooltip series.

##### Single

##### Shared

#### Formatter

The unit for the `HistogramChart`, by default, will be appended to the specified
value. There are two other options in the formatter that allow for greater
customization. The first option enables you to prepend the unit to the value,
while the second option enables you to ignore the original unit and append a
custom string instead. Additionally, there is a custom formatter option
available to allow you to change the input unit to one of your choice, e.g.: if
the input unit is `bits`, you are able to switch and display the unit as
`bytes`, correctly formatted. The formatted value is applied in the axis ticks,
as well as in the tooltip and the axis magnifier. The use cases below outline
each of these scenarios.

The precision of the formatter will adapt automatically based on the data
decimals if there is no precision configuration from the custom formatter
option.

#### Annotations

Annotations are used to visualize specific events or contextual notes on the
`HistogramChart` in the form of markers placed in the bins position.

The marker represents an annotation at a certain bin. They can be either a value
(a certain number) or a range (from-to object), depending on the data provided
to the Annotation. Annotations within the same bin are grouped together under a
single marker that displays the number of grouped annotations. Markers can be
displayed on a single or multiple tracks. When there are more than three tracks,
an overflow scroll is applied.

##### Add annotations to the chart

In order to visualize annotation data inside the `HistogramChart`, a
`HistogramChart.Annotations` component should be initialized. This component
should have at least one track, that contains a marker component per annotation
data point.

An annotation data point should contain the from-to bin information
(`value: {from: number, to:number}`) or a certain point (`value: number`), an
optional `symbol`, `title`, and `description`, which will be displayed in the
tooltip.

##### Marker content

When the `symbol` is provided, it will become the marker content by default.
When not, the `title` will be shown as marker content.

In case the content of the marker is bigger than the size of the marker (bin
size in Histogram), it will expand to fit all the content inside, decoupling
from the original scale. In these particular cases, it is encouraged to use the
indicators, which will represent the real size of the bin.

##### Visual customization

Tracks and markers support visual customization in order to differentiate
various types of annotations.

It's possible to set custom colors on both the track (to be applied to all
markers) and the marker level by using the `color` property on the respective
component. A marker's custom color has precedence over track's. This color can
be set to any `Design System color token`, as well as any `rgb`, `hex` or
`CSS color`.

The `symbol` property allows you to apply an icon, emoji, single letter, glyph,
or Design System icon to either an individual marker or to an entire track. When
applied to a track, this `symbol` will be used as the default.

When markers partially overlap one another, the order of the annotations defines
which marker is displayed on top. Value annotations are always displayed above
Range-based ones. It's also possible to customize the marker display order, by
using the priority property. The higher the value of the priority property, the
higher precedence the marker has. The priority property also affects the color
of markers i.e. within a group, the color of the marker with the highest
priority will be applied to the group.

It's possible to assign a label to a track using the `label` property. Be aware
that labels are hidden by default. To show a track's label, the `showLabels`
property has to be applied to the `HistogramChart.Annotations` component.

##### Visibility

An entire track can be hidden by adding the `hidden` property to the
`HistogramAnnotations.Track` component. The same configuration can be applied to
a marker, by setting the `hidden` property on the `HistogramAnnotations.Marker`
component.

When hovering a marker (with the cursor), an annotation indicator appears over
the chart area. The indicator's visibility can be customized on either a track
or marker level by using the `indicatorsDisplay` property:

- With the `auto` option, the default behaviour is applied - indicators appear
on hover.

- The `always` option sets indicators to always be visible within the chart
area, regardless of the hovering behavior.

- The `never` option sets indicators to never be visible.

##### Custom tooltip

The Annotations supports both default and custom tooltips for annotations. This
allows creators to provide additional detailed information about specific
datapoints or events in the chart.

See Annotations Tooltip
for more

#### Thresholds

Thresholds are used to mark meaningful ranges or values on a `HistogramChart`
and they add contextual information to a numerical axis. There are two variants
of thresholds:

- a specific point represented on the Y-axis and a line across.

- a range - or filled area - represented by a pill on the Y-axis and a band
across.

##### Point and Range

Both point and range can be represented by static or dynamic data sources. A
static data source has a single value representing a point or a single key-value
pair representing a fixed range. A dynamic data source has a data array
containing more than one value or various key-value pairs.

There are three different types of threshold markers:

Range filled, where the value range is defined in order to display the
threshold band. The upper and lower lines are not drawn unless the pill is
hovered.

Range stroke-only variant, where a value range is defined in order to display
the threshold band represented by upper and lower dashed lines. The upper and
lower lines become continuous lines when the pill is hovered.

Point, where only one value is required to display the threshold. It's
represented by a dashed line and when the point is hovered the line becomes a
continuous line.

##### Dynamic Point

##### Dynamic Range

##### Dynamic Range Stroke Only

There is no limit defined for the number of threshold ranges or points that can
be used in a single `HistogramChart`.

By default, thresholds are positioned on the left axis and with the use of the
`position` prop, we can place thresholds on the right axis or on both, as
depicted below.

##### Left Axis

##### Right Axis

##### Dual Axis

#### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application. The fallback UI occupies the full
width and height of the chart, ensuring that users are still provided with a
meaningful interface even in the presence of errors.

The `ErrorState` subcomponent offers a versatile feature that enables it to
handle both default and custom error messages. You can provide a custom message
through the `ErrorState` subcomponent, which will then override the default
error message. This flexibility allows developers to tailor error messages to
their specific needs and requirements, ensuring a more personalized and
informative user experience.

The `ErrorState` subcomponent provides the flexibility to format custom error
messages using HTML, which allows for enhanced customization and adaptability in
presenting error information. Furthermore, it is possible to incorporate the
original thrown error within your custom error message, ensuring that users
receive comprehensive and relevant information when an error occurs.

#### EmptyState

The `EmptyState` subcomponent serves as a fallback when there is no data
available to display in a chart. Its purpose is to provide a user-friendly way
of informing the user about the current situation. When there is no data, a
fallback UI is displayed occupying the full width and height of the chart, along
with a default message.

A feature of `EmptyState` is its ability to handle custom messages. It provides
the flexibility to format custom messages using HTML, which allows for enhanced
customization and adaptability in presenting error information.

#### Loading

The `loading` prop is a boolean value that can be passed to the `HistogramChart`
component to control its loading state. When the loading prop is set to true,
the loading indicator appears in the middle of the chart plot to inform the user
that the component is currently fetching or processing data. When the loading
prop is set to false, the component should display its regular content.

#### Toolbar behavioral tracking

The `HistogramChart.Toolbar` subcomponent supports behavioral tracking
attributes that are spread onto the toolbar root element. This allows tracking
of toolbar interactions such as menu opens, mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `HistogramChart.Toolbar` to attach
tracking metadata. See `BehaviorTrackingProps` for the full list of supported
attributes.

#### Download data as CSV

The `HistogramChart` component supports download data in CSV format using a
toolbar button. To enable this feature, a `HistogramChart.Toolbar` subcomponent
must be provided to the `HistogramChart` component. On click of the download
button, raw data will be downloaded as a CSV file.

The CSV file contains the following columns:

- `name` - the name of the series

- `unit` - the unit of the series

- `from` - the start of the bin range

- `to` - the end of the bin range

- `value` - the value of the bin

It's also possible to programmatically trigger the download of the CSV file by
calling the `downloadData` method on the `HistogramChart` instance reference.

#### Intent options

The `HistogramChart` supports intent options in the toolbar. The intents appear
in the toolbar's dropdown menu, allowing users to perform actions such as
sharing a chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `HistogramChart`, use the `HistogramChart.Intent`
subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in HistogramChart:

#### Styling

The `HistogramChart` also accepts custom styling, which can be set using the
props `className` and/or `style` as in a regular html element.Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Size
- Series actions
- Change the chart color/s
- Value representation
- Legend
- Chart Interactions
- Axes
- Tooltip
- Formatter
- Annotations
- Thresholds
- Error state
- EmptyState
- Loading
- Toolbar behavioral tracking
- Download data as CSV
- Intent options
- Styling

### Props

A `HistogramChart` is a type of graph that represents the distribution of
numerical data. It’s constructed by dividing the entire range of values into a
series of intervals—known as bins and then counting how many values fall into
each interval. The bins are typically of equal size and are adjacent to each
other, with no gaps. Each bin is represented by a bar, where the height of the
bar reflects the frequency or count of data points within that interval

OverviewProperties

#### HistogramChartProps
extends`, , , <>` |
 | Name | Type | Default | Description
 | `data` | [] | | Data object for the histogram chart
 | `height?` | | | `300px` | Chart height. When a number is specified, it's treated as pixels,
otherwise a valid height string is expected.
 | `width?` | | | `100%` | Chart width. When a number is specified, it's treated as pixels,
otherwise a valid width string is expected.
 | `seriesActions?` | (series: , bin: ) => | | Actions to be shown in the legend and tooltip actions
 | `truncationMode?` | | `'middle'` | Truncation mode to use (start, middle, end)
Applied to all the parts that truncate text.
 | `colorPalette?` | | | `"categorical"` | Color palette to be used for the bar category.
 | `loading?` | | `false` | Show the loading indicator when truthy.
 | `valueRepresentation?` | | `"absolute"` | The way values are represented. "absolute" will display the value as it is, and "relative" displays a percentage value considering the other dimensions values within a categories.
 | `infiniteZoom?` | | `false` | Enables infinite zooming

### HistogramChart.Legend

To configure the legend, add `HistogramChart.Legend` to the histogram chart.

#### HistogramChartLegendProps

##### Signature:
`export declare type HistogramChart = ;`

### HistogramChart.Tooltip

To configure the tooltip, add `HistogramChart.Tooltip` to the histogram chart.

#### HistogramChartTooltipProps
 |
 | Name | Type | Default | Description
 | `variant?` | | | Whether the tooltip should contain bins from
all series or just the closest one.

### HistogramChart.XAxis

To configure the x-axis, add `HistogramChart.XAxis` to the histogram chart.

#### HistogramChartXAxisProps
 |
 | Name | Type | Default | Description
 | `max?` | | | | `'auto'` | The max value configuration to display in the axis
 | `min?` | | | | `'auto'` | The min value configuration to display in the axis
 | `label?` | | | The title used for the axis
 | `scale?` | | | The scale to be used
 | `formatter?` | | | | Formatter to be applied for each tick of the axis
 | `unit?` | | | The unit for the axis

### HistogramChart.YAxis

To configure the y-axis, add `HistogramChart.YAxis` to the histogram chart.

#### HistogramChartYAxisProps
 |
 | Name | Type | Default | Description
 | `max?` | | | | `'auto'` | The max value configuration to display in the axis
 | `min?` | | | | `'auto'` | The min value configuration to display in the axis
 | `label?` | | | The title used for the axis
 | `scale?` | | | The scale to be used
 | `formatter?` | | | | Formatter to be applied for each tick of the axis
 | `position?` | | | `'left'` | The position of the y axis relative to
the histogram chart

### HistogramChart.ThresholdIndicator

`HistogramChart.ThresholdIndicator` provides a slot for defining thresholds in
the chart.

#### HistogramThresholdIndicatorProps

##### Signature:
`export declare type HistogramThresholdIndicatorProps = ;`

### HistogramChart.EmptyState

`HistogramChart.EmptyState` provides a slot where the Empty state wrapper can be
set.

#### EmptyStateProp
 |
 | Name | Type | Default | Description
 | `children` | | |

### HistogramChart.ErrorState

`HistogramChart.ErrorState` provides a slot where the Error state wrapper can be
set.

#### ErrorStateProps
 |
 | Name | Type | Default | Description
 | `children` | | ((errorMessage: ) => .) | |

### HistogramChart.Select

`HistogramChart.Select` provides a slot that enables functionality for selecting
a specific area in the chart.

#### SelectProps
 |
 | Name | Type | Default | Description
 | `actions?` | (selectedSeries: [], selectionDomain: [, ]) => | <> | | Custom actions handler

### HistogramChart.Intent

`HistogramChart.Intent` provides a slot to set intents that will appear in the
toolbar.

#### IntentProps

##### Signature:
`export declare type IntentProps = | ;`

### HistogramChart.ColorRule

`HistogramChart.ColorRule` provides a slot to apply conditional coloring to your
chart series based on their values or names.

#### ColorRuleProps

##### Signature:
`export declare type ColorRuleProps = {
 valueAccessor?: ;
 comparator: ;
 matchValue: ;
} & ;`

### HistogramChart.Annotations

`HistogramChart.Annotations` provides a slot for configuring annotations in the
histogram.

#### HistogramAnnotationsProps
extends |
 | Name | Type | Default | Description
 | `visibleTracksLimit?` | | `3` | How many tracks to show by default, if there are more tracks than the specified here a scrollbar will be added.

### HistogramAnnotations.Track

`HistogramAnnotations.Track` provides a slot for configuring the track in the
`HistogramChart.Annotations`.

#### HistogramAnnotationsTrackProps
extends |
 | Name | Type | Default | Description
 | `indicatorsDisplay?` | | `'auto'` | Defines how to show the annotations indicators: always, never, or on hover (auto) at Track level

### HistogramAnnotations.Marker

`HistogramAnnotations.Marker` provides a slot for configuring the marker in the
`HistogramChart.Annotations`.

#### HistogramAnnotationsMarkerProps
extends`, ` |
 | Name | Type | Default | Description
 | `indicatorsDisplay?` | | `'auto'` | Defines how to show the marker indicator on top of the chart: always, never, or on hover (auto)

### HistogramAnnotations.Tooltip

`HistogramAnnotations.Tooltip` provides a slot for defining a custom tooltip for
the annotations.

#### AnnotationsTooltipProps
 |
 | Name | Type | Default | Description
 | `hidden?` | | `false` | Defines whether tooltip show be hidden or not
 | `children?` | | | The ChoroplethLayer tooltip handler template

### HistogramChart.Toolbar

`HistogramChart.Toolbar` provides a slot to customize the toolbar of the chart.

#### HistogramToolbarSlotProps

##### Signature:
`export declare type HistogramToolbarSlotProps = ;`

### HistogramChart.DownloadCSV

`HistogramChart.DownloadCSV` provides a slot to toggle the download CSV of the
chart.

### HistogramChart.Zoom

`HistogramChart.Zoom` provides a slot to toggle the zoom of the chart.

#### ZoomSlotProps
 |
 | Name | Type | Default | Description
 | `disabled?` | | | Whether the zoom is disabled.

### HistogramChart.Pan

`HistogramChart.Pan` provides a slot to toggle the pan of the chart.

#### PanSlotProps
 |
 | Name | Type | Default | Description
 | `disabled?` | | | Whether the pan is disabled.Still have questions?Find answers in the Dynatrace Community
- HistogramChart.Legend
- HistogramChart.Tooltip
- HistogramChart.XAxis
- HistogramChart.YAxis
- HistogramChart.ThresholdIndicator
- HistogramChart.EmptyState
- HistogramChart.ErrorState
- HistogramChart.Select
- HistogramChart.Intent
- HistogramChart.ColorRule
- HistogramChart.Annotations
- HistogramAnnotations.Track
- HistogramAnnotations.Marker
- HistogramAnnotations.Tooltip
- HistogramChart.Toolbar
- HistogramChart.DownloadCSV
- HistogramChart.Zoom
- HistogramChart.Pan

---

## HoneycombChart

`/design/data-visualizations/charts/HoneycombChart/`

The `HoneycombChart` is used to display data in a grid using various shapes for
data points.

A honeycomb chart organizes and presents data in a visually structured way,
making it easier for viewers to analyze and interpret information.

OverviewProperties

### Import

`tsx
import { HoneycombChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `HoneycombChart` can compare the values of its nodes based on a `string`
(category) or a `number`. For a category-based hive, provide `data` as a string,
an array of strings, or objects that contain a `value` prop as a string.

`tsx
[ { value: 'Severe', name: 'dts-eu-zone1-server-1' }, { value: 'Emergency', name: 'dts-eu-zone1-server-2' }, { value: 'Notice', name: 'dts-eu-zone1-server-3' },];
`

For numeric hives, the `data` prop expects either a number, an array of numbers,
or objects with a numeric `value` prop.

`tsx
[ { value: 10757, name: 'Severe' }, { value: 4106, name: 'Emergency' }, { value: 1652, name: 'Notice' },];
`

Learn more about the data format here.

Additionally, for numeric hives, you can set the boundaries of the data shown
with the `min` and `max` props. These props support `data-max` in the `max`
property and `data-min` in the `min` property. These special values allow for
granular control over the boundaries. By default, the `min` prop uses the
`data-min` value, and the `max` prop uses the `data-max` value. These modes
automatically determine the hive's minimum and maximum values based on the
chart's data.

##### Labels

The nodes within a hive could show corresponding `name` and `value` just setting
the `showLabels` prop in the `HoneycombChart`. It always will try to fit both
the name and the value, but if the height of both is higher than the area
assigned for text, will try to fit one. If the height of the text area isn't
enough to fit neither the value, neither the name, then the node will appear
without labels. In case the name is wider than the text area, an ellipsis will
be applied to it.

##### Shapes

The nodes in the honeycomb can be set in 3 different shapes: `'circle'`,
`'square'` and `'hexagon'`. (`'hexagon'` being the default one).

##### Chart Size

By default, the chart will use all the available container size up to a maximum
height of 300 pixels. The `width` and `height` props can be used to control the
chart's dimensions. Both accept numeric values (treated as pixels) or CSS unit
strings like `"100%"`, `"500px"`, or `"50vw"` for flexible sizing.

The way how the text should be truncated if it exceeds the available space can
be specified with `truncationMode` prop. Available values are `start`, `end` and
`middle`, being `middle` the default one.

##### Loading

The `loading` prop is a boolean value that can be passed to the `HoneycombChart`
component to control its loading state. When the loading prop is set to true,
the loading indicator appears in the middle of the chart plot to inform the user
that the component is currently fetching or processing data. When the loading
prop is set to false, the component should display its regular content.

#### Legend

The purpose of the legend is to provide additional identifying information for
the chart, without the need to interact with it.

##### Position

By default, the position of the legend of the `HoneycombChart` is set
automatically. This option prioritizes the legend placement to the right of the
chart area. When the chart width is reduced, the legend is repositioned to the
area beneath the chart. It is also possible to explicitly set the chart's legend
position to `right` or `bottom` using legend's `position` prop.

#### Toolbar

The toolbar allows you to download data and use added Intents. Displayed by
default, it can be customized by adding the `HoneycombChart.Toolbar`
subcomponent, which supports the `hidden` and `placement` props.

##### Behavioral tracking

The `HoneycombChart.Toolbar` subcomponent supports behavioral tracking
attributes that are spread onto the toolbar root element. This allows tracking
of toolbar interactions such as menu opens, mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `HoneycombChart.Toolbar` to attach
tracking metadata. See `BehaviorTrackingProps` for the full list of supported
attributes.

##### Download data as CSV

The `HoneycombChart` component allows data to be downloaded in CSV format via a
toolbar button. To enable this feature, add the `HoneycombChart.DownloadCSV`
subcomponent to the `HoneycombChart`. Clicking the button will download the raw
data as a CSV file.

#### Intent options

The `HoneycombChart` supports intent options in the toolbar. The intents appear
in the toolbar's dropdown menu, allowing users to perform actions such as
sharing a chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `HoneycombChart`, use the `HoneycombChart.Intent`
subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in HoneycombChart:

#### Change the chart color/s

The `HoneycombChart` provides several ways to customize the appearance of your
data:

- Predefined Color Palettes: Choose from a set of built-in color palettes.

- Custom Ranges: Define your own color ranges for numerical data.

- Color Rules: Apply conditional coloring based on data values.

##### Using Color Palettes

The `HoneycombChart` provides a set of predefined color palettes that can be
used out of the box to provide more appealing visualizations. See
Charts Colors for more info.

##### Using predefined color palette

The `HoneycombChart` is able to assign colors to the nodes based on the value
distribution of each node compared to the total. Domain will be divided in an
amount of 'groups' equal to the quantity of colors in the palette. Each node
will receive the color of the group that fits its value.

##### Coloring a numerical dataset using custom ranges

To define custom ranges and colors, pass an array of `ColoredRange` objects to
the `colorScheme` prop. This allows you to specify exact value ranges and their
corresponding colors.

##### Coloring a categorical dataset with predefined color scheme

If a categorical dataset is used, then the value of each node should be a
string. A predefined color palette can be used to map the categories in the
value of the node to the specific predefined color.

##### Coloring a categorical dataset using custom categories and color scheme

If none of the predefined color palettes fit your case, the `HoneycombChart` is
able to process a `key-value` object as `colorScheme` taking each `key` as the
category label and the `value` as its assigned color.

##### Using Color Rules

For advanced coloring scenarios, use the `HoneycombChart.ColorRule` slot to
apply conditional coloring based on your data values. This is particularly
useful for highlighting specific nodes or applying business logic to your
visualizations.

Color rules can be applied to both numerical and categorical data:

For Numerical Data:

- Color nodes based on their value thresholds

- Highlight specific value ranges

- Apply colors based on nested properties

For Categorical Data:

- Color nodes based on exact matches

- Use pattern matching for text values

- Apply different colors to different categories

Example Rules:

`tsx
// Numerical rule: Color nodes with value >= 5000 in redHoneycombChart.ColorRule comparator="greater-or-equal" matchValue={5000} colorPalette="red-inverted"/>// Text rule: Color nodes containing 'Emergency' in their nameHoneycombChart.ColorRule comparator="contains" matchValue="Emergency" valueAccessor="name" colorPalette="red"/>// Categorical rule: Color nodes with category 'Europe' in purpleHoneycombChart.ColorRule comparator="equals" matchValue="Europe" colorPalette="purple-rain"/>
`

For more details about available comparators and options, see the
Color Rules
section.

##### Filtering values in numeric dataset

The `HoneycombChart` can focus the applied color palette to a specified range
using the `min` and `max` props. All nodes will be preserved, but those outside
the boundaries will use a default color.

#### States

If the app experiences any issue like an error or an empty dataset, two
mechanisms exist to deal with those situations in a graceful way.

##### Error state

###### Default

In case of an error thrown inside the chart, a predefined error message will be
shown.

###### Custom

If you prefer to create your own error screen to preserve styles and information
shown, you can create your own error state presenter.

##### Empty State

###### Default

When no data is provided to the chart, a predefined empty state message will be
displayed.

###### Custom

An error message can be customized using `HoneycombChart.ErrorState`
subcomponent.

#### User actions

A user action is a creator-defined interaction with a given node in the hive.
Basic interactions include copying the node name and inspecting the underlying
data of it. In order to enable user actions, the `ChartSeriesAction`
subcomponent needs to be appended within the `HoneycombChart`. More
subcomponents can be added within this component, for instance the
`ChartSeriesAction.Item`, where custom logic can be applied. `Intents` could be
added as part of the series action as well with `ChartSeriesAction.Intent`.

#### Formatter and Unit

The `HoneycombChart` provides a way to format the values of the chart nodes. The
`formatter` prop at the root component can be used to format the values shown in
the tooltip on node hover and the legend ticks. The `unit` prop can be used to
add a unit to the values of the nodes. When both props are specified the
`formatter` will be applied with the provided unit (formatting options objects
are an exception). When no formatter is provided a default formatter with value
abbreviation will be used.

Note that the `formatter` and the `unit` props will be applied only to numeric
data.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Legend
- Toolbar
- Intent options
- Change the chart color/s
- States
- User actions
- Formatter and Unit

### Props

The `HoneycombChart` is used to display data in a grid using various shapes for
data points.

A honeycomb chart organizes and presents data in a visually structured way,
making it easier for viewers to analyze and interpret information.

OverviewProperties

#### HoneycombChartProps

##### Signature:
`export declare type HoneycombChartProps = | ;`

### HoneycombChart.Legend

To configure the legend, add `HoneycombChart.Legend` to the honeycomb chart.

#### HoneycombLegendProps

##### Signature:
`export declare type Honeycomb = ;`

### HoneycombChart.EmptyState

`HoneycombChart.EmptyState` provides a slot where the Empty state wrapper can be
set.

#### EmptyStateProp
 |
 | Name | Type | Default | Description
 | `children` | | |

### HoneycombChart.ErrorState

`HoneycombChart.ErrorState` provides a slot where the Error state wrapper can be
set.

#### ErrorStateProps
 |
 | Name | Type | Default | Description
 | `children` | | ((errorMessage: ) => .) | |

### HoneycombChart.Toolbar

`HoneycombChart.Toolbar` is a slot to hide or to configure the toolbar.

#### BaseToolbarProps
extends`, ` |
 | Name | Type | Default | Description
 | `hidden?` | | `false` | Decides if the toolbar is visible or hiddenStill have questions?Find answers in the Dynatrace Community
- HoneycombChart.Legend
- HoneycombChart.EmptyState
- HoneycombChart.ErrorState
- HoneycombChart.Toolbar

---

## MeterBarChart

`/design/data-visualizations/charts/MeterBarChart/`

The `MeterBarChart` provides a lightweight and simple visualization progress
toward a completion, consumption of a total, etc. It consists of a horizontal
bar that gradually fills up with color or shading as it approaches the max
value.

OverviewProperties

### Import

`tsx
import { MeterBarChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `MeterBarChart` expects a single value as an input. This value needs to be
passed to the visualisation's `value` prop as a `Number`.

You can also provide custom `min` and `max` props to set the scale of the
`MeterBarChart`, and if none are provided the default `min` will be 0 and `max`
will be 100.

It is also possible to delegate the component to generate the labels by setting
, and
slots, to respectively generate automatically min, max, and value labels (the
formatting will be applied automatically).

Learn more about the data format here.

#### Object values

The `MeterBarChart` accepts object values in addition to numeric values. When
passing an object value, a `valueAccessor` prop needs to be specified to
indicate which field should be used as the chart's display value.

In the example above, the chart displays the value from the `value` field, while
the ColorRule evaluates against the `count` field using its own `valueAccessor`
prop. This enables conditional coloring based on different properties within the
data object.

#### Change the chart color/s

The `MeterBarChart` provides several ways to customize the appearance of your
data:

- Direct Color Assignment: Set a single color for the entire bar.

- Color Rules: Apply conditional coloring based on the bar's value.

##### Direct Color Assignment

The `MeterBarChart` has a default color for the bar segment, but it accepts a
`color` prop that can be set to any valid color string that utilizes a format
supported by web browsers, including RGB, HSL and HEX.

##### Using Color Rules

For more advanced coloring scenarios, you can use the `MeterBarChart.ColorRule`
slot to apply conditional coloring based on the bar's value. This is
particularly useful for creating visual indicators for different value ranges.

Color rules can be applied based on the bar's value using different comparators:

- `'greater-than'`

- `'less-than'`

- `'greater-or-equal'`

- `'less-or-equal'`

- `'equals'`

In the example above, we're using rules to change the bar color based on value
thresholds:

- Values ≥ 80 are shown in red

- Values ≥ 60 (but

- Values below 60 use the default color

You can combine multiple rules to create complex coloring schemes. When multiple
rules match, the most specific rule (highest `matchValue` for 'greater'
comparators, lowest for 'less' comparators) will take precedence.

For more details about available comparators and options, see the
Color Rules
section.

#### Customize chart information

There is a set of subcomponents that can be used on the `MeterBarChart` to
display more information about the chart: ,
, and .

In order to add additional context to a `MeterBarChart`, it's possible to use
the `prefixIcon` prop to set a prefixed symbol as a ReactNode, consisting of an
icon, emoji, single character, glyph, or Design System icon.

It will be displayed to the left of the label.

#### Sizing

Different sizes can be set on the `MeterBarChart` to display the information,
using the prop `size`. This prop allows us to use three values: `size8` (small),
`size16` (medium), `size24` (large) and `auto` (dynamic - based on the parent's
height). It will only affect the height of the visualization. If you don't
provide any size the default will be `size16`.

#### Thresholds

Thresholds are used to mark meaningful values on a `MeterBarChart`. In order to
set one or multiple thresholds, you can use
slot. You can also optionally display the threshold indicator via the
`showIndicator` prop. By default the thresholds legend won't be shown, to enable
it you can use slot.

#### Add tooltip

The `MeterBarChart` has an optional Tooltip to display additional information
and will be shown when the user hovers over the segment. Use the subcomponent
 to enable it. You can customize the label displayed in
the tooltip by passing a `name` prop. If no `name` is provided, it defaults to
`"Value"`.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the
`MeterBarChart`. More subcomponents can be added within this component, for
instance `ChartSeriesAction.Item`, where you can provide a custom action that
will appear in the legend menu. That action can execute any custom logic in its
`onSelect` callback or get disabled via a `disabled` prop. `Intents` could be
added as part of the series action as well with `ChartSeriesAction.Intent`.

#### Toolbar behavioral tracking

The `MeterBarChart.Toolbar` subcomponent supports behavioral tracking attributes
that are spread onto the toolbar root element. This allows tracking of toolbar
interactions such as menu opens, mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `MeterBarChart.Toolbar` to attach
tracking metadata. See `BehaviorTrackingProps` for the full list of supported
attributes.

#### Intent options

The `MeterBarChart` supports intent options in the toolbar. The intents appear
in the toolbar's dropdown menu, allowing users to perform actions such as
sharing a chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `MeterBarChart`, use the `MeterBarChart.Intent`
subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in MeterBarChart:

#### Formatter

The `MeterBarChart` has a formatter prop that accepts any function to provide
format to the relevant chart values. One of the uses of this formatter can be to
attach a custom unit or string to the value. The default formatter shows the
value without any format.

Additionally, there is a custom formatter option available to allow you to
change the input unit to one of your choice, e.g.: if the input unit is `bits`,
you are able to switch and display the unit as `bytes`, correctly formatted. The
formatted value will appear in the chart tooltip. The use cases below outline
each of these scenarios.

#### Styling

The `MeterBarChart` also accepts custom styling, which could be set using the
props `className` and/or `style`, as a regular html element

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Object values
- Change the chart color/s
- Customize chart information
- Sizing
- Thresholds
- Add tooltip
- Series actions
- Toolbar behavioral tracking
- Intent options
- Formatter
- Styling

### Props

The `MeterBarChart` provides a lightweight and simple visualization progress
toward a completion, consumption of a total, etc. It consists of a horizontal
bar that gradually fills up with color or shading as it approaches the max
value.

OverviewProperties

#### MeterBarChartProps

##### Signature:
`export declare type MeterBarChartProps = | ;`Prop Table did not receive dataStill have questions?Find answers in the Dynatrace Community

---

## MultiMeterBarChart

`/design/data-visualizations/charts/MultiMeterBarChart/`

The `MultiMeterBarChart` is a more complex version of the single meter bar, it
allows for different data inputs to be considered when presenting progress
toward a goal, consumption of a total, etc.

OverviewProperties

### Import

`tsx
import { MultiMeterBarChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `MultiMeterBarChart` expects one or various `MultiMeterBarChart.Segment`
subcomponents to be rendered along with it. These subcomponents expect a `value`
prop as a `Number`.

You can also provide custom `min` and `max` props to set the scale of the
`MultiMeterBarChart`, and if none are provided the default `min` will be 0 and
`max` will be the total value of all segments.

It is also possible to delegate the component to generate the labels by setting
, and
 slots, to respectively generate automatically
min, max, and value labels (the formatting will be applied automatically).

Learn more about the data format here.

#### Object values

Each `MultiMeterBarChart.Segment` accepts object values in addition to numeric
values. When passing an object value to a segment, a `valueAccessor` prop needs
to be specified on that segment to indicate which field should be used as the
segment's display value.

In the example above, each segment displays its value from the `value` field.
ColorRules can use their own `valueAccessor` prop to evaluate conditions against
different properties in the data object, such as `count` or `priority`.
ColorRules can also access segment properties like `name` by setting
`valueAccessor="name"`.

#### Change the chart color/s

The `MultiMeterBarChart` provides several ways to customize the appearance of
your data:

- Predefined Color Palettes: Choose from a set of built-in color palettes.

- Custom Colors: Define your own color schemes for individual segments.

- Color Rules: Apply conditional coloring based on data values or segment
names.

##### Using Color Palettes

The `MultiMeterBarChart` has a default color palette for the segments. This
could be changed with the `colorPalette` prop that can be set to any of
predefined color palettes and it also accepts custom color palettes. See
coloring for more details.

#### Override segment color

The `MultiMeterBarChart.Segment` has `color` prop that can be set to override
the color that comes from the color palette. See
coloring for more details.

#### Using Color Rules

For more advanced coloring scenarios, you can use the
`MultiMeterBarChart.ColorRule` slot to apply conditional coloring based on your
data values. This is particularly useful for highlighting specific segments or
applying business logic to your visualizations.

Color rules can be applied based on different criteria:

- Value-based rules: Apply colors based on segment values using comparators
like 'greater-than', 'less-than', etc.

- Name-based rules: Match segment names using 'starts-with', 'ends-with', or
'matches-phrase' comparators

- Multiple rules: Combine multiple rules for complex coloring logic

In the example above, we're using several rules:

- Color any segment with a value ≥ 0 using the 'swamps' color palette

- Color any segment with a value ≥ 30 in red

- Color any segment whose name starts with "Poor" in rebeccapurple

For more details about available comparators and options, see the
Color Rules
section.

#### Customize chart information

There is a set of subcomponents that can be used on the `MultiMeterBarChart` to
display more information about the chart: ,
, and
.

In order to add additional context to a `MultiMeterBarChart`, it's possible to
use the `prefixIcon` prop to set a prefixed symbol as a ReactNode, consisting of
an icon, emoji, single character, glyph, or Design System icon.

It will be displayed to the left of the label.

#### Sizing

Different sizes can be set on the `MultiMeterBarChart` to display the
information, using the prop `size`. This prop allows us to use four values:
`size8` (small), `size16` (medium), `size24` (large) and `auto` (dynamic - based
on the parent's height). It will only affect the height of the visualization. If
you dont provide any size the default will be `size16`.

#### Add Legend

Legend can be added to `MultiMeterBarChart` in order to add more information
about the data represented by the chart. Legend is optional and can be included
using the subcomponent .

#### Add tooltip

The `MultiMeterBarChart` has an optional tooltip that displays additional
information when the user hovers over a segment. Use the subcomponent
 to enable it. The tooltip `variant` defines
whether the tooltip should contain data for all items present in the chart
(shared) or only the currently selected one (single). By default, the variant is
single.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the
`MultiMeterBarChart`. More subcomponents can be added within this component, for
instance `ChartSeriesAction.Item`, where you can provide a custom action that
will appear in the legend menu. That action can execute any custom logic in its
`onSelect` callback or get disabled via a `disabled` prop. `Intents` could be
added as part of the series action as well with `ChartSeriesAction.Intent`.

#### Toolbar behavioral tracking

The `MultiMeterBarChart.Toolbar` subcomponent supports behavioral tracking
attributes that are spread onto the toolbar root element. This allows tracking
of toolbar interactions such as menu opens, mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `MultiMeterBarChart.Toolbar` to
attach tracking metadata. See `BehaviorTrackingProps` for the full list of
supported attributes.

#### Intent options

The `MultiMeterBarChart` supports intent options in the toolbar. The intents
appear in the toolbar's dropdown menu, allowing users to perform actions such as
sharing a chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `MultiMeterBarChart`, use the
`MultiMeterBarChart.Intent` subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in
MultiMeterBarChart:

#### Formatter

The `MultiMeterBarChart` has a formatter prop that accepts any function to
provide format to the relevant chart values. One of the uses of this formatter
can be to attach a custom unit or string to the value. The default formatter
shows the value without any format.

Additionally, there is a custom formatter option available to allow you to
change the input unit to one of your choice, e.g.: if the input unit is `bits`,
you are able to switch and display the unit as `bytes`, correctly formatted. The
formatted value will appear in the chart tooltip. The use cases below outline
each of these scenarios.

#### Styling

The `MultiMeterBarChart` also accepts custom styling, which could be set using
the props `className` and/or `style`, as a regular html element

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Object values
- Change the chart color/s
- Override segment color
- Using Color Rules
- Customize chart information
- Sizing
- Add Legend
- Add tooltip
- Series actions
- Toolbar behavioral tracking
- Intent options
- Formatter
- Styling

### Props

The `MultiMeterBarChart` is a more complex version of the single meter bar, it
allows for different data inputs to be considered when presenting progress
toward a goal, consumption of a total, etc.

OverviewProperties

#### MultiMeterBarChartProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `width?` | | | `100%` | The chart width. A valid CSS width is expected.
 | `height?` | | | `300px` | The chart height. A valid CSS height is expected.
 | `min?` | | `0` | Min value for the multi meter bar chart scale.
 | `max?` | | | `'auto'` | Max value for the multi meter bar chart scale.
 | `colorPalette?` | | | `"categorical"` | Color palette to be used for the segments
 | `loading?` | | `false` | Show the loading indicator when truthy.
 | `size?` | | | The size that applies to the value, icon, and label.
 | `unit?` | | | | The custom unit for the value of the multi meter bar.
 | `formatter?` | | | | Custom Formatter for the chart
 | `prefixIcon?` | | | Icon to show left of the label.
 | `seriesActions?` | (seriesData: ) => | | Exposed callback to display series actions

#### MultiMeterBarSegmentProps

##### Signature:
`export declare type MultiMeterBarSegmentProps = | ;`

#### MultiMeterBarChartTooltipProps
 |
 | Name | Type | Default | Description
 | `variant?` | | `"single"` | Variant to be used for the multi meter bar chart tooltipStill have questions?Find answers in the Dynatrace Community

---

## PieChart

`/design/data-visualizations/charts/PieChart/`

The `PieChart` visualizes data proportions in a circular chart. It divides a
circle into slices, with each slice representing a specific category or value.

OverviewProperties

### Import

`tsx
import { PieChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `PieChart` expects a data structure composed of an array of `slices` and an
optional `unit` as a string.

Each `slice` of the chart should contain the following attributes:

- Category: The name or label for the slice.

- Value: The numerical value representing the size of the slice.

- Color: An optional color assigned to the slice.

Unit: An optional string representing the unit of measurement for the values.

`tsx
{ slices: [ { category: 'EMEA', value: 66, }, ], unit: '$',}
`

Learn more about the data format here.

#### Change the size of a chart

By default, the chart will use the width and height of the available container
while using a 1:1 aspect ratio. The height of the container is 300 pixels by
default, but both a width and a height specified in pixels can be manually set.
If a number is passed to this prop without any unit specified, it will be
treated as `px`.

#### Labels

By default, slice labels are enabled. In order to hide all the labels in the
chart, add the `hidden` prop to the subcomponent.

Labels that don't fit a specific slice will be automatically hidden independent
of the configuration value setting.

The default values for the labels will be `relative` but you can also set it to
the `absolute` value, using the `valueType` prop

#### Change the chart color/s

The `PieChart` provides several ways to customize the appearance of your data:

- Predefined Color Palettes: Choose from a set of built-in color palettes.

- Custom Colors: Define your own color schemes.

- Color Rules: Apply conditional coloring based on data values.

##### Using Color Palettes

The `PieChart` provides a set of predefined color palettes and it also accepts
custom color palettes. See coloring for more
details.

##### Direct Color Assignment

You can directly assign colors to specific slices by including a `color`
property in your data. This takes precedence over the color palette.

##### Using Color Rules

For more advanced coloring scenarios, you can use the `PieChart.ColorRule` slot
to apply conditional coloring based on your data values. This is particularly
useful for highlighting specific data points or applying business logic to your
visualizations.

Color rules can be applied based on different criteria:

- Value-based rules: Color slices based on their numeric value

- Category-based rules: Color specific categories

- Date-based rules: Color based on date comparisons

- Custom property rules: Color based on any property in your data

For more details about available comparators and options, see the
Color Rules
section.

#### Grouping

The grouping defines a way to aggregate multiple slices into a single one.

The slices are grouped depending on a given `threshold` prop. All the slices
with a value that match the input threshold will be part of the group.

It is possible to specify three different types of thresholds:

- `relative`: The threshold is the relative value of the slices (distribution in
percentage). All values lower than the threshold will be part of the group.

- `absolute`: The threshold is the absolute value of the slices. All values
lower than the threshold will be part of the group.

- `number-of-slices`: The threshold is the ordinal number of the slices. Once
the number of slices specified in the threshold is reached, all the others
will be grouped.

By default, the group name is `Other`. This value can be changed by providing it
in the configuration via the `name` prop.

To configure custom groups, use the subcomponent configuration
. If the group configuration is not provided, the
grouping is relative: 2% as default.

#### Legend customization

The purpose of the legend is to provide additional identifying information for
the chart without needing to interact with it directly.

##### Visibility

The legend for the `PieChart` will be shown by default, but it can be optionally
hidden by making use of the `hidden` prop on the subcomponent.

##### Legend position

By default, the legend of the `PieChart` is positioned automatically
(`{position: "auto"}`) to the right, if it has space, or to the bottom if
there's not enough space on the right. It is also possible to customize the
chart's legend position by setting the desired position: `right` or `bottom`.

##### Legend ratio

By default, the legend occupies `75%` of the container width, in the case where
the legend is positioned on the right and `25%` of the container height if the
legend position is on the bottom.

It is possible to override the default legend ratio by setting a custom
percentage value for the ratio prop. The expected value should be in the range
of `5-80`. Values out of expected ranges will roll back to the default legend
ratio.

#### Truncation Mode

The purpose of truncation is to gracefully handle extra long tooltips or legends
within data visualization components. By changing the value of this property,
you have control over where truncation is applied within charts. By default, the
truncation is applied to the `middle` value with the use of an ellipsis.
Truncation can, however be changed to instead be applied at the `start` or `end`
of data visualization component elements.

#### Formatter

As the `PieChart` expects an array of categories with a value and an optional
unit, by default this optional unit will be appended to the specified value, if
it is included. There are two other options in the formatter that allow for
greater customization. The first option enables you to prepend the unit to the
value, while the second option enables you to ignore the original unit and
append a custom string instead.

Additionally, there is a custom formatter option available to allow you to
change the input unit to one of your choice, e.g.: if the input unit is `bits`,
you are able to switch and display the unit as `bytes`, correctly formatted. The
formatted value will appear in the chart tooltip. The use cases below outline
each of these scenarios.

#### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application. The fallback UI occupies the full
width and height of the chart, ensuring that users are still provided with a
meaningful interface even in the presence of errors.

#### EmptyState

The `EmptyState` subcomponent serves as a fallback when there is no data
available to display in a chart. Its purpose is to provide a user-friendly way
of informing the user about the current situation. When there is no data, a
fallback UI is displayed occupying the full width and height of the chart, along
with a default message.

#### Loading

The `loading` prop is a boolean value that can be passed to the `PieChart`
component to control its loading state. When the loading prop is set to true,
the loading indicator appears in the middle of the chart plot to inform the user
that the component is currently fetching or processing data. When the loading
prop is set to false, the component should display its regular content.

#### Toolbar

The toolbar allows you to download data and use added Intents. Displayed by
default, it can be customized by adding the `PieChart.Toolbar` subcomponent,
which supports the `hidden` and `placement` props.

##### Behavioral tracking

The `PieChart.Toolbar` subcomponent supports behavioral tracking attributes that
are spread onto the toolbar root element. This allows tracking of toolbar
interactions such as menu opens, mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `PieChart.Toolbar` to attach
tracking metadata. See `BehaviorTrackingProps` for the full list of supported
attributes.

#### Download data as CSV

The `PieChart` component allows data to be downloaded in CSV format via a
toolbar button. To enable this feature, add the `PieChart.DownloadCSV`
subcomponent to the `PieChart`. Clicking the button will download the raw data
as a CSV file.

The CSV file contains the following columns:

- `category` - the name of the category

- `value` - the value of the category

- `unit` - the unit of the category

It's also possible to programmatically trigger the download of the CSV file by
calling the `downloadData` method on the `PieChart` instance reference.

#### Intent options

The `PieChart` supports intent options in the toolbar. The intents appear in the
toolbar's dropdown menu, allowing users to perform actions such as sharing a
chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `PieChart`, use the `PieChart.Intent` slot, which
contains different props:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

#### Styling

The `PieChart` also accepts custom styling, which could be set using the props
`className` and/or `style`, as a regular html element

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change the size of a chart
- Labels
- Change the chart color/s
- Grouping
- Legend customization
- Truncation Mode
- Formatter
- Error state
- EmptyState
- Loading
- Toolbar
- Download data as CSV
- Intent options
- Styling

### Props

The `PieChart` visualizes data proportions in a circular chart. It divides a
circle into slices, with each slice representing a specific category or value.

OverviewProperties

#### PieChartProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `data` | | | Categorical data of the chart.
 | `width?` | | | `100%` | The width of the chart. A number or a string with accepted CSS units is expected.
 | `height?` | | | `300px.` | The height of the chart. If a number is passed, it will be treated as px.
 | `colorPalette?` | | | `'categorical'.` | Set of Color palette to be used in charts.
 | `formatter?` | | | | Custom Formatter for the chart
 | `truncationMode?` | | `'middle'` | Truncation mode to use (start, middle, end)
Applied to all the parts that truncate text.
 | `seriesActions?` | (slice: ) => | | Exposed callback to display series actions for a slice
 | `loading?` | | `false` | Show the loading indicator when truly.

#### LabelsConfig
 |
 | Name | Type | Default | Description
 | `hidden?` | | `false (all the labels are displayed).` | Hides the slice labels.
 | `valueType?` | | `'relative'` | Display the label with a relative or absolute value.

#### ThresholdConfig
 |
 | Name | Type | Default | Description
 | `type` | | `'relative'.` | Type of the grouping threshold. Can be "relative", "absolute" or "number-of-slices".
 | `value` | | | Value of the group threshold.
Default is dynamically calculated depending on the chart size for relative and absolute. 10 in case of number-of-slices.

#### GroupConfig
 |
 | Name | Type | Default | Description
 | `name?` | | `'Other'.` | Name of the group.
 | `threshold` | | | The threshold for the group.

### PieChart.Toolbar

`PieChart.Toolbar` is a slot to hide or to configure the toolbar.

#### BaseToolbarProps
extends`, ` |
 | Name | Type | Default | Description
 | `hidden?` | | `false` | Decides if the toolbar is visible or hiddenStill have questions?Find answers in the Dynatrace Community
- PieChart.Toolbar

---

## ShareChartConfig

`/design/data-visualizations/charts/ShareChartConfig/`

### Import

`tsx
import { TimeseriesChartConfig, CategoricalBarChartConfig, SingleValueConfig, PieChartConfig, DonutChartConfig, MeterBarChartConfig, MultiMeterBarChartConfig, HoneycombChartConfig, XYChartConfig,} from '@dynatrace/strato-components/charts';
`

### Use cases

#### Multiple chart configuration

In certain situations, it may be beneficial to share a common chart
configuration across multiple charts of the same type. To avoid the need for
repeating the same configuration in each instance, all charts provide a config
provider that can be utilized. This provider accepts an object, where the keys
are either props of the chart component or the corresponding object
representation of each of the chart subcomponent props (e.g.
TimeseriesChart.Legend, CategoricalBarChart.ValueAxis, PieChart.Legend, etc.).

NoteThe configuration set using this provider has a lower priority than the specific
configuration of each chart. This means that if a chart has a specific
configuration, it will override the corresponding property from the provider
configuration.

#### Export chart config

A chart's configuration can be exported at any time for various purposes, such
as sharing the configuration with other applications
through an intent. The current configuration
can be retrieved by creating and assigning a `ref` to the corresponding `ref`
property of the chart, and then calling `ref.getConfig()` method.

NoteWhen the "getConfig" method is invoked, a snapshot of the serialized
configuration is returned. As such, it will not change if the chart's
configuration is subsequently modified. It is recommended to ensure that all
configurations have been applied to the chart before calling this method.

#### Import chart config

The configuration provider for each chart also accepts a `string` as an input
for importing a serialized configuration. When a string is provided, it is
internally parsed and applied as the chart configuration.

NoteIf the configuration provided does not match the properties of the chart
configuration, any unknown properties will be ignored. Additionally, if required
properties are not provided, or the given configuration is invalid, default
values will be applied.
NoteDue to potential version mismatches in chart packages used in different
applications, importing a configuration from another application may not result
in a perfect match.
CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Multiple chart configuration
- Export chart config
- Import chart config

---

## SingleValue

`/design/data-visualizations/charts/SingleValue/`

The `SingleValue` is a simple and concise representation of a single data point
or metric , which can either be a text or a number.

OverviewProperties

### Import

`tsx
import { SingleValue } from '@dynatrace/strato-components/charts';
`

### Use cases

The `SingleValue` expects a single value as an input. You must pass this value
to the visualisation's `data` prop as either a `Number` or `String`. Learn more
about the data format here.

#### Change the size of the SingleValue

The `SingleValue` component will always use all of the available space that it
is given. In order to control the size of the `SingleValue`, it has to be
wrapped inside a container and the container set to your desired size.

#### Customizing and formatting units

When passing a number to the `data` attribute, you can use the `formatter` prop
to change how the number is represented. All the Design System formatters
together with their respective configurations are supported. The suffix provided
by certain formatters will be overwritten by the `unit` prop if defined.

##### Unit prop usage

The `unit` prop accepts either a string or a Unit type from
`@dynatrace-sdk/units`:

`tsx
// String unitSingleValue data={95174635.2456} unit="GigaByte" />// Unit type from @dynatrace-sdk/unitsimport { units } from '@dynatrace-sdk/units';SingleValue data={1024} unit={units.data.byte} />// Custom string unitsSingleValue data={38.9} unit="°C" />SingleValue data={1500} unit="ms" />
`

#### Change the color of the SingleValue

You can customize the `SingleValue`'s appearance in several ways:

- Direct Color Assignment: Use the `color` prop to set any
`Design System color token`, `rgb`, `hex`, or `CSS color`.

- Color Rules: Apply conditional coloring based on the value or other
properties.

##### Direct Color Assignment

With the `color` prop you can change the `SingleValue`'s color to any
`Design System color token` as well as any `rgb`, `hex` or `CSS color`. If no
color is set, the default color is automatically set based on the current theme.

##### Using Color Rules

For more advanced coloring scenarios, you can use the `SingleValue.ColorRule`
slot to apply conditional coloring based on your data values. This is
particularly useful for highlighting specific data points or applying business
logic to your visualizations.

Color rules can be applied based on different criteria:

- String-based rules: Match text patterns in your data using comparators
like 'starts-with', 'ends-with', or 'matches-phrase'

- Numeric rules: Apply colors based on numeric comparisons like
'greater-than', 'less-than', etc.

- Multiple rules: Combine multiple rules for complex coloring logic

In the example above, we're using several rules:

- Color any value starting with "HOST" using the 'magenta-inverted' color
palette

- Color any value ending with "768C" with a specific hex color (#00ffff)

- Color any value exactly matching "Series 2" using the
'blue-turquoise-inverted' palette

For more details about available comparators and options, see the
Color Rules
section.

#### Add more context to a Single Value

In order to add additional context to a `SingleValue`, you can add any
combination of the following props to the visualization:

- `prefixIcon`: This prop allows you to set a prefixed symbol as a ReactNode,
consisting of an icon, emoji, single character, glyph, or Design System icon.
It will be displayed to the left of the value.

- `unit`: With this prop it is possible to set a custom unit to be displayed
with the single value, which will be appended to the right of the value. This
prop takes priority over units provided with the formatter prop.

- `label`: This prop enables you to set a custom text which will be shown above
the value.

#### Add additional context by visualizing a trend over time

In its most basic configuration a `SingleValue` displays exactly that, a single
value. In most use cases, however, a numerical value changes over time. In order
to add additional context to the value being displayed and its change over time
an optional `sparkline` can be added to the `SingleValue` visualization.

##### Sparkline

In order to display a `Sparkline` within the `SingleValue` component you need to
add the subcomponent to the `SingleValue` chart. The `Sparkline`
component requires data of type `Timeseries` or `Timeseries[]` to be passed to
the `data` prop. If more than one series is provided, the first one is used. The
datapoints within the series need to provide a time dimension as well as a
numerical value.

The `Sparkline` has three variants and can be either displayed as a
`line`(default), `area` or `bar`.

You can further customise the `Sparkline` by setting its `color` prop to any of
the `Design System ColorPalette`.

Lastly, x-axis ticks can be visualized on the `Sparkline` by using the
`showTicks` prop. By default, these ticks are hidden.

#### Loading

The `SingleValue` component is able to show the default loading indicator
setting the `loading` prop to `true`.

#### Empty State

By using the subcomponent it is possible to define a custom
message that will be displayed if no data was provided to the `SingleValue`
component.

#### Error State

The subcomponent can be used to customise the error message
that will be displayed when an error occurs in the `SingleValue` component.

#### Intent options

The `SingleValue` supports intent options in the toolbar. The intents appear in
the toolbar's dropdown menu, allowing users to perform actions such as sharing a
chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `SingleValue`, use the `SingleValue.Intent`
subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in SingleValue:

#### Thresholds on Sparkline

Thresholds are used to mark meaningful ranges or values on a `Sparkline` and
they add contextual information to a numerical axis. There are two variants of
thresholds:

- a specific point represented by a line across.

- a range - or filled area - represented by a band across.

##### Point and Range

Both point and range can be represented by static or dynamic data sources. A
static data source has a single value representing a point or a single key-value
pair representing a fixed range. A dynamic data source has a data array
containing more than one value or various key-value pairs.

There are three different types of threshold markers:

Range filled, where the value range is defined in order to display the
threshold band. The upper and lower lines are not drawn.

Range stroke-only variant, where a value range is defined in order to display
the threshold band represented by upper and lower dashed lines.

Point, where only one value is required to display the threshold. It's
represented by a dashed line.

##### Dynamic Point and Dynamic Range

##### Dynamic Range Stroke Only and Static Ranges

##### Point and Range with Area Variant

#### Add detailed information about the trend

Another way to add detailed information about the `SingleValue` trend is to use
a `Trend` component.

##### Trend

The `Trend` allows you to configure and display a current state of trend
including trend direction icon, color, trend value, and label.

In order to display a `Trend` within the `SingleValue` component you need to add
the subcomponent to the `SingleValue` component.

##### Trend anatomy

The `Trend` component consists of the following elements:

- icon

- value

- label

If label and value are empty the trend direction icon will be hidden.

To set the trend direction the `direction` prop should be used. The `direction`
prop accepts one of the following values: `upward`, `downward`, and `neutral`.

The `showIcon` prop is used to show or hide the trend direction icon. By
default, the `showIcon` prop is set to `true`.

The `value` prop is used to set the trend value. The `value` prop accepts a
numeric value.

The `label` prop is used to set the trend label.

##### Trend direction calculation based on value

When a `value` prop is provided without a `direction` prop, the trend direction
is calculated based on the `value` prop's sign: positive value results in
`upward` trend direction, negative value in `downward` trend, and zero value in
`neutral` trend direction.

In case neither the `direction` nor `value` prop is provided, the trend
direction is set to `neutral`.

##### Trend coloring and formatting options

The color for each direction of a trend can be customized using the
`colorOverrides` prop. The `colorOverrides` prop accepts an object with the
following optional keys: `upward`, `downward`, and `neutral`. Each key accepts a
string representing a valid CSS color.

The `formatter` prop can be used to format the trend value including adding a
unit (e.g. `bytes`, `bits`, etc.).

##### Inverse trend

An upward trend direction doesn't always represent a positive change, and the
downtrend doesn't always represent a negative one. For example, when displaying
a trend of a response time, a downward trend direction represents a positive
change, while an upward trend in a host CPU usage represents a negative change.

To inverse a trend the `inverseTrend` prop should be used. Currently, the
`inverseTrend` prop accepts two options: `none` and `color`. The `none` option
doesn't affect the trend in any way and is a default behaviour. The `color`
option inverts the default colors of the icon and the value (i.e. the icon and
the value are colored as if the trend direction is opposite to the actual trend
direction).

When `colorOverrides` are used, the `inverseTrend` prop with `color` option gets
ignored.

#### Putting it all together

#### Render multiple SingleValues in a grid

In order to render multiple `SingleValue` components in a grid, you can use the
`SingleValueGrid` component. `SingleValue` components in the grid will share the
internal layout and styles to create a consistent look and feel. The component
will occupy all the available space in the container it's located in and
automatically render the `SingleValue` components.

The `SingleValueGrid` component expects an array of strings, numbers, or objects
of a free shape.

##### Control over the grid elements using accessors

In order to have more granular control over the grid elements look, you can pass
an array of objects to the `SingleValueGrid` component. Using `Value`, `Trend`,
and `Sparkline` subcomponents with various accessors you can customize the grid
elements. Accessor is a string that represents a name of a prop name (or nested
prop name using a dot notation, e.g. `trend.direction`) in the data array object
that should be used to override original prop of the `SingleValue` component and
it's subcomponents.

###### Grid accessors and props

On the `SingleValueGrid` component, you can use the following accessors:

- `colorAccessor` - accessor to override a colors for individual grid elements.

- `labelAccessor` - accessor to override a label.

- `prefixIconAccessor` - accessor to override a prefix icon.

The `SingleValueGrid` also accepts a `color` prop to set a default color for all
grid elements. When both `color` and `colorAccessor` props are provided, the
grid element will try to access a color in the data object using the
`colorAccessor`, and if it's not found, the `color` prop value will be applied.
The same logic applies to most of the accessors.

On a grid level it's also possible to set value alignment using the `alignment`
prop and thresholds using the `thresholds` prop.

The `SingleValueGrid` also supports intent options using the
`SingleValueGrid.Intent` subcomponent, which works the same way as the
`SingleValue.Intent` subcomponent described in the
Intent options section above.

Additionally, you can also toggle the prop `applyThresholdBackground` to set the
applicable threshold color to the background of all the SingleValue components
inside the grid.

###### Loading state in grid

The `SingleValueGrid` supports a grid-level `loading` prop. When `loading` is
set to `true`:

- a single `SingleValue` loading indicator/overlay is set over the whole grid,

- individual item values may be `null`/`undefined` while the overlay is shown.

GIVEN a `SingleValueGrid` with `loading` set to `true` WHEN the component
renders THEN a loading overlay with spinner is set over the grid

Use the dedicated Loading use case below to inspect the overlay across all grid
items.

###### Value accessors and props

On the `Value` subcomponent, you can use the following accessors:

- `dataAccessor` - accessor to get a value from data array object.

- `formatterAccessor` - accessor to retrieve the formatter options for the
value.

- `unitAccessor` - accessor to retrieve the unit for the value.

The `unit` and `formatter` props can be used to set a default unit and formatter
for all grid elements. The `unit` prop accepts either a string or a Unit type
from `@dynatrace-sdk/units`:

`tsx
// Using string units in data objectsconst data = [ { data: 38.9, label: 'Temperature', unit: '°C' }, { data: 12, label: 'Count', unit: 'hosts' },];// Using Unit types in data objectsimport { units } from '@dynatrace-sdk/units';const data = [{ data: 1024, label: 'Memory', unit: units.data.byte }];// Setting default unit on SingleValueGrid.Value componentSingleValueGrid.Value dataAccessor="data" unit="ms" // string unit unitAccessor="unit"/>;
`

###### Trend accessors and props

On the `Trend` subcomponent, you can use the following accessors:

- `directionAccessor` - accessor to get a trend direction.

- `valueAccessor` - accessor to get a trend value.

- `labelAccessor` - accessor to get a trend value.

- `formatterAccessor` - accessor to get formatter for the trend value.

- `inverseTrendAccessor` - accessor to retrieve an inverse trend options.

###### Sparkline accessors and props

The `Sparkline` subcomponent extends the standard `Sparkline` component with two
accessors:

- `dataAccessor` - accessor to get a data for the sparkline.

- `colorAccessor` - accessor to get a color of the sparkline.

##### Grid - putting it all together

Let's have a look at the grid with all the accessors and props in action.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Change the size of the SingleValue
- Customizing and formatting units
- Change the color of the SingleValue
- Add more context to a Single Value
- Add additional context by visualizing a trend over time
- Loading
- Empty State
- Error State
- Intent options
- Thresholds on Sparkline
- Add detailed information about the trend
- Putting it all together
- Render multiple SingleValues in a grid

### Props

The `SingleValue` is a simple and concise representation of a single data point
or metric , which can either be a text or a number.

OverviewProperties

#### SingleValueProps
extends |
 | Name | Type | Default | Description
 | `loading?` | | `false` | Show the loading indicator when truly.
 | `width?` | | | `100%` | Chart width. When a number is specified, it's treated in pixels,
otherwise a valid width string is expected (e.g., "100%", "200px").
 | `height?` | | | `100%` | Chart height. When a number is specified, it's treated in pixels,
otherwise a valid height string is expected (e.g., "100px", "50%").

### SingleValue.Sparkline

`SingleValue.Sparkline` provides a subcomponent where the Sparkline component
can be added.

#### SingleValueSparklineProps

##### Signature:
`export declare type SingleValue = >;`

#### SparklineProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `data` | | [] | | Data to show
 | `color?` | | | Sparkline color
 | `variant?` | | | Sparkline variant (line, area)
 | `showTicks?` | | | Whether Sparkline shows X Axis ticks or not
 | `loading?` | | | When true: Sets an overlay with default loader
 | `gapPolicy?` | | | Gap policy
 | `curve?` | | `'linear'` | Curve shape of the series
 | `showContextValues?` | | | Whether Sparkline shows min/max values or not
 | `labelsAlignment?` | | | Whether Sparkline aligns labels to left or right
Curve shape of the series
 | `labelsFixedWidth?` | | | When Sparkline labels have a fixed width
 | `width?` | | | | Width of the sparkline component
Accepts string values (e.g., '100%', '200px') or numeric values (rendered as pixels)
 | `height?` | | | | Height of the sparkline component
Accepts string values (e.g., '50px', '100%') or numeric values (rendered as pixels)

#### SparklineYAxisProps
 |
 | Name | Type | Default | Description
 | `max?` | | | `'data-max'` | Maximal value on the y-axis.
 | `min?` | | | `'data-min'` | Minimal value on the y-axis.
 | `scale?` | | `'linear'` | The scale of the Y axis values. Is only applied to the bar variant.
 | `formatter?` | | | | Sparkline Y tick formatter

#### SingleValue.Sparkline.YAxis

`SingleValue.Sparkline.YAxis` provides a subcomponent to configure the Y-axis of
the Sparkline incorporated into the SingleValue component.

#### SparklineYAxisProps
 |
 | Name | Type | Default | Description
 | `max?` | | | `'data-max'` | Maximal value on the y-axis.
 | `min?` | | | `'data-min'` | Minimal value on the y-axis.
 | `scale?` | | `'linear'` | The scale of the Y axis values. Is only applied to the bar variant.
 | `formatter?` | | | | Sparkline Y tick formatter

### SingleValue.Trend

`SingleValue.Trend` provides a subcomponent where the Trend component can be
added.

#### TrendProps
 |
 | Name | Type | Default | Description
 | `direction?` | | | The direction of a trend.
 | `showIcon?` | | `true` | Flag to show the icon or not.
 | `value?` | | | The trend value
 | `label?` | | | The trend label
 | `inverseTrend?` | | `'none'` | Inverts 'upward' and 'downward' color options.
 | `colorsOverride?` | | | Overrides colors of the trend icon and value for trend directions.
 | `formatter?` | | | | If specified, the value will be formatted with given formatter options.

### SingleValue.EmptyState

`SingleValue.EmptyState` provides a subcomponent where the Empty state wrapper
can be set.

#### EmptyStateProp
 |
 | Name | Type | Default | Description
 | `children` | | |

### SingleValue.ErrorState

`SingleValue.ErrorState` provides a subcomponent where the Error state wrapper
can be set.

#### ErrorStateProps
 |
 | Name | Type | Default | Description
 | `children` | | ((errorMessage: ) => .) | |

### SingleValueGrid

#### SingleValueGridProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `loading?` | | `false` | Show the loading indicator when truly.
 | `data` | ( | | )[] | | The data source for the SingleValueGrid component.
 | `color?` | | | The default color for the SingleValues.
This color will be overwritten by individual colors specified in the SingleValueGridData or ColorRules slot.
 | `colorAccessor?` | | | Accessor function to override colors for individual SingleValue components.
 | `applyThresholdBackground?` | | | This option will define if the color is applied to the value or to the background.
 | `labelAccessor?` | | | Accessor function for individual labels of each SingleValue component.
 | `prefixIconAccessor?` | | | Accessor function for individual prefix icons of each SingleValue component.
 | `alignment?` | | `'start'` | Horizontal alignment of icons, values, units, labels, and trends within each SingleValue component.
 | `seriesActions?` | (data: ) => | | Actions to be shown in individual SingleValue components

#### SingleValueGridValueProps
 |
 | Name | Type | Default | Description
 | `dataAccessor?` | | | Accessor function to retrieve the data for the value.
 | `formatter?` | | | | Formatter options for formatting the value.
 | `formatterAccessor?` | | | Accessor function to retrieve the formatter options for the value.
 | `unit?` | | | Unit for the value.
 | `unitAccessor?` | | | Accessor function to retrieve the unit for the value.

#### SingleValueGridSparklineProps
extends |
 | Name | Type | Default | Description
 | `dataAccessor?` | | | Accessor function or string to retrieve the data for the sparkline.
 | `colorAccessor?` | | | Accessor function to retrieve the color of the sparkline.

#### SingleValueGridTrendProps
 |
 | Name | Type | Default | Description
 | `directionAccessor?` | | | Accessor to retrieve the trend direction.
 | `valueAccessor?` | | | Accessor to retrieve the trend value.
 | `labelAccessor?` | | | Accessor to retrieve the trend label.
 | `showIcon?` | | `true` | Determines whether to show the trend icon.
 | `colorsOverride?` | | | Overrides the colors of the trend icon and value for different trend directions.
 | `formatter?` | | | | Formatter options or function to format the trend value.
 | `formatterAccessor?` | | | Accessor to retrieve the formatter options for the trend value.
 | `inverseTrend?` | | `'none'` | Inverts 'upward' and 'downward' color options.
 | `inverseTrendAccessor?` | | | Accessor to retrieve the inverse trend options.Still have questions?Find answers in the Dynatrace Community
- SingleValue.Sparkline
- SingleValue.Sparkline.YAxis
- SingleValue.Trend
- SingleValue.EmptyState
- SingleValue.ErrorState
- SingleValueGrid

---

## Sparkline

`/design/data-visualizations/charts/Sparkline/`

The `Sparkline` is a compact and simple data visualization that displays a trend
or pattern of data in a small, condensed format. It typically consists of a
single line or area graph, without axes or labels, that represents the variation
of data points over time.

OverviewProperties

### Import

`tsx
import { Sparkline } from '@dynatrace/strato-components/charts';
`

### Use cases

The `Sparkline` component requires you to pass data of type `Timeseries` or
`Timeseries[]` to the data prop. A `Timeseries` object has a `name`, an array of
`TimeseriesDatapoint` and an optional `unit`. Each data point must have a
numeric `value`, a `start`, and optional `center` and `end` dates. If you
provide more than one series, only the first one is used.

`tsx
[ { name: ['Query consumption'], unit: 'byte', datapoints: [ { start: new Date('Wed, 22 Mar 2022 12:00:00 UTC'), end: new Date('Wed, 22 Mar 2022 12:01:00 UTC'), value: 13434958, }, { start: new Date('Thu, 22 Mar 2022 12:01:00 UTC'), end: new Date('Wed, 22 Mar 2022 12:02:00 UTC'), value: 129555269, }, { start: new Date('Thu, 22 Mar 2022 12:02:00 UTC'), end: new Date('Wed, 22 Mar 2022 12:03:00 UTC'), value: 74177850, }, ], },];
`

Learn more about the data format here.

You can further customise the `Sparkline` by setting its `color` prop to any of
the Design System `ColorPalette`.

The `Sparkline` is able to show the default loading indicator setting the
`loading` prop to `true`.

Lastly, x-axis ticks can be visualized on the `Sparkline` by using the
`showTicks` prop. By default, these ticks are hidden.

#### Variants

The `Sparkline` has three variants and can be displayed as a `line` (default),
`area`, or `bar`. It is important to note that not all features and props apply
to all variants equally, for example curve has no effect in `bar` variant, and
scale has effect only in `bar` variant

#### Loading

#### Empty State

By using the subcomponent it is possible to define a custom
message that will be displayed if no data was provided to the `Sparkline`
component.

#### Error State

The subcomponent can be used to customise the error message
that will be displayed when an error occurs in the `Sparkline` component.

#### Scales

The `Sparkline` component supports the Y-axis scale configuration. To configure
a scale, the `Sparkline.YAxis` subcomponent should be used. The
`Sparkline.YAxis` component requires a `scale` prop to be passed with the two
possible options: `linear` (default) or `log`.

#### Gap policy

Gaps in data refer to missing or unrepresented values between existing data
points. In a dataset exclusively with timestamps, no continuity can be
determined and therefore there are always “gaps” between data points regardless
of the resolution of the dataset. In a timeframe dataset however, gaps are
considered when the end timestamp of the previous data point is earlier than the
start timestamp of the next data point, meaning there is a timespan between the
end of a previous data point and the next one with no given value.

The Sparkline provides the `gapPolicy` prop to configure how gaps are visualized
in a chart. There are two `gapPolicy` options available: gap, and connect.

- The `gap` option displays gaps on the chart as is (e.g. breaks along a line).
This option helps to see the absence of data during a period of time.

- The `connect` option connects consecutive data points irrespective of the gap
using linear interpolation.

#### Context values

The Sparkline provides the `showContextValues` prop which allows to display
indicators with labels showing the maximum and minimum values of the provided
data. The indicators will highlight both the maximum and minimum value of the
dataset.

If you provide a custom `YAxis`, the context values will only be visible if they
are within your custom `Axis` minimum and maximum value.

#### Thresholds

Thresholds are used to mark meaningful ranges or values on a `Sparkline` and
they add contextual information to a numerical axis. There are two variants of
thresholds:

- a specific point represented by a line across.

- a range - or filled area - represented by a band across.

#### X-axis

To configure the x-axis of the `Sparkline`, the `Sparkline.XAxis` subcomponent
can be added. The axis boundaries can be set using the `min` and `max` props,
which support timestamps of type `number` and `Date`, as well as `auto` and
`data-min` for the `min` property and `data-max` for the `max` property.

By default, the `auto` value is used for both `min` and `max` properties, which
automatically determines the minimum and maximum values of the x-axis scale
based on the data provided in the chart (similar to `data-min` and `data-max`).

##### Point and Range

Both point and range can be represented by static or dynamic data sources. A
static data source has a single value representing a point or a single key-value
pair representing a fixed range. A dynamic data source has a data array
containing more than one value or various key-value pairs.

There are three different types of threshold markers:

Range filled, where the value range is defined in order to display the
threshold band. The upper and lower lines are not drawn.

Range stroke-only variant, where a value range is defined in order to display
the threshold band represented by upper and lower dashed lines.

Point, where only one value is required to display the threshold. It's
represented by a dashed line.

##### Dynamic Point and Dynamic Range

##### Dynamic Range Stroke Only and Static Ranges

##### Point and Range with Area Variant and Ticks

#### Series Range

The `Sparkline` component supports `curve` prop only in the line and area
variant. By default, this value is set to `linear` showing sharp corners in the
joins of the lines. It can also be set to `smooth` providing a continuous curve.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Variants
- Loading
- Empty State
- Error State
- Scales
- Gap policy
- Context values
- Thresholds
- X-axis
- Series Range

### Props

The `Sparkline` is a compact and simple data visualization that displays a trend
or pattern of data in a small, condensed format. It typically consists of a
single line or area graph, without axes or labels, that represents the variation
of data points over time.

OverviewProperties

#### SparklineProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `data` | | [] | | Data to show
 | `color?` | | | Sparkline color
 | `variant?` | | | Sparkline variant (line, area)
 | `showTicks?` | | | Whether Sparkline shows X Axis ticks or not
 | `loading?` | | | When true: Sets an overlay with default loader
 | `gapPolicy?` | | | Gap policy
 | `curve?` | | `'linear'` | Curve shape of the series
 | `showContextValues?` | | | Whether Sparkline shows min/max values or not
 | `labelsAlignment?` | | | Whether Sparkline aligns labels to left or right
Curve shape of the series
 | `labelsFixedWidth?` | | | When Sparkline labels have a fixed width
 | `width?` | | | | Width of the sparkline component
Accepts string values (e.g., '100%', '200px') or numeric values (rendered as pixels)
 | `height?` | | | | Height of the sparkline component
Accepts string values (e.g., '50px', '100%') or numeric values (rendered as pixels)

#### SparklineYAxisProps
 |
 | Name | Type | Default | Description
 | `max?` | | | `'data-max'` | Maximal value on the y-axis.
 | `min?` | | | `'data-min'` | Minimal value on the y-axis.
 | `scale?` | | `'linear'` | The scale of the Y axis values. Is only applied to the bar variant.
 | `formatter?` | | | | Sparkline Y tick formatter

#### SparklineThresholdProps
DeprecatedUse Sparkline.ThresholdIndicatorProps instead. |
 | Name | Type | Default | Description
 | `data` | | | The threshold data to be graphed by the component
 | `color` | | | The unique color picked for this timeseries representation in HEX, RGB, Color Token or HSL.
 | `strokeOnly?` | | | Whereas to show the threshold ranges filled or only the strokes

### Sparkline.ThresholdIndicator

`Sparkline.ThresholdIndicator` provides a slot for defining thresholds in the
chart.

#### SparklineThresholdIndicatorProps
 |
 | Name | Type | Default | Description
 | `data` | | | The threshold data to be graphed by the component
 | `color` | | | The unique color picked for this timeseries representation in HEX, RGB, Color Token or HSL.
 | `strokeOnly?` | | | Whereas to show the threshold ranges filled or only the strokesStill have questions?Find answers in the Dynatrace Community
- Sparkline.ThresholdIndicator

---

## TimeseriesChart

`/design/data-visualizations/charts/TimeseriesChart/`

The `TimeseriesChart` visually represents data in sequential order of time. It's
used to observe trends, patterns, and fluctuations in the data over a specific
time period.

OverviewProperties

### Import

`tsx
import { TimeseriesChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `TimeseriesChart` expects a data structure composed of an array of
`datapoints`, a `name` as a string or an array of strings (which will be
displayed in the tooltip and the legend), and an optional `unit` as a string or
Unit.

Each `datapoint` should contain the following attributes:

- start: the starting timestamp for the datapoint representation.

- value: A number represented in the datapoint. This can either be the absolute
value or a relative value.

- end: An optional attribute that represents an ending timestamp for the
datapoint representation.

- center: An optional attribute for that sits in the middle between start and
end.

The time dimension can either be handled as a `timestamp` if only a start
timestamp is given, or as a `timeframe` if both a start and an end timestamp are
provided for the datapoint.

`tsx
[ { name: ['pl1l-vh48.example.com', 'HYPERVISOR-CC7CFC844F787622'], unit: 'percent', datapoints: [ { start: new Date('Tue, 05 Apr 2022 12:18:00 UTC'), end: new Date('Tue, 12 Apr 2022 12:19:00 UTC'), value: 51, }, ], },];
`

Learn more about the data format here.

#### Size

By default, the chart will use all the available container size up to a maximum
height of 300 pixels and width of 100%. This height and width can be changed by
providing a value in the `height` and `width` props of the `TimeseriesChart`. If
a number is passed to these props, it will be treated as `px`. If a string is
passed, it will be treated as a CSS string.

#### Variants

The `TimeseriesChart` supports three different chart variants: Area, bar and
line. If no value is provided in the `variant` prop, the line variant is used by
default. It is important to note that not all features and props apply to all
variants equally. Each of these specific cases are outlined in the use cases
below.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the
`TimeseriesChart`. More subcomponents can be added within this component, for
instance `ChartSeriesAction.Item`, where you can provide a custom action that
will appear in the legend menu. That action can execute any custom logic in its
`onSelect` callback or get disabled via a `disabled` prop. `Intents` could be
added as part of the series action as well with `ChartSeriesAction.Intent`.

#### Messages

This feature allows you to display messages in the browser console using a
custom handler. In addition to the text output itself, each message also
includes a level of severity, namely `warning` or `error`. Chart messages can be
used to notify you about inconsistencies in the data for instance. The messages
of type `ChartMessage` can be passed to the `TimeseriesChart` using the
`onMessage` prop.

#### Gap policy

Gaps in data refer to missing or unrepresented values between existing data
points. In a dataset exclusively with timestamps, no continuity can be
determined and therefore there are always “gaps” between data points regardless
of the resolution of the dataset. In a timeframe dataset however, gaps are
considered when the end timestamp of the previous data point is earlier than the
start timestamp of the next data point, meaning there is a timespan between the
end of a previous data point and the next one with no given value.

The TimeseriesChart provides the `gapPolicy` prop to configure how gaps are
visualized in a chart. There are three `gapPolicy` options available: gap,
connect, and threshold.

- The `gap` option displays gaps on the chart as is (e.g. breaks along a line).
This option helps to see the absence of data during a period of time.

- The `connect` option connects consecutive data points irrespective of the gap
using linear interpolation.

- The `threshold` option provides a mechanism to configure thresholds of a
certain time (e.g. 30 seconds, 5 minutes, 1 day, 3 months, etc.). When the gap
between sequential data points in the dataset is less than or equal to the
threshold, then the data points will be connected.

Note: The `gapPolicy` prop is only supported in area and line chart variants and
with the band subcomponent. The bar chart variant doesn't support a gapPolicy
and does not react to the property configuration.

#### Value representation

By default, values within a chart are displayed as is - with their absolute
value (e.g. 3.14 kB). This can, however, be changed so that instead of absolute
values, relative values are represented. Relative values indicate the proportion
that a given series or datapoint contributes to the sum (100%) of a given
timestamp or timeframe. The `valueRepresentation` prop can be used to change
this behavior. Only timeframes/timestamps with the same unit will be stacked. If
there is only one series of a given unit, the relative value is based on the
maximum value within the given series.

In the line and band variant, relative values are always calculated based on
the highest value in the dataset, regardless of whether the series are stacked
or not. This ensures consistency in representation, as the highest value in the
series becomes the baseline for calculating the relative percentages.

#### Change the chart color/s

The `TimeseriesChart` provides several ways to customize the appearance of your
data:

- Predefined Color Palettes: Choose from a set of built-in color palettes.

- Custom Colors: Define your own color schemes.

- Color Rules: Apply conditional coloring based on data values.

##### Using Color Palettes

The `TimeseriesChart` provides a set of predefined color palettes and it also
accepts custom color palettes. See coloring for
more details.

##### Using Color Rules

For more advanced coloring scenarios, you can use the
`TimeseriesChart.ColorRule` slot to apply conditional coloring based on your
data values. Here are some examples:

Series with Conditional Coloring

##### Direct Color Override

You can also directly override colors for specific series using the `color` prop
on chart shapes. This approach is simpler but less flexible than using color
rules.

#### Legend

The purpose of the legend is to provide additional identifying information for
the chart, without needing to interact with the legend directly.

#### Truncation Mode

The purpose of truncation is to gracefully handle extra long labels within data
visualization components. By changing the value of this property, you have
control over where truncation is applied within charts. By default, the
truncation is applied to the `middle` of labels with the use of an ellipsis.
Truncation can, however be changed to instead be applied at the `start` or `end`
of data visualization component labels.

#### Series curve

You can select the curve shape of the line, band and area series via the `curve`
prop. The available options are 'linear' where line joins will be straight
(default option) or 'smooth' for a more fluid curve.

##### Visibility

The legend of the `TimeseriesChart` is shown by default. In order to hide or
show the legend, you need to set the value of `legend.hidden` on the
subcomponent.

##### Position

By default, the position of the legend of the `TimeseriesChart` is set
automatically. This option prioritizes the legend placement to the right of the
chart area. When the chart width is reduced, the legend is repositioned to the
area beneath the chart. It is also possible to explicitly set the chart's legend
position to right or bottom with the `position` prop.

##### Legend ratio

By default, the legend occupies `25%` of the container width, in the case where
the legend is positioned on the right and `25%` of the container height if the
legend position is on the bottom.

It is possible to override the default legend ratio by setting a custom
percentage value for the ratio prop. The expected value is in the range of
`5-80`. Values out of expected ranges will roll back to the default legend
ratio.

#### Chart Interactions

The `TimeseriesChart` provides various interactions (e.g. zoom-x, zoom in, zoom
out, and pan) that can be optionally enabled. See
chart interactions for more details.

#### Shared Crosshair

This feature enables you to synchronize the crosshair position across multiple
charts. To synchronize crosshair between charts `SynchronizationProvider`
component should be used as a wrapper around the charts that need to share the
crosshair position.

#### Download data as CSV

The `TimeseriesChart` component supports download data in CSV format using a
toolbar button. To enable this feature, a `TimeseriesChart.Toolbar` subcomponent
must be provided to the `TimeseriesChart` component. On click of the download
button, raw data will be downloaded as a CSV file.

The CSV file contains the following columns:

- `dimension-(n)` - the name of the dimension, where `n` is the index of the
dimension

- `series` - the full name of the series (all dimensions concatenated using `•`
symbol)

- `unit` - the unit of the series

- `start` - the start timestamp of the data point

- `end` - the end timestamp of the data point

- `value` - the value of the data point

It's also possible to programmatically trigger the download of the CSV file by
calling the `downloadData` method on the `TimeseriesChart` instance reference.

#### Toolbar behavioral tracking

The `TimeseriesChart.Toolbar` subcomponent supports behavioral tracking
attributes that are spread onto the toolbar root element. This allows tracking
of toolbar interactions such as menu opens, zoom/pan mode changes, and download
actions.

Pass any `data-dt-*` attributes directly on `TimeseriesChart.Toolbar` to attach
tracking metadata. See `BehaviorTrackingProps` for the full list of supported
attributes.

#### Intent options

The `TimeseriesChart` supports intent options in the toolbar. The intents appear
in the toolbar's dropdown menu, allowing users to perform actions such as
sharing a chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `TimeseriesChart`, use the `TimeseriesChart.Intent`
subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in TimeseriesChart:

#### Multiple chart configuration

Given certain situations it can be helpful to share a common chart configuration
across several `TimeseriesChart` instances. To avoid repeating the same
configuration in all instances, the `TimeseriesChartConfig` provider can be
used. It accepts an object where the keys are either props of the
`TimeseriesChart` component, or the corresponding object representation of each
one of the `TimeseriesChart` subcomponents props. (`TimeseriesChart.Legend`,
`TimeseriesChart.YAxis`, `Timeseries.XAxis`, `Timeseries.Tooltip`).

A specific configuration of a `TimeseriesChart` instance will take precedence
over the one specified in the `TimeseriesChartConfig`.

#### Axes

To configure the axes of the `TimeseriesChart`, the `TimeseriesChart.XAxis` and
`TimeseriesChart.YAxis` subcomponents can be added. The `label` property sets
the axis label. Axis scale boundaries can be set with the `min` and `max` props.
The Y-axis `scale` property can be used to set the value scale to either
`linear` or `log` (logarithmic).

The `TimeseriesChart.XAxis` supports timestamps of type `number`, whereas the
`TimeseriesChart.YAxis` subcomponent also supports `data-max` in the `max`
property and `data-min` in the `min` property. These special values allow for
granular control over the Y-axis scale boundaries. By default, the `auto` value
is used for both `min` and `max` properties. The `auto` mode automatically
determines both the minimum and maximum values of the Y-axis scale based on the
data in the chart (similar to `data-min` and `data-max`) and sets the Y-axis
baseline to zero.

##### Multiple Y-axes

The `TimeseriesChart` supports multiple Y-axes. `TimeseriesChart.YAxis` provides
a `position` property which can be set to either `left` or `right`.

When you specify multiple Y-axes, the chart automatically assigns data series to
Y-axes based on the unique units of the data. The first unique unit is assigned
to the left Y-axis, and the second unique unit to the right Y-axis. Note that
any additional data series with different units from those already used will not
be displayed.

Filtering the data on the legend could result in moving the data from the right
axis to the left if there are no left series displayed in the legend.

Currently, it's not possible to assign data series to specific Y-axes, nor is it
possible to use the same unit for both Y-axes.

Having a timeseries with two units with different Y-Axes defined:

- If only one left Y-Axis is defined, only the first unit will be displayed on
the left.

- If only one right Y-Axis is defined, only the first unit will be displayed on
the right.

- If both Y-Axes are defined, the first unit will be placed on the left, and the
second unit on the right.

- If both Y-Axes are defined and the `valueRepresentation` is set to relative,
only the left axis will be displayed and show the percentage.

#### Tooltip

Tooltips are used to display additional detailed information about a selected
data point and can be enabled by adding the `TimeseriesChart.Tooltip`
subcomponent. The tooltip `variant` defines whether the tooltip should contain
data points from all series (shared) for the selected timestamp, or just the
closest one (single). The `seriesDisplayMode` prop can be used to define whether
the tooltip should be comprised of a single line of information or multiple
lines.

The Tooltip items sequence, will appear in the same order of the series plotted
in the chart.

##### Single

##### Shared

#### Formatter

The unit for the `TimeseriesChart`, by default, will be appended to the
specified value. There are two other options in the formatter that allow for
greater customization. The first option enables you to prepend the unit to the
value, while the second option enables you to ignore the original unit and
append a custom string instead. Additionally, there is a custom formatter option
available to allow you to change the input unit to one of your choice, e.g.: if
the input unit is `bits`, you are able to switch and display the unit as
`bytes`, correctly formatted. The formatted value is applied in the axis ticks,
as well as in the tooltip and the axis magnifier. The use cases below outline
each of these scenarios.

The precision of the formatter will adapt automatically based on the data
decimals if there is no precision configuration from the custom formatter
option.

#### Annotations

Annotations are used to visualize specific events or contextual notes on the
`TimeseriesChart` in the form of markers placed in time-based tracks.

The marker represents an annotation at a certain point or period in time. They
can be either timestamp-based (a circular shaped marker) or timeframe-based (a
pill shaped marker) depending on the type of the annotation data point.
Annotations with the same timestamp/timeframe are grouped together under a
single marker that displays the number of grouped annotations. Markers can be
displayed on a single or multiple tracks. When there are more than three tracks,
an overflow scroll is applied.

##### Add annotations to the chart

In order to visualize annotation data inside the `TimeseriesChart` a
`TimeseriesChart.Annotations` component should be initialized. This component
should have at least one track, that contains a marker component per annotation
data point.

An annotation data point should contain a time dimension just as the
`TimeseriesChart` (`start` and optional `end`), an optional `symbol`, `title`,
and `description`, which will be displayed in the tooltip.

##### Marker content

When the `symbol` is provided, it will become the marker content by default.
When not, the `title` will be shown as marker content.

In case the content of the marker is bigger than the size of the marker
(timestamp/timeframe size in TimeseriesChart), it will expand to fit all the
content inside, decoupling from the original scale. In these particular cases,
it is encouraged to use the indicators, which will represent the real size of
the bin.

##### Visual customization

Tracks and markers support visual customization in order to differentiate
various types of annotations.

It's possible to set custom colors on both the track (to be applied to all
markers) and the marker level by using the `color` property on the respective
component. A marker's custom color has precedence over track's. This color can
be set to any `Design System color token`, as well as any `rgb`, `hex` or
`CSS color`.

The `symbol` property allows you to apply an icon, emoji, single letter, glyph,
or Design System icon to either an individual marker or to an entire track. When
applied to a track, this `symbol` will be used as the default. As with the color
property, a marker's custom symbol has higher priority than track's.

When markers partially overlap one another, the order of the annotations defines
which marker is displayed on top. Timestamp-based annotations are always
displayed above timeframe-based ones. It's also possible to customize the marker
display order, by using the `priority` property. The higher the value of the
priority property, the higher precedence the marker has. The priority property
also affects the color of markers i.e. within a group, the color of the marker
with the highest priority will be applied to the group.

It's possible to assign a label to a track using the `label` property. Be aware
that labels are hidden by default. To show a track's label, the `showLabels`
property has to be applied to the `TimeseriesChart.Annotations` component.

##### Visibility

An entire track can be hidden by adding the `hidden` property to the
`TimeseriesAnnotations.Track` component. The same configuration can be applied
to a marker, by setting the `hidden` property on the
`TimeseriesAnnotations.Marker` component.

When hovering a marker (with the cursor), an annotation indicator appears over
the chart area. The indicator's visibility can be customized on either a track
or marker level by using the `indicatorsDisplay` property:

- With the `auto` option, the default behaviour is applied - indicators appear
on hover.

- The `always` option sets indicators to always be visible within the chart
area, regardless of the hovering behavior.

- The `never` option sets indicators to never be visible.

##### Custom tooltip

The Annotations supports both default and custom tooltips for annotations. This
allows creators to provide additional detailed information about specific
datapoints or events in the chart.

See Annotations Tooltip
for more

##### Custom actions

Annotations support both out-of-the-box and custom interactions. When hovering
over markers and marker groups, additional detailed information is displayed in
the annotation tooltip (out-of-the-box interaction). Similarly to the
`TimeseriesChart` series actions, the `TimeseriesChart.Annotations`component
supports custom actions which can be defined by the Creator.

#### Band chart

A time series based band chart, also known as a prediction band chart or a
confidence band chart, is a type of chart geometry that is commonly used in time
series analysis and forecasting. The chart is designed to visualize and
understand the uncertainty surrounding a predicted value based on historical
data, or fluctuations of a value in a given time period (i.e. `min` & `max`).

A median line chart (displaying the `average`) together with a band chart
(displaying `min` & `max` values) is useful for better understanding the context
around a given metric value. The band chart helps to visualize the range and/or
level of uncertainty because it helps to visualize the trend of the data and the
level of uncertainty around a given metric or trend. In forecasting usecases
comparing the current value of the data to the prediction band, it is possible
to identify whether or not the data is following the expected trend or deviating
from it.

In terms of data structure, time series charts typically display a single value
for each point in time, whereas band charts, also known as confidence interval
charts, display a range of values by plotting two lines: one for the minimum
value ('lower band', `y0`) and one for the maximum value (upper band, `y1`).

##### Basic usage

The band is defined as a subcomponent within the time series chart by using the
`TimeseriesChart.Band` sub-component. See below, for the most simple example of
a band chart.

##### Stroke and fill properties

By default, the band chart is rendered with the area between its bounds
"filled". For use cases in which this is too distracting or where one needs to
compare two bands to one another, the chart geometry also has a `strokeOnly`
property. When set to `true`, only the lines (strokes) delimitating the bounds
of the band will be visible.

##### Equal values

When the `y0` and `y1` values in the dataset are equal a line is rendered
instead of a band.

##### Gaps in the data

As the band chart is an extension of the time series chart, the same gap
policies apply to it (see above).

##### Multiple bands

Multiple bands can be rendered in the same chart and combined with other
geometries. A common use case is rendering a band chart (showing `min` & `max`)
together with a `Timeseries.Line` (showing the `average`).

#### Combination charts (multiple geometries)

Using configuration per series allows for a single series to have a different
configuration, which is more specific than the global one. In order to do so, we
can use a subcomponent for each shape (,
, and
). Each subcomponent will enable different properties
depending on the type of shape. If there is not any variant or subcomponent set
and only the data is set, the default variant will be `Line.` There are some
common configurations between shapes, which are:

- `color`: The color of the series. It will override the color palette
configuration for this specific series.

- `valueRepresentation`: It is possible to use a different value representation
than the global one only if there is no secondary unit attached to the right
axis. If the right axis is already assigned to a unit, the value
representation will roll back to `absolute`, and the override will be ignored.
This property doesn't apply to the band shape.

NoteBe aware that the series configuration managed through the subcomponents won't
be part of the shareable configuration.

##### Ordering

In a few words, the shape types (line, bars, area, band) will appear in the same
order set on the subcomponents. When a global variant is defined in the chart
configuration, it will always have lower priority (it will always be rendered
below the other shapes) than the other geometries.

##### Line

In order to display data as a line (i.e. using the line geometry) within the
chart, pass your data to a subcomponent. The
available properties for a series rendered as a line are as follows:

- `gapPolicy`: It can be either `gap`, `connect`, or `threshold`. More details
in the gap policy section.

- `pointsDisplay`: Whether to show data points always, never, or depending on a
width-based threshold amount.

##### Bar

In order to display data as a bar (i.e. using the bar geometry) within the
chart, pass your data to a subcomponent. If several
series with the same shape type and unit are added on the same
timeframe/timestamp, the data will be stacked.

##### Area

In order to display data as an area (i.e. using the area geometry) within the
chart, pass your data to a subcomponent. The
available properties for a series rendered as an area are as follows:

- ` gapPolicy`: It can be either `gap`, `connect`, or `threshold`. More details
in the gap policy section.

- `pointsDisplay`: Whether to show data points always, never, or depending on a
width-based threshold amount.

If several series with the same shape type and unit are added on the same
timeframe/timestamp, the data will be stacked.

#### Thresholds

Thresholds are used to mark meaningful ranges or values on a `TimeseriesChart`
and they add contextual information to a numerical axis. There are two variants
of thresholds:

- a specific point represented on the Y-axis and a line across.

- a range - or filled area - represented by a pill on the Y-axis and a band
across.

##### Point and Range

Both point and range can be represented by static or dynamic data sources. A
static data source has a single value representing a point or a single key-value
pair representing a fixed range. A dynamic data source has a data array
containing more than one value or various key-value pairs.

There are three different types of threshold markers:

Range filled, where the value range is defined in order to display the
threshold band. The upper and lower lines are not drawn unless the pill is
hovered.

Range stroke-only variant, where a value range is defined in order to display
the threshold band represented by upper and lower dashed lines. The upper and
lower lines become continuous lines when the pill is hovered.

Point, where only one value is required to display the threshold. It's
represented by a dashed line and when the point is hovered the line becomes a
continuous line.

##### Dynamic Point

##### Dynamic Range

##### Dynamic Range Stroke Only

There is no limit defined for the number of threshold ranges or points that can
be used in a single `TimeseriesChart`.

By default, thresholds are positioned on the left axis and with the use of the
`position` prop, we can place thresholds on the right axis or on both, as
depicted below.

##### Left Axis

##### Right Axis

##### Dual Axis

#### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application. The fallback UI occupies the full
width and height of the chart, ensuring that users are still provided with a
meaningful interface even in the presence of errors.

The `ErrorState` subcomponent offers a versatile feature that enables it to
handle both default and custom error messages. You can provide a custom message
through the `ErrorState` subcomponent, which will then override the default
error message. This flexibility allows developers to tailor error messages to
their specific needs and requirements, ensuring a more personalized and
informative user experience.

The `ErrorState` subcomponent provides the flexibility to format custom error
messages using HTML, which allows for enhanced customization and adaptability in
presenting error information. Furthermore, it is possible to incorporate the
original thrown error within your custom error message, ensuring that users
receive comprehensive and relevant information when an error occurs.

#### EmptyState

The `EmptyState` subcomponent serves as a fallback when there is no data
available to display in a chart. Its purpose is to provide a user-friendly way
of informing the user about the current situation. When there is no data, a
fallback UI is displayed occupying the full width and height of the chart, along
with a default message.

A feature of `EmptyState` is its ability to handle custom messages. It provides
the flexibility to format custom messages using HTML, which allows for enhanced
customization and adaptability in presenting error information.

#### Loading

The `loading` prop is a boolean value that can be passed to the
`TimeseriesChart` component to control its loading state. When the loading prop
is set to true, the loading indicator appears in the middle of the chart plot to
inform the user that the component is currently fetching or processing data.
When the loading prop is set to false, the component should display its regular
content.

#### Styling

The `TimeseriesChart` also accepts custom styling, which can be set using the
props `className` and/or `style` as in a regular html element.Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Size
- Variants
- Series actions
- Messages
- Gap policy
- Value representation
- Change the chart color/s
- Legend
- Truncation Mode
- Series curve
- Chart Interactions
- Shared Crosshair
- Download data as CSV
- Toolbar behavioral tracking
- Intent options
- Multiple chart configuration
- Axes
- Tooltip
- Formatter
- Annotations
- Band chart
- Combination charts (multiple geometries)
- Thresholds
- Error state
- EmptyState
- Loading
- Styling

### Props

The `TimeseriesChart` visually represents data in sequential order of time. It's
used to observe trends, patterns, and fluctuations in the data over a specific
time period.

OverviewProperties

#### TimeseriesChartProps
extends`, , , <>` |
 | Name | Type | Default | Description
 | `data?` | [] | | The series data passed to the chart
 | `height?` | | | `300px` | The height of the chart. If a number is passed, it will be treated as px.
 | `width?` | | | `100%` | Chart width. When a number is specified, it's treated as pixels,
otherwise a valid width string is expected.
 | `variant?` | | `'line'` | Variant to configure the type of chart
 | `seriesActions?` | (timeseries: , datapoint?: | ) => | | Exposed callback to display series actions for a series
 | `onMessage?` | (messages: []) => | | Messages emitted by the chart
 | `gapPolicy?` | | | The gap policy to be applied to all series of the chart
 | `pointsDisplay?` | | `'auto` | Show the datapoints always, never or based on a threshold amount.
 | `valueRepresentation?` | | | The value representation to be used, either absolute or relative
 | `loading?` | | `false` | Show the loading indicator when truly.
 | `colorPalette?` | | | `'categorical'` | Color palette that will be applied to the chart.
 | `truncationMode?` | | `'middle'` | Truncation mode to use (start, middle, end)
Applied to all the parts that truncate text.
 | `curve?` | | `'linear'` | Defines the curve shape of the series
 | `infiniteZoom?` | | `'false'` | Enables infinite zooming
 | `children?` | | |

### TimeseriesChart.Legend

To configure the legend, add `TimeseriesChart.Legend` to the time series chart.

#### TimeseriesChartLegendProps

##### Signature:
`export declare type TimeseriesChart = ;`

### TimeseriesChart.Tooltip

To configure the tooltip, add `TimeseriesChart.Tooltip` to the time series
chart.

#### TimeseriesChartTooltipProps
 |
 | Name | Type | Default | Description
 | `variant?` | | | Whether the tooltip should contain datapoints from all series for the selected timestamp, or just the closest one.
 | `seriesDisplayMode?` | | | The tooltip items display mode. When it's undefined and variant is 'shared', then set to 'single-line', if variant is 'single', then set to 'multi-line'.

### TimeseriesChart.XAxis

To configure the x-axis, add `TimeseriesChart.XAxis` to the time series chart.

#### TimeseriesChartXAxisProps
 |
 | Name | Type | Default | Description
 | `max?` | | | | | The maximum point in time for the X axis.
It can either be:
a number representing a timestamp,
an ISO8601-compliant string,
or a Date object
 | `min?` | | | | | The minimum point in time for the X axis.
It can either be:
a number representing a timestamp,
an ISO8601-compliant string,
or a Date object
 | `label?` | | | The label to display alongside the axis.

### TimeseriesChart.YAxis

To configure the y-axis, add `TimeseriesChart.YAxis` to the time series chart.

#### TimeseriesChartYAxisProps
 |
 | Name | Type | Default | Description
 | `max?` | | `'auto'` | Maximal value on the y-axis.
 | `min?` | | `'auto'` | Minimal value on the y-axis.
 | `position?` | | | The position of the Y-axis relative to the chart area.
 | `label?` | | | The label to display alongside the axis.
 | `scale?` | | | The scale of the Y axis values.
 | `formatter?` | | | | Timeseries tick formatter

### TimeseriesChart.ThresholdIndicator

`TimeseriesChart.ThresholdIndicator` provides a slot for defining annotations in
the chart.

#### TimeseriesChartThresholdIndicatorProps

##### Signature:
`export declare type TimeseriesChartThresholdIndicatorProps = ;`

### TimeseriesChart.EmptyState

`TimeseriesChart.EmptyState` provides a slot where the Empty state wrapper can
be set.

#### EmptyStateProp
 |
 | Name | Type | Default | Description
 | `children` | | |

### TimeseriesChart.ErrorState

`TimeseriesChart.ErrorState` provides a slot where the Error state wrapper can
be set.

#### ErrorStateProps
 |
 | Name | Type | Default | Description
 | `children` | | ((errorMessage: ) => .) | |

### TimeseriesChart.Select

`TimeseriesChart.Select` provides a slot that enables functionality for
selecting a specific area in the chart.

#### SelectProps
 |
 | Name | Type | Default | Description
 | `actions?` | (selectedSeries: [], selectionDomain: [, ]) => | <> | | Custom actions handler

### TimeseriesChart.Intent

`TimeseriesChart.Intent` provides a slot to set intents that will appear in the
toolbar.

#### IntentProps

##### Signature:
`export declare type IntentProps = | ;`

### TimeseriesChart.ColorRule

`TimeseriesChart.ColorRule` provides a slot to apply conditional coloring to
your chart series based on their values or names.

#### ColorRuleProps

##### Signature:
`export declare type ColorRuleProps = {
 valueAccessor?: ;
 comparator: ;
 matchValue: ;
} & ;`

### TimeseriesChart.Annotations

`TimeseriesChart.Annotations` provides a slot for defining annotations in the
chart.

#### TimeseriesChartAnnotationsProps
extends |
 | Name | Type | Default | Description
 | `visibleTracksLimit?` | | `3` | How many tracks to show by default, if there are more tracks than the specified here a scrollbar will be added.

### TimeseriesAnnotations.Track

`TimeseriesAnnotations.Track` provides a slot for defining a track in the
`TimeseriesChart.Annotations`.

#### TimeseriesAnnotationsTrackProps
extends |
 | Name | Type | Default | Description
 | `indicatorsDisplay?` | | `'auto'` | Defines how to show the annotations indicators: always, never, or on hover (auto) at Track level

### TimeseriesAnnotations.Marker

`TimeseriesAnnotations.Marker` provides a slot for defining a marker in the
`TimeseriesChart.Annotations`.

#### TimeseriesAnnotationsMarkerProps
extends`, ` |
 | Name | Type | Default | Description
 | `indicatorsDisplay?` | | `'auto'` | Defines how to show the marker indicator on top of the chart: always, never, or on hover (auto)

### TimeseriesAnnotations.Tooltip

`TimeseriesAnnotations.Tooltip` provides a slot for defining a custom tooltip
for the annotations.

#### AnnotationsTooltipProps
 |
 | Name | Type | Default | Description
 | `hidden?` | | `false` | Defines whether tooltip show be hidden or not
 | `children?` | | | The ChoroplethLayer tooltip handler template

### TimeseriesChart.Toolbar

`TimeseriesChart.Toolbar` provides a slot to customize the toolbar of the chart.

#### TimeseriesChartToolbarSlotProps

##### Signature:
`export declare type TimeseriesChartToolbarSlotProps = ;`

### TimeseriesChart.DownloadCSV

`TimeseriesChart.DownloadCSV` provides a slot to toggle the download CSV of the
chart.

Prop Table did not receive data

### TimeseriesChart.Zoom

`TimeseriesChart.Zoom` provides a slot to toggle the zoom of the chart.

#### TimeseriesZoomSlotProps
 |
 | Name | Type | Default | Description
 | `disabled?` | | | Whether the zoom is disabled.

### TimeseriesChart.Pan

`TimeseriesChart.Pan` provides a slot to toggle the pan of the chart.

#### TimeseriesPanSlotProps
 |
 | Name | Type | Default | Description
 | `disabled?` | | | Whether the pan is disabled.

### TimeseriesChart.Line

`TimeseriesChart.Line` provides a slot for defining a `Line`.

#### TimeseriesChartLineProps
extends |
 | Name | Type | Default | Description
 | `data` | | | The series data passed to the line
 | `gapPolicy?` | | | Defines how gaps are handled (connect vs. gap)
 | `pointsDisplay?` | | | Whether to show data points always, never, or depending on a width-based threshold amount

### TimeseriesChart.Area

`TimeseriesChart.Area` provides a slot for defining a `Area`.

#### TimeseriesChartAreaProps
extends |
 | Name | Type | Default | Description
 | `data` | | | The series data passed to the area
 | `gapPolicy?` | | | Defines how gaps are handled (connect vs. gap)
 | `pointsDisplay?` | | | Whether to show data points always, never, or depending on a width-based threshold amount

### TimeseriesChart.Bar

`TimeseriesChart.Bar` provides a slot for defining a `Bar`.

#### TimeseriesChartBarProps
extends |
 | Name | Type | Default | Description
 | `data` | | | The series data passed to the bar

### TimeseriesChart.Band

`TimeseriesChart.Band` provides a slot for defining a `Band`.

#### TimeseriesChartBandProps
 |
 | Name | Type | Default | Description
 | `data` | | | The series data passed to the band
 | `strokeOnly?` | | | Whether only the band chart edges strokes are visible. Default value: false
 | `color?` | | | The unique color picked for this time series representation in HEX, RGB, Color Token or HSL.
 | `seriesAction?` | (series: ) => | | Exposed callback to display series action for a series
 | `gapPolicy?` | | | Still have questions?Find answers in the Dynatrace Community
- TimeseriesChart.Legend
- TimeseriesChart.Tooltip
- TimeseriesChart.XAxis
- TimeseriesChart.YAxis
- TimeseriesChart.ThresholdIndicator
- TimeseriesChart.EmptyState
- TimeseriesChart.ErrorState
- TimeseriesChart.Select
- TimeseriesChart.Intent
- TimeseriesChart.ColorRule
- TimeseriesChart.Annotations
- TimeseriesAnnotations.Track
- TimeseriesAnnotations.Marker
- TimeseriesAnnotations.Tooltip
- TimeseriesChart.Toolbar
- TimeseriesChart.DownloadCSV
- TimeseriesChart.Zoom
- TimeseriesChart.Pan
- TimeseriesChart.Line
- TimeseriesChart.Area
- TimeseriesChart.Bar
- TimeseriesChart.Band

---

## TreeMap

`/design/data-visualizations/charts/TreeMap/`

The `TreeMap` visualizes the distribution of hierarchical data. It uses nested
rectangles of different sizes and colors to show how much each category or
subcategory contributes to the whole data set.

OverviewProperties

### Import

`tsx
import { TreeMap } from '@dynatrace/strato-components/charts';
`

### Use cases

The `TreeMap` component requires a structured tree object containing
hierarchical data, with an optional `unit` specified as a string. This data
should support two levels of categories: `ClusterNode` and `LeafNode`.

##### Structure

Tree Object: The root of the dataset, containing the overall structure.

- value: A numerical value representing the total value at the root level. - nodes:
An array of cluster nodes. - name: An optional string representing the name of the
root node.

Cluster Nodes: Each parent node represents a category and includes:

- name: A string representing the name of the category. - value: A numerical value
representing the total value of the category. - nodes: An array of leaf nodes.

Leaf Nodes: Each child node represents a sub-category and includes:

- name: A string representing the name of the sub-category. - value: A number representing
the value of the sub-category.

The displayed data can be adjusted by setting limits. These limits can be
defined using the `min` and `max` properties. Setting those limits is
particularly useful when displaying numerical values in the legend
`nameAccessor='value'`

The min property can use the `data-min` value, and the max property can use the
`data-max` value. These special values provide detailed control over the
boundaries.

By default, the data-min value is used for the min property, and the data-max
value is used for the max property. These settings automatically determine the
minimum and maximum values for the nodes in the chart.

Additionally, the min and max properties can also accept numeric values. This
allows you to manually set specific numerical limits for the data display,
giving you even more control over the range of data shown in the chart.

`tsx
{ tree: { name: '', value: 0, nodes: [ { name: 'India', value: 117200000, nodes: [ { name: 'Delhi', value: 27000000, } ] } ] }}
`

Learn more about the data format here.

#### Size

By default, the chart will use all the available container size up to a maximum
height of 300 pixels. This maximum height can be changed by providing a value in
the `height` prop of the `TreeMap` instance. If a number is passed to this prop
without any unit specified, it will be treated as `px`.

#### Series actions

A series action is a creator-defined interaction with a given node in the chart.
The default interaction included is copying a node name. Inspecting the
underlying data of said node is an example of a basic creator-defined action. In
order to enable chart interactions, the `ChartSeriesAction` subcomponent needs
to be appended within the `TreeMap`. More subcomponents can be added within this
component, for instance `ChartSeriesAction.Item`, where you can provide a custom
action that will appear in the legend menu. That action can execute any custom
logic in its `onSelect` callback or get disabled via a `disabled` prop.
`Intents` could be added as part of the series action as well with
`ChartSeriesAction.Intent`.

#### Legend

The purpose of the legend is to provide additional identifying information for
the chart, without needing to interact with the legend directly.

##### Visibility

The legend of the `TreeMap` is shown by default. In order to hide or show the
legend, you need to set the value of `legend.hidden` on the subcomponent.

##### Position

By default, the position of the legend of the `TreeMap` is set automatically.
This option prioritizes the legend placement to the right of the chart area.
When the chart width is reduced, the legend is repositioned to the area beneath
the chart. It is also possible to explicitly set the chart's legend position to
right or bottom with the `position` prop.

##### Legend ratio

By default, the legend occupies `25%` of the container width, in the case where
the legend is positioned on the right and `25%` of the container height if the
legend position is on the bottom.

It is possible to override the default legend ratio by setting a custom
percentage value for the ratio prop. The expected value is in the range of
`5-80`. Values out of expected ranges will roll back to the default legend
ratio.

#### Formatter

The `TreeMap` component expects a structured tree object with a value and an
optional unit, by default this optional unit will be appended to the specified
value, if it is included. There are two other options in the formatter that
allow for greater customization. The first option enables you to prepend the
unit to the value, while the second option enables you to ignore the original
unit and append a custom string instead. Additionally, there is a custom
formatter option available to allow you to change the input unit to one of your
choice, e.g.: if the input unit is `bits`, you are able to switch and display
the unit as `bytes`, correctly formatted. The formatted value is applied in the
tooltip. The use cases below outline each of these scenarios.

#### Toolbar

The toolbar is where you can download data and use added Intents. It is
displayed by default, but to customize it, you can add the `TreeMap.Toolbar`
subcomponent, which supports the optional `hidden` and `placement` props.

##### Behavioral tracking

The `TreeMap.Toolbar` subcomponent supports behavioral tracking attributes that
are spread onto the toolbar root element. This allows tracking of toolbar
interactions such as menu opens, mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `TreeMap.Toolbar` to attach tracking
metadata. See `BehaviorTrackingProps` for the full list of supported attributes.

#### Download data as CSV

The `TreeMap` component supports download data in CSV format using a toolbar
button. To enable this feature, a `TreeMap.DownloadCSV` subcomponent must be
provided to the `TreeMap` component. On click of the download button, raw data
will be downloaded as a CSV file.

The CSV file contains the following columns:

- `name` - the name of the node

- `value` - the value of the node

- `parent` - the parent of the node

It's also possible to programmatically trigger the download of the CSV file by
calling the `downloadData` method on the `TreeMap` instance reference.

#### Intent options

The `TreeMap` supports intent options in the toolbar. The intents appear in the
toolbar's dropdown menu, allowing users to perform actions such as sharing a
chart or viewing data in another application.

When a single intent is configured and no download button is shown, the intent
appears directly in the toolbar. When multiple intents are configured, or when
both an intent and a download button are present, they are grouped under a
More options submenu.

To add intent options to a `TreeMap`, use the `TreeMap.Intent` subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in TreeMap:

#### Label Display

The `TreeMap` component offers a `labelsDisplay` prop to control how labels are
presented.

When `labelsDisplay` is set to `cluster`, labels will appear above each group of
nodes, indicating the name of the parent cluster. When `labelDisplay` is set to
`nodes`, labels will be displayed within each node, showing the name of the
individual child node.

These options can be combined by setting the `labelDisplay` prop to `all`. In
this mode, both parent cluster names and individual child node names will be
displayed simultaneously.

#### Coloring

The `TreeMap` component provides a set of predefined color palettes that can be
used out of the box to provide more appealing visualisations. See
Charts Colors for more info.

##### Color Rules

The `TreeMap` component supports conditional coloring based on custom rules
using the `TreeMap.ColorRule` slot. Color rules allow you to apply specific
colors to nodes based on their properties, such as value comparisons or string
matching.

Each `TreeMap.ColorRule` accepts the following properties:

- `comparator`: The comparison operator (e.g., 'greater-than', 'equals',
'starts-with', 'contains').

- `matchValue`: The value to compare against.

- `valueAccessor`: Optional, specifies which property of the node to evaluate.
When omitted, the default target depends on the chart's `nameAccessor` prop:
if `nameAccessor="value"` the rule evaluates `node.value`; otherwise it
evaluates `node.name`. For explicit numerical comparisons on node values,
always set `valueAccessor="value"`.

- `color` and `colorPalette` are mutually exclusive.

- `color`: A specific color string (e.g., 'red', '#ff0000').

- `colorPalette`: A predefined color palette name.

Rules are evaluated in the order they are defined, and the last matching rule
applies.

Slot Usage Examples:

`tsx
TreeMap data={data} colorPalette="fireplace"> {/* Numerical comparison with single color */} TreeMap.ColorRule comparator="greater-than" matchValue={100} color="red" /> {/* String matching with color palette */} TreeMap.ColorRule comparator="starts-with" matchValue="Error" colorPalette="log-level" /> {/* Custom property access */} TreeMap.ColorRule comparator="greater-than" matchValue={50} color="blue" valueAccessor="temperature" />TreeMap>
`

#### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application. The fallback UI occupies the full
width and height of the chart, ensuring that users are still provided with a
meaningful interface even in the presence of errors.

The `ErrorState` subcomponent offers a versatile feature that enables it to
handle both default and custom error messages. You can provide a custom message
through the `ErrorState` subcomponent, which will then override the default
error message. This flexibility allows developers to tailor error messages to
their specific needs and requirements, ensuring a more personalized and
informative user experience.

The `ErrorState` subcomponent provides the flexibility to format custom error
messages using HTML, which allows for enhanced customization and adaptability in
presenting error information. Furthermore, it is possible to incorporate the
original thrown error within your custom error message, ensuring that users
receive comprehensive and relevant information when an error occurs.

#### EmptyState

The `EmptyState` subcomponent serves as a fallback when there is no data
available to display in a chart. Its purpose is to provide a user-friendly way
of informing the user about the current situation. When there is no data, a
fallback UI is displayed occupying the full width and height of the chart, along
with a default message.

A feature of `EmptyState` is its ability to handle custom messages. It provides
the flexibility to format custom messages using HTML, which allows for enhanced
customization and adaptability in presenting error information.

#### Loading

The `loading` prop is a boolean value that can be passed to the `TreeMap`
component to control its loading state. When the loading prop is set to true,
the loading indicator appears in the middle of the chart plot to inform the user
that the component is currently fetching or processing data. When the loading
prop is set to false, the component should display its regular content.

#### Styling

The `TreeMap` also accepts custom styling, which could be set using the props
`className` and/or `style`, as a regular html element

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Size
- Series actions
- Legend
- Formatter
- Toolbar
- Download data as CSV
- Intent options
- Label Display
- Coloring
- Error state
- EmptyState
- Loading
- Styling

### Props

The `TreeMap` visualizes the distribution of hierarchical data. It uses nested
rectangles of different sizes and colors to show how much each category or
subcategory contributes to the whole data set.

OverviewProperties

#### TreeMapProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `data` | | | The tree map data to display.
 | `width?` | | | `100%` | Optional width of the chart.
 | `height?` | | | `400` | Optional height of the chart.
 | `colorPalette?` | | | [] | `'categorical'` | Color palette to use for coloring the tree nodes. Nodes of height 1
get a color assigned from the palette.
 | `formatter?` | | | | Custom value formatter for the chart.
 | `unit?` | | | | Optional unit for value formatting. Takes priority over data.unit
 | `truncationMode?` | | `'middle'` | The text truncation mode used for the chart legend.
 | `loading?` | | `false` | Show the loading indicator.
 | `labelsDisplay?` | | `'none'` | Show/hide label on TreeMap nodes and clusters
 | `seriesActions?` | (node: ) => | | Exposed callback to display series actions for a node
 | `nameAccessor?` | | `undefined` | Data accessor on leaf nodes by which legend can be defined
 | `min?` | | | | The min value configuration to display
 | `max?` | | | | The max value configuration to display

### TreeMap.Legend

To configure the legend, add `TreeMap.Legend` to the TreeMap chart.

#### TreemapChartLegendConfig

##### Signature:
`export declare type TreemapChartLegendConfig = ;`

### TreeMap.Tooltip

To configure the tooltip, add `TreeMap.Tooltip` to the TreeMap chart.

### TreeMap.EmptyState

`TreeMap.EmptyState` provides a slot where the Empty state wrapper can be set.

#### EmptyStateProp
 |
 | Name | Type | Default | Description
 | `children` | | |

### TreeMap.ErrorStateSlotProps

`TreeMap.ErrorState` provides a slot where the Error state wrapper can be set.

#### ErrorStateProps
 |
 | Name | Type | Default | Description
 | `children` | | ((errorMessage: ) => .) | |

### TreeMap.Toolbar

`TreeMap.Toolbar` is a slot to hide or to configure the toolbar.

#### CompactToolbarProps

##### Signature:
`export declare type CompactToolbarProps = & {
 hidden?: ;
 placement?: [];
};`Still have questions?Find answers in the Dynatrace Community
- TreeMap.Legend
- TreeMap.Tooltip
- TreeMap.EmptyState
- TreeMap.ErrorStateSlotProps
- TreeMap.Toolbar

---

## XYChart

`/design/data-visualizations/charts/XYChart/`

The `XYChart` encompasses various types of charts that utilize both x-axis and
y-axis for data representation, designed to visually display and analyze data
that involve two numerical variables.

OverviewProperties

### Import

`tsx
import { XYChart } from '@dynatrace/strato-components/charts';
`

### Use cases

The `XYChart` encompasses various types of charts that utilize both X-axis and
Y-axis for data representation, designed to visually display and analyze data
that involve two numerical variables. The following variants are currently
supported: RectSeries,
DotSeries,
LineSeries and
BarSeries.

#### Data

The data provided to the `XYChart` component via the `data` property will be
used in combination with the accessors of each series.

The series subcomponent has an optional `data` property that can be used to
provide specific data for that series.

Learn more about the data format here.

#### Data accessors

Accessors specify how to retrieve data from your data structure. Accessor
strings that contain dots allow you to retrieve nested data. If the actual
property key contains a dot, you can escape an accessor by enclosing the string
in square brackets.

#### Truncation mode

The purpose of truncation is to gracefully handle extra long labels within data
visualization components. By changing the value of the `truncationMode`
property, you have control over where truncation is applied within charts. By
default, the truncation is applied to the middle of labels with the use of an
ellipsis. Truncation can, however, be changed to instead be applied at the start
or end of data visualization component labels.

#### Coloring

The `XYChart` provides several ways to customize the appearance of your data:

- Predefined Color Palettes: Use built-in color schemes

- Custom Color Palettes: Define your own color schemes

- Color Rules: Apply conditional coloring based on data values.

##### Predefined Color Palettes

The `XYChart`'s `colorPalette` property supports predefined color palettes,
which are useful for consistent theming across your application. See
coloring for more details.

##### Custom Color Palettes

Custom color palettes can be useful when you need specific colors for your data,
especially for categorical data of type string.

##### Using Color Rules

For advanced coloring scenarios, you can use the `XYChart.ColorRule` slot to
apply conditional coloring based on data values. Color Rule slots behave
differently depending on the series type:

- RectSeries (heatmaps): Applies solid colors to individual tiles that match
the rule

- DotSeries, LineSeries, BarSeries: Applies colors at the series level when
any datapoint matches

This is particularly useful for highlighting specific data points or ranges that
meet certain criteria, such as error states, thresholds, or specific categories.

###### Supported comparators

Color rules support various comparison operators that can be used to match data
values:

- Numerical comparisons: `'less-than'`, `'less-or-equal'`, `'greater-than'`,
`'greater-or-equal'`

- Equality comparisons: `'equals'`, `'not-equals'`

- String comparisons: `'starts-with'`, `'not-starts-with'`, `'ends-with'`,
`'not-ends-with'`, `'contains'`, `'not-contains'`, `'matches-phrase'`,
`'not-matches-phrase'`

You can apply rules to different data properties using the `valueAccessor` prop,
which defaults to the y-value if not specified. When multiple rules match a data
point, the last rule in the array takes precedence.

For more details about available comparators and options, see the
Color Rules
section.

##### Custom Color Ranges

Custom color ranges can be useful to apply gradient-based coloring to data of
type number.

#### Size

By default, the chart will use all the available space up to a maximum height of
300 pixels and a width of 100% of the container. This maximum height and width
can be changed by providing a value in the `height` and `width` properties of
the `XYChart`. Both accept a number (treated as pixels) or a CSS string (e.g.,
`"500px"`, `"60%"`).

#### Axes

To display a series in the plot, it is necessary to include both `XYChart.XAxis`
and `XYChart.YAxis` subcomponents, which will require an `id` property that
matches the `xAxisId` and `yAxisId` used in a given series.

You will also need to define the `type` property, used to determine the axis
scale type, which can be `numerical`, `log`, `time` or `categorical`, as well as
the `position` to indicate where the axis should be placed, which can be
`bottom`, `top`, `left` or `right`. You can add as many axes as needed to the
chart but only the first axis of each position will be visually displayed.

##### Mirrored Axes

There is an additional position option called `both` for displaying a mirrored
axis for either the `XYChart.XAxis` or the `XYChart.YAxis`.

##### Axis label

The `label` property can be used to include a text label for a given axis. If
set, it will also be shown in the tooltip identifying the corresponding data.

##### Reversed Axis

The `reversed` property inverts the scale on the chosen axis.

##### Axis visibility

The `hidden` property can be used to visually hide the axis.

##### Axis layout and size

The `tickLabelLayout` property gives you the option to choose between a
`horizontal` (default) or `vertical` layout for the axis tick values.

The `tickLabelMaxSize` TBD.

##### Axis min and max

The `min` and `max` properties define the axis boundaries. By default, the
`auto` setting is applied to both `min` and `max` properties, which
automatically calculates the axis scale's minimum and maximum values from the
chart data, akin to `data-min` and `data-max`, and establishes the baseline of
the Y-axis at zero. A custom number or date can also be provided to set custom
axis boundaries.

##### Axis unit and formatter

With the `unit` property you can provide a unit that will be displayed along the
data in the chart. The `formatter` will allow you to format data of type date or
number.

##### Gap policy

Gaps in data refer to missing or unrepresented values between existing data
points. In a dataset exclusively with timestamps, no continuity can be
determined and therefore there are always “gaps” between data points regardless
of the resolution of the dataset. In a timeframe dataset however, gaps are
considered when the end timestamp of the previous data point is earlier than the
start timestamp of the next data point, meaning there is a timespan between the
end of a previous data point and the next one with no given value. This concept
can also be applied for any type of continuous numerical domain (not only time).

The XYChart axes provide the `gapPolicy` prop to configure how gaps are
visualized in a chart. There are three `gapPolicy` options available: `gap`,
`connect`, and `threshold`.

- The `gap` option displays gaps on the chart as is (e.g. breaks along a line).
This option helps to see the absence of data during a period of time or number
unit.

- The `connect` option connects consecutive data points irrespective of the gap
using linear interpolation.

- The `threshold` option provides a mechanism to configure thresholds of a
certain time or number (e.g. 30 seconds, 5 minutes, 1 day, 3 months, etc. or
positive integers). When the gap between sequential data points in the dataset
is less than or equal to the threshold, then the data points will be
connected.

Note: The `gapPolicy` prop is only supported in line chart variants. The other
variants do not support a gap policy and do not react to the property
configuration for this axis.

##### Multiple axes

When using any `XYChart` up to four different axes can be visually displayed at
the same time.

#### Legend

The purpose of the legend is to provide additional identifying information for
the chart, without needing to interact with the legend directly. If there are
multiple series in the chart, only the first series will be reflected on the
legend.

##### Visibility

The legend of the `XYChart` will be displayed by default, but can be optionally
hidden by setting the `hidden` property to true on the `XYChart.Legend`
subcomponent.

##### Position

By default, the position of the legend of the `XYChart` is set automatically to
the right of the chart area. When the chart width is reduced, the legend is
repositioned to the area beneath the chart. It is also possible to explicitly
set the chart's legend position to right or bottom with the `position` prop.

##### Legend ratio

By default, the legend occupies `25%` of the container width, in the case where
the legend is positioned on the right and `25%` of the container height if the
legend position is on the bottom.

It is possible to override the default legend ratio by setting a custom
percentage value for the `ratio` prop. The expected value is in the range of
`5-80`. Values out of expected ranges will roll back to the default legend
ratio.

#### Empty state

The EmptyState subcomponent serves as a fallback when there is no data available
to display in a chart. Its purpose is to provide a user-friendly way of
informing the user about the current situation. When there is no data, a
fallback UI is displayed occupying the full width and height of the chart, along
with a default message.

#### Error state

The `ErrorState` subcomponent is responsible for handling errors in a graceful
manner, ultimately improving the overall user experience. Its primary function
is to catch any errors that may occur with the data and display a fallback UI
instead of crashing the entire application. The fallback UI occupies the full
width and height of the chart, ensuring that users are still provided with a
meaningful interface even in the presence of errors.

#### Loading state

The `loading` property is a boolean value that can be passed to the `XYChart`
component to control its loading state. When the loading prop is set to true,
the loading indicator appears in the middle of the chart plot to inform the user
that the component is currently fetching or processing data. When the loading
prop is set to false, the component should display its regular content.

#### Chart Interactions

The `XYChart` provides various interactions (e.g. zoom-x, zoom in, zoom out, and
pan) that are enabled all by default. See
chart interactions for more details.

##### Zoom and Pan

Every X-axis can opt-in or out of having the zoom and pan enabled. This also
applies regardless of the position (top, bottom). To disable these interactions,
`disableZoom` and `disablePan` can be specified as props for the `XAxis`
subcomponent.

As soon as there's one X-axis with zoom, the controls and interactions are
enabled. When performing any zoom interaction, it affects to all the X-axis
with also zoom enabled.

Categorical axis are excluded and will never be zoomed or panned.

##### onZoomChange

You can subscribe to changes on interactions made on X-axis in the `XYChart` by
specifying a callback `onZoomChange` for the `XAxis` subcomponent. See
chart interactions to know all possibilities.

##### Infinite Zoom

The infinite zoom provides a way to zoom and pan without limits. This way, the
boundaries set by the current domain will be bypassed.

If the customer enables the feature and exceeds the data domain, the chart won't
show any data unless the consumer provides new ones for the new domain.

This feature can be enabled by defining `infiniteZoom` prop for the desired
`XAxis` subcomponent.

##### Initial and Current zoom

A chart's domain is determined by its data, and each axis can define its scale
boundaries by a `min` and `max` property as explained
here. However, there's a way to set the
`initialZoom` (min, max) of the chart by setting this property on the desired
`XAxis` subcomponent. This will cause the chart to display plot information at
this initial specified domain, no matter the dataset used. There's another
property called `currentZoom` (min, max) that can also be combined with the
`initialZoom` to perform other more advanced actions, like synchronized zoom
between Charts.

The priority in which these properties are being considered for plotting the
information on the chart is the following:

- `currentZoom` (Highest priority)

- `initialZoom`

- Custom min/max on axis

- Domain derived from data (Lowest priority)

#### Toolbar

The toolbar is one of the ways to visually interact with the chart. In the
`XYChart`, it's displayed by default, but in order to customize it, a
`XYChart.Toolbar` subcomponent must be added. This subcomponent supports
`hidden`, `draggable`, `placement` and `collapsed` props.

##### Behavioral tracking

The `XYChart.Toolbar` subcomponent supports behavioral tracking attributes that
are spread onto the toolbar root element. This allows tracking of toolbar
interactions such as menu opens, zoom/pan mode changes, and download actions.

Pass any `data-dt-*` attributes directly on `XYChart.Toolbar` to attach tracking
metadata. See `BehaviorTrackingProps` for the full list of supported attributes.

#### Download data as CSV

The `XYChart` component supports download data in CSV format using a toolbar
button; this is enabled by default in the toolbar.

Each series that derives from `XYChart` have their own accessors. There are
accessors with the same names and accessors exclusive to a variant. When
downloading the data in a CSV, the columns will be the `series` followed by all
the accessors of all series variants, even if they are not included in the chart
itself.

The values of accessors in series that are not used in are null.

The accessors and their meanings are:

- `series` - the type and number of the series.

- `x0` - the value corresponding to the data from the x0 accessor.

- `x1` - the value corresponding to the data from the x1 accessor.

- `y0` - the value corresponding to the data from the y0 accessor.

- `y1` - the value corresponding to the data from the y1 accessor.

- `value` - `Rect exclusive` - the value corresponding to the data from the
valueAccessor.

It's also possible to programmatically trigger the download of the CSV file via
the `downloadData` function in the `XYChartRef`.

#### Intent options

The `XYChart` supports intent options in the toolbar. The intents appear in the
toolbar's dropdown menu, allowing users to perform actions such as sharing a
chart or viewing data in another application. When a single intent is configured
and no download button is shown, the intent appears directly in the toolbar.
When multiple intents are configured, or when both an intent and a download
button are present, they are grouped under a More options submenu. To add
intent options to a `XYChart`, use the `XYChart.Intent` subcomponent:

##### Intent properties

- `payload`: An object containing the data to be passed to the target app. The
structure depends on the target application's requirements.

- `options`: Configuration options for the intent.

- `keyProperties`: Array of properties that should be included as keys in the
intent.

- `recommendedAppId`: Suggested target application ID.

- `recommendedIntentId`: Suggested intent ID.

- `responseProperties`: Array of properties to be included in the response.

- `icon`: Optional custom icon to be displayed next to the intent option.

- `onResponse`: Optional callback function that is called when a response is
received from the target app.

##### Examples

The following examples demonstrate different intent options in XYChart:

#### Styling

The `XYChart` also accepts custom styling, which can be set using the properties
`className` and `style` as in a regular html element.

#### Annotations

Annotations are used to visualize specific events or contextual notes on the
`XYChart` in the form of markers placed in time-based or numerical-based tracks.

The marker represents an annotation at a certain point. They can be either a
value (a certain time or number) or a range (from-to object), depending on the
data provided to the Annotation. Annotations within the same
timestamp/timeframe/number are grouped together under a single marker that
displays the number of grouped annotations. Markers can be displayed on a single
or multiple tracks. When there are more than three tracks, an overflow scroll is
applied.

##### Add annotations to the chart

In order to visualize annotation data inside the `XYChart`, a
`XYChart.Annotations` component should be initialized. This component should
have at least one track, that contains a marker component per annotation data
point.

The data provided to the `XYChart.Annotations` component via the `data` property
is combined with the defined accessors to generate the corresponding tracks and
markers. Also a mandatory `xAxisId` is required to match with the corresponding
`XYChart.XAxis`, which can be either the bottom or the top one.

The `XYChartAnnotations.Track` should have a unique track ID (`trackIdAccessor`)
that will be used to match all the markers that belong to that specific track.
Additional optional parameters include: `labelAccessor`, `colorAccessor`,
`symbol`, `indicatorDisplay` and `hidden`.

An annotation data point `XYChartAnnotations.Marker` should have a unique track
ID (`trackByAccessor`) that will be used to match the track it belongs.
Additional parameters include some which are mandatory `startAccessor` and
`endAccessor`, and an optional `symbol`, `titleAccessor`, `descriptionAccessor`,
`colorAccessor` and `priority`, which will be displayed in the tooltip.

##### Marker content

When the `symbol` is provided, it will become the marker content by default.
When not, the data obtained through `titleAccessor` will be shown as marker
content.

In case the content of the marker is bigger than the size of the marker, it will
expand to fit all the content inside, decoupling from the original scale. In
these particular cases, it is encouraged to use the indicators, which will
represent the real size of the bin.

##### Visual customization

Tracks and markers support visual customization in order to differentiate
various types of annotations.

It's possible to set custom colors on both the track (to be applied to all
markers) and the marker level by using the data obtained through `colorAccessor`
property on the respective component. A marker's custom color has precedence
over track's. This color can be set to any `Design System color token`, as well
as any `rgb`, `hex` or `CSS color`.

The `symbol` property allows you to apply an icon, emoji, single letter, glyph,
or Design System icon to either an individual marker or to an entire track. When
applied to a track, this `symbol` will be used as the default.

When markers partially overlap one another, the order of the annotations defines
which marker is displayed on top. Value annotations are always displayed above
Range-based ones. It's also possible to customize the marker display order, by
using the `priority` property. The higher the value of the `priority` property,
the higher precedence the marker has. The `priority` property also affects the
color of markers i.e. within a group, the color of the marker with the highest
priority will be applied to the group.

It's possible to assign a label to a track using the data obtained through
`labelAccessor` property. Be aware that labels are hidden by default. To show a
track's label, the `showLabels` property has to be applied to the
`XYChart.Annotations` component.

##### Visibility

An entire track can be hidden by adding the `hidden` property to the
`XYChartAnnotations.Track` component. The same configuration can be applied to a
marker, by setting the `hidden` property on the `XYChartAnnotations.Marker`
component.

When hovering a marker (with the cursor), an annotation indicator appears over
the chart area. The indicator's visibility can be customized on either a track
or marker level by using the `indicatorsDisplay` property:

- With the `auto` option, the default behaviour is applied - indicators appear
on hover.

- The `always` option sets indicators to always be visible within the chart
area, regardless of the hovering behavior.

- The `never` option sets indicators to never be visible.

##### Custom tooltip

The Annotations supports both default and custom tooltips for annotations. This
allows creators to provide additional detailed information about specific
datapoints or events in the chart.

See Annotations Tooltip
for more

#### Thresholds

Thresholds are used to mark meaningful ranges or values, and they can add
contextual information to axes of type numerical (log and linear) and time.

Thresholds may represent either a single point or a range, and can be defined as
static or dynamic. In order to link the threshold to a specific axis, a valid
`yAxisId` property must be set, as well as an additional `xAxisId` property if
the threshold is of type dynamic.

Customization of thresholds is possible through additional properties such as
`color`, `label` and `strokeOnly` (only for ranges). The `label` property can be
used to display a label for the threshold, which will be shown in the tooltip
when hovering over the threshold. The `color` property allows you to set a
custom color for the threshold line, while the `strokeOnly` property will modify
the display of the range threshold to show only the stroke without filling the
area.

##### Point and Range

Both point and range thresholds can be represented by static or dynamic data
sources. A static data source has a single value representing a point or a
single key-value pair representing a fixed range. A dynamic data source has a
data array containing more than one value or various key-value pairs.

##### Dynamic Thresholds

#### Shared Crosshair

The shared crosshair feature allows you to synchronize the crosshair position
across multiple `XYChart` or `Timeseries` instances. This is especially useful
for comparing time-based data points across different charts.

To enable crosshair synchronization, wrap the charts you want to synchronize
with the `SynchronizationProvider` component.

Important notes for XYChart:

- x-axis Only: The shared crosshair synchronization only works for the X
axis. y-axis are not supported.

- Supported Axis: The shared crosshair will only synchronize on visible
time axes. Numerical or categorical axes are not supported for crosshair
synchronization.

- Axis Priority: If both a bottom and a top time axis are present and
visible, the bottom axis takes priority for synchronization.

- Hidden Axes: Axes marked as `hidden` will not trigger or participate in
crosshair synchronization, even if they are of type `time`.

#### Custom Tooltip

The XYChart component supports custom tooltips via the `XYChart.Tooltip`
subcomponent. This allows you to fully control the content and layout of
tooltips for different series types.

Wrap your custom rendering logic in `XYChart.Tooltip` and use the provided
payload to determine which series is being hovered. You can return any JSX,
`null` to hide the tooltip for a specific series, or `undefined` to fall back to
the default tooltip. You can also pass `hidden` to `XYChart.Tooltip` to suppress
the tooltip entirely without a render function.

#### Value representation

By default, values within a chart are displayed as is - with their absolute
value (e.g. 3.14 kB). However, for numerical axes this can be changed so that
instead of absolute values, relative values are used. The property
`valueRepresentation` can be set to `relative` in a numerical axis to show all
data related to that axis as relative.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Data
- Data accessors
- Truncation mode
- Coloring
- Size
- Axes
- Legend
- Empty state
- Error state
- Loading state
- Chart Interactions
- Toolbar
- Download data as CSV
- Intent options
- Styling
- Annotations
- Thresholds
- Shared Crosshair
- Custom Tooltip
- Value representation

### Props

The `XYChart` encompasses various types of charts that utilize both x-axis and
y-axis for data representation, designed to visually display and analyze data
that involve two numerical variables.

OverviewProperties

#### XYChartProps
extends`, , ` |
 | Name | Type | Default | Description
 | `data` | [] | | Data object for the xy chart.
 | `height?` | | | `300px` | Chart height. When a number is specified, it's treated as pixels,
otherwise a valid height string is expected.
 | `width?` | | | `100%` | Chart width. When a number is specified, it's treated as pixels,
otherwise a valid width string is expected.
 | `colorPalette?` | | `'blue'` | Color palette for the xy chart.
 | `loading?` | | `false` | Show the loading indicator when truthy.
 | `truncationMode?` | | `'middle'` | Truncation mode to be used as start, middle or end, and applied to all the parts that truncate text.
 | `__downloadDataCallback?` | () => | | Callback invoked when a download is triggered. Receives the CSV string
so the caller can drive the actual download (e.g. for migration purposes).
When provided, the default browser download is skipped.

#### XYChart.XAxis

To configure the x-axis, add `XYChart.XAxis` to the xy chart.

#### XYChartXAxisProps

##### Signature:
`export declare type XYChartXAxisProps = & {
 /**
 * Whether the tick labels are displayed in a or layout.
 * @defaultValue
 */
 tickLabelLayout?: ;
 /** The position for the xy chart x-axis */
 position: ;
 /** If true, the zoom interaction will be disabled
 * @defaultValue false
 */
 disableZoom?: ;
 /** If true, the pan interaction will be disabled
 * @defaultValue false
 */
 disablePan?: ;
 /** Sets the new zoom and pan domain boundaries, overwriting the ones that come from the data */
 initialZoom?: [, ] | [, ];
 /** Sets the domain of the axis to start at the specified values */
 currentZoom?: [, ] | [, ];
 /** If true, the chart will be able to zoom and pan outside the set boundaries
 * @defaultValue false
 */
 infiniteZoom?: ;
 /** Handler triggered when there is a change on the time domain caused by a zoom action */
 onZoomChange?: ;
};`

#### XYChart.YAxis

To configure the y-axis, add `XYChart.YAxis` to the xy chart.

#### XYChartYAxisProps

##### Signature:
`export declare type XYChartYAxisProps = & {
 position: ;
};`

#### XYChart.Legend

To configure the legend, add `XYChart.Legend` to the xy chart.

#### XYChartChartLegendProps

##### Signature:
`export declare type XYChartChart = ;`

#### XYChart.Toolbar

To customise the toolbar, add `XYChart.Toolbar` to the xy chart.

#### XYChartToolbarProps

##### Signature:
`export declare type XYChartToolbarProps = & {
 /** Decides if the toolbar is visible or hidden
 * @defaultValue false
 */
 hidden?: ;
};`

#### XYChart.EmptyState

`XYChart.EmptyState` provides a slot where the Empty state wrapper can be set.

#### EmptyStateProp
 |
 | Name | Type | Default | Description
 | `children` | | |

#### XYChart.ErrorState

`XYChart.ErrorState` provides a slot where the Error state wrapper can be set.

#### ErrorStateProps
 |
 | Name | Type | Default | Description
 | `children` | | ((errorMessage: ) => .) | |

#### XYChart.RectSeries

`XYChart.RectSeries` provides a slot for defining a `RectSeries`.

#### XYChartRectSeriesProps
extends |
 | Name | Type | Default | Description
 | `x1Accessor?` | | | Accessor function to retrieve the data for the x1.
 | `y1Accessor?` | | | Accessor function to retrieve the data for the y1.
 | `valueAccessor` | | | Accessor function to retrieve the data for the value.
 | `valueAccessorLabel?` | | | A custom label to overwrite the valueAccessor when naming the value
 | `valueMin?` | | | If specified, all values coming from the valueAccessor that are under this number will display a default color.
Doesn't apply for category values.
 | `valueMax?` | | | If specified, all values coming from the valueAccessor that are above this number will display a default color.
Doesn't apply for category values.
 | `valueFormatter?` | | | | If specified, the value coming from the valueAccessor will be formatted with given formatter options.
Doesn't apply for string values.
 | `valueUnit?` | | | A custom unit to be displayed in the Legend for number values
 | `actions?` | (datapoint: , series?: ) => | | Custom actions to be shown in the tooltip and legend.
For tooltip, information about the selected datapoint is displayed.
For legend, the first parameter returns the first datapoint of the series and the second parameter returns the series object.

#### XYChart.DotSeries

`XYChart.DotSeries` provides a slot for defining a `DotSeries`.

#### XYChartDotSeriesProps

##### Signature:
`export declare type Props = & & {
 /**
 * Series name.
 * @deprecated - Use nameAccessor instead. This key will be removed in a future release.
 */
 name?: ;
 /**
 * Accessor function to retrieve the data for the x1.
 */
 x1Accessor?: ;
 /**
 * Accessor function to retrieve the data for the y1.
 */
 y1Accessor?: ;
 /**
 * Series ID accessor.
 */
 seriesIdAccessor?: ;
 /**
 * Series name accessor.
 */
 nameAccessor?: ;
 /**
 * Custom actions to be shown in the tooltip and legend.
 * For tooltip, information about the selected datapoint is displayed.
 * For legend, the first parameter returns the first datapoint of the series and the second parameter returns the series object.
 */
 actions?: (datapoint: , series?: ) => ;
 /**
 * Determines the visual appearance of the dot, such as , , , or .
 * @defaultValue
 */
 shape?: ;
};`

#### XYChart.LineSeries

`XYChart.LineSeries` provides a slot for defining a `LineSeries`.

#### XYChartLineSeriesProps

##### Signature:
`export declare type Props = & & {
 /**
 * Accessor function to retrieve the data for the x1.
 */
 x1Accessor?: ;
 /**
 * Accessor function to retrieve the data for the y1.
 */
 y1Accessor?: ;
 /**
 * Series ID accessor.
 */
 seriesIdAccessor: ;
 /**
 * Series name accessor.
 */
 nameAccessor: ;
 /**
 * Custom actions to be shown in the tooltip and legend.
 * For tooltip, information about the selected datapoint is displayed.
 * For legend, the first parameter returns the first datapoint of the series and the second parameter returns the series object.
 */
 actions?: (datapoint: , series?: ) => ;
 /**
 * Show the datapoints always, or auto based on a threshold amount.
 * @defaultValue
 */
 pointsDisplay?: ;
 /**
 * Line interpolation curve type
 */
 curve?: ;
};`

### XYChart.ThresholdIndicator

`XYChart.ThresholdIndicator` provides a slot for defining thresholds

#### XYChartThresholdIndicatorProps

##### Signature:
`export declare type XYChartThresholdIndicatorProps = | ;`

### XYChart.Select

`XYChart.Select` provides a slot that enables functionality for selecting a
specific area in the chart.

#### SelectProps
 |
 | Name | Type | Default | Description
 | `actions?` | (selectedSeries: [], selectionDomain: [, ]) => | <> | | Custom actions handler

### XYChart.Intent

`XYChart.Intent` provides a slot to set intents that will appear in the toolbar.

#### IntentProps

##### Signature:
`export declare type IntentProps = | ;`

### XYChart.ColorRule

`XYChart.ColorRule` provides a slot to apply conditional coloring to your chart
series based on their values or names.

#### ColorRuleProps

##### Signature:
`export declare type ColorRuleProps = {
 valueAccessor?: ;
 comparator: ;
 matchValue: ;
} & ;`

### XYChart.CustomTooltip

`XYChart.CustomTooltip` provides a slot for defining a custom tooltip in your
chart.

#### XYChartCustomTooltipProps

##### Signature:
`export declare type XYChartCustomTooltipProps = {
 /**
 * The children function receives the tooltip payload and returns custom tooltip content as React nodes.
 * Return to hide the tooltip, or to use the default.
 */
 children?: (tooltipPayload: ) => ;
};` |
 | Name | Type | Default | Description
 | `children?` | (tooltipPayload: ) => | | The children function receives the tooltip payload and returns custom tooltip content as React nodes.
Return null to hide the tooltip, or undefined to use the default.

### XYChart.Annotations

`XYChart.Annotations` provides a slot for defining annotations in the chart.

#### XYChartAnnotationsProps
extends |
 | Name | Type | Default | Description
 | `data` | [] | | Data object for the xy chart.
 | `xAxisId` | | | Unique Id required to attach the annotations to its x-axis.
 | `showLabels?` | | `false` | Flag for showing/hiding track labels
 | `fixedTracks?` | | `3` | Amount of tracks visible without scrolling.
 | `annotationsActions?` | | | Custom annotations actions on entry selection.

### XYChartAnnotations.Track

`XYChartAnnotations.Track` provides a slot for defining a track in the
`XYChart.Annotations`.

#### XYChartAnnotationsMarkerProps
 |
 | Name | Type | Default | Description
 | `startAccessor` | | | Indicates what data field from the data object should be used as the start point for the markers
 | `endAccessor` | | | Indicates what data field from the data object should be used as the end point of the markers
 | `trackByAccessor` | | | Indicates what data field from the data object should be used to link this marker to a track. It must contain the unique id of a track.
 | `descriptionAccessor?` | | | Indicates what data field from the data object should be used as the description of each marker
 | `colorAccessor?` | | `Colors.Charts.Categorical.Color01.Default` | Indicates what data field from the data object should be used as the color of each marker
 | `titleAccessor?` | | | Indicates what data field from the data object should be used as the title of each marker
 | `symbol?` | | ((t: ) => ) | | letter/emoji/icon/glyph or Unicode character
 | `indicatorsDisplay?` | | ((t: ) => ) | | Defines the display behaviour of marker's indicators of a particular track
 | `hidden?` | | ((t: ) => ) | | Flag to hide a marker
 | `priority?` | | ((t: ) => ) | | Priority of annotation in case of overlapping. The higher the number, the higher priority

### XYChartAnnotations.Marker

`XYChartAnnotations.Marker` provides a slot for defining a marker in the
`XYChart.Annotations`.

#### XYChartAnnotationsTrackProps
 |
 | Name | Type | Default | Description
 | `trackIdAccessor` | | | track Unique ID
 | `labelAccessor?` | | | Indicates what data field from the data object should be used as the label for each track
 | `colorAccessor?` | | | Indicates what data field from the data object should be used as the color of each track
 | `symbol?` | | ((t: ) => ) | | letter/emoji/icon/glyph or Unicode character
 | `indicatorsDisplay?` | | ((t: ) => ) | | Defines the display behaviour of marker's indicators of the entire track
 | `hidden?` | | ((t: ) => ) | | Flag to hide a track

### XYChartAnnotations.Tooltip

`XYChartAnnotations.Tooltip` provides a slot for defining a custom tooltip for
the annotations.

#### AnnotationsTooltipProps
 |
 | Name | Type | Default | Description
 | `hidden?` | | `false` | Defines whether tooltip show be hidden or not
 | `children?` | | | The ChoroplethLayer tooltip handler templateStill have questions?Find answers in the Dynatrace Community
- XYChart.XAxis
- XYChart.YAxis
- XYChart.Legend
- XYChart.Toolbar
- XYChart.EmptyState
- XYChart.ErrorState
- XYChart.RectSeries
- XYChart.DotSeries
- XYChart.LineSeries
- XYChart.ThresholdIndicator
- XYChart.Select
- XYChart.Intent
- XYChart.ColorRule
- XYChart.CustomTooltip
- XYChart.Annotations
- XYChartAnnotations.Track
- XYChartAnnotations.Marker
- XYChartAnnotations.Tooltip

---

## XYChart-AreaSeries

`/design/data-visualizations/charts/XYChart-AreaSeries/`

## AreaSeries
An area series chart fills the region between data points and a baseline, making
it effective for visualizing magnitudes, trends, and cumulative values over a
continuous range. It combines line-based trend visibility with filled regions to
emphasize volume, helping to reveal patterns and comparisons across series.

OverviewProperties

### Import

`tsx
import { XYChart } from '@dynatrace/strato-components/charts';
`

### Overview

To better understand the accessor patterns, here are some common terms used in
this documentation:

- Primary Accessor: Defines the area's position along the main axis (e.g.,
`x0Accessor` for vertical areas).

- Growth Accessor: Defines the area's upper boundary (e.g., `y1Accessor` for
vertical areas).

- Baseline Accessor: Defines the area's lower boundary (e.g., `y0Accessor`
for vertical bands). When omitted, the area fills from the growth value down
to the axis.

- Primary Axis: The axis associated with the primary accessor.

- Growth Axis: The axis associated with the growth accessor.

#### Area vs Band

The AreaSeries can render in two visual modes depending on the accessor pattern:

- Area: When only a growth accessor is provided (no baseline accessor), the
filled region extends from the data line down to the axis origin. This is the
standard area chart.

- Band: When both a growth accessor and a baseline accessor are provided
(e.g., `y0Accessor` and `y1Accessor`), the filled region spans between the two
values. This is useful for confidence intervals, min-max ranges, or tolerance
bands.

The following example shows the same data rendered as an area (no baseline) and
as a band (with a baseline). When `y0Accessor` is omitted the filled region
extends to the axis; when it is provided the fill spans between `y0` and `y1`.

### Usage

Add `XYChart.AreaSeries` inside `XYChart`. Provide accessors to describe the
area's position (primary accessor) and upper boundary (growth accessor).
Orientation is inferred from the accessor pattern.

Required accessors depend on the pattern:

- Vertical area: `x0Accessor` (position) + `y1Accessor` (height)

- Horizontal area: `y0Accessor` (position) + `x1Accessor` (width)

- Vertical band: `x0Accessor` + `y0Accessor` + `y1Accessor`

- Horizontal band: `y0Accessor` + `x0Accessor` + `x1Accessor`

- Vertical area with x-range (timeframe): `x0Accessor` + `x1Accessor` +
`y1Accessor`

- Horizontal area with y-range (timeframe): `y0Accessor` + `y1Accessor` +
`x1Accessor`

Additionally:

- `seriesIdAccessor`: groups datapoints into series (enables multiple series in
one AreaSeries slot)

- `nameAccessor`: series label for legends and tooltips

The `XYChart.AreaSeries` subcomponent also includes the optional properties:
`data`, `color`, `actions`, `pointsDisplay` and `curve`.

Assign the series to axes via `xAxisId` and `yAxisId`. See
XYChart docs for axis configuration.

### Stacking

When multiple series share the same growth axis (numerical, time, or log), the
AreaSeries automatically stacks them. Each area's filled region starts where the
previous one ends.

### Data

The `data` property can be used to overwrite the `XYChart` component for a
specific series.

#### Custom Tooltip

The XYChart component supports custom tooltips via the `XYChart.CustomTooltip`
subcomponent. This allows you to fully control the content and layout of
tooltips for different series types.

Wrap your custom rendering logic in `XYChart.CustomTooltip` and use the provided
payload to determine which series is being hovered. You can return any JSX, or
null to hide the tooltip for a specific series. If you return undefined, the
default tooltip will be used.

#### Points Display

The `pointsDisplay` prop allows you to customize when data points are shown on
the area: `never` hides all points, `always` displays all points, and `auto`
(default) shows points based on a ratio between density of points for the
current series and the chart's width.

#### Value representation

Relative values indicate the proportion that a given dimension contributes to
the total. The `valueRepresentation` prop on the axis can be used to switch
between absolute and relative display.

- For single areas and band configurations, the relative value is based on the
maximum absolute value within the series.

- For stacked areas, each area will scale relative to the total stack height at
each point, so the full height represents 100%. In case of having positive and
negative values, they are scaled together where 100% is the highest absolute
value amongst the two parts.

#### Series curve

You can select the curve shape of the `AreaSeries` via the `curve` prop. The
available options are `linear` where line joins will be straight (default
option) or `smooth` for a more fluid curve.

#### Gap policy

The AreaSeries respects the `gapPolicy` set on a numerical or time axis. For
time axes, gap policy defaults to `gap`. Three options are available:

- `connect`: interpolates across the gap, connecting consecutive data points
regardless of the distance between them. This is the default behavior for
numerical axes.

- `gap`: leaves the gap visible as a break in the area. This option is only
available for time axes, where it is the default behavior.

- `threshold`: defines a maximum distance between consecutive data points. When
the distance is within the threshold, data points are connected; otherwise, a
gap is displayed. For time axes, the threshold is specified as a duration
string (e.g., `'3h'`, `'1d'`). For numerical axes, the threshold is a number
representing the maximum allowed distance between consecutive values.

For numerical axes, `gapPolicy` defaults to `connect`. Use the `threshold`
option to introduce gaps when the distance between data points exceeds a
specified value.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the `XYChart`. More
subcomponents can be added within this component, for instance
`ChartSeriesAction.Item`, where you can provide a custom action that will appear
in the legend menu. That action can execute any custom logic in its `onSelect`
callback or get disabled via a `disabled` prop. `Intents` could be added as part
of the series action as well with `ChartSeriesAction.Intent`.

If the datapoint belongs to a stack that has a categorical primary axis, the
datapoint together with the other stacked datapoints in the same category will
be returned.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Overview
- Area vs Band
- Usage
- Stacking
- Data
- Custom Tooltip
- Points Display
- Value representation
- Series curve
- Gap policy
- Series actions

### Props

- XYChart-AreaSeries
## AreaSeries
An area series chart fills the region between data points and a baseline, making
it effective for visualizing magnitudes, trends, and cumulative values over a
continuous range. It combines line-based trend visibility with filled regions to
emphasize volume, helping to reveal patterns and comparisons across series.

OverviewProperties

### XYChart.AreaSeries

`XYChart.AreaSeries` provides a slot for defining an `AreaSeries`.

#### XYChartAreaSeriesProps

##### Signature:
`export declare type Props = & & {
 x0Accessor?: ;
 y0Accessor?: ;
 x1Accessor?: ;
 y1Accessor?: ;
 seriesIdAccessor: ;
 nameAccessor: ;
 /**
 * Show the datapoints always, or auto based on a threshold amount.
 * @defaultValue
 */
 pointsDisplay?: ;
 /**
 * Area interpolation curve type
 */
 curve?: ;
 /**
 * Custom actions to be shown in the legend.
 * (Upcoming for tooltip)
 * For legend, the first parameter returns the first datapoint of the series and the second parameter returns the series object.
 */
 actions?: (datapoint: , series?: ) => ;
};`Still have questions?Find answers in the Dynatrace Community
- XYChart.AreaSeries

---

## XYChart-BarSeries

`/design/data-visualizations/charts/XYChart-BarSeries/`

## BarSeries
The BarSeries renders rectangular bars to visualize values across categories,
numbers or time. It supports simple, grouped (clustered), and stacked layouts,
making it ideal for comparisons, totals, and distributions. The BarSeries works
with numeric, time, and categorical axes, and handles a wide range of data
types—perfect for Bar, Column, and Stacked charts.

OverviewProperties

### Import

`tsx
import { XYChart } from '@dynatrace/strato-components/charts';
`

### Overview

To better understand the accessor patterns, here are some common terms used in
this documentation:

- Primary Accessor: Defines the bar's position along the main axis (e.g.,
`x0Accessor` for vertical bars).

- Growth Accessor: Defines the bar's length or height (e.g., `y1Accessor`
for vertical bars).

- Primary Axis: The axis associated with the primary accessor.

- Growth Axis: The axis associated with the growth accessor.

- Base Bucket: A discrete slot or category on the primary axis where one or
more bars are drawn. For a categorical axis, each category is a bucket.

A Bar series displays values as rectangular bars spreading from a configurable
base X or Y axis. It supports three variants: single, stacked, and grouped, and
works with categorical, numerical, time, and log axes.

- Single: one bar per base bucket, shown as a vertical or horizontal bar.

- Stacked: bars from multiple series accumulate along the growth axis. Supported
only when the growth accessor is numerical, time, or log.

- Grouped: multiple series appear side-by-side within each base bucket for
direct comparison. Supported only when the primary accessor is categorical.

- Range bars: a bar that spans between two values. Available in the grouped and
single variants.

- Full rectangles: manual placement using four accessors (`x0Accessor`,
`x1Accessor`, `y0Accessor`, `y1Accessor`) to draw arbitrary rectangles; useful
for waterfall-like layouts (single variant only).

### Usage

Add `XYChart.BarSeries` inside `XYChart`. Provide accessors to describe the
bar’s position (primary accessor) and growth (growth accessor). Orientation is
inferred from the accessor pattern, no orientation prop required.

Required accessors depend on the pattern:

- Vertical single bars: `x0Accessor` (position) + `y1Accessor` (height)

- Horizontal single bars: `y0Accessor` (position) + `x1Accessor` (width)

- Vertical floating bars: `x0Accessor` + `y0Accessor` + `y1Accessor`

- Horizontal floating bars: `y0Accessor` + `x0Accessor` + `x1Accessor`

- Vertical range bars: `x0Accessor` + `x1Accessor` + `y1Accessor`

- Horizontal range bars: `y0Accessor` + `y1Accessor` + `x1Accessor`

- Full rectangle (manual placement): `x0Accessor` + `x1Accessor` +
`y0Accessor` + `y1Accessor` (single variant only)

Additionally:

- `seriesIdAccessor`: groups datapoints into series (enables multiple series in
one BarSeries slot)

- `nameAccessor`: series label for legends and tooltips

Assign the series to axes via `xAxisId` and `yAxisId`. See
XYChart docs for axis configuration.

### Variants

#### Single

This type refers to independent bars, which support all valid accessor patterns.
Specific details for the accessors structure can be found below:

- Automatic direction:

- Vertical bars: `x0Accessor + y1Accessor`

- Horizontal bars: `y0Accessor + x1Accessor`

- Waterfall-like rectangles:

- Use `variant="single"` with
`x0Accessor + x1Accessor + y0Accessor + y1Accessor` to manually position
rectangles. Stacking and grouping are not supported for full rectangles.

- Note:

- Multiple floating range bars per category can overlap in `variant="single"`.
Use `variant="group"` with `x0Accessor + y0Accessor + y1Accessor` to show
them side-by-side.

Examples:

#### Stack

Data can be displayed stacked by setting the BarSeries `variant` to `stack`.
Bars stack at the same primary accessor by using the `seriesIdAccessor` to group
the data. Stack behaviour is supported for all axes except categorical-type if
they belong to a growth axis.

These accessors patterns are valid for stacking:

- Vertical stacked bars: `x0Accessor + y1Accessor`

- Horizontal stacked bars: `y0Accessor + x1Accessor`

- Stacked bars with X-range span: `x0Accessor + x1Accessor + y1Accessor` (stacks
vertically, grouped by the X range)

- Stacked bars with Y-range span: `y0Accessor + y1Accessor + x1Accessor` (stacks
horizontally, grouped by the Y range)

The following accessor patterns are not supported for stacking:

- Floating range bars (Y-range only: `y0Accessor + y1Accessor`)

- Full rectangles (`x0Accessor + x1Accessor + y0Accessor + y1Accessor`)

Examples:

#### Group

Data can also be displayed grouped by setting the BarSeries `variant` to
`group`, where the bars will be positioned side-by-side within the same bucket.
In order to group, a categorical primary axis is required (the axis used for
`x0Accessor` in vertical bars or `y0Accessor` in horizontal bars). If the
primary axis is numerical, time, or log (i.e., not categorical), the series will
fall back to `variant="single"`.

These accessors patterns are valid for grouping:

- Vertical grouped bars: `x0Accessor + y1Accessor`

- Vertical grouped range bars: `x0Accessor + y0Accessor + y1Accessor`

- Horizontal grouped bars: `y0Accessor + x1Accessor`

- Horizontal grouped range bars: `y0Accessor + x0Accessor + x1Accessor`

The following accessor patterns are not supported for grouping:

- X-range with growth (`x0Accessor + x1Accessor + y1Accessor`)

- Y-range with growth (`y0Accessor + y1Accessor + x1Accessor`)

- Full rectangles (`x0Accessor + x1Accessor + y0Accessor + y1Accessor`)

Examples:

### Axis compatibility

The rendering behavior of `BarSeries` variants is tightly coupled with the axis
types they are assigned to. To ensure the chart renders as expected, please note
the following requirements:

- Grouping requires a categorical primary axis (e.g., categorical X-axis for
vertical bars).

- Stacking works with numerical, time, and log axes. A categorical growth axis
cannot stack.

- Unsupported combinations automatically fall back to supported behavior,
typically `variant="single"`, and log a warning.

### Data

The data provided to the `BarSeries` component via the `data` property will be
used in combination with the accessors of each series.

#### Coloring

By using the `color` and `colorPalette` properties in the `BarSeries` you can
overwrite the coloring from the `XYChart` component. These two properties are
mutually exclusive. For more information about how to use coloring in the chart
you can refer to the XYChart docs.

The `XYChart.BarSeries` subcomponent supports functions for the `color` and
`colorPalette` props to customize coloring per series in case more than one
series is presented in the same slot.

#### Color Rules

`ColorRules` are advanced coloring tools for the chart, allowing you to apply
conditional coloring based on data values. See more details in the
XYChart docs.

#### Series actions

A series action is a creator, defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the `XYChart`. More
subcomponents can be added within this component, for instance
`ChartSeriesAction.Item`, where you can provide a custom action that will appear
in the legend menu. That action can execute any custom logic in its `onSelect`
callback or get disabled via a `disabled` prop. `Intents` could be added as part
of the series action as well with `ChartSeriesAction.Intent`.

If the datapoint belongs to a stack or group that belongs to a categorical
primary axis, the datapoint together with the other datapoints in the same stack
or group will be returned to be used in the action.

#### Custom Tooltip

The XYChart component supports custom tooltips via the XYChart.CustomTooltip
subcomponent. This allows you to fully control the content and layout of
tooltips for different series types.

Wrap your custom rendering logic in XYChart.CustomTooltip and use the provided
payload to determine which series is being hovered. You can return any JSX, or
null to hide the tooltip for a specific series. If you return undefined, the
default tooltip will be used.

#### Value representation

Relative values indicate the proportion that a given dimension contributes to
the sum (100%) of a given bar. The `valueRepresentation` prop can be used to
change this behavior.

- For series with only a single dimension, the relative value is based on the
maximum value within the given series.

- For series with stacked bars, each bar will scale relative to itself, meaning
the total height of the stack will be 100%. In case of having positive and
negative values in the same stack, the positive and negative values will be
scaled together, where the 100% will be the highest absolute value amongst the
two positive and negative parts of it. This allows for easy comparison of the
relative contribution of each dimension within the stack, regardless of the
difference amongst absolute values.

- For series with grouped bars, each bar will scale relative to the total
addition of all bars within the same category, allowing for easy comparison of
the relative contribution of each bar within the category regardless of the
difference amongst absolute values. In case of having positive and negative
values in the same category, the positive and negative values will be scaled
together, where the 100% will be the highest absolute addition of bars amongst
the two positive and negative parts of it. This allows for easy comparison of
the relative contribution of each bar within the category, regardless of the
difference amongst absolute values.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Overview
- Usage
- Variants
- Single
- Stack
- Group
- Axis compatibility
- Data
- Coloring
- Color Rules
- Series actions
- Custom Tooltip
- Value representation

### Props

- XYChart-BarSeries
## BarSeries
The BarSeries renders rectangular bars to visualize values across categories,
numbers or time. It supports simple, grouped (clustered), and stacked layouts,
making it ideal for comparisons, totals, and distributions. The BarSeries works
with numeric, time, and categorical axes, and handles a wide range of data
types—perfect for Bar, Column, and Stacked charts.

OverviewProperties

### XYChart.BarSeries

`XYChart.BarSeries` provides a slot for defining a `BarSeries`.

#### XYChartBarSeriesProps

##### Signature:
`export declare type Props = ( | | ) & {
 /**
 * Custom actions to be shown in the tooltip and legend.
 * For tooltip, information about the selected datapoint is displayed.
 * For legend, the first parameter returns the first datapoint of the series and the second parameter returns the series object.
 */
 actions?: (datapoint: , series?: ) => ;
};`Still have questions?Find answers in the Dynatrace Community
- XYChart.BarSeries

---

## XYChart-DotSeries

`/design/data-visualizations/charts/XYChart-DotSeries/`

## DotSeries
The DotSeries is a type of shape that provides a two-dimensional representation
of data in which pairs of values are shown. This shape turns out great for
representing groups of values spread in classes. It can be an essential
component when creating charts such as Scatter and Dot Plots.

OverviewProperties

### Import

`tsx
import { XYChart } from '@dynatrace/strato-components/charts';
`

### Use cases

A Dot series visualizes data as individual dots and is used to create charts
like scatter plots, strip plots, opposite diagrams, or dot charts.

##### Scatter plot

##### Strip plot

##### Opposite diagram

### Usage

To display a Dot Series, add the `XYChart.DotSeries` subcomponent within the
`XYChart` component.

This series requires four essential properties that will function as data
accessors and identifier of the series:

- `x0Accessor`: indicates the X value of the data point within the X-domain.

- `y0Accessor`: indicates the Y value of the data point within the Y-domain.

- `name`: indicates the name of the series.

- `seriesIdAccessor`: specifies which data should be used as the unique
identifier for each series. This identifier will be used to group data points
belonging to the same series, allowing multiple series per slot.

- `nameAccessor`: indicates what data should be used as the name of the series.

These accessors support numerical, categorical and time data. When using the
time data, a single accessor is enough for timestamps, but this series also
supports timeframes. If using a timeframe, a second pair of accessors is needed
in order to define the position of the point. In this case the series will
position the data point in the average time of both end points of the timeframe.

- `x1Accessor`: indicates the X end point value for a data point timeframe.

- `y1Accessor`: indicates the Y end point value for a data point timeframe.

It's relevant to comment that these two accessors have no utility when using
non-temporal data.

These accessors will extract the specified data from the provided object array
via the `data` property. It’s crucial to note that the accessors are used to
position the data points in the 2-dimensional space; incorrect specification of
any accessor will result in an inability to generate the DotSeries correctly.

Additionally, a `XYChart.DotSeries` will need to be assigned to at least one
x-axis and one y-axis via valid `xAxisId` and `yAxisId` properties. For a more
detailed explanation of the axis configuration, please refer to the
XYChart docs.

The `XYChart.DotSeries` subcomponent includes some other optional properties:
`data`, `colorPalette`, `color` and `actions`.

The `data`, `colorPalette` and `color` properties can be used to overwrite the
`XYChart` component for a specific series.

#### Data

The data provided to the `DotSeries` component via the `data` property will be
used in combination with the accessors of each series.

#### Coloring

By using the `color` and `colorPalette` properties in the `DotSeries` you can
overwrite the coloring from the `XYChart` component. These two properties are
mutually exclusive. For more information about how to use coloring in the chart
you can refer to the XYChart docs.

##### Color

The `color` property allows you to set any desired color as the color of the
dots of a specific series.

##### Color Rules

`ColorRules` are advanced coloring tools for the chart, allowing you to apply
conditional coloring based on data values. See more details in the
XYChart docs.

#### Shapes

The `shape` property on `DotSeries` allows you to display different geometric
shapes for each data point in the series. In addition to the default `circle`,
you can now choose between `square`, `diamond`, and `triangle` shapes.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the `XYChart`. More
subcomponents can be added within this component, for instance
`ChartSeriesAction.Item`, where you can provide a custom action that will appear
in the legend menu. That action can execute any custom logic in its `onSelect`
callback or get disabled via a `disabled` prop. `Intents` could be added as part
of the series action as well with `ChartSeriesAction.Intent`.

#### Custom Tooltip

The XYChart component supports custom tooltips via the XYChart.CustomTooltip
subcomponent. This allows you to fully control the content and layout of
tooltips for different series types.

Wrap your custom rendering logic in XYChart.CustomTooltip and use the provided
payload to determine which series is being hovered. You can return any JSX, or
null to hide the tooltip for a specific series. If you return undefined, the
default tooltip will be used.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Usage
- Data
- Coloring
- Shapes
- Series actions
- Custom Tooltip

### Props

- XYChart-DotSeries
## DotSeries
The DotSeries is a type of shape that provides a two-dimensional representation
of data in which pairs of values are shown. This shape turns out great for
representing groups of values spread in classes. It can be an essential
component when creating charts such as Scatter and Dot Plots.

OverviewProperties

### XYChart.DotSeries

`XYChart.DotSeries` provides a slot for defining a `DotSeries`.

#### XYChartDotSeriesProps

##### Signature:
`export declare type Props = & & {
 /**
 * Series name.
 * @deprecated - Use nameAccessor instead. This key will be removed in a future release.
 */
 name?: ;
 /**
 * Accessor function to retrieve the data for the x1.
 */
 x1Accessor?: ;
 /**
 * Accessor function to retrieve the data for the y1.
 */
 y1Accessor?: ;
 /**
 * Series ID accessor.
 */
 seriesIdAccessor?: ;
 /**
 * Series name accessor.
 */
 nameAccessor?: ;
 /**
 * Custom actions to be shown in the tooltip and legend.
 * For tooltip, information about the selected datapoint is displayed.
 * For legend, the first parameter returns the first datapoint of the series and the second parameter returns the series object.
 */
 actions?: (datapoint: , series?: ) => ;
 /**
 * Determines the visual appearance of the dot, such as , , , or .
 * @defaultValue
 */
 shape?: ;
};`Still have questions?Find answers in the Dynatrace Community
- XYChart.DotSeries

---

## XYChart-LineSeries

`/design/data-visualizations/charts/XYChart-LineSeries/`

## LineSeries
A line series chart connects data points with a continuous line, making it easy
to observe changes or trends over 2-variable paired data, helping to reveal
dependencies or correlations (or both). The chart allows for assigning the
variables to both X and Y-axis.

OverviewProperties

### Import

`tsx
import { XYChart } from '@dynatrace/strato-components/charts';
`

### Use cases

A Line Series Chart in an XY Chart is a tool used for visualizing trends,
relationships, and patterns in data over a continuous range, such as time or
numerical values.

### Usage

To display a Line Series, add the `XYChart.LineSeries` subcomponent within the
`XYChart` component.

This series requires five essential properties that will function as data
accessors:

- `x0Accessor`: indicates what data should be used as the start point for the
x-axis baseline.

- `x1Accessor`: indicates what data should be used as the end point for the
x-axis baseline. It can be used for all types of axes, except for categorical
ones.

- `y0Accessor`: indicates what data should be used as the start point for the
y-axis baseline.

- `y1Accessor`: indicates what data should be used as the end point for the
y-axis baseline. It can be used for all types of axes, except for categorical
ones.

- `seriesIdAccessor`: specifies which data should be used as the unique
identifier for each series. This identifier will be used to group data points
belonging to the same series, allowing multiple series per slot.

- `nameAccessor`: indicates what data should be used as the name of the series.

These accessors will extract the specified data from the provided object array
via the `data` property. It’s crucial to note that the accessors are used to
position the data points in the 2-dimensional space; incorrect specification of
any accessor will result in an inability to generate the LineSeries correctly.

Additionally, a `XYChart.LineSeries` will need to be assigned to at least one
x-axis and one y-axis via valid `xAxisId` and `yAxisId` properties. For a more
detailed explanation of the axis configuration, please refer to the
XYChart docs.

The `XYChart.LineSeries` subcomponent includes some other optional properties:
`data`, `colorPalette`, `color`, `actions`, `pointsDisplay` and `curve`.

The `data`, `colorPalette` and `color` properties can be used to overwrite the
`XYChart` component for a specific series.

#### Data

The data provided to the `LineSeries` component via the `data` property will be
used in combination with the accessors of each series.

#### Coloring

By using the `color` and `colorPalette` properties in the `LineSeries` you can
overwrite the coloring from the `XYChart` component. These two properties are
mutually exclusive. For more information about how to use coloring in the chart
you can refer to the XYChart docs.

The `XYChart.LineSeries` subcomponent supports functions for the `color` and
`colorPalette` props to customize coloring per series in case more than one
series is presented in the same slot.

##### Color

The `color` property allows you to set any desired color for the lines of a
specific series.

##### Color Rules

`ColorRules` are advanced coloring tools for the chart, allowing you to apply
conditional coloring based on data values. See more details in the
XYChart docs.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the `XYChart`. More
subcomponents can be added within this component, for instance
`ChartSeriesAction.Item`, where you can provide a custom action that will appear
in the legend menu. That action can execute any custom logic in its `onSelect`
callback or get disabled via a `disabled` prop. `Intents` could be added as part
of the series action as well with `ChartSeriesAction.Intent`.

#### Points Display

The `pointsDisplay` prop allows you to customize when data points are shown on
the line: `never` hides all points, `always` displays all points, and `auto`
(default) shows points based on a ratio between density of points for the
current series and the chart's width.

#### Series curve

You can select the curve shape of the `LineSeries` via the `curve` prop. The
available options are `linear` where line joins will be straight (default
option) or `smooth` for a more fluid curve.

#### Custom Tooltip

The XYChart component supports custom tooltips via the XYChart.CustomTooltip
subcomponent. This allows you to fully control the content and layout of
tooltips for different series types.

Wrap your custom rendering logic in XYChart.CustomTooltip and use the provided
payload to determine which series is being hovered. You can return any JSX, or
null to hide the tooltip for a specific series. If you return undefined, the
default tooltip will be used.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Usage
- Data
- Coloring
- Series actions
- Points Display
- Series curve
- Custom Tooltip

### Props

- XYChart-LineSeries
## LineSeries
A line series chart connects data points with a continuous line, making it easy
to observe changes or trends over 2-variable paired data, helping to reveal
dependencies or correlations (or both). The chart allows for assigning the
variables to both X and Y-axis.

OverviewProperties

### XYChart.LineSeries

`XYChart.LineSeries` provides a slot for defining a `LineSeries`.

#### XYChartLineSeriesProps

##### Signature:
`export declare type Props = & & {
 /**
 * Accessor function to retrieve the data for the x1.
 */
 x1Accessor?: ;
 /**
 * Accessor function to retrieve the data for the y1.
 */
 y1Accessor?: ;
 /**
 * Series ID accessor.
 */
 seriesIdAccessor: ;
 /**
 * Series name accessor.
 */
 nameAccessor: ;
 /**
 * Custom actions to be shown in the tooltip and legend.
 * For tooltip, information about the selected datapoint is displayed.
 * For legend, the first parameter returns the first datapoint of the series and the second parameter returns the series object.
 */
 actions?: (datapoint: , series?: ) => ;
 /**
 * Show the datapoints always, or auto based on a threshold amount.
 * @defaultValue
 */
 pointsDisplay?: ;
 /**
 * Line interpolation curve type
 */
 curve?: ;
};`Still have questions?Find answers in the Dynatrace Community
- XYChart.LineSeries

---

## XYChart-RectSeries

`/design/data-visualizations/charts/XYChart-RectSeries/`

## RectSeries
A `RectSeries` is a type of shape that provides a two-dimensional representation
of data in which various values are represented by colors. This shape excels at
allowing the user to compare values and observe patterns. One of the most
popular uses this shape can be used for are HeatMaps.

OverviewProperties

### Import

`tsx
import { XYChart } from '@dynatrace/strato-components/charts';
`

### Use cases

A Rect series visualizes data as colored rectangles and is used to create charts
like heatmaps, Gantt charts, or availability charts.

##### Heatmap

##### Gantt chart

##### Availability chart

### Usage

To display a `RectSeries`, add the `XYChart.RectSeries` subcomponent within the
`XYChart` component.

This series requires five essential properties that will function as data
accessors:

- `x0Accessor`: indicates what data should be used as the start point for the
x-axis baseline.

- `x1Accessor`: indicates what data should be used as the end point for the
x-axis baseline. Not required for categorical-type axes.

- `y0Accessor`: indicates what data should be used as the start point for the
y-axis baseline.

- `y1Accessor`: indicates what data should be used as the end point for the
y-axis baseline. Not required for categorical-type axes.

- `valueAccessor`: indicates what data should be used as the tile value, which
represents the intensity of the tile color.

These accessors will extract the specified data from the provided object array
via the `data` property. It’s crucial to note that the accessors are used to
construct each cell’s dimensions; incorrect specification of any accessor will
result in an inability to generate the correct rect series.

Additionally, a `XYChart.RectSeries` will need to be assigned to at least one
x-axis and one y-axis via valid `xAxisId` and `yAxisId` properties. For a more
detailed explanation of the axis configuration, please refer to the
XYChart docs.

The `XYChart.RectSeries` subcomponent includes some other optional properties:
`data`, `colorPalette`, `valueAccessorLabel`, `valueUnit`, `valueFormatter`,
`valueMin`, `valueMax` and `actions`.

The `data` and `colorPalette` properties can be used to overwrite the `XYChart`
component for a specific series.

#### Data

The data provided to the `RectSeries` component via the `data` property will be
used in combination with the accessors of each series.

#### Coloring

By using the `colorPalette` property in the `RectSeries` you can overwrite the
coloring from the `XYChart` component. For more information about how to use
coloring in the chart you can refer to the XYChart docs.

##### Color Rules

`ColorRules` are advanced coloring tools for the chart, allowing you to apply
conditional coloring based on data values. See more details in the
XYChart docs.

##### Overlapping tiles

The sides of the tiles can be defined freely, in case of overlapping amongst two
or more tiles, these will transparent through one another and show a mixed
color.

##### Min and max values

By setting the `valueMin` and `valueMax` properties, you can establish
boundaries for all values. Values outside these boundaries will display a
default color. Note that string values are not affected by these boundaries and
will display their original color.

#### Value Label

Given the `valueAccessor` depends on how the data is named and structured, the
final result can be complicated to understand for the user. By using the
property `valueAccessorLabel` any name can be set in order to identify the
value.

#### Unit and formatter

You can apply a unit and formatter to the data extracted by the `valueAccessor`
via `valueUnit` and `valueFormatter` as long as it is of type number. If the
data is of type string then these properties will be disregarded.

#### Series actions

A series action is a creator-defined interaction with a given data point in the
chart. Basic interactions include copying a series name and inspecting the
underlying data of a data point. Series actions support both synchronous and
asynchronous callbacks. In order to enable chart interactions, the
`ChartSeriesAction` subcomponent needs to be appended within the `XYChart`. More
subcomponents can be added within this component, for instance
`ChartSeriesAction.Item`, where you can provide a custom action that will appear
in the legend menu. That action can execute any custom logic in its `onSelect`
callback or get disabled via a `disabled` prop. `Intents` could be added as part
of the series action as well with `ChartSeriesAction.Intent`.

#### Custom Tooltip

The XYChart component supports custom tooltips via the XYChart.CustomTooltip
subcomponent. This allows you to fully control the content and layout of
tooltips for different series types.

Wrap your custom rendering logic in XYChart.CustomTooltip and use the provided
payload to determine which series is being hovered. You can return any JSX, or
null to hide the tooltip for a specific series. If you return undefined, the
default tooltip will be used.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Usage
- Data
- Coloring
- Value Label
- Unit and formatter
- Series actions
- Custom Tooltip

### Props

- XYChart-RectSeries
## RectSeries
A `RectSeries` is a type of shape that provides a two-dimensional representation
of data in which various values are represented by colors. This shape excels at
allowing the user to compare values and observe patterns. One of the most
popular uses this shape can be used for are HeatMaps.

OverviewProperties

### XYChart.RectSeries

`XYChart.RectSeries` provides a slot for defining a `RectSeries`.

#### XYChartRectSeriesProps
extends |
 | Name | Type | Default | Description
 | `x1Accessor?` | | | Accessor function to retrieve the data for the x1.
 | `y1Accessor?` | | | Accessor function to retrieve the data for the y1.
 | `valueAccessor` | | | Accessor function to retrieve the data for the value.
 | `valueAccessorLabel?` | | | A custom label to overwrite the valueAccessor when naming the value
 | `valueMin?` | | | If specified, all values coming from the valueAccessor that are under this number will display a default color.
Doesn't apply for category values.
 | `valueMax?` | | | If specified, all values coming from the valueAccessor that are above this number will display a default color.
Doesn't apply for category values.
 | `valueFormatter?` | | | | If specified, the value coming from the valueAccessor will be formatted with given formatter options.
Doesn't apply for string values.
 | `valueUnit?` | | | A custom unit to be displayed in the Legend for number values
 | `actions?` | (datapoint: , series?: ) => | | Custom actions to be shown in the tooltip and legend.
For tooltip, information about the selected datapoint is displayed.
For legend, the first parameter returns the first datapoint of the series and the second parameter returns the series object.Still have questions?Find answers in the Dynatrace Community
- XYChart.RectSeries

---

## convertToTimeseries

`/design/data-visualizations/charts/convertToTimeseries/`

The `convertToTimeseries` function takes a set of Grail records and converts it
to `Timeseries` which can be used for charting.

### Import

`tsx
import { convertToTimeseries } from '@dynatrace/strato-components/charts';
`

### Use cases

Pass an array in the format of `RangedFieldTypes` and dataset in the format of
`ResultRecord` and receive an array of `Timeseries` data.

#### Exclude fields from being converted

The parameter `hiddenFieldIds` provides a way to specify a list of field ids
that should not be converted.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Exclude fields from being converted

---

