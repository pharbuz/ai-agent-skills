# Strato foundations: tokens, layout, a11y, patterns, versioning

Distilled from <https://developer.dynatrace.com/design/> (Foundations, Design
tokens, Patterns, Strato versioning). Use this when styling, theming, laying out,
or applying UX patterns in a Dynatrace app.

## About Strato

Strato is Dynatrace's design system for building Platform apps, and the successor
to **Barista**. It provides design tokens, React components, charts, and icons
tuned for observability, analytics, and data-visualization UIs.

Packages:

```bash
@dynatrace/strato-components          # core React components
@dynatrace/strato-components-preview  # preview/newer components (forms, table helpers, filters)
@dynatrace/strato-design-tokens       # colors, typography, spacing, borders, shadows, …
@dynatrace/strato-icons               # functional icons
@dynatrace/strato-geo                 # geospatial maps
```

Keep them current with `npx dt-app update` (recommended ~every 2 weeks).

---

## Design tokens

Tokens are the single source of truth for visual style. **Always prefer tokens
over hard-coded values** — they encode light/dark theming and consistency. Import
each group as a default export:

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import Typography from '@dynatrace/strato-design-tokens/typography';
import Spacings from '@dynatrace/strato-design-tokens/spacings';
import Borders from '@dynatrace/strato-design-tokens/borders';
```

### Colors

Colors are **semantic** (named by role, not by hue) so they adapt to theme
automatically. Main groups and their intent sub-scales
(`Neutral`, `Primary`, `Success`, `Warning`, `Critical`):

| Group | Use for | Examples |
|-------|---------|----------|
| `Colors.Theme.*` | Raw theme palette (Foreground, Background, Neutral, Primary, Success, Warning, Critical) | `Colors.Theme.Primary.50` |
| `Colors.Background.*` | Surfaces & fills: `Base`, `Surface`, `Container.<intent>`, `Field.<intent>`, `Shell` | `Colors.Background.Surface.Default` |
| `Colors.Text.*` | Text by intent (+ `.OnAccent` on colored fills) | `Colors.Text.Neutral.Default` |
| `Colors.Border.*` | Borders by intent (+ `.OnAccent`) | `Colors.Border.Neutral.Default` |
| `Colors.Icon.*` | Icon colors by intent | `Colors.Icon.Primary.Default` |
| `Colors.Charts.*` | Data-viz palettes: `Categorical`, `Sequential`, `Diverging`, `Status`, `Threshold`, `Apdex`, `Loglevel`, `Rainbow`, … | `Colors.Charts.Categorical.Color01.Default` |

Full token tables: <https://developer.dynatrace.com/design/design-tokens/Colors/>.

### Typography

Import `Typography` and apply a named style. Font family is
`DynatraceFlow, Roboto, Helvetica, sans-serif`. Scales (each with levels):

- `Typography.Display.Level1..3` — large display (64 / 56 / 48 px)
- `Typography.Heading.Level1..6` — headings (32 / 28 / 24 / 20 / 16 / 14 px)
- `Typography.Subtitle.Display|Heading.Level1..3` — subtitles
- `Typography.Text.*` — body text (the default reading text)

Prefer the **`Heading`, `Text`, `Paragraph`** typography components
(see [`typography.md`](typography.md)) over applying tokens by hand.

### Spacings

Non-linear scale; the token name embeds its px value (`Size16` = 16px). Use for
gaps, padding, margins:

```
Size0(0)  Size2(2)  Size4(4)  Size6(6)  Size8(8)  Size12  Size16  Size20
Size24  Size28  Size32  Size36  Size40  Size48  Size56  Size64
```

```tsx
const style = { padding: Spacings.Size16, gap: Spacings.Size8 };
```

### Other token groups

`Borders` (style/width/radius), `BoxShadows`, `Elevations` (z-index/stacking),
`Breakpoints` (responsive), `Animations` (motion). All under
`@dynatrace/strato-design-tokens/*` and documented at
<https://developer.dynatrace.com/design/design-tokens/>.

---

## Layout

Build responsive layouts with the layout components (see [`layouts.md`](layouts.md))
rather than raw CSS:

- **`Grid`** — 2D layouts; works with the `Breakpoints` tokens.
- **`Flex` / `FlexItem`** — 1D flexible layouts; the workhorse for most UIs.
- Respect a sensible **minimum width**; use breakpoints for adaptation.

Centered vs full-width: use **centered** layouts for reading/forms, **full-width**
for dense data (tables, dashboards). Establish visual hierarchy with
`Base` → `Surface` → `Container` background layers.

---

## Accessibility (build it in, don't bolt it on)

Strato components are accessible by default; keep them that way:

- Give every control an **accessible name** (visible label or `aria-label`).
- Associate **form field labels** with inputs (`FormField` does this for you).
- Ensure **keyboard** operability and visible focus; don't trap focus.
- Announce **state changes** (loading, errors) to assistive tech.
- Never rely on **color alone** for status — pair with text/icon.
- Provide **alt text** for meaningful images; adequate **target sizes**.

Reference: <https://developer.dynatrace.com/design/foundations/accessibility/>.

---

## Pattern: forms & validation

From <https://developer.dynatrace.com/design/patterns/forms-validation/>.

- **Anatomy**: clear `Labels`, optional `Placeholders` (never as the label),
  `Hints` for help, and explicit marking of `Required` fields.
- **Building a form**: consistent `Spacing` (use spacing tokens), sensible
  `Columns`, and field `Sizing` matched to expected input length.
- **Buttons in forms**: consistent alignment and spacing; primary action
  emphasized, secondary actions de-emphasized.
- Compose `FormField` (label + validation + hint) with the form controls in
  [`forms.md`](forms.md). Validate on submit/blur and surface errors near the
  field with an accessible announcement.

---

## Versioning & lifecycle

Strato follows **semantic versioning** with a regular release cadence. Component
lifecycle states:

- **New** — recently added; API may still change.
- **Stable** — production-ready; backward-compatible within the major.
- **Deprecated** — slated for removal; migrate away.

Update with `npx dt-app update` (all Strato packages) or npm per package. Watch
**Upcoming changes** for advance notice of breaking changes, and the
**Release notes**. Reference:
<https://developer.dynatrace.com/design/strato-versioning/>.
