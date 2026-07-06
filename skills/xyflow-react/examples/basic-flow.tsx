/**
 * Basic controlled flow: state via useNodesState/useEdgesState, new connections
 * via addEdge, plus the standard helper components.
 *
 * npm install @xyflow/react
 */
import { useCallback } from 'react';
import {
  ReactFlow,
  Background,
  BackgroundVariant,
  Controls,
  MiniMap,
  Panel,
  addEdge,
  useNodesState,
  useEdgesState,
  MarkerType,
  type Node,
  type Edge,
  type Connection,
} from '@xyflow/react';

// Required once in your app (imports the default node/edge/controls styling).
import '@xyflow/react/dist/style.css';

const initialNodes: Node[] = [
  {
    id: '1',
    type: 'input', // built-in types: 'input' | 'default' | 'output' | 'group'
    position: { x: 0, y: 0 },
    data: { label: 'Start' },
  },
  { id: '2', position: { x: -120, y: 120 }, data: { label: 'Step A' } },
  { id: '3', position: { x: 120, y: 120 }, data: { label: 'Step B' } },
  {
    id: '4',
    type: 'output',
    position: { x: 0, y: 240 },
    data: { label: 'Done' },
  },
];

const initialEdges: Edge[] = [
  { id: 'e1-2', source: '1', target: '2', animated: true },
  { id: 'e1-3', source: '1', target: '3' },
  {
    id: 'e2-4',
    source: '2',
    target: '4',
    label: 'merge',
    markerEnd: { type: MarkerType.ArrowClosed },
  },
];

export default function BasicFlow() {
  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  // Always memoize handlers (or define them outside the component) —
  // inline handlers can push React Flow into an infinite re-render loop.
  const onConnect = useCallback(
    (connection: Connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges],
  );

  return (
    // The parent of <ReactFlow /> must have explicit dimensions.
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        fitView
        fitViewOptions={{ padding: 0.2 }}
        snapToGrid
        snapGrid={[15, 15]}
      >
        <Background variant={BackgroundVariant.Dots} gap={15} />
        <Controls />
        <MiniMap zoomable pannable />
        <Panel position="top-left">Basic controlled flow</Panel>
      </ReactFlow>
    </div>
  );
}
