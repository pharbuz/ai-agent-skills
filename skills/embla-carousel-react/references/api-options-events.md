# API, Options, And Events

## Hook Signature

```tsx
const [emblaRef, emblaApi] = useEmblaCarousel(options, plugins);
```

`emblaApi` is undefined until initialization. Guard every method call.

## Common Options

```tsx
useEmblaCarousel({
  align: "center",
  axis: "x",
  containScroll: "trimSnaps",
  direction: "ltr",
  slidesToScroll: 1,
  loop: false,
  dragFree: false,
  skipSnaps: false,
  duration: 25,
  startIndex: 0,
  active: true,
  breakpoints: {
    "(min-width: 768px)": { slidesToScroll: 2 },
  },
});
```

- `align`: snap alignment; use `"start"` for card rails and `"center"` for
  featured slides.
- `axis`: `"x"` or `"y"`; vertical carousels also need vertical CSS.
- `containScroll`: usually `"trimSnaps"` for clipped ends.
- `slidesToScroll`: group by number or `"auto"`.
- `loop`: clones/loops when possible; may disable itself if there are too few
  slides.
- `dragFree`: momentum scrolling without strict snap pagination.
- `active`: enable/disable the carousel, useful with breakpoints.
- `watchDrag`, `watchResize`, `watchSlides`, `watchFocus`: keep default `true`
  unless implementing custom behavior.

Set `useEmblaCarousel.globalOptions` only once, before any carousel initializes.

## Methods

Use methods only after `emblaApi` exists.

- Movement: `scrollPrev()`, `scrollNext()`, `scrollTo(index)`.
- State: `canScrollPrev()`, `canScrollNext()`, `selectedScrollSnap()`,
  `previousScrollSnap()`, `scrollSnapList()`, `slidesInView()`,
  `slidesNotInView()`, `scrollProgress()`.
- Nodes: `rootNode()`, `containerNode()`, `slideNodes()`.
- Lifecycle: `reInit(options?, plugins?)`, `destroy()`.
- Events/plugins: `on(event, cb)`, `off(event, cb)`, `emit(event)`, `plugins()`.

Prefer deriving React state from events instead of reading API state during
render.

## Event Pattern

Event listeners persist across `reInit`, so keep callback identities stable and
unsubscribe when the React effect cleans up.

```tsx
import { useCallback, useEffect, useState } from "react";
import type { EmblaCarouselType } from "embla-carousel";

const [selectedIndex, setSelectedIndex] = useState(0);

const onSelect = useCallback((api: EmblaCarouselType) => {
  setSelectedIndex(api.selectedScrollSnap());
}, []);

useEffect(() => {
  if (!emblaApi) return;
  onSelect(emblaApi);
  emblaApi.on("select", onSelect).on("reInit", onSelect);
  return () => {
    emblaApi.off("select", onSelect).off("reInit", onSelect);
  };
}, [emblaApi, onSelect]);
```

Common events:

- `init`: first initialization only.
- `reInit`: hard reset, including resize-triggered resets.
- `select`: selected snap changed.
- `scroll`: high frequency; throttle/debounce expensive work.
- `settle`: scrolling finished.
- `slidesInView`: visible slides changed.
- `resize`: Embla observed resize.
- `slidesChanged`: slide list changed.
- `slideFocus`: slide received focus.
- `pointerDown`, `pointerUp`: user pointer interaction.
- `destroy`: final lifecycle event.

## TypeScript

Import React wrapper from `embla-carousel-react`; import shared types from
`embla-carousel`.

```tsx
import useEmblaCarousel from "embla-carousel-react";
import type {
  EmblaCarouselType,
  EmblaEventType,
  EmblaOptionsType,
} from "embla-carousel";
```

With pnpm, add `embla-carousel` explicitly as a dev dependency before importing
these types.

## React State Rules

- Memoize computed `options` and `plugins` arrays with `useMemo`.
- Memoize event handlers with `useCallback`.
- Do not call `emblaApi` methods during render.
- If slides are dynamic, rely on `watchSlides` or call `reInit` after DOM
  changes when automatic watching is disabled.
