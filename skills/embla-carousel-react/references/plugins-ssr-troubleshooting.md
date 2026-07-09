# Plugins, SSR, And Troubleshooting

## Plugin Pattern

Install each official plugin separately. Package names start with
`embla-carousel-`.

```bash
npm install embla-carousel-autoplay --save
```

Pass plugins as the second hook argument.

```tsx
import Autoplay from "embla-carousel-autoplay";
import useEmblaCarousel from "embla-carousel-react";

const plugins = useMemo(() => [Autoplay({ delay: 4000 })], []);
const [emblaRef, emblaApi] = useEmblaCarousel({ loop: true }, plugins);
```

Access plugin APIs from `emblaApi.plugins()`.

```tsx
useEffect(() => {
  if (!emblaApi) return;
  emblaApi.plugins().autoplay?.play();
}, [emblaApi]);
```

## Common Official Plugins

- `embla-carousel-autoplay`: automatic slide transitions.
- `embla-carousel-auto-scroll`: continuous scrolling.
- `embla-carousel-auto-height`: adapt height to selected slide.
- `embla-carousel-class-names`: add state classes to slides/snaps.
- `embla-carousel-fade`: fade transition instead of sliding.
- `embla-carousel-wheel-gestures`: wheel/trackpad gesture support.

## Autoplay

Autoplay v9 docs require `play()` to start; for v8 projects, inspect the
installed plugin behavior and local examples before changing existing behavior.

Useful options:

```tsx
Autoplay({
  delay: 4000,
  stopOnLastSnap: false,
  stopOnInteraction: true,
  stopOnMouseEnter: true,
  stopOnFocusIn: true,
});
```

Useful methods:

```tsx
emblaApi.plugins().autoplay?.play();
emblaApi.plugins().autoplay?.stop();
emblaApi.plugins().autoplay?.reset();
emblaApi.plugins().autoplay?.isPlaying();
```

For progress bars, use the plugin events available in the installed version
instead of a raw interval when possible.

## SSR And Next.js

`embla-carousel-react` uses browser APIs through the initialized ref. In Next.js
App Router, put Embla components behind `"use client"`.

```tsx
"use client";

import useEmblaCarousel from "embla-carousel-react";
```

Avoid server-rendered output that depends on `emblaApi`; initialize selected
state after the API exists. If a plugin touches `window` during import in the
current version, import it dynamically inside a client component or isolate the
carousel with `next/dynamic({ ssr: false })`.

## Troubleshooting

- Nothing moves: ensure `ref={emblaRef}` is on the viewport, not the container.
- Slides stack vertically: set `.embla__container { display: flex; }`.
- Slides overflow or sizes are wrong: set `.embla__slide { min-width: 0; }`.
- Drag conflicts with buttons: move controls outside `.embla__viewport`.
- Prev/next disabled state is stale: update on both `select` and `reInit`.
- Event handler runs multiple times: stabilize callback identity and call `off`
  in effect cleanup.
- Loop does not loop: Embla may disable loop if content is insufficient.
- Carousel shifts after images load: give media stable dimensions or call
  `reInit` after layout-changing content loads.
- Type imports fail under pnpm: add `embla-carousel` as a direct dev dependency.
- Scroll event causes jank: throttle work and avoid React state writes on every
  `scroll` event unless necessary.
- Options changes reset position unexpectedly: memoize options and avoid
  creating a fresh object every render.

## Version Notes

- Stable npm `latest` is v8.6.0; npm `next` is v9.0.0-rc02 at the time this
  skill was created.
- Current docs pages may default to v9. Prefer `/docs/v8/...` for stable v8
  projects and `/docs/...` for v9/next projects.
- Some names differ between versions. If a method from docs fails, inspect the
  installed package types before patching blindly.
