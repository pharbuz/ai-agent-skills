# Layouts

React Sigma layout packages wrap Graphology layout algorithms.

## Non-Iterative Layouts

Non-iterative hooks compute positions once and return `{ positions, assign }`.
Call `assign()` to write coordinates back to the graph.

```tsx
import { useLayoutCircular } from "@react-sigma/layout-circular";
import { useEffect } from "react";

function CircularLayout() {
  const { assign } = useLayoutCircular();

  useEffect(() => {
    assign();
  }, [assign]);

  return null;
}
```

Packages:

- `@react-sigma/layout-random`: `useLayoutRandom`
- `@react-sigma/layout-circular`: `useLayoutCircular`
- `@react-sigma/layout-circlepack`: `useLayoutCirclepack`

## Iterative Layouts

Regular iterative hooks expose the same `{ positions, assign }` shape but can
be expensive on large graphs. Prefer worker APIs for live layouts.

```tsx
import { useLayoutForceAtlas2 } from "@react-sigma/layout-forceatlas2";

function AssignForceAtlas2() {
  const { assign } = useLayoutForceAtlas2({
    settings: { slowDown: 10 },
  });

  return <button onClick={assign}>Layout</button>;
}
```

Iterative packages:

- `@react-sigma/layout-force`: `useLayoutForce`
- `@react-sigma/layout-forceatlas2`: `useLayoutForceAtlas2`
- `@react-sigma/layout-noverlap`: `useLayoutNoverlap`

## Worker Layouts

Worker hooks return `{ stop, start, kill, isRunning }`.

```tsx
import { useWorkerLayoutForceAtlas2 } from "@react-sigma/layout-forceatlas2";
import { useEffect } from "react";

function ForceAtlas2Worker() {
  const { start, stop, kill, isRunning } = useWorkerLayoutForceAtlas2({
    settings: { slowDown: 10 },
  });

  useEffect(() => {
    start();
    return () => {
      stop();
      kill();
    };
  }, [start, stop, kill]);

  return <button onClick={isRunning ? stop : start}>{isRunning ? "Stop" : "Start"}</button>;
}
```

Worker exports:

- `@react-sigma/layout-force`: `useWorkerLayoutForce`, `LayoutForceControl`
- `@react-sigma/layout-forceatlas2`: `useWorkerLayoutForceAtlas2`,
  `LayoutForceAtlas2Control`
- `@react-sigma/layout-noverlap`: `useWorkerLayoutNoverlap`,
  `LayoutNoverlapControl`

## Worker Controls

```tsx
import { ControlsContainer } from "@react-sigma/core";
import { LayoutForceAtlas2Control } from "@react-sigma/layout-forceatlas2";

<ControlsContainer position="bottom-right">
  <LayoutForceAtlas2Control settings={{ settings: { slowDown: 10 } }} />
</ControlsContainer>;
```

Use controls when users should start and stop layouts from the graph UI. Use
hooks when layout lifecycle is driven by app state.

## Factories

`@react-sigma/layout-core` contains generic factory helpers:

- `useLayoutFactory`: wrap a Graphology layout with a React hook returning
  `positions` and `assign`.
- `useWorkerLayoutFactory`: wrap a Graphology worker layout with a React hook
  returning `stop`, `start`, `kill`, and `isRunning`.
- `WorkerLayoutControl`: build control UI for worker hooks.
