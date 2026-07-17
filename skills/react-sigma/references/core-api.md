# Core API

## SigmaContainer

`SigmaContainer` creates the Sigma renderer and provides React context for all
React Sigma hooks and controls. The container must have a visible size.

```tsx
<SigmaContainer
  graph={graph}
  settings={{
    allowInvalidContainer: true,
    defaultEdgeType: "arrow",
    labelRenderedSizeThreshold: 12,
  }}
  style={{ height: 500 }}
/>
```

`graph` can be:

- A Graphology graph instance, for example `new Graph()` or `Graph.from(data)`.
- A Graphology constructor, for example `graph={MultiDirectedGraph}`.
- Omitted, in which case React Sigma creates a default Graphology graph.

Use a constructor when descendants will load a graph and the backing graph class
matters, such as a directed multigraph with parallel edges.

## Graph Loading

Use the `graph` prop for a ready graph. Use `useLoadGraph()` when the graph is
created after mount, fetched, generated, or rebuilt from UI state.

```tsx
function Loader({ data }: { data: SerializedGraph }) {
  const loadGraph = useLoadGraph();

  useEffect(() => {
    loadGraph(Graph.from(data));
  }, [data, loadGraph]);

  return null;
}
```

Required node attributes for visible graphs: numeric `x`, `y`, and `size`.
Typical attributes are `label`, `color`, and custom fields for search/filtering.

## Hooks

- `useSigma()`: returns the Sigma instance; use for graph, camera, coordinate,
  and renderer access.
- `useSigmaContext()`: returns the React Sigma context object.
- `useLoadGraph()`: returns a function that replaces the graph in Sigma.
- `useRegisterEvents()`: registers Sigma event handlers.
- `useCamera()`: camera helpers for moving, zooming, and reading camera state.
- `useFullScreen()`: fullscreen state and toggling helpers.
- `useSetSettings()`: updates Sigma settings from React.

All hooks must run inside a descendant of `SigmaContainer`.

## Controls

```tsx
<ControlsContainer position="bottom-right">
  <ZoomControl />
  <FullScreenControl />
</ControlsContainer>
```

`ControlsContainer` positions: `top-right`, `top-left`, `bottom-right`,
`bottom-left`.

`ZoomControl` supports children for zoom in, zoom out, and reset, plus labels
for I18N. `FullScreenControl` supports children for enter and exit fullscreen.
Worker layout controls use children for start/stop states.

## Events

Register events in an effect and keep dependencies stable.

```tsx
function Events() {
  const registerEvents = useRegisterEvents();

  useEffect(() => {
    registerEvents({
      clickNode: ({ node }) => console.log("node", node),
      enterEdge: ({ edge }) => console.log("edge", edge),
      clickStage: ({ event }) => console.log("stage", event),
      updated: ({ x, y, ratio }) => console.log("camera", x, y, ratio),
    });
  }, [registerEvents]);

  return null;
}
```

Common event groups: node events, edge events, stage events, mouse events,
touch events, lifecycle events (`kill`, `resize`, `beforeRender`,
`afterRender`), and camera `updated`.

## External Sigma Access

Prefer descendants and hooks. If the app must coordinate with external state,
forward a ref through `SigmaContainer` and treat the value as the low-level
Sigma instance. Use this only when you know the Sigma API because it bypasses
the normal hook boundary.
