## Align

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/nodes.ts#L174)

The `Align` type contains the values expected by the `align` prop of the [NodeToolbar](https://reactflow.dev/api-reference/components/node-toolbar) component

```ts
export type Align = 'center' | 'start' | 'end';
```

## AriaLabelConfig

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/constants.ts/)

With the `AriaLabelConfig` you can customize the aria labels used by React Flow. This is useful if you want to translate the labels or if you want to change them to better suit your application.

### Fields

* `node.a11yDescription.default: string`
* `node.a11yDescription.keyboardDisabled: string`
* `node.a11yDescription.ariaLiveMessage: ({ direction, x, y }: { direction: string; x: number; y: number; }) => string`
* `edge.a11yDescription.default: string`
* `controls.ariaLabel: string`
* `controls.zoomIn.ariaLabel: string`
* `controls.zoomOut.ariaLabel: string`
* `controls.fitView.ariaLabel: string`
* `controls.interactive.ariaLabel: string`
* `minimap.ariaLabel: string`
* `handle.ariaLabel: string`

### Default config

```js
const defaultAriaLabelConfig = {
  'node.a11yDescription.default':
    'Press enter or space to select a node. Press delete to remove it and escape to cancel.',
  'node.a11yDescription.keyboardDisabled':
    'Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.',
  'node.a11yDescription.ariaLiveMessage': ({ direction, x, y }: { direction: string; x: number; y: number }) =>
    `Moved selected node ${direction}. New position, x: ${x}, y: ${y}`,
  'edge.a11yDescription.default':
    'Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.',

  // Control elements
  'controls.ariaLabel': 'Control Panel',
  'controls.zoomIn.ariaLabel': 'Zoom In',
  'controls.zoomOut.ariaLabel': 'Zoom Out',
  'controls.fitView.ariaLabel': 'Fit View',
  'controls.interactive.ariaLabel': 'Toggle Interactivity',

  // Mini map
  'minimap.ariaLabel': 'Mini Map',

  // Handle
  'handle.ariaLabel': 'Handle',
};
```

## BackgroundVariant

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/Background/types.ts)

The three variants are exported as an enum for convenience. You can either import
the enum and use it like `BackgroundVariant.Lines` or you can use the raw string
value directly.

```ts
export enum BackgroundVariant {
  Lines = 'lines',
  Dots = 'dots',
  Cross = 'cross',
}
```

## ColorMode

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts)

The `ColorMode` type defines the available color modes for the ReactFlow component. This can be used to control the theme of the flow diagram.

```ts
export type ColorMode = 'light' | 'dark' | 'system';
```

## ConnectionLineComponentProps

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts/#L193)

