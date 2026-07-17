---
name: react-sigma
description: >-
  Build, configure, debug, or refactor React graph visualization code with
  `@react-sigma/*`. Trigger WHENEVER the user installs or imports
  `@react-sigma/core`, `SigmaContainer`, `useSigma`, `useLoadGraph`,
  `useRegisterEvents`, `@react-sigma/graph-search`,
  `@react-sigma/minimap`, or any `@react-sigma/layout-*` package; uses
  graphology graphs, Sigma settings, controls, events, layouts, workers,
  search, minimap, drag and drop, external Sigma state, multigraphs,
  parallel edges, and fixes blank containers, missing coordinates, worker
  cleanup, CSS imports, React 18/19 peer dependencies, and graphology/sigma
  integration issues.
---

# react-sigma

Use this skill for React graph visualizations built with `@react-sigma/*`, the
React bindings around Sigma.js and Graphology. The documentation and npm
registry showed `@react-sigma/* 5.0.6` on 2026-07-17.

```bash
npm ls @react-sigma/core sigma graphology react
npm view @react-sigma/core version peerDependencies
```

## Default Workflow

1. Identify the package surface: core rendering, controls/events, layouts,
   graph search, minimap, or advanced Sigma access.
2. Check installed versions of `@react-sigma/*`, `sigma`, `graphology`, and
   React. Keep all `@react-sigma/*` packages on the same version.
3. Render a `SigmaContainer` with a fixed non-zero height and import
   `@react-sigma/core/lib/style.css`.
4. Use a Graphology graph instance or constructor. Every displayed node needs
   numeric `x`, `y`, and `size`; labels and colors are normal node attributes.
5. Call React Sigma hooks only inside descendants of `SigmaContainer`.
6. Use `useLoadGraph()` for dynamically built or fetched graphs; use the
   `graph` prop for an existing graph instance or graph constructor.
7. For iterative layouts, prefer worker hooks/controls and stop or kill workers
   during unmount or when switching graphs.
8. For package add-ons, install required peer packages and import add-on CSS
   when the reference says so.

## Minimal Graph

```tsx
import { SigmaContainer, useLoadGraph } from "@react-sigma/core";
import "@react-sigma/core/lib/style.css";
import Graph from "graphology";
import { useEffect } from "react";

function LoadGraph() {
  const loadGraph = useLoadGraph();

  useEffect(() => {
    const graph = new Graph();
    graph.addNode("a", { x: 0, y: 0, size: 10, label: "A" });
    graph.addNode("b", { x: 1, y: 1, size: 10, label: "B" });
    graph.addEdge("a", "b");
    loadGraph(graph);
  }, [loadGraph]);

  return null;
}

export function GraphView() {
  return (
    <SigmaContainer style={{ height: 420 }}>
      <LoadGraph />
    </SigmaContainer>
  );
}
```

## Decision Rules

- Do not call `useSigma()`, `useLoadGraph()`, `useRegisterEvents()`, or layout
  hooks outside `SigmaContainer`.
- Do not pass a plain object as a graph; convert serialized data with
  `Graph.from(serializedGraph)` or build a Graphology instance.
- Use a graph constructor in `SigmaContainer graph={MultiDirectedGraph}` when
  the graph needs parallel edges or directed multigraph behavior.
- Use Sigma settings for renderer behavior: `defaultNodeType`,
  `defaultEdgeType`, `nodeProgramClasses`, `edgeProgramClasses`, labels,
  z-index, and camera/interaction settings.
- Use `ControlsContainer` for built-in and add-on controls; valid positions are
  `top-right`, `top-left`, `bottom-right`, and `bottom-left`.
- For search, index custom attributes through `prop_<attributeName>`.
- For drag and drop, convert viewport coordinates to graph coordinates with
  `sigma.viewportToGraph(event)` and prevent Sigma camera movement while
  dragging.

## References

- Read [references/packages-and-imports.md](references/packages-and-imports.md)
  for every `@react-sigma/*` package, install commands, peer dependencies, and
  public exports.
- Read [references/core-api.md](references/core-api.md) for `SigmaContainer`,
  hooks, controls, events, settings, graph loading, and external Sigma access.
- Read [references/layouts.md](references/layouts.md) for layout packages,
  regular hooks, worker hooks, worker controls, and factory APIs.
- Read [references/search-and-minimap.md](references/search-and-minimap.md)
  for graph search, search context, result display, minisearch options, and
  minimap usage.
- Read [references/examples-core.md](references/examples-core.md) for load
  graph, events, drag-and-drop, controls, and external-state examples.
- Read [references/examples-addons.md](references/examples-addons.md) for
  layouts, graph search, minimap, multigraph, and parallel-edge examples.
