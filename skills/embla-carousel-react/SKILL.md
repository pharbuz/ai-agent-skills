---
name: embla-carousel-react
description: >-
  Build, configure, debug, or refactor React carousels with
  `embla-carousel-react`. Trigger WHENEVER the user installs or imports
  `embla-carousel-react`; uses `useEmblaCarousel`, `emblaRef`, `emblaApi`,
  `EmblaOptionsType`, `EmblaCarouselType`, `scrollPrev`, `scrollNext`,
  `scrollTo`, `selectedScrollSnap`, `canScrollPrev`, `canScrollNext`, `on`,
  `off`, `reInit`, `slidesInView`, `scrollProgress`, or plugins such as
  `embla-carousel-autoplay`, `auto-scroll`, `auto-height`, `class-names`,
  `fade`, or `wheel-gestures`; implements carousel slides, dots, prev/next
  buttons, autoplay, responsive slide sizes, loop/drag/free-scroll behavior,
  accessibility, SSR, or fixes broken dragging, missing overflow, layout shift,
  disabled controls, event listener leaks, or pnpm TypeScript import issues.
---

# embla-carousel-react

Use this skill for React carousels powered by Embla. Default to the stable v8 API
unless the target repo already depends on `embla-carousel-react@next` / v9.
As of the checked package metadata, npm `latest` is `8.6.0` and `next` is
`9.0.0-rc02`.

## Default Workflow

1. Inspect `package.json` and lockfile for `embla-carousel-react`,
   `embla-carousel`, and plugin versions.
2. Install `embla-carousel-react` if missing; install `embla-carousel` as a dev
   dependency when importing types in pnpm projects.
3. Use the required DOM structure: viewport with `ref={emblaRef}`, flex
   container, non-shrinking slides.
4. Keep navigation controls outside the viewport to avoid drag conflicts.
5. Read API from `[emblaRef, emblaApi] = useEmblaCarousel(options, plugins)`.
6. Subscribe to events in `useEffect`; remove listeners with `off` unless the
   handler is intentionally one-shot.
7. Memoize options, plugins, and callbacks when they are derived values.
8. Test drag, keyboard/focus behavior, resize behavior, and SSR/client hydration.

## Minimal React Pattern

```tsx
import useEmblaCarousel from "embla-carousel-react";

export function Carousel({ slides }: { slides: React.ReactNode[] }) {
  const [emblaRef, emblaApi] = useEmblaCarousel({ loop: false });

  return (
    <div className="embla">
      <div className="embla__viewport" ref={emblaRef}>
        <div className="embla__container">
          {slides.map((slide, index) => (
            <div className="embla__slide" key={index}>
              {slide}
            </div>
          ))}
        </div>
      </div>
      <button onClick={() => emblaApi?.scrollPrev()}>Previous</button>
      <button onClick={() => emblaApi?.scrollNext()}>Next</button>
    </div>
  );
}
```

```css
.embla__viewport {
  overflow: hidden;
}
.embla__container {
  display: flex;
  touch-action: pan-y pinch-zoom;
}
.embla__slide {
  flex: 0 0 100%;
  min-width: 0;
}
```

## Decision Rules

- Use `loop: true` only when the slide count and layout can support looping.
- Use CSS `flex-basis` for slide size; use `slidesToScroll` for grouping.
- Use `axis: "y"` plus vertical CSS layout for vertical carousels.
- Use `dragFree` for momentum/free-scroll galleries, not paginated hero sliders.
- Use `containScroll: "trimSnaps"` for bounded scroll areas.
- Use `active` or `breakpoints` to disable/reconfigure carousels responsively.
- Use `reInit` sparingly; React wrapper reinitializes when reactive options
  change.

## References

- Read [references/setup-and-layout.md](references/setup-and-layout.md) for
  installation, required markup, CSS, responsive slide sizing, controls, dots,
  and accessibility notes.
- Read [references/api-options-events.md](references/api-options-events.md) for
  options, methods, events, TypeScript types, pnpm notes, and listener patterns.
- Read [references/plugins-ssr-troubleshooting.md](references/plugins-ssr-troubleshooting.md)
  for Autoplay and other plugins, SSR/Next.js guidance, and common bugs.
