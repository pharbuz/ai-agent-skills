## useConnection()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useConnection.ts)

The `useConnection` hook returns the current connection state when there is an active connection interaction. If no connection interaction is active, it returns `null` for every property. A typical use case for this hook is to colorize handles based on a certain condition (e.g. if the connection is valid or not).

```tsx
import { useConnection } from '@xyflow/react';

export default function App() {
  const connection = useConnection();

  return (
    <div>
      {connection ? `Someone is trying to make a connection from ${connection.fromNode} to this one.` : 'There are currently no incoming connections!'}
    </div>
  );
}
```

### Signature

The `useConnection` hook returns the current connection when there is an active
connection interaction. If no connection interaction is active, it returns null
for every property. A typical use case for this hook is to colorize handles
based on a certain condition (e.g. if the connection is valid or not).

##### Parameters

* `connectionSelector?: (connection: ConnectionState<InternalNode<NodeType>>) => SelectorReturn` An optional selector function used to extract a slice of the
  `ConnectionState` data. Using a selector can prevent component re-renders where data you don't
  otherwise care about might change. If a selector is not provided, the entire `ConnectionState`
  object is returned unchanged.

##### Returns

`SelectorReturn`

## useEdgesState()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodesEdgesState.ts)

This hook makes it easy to prototype a controlled flow where you manage the
state of nodes and edges outside the `ReactFlowInstance`. You can think of it
like React's `useState` hook with an additional helper callback.

```jsx
import { ReactFlow, useNodesState, useEdgesState } from '@xyflow/react';

const initialNodes = [];
const initialEdges = [];

export default function () {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
    />
  );
}
```

### Signature

This hook makes it easy to prototype a controlled flow where you manage the
state of nodes and edges outside the `ReactFlowInstance`. You can think of it
like React's `useState` hook with an additional helper callback.

##### Parameters

* `initialEdges: EdgeType[]`

##### Returns

`[edges: EdgeType[], setEdges: Dispatch<SetStateAction<EdgeType[]>>, onEdgesChange: OnEdgesChange<EdgeType>]`

### TypeScript

This hook accepts a generic type argument of custom edge types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const nodes = useEdgesState<CustomEdgeType>();
```

### Notes

* This hook was created to make prototyping easier and our documentation
  examples clearer. Although it is OK to use this hook in production, in
  practice you may want to use a more sophisticated state management solution
  like [Zustand](https://reactflow.dev/docs/guides/state-management/) instead.

## useEdges()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useEdges.ts)

This hook returns an array of the current edges. Components that use this hook
will re-render **whenever any edge changes**.

```jsx
import { useEdges } from '@xyflow/react';

export default function () {
  const edges = useEdges();

  return <div>There are currently {edges.length} edges!</div>;
}
```

### Signature

This hook returns an array of the current edges. Components that use this hook
will re-render **whenever any edge changes**.

This function does not accept any parameters.

##### Returns

`EdgeType[]`

### TypeScript

This hook accepts a generic type argument of custom edge types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const nodes = useEdges<CustomEdgeType>();
```

### Notes

