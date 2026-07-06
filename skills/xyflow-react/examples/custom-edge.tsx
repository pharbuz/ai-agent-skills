/**
 * Custom edge: bezier path via getBezierPath + <BaseEdge />, with a div-based
 * delete button positioned on the edge through <EdgeLabelRenderer />.
 */
import { useCallback } from 'react';
import {
  ReactFlow,
  Background,
  BaseEdge,
  EdgeLabelRenderer,
  getBezierPath,
  useNodesState,
  useEdgesState,
  useReactFlow,
  ReactFlowProvider,
  addEdge,
  type Connection,
  type Edge,
  type EdgeProps,
  type EdgeTypes,
  type Node,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';

function ButtonEdge({
  id,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  markerEnd,
  style,
}: EdgeProps) {
  const { setEdges } = useReactFlow();
  const [edgePath, labelX, labelY] = getBezierPath({
    sourceX,
    sourceY,
    sourcePosition,
    targetX,
    targetY,
    targetPosition,
  });

  return (
    <>
      {/* BaseEdge renders the visible path + invisible interaction helper */}
      <BaseEdge id={id} path={edgePath} markerEnd={markerEnd} style={style} />
      {/* Edges are SVG — EdgeLabelRenderer portals into a div layer on top */}
      <EdgeLabelRenderer>
        <button
          className="nodrag nopan"
          style={{
            position: 'absolute',
            transform: `translate(-50%, -50%) translate(${labelX}px, ${labelY}px)`,
            pointerEvents: 'all', // labels ignore pointer events by default
          }}
          onClick={() => setEdges((edges) => edges.filter((e) => e.id !== id))}
        >
          ×
        </button>
      </EdgeLabelRenderer>
    </>
  );
}

// Referentially stable, like nodeTypes.
const edgeTypes: EdgeTypes = { button: ButtonEdge };

const initialNodes: Node[] = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'Node 1' } },
  { id: '2', position: { x: 200, y: 150 }, data: { label: 'Node 2' } },
];

const initialEdges: Edge[] = [
  { id: 'e1-2', source: '1', target: '2', type: 'button' },
];

function Flow() {
  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (connection: Connection) =>
      // New edges also get the custom type
      setEdges((eds) => addEdge({ ...connection, type: 'button' }, eds)),
    [setEdges],
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      edgeTypes={edgeTypes}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      fitView
    >
      <Background />
    </ReactFlow>
  );
}

export default function CustomEdgeExample() {
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlowProvider>
        <Flow />
      </ReactFlowProvider>
    </div>
  );
}
