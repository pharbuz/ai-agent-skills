## addEdge()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/edges/general.ts/#L100)

This util is a convenience function to add a new [`Edge`](https://reactflow.dev/api-reference/types/edge) to an
array of edges. It also performs some validation to make sure you don't add an
invalid edge or duplicate an existing one.

```js
import { useCallback } from 'react';
import {
  ReactFlow,
  addEdge,
  useNodesState,
  useEdgesState,
} from '@xyflow/react';

export default function Flow() {
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const onConnect = useCallback(
    (connection) => {
      setEdges((oldEdges) => addEdge(connection, oldEdges));
    },
    [setEdges],
  );

  return <ReactFlow nodes={nodes} edges={edges} onConnect={onConnect} />;
}
```

### Signature

##### Parameters

* `edgeParams: EdgeType | Connection`
* `edges: EdgeType[]`
* `options.getEdgeId?: GetEdgeId` Custom function to generate edge IDs. If not provided, the default `getEdgeId` function is used.
* `options.onError?: OnError` Called when edge validation fails. If not provided, a default dev warning is used.

##### Returns

`EdgeType[]`

### Notes

* If an edge with the same `target` and `source` already exists (and the same
  `targetHandle` and `sourceHandle` if those are set), then this util won't add
  a new edge even if the `id` property is different.

## applyEdgeChanges()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/utils/changes.ts/#L167)

Various events on the [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow) component can produce an
[`EdgeChange`](https://reactflow.dev/api-reference/types/edge-change) that describes how to update the edges of your
flow in some way. If you don't need any custom behavior, this util can be used to
take an array of these changes and apply them to your edges.

```js
import { useState, useCallback } from 'react';
import { ReactFlow, applyEdgeChanges } from '@xyflow/react';

export default function Flow() {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);
  const onEdgesChange = useCallback(
    (changes) => {
      setEdges((oldEdges) => applyEdgeChanges(changes, oldEdges));
    },
    [setEdges],
  );

  return (
    <ReactFlow nodes={nodes} edges={edges} onEdgesChange={onEdgesChange} />
  );
}
```

### Signature

Drop in function that applies edge changes to an array of edges.

##### Parameters

* `changes: EdgeChange<EdgeType>[]` Array of changes to apply.
* `edges: EdgeType[]` Array of edge to apply the changes to.

##### Returns

`EdgeType[]`

### Notes

* If you don't need any custom behavior, the [`useEdgesState`](https://reactflow.dev/api-reference/hooks/use-edges-state)
  hook conveniently wraps this util and React's `useState` hook for you and might
  be simpler to use.

## applyNodeChanges()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/utils/changes.ts/#L140)

Various events on the [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow) component can produce a
[`NodeChange`](https://reactflow.dev/api-reference/types/node-change) that describes how to update the nodes of your
flow in some way. If you don't need any custom behavior, this util can be used to
take an array of these changes and apply them to your nodes.

```js
import { useState, useCallback } from 'react';
import { ReactFlow, applyNodeChanges } from '@xyflow/react';

export default function Flow() {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);
  const onNodesChange = useCallback(
    (changes) => {
      setNodes((oldNodes) => applyNodeChanges(changes, oldNodes));
    },
    [setNodes],
  );

  return (
    <ReactFlow nodes={nodes} edges={edges} onNodesChange={onNodesChange} />
  );
}
```

### Signature

Drop in function that applies node changes to an array of nodes.

##### Parameters

* `changes: NodeChange<NodeType>[]` Array of changes to apply.
* `nodes: NodeType[]` Array of nodes to apply the changes to.

##### Returns

`NodeType[]`

### Notes

* If you don't need any custom behavior, the [`useNodesState`](https://reactflow.dev/api-reference/hooks/use-nodes-state)
  hook conveniently wraps this util and React's `useState` hook for you and might
  be simpler to use.

## getBezierPath()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/edges/bezier-edge.ts/#L95)

The `getBezierPath` util returns everything you need to render a bezier edge
between two nodes.

```js
import { Position, getBezierPath } from '@xyflow/react';

const source = { x: 0, y: 20 };
const target = { x: 150, y: 100 };

const [path, labelX, labelY, offsetX, offsetY] = getBezierPath({
  sourceX: source.x,
  sourceY: source.y,
  sourcePosition: Position.Right,
  targetX: target.x,
  targetY: target.y,
  targetPosition: Position.Left,
});

console.log(path); //=> "M0,20 C75,20 75,100 150,100"
console.log(labelX, labelY); //=> 75, 60
console.log(offsetX, offsetY); //=> 75, 40
```

### Signature

The `getBezierPath` util returns everything you need to render a bezier edge
between two nodes.

##### Parameters

* `[0].sourceX: number` The `x` position of the source handle.
* `[0].sourceY: number` The `y` position of the source handle.
* `[0].sourcePosition?: Position` The position of the source handle.
* `[0].targetX: number` The `x` position of the target handle.
* `[0].targetY: number` The `y` position of the target handle.
* `[0].targetPosition?: Position` The position of the target handle.
* `[0].curvature?: number` The curvature of the bezier edge.

##### Returns

`[path: string, labelX: number, labelY: number, offsetX: number, offsetY: number]`

### Notes

* This function returns a tuple (aka a fixed-size array) to make it easier to
  work with multiple edge paths at once.

## getConnectedEdges()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/graph.ts/#L224)

This utility filters an array of edges, keeping only those where either the source or target node is present in the given array of nodes.

```js
import { getConnectedEdges } from '@xyflow/react';

const nodes = [
  { id: 'a', position: { x: 0, y: 0 } },
  { id: 'b', position: { x: 100, y: 0 } },
];
const edges = [
  { id: 'a->c', source: 'a', target: 'c' },
  { id: 'c->d', source: 'c', target: 'd' },
];

const connectedEdges = getConnectedEdges(nodes, edges);
// => [{ id: 'a->c', source: 'a', target: 'c' }]
```

### Signature

This utility filters an array of edges, keeping only those where either the source or target
node is present in the given array of nodes.

##### Parameters

* `nodes: NodeType[]` Nodes you want to get the connected edges for.
* `edges: EdgeType[]` All edges.

##### Returns

`EdgeType[]`

## getIncomers()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/graph.ts/#L91)

This util is used to tell you what nodes, if any, are connected to the given node
as the *source* of an edge.

```ts
import { getIncomers } from '@xyflow/react';

const nodes = [];
const edges = [];

const incomers = getIncomers(
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'node' } },
  nodes,
  edges,
);
```

### Signature

This util is used to tell you what nodes, if any, are connected to the given node
as the *source* of an edge.

##### Parameters

* `node: NodeType | { id: string; }` The node to get the connected nodes from.
* `nodes: NodeType[]` The array of all nodes.
* `edges: EdgeType[]` The array of all edges.

##### Returns

`NodeType[]`

## getNodesBounds()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/graph.ts/#L133)

Returns the bounding box that contains all the given nodes in an array. This can
be useful when combined with [`getViewportForBounds`](https://reactflow.dev/api-reference/utils/get-viewport-for-bounds)
to calculate the correct transform to fit the given nodes in a viewport.

> \[!NOTE]
>
> This function was previously called `getRectOfNodes`

```js
import { getNodesBounds } from '@xyflow/react';

const nodes = [
  {
    id: 'a',
    position: { x: 0, y: 0 },
    data: { label: 'a' },
    width: 50,
    height: 25,
  },
  {
    id: 'b',
    position: { x: 100, y: 100 },
    data: { label: 'b' },
    width: 50,
    height: 25,
  },
];

const bounds = getNodesBounds(nodes);
```

### Signature

Returns the bounding box that contains all the given nodes in an array. This can
be useful when combined with [`getViewportForBounds`](https://reactflow.dev/api-reference/utils/get-viewport-for-bounds)
to calculate the correct transform to fit the given nodes in a viewport.

##### Parameters

* `nodes: (string | NodeType | InternalNodeBase<NodeType>)[]` Nodes to calculate the bounds for.
* `params.nodeOrigin?: NodeOrigin` Origin of the nodes: `[0, 0]` for top-left, `[0.5, 0.5]` for center.
* `params.nodeLookup?: NodeLookup<InternalNodeBase<NodeType>>`

##### Returns

`Rect`

## getOutgoers()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/graph.ts/#L64)

This util is used to tell you what nodes, if any, are connected to the given node
as the *target* of an edge.

```ts
import { getOutgoers } from '@xyflow/react';

const nodes = [];
const edges = [];

const outgoers = getOutgoers(
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'node' } },
  nodes,
  edges,
);
```

### Signature

This util is used to tell you what nodes, if any, are connected to the given node
as the *target* of an edge.

##### Parameters

* `node: NodeType | { id: string; }` The node to get the connected nodes from.
* `nodes: NodeType[]` The array of all nodes.
* `edges: EdgeType[]` The array of all edges.

##### Returns

`NodeType[]`

## getSimpleBezierPath()

[Source on Github](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/Edges/SimpleBezierEdge.tsx/#L32)

The `getSimpleBezierPath` util returns everything you need to render a simple
bezier edge between two nodes.

```js
import { Position, getSimpleBezierPath } from '@xyflow/react';

const source = { x: 0, y: 20 };
const target = { x: 150, y: 100 };

const [path, labelX, labelY, offsetX, offsetY] = getSimpleBezierPath({
  sourceX: source.x,
  sourceY: source.y,
  sourcePosition: Position.Right,
  targetX: target.x,
  targetY: target.y,
  targetPosition: Position.Left,
});

console.log(path); //=> "M0,20 C75,20 75,100 150,100"
console.log(labelX, labelY); //=> 75, 60
console.log(offsetX, offsetY); //=> 75, 40
```

### Signature

The `getSimpleBezierPath` util returns everything you need to render a simple
bezier edge between two nodes.

##### Parameters

* `[0].sourceX: number`
* `[0].sourceY: number`
* `[0].sourcePosition?: Position`
* `[0].targetX: number`
* `[0].targetY: number`
* `[0].targetPosition?: Position`

##### Returns

`[path: string, labelX: number, labelY: number, offsetX: number, offsetY: number]`

### Notes

* This function returns a tuple (aka a fixed-size array) to make it easier to
  work with multiple edge paths at once.

## getSmoothStepPath()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/edges/smoothstep-edge.ts/#L215)

The `getSmoothStepPath` util returns everything you need to render a stepped path
between two nodes. The `borderRadius` property can be used to choose how rounded
the corners of those steps are.

```js
import { Position, getSmoothStepPath } from '@xyflow/react';

const source = { x: 0, y: 20 };
const target = { x: 150, y: 100 };

const [path, labelX, labelY, offsetX, offsetY] = getSmoothStepPath({
  sourceX: source.x,
  sourceY: source.y,
  sourcePosition: Position.Right,
  targetX: target.x,
  targetY: target.y,
  targetPosition: Position.Left,
});

console.log(path); //=> "M0 20L20 20L 70,20Q 75,20 75,25L 75,95Q ..."
console.log(labelX, labelY); //=> 75, 60
console.log(offsetX, offsetY); //=> 75, 40
```

### Signature

The `getSmoothStepPath` util returns everything you need to render a stepped path
between two nodes. The `borderRadius` property can be used to choose how rounded
the corners of those steps are.

##### Parameters

* `[0].sourceX: number` The `x` position of the source handle.
* `[0].sourceY: number` The `y` position of the source handle.
* `[0].sourcePosition?: Position` The position of the source handle.
* `[0].targetX: number` The `x` position of the target handle.
* `[0].targetY: number` The `y` position of the target handle.
* `[0].targetPosition?: Position` The position of the target handle.
* `[0].borderRadius?: number`
* `[0].centerX?: number`
* `[0].centerY?: number`
* `[0].offset?: number`
* `[0].stepPosition?: number` Controls where the bend occurs along the path.
  0 = at source, 1 = at target, 0.5 = midpoint

##### Returns

`[path: string, labelX: number, labelY: number, offsetX: number, offsetY: number]`

### Notes

* This function returns a tuple (aka a fixed-size array) to make it easier to
  work with multiple edge paths at once.
* You can set the `borderRadius` property to `0` to get a step edge path.

## getStraightPath()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/edges/straight-edge.ts/#L30)

Calculates the straight line path between two points.

```js
import { getStraightPath } from '@xyflow/react';

const source = { x: 0, y: 20 };
const target = { x: 150, y: 100 };

const [path, labelX, labelY, offsetX, offsetY] = getStraightPath({
  sourceX: source.x,
  sourceY: source.y,
  targetX: target.x,
  targetY: target.y,
});

console.log(path); //=> "M 0,20L 150,100"
console.log(labelX, labelY); //=> 75, 60
console.log(offsetX, offsetY); //=> 75, 40
```

### Signature

Calculates the straight line path between two points.

##### Parameters

* `[0].sourceX: number` The `x` position of the source handle.
* `[0].sourceY: number` The `y` position of the source handle.
* `[0].targetX: number` The `x` position of the target handle.
* `[0].targetY: number` The `y` position of the target handle.

##### Returns

`[path: string, labelX: number, labelY: number, offsetX: number, offsetY: number]`

### Notes

* This function returns a tuple (aka a fixed-size array) to make it easier to work with multiple edge paths at once.

## getViewportForBounds()

[Source on Github](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/general.ts/#L170)

This util returns the viewport for the given bounds.
You might use this to pre-calculate the viewport for a given set of nodes on the
server or calculate the viewport for the given bounds *without* changing the
viewport directly.

> \[!NOTE]
>
> This function was previously called `getTransformForBounds`

```js
import { getViewportForBounds } from '@xyflow/react';

const { x, y, zoom } = getViewportForBounds(
  {
    x: 0,
    y: 0,
    width: 100,
    height: 100,
  },
  1200,
  800,
  0.5,
  2,
);
```

### Signature

Returns a viewport that encloses the given bounds with padding.

##### Parameters

* `bounds: Rect` Bounds to fit inside viewport.
* `width: number` Width of the viewport.
* `height: number` Height of the viewport.
* `minZoom: number` Minimum zoom level of the resulting viewport.
* `maxZoom: number` Maximum zoom level of the resulting viewport.
* `padding: Padding` Padding around the bounds.

##### Returns

* `x: number`
* `y: number`
* `zoom: number`

### Notes

* This is quite a low-level utility. You might want to look at the
  [`fitView`](https://reactflow.dev/api-reference/types/react-flow-instance#fitview) or
  [`fitBounds`](https://reactflow.dev/api-reference/types/react-flow-instance#fitbounds) methods for a more practical
  api.

## isEdge()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/graph.ts/#L39-L40)

Test whether an object is usable as an [`Edge`](https://reactflow.dev/api-reference/types/edge). In TypeScript
this is a type guard that will narrow the type of whatever you pass in to
[`Edge`](https://reactflow.dev/api-reference/types/edge) if it returns `true`.

```js
import { isEdge } from '@xyflow/react';

const edge = {
  id: 'edge-a',
  source: 'a',
  target: 'b',
};

if (isEdge(edge)) {
  // ...
}
```

### Signature

Test whether an object is usable as an [`Edge`](https://reactflow.dev/api-reference/types/edge).
In TypeScript this is a type guard that will narrow the type of whatever you pass in to
[`Edge`](https://reactflow.dev/api-reference/types/edge) if it returns `true`.

##### Parameters

* `element: unknown` The element to test

##### Returns

`boolean`

## isNode()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/graph.ts/#L49)

Test whether an object is usable as a [`Node`](https://reactflow.dev/api-reference/types/node). In TypeScript
this is a type guard that will narrow the type of whatever you pass in to
[`Node`](https://reactflow.dev/api-reference/types/node) if it returns `true`.

```js
import { isNode } from '@xyflow/react';

const node = {
  id: 'node-a',
  data: {
    label: 'node',
  },
  position: {
    x: 0,
    y: 0,
  },
};

if (isNode(node)) {
  // ..
}
```

### Signature

Test whether an object is usable as an [`Node`](https://reactflow.dev/api-reference/types/node).
In TypeScript this is a type guard that will narrow the type of whatever you pass in to
[`Node`](https://reactflow.dev/api-reference/types/node) if it returns `true`.

##### Parameters

* `element: unknown` The element to test.

##### Returns

`boolean`

## reconnectEdge()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/system/src/utils/edges/general.ts)

A handy utility to update an existing [`Edge`](https://reactflow.dev/api-reference/types/edge) with new
properties. This searches your edge array for an edge with a matching `id` and updates its
properties with the connection you provide.

```js
const onReconnect = useCallback(
  (oldEdge: Edge, newConnection: Connection) => setEdges((els) => reconnectEdge(oldEdge, newConnection, els)),
  []
);
```

### Signature

##### Parameters

* `oldEdge: EdgeType`
* `newConnection.source: string` The id of the node this connection originates from.
* `newConnection.target: string` The id of the node this connection terminates at.
* `newConnection.sourceHandle: string | null` When not `null`, the id of the handle on the source node that this connection originates from.
* `newConnection.targetHandle: string | null` When not `null`, the id of the handle on the target node that this connection terminates at.
* `edges: EdgeType[]`
* `options.shouldReplaceId?: boolean` Should the id of the old edge be replaced with the new connection id.
* `options.getEdgeId?: GetEdgeId` Custom function to generate edge IDs. If not provided, the default `getEdgeId` function is used.
* `options.onError?: OnError` Called when edge validation fails. If not provided, a default dev warning is used.

##### Returns

`EdgeType[]`
