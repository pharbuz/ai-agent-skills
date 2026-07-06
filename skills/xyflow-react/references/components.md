## <Background />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/Background/Background.tsx)

The `<Background />` component makes it convenient to render different types of
backgrounds common in node-based UIs. It comes with three variants: `lines`,
`dots` and `cross`.

```jsx
import { useState } from 'react';
import { ReactFlow, Background, BackgroundVariant } from '@xyflow/react';

export default function Flow() {
  return (
    <ReactFlow defaultNodes={[...]} defaultEdges={[...]}>
      <Background color="#ccc" variant={BackgroundVariant.Dots} />
    </ReactFlow>
  );
}
```

### Props

* `id?: string` When multiple backgrounds are present on the page, each one should have a unique id.
* `color?: string` Color of the pattern.
* `bgColor?: string` Color of the background.
* `className?: string` Class applied to the container.
* `patternClassName?: string` Class applied to the pattern.
* `gap?: number | [number, number]` The gap between patterns. Passing in a tuple allows you to control the x and y gap
  independently.
* `size?: number` The radius of each dot or the size of each rectangle if `BackgroundVariant.Dots` or
  `BackgroundVariant.Cross` is used. This defaults to 1 or 6 respectively, or ignored if
  `BackgroundVariant.Lines` is used.
* `offset?: number | [number, number]` Offset of the pattern.
* `lineWidth?: number` The stroke thickness used when drawing the pattern.
* `variant?: BackgroundVariant` Variant of the pattern.
* `style?: CSSProperties` Style applied to the container.

### Examples

#### Combining multiple backgrounds

It is possible to layer multiple `<Background />` components on top of one another
to create something more interesting. The following example shows how to render a
square grid accented every 10th line.

```tsx
import { ReactFlow, Background, BackgroundVariant } from '@xyflow/react';

import '@xyflow/react/dist/style.css';

export default function Flow() {
  return (
    <ReactFlow defaultNodes={[...]} defaultEdges={[...]}>
      <Background
        id="1"
        gap={10}
        color="#f1f1f1"
        variant={BackgroundVariant.Lines}
      />

      <Background
        id="2"
        gap={100}
        color="#ccc"
        variant={BackgroundVariant.Lines}
      />
    </ReactFlow>
  );
}
```

### Notes

* When combining multiple `<Background />` components it's important to give each
  of them a unique `id` prop!

## <BaseEdge />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/Edges/BaseEdge.tsx)

The `<BaseEdge />` component gets used internally for all the edges. It can be
used inside a custom edge and handles the invisible helper edge and the edge label
for you.

```jsx
import { BaseEdge } from '@xyflow/react';

export function CustomEdge({ sourceX, sourceY, targetX, targetY, ...props }) {
  const [edgePath] = getStraightPath({
    sourceX,
    sourceY,
    targetX,
    targetY,
  });

  const { label, labelStyle, markerStart, markerEnd, interactionWidth } = props;

  return (
    <BaseEdge
      path={edgePath}
      label={label}
      labelStyle={labelStyle}
      markerEnd={markerEnd}
      markerStart={markerStart}
      interactionWidth={interactionWidth}
    />
  );
}
```

### Props

* `path: string` The SVG path string that defines the edge. This should look something like
  `'M 0 0 L 100 100'` for a simple line. The utility functions like `getSimpleBezierEdge` can
  be used to generate this string for you.
* `markerStart?: string` The id of the SVG marker to use at the start of the edge. This should be defined in a
  `<defs>` element in a separate SVG document or element. Use the format "url(#markerId)" where markerId is the id of your marker definition.
* `markerEnd?: string` The id of the SVG marker to use at the end of the edge. This should be defined in a `<defs>`
  element in a separate SVG document or element. Use the format "url(#markerId)" where markerId is the id of your marker definition.
* `label?: ReactNode` The label or custom element to render along the edge. This is commonly a text label or some
  custom controls.
* `labelStyle?: CSSProperties` Custom styles to apply to the label.
* `labelShowBg?: boolean`
* `labelBgStyle?: CSSProperties`
* `labelBgPadding?: [number, number]`
* `labelBgBorderRadius?: number`
* `interactionWidth?: number` The width of the invisible area around the edge that the user can interact with. This is
  useful for making the edge easier to click or hover over.
* `labelX?: number` The x position of edge label
* `labelY?: number` The y position of edge label
* `...props: Omit<SVGAttributes<SVGPathElement>, "d" | "path" | "markerStart" | "markerEnd">`

