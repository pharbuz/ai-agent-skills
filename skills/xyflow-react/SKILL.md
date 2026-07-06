---
name: xyflow-react
description: >-
  Build node-based UIs (flowcharts, diagrams, visual editors, workflow builders)
  with React Flow v12 — the `@xyflow/react` package (formerly `reactflow`).
  Trigger WHENEVER the user imports from `@xyflow/react` or `reactflow`; renders
  a `<ReactFlow />` or `<ReactFlowProvider />` component; works with `Node` /
  `Edge` objects, `nodeTypes` / `edgeTypes`, or custom nodes and edges with
  `<Handle />`, `NodeProps`, `EdgeProps`, `<BaseEdge />`, or
  `<EdgeLabelRenderer />`; wires state with `useNodesState`, `useEdgesState`,
  `onNodesChange`, `onEdgesChange`, `onConnect`, `applyNodeChanges`,
  `applyEdgeChanges`, or `addEdge`; calls `useReactFlow()` or any
  `ReactFlowInstance` method (`fitView`, `setCenter`, `screenToFlowPosition`,
  `updateNodeData`, `deleteElements`, `getIntersectingNodes`…); uses helper
  components (`<Background />`, `<Controls />`, `<MiniMap />`, `<Panel />`,
  `<NodeResizer />`, `<NodeToolbar />`, `<ViewportPortal />`); uses hooks like
  `useConnection`, `useNodeConnections`, `useNodesData`, `useStore`,
  `useKeyPress`, `useUpdateNodeInternals`, `useViewport`; or renders edge paths
  with `getBezierPath` / `getSmoothStepPath` / `getStraightPath`. Covers the
  full reactflow.dev API reference: the ReactFlow component props, all built-in
  components, hooks, types, and util functions.
---

# xyflow-react — React Flow (@xyflow/react)

React Flow builds interactive node-based UIs: flowcharts, diagrams, visual
programming tools, workflow editors. Since v12 the package is `@xyflow/react`
(the old `reactflow` package is v11 and legacy — prefer `@xyflow/react`,
current: v12.x).

```bash
npm install @xyflow/react
```

```tsx
import { useCallback } from 'react';
import {
  ReactFlow, Background, Controls, MiniMap,
  useNodesState, useEdgesState, addEdge,
  type Node, type Edge, type Connection,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';   // required once, or base.css for headless styling

const initialNodes: Node[] = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'Hello' } },
  { id: '2', position: { x: 0, y: 100 }, data: { label: 'World' } },
];
const initialEdges: Edge[] = [{ id: 'e1-2', source: '1', target: '2' }];

export default function Flow() {
  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const onConnect = useCallback(
    (conn: Connection) => setEdges((eds) => addEdge(conn, eds)),
    [setEdges],
  );

  return (
    <div style={{ width: '100vw', height: '100vh' }}>  {/* parent needs dimensions */}
      <ReactFlow
        nodes={nodes} edges={edges}
        onNodesChange={onNodesChange} onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        fitView
      >
        <Background />
        <Controls />
        <MiniMap />
      </ReactFlow>
    </div>
  );
}
```

## Core concepts

- **Controlled flow**: you own `nodes`/`edges` state and pass `onNodesChange` /
  `onEdgesChange` / `onConnect` (usually via `useNodesState` / `useEdgesState`
  or `applyNodeChanges` / `applyEdgeChanges` + `addEdge`). **Uncontrolled**: pass
  `defaultNodes` / `defaultEdges` and React Flow manages state itself.
- **Custom nodes**: map a `type` string to a component in `nodeTypes`
  (define the object **outside** the component or memoize it). The component
  receives `NodeProps` (`id`, `data`, `selected`, `dragging`…) and renders
  `<Handle type="source|target" position={Position.X} />` connection points.
- **Custom edges**: map `type` in `edgeTypes`; component receives `EdgeProps`,
  computes a path with `getBezierPath` / `getSmoothStepPath` /
  `getStraightPath`, renders `<BaseEdge path={...} />` and optionally
  `<EdgeLabelRenderer>` for div-based labels.
