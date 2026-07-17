# Search And Minimap

## Graph Search

Install `@react-sigma/graph-search` with its peer dependencies.

```bash
npm install @react-sigma/graph-search minisearch react-select
```

Import the add-on CSS.

```tsx
import { GraphSearch, GraphSearchOption } from "@react-sigma/graph-search";
import "@react-sigma/graph-search/lib/style.css";
```

`GraphSearch` builds a MiniSearch index synchronized with the Graphology graph
inside `SigmaContainer`. It can search nodes, edges, or both depending on the
`type` prop.

```tsx
function NodeSearch() {
  const [selected, setSelected] = useState<GraphSearchOption | null>(null);

  return (
    <GraphSearch
      type="nodes"
      value={selected}
      onChange={setSelected}
      minisearchOptions={{ fields: ["label", "prop_tag"] }}
    />
  );
}
```

Node and edge attributes are indexed with the `prop_` prefix to avoid collisions.
For a node attribute named `tag`, search field `prop_tag`.

Use `postSearchResult(options)` to filter, rank, truncate, or append message
items to the result list.

```tsx
const postSearchResult = (options: GraphSearchOption[]) =>
  options.length <= 10
    ? options
    : [...options.slice(0, 10), { type: "message", message: "More results" }];
```

## Search Context

Use `GraphSearchContextProvider` when the application owns the index or when
multiple search inputs/result displays need shared state.

```tsx
import {
  GraphSearchContextProvider,
  GraphSearchInput,
  NodeById,
  useGraphSearch,
} from "@react-sigma/graph-search";

function SearchPanel() {
  const { selected } = useGraphSearch();
  return (
    <>
      <GraphSearchInput type="nodes" />
      {selected?.type === "nodes" ? <NodeById id={selected.id} /> : null}
    </>
  );
}

<GraphSearchContextProvider>
  <SearchPanel />
</GraphSearchContextProvider>;
```

Display helpers:

- `Node` and `Edge`: render result items passed as props.
- `NodeById` and `EdgeById`: render graph items by id/key.
- `GraphSearchInput`: lower-level input component.
- `useGraphSearch`: read and control search state from context.

All search components must be inside `SigmaContainer`.

## Minimap

Install `@react-sigma/minimap`.

```bash
npm install @react-sigma/minimap
```

```tsx
import { ControlsContainer } from "@react-sigma/core";
import { MiniMap } from "@react-sigma/minimap";

<ControlsContainer position="top-right">
  <MiniMap width="100px" height="100px" />
</ControlsContainer>;
```

Use a minimap when the graph is larger than the viewport or users need spatial
orientation while zooming and panning.
