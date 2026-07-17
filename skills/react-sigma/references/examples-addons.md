# Add-On Examples

These examples cover the documentation pages for layouts, graph search,
minimap, multigraphs, and parallel edges.

## Circular Layout

```tsx
import { useLayoutCircular } from "@react-sigma/layout-circular";

function LayoutCircular() {
  const { assign } = useLayoutCircular();

  useEffect(() => {
    assign();
  }, [assign]);

  return null;
}
```

## ForceAtlas2 Control

```tsx
import { ControlsContainer, SigmaContainer } from "@react-sigma/core";
import { LayoutForceAtlas2Control } from "@react-sigma/layout-forceatlas2";

export function ForceAtlas2Graph({ graph }: { graph: Graph }) {
  return (
    <SigmaContainer graph={graph} style={{ height: 500 }}>
      <ControlsContainer position="bottom-right">
        <LayoutForceAtlas2Control settings={{ settings: { slowDown: 10 } }} />
      </ControlsContainer>
    </SigmaContainer>
  );
}
```

## Worker Layout Hook

```tsx
function AutoForceAtlas2() {
  const { start, stop, kill, isRunning } = useWorkerLayoutForceAtlas2({
    settings: { slowDown: 10 },
  });

  useEffect(() => {
    start();
    return () => {
      stop();
      kill();
    };
  }, [kill, start, stop]);

  return <button onClick={isRunning ? stop : start}>{isRunning ? "Stop" : "Start"}</button>;
}
```

## Graph Search

```tsx
import { GraphSearch, GraphSearchOption } from "@react-sigma/graph-search";
import "@react-sigma/graph-search/lib/style.css";

function SearchControl() {
  const [selectedNode, setSelectedNode] = useState<string | null>(null);
  const [focusNode, setFocusNode] = useState<string | null>(null);

  const onFocus = (value: GraphSearchOption | null) =>
    setFocusNode(value?.type === "nodes" ? value.id : null);

  const onChange = (value: GraphSearchOption | null) =>
    setSelectedNode(value?.type === "nodes" ? value.id : null);

  return (
    <GraphSearch
      type="nodes"
      value={selectedNode ? { type: "nodes", id: selectedNode } : null}
      onFocus={onFocus}
      onChange={onChange}
      minisearchOptions={{ fields: ["label", "prop_tag"] }}
    />
  );
}
```

Pair search with a focus helper that uses `useSigma()` and camera methods to
move to the selected node.

## Minimap

```tsx
import { MiniMap } from "@react-sigma/minimap";

<ControlsContainer position="top-right">
  <MiniMap width="100px" height="100px" />
</ControlsContainer>;
```

## Multigraph And Parallel Edges

```tsx
import EdgeCurveProgram, {
  DEFAULT_EDGE_CURVATURE,
  indexParallelEdgesIndex,
} from "@sigma/edge-curve";
import { MultiDirectedGraph } from "graphology";
import { EdgeArrowProgram } from "sigma/rendering";

const graph = new MultiDirectedGraph();
graph.addNode("a", { x: 0, y: 0, size: 8, label: "A" });
graph.addNode("b", { x: 1, y: 1, size: 8, label: "B" });
graph.addEdge("a", "b");
graph.addEdge("a", "b");
graph.addEdge("b", "a");

indexParallelEdgesIndex(graph, {
  edgeIndexAttribute: "parallelIndex",
  edgeMaxIndexAttribute: "parallelMaxIndex",
});

graph.forEachEdge((edge, attrs) => {
  if (typeof attrs.parallelIndex === "number") {
    graph.mergeEdgeAttributes(edge, {
      type: "curved",
      curvature:
        DEFAULT_EDGE_CURVATURE +
        (3 * DEFAULT_EDGE_CURVATURE * attrs.parallelIndex) /
          (attrs.parallelMaxIndex || 1),
    });
  } else {
    graph.setEdgeAttribute(edge, "type", "straight");
  }
});

<SigmaContainer
  graph={graph}
  settings={{
    renderEdgeLabels: true,
    defaultEdgeType: "straight",
    edgeProgramClasses: {
      straight: EdgeArrowProgram,
      curved: EdgeCurveProgram,
    },
  }}
/>;
```