### Notes

* If you want to use an edge marker with the [`<BaseEdge />`](https://reactflow.dev/api-reference/components/base-edge) component,
  you can pass the `markerStart` or `markerEnd` props passed to your custom edge
  through to the [`<BaseEdge />`](https://reactflow.dev/api-reference/components/base-edge) component. You can see all the props
  passed to a custom edge by looking at the [`EdgeProps`](https://reactflow.dev/api-reference/types/edge-props) type.

## <ControlButton />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/Controls/ControlButton.tsx)

You can add buttons to the control panel by using the `<ControlButton />` component
and pass it as a child to the [`<Controls />`](https://reactflow.dev/api-reference/components/controls) component.

```jsx
import { MagicWand } from '@radix-ui/react-icons'
import { ReactFlow, Controls, ControlButton } from '@xyflow/react'

export default function Flow() {
  return (
    <ReactFlow nodes={[...]} edges={[...]}>
      <Controls>
        <ControlButton onClick={() => alert('Something magical just happened. ✨')}>
          <MagicWand />
        </ControlButton>
      </Controls>
    </ReactFlow>
  )
}
```

### Props

The `<ControlButton />` component accepts any prop valid on a HTML `<button />`
element.

* `...props: ButtonHTMLAttributes<HTMLButtonElement>`

## <Controls />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/Controls/Controls.tsx)

The `<Controls />` component renders a small panel that contains convenient
buttons to zoom in, zoom out, fit the view, and lock the viewport.

```tsx
import { ReactFlow, Controls } from '@xyflow/react'

export default function Flow() {
  return (
    <ReactFlow nodes={[...]} edges={[...]}>
      <Controls />
    </ReactFlow>
  )
}
```

### Props

For TypeScript users, the props type for the `<Controls />` component is exported
as `ControlProps`.

* `showZoom?: boolean` Whether or not to show the zoom in and zoom out buttons. These buttons will adjust the viewport
  zoom by a fixed amount each press.
* `showFitView?: boolean` Whether or not to show the fit view button. By default, this button will adjust the viewport so
  that all nodes are visible at once.
* `showInteractive?: boolean` Show button for toggling interactivity
* `fitViewOptions?: FitViewOptionsBase<NodeType>` Customise the options for the fit view button. These are the same options you would pass to the
  fitView function.
* `onZoomIn?: () => void` Called in addition the default zoom behavior when the zoom in button is clicked.
* `onZoomOut?: () => void` Called in addition the default zoom behavior when the zoom out button is clicked.
* `onFitView?: () => void` Called when the fit view button is clicked. When this is not provided, the viewport will be
  adjusted so that all nodes are visible.
* `onInteractiveChange?: (interactiveStatus: boolean) => void` Called when the interactive (lock) button is clicked.
* `position?: PanelPosition` Position of the controls on the pane
* `children?: ReactNode`
* `style?: CSSProperties` Style applied to container
* `className?: string` Class name applied to container
* `aria-label?: string`
* `orientation?: "horizontal" | "vertical"`

### Notes

* To extend or customize the controls, you can use the [`<ControlButton />`](https://reactflow.dev/api-reference/components/control-button)
  component

## <EdgeLabelRenderer />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/EdgeLabelRenderer/index.tsx)

Edges are SVG-based. If you want to render more complex labels you can use the
`<EdgeLabelRenderer />` component to access a div based renderer. This component
is a portal that renders the label in a `<div />` that is positioned on top of
the edges. You can see an example usage of the component in the [edge label renderer](https://reactflow.dev/examples/edges/edge-label-renderer)
example.

```jsx
import React from 'react';
import { getBezierPath, EdgeLabelRenderer, BaseEdge } from '@xyflow/react';

const CustomEdge = ({ id, data, ...props }) => {
  const [edgePath, labelX, labelY] = getBezierPath(props);

  return (
    <>
      <BaseEdge id={id} path={edgePath} />
      <EdgeLabelRenderer>
        <div
          style={{
            position: 'absolute',
            transform: `translate(-50%, -50%) translate(${labelX}px,${labelY}px)`,
            background: '#ffcc00',
            padding: 10,
            borderRadius: 5,
            fontSize: 12,
            fontWeight: 700,
          }}
          className="nodrag nopan"
        >
          {data.label}
        </div>
      </EdgeLabelRenderer>
    </>
  );
};

export default CustomEdge;
```

### Props

* `children: ReactNode`

### Notes

* The `<EdgeLabelRenderer />` has no pointer events by default. If you want to
  add mouse interactions you need to set the style `pointerEvents: 'all'` and add
  the `nopan` class on the label or the element you want to interact with.

## <EdgeText />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/Edges/EdgeText.tsx)

You can use the `<EdgeText />` component as a helper component to display text
within your custom edges.

```jsx
import { EdgeText } from '@xyflow/react';

export function CustomEdgeLabel({ label }) {
  return (
    <EdgeText
      x={100}
      y={100}
      label={label}
      labelStyle={{ fill: 'white' }}
      labelShowBg
      labelBgStyle={{ fill: 'red' }}
      labelBgPadding={[2, 4]}
      labelBgBorderRadius={2}
    />
  );
}
```

### Props

For TypeScript users, the props type for the `<EdgeText />` component is exported
as `EdgeTextProps`.

* `x: number` The x position where the label should be rendered.
* `y: number` The y position where the label should be rendered.
* `label?: ReactNode` The label or custom element to render along the edge. This is commonly a text label or some
  custom controls.
* `labelStyle?: CSSProperties` Custom styles to apply to the label.
* `labelShowBg?: boolean`
* `labelBgStyle?: CSSProperties`
* `labelBgPadding?: [number, number]`
* `labelBgBorderRadius?: number`
* `...props: Omit<SVGAttributes<SVGElement>, "x" | "y">`

Additionally, you may also pass any standard React HTML attributes such as `onClick`,
`className` and so on.

## <EdgeToolbar />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/EdgeToolbar/EdgeToolbar.tsx)

This component can render a toolbar to one side of a custom edge. This toolbar doesn't
scale with the viewport so that the content doesn't get too small when zooming out.

```jsx
import { memo } from 'react';
import { EdgeToolbar, BaseEdge, getBezierPath, type EdgeProps } from '@xyflow/react';

function CustomEdge(props: EdgeProps) {
  const [edgePath, centerX, centerY] = getBezierPath(props);

  return (
    <>
      <BaseEdge id={props.id} path={edgePath} />
      <EdgeToolbar
        edgeId={props.id}
        x={centerX}
        y={centerY}
        isVisible
      >
        <button>
          some button
        </button>
      </EdgeToolbar>
    </>
  );
}

export default memo(CustomEdge);
```

### Props

* `x: number` The `x` position of the edge toolbar.
* `y: number` The `y` position of the edge toolbar.
* `isVisible?: boolean` If `true`, edge toolbar is visible even if edge is not selected.
* `alignX?: "left" | "center" | "right"` Align the vertical toolbar position relative to the passed x position.
* `alignY?: "center" | "top" | "bottom"` Align the horizontal toolbar position relative to the passed y position.
* `edgeId: string` An edge toolbar must be attached to an edge.
* `...props: HTMLAttributes<HTMLDivElement>`

### Notes

* By default, the toolbar is only visible when the edge is selected. You can override this
  behavior by setting the `isVisible` prop to `true`.

## <Handle />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/Handle/index.tsx)

The `<Handle />` component is used in your [custom nodes](https://reactflow.dev/learn/customization/custom-nodes)
to define connection points.

```jsx
import { Handle, Position } from '@xyflow/react';

export const CustomNode = ({ data }) => {
  return (
    <>
      <div style={{ padding: '10px 20px' }}>
        {data.label}
      </div>

      <Handle type="target" position={Position.Left} />
      <Handle type="source" position={Position.Right} />
    </>
  );
};
```

### Props

For TypeScript users, the props type for the `<Handle />` component is exported
as `HandleProps`.

* `id?: string | null` Id of the handle.
* `type: 'source' | 'target'` Type of the handle.
* `position: Position` The position of the handle relative to the node. In a horizontal flow source handles are
  typically `Position.Right` and in a vertical flow they are typically `Position.Top`.
* `isConnectable?: boolean` Should you be able to connect to/from this handle.
* `isConnectableStart?: boolean` Dictates whether a connection can start from this handle.
* `isConnectableEnd?: boolean` Dictates whether a connection can end on this handle.
* `isValidConnection?: IsValidConnection` Called when a connection is dragged to this handle. You can use this callback to perform some
  custom validation logic based on the connection target and source, for example. Where possible,
  we recommend you move this logic to the `isValidConnection` prop on the main ReactFlow
  component for performance reasons.
* `onConnect?: OnConnect` Callback called when connection is made
* `...props: Omit<DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement>, "id">`

## <MiniMap />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/MiniMap/MiniMap.tsx)

The `<MiniMap />` component can be used to render an overview of your flow. It
renders each node as an SVG element and visualizes where the current viewport is
in relation to the rest of the flow.

```jsx
import { ReactFlow, MiniMap } from '@xyflow/react';

export default function Flow() {
  return (
    <ReactFlow nodes={[...]]} edges={[...]]}>
      <MiniMap nodeStrokeWidth={3} />
    </ReactFlow>
  );
}
```

### Props

For TypeScript users, the props type for the `<MiniMap />` component is exported
as `MiniMapProps`.

* `position?: PanelPosition` Position of minimap on pane.
* `onClick?: (event: MouseEvent<Element, MouseEvent>, position: XYPosition) => void` Callback called when minimap is clicked.
* `nodeColor?: string | GetMiniMapNodeAttribute<Node>` Color of nodes on minimap.
* `nodeStrokeColor?: string | GetMiniMapNodeAttribute<Node>` Stroke color of nodes on minimap.
* `nodeClassName?: string | GetMiniMapNodeAttribute<Node>` Class name applied to nodes on minimap.
* `nodeBorderRadius?: number` Border radius of nodes on minimap.
* `nodeStrokeWidth?: number` Stroke width of nodes on minimap.
* `nodeComponent?: ComponentType<MiniMapNodeProps>` A custom component to render the nodes in the minimap. This component must render an SVG
  element!
* `bgColor?: string` Background color of minimap.
* `maskColor?: string` The color of the mask that covers the portion of the minimap not currently visible in the
  viewport.
* `maskStrokeColor?: string` Stroke color of mask representing viewport.
* `maskStrokeWidth?: number` Stroke width of mask representing viewport.
* `onNodeClick?: (event: MouseEvent<Element, MouseEvent>, node: Node) => void` Callback called when node on minimap is clicked.
* `pannable?: boolean` Determines whether you can pan the viewport by dragging inside the minimap.
* `zoomable?: boolean` Determines whether you can zoom the viewport by scrolling inside the minimap.
* `ariaLabel?: string | null` There is no text inside the minimap for a screen reader to use as an accessible name, so it's
  important we provide one to make the minimap accessible. The default is sufficient, but you may
  want to replace it with something more relevant to your app or product.
* `inversePan?: boolean` Invert direction when panning the minimap viewport.
* `zoomStep?: number` Step size for zooming in/out on minimap.
* `offsetScale?: number` Offset the viewport on the minimap, acts like a padding.
* `...props: Omit<HTMLAttributes<SVGSVGElement>, "onClick">`

### Examples

#### Making the mini map interactive

By default, the mini map is non-interactive. To allow users to interact with the
viewport by panning or zooming the minimap, you can set either of the `zoomable`
or `pannable` (or both!) props to `true`.

```jsx
import { ReactFlow, MiniMap } from '@xyflow/react';

export default function Flow() {
  return (
    <ReactFlow nodes={[...]]} edges={[...]]}>
      <MiniMap pannable zoomable />
    </ReactFlow>
  );
}
```

#### Implement a custom mini map node

It is possible to pass a custom component to the `nodeComponent` prop to change
how nodes are rendered in the mini map. If you do this you **must** use only
SVG elements in your component if you want it to work correctly.

```jsx
import { ReactFlow, MiniMap } from '@xyflow/react';

export default function Flow() {
  return (
    <ReactFlow nodes={[...]]} edges={[...]]}>
      <MiniMap nodeComponent={MiniMapNode} />
    </ReactFlow>
  );
}

function MiniMapNode({ x, y }) {
  return <circle cx={x} cy={y} r="50" />;
}
```

Check out the documentation for [`MiniMapNodeProps`](https://reactflow.dev/api-reference/types/mini-map-node-props)
to see what props are passed to your custom component.

#### Customising mini map node color

The `nodeColor`, `nodeStrokeColor`, and `nodeClassName` props can be a function
that takes a [`Node`](https://reactflow.dev/api-reference/types/node) and computes a value for the prop. This can
be used to customize the appearance of each mini map node.

This example shows how to color each mini map node based on the node's type:

```jsx
import { ReactFlow, MiniMap } from '@xyflow/react';

export default function Flow() {
  return (
    <ReactFlow nodes={[...]]} edges={[...]]}>
      <MiniMap nodeColor={nodeColor} />
    </ReactFlow>
  );
}

function nodeColor(node) {
  switch (node.type) {
    case 'input':
      return '#6ede87';
    case 'output':
      return '#6865A5';
    default:
      return '#ff0072';
  }
}
```

### TypeScript

This component accepts a generic type argument of custom node types. See this
[section in our Typescript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
<MiniMap<CustomNodeType> nodeColor={nodeColor} />
```

## <NodeResizeControl />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/NodeResizer/NodeResizeControl.tsx)

To create your own resizing UI, you can use the `NodeResizeControl` component where you can pass children (such as icons).

### Props

For TypeScript users, the props type for the `<NodeResizeControl />` component is exported
as `ResizeControlProps`.

* `nodeId?: string` Id of the node it is resizing.
* `color?: string` Color of the resize handle.
* `minWidth?: number` Minimum width of node.
* `minHeight?: number` Minimum height of node.
* `maxWidth?: number` Maximum width of node.
* `maxHeight?: number` Maximum height of node.
* `keepAspectRatio?: boolean` Keep aspect ratio when resizing.
* `shouldResize?: (event: ResizeDragEvent, params: ResizeParamsWithDirection) => boolean` Callback to determine if node should resize.
* `autoScale?: boolean` Scale the controls with the zoom level.
* `onResizeStart?: OnResizeStart` Callback called when resizing starts.
* `onResize?: OnResize` Callback called when resizing.
* `onResizeEnd?: OnResizeEnd` Callback called when resizing ends.
* `position?: ControlLinePosition | 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right'` Position of the control.
* `variant?: ResizeControlVariant` Variant of the control.
* `resizeDirection?: 'horizontal' | 'vertical'` The direction the user can resize the node.
  If not provided, the user can resize in any direction.
* `className?: string`
* `style?: CSSProperties`
* `children?: ReactNode`

## <NodeResizer />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/NodeResizer/NodeResizer.tsx)

The `<NodeResizer />` component can be used to add a resize functionality to your
nodes. It renders draggable controls around the node to resize in all directions.

```jsx
import { memo } from 'react';
import { Handle, Position, NodeResizer } from '@xyflow/react';

const ResizableNode = ({ data }) => {
  return (
    <>
      <NodeResizer minWidth={100} minHeight={30} />
      <Handle type="target" position={Position.Left} />
      <div style={{ padding: 10 }}>{data.label}</div>
      <Handle type="source" position={Position.Right} />
    </>
  );
};

export default memo(ResizableNode);
```

### Props

For TypeScript users, the props type for the `<NodeResizer />` component is exported
as `NodeResizerProps`.

* `nodeId?: string` Id of the node it is resizing.
* `color?: string` Color of the resize handle.
* `handleClassName?: string` Class name applied to handle.
* `handleStyle?: CSSProperties` Style applied to handle.
* `lineClassName?: string` Class name applied to line.
* `lineStyle?: CSSProperties` Style applied to line.
* `isVisible?: boolean` Are the controls visible.
* `minWidth?: number` Minimum width of node.
* `minHeight?: number` Minimum height of node.
* `maxWidth?: number` Maximum width of node.
* `maxHeight?: number` Maximum height of node.
* `keepAspectRatio?: boolean` Keep aspect ratio when resizing.
* `autoScale?: boolean` Scale the controls with the zoom level.
* `shouldResize?: (event: ResizeDragEvent, params: ResizeParamsWithDirection) => boolean` Callback to determine if node should resize.
* `onResizeStart?: OnResizeStart` Callback called when resizing starts.
* `onResize?: OnResize` Callback called when resizing.
* `onResizeEnd?: OnResizeEnd` Callback called when resizing ends.

### Examples

A full demo is at <https://reactflow.dev/examples/nodes/node-resizer>. The two most
common patterns:

Always-on resizer inside a custom node:

```jsx
import { memo } from 'react';
import { Handle, Position, NodeResizer } from '@xyflow/react';

const ResizableNode = ({ data }) => (
  <>
    <NodeResizer minWidth={100} minHeight={30} />
    <Handle type="target" position={Position.Left} />
    <div style={{ padding: 10 }}>{data.label}</div>
    <Handle type="source" position={Position.Right} />
  </>
);

export default memo(ResizableNode);
```

Resizer only visible while the node is selected (pass the `selected` prop from
`NodeProps` to `isVisible`):

```jsx
const ResizableNodeSelected = ({ data, selected }) => (
  <>
    <NodeResizer color="#ff0071" isVisible={selected} minWidth={100} minHeight={30} />
    <Handle type="target" position={Position.Left} />
    <div style={{ padding: 10 }}>{data.label}</div>
    <Handle type="source" position={Position.Right} />
  </>
);
```

For a fully custom resize UI (own icon, single corner control), use
[`<NodeResizeControl />`](https://reactflow.dev/api-reference/components/node-resize-control) with children instead.

### Notes

* Take a look at the docs for the [`NodeProps`](https://reactflow.dev/api-reference/types/node-props) type or the
  guide on [custom nodes](https://reactflow.dev/learn/customization/custom-nodes) to see how to
  implement your own nodes.

## <NodeToolbar />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/NodeToolbar/NodeToolbar.tsx)

This component can render a toolbar or tooltip to one side of a custom node. This
toolbar doesn't scale with the viewport so that the content is always visible.

```jsx
import { memo } from 'react';
import { Handle, Position, NodeToolbar } from '@xyflow/react';

const CustomNode = ({ data }) => {
  return (
    <>
      <NodeToolbar isVisible={data.toolbarVisible} position={data.toolbarPosition}>
        <button>delete</button>
        <button>copy</button>
        <button>expand</button>
      </NodeToolbar>

      <div style={{ padding: '10px 20px' }}>
        {data.label}
      </div>

      <Handle type="target" position={Position.Left} />
      <Handle type="source" position={Position.Right} />
    </>
  );
};

export default memo(CustomNode);
```

### Props

For TypeScript users, the props type for the `<NodeToolbar />` component is exported
as `NodeToolbarProps`. Additionally, the `<NodeToolbar />` component accepts all props of the HTML `<div />`
element.

* `nodeId?: string | string[]` By passing in an array of node id's you can render a single tooltip for a group or collection
  of nodes.
* `isVisible?: boolean` If `true`, node toolbar is visible even if node is not selected.
* `position?: Position` Position of the toolbar relative to the node.
* `offset?: number` The space between the node and the toolbar, measured in pixels.
* `align?: Align` Align the toolbar relative to the node.
* `...props: HTMLAttributes<HTMLDivElement>`

### Notes

* By default, the toolbar is only visible when a node is selected. If multiple
  nodes are selected it will not be visible to prevent overlapping toolbars or
  clutter. You can override this behavior by setting the `isVisible` prop to
  `true`.

## <Panel />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/Panel/index.tsx)

The `<Panel />` component helps you position content above the viewport. It is
used internally by the [`<MiniMap />`](https://reactflow.dev/api-reference/components/minimap) and [`<Controls />`](https://reactflow.dev/api-reference/components/controls)
components.

```jsx
import { ReactFlow, Panel } from '@xyflow/react';

export default function Flow() {
  return (
    <ReactFlow nodes={[...]} fitView>
      <Panel position="top-left">top-left</Panel>
      <Panel position="top-center">top-center</Panel>
      <Panel position="top-right">top-right</Panel>
      <Panel position="bottom-left">bottom-left</Panel>
      <Panel position="bottom-center">bottom-center</Panel>
      <Panel position="bottom-right">bottom-right</Panel>
      <Panel position="center-left">center-left</Panel>
      <Panel position="center-right">center-right</Panel>
    </ReactFlow>
  );
}
```

### Props

For TypeScript users, the props type for the `<Panel />` component is exported
as `PanelProps`. Additionally, the `<Panel />` component accepts all props of the HTML `<div />`
element.

* `position?: PanelPosition` The position of the panel.
* `...props: DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement>`

## <ViewportPortal />

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/ViewportPortal/index.tsx)

`<ViewportPortal />` component can be used to add components to the same viewport of the flow where nodes and edges are rendered.
This is useful when you want to render your own components that adhere to the same coordinate system as the nodes & edges and are also
affected by zooming and panning

```jsx
import React from 'react';
import { ViewportPortal } from '@xyflow/react';

export default function () {
  return (
    <ViewportPortal>
      <div
        style={{ transform: 'translate(100px, 100px)', position: 'absolute' }}
      >
        This div is positioned at [100, 100] on the flow.
      </div>
    </ViewportPortal>
  );
}
```

### Props

* `children: ReactNode`
