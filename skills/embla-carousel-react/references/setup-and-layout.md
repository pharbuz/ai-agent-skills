# Setup And Layout

## Install

```bash
npm install embla-carousel-react --save
pnpm add embla-carousel-react
yarn add embla-carousel-react
```

For pnpm + TypeScript imports from `embla-carousel`, also install:

```bash
pnpm add -D embla-carousel
```

## Required Structure

The viewport receives `ref={emblaRef}` and hides overflow. The container is the
scrollable flex row. Slides must not shrink.

```tsx
import useEmblaCarousel from "embla-carousel-react";

export function EmblaCarousel() {
  const [emblaRef] = useEmblaCarousel();

  return (
    <div className="embla">
      <div className="embla__viewport" ref={emblaRef}>
        <div className="embla__container">
          <div className="embla__slide">Slide 1</div>
          <div className="embla__slide">Slide 2</div>
          <div className="embla__slide">Slide 3</div>
        </div>
      </div>
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

## Slide Sizes

Use CSS, not JavaScript, for most slide sizing:

```css
.embla__slide {
  flex: 0 0 80%;
  min-width: 0;
}

@media (min-width: 768px) {
  .embla__slide {
    flex-basis: 33.3333%;
  }
}
```

For gaps, put spacing on slides or use a container gap and compensate if the
design requires exact outer alignment. Keep `min-width: 0`; missing it is a
common cause of overflow and broken measurements.

## Controls

Keep prev/next and dot buttons outside `.embla__viewport` to avoid pointer and
drag conflicts.

```tsx
const scrollPrev = () => emblaApi?.scrollPrev();
const scrollNext = () => emblaApi?.scrollNext();
```

Track disabled state with `select` and `reInit` events:

```tsx
const [prevDisabled, setPrevDisabled] = useState(true);
const [nextDisabled, setNextDisabled] = useState(true);

const updateButtons = useCallback((api: EmblaCarouselType) => {
  setPrevDisabled(!api.canScrollPrev());
  setNextDisabled(!api.canScrollNext());
}, []);

useEffect(() => {
  if (!emblaApi) return;
  updateButtons(emblaApi);
  emblaApi.on("select", updateButtons).on("reInit", updateButtons);
  return () => {
    emblaApi.off("select", updateButtons).off("reInit", updateButtons);
  };
}, [emblaApi, updateButtons]);
```

## Dots

Build dots from `scrollSnapList()` and update current index from
`selectedScrollSnap()`.

```tsx
const [selectedIndex, setSelectedIndex] = useState(0);
const [scrollSnaps, setScrollSnaps] = useState<number[]>([]);

const onSelect = useCallback((api: EmblaCarouselType) => {
  setSelectedIndex(api.selectedScrollSnap());
}, []);

useEffect(() => {
  if (!emblaApi) return;
  setScrollSnaps(emblaApi.scrollSnapList());
  onSelect(emblaApi);
  emblaApi.on("select", onSelect).on("reInit", onSelect);
  return () => {
    emblaApi.off("select", onSelect).off("reInit", onSelect);
  };
}, [emblaApi, onSelect]);
```

## Accessibility

- Use native `<button>` elements for controls.
- Add meaningful `aria-label` text for icon-only controls.
- Use `aria-current` or `aria-selected` for the active dot.
- Pause or stop autoplay on interaction when motion could distract.
- Do not trap focus inside slides; let users tab through visible controls.