- **Instance access**: `useReactFlow()` returns the `ReactFlowInstance`
  (`fitView`, `setCenter`, `screenToFlowPosition`, `updateNode(Data)`,
  `addNodes`, `deleteElements`, `getIntersectingNodes`…). It requires a
  `<ReactFlowProvider>` ancestor (or being inside `<ReactFlow>`).
- **Event handlers defined inline cause re-render loops** — declare them with
  `useCallback` or outside the component.
- Node `width`/`height` are measured and read-only; positions are in flow
  coordinates — convert screen coords with `screenToFlowPosition` (e.g. for
  drag-and-drop from a sidebar).

## Gotchas

- Import CSS once: `@xyflow/react/dist/style.css` (or `dist/base.css` minimal).
- The `<ReactFlow />` parent container must have an explicit width and height.
- `nodeTypes` / `edgeTypes` objects must be referentially stable, otherwise
  React Flow warns (error 002) and recreates all nodes.
- Hooks like `useReactFlow`, `useNodes`, `useStore` need `<ReactFlowProvider>`
  when used outside the `<ReactFlow>` component tree.
- After adding/removing handles programmatically, call
  `useUpdateNodeInternals()(nodeId)` so edges reposition.
- v11 → v12: package renamed `reactflow` → `@xyflow/react`; `onEdgeUpdate` →
  `onReconnect`; `updateEdge` util → `reconnectEdge`; `project()` →
  `screenToFlowPosition()`; `getRectOfNodes` → `getNodesBounds`;
  `node.width/height` are measured values, use `node.measured` in v12 handlers.

## Reference files

Full API documentation mirrored from <https://reactflow.dev/api-reference>
(React Flow v12):

- [references/react-flow-component.md](references/react-flow-component.md) —
  `<ReactFlow />` props (common, viewport, edge, event handlers, interaction,
  connection line, keyboard, style) and `<ReactFlowProvider />`.
- [references/components.md](references/components.md) — built-in components:
  `<Background />`, `<BaseEdge />`, `<ControlButton />`, `<Controls />`,
  `<EdgeLabelRenderer />`, `<EdgeText />`, `<EdgeToolbar />`, `<Handle />`,
  `<MiniMap />`, `<NodeResizeControl />`, `<NodeResizer />`, `<NodeToolbar />`,
  `<Panel />`, `<ViewportPortal />`.
- [references/hooks.md](references/hooks.md) — all hooks: `useConnection`,
  `useEdges(State)`, `useHandleConnections` (deprecated → `useNodeConnections`),
  `useInternalNode`, `useKeyPress`, `useNodeConnections`, `useNodeId`,
  `useNodes(State)`, `useNodesData`, `useNodesInitialized`,
  `useOnSelectionChange`, `useOnViewportChange`, `useReactFlow`, `useStore`,
  `useStoreApi`, `useUpdateNodeInternals`, `useViewport`.
- [references/types.md](references/types.md) — all types: `Node`, `Edge`,
  `NodeProps`, `EdgeProps`, `Connection`, `NodeChange` / `EdgeChange`,
  `ReactFlowInstance` (all methods), `Viewport`, `FitViewOptions`,
  `InternalNode`, `MarkerType`, `Position`, enums and callback types (`On*`).
- [references/utils.md](references/utils.md) — util functions: `addEdge`,
  `applyNodeChanges`, `applyEdgeChanges`, `getBezierPath`,
  `getSimpleBezierPath`, `getSmoothStepPath`, `getStraightPath`,
  `getConnectedEdges`, `getIncomers`, `getOutgoers`, `getNodesBounds`,
  `getViewportForBounds`, `isNode`, `isEdge`, `reconnectEdge`.

## Examples

- [examples/basic-flow.tsx](examples/basic-flow.tsx) — controlled flow with
  `useNodesState` / `useEdgesState`, Background, Controls, MiniMap.
- [examples/custom-node.tsx](examples/custom-node.tsx) — typed custom node with
  handles, `nodeTypes`, and `updateNodeData` from `useReactFlow`.
- [examples/custom-edge.tsx](examples/custom-edge.tsx) — custom edge with
  `getBezierPath`, `<BaseEdge />`, `<EdgeLabelRenderer />` and an edge button.
