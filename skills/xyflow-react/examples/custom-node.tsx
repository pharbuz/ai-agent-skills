/**
 * Custom node with typed data, source/target handles, and an input that
 * writes back into the node's data via updateNodeData (useReactFlow).
 */
import { memo, useCallback } from 'react';
import {
  ReactFlow,
  ReactFlowProvider,
  Background,
  Handle,
  Position,
  useNodesState,
  useEdgesState,
  useReactFlow,
  type Node,
  type NodeProps,
  type NodeTypes,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';

// Type the node: custom data + the `type` string it is registered under.
type TextNode = Node<{ text: string }, 'text'>;

const TextNodeComponent = memo(({ id, data, selected }: NodeProps<TextNode>) => {
  const { updateNodeData } = useReactFlow();

  const onChange = useCallback(
    (evt: React.ChangeEvent<HTMLInputElement>) =>
      // Merged into existing data by default; { replace: true } to overwrite.
      updateNodeData(id, { text: evt.target.value }),
    [id, updateNodeData],
  );

  return (
    <div
      style={{
        padding: 10,
        borderRadius: 6,
        background: 'white',
        border: `1px solid ${selected ? '#ff0071' : '#ddd'}`,
      }}
    >
      <Handle type="target" position={Position.Top} />
      <label style={{ display: 'block', fontSize: 10 }}>text</label>
      {/* "nodrag" stops node dragging while interacting with the input */}
      <input className="nodrag" value={data.text} onChange={onChange} />
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
});

// Must be referentially stable — define outside the component (or useMemo),
// otherwise React Flow re-creates all nodes on every render (warning 002).
const nodeTypes: NodeTypes = { text: TextNodeComponent };

const initialNodes: TextNode[] = [
  { id: '1', type: 'text', position: { x: 0, y: 0 }, data: { text: 'hello' } },
  { id: '2', type: 'text', position: { x: 0, y: 140 }, data: { text: 'world' } },
];

function Flow() {
  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([
    { id: 'e1-2', source: '1', target: '2' },
  ]);

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      nodeTypes={nodeTypes}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      fitView
    >
      <Background />
    </ReactFlow>
  );
}

export default function CustomNodeExample() {
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      {/* Provider lets useReactFlow work anywhere in the tree */}
      <ReactFlowProvider>
        <Flow />
      </ReactFlowProvider>
    </div>
  );
}