If you want to render a custom component for connection lines, you can set the
`connectionLineComponent` prop on the
[`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow#connection-connectionLineComponent) component.
The `ConnectionLineComponentProps` are passed to your custom component.

### Props

If you want to render a custom component for connection lines, you can set the
`connectionLineComponent` prop on the [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow#connection-connectionLineComponent)
component. The `ConnectionLineComponentProps` are passed to your custom component.

* `connectionLineStyle?: CSSProperties`
* `connectionLineType: ConnectionLineType`
* `fromNode: InternalNode<NodeType>` The node the connection line originates from.
* `fromHandle: Handle` The handle on the `fromNode` that the connection line originates from.
* `fromX: number`
* `fromY: number`
* `toX: number`
* `toY: number`
* `fromPosition: Position`
* `toPosition: Position`
* `connectionStatus: "valid" | "invalid" | null` If there is an `isValidConnection` callback, this prop will be set to `"valid"` or `"invalid"`
  based on the return value of that callback. Otherwise, it will be `null`.
* `toNode: InternalNode<NodeType> | null`
* `toHandle: Handle | null`
* `pointer: XYPosition`

## ConnectionLineComponent

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts#L265)

The `ConnectionLineComponent` type allows you to provide a custom React component to render the connection line when users create new edges. The component receives `ConnectionLineComponentProps` as its props.

```ts
type ConnectionLineComponent = React.ComponentType<ConnectionLineComponentProps>;
```

## ConnectionLineType

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/edges.ts/#L62)

If you set the `connectionLineType` prop on your [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow#connection-connectionLineType)
component, it will dictate the style of connection line rendered when creating
new edges.

```ts
export enum ConnectionLineType {
  Bezier = 'default',
  Straight = 'straight',
  Step = 'step',
  SmoothStep = 'smoothstep',
  SimpleBezier = 'simplebezier',
}
```

### Notes

* If you choose to render a custom connection line component, this value will be
  passed to your component as part of its [`ConnectionLineComponentProps`](https://reactflow.dev/api-reference/types/connection-line-component-props).

## ConnectionMode

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L68)

The `ConnectionMode` enum provides two options for connection behavior in React Flow:

* `Strict`: Connections can only be made starting from a source handle and ending on a target handle
* `Loose`: Connections can be made between any handles, regardless of type

```ts
enum ConnectionMode {
  Strict = 'strict',
  Loose = 'loose',
}
```

## ConnectionState

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts/#L148-L174)

The `ConnectionState` type bundles all information about an ongoing connection. It is returned by the [`useConnection`](https://reactflow.dev/api-reference/hooks/use-connection) hook.

```ts
type NoConnection = {
  inProgress: false;
  isValid: null;
  from: null;
  fromHandle: null;
  fromPosition: null;
  fromNode: null;
  to: null;
  toHandle: null;
  toPosition: null;
  toNode: null;
};
type ConnectionInProgress = {
  inProgress: true;
  isValid: boolean | null;
  from: XYPosition;
  fromHandle: Handle;
  fromPosition: Position;
  fromNode: NodeBase;
  to: XYPosition;
  toHandle: Handle | null;
  toPosition: Position;
  toNode: NodeBase | null;
};

type ConnectionState = ConnectionInProgress | NoConnection;
```

### Fields

The `ConnectionState` type bundles all information about an ongoing connection.
It is returned by the [`useConnection`](https://reactflow.dev/api-reference/hooks/use-connection) hook.

* `inProgress: boolean` Indicates whether a connection is currently in progress.
* `isValid: boolean | null` If an ongoing connection is above a handle or inside the connection radius, this will be `true`
  or `false`, otherwise `null`.
* `from: XYPosition | null` Returns the xy start position or `null` if no connection is in progress.
* `fromHandle: Handle | null` Returns the start handle or `null` if no connection is in progress.
* `fromPosition: Position | null` Returns the side (called position) of the start handle or `null` if no connection is in progress.
* `fromNode: NodeType | null` Returns the start node or `null` if no connection is in progress.
* `to: XYPosition | null` Returns the xy end position or `null` if no connection is in progress.
* `toHandle: Handle | null` Returns the end handle or `null` if no connection is in progress.
* `toPosition: Position | null` Returns the side (called position) of the end handle or `null` if no connection is in progress.
* `toNode: NodeType | null` Returns the end node or `null` if no connection is in progress.
* `pointer: XYPosition | null` Returns the pointer position or `null` if no connection is in progress.

## Connection

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts/#L29-L34)

The `Connection` type is the basic minimal description of an
[`Edge`](https://reactflow.dev/api-reference/types/edge) between two nodes. The
[`addEdge`](https://reactflow.dev/api-reference/utils/add-edge) util can be used to upgrade a `Connection` to
an [`Edge`](https://reactflow.dev/api-reference/types/edge).

### Fields

The `Connection` type is the basic minimal description of an [`Edge`](https://reactflow.dev/api-reference/types/edge)
between two nodes. The [`addEdge`](https://reactflow.dev/api-reference/utils/add-edge) util can be used to upgrade
a `Connection` to an [`Edge`](https://reactflow.dev/api-reference/types/edge).

* `source: string` The id of the node this connection originates from.
* `target: string` The id of the node this connection terminates at.
* `sourceHandle: string | null` When not `null`, the id of the handle on the source node that this connection originates from.
* `targetHandle: string | null` When not `null`, the id of the handle on the target node that this connection terminates at.

## CoordinateExtent

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/utils.ts/#L36-L37)

A coordinate extent represents two points in a coordinate system: one in the top
left corner and one in the bottom right corner. It is used to represent the
bounds of nodes in the flow or the bounds of the viewport.

```ts
export type CoordinateExtent = [[number, number], [number, number]];
```

### Notes

* Props that expect a `CoordinateExtent` usually default to `[[-∞, -∞], [+∞, +∞]]`
  to represent an unbounded extent.

## DefaultEdgeOptions

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts/#L88-L89)

Many properties on an [`Edge`](https://reactflow.dev/api-reference/types/edge) are optional. When a new edge is
created, the properties that are not provided will be filled in with the default values
passed to the `defaultEdgeOptions` prop of the
[`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow#defaultedgeoptions) component.

### Fields

Many properties on an [`Edge`](https://reactflow.dev/api-reference/types/edge) are optional. When a new edge is created,
the properties that are not provided will be filled in with the default values
passed to the `defaultEdgeOptions` prop of the [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow#defaultedgeoptions) component.

* `type?: string | undefined` Type of edge defined in `edgeTypes`.
* `animated?: boolean`
* `hidden?: boolean`
* `deletable?: boolean`
* `selectable?: boolean`
* `data?: Record<string, unknown>` Arbitrary data passed to an edge.
* `markerStart?: EdgeMarkerType` Set the marker on the beginning of an edge.
* `markerEnd?: EdgeMarkerType` Set the marker on the end of an edge.
* `zIndex?: number`
* `ariaLabel?: string`
* `interactionWidth?: number` ReactFlow renders an invisible path around each edge to make them easier to click or tap on.
  This property sets the width of that invisible path.
* `label?: ReactNode` The label or custom element to render along the edge. This is commonly a text label or some
  custom controls.
* `labelStyle?: CSSProperties` Custom styles to apply to the label.
* `labelShowBg?: boolean`
* `labelBgStyle?: CSSProperties`
* `labelBgPadding?: [number, number]`
* `labelBgBorderRadius?: number`
* `style?: CSSProperties`
* `className?: string`
* `reconnectable?: boolean | HandleType` Determines whether the edge can be updated by dragging the source or target to a new node.
  This property will override the default set by the `edgesReconnectable` prop on the
  `<ReactFlow />` component.
* `focusable?: boolean`
* `ariaRole?: AriaRole` The ARIA role attribute for the edge, used for accessibility.
* `domAttributes?: Omit<SVGAttributes<SVGGElement>, "id" | "style" | "className" | "role" | "aria-label" | "dangerouslySetInnerHTML">` General escape hatch for adding custom attributes to the edge's DOM element.

## DeleteElements

DeleteElements deletes provided nodes and edges and handles deleting any connected edges as well as child nodes. Returns successfully deleted edges and nodes asynchronously.

```ts
export type DeleteElements = (payload: {
  nodes?: (Partial<Node> & { id: Node['id'] })[];
  edges?: (Partial<Edge> & { id: Edge['id'] })[];
}) => Promise<{
  deletedNodes: Node[];
  deletedEdges: Edge[];
}>;
```

## EdgeChange

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/changes.ts/#L68-L72)

The [`onEdgesChange`](https://reactflow.dev/api-reference/react-flow#on-edges-change) callback takes
an array of `EdgeChange` objects that you should use to update your flow's state.
The `EdgeChange` type is a union of four different object types that represent that
various ways an edge can change in a flow.

```ts
export type EdgeChange =
  | EdgeAddChange
  | EdgeRemoveChange
  | EdgeReplaceChange
  | EdgeSelectionChange;
```

### Variants

#### EdgeAddChange

* `item: EdgeType`
* `type: "add"`
* `index?: number`

#### EdgeRemoveChange

* `id: string`
* `type: "remove"`

#### EdgeReplaceChange

* `id: string`
* `item: EdgeType`
* `type: "replace"`

#### EdgeSelectionChange

* `id: string`
* `type: "select"`
* `selected: boolean`

## EdgeMarker

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/edges.ts/#L70-L78)

Edges can optionally have markers at the start and end of an edge. The `EdgeMarker` type
is used to configure those markers! Check the docs for
[`MarkerType`](https://reactflow.dev/api-reference/types/marker-type) for details on what types of edge marker
are available.

### Fields

Edges can optionally have markers at the start and end of an edge. The `EdgeMarker`
type is used to configure those markers! Check the docs for [`MarkerType`](https://reactflow.dev/api-reference/types/marker-type)
for details on what types of edge marker are available.

* `type: MarkerType | "arrow" | "arrowclosed"`
* `color?: string | null`
* `width?: number`
* `height?: number`
* `markerUnits?: string`
* `orient?: string`
* `strokeWidth?: number`

## EdgeMouseHandler

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts#L81)

The `EdgeMouseHandler` type defines the callback function that is called when mouse events occur on an edge. This callback receives the event and the edge that triggered it.

```ts
type EdgeMouseHandler = (event: React.MouseEvent, edge: Edge) => void;
```

##### Parameters

* `event: MouseEvent<Element, MouseEvent>`
* `edge: EdgeType`

##### Returns

`void`

## EdgeProps

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts/#L100)

When you implement a custom edge it is wrapped in a component that enables some basic
functionality. The `EdgeProps` type takes a generic parameter to specify the type of edges
you use in your application:

```ts
type AppEdgeProps = EdgeProps<MyEdgeType>;
```

Your custom edge component receives the following props:

### Fields

When you implement a custom edge it is wrapped in a component that enables some
basic functionality. The `EdgeProps` type is the props that are passed to this.

* `id: EdgeType["id"]` Unique id of an edge.
* `type?: EdgeType["type"]` Type of edge defined in `edgeTypes`.
* `animated?: EdgeType["animated"]`
* `data?: EdgeType["data"]` Arbitrary data passed to an edge.
* `style?: EdgeType["style"]`
* `selected?: EdgeType["selected"]`
* `source: EdgeType["source"]` Id of source node.
* `target: EdgeType["target"]` Id of target node.
* `selectable?: EdgeType["selectable"]`
* `deletable?: EdgeType["deletable"]`
* `sourceX: number`
* `sourceY: number`
* `targetX: number`
* `targetY: number`
* `sourcePosition: Position`
* `targetPosition: Position`
* `label?: ReactNode` The label or custom element to render along the edge. This is commonly a text label or some
  custom controls.
* `labelStyle?: CSSProperties` Custom styles to apply to the label.
* `labelShowBg?: boolean`
* `labelBgStyle?: CSSProperties`
* `labelBgPadding?: [number, number]`
* `labelBgBorderRadius?: number`
* `sourceHandleId?: string | null`
* `targetHandleId?: string | null`
* `markerStart?: string`
* `markerEnd?: string`
* `pathOptions?: any`
* `interactionWidth?: number`

## EdgeTypes

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts#L76)

The `EdgeTypes` type is used to define custom edge types. Each key in the object represents an edge type, and the value is the component that should be rendered for that type.

```ts
export type EdgeTypes = {
  [key: string]: React.ComponentType<EdgeProps>;
};
```

## Edge

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts/#L34-L353)

Where a [`Connection`](https://reactflow.dev/api-reference/types/connection) is the minimal description of an edge between
two nodes, an `Edge` is the complete description with everything React Flow needs
to know in order to render it.

```ts
export type Edge<T> = DefaultEdge<T> | SmoothStepEdge<T> | BezierEdge<T>;
```

### Variants

#### Edge

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts/#L34-L353)

An `Edge` is the complete description with everything React Flow needs
to know in order to render it.

* `id: string` Unique id of an edge.
* `type?: EdgeType` Type of edge defined in `edgeTypes`.
* `source: string` Id of source node.
* `target: string` Id of target node.
* `sourceHandle?: string | null` Id of source handle, only needed if there are multiple handles per node.
* `targetHandle?: string | null` Id of target handle, only needed if there are multiple handles per node.
* `animated?: boolean`
* `hidden?: boolean`
* `deletable?: boolean`
* `selectable?: boolean`
* `data?: EdgeData` Arbitrary data passed to an edge.
* `selected?: boolean`
* `markerStart?: EdgeMarkerType` Set the marker on the beginning of an edge.
* `markerEnd?: EdgeMarkerType` Set the marker on the end of an edge.
* `zIndex?: number`
* `ariaLabel?: string`
* `interactionWidth?: number` ReactFlow renders an invisible path around each edge to make them easier to click or tap on.
  This property sets the width of that invisible path.
* `label?: ReactNode` The label or custom element to render along the edge. This is commonly a text label or some
  custom controls.
* `labelStyle?: CSSProperties` Custom styles to apply to the label.
* `labelShowBg?: boolean`
* `labelBgStyle?: CSSProperties`
* `labelBgPadding?: [number, number]`
* `labelBgBorderRadius?: number`
* `style?: CSSProperties`
* `className?: string`
* `reconnectable?: boolean | HandleType` Determines whether the edge can be updated by dragging the source or target to a new node.
  This property will override the default set by the `edgesReconnectable` prop on the
  `<ReactFlow />` component.
* `focusable?: boolean`
* `ariaRole?: AriaRole` The ARIA role attribute for the edge, used for accessibility.
* `domAttributes?: Omit<SVGAttributes<SVGGElement>, "id" | "style" | "className" | "role" | "aria-label" | "dangerouslySetInnerHTML">` General escape hatch for adding custom attributes to the edge's DOM element.

#### SmoothStepEdge

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts/#L45-L46)

The `SmoothStepEdge` variant has all the same fields as an `Edge`, but it also has the following additional fields:

{/\* type SmoothStepEdge isn't exported, and conflicts with SmoothStepEdge component name \*/}
\[APIDocs: missing componentName, functionName, or typeName]

#### BezierEdge

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/edges.ts/#L52-L53)

The `BezierEdge` variant has all the same fields as an `Edge`, but it also has the following additional fields:

{/\* type BezierEdge isn't exported, and conflicts with BezierEdge component name \*/}
\[APIDocs: missing componentName, functionName, or typeName]

### Default edge types

You can create any of React Flow's default edges by setting the `type` property
to one of the following values:

* `"default"`
* `"straight"`
* `"step"`
* `"smoothstep"`
* `"simplebezier"`

If you don't set the `type` property at all, React Flow will fallback to the
`"default"` bezier curve edge type.

These default edges are available even if you set the [`edgeTypes`](https://reactflow.dev/api-reference/react-flow#edge-types)
prop to something else, unless you override any of these keys directly.

## FitViewOptions

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts/#L67-L68)

When calling [`fitView`](https://reactflow.dev/api-reference/types/react-flow-instance#fitview) these options
can be used to customize the behavior. For example, the `duration` option can be used to
transform the viewport smoothly over a given amount of time.

### Fields

When calling [`fitView`](https://reactflow.dev/api-reference/types/react-flow-instance#fitview) these options
can be used to customize the behaviour. For example, the `duration` option can be used to
transform the viewport smoothly over a given amount of time.

* `padding?: Padding`
* `includeHiddenNodes?: boolean`
* `minZoom?: number`
* `maxZoom?: number`
* `duration?: number`
* `ease?: (t: number) => number`
* `interpolate?: "smooth" | "linear"`
* `nodes?: (NodeType | { id: string; })[]`

## HandleConnection

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts/#L36-L37)

The `HandleConnection` type is an extension of a basic
[Connection](https://reactflow.dev/api-reference/types/connection) that includes the `edgeId`.

### Fields

The `HandleConnection` type is an extension of a basic [Connection](https://reactflow.dev/api-reference/types/connection) that includes the `edgeId`.

* `source: string` The id of the node this connection originates from.
* `target: string` The id of the node this connection terminates at.
* `sourceHandle: string | null` When not `null`, the id of the handle on the source node that this connection originates from.
* `targetHandle: string | null` When not `null`, the id of the handle on the target node that this connection terminates at.
* `edgeId: string`

## Handle

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/handles.ts/#L5)

The `Handle` type represents the attributes of a handle.

### Fields

* `id?: string | null`
* `nodeId: string`
* `x: number`
* `y: number`
* `position: Position`
* `type: 'source' | 'target'`
* `width: number`
* `height: number`

## InternalNode

[Source on GitHub](https://github.com/xyflow/xyflow/blob/99985b52026cf4ac65a1033178cf8c2bea4e14fa/packages/system/src/types/nodes.ts#L68)

The `InternalNode` type is identical to the base [`Node`](https://reactflow.dev/api-reference/types/node) type
but is extended with some additional properties used internally by React Flow. Some
functions and callbacks that return nodes may return an `InternalNode`.

### Fields

* `width?: NodeType["width"]`
* `height?: NodeType["height"]`
* `id: NodeType["id"]` Unique id of a node.
* `position: NodeType["position"]` Position of a node on the pane.
* `type?: NodeType["type"]` Type of node defined in nodeTypes
* `data: NodeType["data"]` Arbitrary data passed to a node.
* `sourcePosition?: NodeType["sourcePosition"]` Only relevant for default, source, target nodeType. Controls source position.
* `targetPosition?: NodeType["targetPosition"]` Only relevant for default, source, target nodeType. Controls target position.
* `hidden?: NodeType["hidden"]` Whether or not the node should be visible on the canvas.
* `selected?: NodeType["selected"]`
* `dragging?: NodeType["dragging"]` Whether or not the node is currently being dragged.
* `draggable?: NodeType["draggable"]` Whether or not the node is able to be dragged.
* `selectable?: NodeType["selectable"]`
* `connectable?: NodeType["connectable"]`
* `deletable?: NodeType["deletable"]`
* `dragHandle?: NodeType["dragHandle"]` A class name that can be applied to elements inside the node that allows those elements to act
  as drag handles, letting the user drag the node by clicking and dragging on those elements.
* `initialWidth?: NodeType["initialWidth"]`
* `initialHeight?: NodeType["initialHeight"]`
* `parentId?: NodeType["parentId"]` Parent node id, used for creating sub-flows.
* `zIndex?: NodeType["zIndex"]`
* `extent?: NodeType["extent"]` Boundary a node can be moved in.
* `expandParent?: NodeType["expandParent"]` When `true`, the parent node will automatically expand if this node is dragged to the edge of
  the parent node's bounds.
* `ariaLabel?: NodeType["ariaLabel"]`
* `origin?: NodeType["origin"]` Origin of the node relative to its position.
* `handles?: NodeType["handles"]`
* `measured: { width?: number; height?: number; }`
* `internals: { positionAbsolute: XYPosition; z: number; rootParentIndex?: number; userNode: NodeType; handleBounds?: NodeHandleBounds; bounds?: NodeBounds; }`

## IsValidConnection

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts#L212)

The `IsValidConnection` type represents a function that validates whether a connection between nodes is allowed. It receives a [`Connection`](https://reactflow.dev/api-reference/types/connection) and returns a boolean indicating whether the connection is valid and therefore should be created.

```ts
type IsValidConnection = (edge: Edge | Connection) => boolean;
```

This type can be used to type the `isValidConnection` function.
If the function returns `true`, the connection is valid and can be created.

##### Parameters

* `edge: EdgeType | Connection`

##### Returns

`boolean`

## KeyCode

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L155)

The `KeyCode` type is used to specify keyboard key codes or combinations, such as deleting nodes or enabling multi-selection. It can be a single string or an array of strings representing key codes.

```ts
type KeyCode = string | Array<string>;
```

## MarkerType

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/edges.ts/#L82-L83)

Edges may optionally have a marker on either end. The MarkerType type enumerates
the options available to you when configuring a given marker.

```ts
export enum MarkerType {
  Arrow = 'arrow',
  ArrowClosed = 'arrowclosed',
}
```

## MiniMapNodeProps

[Source on GitHub](https://github.com/xyflow/xyflow/blob/487b13c9ad8903789f56c6fcfd8222f9cb74b812/packages/react/src/additional-components/MiniMap/types.ts/#L60)

The MiniMapNodeProps type defines the props for nodes in the MiniMap component. This is
only relevant if you pass a custom node type to the MiniMap.

### Fields

The props that are passed to the MiniMapNode component

* `id: string`
* `x: number`
* `y: number`
* `width: number`
* `height: number`
* `borderRadius: number`
* `className: string`
* `color?: string`
* `shapeRendering: string`
* `strokeColor?: string`
* `strokeWidth?: number`
* `style?: CSSProperties`
* `selected: boolean`
* `onClick?: (event: MouseEvent<Element, MouseEvent>, id: string) => void`

```
```

## NodeChange

[Source on GitHub](https://github.com/xyflow/xyflow/blob/487b13c9ad8903789f56c6fcfd8222f9cb74b812/packages/system/src/types/changes.ts/#L47)

The [`onNodesChange`](https://reactflow.dev/api-reference/react-flow#on-nodes-change) callback takes
an array of `NodeChange` objects that you should use to update your flow's state.
The `NodeChange` type is a union of six different object types that represent that
various ways an node can change in a flow.

```ts
export type NodeChange =
  | NodeDimensionChange
  | NodePositionChange
  | NodeSelectionChange
  | NodeRemoveChange
  | NodeAddChange
  | NodeReplaceChange;
```

### Variant types

#### NodeDimensionChange

* `id: string`
* `type: "dimensions"`
* `dimensions?: Dimensions`
* `resizing?: boolean`
* `setAttributes?: boolean | "width" | "height"`

#### NodePositionChange

* `id: string`
* `type: "position"`
* `position?: XYPosition`
* `positionAbsolute?: XYPosition`
* `dragging?: boolean`

#### NodeSelectionChange

* `id: string`
* `type: "select"`
* `selected: boolean`

#### NodeRemoveChange

* `id: string`
* `type: "remove"`

#### NodeAddChange

* `item: NodeType`
* `type: "add"`
* `index?: number`

#### NodeReplaceChange

* `id: string`
* `item: NodeType`
* `type: "replace"`

## NodeConnection

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts/#L36-L37)

The `NodeConnection` type is an extension of a basic
[Connection](https://reactflow.dev/api-reference/types/connection) that includes the `edgeId`.

### Fields

The `NodeConnection` type is an extension of a basic [Connection](https://reactflow.dev/api-reference/types/connection) that includes the `edgeId`.

* `source: string` The id of the node this connection originates from.
* `target: string` The id of the node this connection terminates at.
* `sourceHandle: string | null` When not `null`, the id of the handle on the source node that this connection originates from.
* `targetHandle: string | null` When not `null`, the id of the handle on the target node that this connection terminates at.
* `edgeId: string`

## NodeHandle

[Source on GitHub](https://github.com/xyflow/xyflow/blob/13897512d3c57e72c2e27b14ffa129412289d948/packages/system/src/types/nodes.ts#L139)

The `NodeHandle` type is used to define a handle for a node if server-side rendering is used. On the server, React Flow can't measure DOM nodes, so it's necessary to define the handle position dimensions.

Type for the handles of a node

* `width?: number`
* `height?: number`
* `id?: string | null`
* `x: number`
* `y: number`
* `position: Position`
* `type: 'source' | 'target'`

## NodeMouseHandler

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/nodes.ts)

The `NodeMouseHandler` type defines the callback function that is called when mouse events
occur on a node. This callback receives the event and the node that triggered it.

```ts
export type NodeMouseHandler = (event: React.MouseEvent, node: Node) => void;
```

##### Parameters

* `event: MouseEvent<Element, MouseEvent>`
* `node: NodeType`

##### Returns

`void`

## NodeOrigin

The origin of a Node determines how it is placed relative to its own coordinates.
`[0, 0]` places it at the top left corner, `[0.5, 0.5]` right in the center and `[1, 1]` at the bottom right of its position.

```ts
export type NodeOrigin = [number, number];
```

## NodeProps

## NodeProps<T>

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/nodes.ts/#L89)

When you implement a [custom node](https://reactflow.dev/learn/customization/custom-nodes) it is wrapped in a
component that enables basic functionality like selection and dragging.

### Usage

```tsx
import { useState } from 'react';
import { NodeProps, Node } from '@xyflow/react';

export type CounterNode = Node<
  {
    initialCount?: number;
  },
  'counter'
>;

export default function CounterNode(props: NodeProps<CounterNode>) {
  const [count, setCount] = useState(props.data?.initialCount ?? 0);

  return (
    <div>
      <p>Count: {count}</p>
      <button className="nodrag" onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

Remember to register your custom node by adding it to the
[`nodeTypes`](https://reactflow.dev/api-reference/react-flow#nodetypes) prop of your `<ReactFlow />` component.

```tsx
import { ReactFlow } from '@xyflow/react';
import CounterNode from './CounterNode';

const nodeTypes = {
  counterNode: CounterNode,
};

export default function App() {
  return <ReactFlow nodeTypes={nodeTypes} ... />
}
```

You can read more in our [custom node guide](https://reactflow.dev/learn/customization/custom-nodes).

### Fields

Your custom node receives the following props:

When you implement a [custom node](https://reactflow.dev/learn/customization/custom-nodes) it is
wrapped in a component that enables basic functionality like selection and
dragging. Your custom node receives `NodeProps` as props.

* `id: NodeType["id"]` Unique id of a node.
* `data: NodeType["data"]` Arbitrary data passed to a node.
* `width?: NodeType["width"]`
* `height?: NodeType["height"]`
* `sourcePosition?: NodeType["sourcePosition"]` Only relevant for default, source, target nodeType. Controls source position.
* `targetPosition?: NodeType["targetPosition"]` Only relevant for default, source, target nodeType. Controls target position.
* `dragHandle?: NodeType["dragHandle"]` A class name that can be applied to elements inside the node that allows those elements to act
  as drag handles, letting the user drag the node by clicking and dragging on those elements.
* `parentId?: NodeType["parentId"]` Parent node id, used for creating sub-flows.
* `type: NodeType["type"]` Type of node defined in nodeTypes
* `dragging: NodeType["dragging"]` Whether or not the node is currently being dragged.
* `zIndex: NodeType["zIndex"]`
* `selectable: NodeType["selectable"]`
* `deletable: NodeType["deletable"]`
* `selected: NodeType["selected"]`
* `draggable: NodeType["draggable"]` Whether or not the node is able to be dragged.
* `isConnectable: boolean` Whether a node is connectable or not.
* `positionAbsoluteX: number` Position absolute x value.
* `positionAbsoluteY: number` Position absolute y value.

## NodeTypes

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/nodes.ts)

The `NodeTypes` type is used to define custom node types. Each key in the object represents a node type, and the value is the component that should be rendered for that type.

```ts
type NodeTypes = {
  [key: string]: React.ComponentType<NodeProps>;
};
```

## Node

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/nodes.ts/#L10)

The `Node` type represents everything React Flow needs to know about a given node.
Many of these properties can be manipulated both by React Flow or by you, but
some such as `width` and `height` should be considered read-only.

### Fields

The `Node` type represents everything React Flow needs to know about a given node.
Whenever you want to update a certain attribute of a node, you need to create a new
node object.

* `id: string` Unique id of a node.
* `position: XYPosition` Position of a node on the pane.
* `data: NodeData` Arbitrary data passed to a node.
* `sourcePosition?: Position` Only relevant for default, source, target nodeType. Controls source position.
* `targetPosition?: Position` Only relevant for default, source, target nodeType. Controls target position.
* `hidden?: boolean` Whether or not the node should be visible on the canvas.
* `selected?: boolean`
* `dragging?: boolean` Whether or not the node is currently being dragged.
* `draggable?: boolean` Whether or not the node is able to be dragged.
* `selectable?: boolean`
* `connectable?: boolean`
* `deletable?: boolean`
* `dragHandle?: string` A class name that can be applied to elements inside the node that allows those elements to act
  as drag handles, letting the user drag the node by clicking and dragging on those elements.
* `width?: number`
* `height?: number`
* `initialWidth?: number`
* `initialHeight?: number`
* `parentId?: string` Parent node id, used for creating sub-flows.
* `zIndex?: number`
* `extent?: CoordinateExtent | "parent" | null` Boundary a node can be moved in.
* `expandParent?: boolean` When `true`, the parent node will automatically expand if this node is dragged to the edge of
  the parent node's bounds.
* `ariaLabel?: string`
* `origin?: NodeOrigin` Origin of the node relative to its position.
* `handles?: NodeHandle[]`
* `measured?: { width?: number; height?: number; }`
* `type?: string | NodeType | (NodeType & undefined)` Type of node defined in nodeTypes
* `style?: CSSProperties`
* `className?: string`
* `resizing?: boolean`
* `focusable?: boolean`
* `ariaRole?: AriaRole` The ARIA role attribute for the node element, used for accessibility.
* `domAttributes?: Omit<HTMLAttributes<HTMLDivElement>, "id" | "draggable" | "style" | "className" | "role" | "aria-label" | "defaultValue" | keyof DOMAttributes<HTMLDivElement>>` General escape hatch for adding custom attributes to the node's DOM element.

### Default node types

You can create any of React Flow's default nodes by setting the `type` property
to one of the following values:

* `"default"`
* `"input"`
* `"output"`
* `"group"`

If you don't set the `type` property at all, React Flow will fallback to the
`"default"` node with both an input and output port.

These default nodes are available even if you set the [`nodeTypes`](https://reactflow.dev/api-reference/react-flow#node-types)
prop to something else, unless you override any of these keys directly.

### Notes

* You shouldn't try to set the `width` or `height` of a node directly. It is
  calculated internally by React Flow and used when rendering the node in the
  viewport. To control a node's size you should use the `style` or `className`
  props to apply CSS styles instead.

## OnBeforeDelete

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts#L207)

The `OnBeforeDelete` type defines the callback function that is called before nodes or edges are deleted. This callback receives an object containing the nodes and edges that are about to be deleted.

```ts
type OnBeforeDelete = (params: {
  nodes: Node[];
  edges: Edge[];
}) => Promise<boolean | {
  nodes: Node[];
  edges: Edge[];
})>;
```

##### Parameters

* `__0: { nodes: NodeType[]; edges: EdgeType[]; }`

##### Returns

`Promise<boolean | { nodes: NodeType[]; edges: EdgeType[]; }>`

## OnConnectEnd

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L89)

The `OnConnectEnd` type represents a callback function that is called when finishing or canceling a connection attempt. It receives the mouse or touch event and the final state of the connection attempt.

```ts
type OnConnectEnd = (
  event: MouseEvent | TouchEvent,
  connectionState: FinalConnectionState,
) => void;
```

##### Parameters

* `event: MouseEvent | TouchEvent`
* `connectionState: FinalConnectionState<InternalNodeBase>`

##### Returns

`void`

## OnConnectStart

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L79)

The `OnConnectStart` type represents a callback function that is called when starting to create a connection between nodes. It receives the mouse or touch event and information about the source node and handle.

```ts
type OnConnectStart = (
  event: MouseEvent | TouchEvent,
  params: OnConnectStartParams,
) => void;
```

##### Parameters

* `event: MouseEvent | TouchEvent`
* `params: OnConnectStartParams`

##### Returns

`void`

## OnConnect

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L80)

The `OnConnect` type represents a callback function that is called when a new connection is created between nodes. It receives a [`Connection`](https://reactflow.dev/api-reference/types/connection) containing the source and target node IDs and their respective handle IDs.

```ts
type OnConnect = (connection: Connection) => void;
```

##### Parameters

* `connection: Connection`

##### Returns

`void`

## OnDelete

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts#L59)

The `OnDelete` type defines the callback function that is called when nodes or edges are deleted. This callback receives an object containing the deleted nodes and edges.

```ts
type OnDelete = (params: { nodes: Node[]; edges: Edge[] }) => void;
```

This type can be used to type the `onDelete` function with a custom node and edge type.

##### Parameters

* `params: { nodes: NodeType[]; edges: EdgeType[]; }`

##### Returns

`void`

## OnEdgesChange

This type is used for typing the [`onEdgesChange`](https://reactflow.dev/api-reference/react-flow#on-edges-change) function.

```tsx
export type OnEdgesChange<EdgeType extends Edge = Edge> = (
  changes: EdgeChange<EdgeType>[],
) => void;
```

### Fields

This type can be used to type the `onEdgesChange` function with a custom edge type.

##### Parameters

* `changes: EdgeChange<EdgeType>[]`

##### Returns

`void`

### Usage

This type accepts a generic type argument of custom edge types. See this
[section in our Typescript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const onEdgesChange: OnEdgesChange = useCallback(
  (changes) => setEdges((eds) => applyEdgeChanges(changes, eds)),
  [setEdges],
);
```

## OnEdgesDelete

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts#L52)

The `OnEdgesDelete` type defines the callback function that is called when edges are deleted. This callback receives an array of the deleted edges.

```ts
type OnEdgesDelete = (edges: Edge[]) => void;
```

##### Parameters

* `edges: EdgeType[]`

##### Returns

`void`

## OnError

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L233)

The `OnError` type defines the callback function that is called when an error occurs. This callback receives an error id and the error message as its argument.

```ts
type OnError = (id: string, error: string) => void;
```

##### Parameters

* `id: string`
* `message: string`

##### Returns

`void`

## OnInit

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts#L113)

The `OnInit` type defines the callback function that is called when the ReactFlow instance is initialized. This callback receives the ReactFlow instance as its argument.

```ts
type OnInit = (reactFlowInstance: ReactFlowInstance) => void;
```

##### Parameters

* `reactFlowInstance: ReactFlowInstance<NodeType, EdgeType>`

##### Returns

`void`

## OnMove

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L16)

The `OnMove` type is a callback that fires whenever the viewport is moved, either by user interaction or programmatically. It receives the triggering event and the new viewport state.

```ts
type OnMove = (event: MouseEvent | TouchEvent | null, viewport: Viewport) => void;
```

This type is used to define the `onMove` handler.

##### Parameters

* `event: MouseEvent | TouchEvent`
* `viewport: Viewport`

##### Returns

`void`

## OnNodeDrag

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/nodes.ts#L34)

The `OnNodeDrag` type defines the callback function that is called when a node is being dragged. This callback receives the event and the node that is being dragged.

```ts
type OnNodeDrag = (event: React.MouseEvent, node: Node) => void;
```

##### Parameters

* `event: MouseEvent | TouchEvent`
* `node: NodeType`
* `nodes: NodeType[]`

##### Returns

`void`

## OnNodesChange

This type is used for typing the [`onNodesChange`](https://reactflow.dev/api-reference/react-flow#on-nodes-change) function.

```tsx
export type OnNodesChange<NodeType extends Node = Node> = (
  changes: NodeChange<NodeType>[],
) => void;
```

### Fields

This type can be used to type the `onNodesChange` function with a custom node type.

##### Parameters

* `changes: NodeChange<NodeType>[]`

##### Returns

`void`

### Usage

This type accepts a generic type argument of custom nodes types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const onNodesChange: OnNodesChange = useCallback(
  (changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
  [setNodes],
);
```

## OnNodesDelete

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts#L51)

The `OnNodesDelete` type defines the callback function that is called when nodes are deleted. This callback receives an array of the deleted nodes.

```ts
type OnNodesDelete = (nodes: Node[]) => void;
```

##### Parameters

* `nodes: NodeType[]`

##### Returns

`void`

## OnReconnect

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L83)

The `OnReconnect` type represents a callback function that is called when an existing edge is reconnected to a different node or handle. It receives the old edge and the new connection details.

```ts
type OnReconnect<EdgeType extends EdgeBase = EdgeBase> = (
  oldEdge: EdgeType,
  newConnection: Connection,
) => void;
```

##### Parameters

* `oldEdge: EdgeType`
* `newConnection: Connection`

##### Returns

`void`

## OnSelectionChangeFunc

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/general.ts#98)

The `OnSelectionChangeFunc` type is a callback that is triggered when the selection of nodes or edges changes. It receives an object containing the currently selected nodes and edges.

```ts
type OnSelectionChangeFunc = (params: { nodes: Node[]; edges: Edge[] }) => void;
```

##### Parameters

* `params: OnSelectionChangeParams<NodeType, EdgeType>`

##### Returns

`void`

## PanOnScrollMode

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L166)

The `PanOnScrollMode` enum controls the panning behavior of the viewport when the user
scrolls. Choose `Free` for unrestricted panning, `Vertical` for up-and-down only, or
`Horizontal` for left-and-right only.

```ts
enum PanOnScrollMode {
  Free = 'free',
  Vertical = 'vertical',
  Horizontal = 'horizontal',
}
```

## PanelPosition

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts/#L111-L112)

This type is mostly used to help position things on top of the flow viewport. For
example both the [`<MiniMap />`](https://reactflow.dev/api-reference/components/minimap) and
[`<Controls />`](https://reactflow.dev/api-reference/components/controls) components take a `position`
prop of this type.

```ts
export type PanelPosition =
  | 'top-left'
  | 'top-center'
  | 'top-right'
  | 'bottom-left'
  | 'bottom-center'
  | 'bottom-right'
  | 'center-left'
  | 'center-right';
```

## Position

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/utils.ts/#L1)

While [`PanelPosition`](https://reactflow.dev/api-reference/types/panel-position) can be used to place a component in the
corners of a container, the `Position` enum is less precise and used primarily
in relation to edges and handles.

```ts
export enum Position {
  Left = 'left',
  Top = 'top',
  Right = 'right',
  Bottom = 'bottom',
}
```

## ProOptions

By default, we render a small attribution in the corner of your flows that links back to
the project. We can't legally require you to keep the attribution — React Flow is
MIT-licensed — but to keep the library MIT, we need your support. Our policy is simple:
**attribution visible, no subscription needed; no attribution, please subscribe.** Read the
full [attribution policy](https://reactflow.dev/remove-attribution) for details.

* `account?: string`
* `hideAttribution: boolean`

## ReactFlowInstance

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/instance.ts/#L178-L179)

The `ReactFlowInstance` provides a collection of methods to query and manipulate the
internal state of your flow. You can get an instance by using the
[`useReactFlow`](https://reactflow.dev/api-reference/hooks/use-react-flow) hook or attaching a listener to the
[`onInit`](https://reactflow.dev/api-reference/react-flow#event-oninit) event.

### Fields

#### Nodes and edges

* `getNodes: () => Node[]` Returns nodes.
* `setNodes: (payload: Node[] | ((nodes: Node[]) => Node[])) => void` Set your nodes array
  to something else by either overwriting it with a new array or by passing in a function to
  update the existing array. If using a function, it is important to make sure a new array is
  returned instead of mutating the existing array. Calling this function will trigger the
  `onNodesChange` handler in a controlled flow.
* `addNodes: (payload: Node | Node[]) => void` Add one or many nodes to your existing nodes
  array. Calling this function will trigger the `onNodesChange` handler in a controlled flow.
* `getNode: (id: string) => Node | undefined` Returns a node by id.
* `getInternalNode: (id: string) => InternalNode<Node> | undefined` Returns an internal node by id.
* `getEdges: () => Edge[]` Returns edges.
* `setEdges: (payload: Edge[] | ((edges: Edge[]) => Edge[])) => void` Set your edges array
  to something else by either overwriting it with a new array or by passing in a function to
  update the existing array. If using a function, it is important to make sure a new array is
  returned instead of mutating the existing array. Calling this function will trigger the
  `onEdgesChange` handler in a controlled flow.
* `addEdges: (payload: Edge | Edge[]) => void` Add one or many edges to your existing edges
  array. Calling this function will trigger the `onEdgesChange` handler in a controlled flow.
* `getEdge: (id: string) => Edge | undefined` Returns an edge by id.
* `toObject: () => ReactFlowJsonObject<Node, Edge>` Returns the nodes, edges and the viewport
  as a JSON object.
* `deleteElements: (params: DeleteElementsOptions) => Promise<{ deletedNodes: Node[]; deletedEdges: Edge[]; }>`
  Deletes nodes and edges.
* `updateNode: (id: string, nodeUpdate: Partial<Node> | ((node: Node) => Partial<Node>), options?: { replace: boolean }) => void`
  Updates a node.
* `updateNodeData: (id: string, dataUpdate: Partial<Node['data']> | ((node: Node) => Partial<Node['data']>), options?: { replace: boolean }) => void`
  Updates the data attribute of a node. By default the new data is merged with the existing
  data; pass `{ replace: true }` to replace it.
* `updateEdge: (id: string, edgeUpdate: Partial<Edge> | ((edge: Edge) => Partial<Edge>), options?: { replace: boolean }) => void`
  Updates an edge.
* `updateEdgeData: (id: string, dataUpdate: Partial<Edge['data']> | ((edge: Edge) => Partial<Edge['data']>), options?: { replace: boolean }) => void`
  Updates the data attribute of an edge.
* `getNodesBounds: (nodes: (string | Node | InternalNode)[]) => Rect` Returns the bounds of
  the given nodes or node ids.
* `getHandleConnections: ({ type, id, nodeId }: { type: HandleType; nodeId: string; id?: string | null }) => HandleConnection[]`
  Get all the connections of a handle belonging to a specific node. The type parameter is
  either `'source'` or `'target'`.
* `getNodeConnections: ({ type, handleId, nodeId }: { type?: HandleType; nodeId: string; handleId?: string | null }) => NodeConnection[]`
  Gets all connections to a node. Can be filtered by handle type and id.

#### Intersections

* `getIntersectingNodes: (node: Node | Rect | { id: string }, partially?: boolean, nodes?: Node[]) => Node[]`
  Find all the nodes currently intersecting with a given node or rectangle. The `partially`
  parameter can be set to `true` to include nodes that are only partially intersecting.
* `isNodeIntersecting: (node: Node | Rect | { id: string }, area: Rect, partially?: boolean) => boolean`
  Determine if a given node or rectangle is intersecting with another rectangle. The
  `partially` parameter can be set to `true` to return `true` even if the node is only
  partially intersecting.

#### Viewport

* `viewportInitialized: boolean` React Flow needs to mount the viewport to the DOM and
  initialize its zoom and pan behavior. This property tells you when the viewport is initialized.
* `zoomIn: (options?: { duration?: number; ease?: (t: number) => number; interpolate?: 'smooth' | 'linear' }) => Promise<boolean>`
  Zooms viewport in by 1.2.
* `zoomOut: (options?: { duration?: number; ease?: (t: number) => number; interpolate?: 'smooth' | 'linear' }) => Promise<boolean>`
  Zooms viewport out by 1 / 1.2.
* `zoomTo: (zoomLevel: number, options?: { duration?: number; ease?: (t: number) => number; interpolate?: 'smooth' | 'linear' }) => Promise<boolean>`
  Zoom the viewport to a given zoom level. Passing in a `duration` will animate the viewport
  to the new zoom level.
* `getZoom: () => number` Get the current zoom level of the viewport.
* `setViewport: (viewport: Viewport, options?: { duration?: number; ease?: (t: number) => number; interpolate?: 'smooth' | 'linear' }) => Promise<boolean>`
  Sets the current viewport.
* `getViewport: () => Viewport` Returns the current viewport.
* `fitView: (fitViewOptions?: FitViewOptions) => Promise<boolean>` Fits the view based on the
  passed options (`padding`, `includeHiddenNodes`, `minZoom`, `maxZoom`, `duration`, `ease`,
  `interpolate`, `nodes`). By default it fits the view to all nodes.
* `setCenter: (x: number, y: number, options?: ViewportHelperFunctionOptions & { zoom?: number }) => Promise<boolean>`
  Center the viewport on a given position. Passing in a `duration` will animate the viewport
  to the new position.
* `fitBounds: (bounds: Rect, options?: ViewportHelperFunctionOptions & { padding?: number }) => Promise<boolean>`
  A low-level utility function to fit the viewport to a given rectangle. By passing in a
  `duration`, the viewport will animate from its current position to the new position. The
  `padding` option can be used to add space around the bounds.
* `screenToFlowPosition: (clientPosition: XYPosition, options?: { snapToGrid?: boolean; snapGrid?: SnapGrid }) => XYPosition`
  With this function you can translate a screen pixel position to a flow position. It is
  useful for implementing drag and drop from a sidebar for example.
* `flowToScreenPosition: (flowPosition: XYPosition) => XYPosition` Translate a position inside
  the flow's canvas to a screen pixel position.

## ReactFlowJsonObject

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/instance.ts/#L5)

A JSON-compatible representation of your flow. You can use this to save the flow to a
database for example and load it back in later.

### Fields

* `nodes: NodeType[]`
* `edges: EdgeType[]`
* `viewport: Viewport`

## Rect

[Source on GitHub](https://github.com/xyflow/xyflow/blob/f0ce2c876d8688e13632bc86286cf857f86dead6/packages/system/src/types/utils.ts/#L39-L40)

The `Rect` type defines a rectangle in a two-dimensional space with dimensions and a
position.

* `width: number`
* `height: number`
* `x: number`
* `y: number`

## ResizeParams

[Source on Github](https://github.com/xyflow/xyflow/blob/v11/packages/node-resizer/src/types.ts/#L4)

The `ResizeParams` type is used to type the various events that are emitted by the
`<NodeResizer />` component. You'll sometimes see this type extended with an additional
direction field too.

### Fields

* `x: number`
* `y: number`
* `width: number`
* `height: number`

## SelectionDragHandler

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/types/nodes.ts#L33)

The `SelectionDragHandler` type is a callback for handling drag events involving selected nodes. It receives the triggering mouse or touch event and an array of the affected nodes.

```ts
type SelectionDragHandler<NodeType extends Node = Node> = (
  event: ReactMouseEvent,
  nodes: NodeType[],
) => void;
```

##### Parameters

* `event: MouseEvent<Element, MouseEvent>`
* `nodes: NodeType[]`

##### Returns

`void`

## SelectionMode

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L223)

The `SelectionMode` enum provides two options for node selection behavior:

* `Full`: A node is only selected when the selection rectangle fully contains it
* `Partial`: A node is selected when the selection rectangle partially overlaps with it

```ts
enum SelectionMode {
  Partial = 'partial',
  Full = 'full',
}
```

## SnapGrid

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts#L157)

The `SnapGrid` type defines the grid size for snapping nodes on the pane. It is used in conjunction with the `snapToGrid` prop to enable grid snapping functionality.

```ts
type SnapGrid = [number, number];
```

## Viewport

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts/#L149-L153)

Internally, React Flow maintains a coordinate system that is independent of the rest of
the page. The `Viewport` type tells you where in that system your flow is currently being
display at and how zoomed in or out it is.

### Fields

Internally, React Flow maintains a coordinate system that is independent of the
rest of the page. The `Viewport` type tells you where in that system your flow
is currently being display at and how zoomed in or out it is.

* `x: number`
* `y: number`
* `zoom: number`

### Notes

* A `Transform` has the same properties as the viewport, but they represent different
  things. Make sure you don't get them muddled up or things will start to look weird!

## XYPosition

All positions are stored in an object with x and y coordinates.

```ts
export type XYPosition = {
  x: number;
  y: number;
};
```

## ZIndexMode

The ZIndexMode type is used to define how z-indexing is calculated for nodes and edges.

* `auto` mode will automatically manage z-indexing for selections and sub flows.
* `basic` mode will only manage z-indexing for selections.
* `manual` mode does not apply any automatic z-indexing.

```ts
export type ZIndexMode = 'auto' | 'basic' | 'manual';
```
