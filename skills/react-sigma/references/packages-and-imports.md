# Packages And Imports

Keep all `@react-sigma/*` packages on the same version. Version `5.0.6` was
current in the npm registry on 2026-07-17.

## Core

```bash
npm install @react-sigma/core sigma graphology
```

`@react-sigma/core` peer dependencies: `graphology ^0.26.0`, `react ^18.0.0 ||
^19.0.0`, `sigma ^3.0.2`.

```ts
import {
  ControlsContainer,
  FullScreenControl,
  SigmaContainer,
  ZoomControl,
  useCamera,
  useFullScreen,
  useLoadGraph,
  useRegisterEvents,
  useSetSettings,
  useSigma,
  useSigmaContext,
} from "@react-sigma/core";
import "@react-sigma/core/lib/style.css";
```

Core exports also include `debounce`, `isEqual`, `EventHandlers`, `GraphType`,
`ControlsContainerProps`, `FullScreenControlProps`, `SigmaContainerProps`,
`SigmaContextInterface`, and `ZoomControlProps`.

## Graph Search

```bash
npm install @react-sigma/graph-search minisearch react-select
```

`@react-sigma/graph-search` depends on `@react-sigma/core` and peers on
`minisearch ^7.1.1` and `react-select ^5.9.0`.

```ts
import {
  Edge,
  EdgeById,
  GraphSearch,
  GraphSearchContextProvider,
  GraphSearchInput,
  Node,
  NodeById,
  useGraphSearch,
} from "@react-sigma/graph-search";
import "@react-sigma/graph-search/lib/style.css";
```

Types: `Document`, `GraphSearchOption`, `ItemType`, `LabelKeys`, `Labels`,
`GraphSearchContextProviderProps`, `GraphSearchContextType`,
`GraphSearchInputProps`, `NodeProps`, `OptionItem`, and `OptionMessage`.

## Layout Packages

```bash
npm install @react-sigma/layout-core
npm install @react-sigma/layout-random graphology-layout
npm install @react-sigma/layout-circular graphology-layout
npm install @react-sigma/layout-circlepack graphology-layout
npm install @react-sigma/layout-force graphology-layout-force
npm install @react-sigma/layout-forceatlas2 graphology-layout-forceatlas2
npm install @react-sigma/layout-noverlap graphology-layout-noverlap
```

`@react-sigma/layout-core` exports `useLayoutFactory`,
`useWorkerLayoutFactory`, and `WorkerLayoutControl`. It also exports
`GraphologyLayout`, `GraphologyWorkerLayout`, `WorkerLayoutControlProps`,
`LayoutHook`, and `LayoutWorkerHook`.

Package exports:

- `@react-sigma/layout-random`: `useLayoutRandom`
- `@react-sigma/layout-circular`: `useLayoutCircular`
- `@react-sigma/layout-circlepack`: `useLayoutCirclepack`
- `@react-sigma/layout-force`: `useLayoutForce`, `useWorkerLayoutForce`,
  `LayoutForceControl`, `LayoutForceControlProps`
- `@react-sigma/layout-forceatlas2`: `useLayoutForceAtlas2`,
  `useWorkerLayoutForceAtlas2`, `LayoutForceAtlas2Control`,
  `LayoutForceAtlas2ControlProps`
- `@react-sigma/layout-noverlap`: `useLayoutNoverlap`,
  `useWorkerLayoutNoverlap`, `LayoutNoverlapControl`,
  `LayoutNoverlapControlProps`

## Minimap

```bash
npm install @react-sigma/minimap
```

```ts
import { MiniMap, MiniMapProps } from "@react-sigma/minimap";
```

`@react-sigma/minimap` depends on `@react-sigma/core`.
