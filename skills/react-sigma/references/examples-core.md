# Core Examples

These examples mirror the documentation example pages and storybook examples,
but are written as compact application patterns.

## Load Graph With Prop

```tsx
import { SigmaContainer } from "@react-sigma/core";
import "@react-sigma/core/lib/style.css";
import { MultiDirectedGraph } from "graphology";

const graph = new MultiDirectedGraph();
graph.addNode("A", { x: 0, y: 0, label: "Node A", size: 10 });
graph.addNode("B", { x: 1, y: 1, label: "Node B", size: 10 });
graph.addEdgeWithKey("rel1", "A", "B", { label: "REL_1" });

export function LoadGraphWithProp() {
  return <SigmaContainer graph={graph} style={{ height: 400 }} />;
}
```

## Load Graph With Hook

```tsx
function MyGraph() {
  const loadGraph = useLoadGraph();

  useEffect(() => {
    const graph = new MultiDirectedGraph();
    graph.addNode("A", { x: 0, y: 0, label: "Node A", size: 10 });
    graph.addNode("B", { x: 1, y: 1, label: "Node B", size: 10 });
    graph.addEdgeWithKey("rel1", "A", "B");
    loadGraph(graph);
  }, [loadGraph]);

  return null;
}
```

## Events

```tsx
function GraphEvents() {
  const registerEvents = useRegisterEvents();

  useEffect(() => {
    registerEvents({
      clickNode: ({ node }) => console.log("clickNode", node),
      doubleClickNode: ({ node }) => console.log("doubleClickNode", node),
      rightClickNode: ({ node }) => console.log("rightClickNode", node),
      enterNode: ({ node }) => console.log("enterNode", node),
      leaveNode: ({ node }) => console.log("leaveNode", node),
      clickEdge: ({ edge }) => console.log("clickEdge", edge),
      clickStage: ({ event }) => console.log("clickStage", event),
      mousemove: ({ x, y }) => console.log("mousemove", x, y),
      touchmove: ({ touches }) => console.log("touchmove", touches),
      updated: ({ x, y, ratio }) => console.log("camera", x, y, ratio),
      beforeRender: () => console.log("beforeRender"),
      afterRender: () => console.log("afterRender"),
      resize: () => console.log("resize"),
      kill: () => console.log("kill"),
    });
  }, [registerEvents]);

  return null;
}
```

## Drag And Drop

```tsx
function DragAndDrop() {
  const registerEvents = useRegisterEvents();
  const sigma = useSigma();
  const [draggedNode, setDraggedNode] = useState<string | null>(null);

  useEffect(() => {
    registerEvents({
      downNode: ({ node }) => {
        setDraggedNode(node);
        sigma.getGraph().setNodeAttribute(node, "highlighted", true);
      },
      mousemovebody: (event) => {
        if (!draggedNode) return;
        const pos = sigma.viewportToGraph(event);
        sigma.getGraph().mergeNodeAttributes(draggedNode, { x: pos.x, y: pos.y });
        event.preventSigmaDefault();
        event.original.preventDefault();
        event.original.stopPropagation();
      },
      mouseup: () => {
        if (!draggedNode) return;
        sigma.getGraph().removeNodeAttribute(draggedNode, "highlighted");
        setDraggedNode(null);
      },
      mousedown: () => {
        if (!sigma.getCustomBBox()) sigma.setCustomBBox(sigma.getBBox());
      },
    });
  }, [draggedNode, registerEvents, sigma]);

  return null;
}
```

## Controls

```tsx
<ControlsContainer position="bottom-right">
  <ZoomControl labels={{ zoomIn: "Plus", zoomOut: "Minus", reset: "Reset" }} />
  <FullScreenControl labels={{ enter: "Fullscreen", exit: "Exit fullscreen" }} />
</ControlsContainer>
```

For custom rendering, pass children to `ZoomControl`, `FullScreenControl`, or a
worker layout control instead of relying on the default icons.

## External State

Use external refs sparingly.

```tsx
const sigmaRef = useRef<Sigma | null>(null);

<SigmaContainer ref={sigmaRef} style={{ height: 400 }}>
  <GraphLoader />
</SigmaContainer>;
```

Prefer hook-based child components unless another system truly needs the Sigma
instance outside the graph tree.
