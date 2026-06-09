# Geo maps (data visualizations)

Strato design-system components in the **Geo maps (data visualizations)** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## BaseLayer

`/design/data-visualizations/geo-maps/BaseLayer/`

The base layer component, used to configure the inclusion and exclusion of
countries and regions

OverviewProperties

### Import

`tsx
import { BaseLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `BaseLayer` component to render a map with controlled countries and
regions. It accepts an array of country codes and region codes in ISO 3166-2
format as `include` or `exclude` props to control the display of regions on the
map. Use the `*` symbol to include all countries and the `-*` suffix to include
all country states. You can control the display of both countries and regions in
the same array.

`tsx
const include = ['ES-*', 'AT'];const exclude = ['ES-CT'];
`

Learn more about the data format here.

#### Inclusion/Exclusion of countries

##### Include only Spain and Austria

##### Include all countries, without Spain and Austria

#### Mix of country and state level regions

##### Include all countries, and all regions of Spain and Austria

##### Include Spain and Austria, without regions: Catalonia, Madrid, Vienna, Upper Austria

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Inclusion/Exclusion of countries
- Mix of country and state level regions

### Props

The base layer component, used to configure the inclusion and exclusion of
countries and regions

OverviewProperties

### BaseLayer

#### BaseLayerProps
 |
 | Name | Type | Default | Description
 | `include?` | [] | | Include countries
 | `exclude?` | [] | | Exclude countriesStill have questions?Find answers in the Dynatrace Community
---

## BubbleLayer

`/design/data-visualizations/geo-maps/BubbleLayer/`

The `BubbleLayer` component renders data points as bubbles on a map, accepting
an array of data points with required properties like latitude and longitude. It
supports customization of bubble size using the radius prop and optional
tooltips for displaying additional information.

OverviewProperties

### Import

`tsx
import { BubbleLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `BubbleLayer` component to render data points with customizable radius.
The `BubbleLayer` component accepts an array of data points as the data prop.
Each data point must have `latitude` and `longitude` as minimum required
properties.

`tsx
[ { radius: 85, longitude: -115.195615, latitude: 36.171462, }, { radius: 35, longitude: -94.556725, latitude: 39.104532, }, { radius: 40, longitude: -73.998772, latitude: 40.717575, },];
`

Learn more about the data format here.

#### Size interpolation

The `sizeInterpolation` prop determines how the size of the bubbles changes with
zoom level.

- `'zoom'`: The size of the bubbles adjusts dynamically based on the zoom level
of the map. As the user zooms in or out, the bubble sizes change accordingly
to maintain relative proportions.

- `'fixed'`:The size of the bubbles remains constant regardless of the zoom
level. This means that as the user zooms in or out, the size of the bubbles on
the map remains the same, offering consistent visual representation.

#### Scale and radius

The `scale` prop controls how the size of the bubbles is scaled, affecting their
visual representation on the map.

##### Linear Scaling

This is the default scaling mode, in which the size of the bubbles is scaled
linearly based on the data range provided. The size of the bubbles increases or
decreases proportionally to data values.

In this scaling mode, the value accessor has to be explicitly provided by
passing to the `radius` prop a callback that returns the value which will be
used to calculate the scale.

Additionally, when using linear scaling, you have the option to specify a
`radiusRange`, which is an array or the minimum and maximum sizes for the bubble
radius in pixels. This allows more control over the size range of bubble
displayed on the map.

##### Logarithmic Scaling

Alternatively, setting the `scale` prop to `'log'` applies logarithmic scaling
to the bubble sizes. Logarithmic scaling is useful for representing data that
spans several orders of magnitude, as it compresses the range of values into a
more visually manageable scale.

Similar to linear scaling, logarithmic scaling also allows for specifying a
`radiusRange` to define the minimum and maximum sizes for the bubble radius.

In this scaling mode, the `radius` prop must be callback function that
dynamically calculates the radius based on the data points.

##### No Scaling

In contrast, when the scale prop is set to `'none'`, no automatic scaling is
applied to the bubble size. A constant number must be provided for the `radius`
prop to set the size of all bubbles uniformly, or a callback function that will
be run for each data point and the returned value used as a radius. When
`radius` prop is not set, the default radius of 12px will be applied.

Be aware, that the `radiusRange` prop is not supported in `none` scaling mode
because it's not possible to derive the scaling mechanism for the provided
range.

#### Tooltip

The `BubbleLayer` component has an optional tooltip that displays additional
data point information when hovering over data points from any of the data
layers. To enable the tooltip a `BubbleLayer.Tooltip` subcomponent should be
passed inside the `BubbleLayer` component. When a `BubbleLayer.Tooltip`
subcomponent is provided without any children, the default tooltip will be used.

By default, the tooltip will display the location information of the hovered
bubble, but
it can be heavily customized.

#### Coloring

The `BubbleLayer` supports two ways of color configuration: granular
configuration using the `color` prop, or using a one of the available legend
subcomponents (e.g. `SequentialLegend`, `ThresholdLegend`, or
`CategoricalLegend`).

Note: Detailed information about coloring can be found in the `MapView`
documentation page under the `Coloring` section.

#### Granular color configuration

For a granular color customization, layer's `color` prop should be used.

#### Color configuration using a legend

To connect a data layer to the legend, a `color` property of the layer should be
set to `legend` string.

##### Sequential legend

##### Threshold legend

##### Categorical legend

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Size interpolation
- Scale and radius
- Tooltip
- Coloring
- Granular color configuration
- Color configuration using a legend

### Props

The `BubbleLayer` component renders data points as bubbles on a map, accepting
an array of data points with required properties like latitude and longitude. It
supports customization of bubble size using the radius prop and optional
tooltips for displaying additional information.

OverviewProperties

### BubbleLayer

#### BubbleLayerProps

##### Signature:
`export declare type BubbleLayerProps = & ( | ) & ( | );`

#### BubbleLayerBaseProps
extends |
 | Name | Type | Default | Description
 | `data` | T[] | | An array of location data items to be displayed as bubbles in the BubbleLayer
 | `sizeInterpolation?` | | | `'fixed'` | Determines the interpolation mode for bubble size.
'zoom': Bubble size changes with zoom.
'fixed': Constant bubble size regardless of zoom level.

#### LocationColorProps
 |
 | Name | Type | Default | Description
 | `color?` | | ((item: T) => ) | | Custom color to apply to the layer

#### LegendColorLayerProps
 |
 | Name | Type | Default | Description
 | `color` | | | When the color prop is set to 'legend', a value accessor is needed
 | `valueAccessor` | | | The value accessor to map data point values to legend color

#### ScaleRadiusProps
 |
 | Name | Type | Default | Description
 | `scale?` | | | `'linear'` | The way the radius is scaled.
 | `radius` | (item: T) => | | The radius property, which determines the size of the bubbles.
It requires a callback that is used as data accessor.
 | `radiusRange?` | [, ] | `[10, 100]` | It determines the min and max size for the bubble radius

#### ScaleNoneProps
 |
 | Name | Type | Default | Description
 | `scale` | | | The way to indicate that scale should not be used
 | `radius?` | | ((item: T) => ) | `12` | The radius property, which determines the size of the bubbles.
It can be a constant number or a function that calculates the radius based on the data item

#### Location
 |
 | Name | Type | Default | Description
 | `latitude` | | | The latitude coordinate of the location.
 | `longitude` | | | The longitude coordinate of the location.

### Tooltip

#### BubbleLayerTooltipData
 |
 | Name | Type | Default | Description
 | `color` | | | The hovered bubble color
 | `radius` | | | The hovered bubble radius
 | `data` | T | | The hovered bubble custom data and location

#### BubbleLayerTooltipHandler

##### Signature:
`export declare type BubbleLayerTooltipHandler = (closestDot: , dotsData: []) => | ;`

#### BubbleLayerTooltipHandlerProps
 |
 | Name | Type | Default | Description
 | `children?` | | | | The BubbleLayer tooltip handler template
 | `seriesActions?` | (location: ) => | | Series actions callback for the default tooltipStill have questions?Find answers in the Dynatrace Community
- Tooltip

---

## ChoroplethLayer

`/design/data-visualizations/geo-maps/ChoroplethLayer/`

The `ChoroplethLayer` component allows users to display divided geographical
areas or regions that are coloured in relation to a given data. It provides an
easy way to visualize how a variable varies across a geographic area or show the
level of variability within a region.

OverviewProperties

### Import

`tsx
import { ChoroplethLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `ChoroplethLayer` subcomponent to apply color to a specific region. The
`ChoroplethLayer` subcomponent accepts an array of data entries as the `data`
prop. Each entry must contain an ISO 3166-2 region code.

You can use the `regionAccessor` prop to access the region where the color needs
to be applied. This can be either a string in the form of a value accessor or a
callback to dynamically construct the region code.

`tsx
[ { country: 'DE', color: '#f7c910', population: 84724070, }, { country: 'AU', color: '#012066', population: 26473055, }, { country: 'BR', color: '#029639', population: 218689752, },];
`

Learn more about the data format here.

#### Tooltip

Finally, when hovering a region in the `ChoroplethLayer`, the tooltip will
output the region `name`, the `color` and all the additional custom props inside
a `data` object.

#### Coloring

The `ChoroplethLayer` supports two ways of color configuration: granular
configuration using the `color` prop, or using a one of the available legend
subcomponents (e.g. `SequentialLegend`, `ThresholdLegend`, or
`CategoricalLegend`).

Note: Detailed information about coloring can be found in the `MapView`
documentation page under the `Coloring` section.

##### Granular color configuration

For a granular color customization, layer's `color` prop should be used.

###### Custom color applied on singular country state

This type of display can be done by providing country/state array for `include`
and `exclude` props in `BaseLayer` component

##### Coloring countries and regions

##### Color configuration using a legend

To connect a data layer to the legend, a `color` property of the layer should be
set to `legend` string.

###### Sequential legend

###### Threshold legend

###### Categorical legend

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Tooltip
- Coloring

### Props

The `ChoroplethLayer` component allows users to display divided geographical
areas or regions that are coloured in relation to a given data. It provides an
easy way to visualize how a variable varies across a geographic area or show the
level of variability within a region.

OverviewProperties

### ChoroplethLayer

#### ChoroplethLayerProps

##### Signature:
`export declare type ChoroplethLayerProps> = & ( | );`

#### ChoroplethLayerBaseProps
extends |
 | Name | Type | Default | Description
 | `data` | T[] | | An array of data items representing regions to be displayed in the ChoroplethLayer
 | `regionAccessor` | | ((t: T) => ) | | A string property or accessor function that specifies how to access the region identifier from the data items.
It can be a string representing the key in the data object or a function that extracts the region identifier

#### ChoroplethCustomColorProps
 |
 | Name | Type | Default | Description
 | `color?` | | ((item: T) => ) | | Color to apply to the layer

#### LegendColorLayerProps
 |
 | Name | Type | Default | Description
 | `color` | | | When the color prop is set to 'legend', a value accessor is needed
 | `valueAccessor` | | | The value accessor to map data point values to legend color

### Tooltip

#### ChoroplethLayerTooltipData
 |
 | Name | Type | Default | Description
 | `color` | | | The hovered region color
 | `name` | | | The hovered region name
 | `data` | T | | The hovered region custom data
 | `seriesActions?` | (data: ) => | | Series actions callback for the default tooltip

#### ChoroplethLayerTooltipHandler

##### Signature:
`export declare type ChoroplethLayerTooltipHandler = (regionData: ) => ;`

#### ChoroplethLayerTooltipHandlerProps
 |
 | Name | Type | Default | Description
 | `children?` | | | | The ChoroplethLayer tooltip handler template
 | `seriesActions?` | (data: ) => | | Series actions callback for the default tooltipStill have questions?Find answers in the Dynatrace Community
- Tooltip

---

## ConnectionLayer

`/design/data-visualizations/geo-maps/ConnectionLayer/`

The `ConnectionLayer` component renders connections between points on a map,
accepting an array of `Connection` data points with required properties like
latitude and longitude. It supports customization of color, thickness, direction
the connection indicators.

OverviewProperties

### Import

`tsx
import { ConnectionLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `ConnectionLayer` to visually represent connections between points on a
world map. The `ConnectionLayer` subcomponent requires an array of `Connection`
objects as its data prop.

Each `Connection` object must contain at least one `path`, which is defined by
an array of data points. Each data point must have at least `latitude` and
`longitude`.

The `ConnectionLayer` automatically connects the points in the paths with lines.
It's commonly used to depict networks combined with geographical data, flight
connections, or any type of connection between different locations.

`tsx
[ { path: [ { name: 'Tangier', latitude: 35.76727, longitude: -5.79975, }, { name: 'Nantes', latitude: 47.218102, longitude: -1.5528, }, ], }, { path: [ { name: 'Barcelona', latitude: 41.3828939, longitude: 2.1774322, }, { name: 'Vienna', latitude: 48.2083537, longitude: 16.3725042, }, ], },];
`

Learn more about the data format here.

#### Customize connection styling

Each `ConnectionLayer` exposes some additional properties as `line` and
`connectionIndicator` to customize the layer's styling.

To alter the `color`, the `thickness`, or any of the other styles of a specific
`Connection` you can utilize the corresponding props.

It is also possible to modify the way the connection is displayed, to do this,
use the `curve` parameter, which allows two values `line` or `smooth`.

### Tooltip

The `Connection Layer` provides a tooltip that displays additional information
about the connected points, when hovering over a connection.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Customize connection styling
- Tooltip

### Props

The `ConnectionLayer` component renders connections between points on a map,
accepting an array of `Connection` data points with required properties like
latitude and longitude. It supports customization of color, thickness, direction
the connection indicators.

OverviewProperties

### ConnectionLayer

#### ConnectionLayerProps

##### Signature:
`export declare type LayerProps = & ( | );`

#### Connection

##### Signature:
`export declare type Connection = {
 /** Array of connections */
 path: [];
};` |
 | Name | Type | Default | Description
 | `path` | [] | | Array of connections

#### Location
 |
 | Name | Type | Default | Description
 | `latitude` | | | The latitude coordinate of the location.
 | `longitude` | | | The longitude coordinate of the location.

#### CurvedLine

##### Signature:
`export declare type CurvedLine = | ;`

### Tooltip

#### ConnectionLayerTooltipData
 |
 | Name | Type | Default | Description
 | `color` | | | The hovered connection color
 | `thickness` | | | The hovered connection thickness
 | `data` | T | | The hovered connection custom data and path locations

#### ConnectionLayerTooltipHandler

##### Signature:
`export declare type ConnectionLayerTooltipHandler = (connectionData: ) => ;`

#### ConnectionLayerTooltipHandlerProps
 |
 | Name | Type | Default | Description
 | `children?` | | | | The ConnectionLayer tooltip handler template
 | `seriesActions?` | (data: ) => | | Series actions callback for the default tooltipStill have questions?Find answers in the Dynatrace Community
- Tooltip

---

## DotLayer

`/design/data-visualizations/geo-maps/DotLayer/`

The `DotLayer` component renders data points on a map, accepting an array of
data points with required properties like latitude and longitude. It provides
support for various shapes, optional features like custom background for icons,
rotation, and tooltips, along with granular color customization and integration
with legends for color configuration.

OverviewProperties

### Import

`tsx
import { DotLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `DotLayer` component to render data points as dots or simple shapes. The
component accepts an array of data points as the data prop. Each data point must
have `latitude` and `longitude` properties as the bare minimum.

`tsx
[ { name: 'Vienna International Airport', latitude: 48.1049967, longitude: 16.5848987, }, { name: 'Barcelona El Prat Josep Tarradellas Airport', latitude: 41.2969439, longitude: 2.0790474, },];
`

Learn more about the data format here.

#### Data point shapes and sizes

The `DotLayer` component supports various shapes for the data points using the
`shape` prop. The supported shapes are `circle`, `square`, `diamondheart`,
`cross`, `star`, `triangle` and `pin`. The default shape is `pin`. The pin act
as a location marker and the tip of the pin will be placed at the location of
the datapoint, instead of the center.

The size of the shape can be adjusted using the `shapeSize` prop, which receives
a number (in pixels) as a value. The default shape size is 32 pixels.

Additionally, emojis, single character strings, and Strato icons are supported
as data point shapes.

Note: Strato icons must be imported from `@dynatrace/strato-icons` namespace.

#### Icon background

The `DotLayer` component provides an optional feature to include a background
for the rendered data points' icons. This feature enhances the visual
representation of the data points on the map.

To enable the optional icon background, use the `background` prop when defining
the `DotLayer`. The `background` prop can take a boolean, a string, or a
callback function:

- If set to `false`, the icon background feature is disabled for the `DotLayer`
and the default background is only shown on a data point hover.

- If set to `true`, the background color is visible without hovering, and the
default background color is applied.

- If a string is provided, the feature is enabled with a custom background color
specified by the CSS string or color token.

- When a callback function is provided, the function should return a string that
specifies the background color for each data point.

#### Bearing

The `DotLayer` component supports rotation of the data points using the
`bearing` prop. The `bearing` prop accepts a number or a callback that returns a
number. The bearing number can between 0 and 360. The default value is 0.

#### Tooltip

The `DotLayer` component has an optional tooltip that displays additional
information when hovering over data point.

By default, the tooltip will display the location information of the hovered
point, but
it can be heavily customized.

#### Coloring

The `DotLayer` supports two ways of color configuration: granular configuration
using the `color` prop, or using a one of the available legend subcomponents
(e.g. `SequentialLegend`, `ThresholdLegend`, or `CategoricalLegend`).

Note: Detailed information about coloring can be found in the `MapView`
documentation page under the `Coloring` section.

##### Granular color configuration

For a granular color customization, layer's `color` prop should be used.

##### Color configuration using a legend

To connect a data layer to the legend, a `color` property of the layer should be
set to `legend` string.

###### Sequential legend

###### Threshold legend

###### Categorical legend

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Data point shapes and sizes
- Icon background
- Bearing
- Tooltip
- Coloring

### Props

The `DotLayer` component renders data points on a map, accepting an array of
data points with required properties like latitude and longitude. It provides
support for various shapes, optional features like custom background for icons,
rotation, and tooltips, along with granular color customization and integration
with legends for color configuration.

OverviewProperties

### DotLayer

#### DotLayerProps

##### Signature:
`export declare type DotLayerProps = & ( | );`

#### DotLayerBaseProps
extends |
 | Name | Type | Default | Description
 | `data` | T[] | | An array of location data items to be displayed in the DotLayer
 | `shape?` | | | | `'pin'` | The shape of the dots
 | `bearing?` | | ((item: T) => ) | `0` | The bearing property, which determines the rotation angle of the dots.
It can be a constant number or a function that calculates the bearing based on the data item
 | `background?` | | | ((item: T) => ) | `false` | The background setting for the DotLayer.
As boolean, it toggles the visibility and sets a default color.
As string, it defines the background color.
 | `shapeSize?` | | `32` | The shapeSize property allows to edit the size of the shape, icon, emoji
or ReactNode passed to the shape property in pixels, minimum value is 1.

#### LocationColorProps
 |
 | Name | Type | Default | Description
 | `color?` | | ((item: T) => ) | | Custom color to apply to the layer

#### LegendColorLayerProps
 |
 | Name | Type | Default | Description
 | `color` | | | When the color prop is set to 'legend', a value accessor is needed
 | `valueAccessor` | | | The value accessor to map data point values to legend color

#### Location
 |
 | Name | Type | Default | Description
 | `latitude` | | | The latitude coordinate of the location.
 | `longitude` | | | The longitude coordinate of the location.

### Tooltip

#### DotLayerTooltipData
 |
 | Name | Type | Default | Description
 | `color` | | | The hovered dot color
 | `bearing` | | | The hovered dot bearing
 | `data` | T | | The hovered dot custom data and location

#### DotLayerTooltipHandler

##### Signature:
`export declare type DotLayerTooltipHandler = (dotData: ) => | ;`

#### DotLayerTooltipHandlerProps
 |
 | Name | Type | Default | Description
 | `children?` | | | | The DotLayer tooltip handler template
 | `seriesActions?` | (data: ) => | | Series actions callback for the default tooltipStill have questions?Find answers in the Dynatrace Community
- Tooltip

---

## MapView

`/design/data-visualizations/geo-maps/MapView/`

The `MapView` is a component that renders a map with various geospatial data
layers.

OverviewProperties

### Import

`tsx
import { MapView } from '@dynatrace/strato-geo';
`

### Use cases

The minimal representation of a `MapView` component is a base layer that
contains a world map.

The height of the `MapView` component must be set explicitly using the `height`
prop. The width of the `MapView` component will be determined by the width of
the parent container.

Learn more about the `MapView` props here.

#### Formatter

There are two other options in the formatter that allow for greater
customization. The first option enables you to prepend the unit to the value,
while the second option enables you to ignore the original unit and append a
custom string instead. Additionally, there is a custom formatter option
available to allow you to change the input unit to one of your choice, e.g.: if
the input unit is `bits`, you are able to switch and display the unit as
`bytes`, correctly formatted. The formatted value is applied in the tooltip and
the legend.

#### Truncation mode

The purpose of truncation is to gracefully handle extra long tooltips or legends
within data visualization components. By changing the value of this property,
you have control over where truncation is applied within charts. By default, the
truncation is applied to the `middle` value with the use of an ellipsis.
Truncation can, however be changed to instead be applied at the `start` or `end`
of data visualization component elements.

#### Controlled and uncontrolled states

The `MapView` component can be used in both controlled and uncontrolled states.
In the uncontrolled state it's possible to configure the initial longitude,
latitude and zoom level of the map using `initialViewState` prop. By default,
the map will be centered on the equator and zoomed out to show the whole world.

In the controlled state, user can attach state handlers to the `MapView`
component using the `onViewStateChange` prop, as well as dynamically change the
longitude, latitude and zoom level of the map.

#### Data layers

The `MapView` component supports rendering of data layers on the map using the
different subcomponents. Multiple data layers of the same type can be rendered.
The order of the data layers is determined by the order of the subcomponents of
the `MapView` component.

For detailed documentation about each data layer, please refer to the respective
docs pages.Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Formatter
- Truncation mode
- Controlled and uncontrolled states
- Data layers

### Props

The `MapView` is a component that renders a map with various geospatial data
layers.

OverviewProperties

### MapView

#### MapViewProps

##### Signature:
`export declare type MapViewProps = & ( | );`

#### MapViewBaseProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `mapStyle?` | | | Styles of maplibre to be overridden
 | `onViewStateChange?` | (viewState: ) => | | Callback to listen for the changes in the ViewState
 | `loading?` | | `false` | Set whether map is loading
 | `height?` | | | `400px` | The height of the chart. If a number is passed, it will be treated as px
 | `truncationMode?` | | `'middle'` | The truncation mode to be used as start, middle or end in the long legend
labels
 | `formatter?` | | | | Map View formatter options
 | `onContextLostError?` | () => | | Callback fired when the map context is lost.
Browsers have a limit of active WebGL canvas contexts.
The map will automatically show an error state, but this callback
allows consumers to perform additional actions (e.g., analytics, custom UI).

#### MapViewControlledProps
extends

#### MapViewUncontrolledProps
extends`<>` |
 | Name | Type | Default | Description
 | `initialViewState?` | | | The initial state of the Map.

#### ViewState
 |
 | Name | Type | Default | Description
 | `longitude?` | | | Longitude at map center
 | `latitude?` | | | Latitude at map center
 | `zoom?` | | | Map zoom level

### MapView Ref

#### MapViewRef
 |
 | Name | Type | Default | Description
 | `element` | | | | The map component root element
 | `downloadData` | () => | | Downloads map raw data .
 | `zoomIn` | () => | | Performs zoom in action on the domain
 | `zoomOut` | () => | | Performs zoom out action on the domain
 | `zoomToFit` | () => | | Performs zoom to fit action on the domain
 | `reset` | () => | | Reset the domain to the default

### Sequential legend

#### SequentialLegendProps
extends |
 | Name | Type | Default | Description
 | `min?` | | | The min boundary
 | `max?` | | | The max boundary
 | `colorPalette?` | [] | | | The color palette to apply to the legend

#### BaseLegendProps

##### Signature:
`export declare type Base = ;`

#### LegendPosition

##### Signature:
`export declare type LegendPosition = (typeof )[];`

#### ColorPalette

##### Signature:
`export declare type ColorPalette = (typeof )[];`

### Threshold legend

#### ThresholdLegendProps
extends |
 | Name | Type | Default | Description
 | `ranges` | [] | | Ranges of the threshold legend

#### BaseLegendProps

##### Signature:
`export declare type Base = ;`

#### LegendPosition

##### Signature:
`export declare type LegendPosition = (typeof )[];`

#### ColorPalette

##### Signature:
`export declare type ColorPalette = (typeof )[];`

#### ColoredRange
 |
 | Name | Type | Default | Description
 | `from` | | | Range starting point
 | `to` | | | Range ending point
 | `color?` | | | The color to use in this range

### Categorical legend

#### CategoricalLegendProps
extends |
 | Name | Type | Default | Description
 | `colorPalette` | [] | | {
 [key: ]: ;
 } | | The color palette to apply to the legend

#### BaseLegendProps

##### Signature:
`export declare type Base = ;`

#### LegendPosition

##### Signature:
`export declare type LegendPosition = (typeof )[];`

#### ColorPalette

##### Signature:
`export declare type ColorPalette = (typeof )[];`

### Legend shared props

#### BaseLegendProps

##### Signature:
`export declare type Base = ;`

### Interactions

#### ChartInteractionsProps
 |
 | Name | Type | Default | Description
 | `onZoomChange?` | | | Callback called when any zoom event has been performed affecting the data timeframe

#### ZoomChangeHandler

##### Signature:
`export declare type ZoomChangeHandler = (newStart: | , newEnd: | , type: ) => ;`

### Toolbar

#### ChartToolbarProps
 |
 | Name | Type | Default | Description
 | `placement?` | | `'top-right'` | Initial placement for the toolbar

#### ToolbarPlacement

##### Signature:
`export declare type ToolbarPlacement = | | | ;`Still have questions?Find answers in the Dynatrace Community
- MapView Ref
- Sequential legend
- Threshold legend
- Categorical legend
- Legend shared props
- Interactions
- Toolbar

---