* Relying on `useEdges` unnecessarily can be a common cause of performance
  issues. Whenever any edge changes, this hook will cause the component to
  re-render. Often we actually care about something more specific, like when
  the *number* of edges changes: where possible try to use
  [`useStore`](https://reactflow.dev/api-reference/hooks/use-store) instead.

## useHandleConnections()

> \[!WARNING]
>
> `useHandleConnections` is deprecated in favor of the more capable
> [useNodeConnections](https://reactflow.dev/api-reference/hooks/use-node-connections).

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useHandleConnections.ts)

This hook returns an array connections on a specific handle or handle type.

```jsx
import { useHandleConnections } from '@xyflow/react';

export default function () {
  const connections = useHandleConnections({ type: 'target', id: 'my-handle' });

  return (
    <div>There are currently {connections.length} incoming connections!</div>
  );
}
```

### Signature

Hook to check if a <Handle /> is connected to another <Handle /> and get the connections.

##### Parameters

* `[0].type: 'source' | 'target'` What type of handle connections do you want to observe?
* `[0].id?: string | null` The handle id (this is only needed if the node has multiple handles of the same type).
* `[0].nodeId?: string` If node id is not provided, the node id from the `NodeIdContext` is used.
* `[0].onConnect?: (connections: Connection[]) => void` Gets called when a connection is established.
* `[0].onDisconnect?: (connections: Connection[]) => void` Gets called when a connection is removed.

##### Returns

`HandleConnection[]`

## useInternalNode()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useInternalNode.ts)

This hook returns the internal representation of a specific node. Components that use this hook
will re-render **whenever any node changes**, including when a node is selected
or moved.

```jsx
import { useInternalNode } from '@xyflow/react';

export default function () {
  const internalNode = useInternalNode('node-1');
  const absolutePosition = internalNode.internals.positionAbsolute;

  return (
    <div>
      The absolute position of the node is at:
      <p>x: {absolutePosition.x}</p>
      <p>y: {absolutePosition.y}</p>
    </div>
  );
}
```

### Signature

This hook returns the internal representation of a specific node.
Components that use this hook will re-render **whenever the node changes**,
including when a node is selected or moved.

##### Parameters

* `id: string` The ID of a node you want to observe.

##### Returns

`InternalNode<NodeType> | undefined`

### TypeScript

This hook accepts a generic type argument of custom node types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const internalNode = useInternalNode<CustomNodeType>();
```

## useKeyPress()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useKeyPress.ts)

This hook lets you listen for specific key codes and tells you whether they are
currently pressed or not.

```jsx
import { useKeyPress } from '@xyflow/react';

export default function () {
  const spacePressed = useKeyPress('Space');
  const cmdAndSPressed = useKeyPress(['Meta+s', 'Strg+s']);

  return (
    <div>
      {spacePressed && <p>Space pressed!</p>}
      {cmdAndSPressed && <p>Cmd + S pressed!</p>}
    </div>
  );
}
```

### Signature

This hook lets you listen for specific key codes and tells you whether they are
currently pressed or not.

##### Parameters

* `keyCode?: KeyCode` The key code (string or array of strings) specifies which key(s) should trigger
  an action.

A **string** can represent:

* A **single key**, e.g. `'a'`
* A **key combination**, using `'+'` to separate keys, e.g. `'a+d'`

An  **array of strings** represents **multiple possible key inputs**. For example, `['a', 'd+s']`
means the user can press either the single key `'a'` or the combination of `'d'` and `'s'`.

* `options.target?: Window | Document | HTMLElement | ShadowRoot | null` Listen to key presses on a specific element.
* `options.actInsideInputWithModifier?: boolean` You can use this flag to prevent triggering the key press hook when an input field is focused.
* `options.preventDefault?: boolean`

##### Returns

`boolean`

### Notes

* This hook does not rely on a `ReactFlowInstance` so you are free to use it
  anywhere in your app!

## useNodeConnections()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodeConnections.ts)

This hook returns an array of connections on a specific node, handle type ('source', 'target') or handle ID.

```jsx
import { useNodeConnections } from '@xyflow/react';

export default function () {
  const connections = useNodeConnections({
    handleType: 'target',
    handleId: 'my-handle',
  });

  return (
    <div>There are currently {connections.length} incoming connections!</div>
  );
}
```

### Signature

This hook returns an array of connections on a specific node, handle type ('source', 'target') or handle ID.

##### Parameters

* `__0?: UseNodeConnectionsParams`

##### Returns

`NodeConnection[]`

## useNodeId()

[Source on Github](https://github.com/xyflow/xyflow/blob/v11/packages/core/src/contexts/NodeIdContext.ts/#L7)

You can use this hook to get the id of the node it is used inside. It is useful
if you need the node's id deeper in the render tree but don't want to manually
drill down the id as a prop.

```js
import { useNodeId } from '@xyflow/react';

export default function CustomNode() {
  return (
    <div>
      <span>This node has an id of </span>
      <NodeIdDisplay />
    </div>
  );
}

function NodeIdDisplay() {
  const nodeId = useNodeId();

  return <span>{nodeId}</span>;
}
```

### Signature

You can use this hook to get the id of the node it is used inside. It is useful
if you need the node's id deeper in the render tree but don't want to manually
drill down the id as a prop.

This function does not accept any parameters.

##### Returns

`string | null`

### Notes

* This hook should only be used within a custom node or its children.

## useNodesData()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodesData.ts)

This hook lets you subscribe to changes of a specific nodes `data` object.

```jsx
import { useNodesData } from '@xyflow/react';

export default function () {
  const nodeData = useNodesData('nodeId-1');

  const nodesData = useNodesData(['nodeId-1', 'nodeId-2']);
}
```

### Signature

This hook lets you subscribe to changes of a specific nodes `data` object.

##### Parameters

* `nodeId: string` The id of the node to get the data from.

##### Returns

`DistributivePick<NodeType, "id" | "type" | "data"> | null`

### TypeScript

This hook accepts a generic type argument of custom node types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const nodesData = useNodesData<NodesType>(['nodeId-1', 'nodeId-2']);
```

## useNodesInitialized()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodesInitialized.ts)

This hook tells you whether all the nodes in a flow have been measured and given
a width and height. When you add a node to the flow, this hook will return
`false` and then `true` again once the node has been measured.

```jsx
import { useReactFlow, useNodesInitialized } from '@xyflow/react';
import { useEffect, useState } from 'react';

const options = {
  includeHiddenNodes: false,
};

export default function useLayout() {
  const { getNodes } = useReactFlow();
  const nodesInitialized = useNodesInitialized(options);
  const [layoutedNodes, setLayoutedNodes] = useState(getNodes());

  useEffect(() => {
    if (nodesInitialized) {
      setLayoutedNodes(yourLayoutingFunction(getNodes()));
    }
  }, [nodesInitialized]);

  return layoutedNodes;
}
```

### Signature

This hook tells you whether all the nodes in a flow have been measured and given
a width and height. When you add a node to the flow, this hook will return
`false` and then `true` again once the node has been measured.

##### Parameters

* `options.includeHiddenNodes?: boolean`

##### Returns

`boolean`

### Notes

* This hook always returns `false` if the internal nodes array is empty.

## useNodesState()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodesEdgesState.ts)

This hook makes it easy to prototype a controlled flow where you manage the
state of nodes and edges outside the `ReactFlowInstance`. You can think of it
like React's `useState` hook with an additional helper callback.

```jsx
import { ReactFlow, useNodesState, useEdgesState } from '@xyflow/react';

const initialNodes = [];
const initialEdges = [];

export default function () {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
    />
  );
}
```

### Signature

This hook makes it easy to prototype a controlled flow where you manage the
state of nodes and edges outside the `ReactFlowInstance`. You can think of it
like React's `useState` hook with an additional helper callback.

##### Parameters

* `initialNodes: NodeType[]`

##### Returns

`[nodes: NodeType[], setNodes: Dispatch<SetStateAction<NodeType[]>>, onNodesChange: OnNodesChange<NodeType>]`

### TypeScript

This hook accepts a generic type argument of custom node types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const nodes = useNodesState<CustomNodeType>();
```

### Notes

* This hook was created to make prototyping easier and our documentation
  examples clearer. Although it is OK to use this hook in production, in
  practice you may want to use a more sophisticated state management solution
  like [Zustand](https://reactflow.dev/docs/guides/state-management/) instead.

## useNodes()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodes.ts)

This hook returns an array of the current nodes. Components that use this hook
will re-render **whenever any node changes**, including when a node is selected
or moved.

```jsx
import { useNodes } from '@xyflow/react';

export default function () {
  const nodes = useNodes();

  return <div>There are currently {nodes.length} nodes!</div>;
}
```

### Signature

This hook returns an array of the current nodes. Components that use this hook
will re-render **whenever any node changes**, including when a node is selected
or moved.

This function does not accept any parameters.

##### Returns

`NodeType[]`

### TypeScript

This hook accepts a generic type argument of custom node types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const nodes = useNodes<CustomNodeType>();
```

### Notes

* Relying on `useNodes` unnecessarily can be a common cause of performance
  issues. Whenever any node changes, this hook will cause the component to
  re-render. Often we actually care about something more specific, like when
  the *number* of nodes changes: where possible try to use
  [`useStore`](https://reactflow.dev/api-reference/hooks/use-store) instead.

## useOnSelectionChange()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useOnSelectionChange.ts)

This hook lets you listen for changes to both node and edge selection. As the
name implies, the callback you provide will be called whenever the selection of
*either* nodes or edges changes.

> \[!WARNING]
>
> You need to memoize the passed `onChange` handler, otherwise the hook will not
> work correctly.

```jsx
import { useState } from 'react';
import { ReactFlow, useOnSelectionChange } from '@xyflow/react';

function SelectionDisplay() {
  const [selectedNodes, setSelectedNodes] = useState([]);
  const [selectedEdges, setSelectedEdges] = useState([]);

  // the passed handler has to be memoized, otherwise the hook will not work correctly
  const onChange = useCallback(({ nodes, edges }) => {
    setSelectedNodes(nodes.map((node) => node.id));
    setSelectedEdges(edges.map((edge) => edge.id));
  }, []);

  useOnSelectionChange({
    onChange,
  });

  return (
    <div>
      <p>Selected nodes: {selectedNodes.join(', ')}</p>
      <p>Selected edges: {selectedEdges.join(', ')}</p>
    </div>
  );
}
```

### Signature

This hook lets you listen for changes to both node and edge selection. As the
name implies, the callback you provide will be called whenever the selection of
*either* nodes or edges changes.

##### Parameters

* `[0].onChange: OnSelectionChangeFunc<NodeType, EdgeType>` The handler to register.

##### Returns

`void`

### Notes

* This hook can only be used in a component that is a child of a
  [`<ReactFlowProvider />`](https://reactflow.dev/api-reference/react-flow-provider) or a
  [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow) component.

## useOnViewportChange()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useOnViewportChange.ts)

The `useOnViewportChange` hook lets you listen for changes to the viewport such
as panning and zooming. You can provide a callback for each phase of a viewport
change: `onStart`, `onChange`, and `onEnd`.

```tsx
import { useCallback } from 'react';
import { useOnViewportChange } from '@xyflow/react';

function ViewportChangeLogger() {
  useOnViewportChange({
    onStart: (viewport: Viewport) => console.log('start', viewport),
    onChange: (viewport: Viewport) => console.log('change', viewport),
    onEnd: (viewport: Viewport) => console.log('end', viewport),
  });

  return null;
}
```

### Signature

The `useOnViewportChange` hook lets you listen for changes to the viewport such
as panning and zooming. You can provide a callback for each phase of a viewport
change: `onStart`, `onChange`, and `onEnd`.

##### Parameters

* `[0].onStart?: OnViewportChange` Gets called when the viewport starts changing.
* `[0].onChange?: OnViewportChange` Gets called when the viewport changes.
* `[0].onEnd?: OnViewportChange` Gets called when the viewport stops changing.

##### Returns

`void`

### Notes

* This hook can only be used in a component that is a child of a
  [`<ReactFlowProvider />`](https://reactflow.dev/api-reference/react-flow-provider) or a
  [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow) component.

## useReactFlow()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useReactFlow.ts)

This hook returns a [`ReactFlowInstance`](https://reactflow.dev/api-reference/types/react-flow-instance) that can
be used to update nodes and edges, manipulate the viewport, or query the current
state of the flow.

```jsx
import { useCallback, useState } from 'react';
import { useReactFlow } from '@xyflow/react';

export function NodeCounter() {
  const reactFlow = useReactFlow();
  const [count, setCount] = useState(0);
  const countNodes = useCallback(() => {
    setCount(reactFlow.getNodes().length);
    // you need to pass it as a dependency if you are using it with useEffect or useCallback
    // because at the first render, it's not initialized yet and some functions might not work.
  }, [reactFlow]);

  return (
    <div>
      <button onClick={countNodes}>Update count</button>
      <p>There are {count} nodes in the flow.</p>
    </div>
  );
}
```

### Signature

This hook returns a ReactFlowInstance that can be used to update nodes and edges, manipulate the viewport, or query the current state of the flow.

This function does not accept any parameters.

##### Returns

`ReactFlowInstance<NodeType, EdgeType>`

### TypeScript

This hook accepts a generic type argument of custom node & edge types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const reactFlow = useReactFlow<CustomNodeType, CustomEdgeType>();
```

### Notes

* This hook can only be used in a component that is a child of a
  [`<ReactFlowProvider />`](https://reactflow.dev/api-reference/react-flow-provider) or a
  [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow) component.
* Unlike [`useNodes`](https://reactflow.dev/api-reference/hooks/use-nodes) or [`useEdges`](https://reactflow.dev/api-reference/hooks/use-edges), this hook won't
  cause your component to re-render when state changes. Instead, you can query
  the state when you need it by using methods on the [`ReactFlowInstance`](https://reactflow.dev/api-reference/types/react-flow-instance)
  this hook returns.

## useStoreApi()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useStore.ts)

In some cases, you might need to access the store directly. This hook returns the store object which can be used on demand to access the state or dispatch actions.

> \[!NOTE]
>
> This hook should only be used if there is no other way to access the internal
> state. For many of the common use cases, there are dedicated hooks available
> such as [`useReactFlow`](https://reactflow.dev/api-reference/hooks/use-react-flow),
> [`useViewport`](https://reactflow.dev/api-reference/hooks/use-viewport), etc.

```tsx
import { useState, useCallback } from 'react';
import { ReactFlow, useStoreApi } from '@xyflow/react';

const NodesLengthDisplay = () => {
  const [nodesLength, setNodesLength] = useState(0);
  const store = useStoreApi();

  const onClick = useCallback(() => {
    const { nodes } = store.getState();
    const length = nodes.length || 0;

    setNodesLength(length);
  }, [store]);

  return (
    <div>
      <p>The current number of nodes is: {nodesLength}</p>
      <button onClick={onClick}>Update node length.</button>
    </div>
  );
};

function Flow() {
  return (
    <ReactFlow nodes={nodes}>
      <NodesLengthDisplay />
    </ReactFlow>
  );
}
```

This example computes the number of nodes in the flow *on-demand*. This is in
contrast to the example in the [`useStore`](https://reactflow.dev/api-reference/hooks/use-store) hook that re-renders
the component whenever the number of nodes changes.

Choosing whether to calculate values on-demand or to subscribe to changes as they
happen is a bit of a balancing act. On the one hand, putting too many heavy
calculations in an event handler can make your app feel sluggish or unresponsive.
On the other hand, computing values eagerly can lead to slow or unnecessary
re-renders.

We make both this hook and [`useStore`](https://reactflow.dev/api-reference/hooks/use-store) available so that you can
choose the approach that works best for your use-case.

### Signature

In some cases, you might need to access the store directly. This hook returns the store object which can be used on demand to access the state or dispatch actions.

This function does not accept any parameters.

##### Returns

* `getState: () => ReactFlowState<NodeType, EdgeType>`
* `setState: (partial: ReactFlowState<NodeType, EdgeType> | Partial<ReactFlowState<NodeType, EdgeType>> | ((state: ReactFlowState<...>) => ReactFlowState<...> | Partial<...>), replace?: boolean | undefined) => void`
* `subscribe: (listener: (state: ReactFlowState<NodeType, EdgeType>, prevState: ReactFlowState<NodeType, EdgeType>) => void) => () => void`

### TypeScript

This hook accepts a generic type argument of custom node & edge types. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const store = useStoreApi<CustomNodeType, CustomEdgeType>();
```

## useStore()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useStore.ts)

This hook can be used to subscribe to internal state changes of the React Flow
component. The `useStore` hook is re-exported from the [Zustand](https://github.com/pmndrs/zustand)
state management library, so you should check out their docs for more details.

<Callout type="info">
  This hook should only be used if there is no other way to access the internal
  state. For many of the common use cases, there are dedicated hooks available
  such as [`useReactFlow`](https://reactflow.dev/api-reference/hooks/use-react-flow),
  [`useViewport`](https://reactflow.dev/api-reference/hooks/use-viewport), etc.
</Callout>

```jsx
import { ReactFlow, useStore } from '@xyflow/react';

const nodesLengthSelector = (state) =>
  state.nodes.length || 0;

const NodesLengthDisplay = () => {
  const nodesLength = useStore(nodesLengthSelector);

  return <div>The current number of nodes is: {nodesLength}</div>;
};

function Flow() {
  return (
    <ReactFlow nodes={[...]}>
      <NodesLengthDisplay />
    </ReactFlow>
  );
}
```

This example computes the number of nodes eagerly. Whenever the number of nodes
in the flow changes, the `<NodesLengthDisplay />` component will re-render. This
is in contrast to the example in the [`useStoreApi`](https://reactflow.dev/api-reference/hooks/use-store-api) hook that only
computes the number of nodes when a button is clicked.

Choosing whether to calculate values on-demand or to subscribe to changes as they
happen is a bit of a balancing act. On the one hand, putting too many heavy
calculations in an event handler can make your app feel sluggish or unresponsive.
On the other hand, computing values eagerly can lead to slow or unnecessary
re-renders.

We make both this hook and [`useStoreApi`](https://reactflow.dev/api-reference/hooks/use-store-api) available so that you
can choose the approach that works best for your use-case.

### Signature

This hook can be used to subscribe to internal state changes of the React Flow
component. The `useStore` hook is re-exported from the [Zustand](https://github.com/pmndrs/zustand)
state management library, so you should check out their docs for more details.

##### Parameters

* `selector: (state: ReactFlowState) => StateSlice` A selector function that returns a slice of the flow's internal state.
  Extracting or transforming just the state you need is a good practice to avoid unnecessary
  re-renders.
* `equalityFn?: (a: StateSlice, b: StateSlice) => boolean` A function to compare the previous and next value. This is incredibly useful
  for preventing unnecessary re-renders. Good sensible defaults are using `Object.is` or importing
  `zustand/shallow`, but you can be as granular as you like.

##### Returns

`StateSlice`

### Examples

#### Triggering store actions

You can manipulate the internal React Flow state by triggering internal actions
through the `useStore` hook. These actions are already used internally throughout
the library, but you can also use them to implement custom functionality.

```jsx
import { useStore } from '@xyflow/react';

const setMinZoomSelector = (state) => state.setMinZoom;

function MinZoomSetter() {
  const setMinZoom = useStore(setMinZoomSelector);

  return <button onClick={() => setMinZoom(6)}>set min zoom</button>;
}
```

### TypeScript

This hook can be typed by typing the selector function. See this
[section in our TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

```tsx
const nodes = useStore((s: ReactFlowState<CustomNodeType>) => s.nodes);
```

## useUpdateNodeInternals()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useUpdateNodeInternals.ts)

When you programmatically add or remove handles to a node or update a node's
handle position, you need to let React Flow know about it using this hook. This
will update the internal dimensions of the node and properly reposition handles
on the canvas if necessary.

```jsx
import { useCallback, useState } from 'react';
import { Handle, useUpdateNodeInternals } from '@xyflow/react';

export default function RandomHandleNode({ id }) {
  const updateNodeInternals = useUpdateNodeInternals();
  const [handleCount, setHandleCount] = useState(0);
  const randomizeHandleCount = useCallback(() => {
    setHandleCount(Math.floor(Math.random() * 10));
    updateNodeInternals(id);
  }, [id, updateNodeInternals]);

  return (
    <>
      {Array.from({ length: handleCount }).map((_, index) => (
        <Handle
          key={index}
          type="target"
          position="left"
          id={`handle-${index}`}
        />
      ))}

      <div>
        <button onClick={randomizeHandleCount}>Randomize handle count</button>
        <p>There are {handleCount} handles on this node.</p>
      </div>
    </>
  );
}
```

### Signature

When you programmatically add or remove handles to a node or update a node's
handle position, you need to let React Flow know about it using this hook. This
will update the internal dimensions of the node and properly reposition handles
on the canvas if necessary.

This function does not accept any parameters.

##### Returns

`UpdateNodeInternals`

### Notes

* This hook can only be used in a component that is a child of a
  [`<ReactFlowProvider />`](https://reactflow.dev/api-reference/react-flow-provider) or a
  [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow) component.

## useViewport()

[Source on GitHub](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useViewport.ts)

The `useViewport` hook is a convenient way to read the current state of the
[`Viewport`](https://reactflow.dev/api-reference/types/viewport) in a component. Components that use this hook
will re-render **whenever the viewport changes**.

```jsx
import { useViewport } from '@xyflow/react';

export default function ViewportDisplay() {
  const { x, y, zoom } = useViewport();

  return (
    <div>
      <p>
        The viewport is currently at ({x}, {y}) and zoomed to {zoom}.
      </p>
    </div>
  );
}
```

### Signature

The `useViewport` hook is a convenient way to read the current state of the
{@link Viewport } in a component. Components that use this hook
will re-render **whenever the viewport changes**.

This function does not accept any parameters.

##### Returns

* `x: number`
* `y: number`
* `zoom: number`

### Notes

* This hook can only be used in a component that is a child of a
  [`<ReactFlowProvider />`](https://reactflow.dev/api-reference/react-flow-provider) or a
  [`<ReactFlow />`](https://reactflow.dev/api-reference/react-flow) component.
