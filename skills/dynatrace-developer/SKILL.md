---
name: dynatrace-developer
description: >-
  Build Dynatrace Platform apps with the Strato design system from
  developer.dynatrace.com. Use this WHENEVER the user works on a Dynatrace app
  (Dynatrace App Engine / AppToolkit), imports from any `@dynatrace/strato-*`
  package, or asks about Strato components (DataTable, Button, TextInput, Select,
  Modal, FlexItem, Flex, DataTableColumn, etc.), design tokens (Colors,
  Typography, Spacings, Borders), charts / data visualizations (TimeseriesChart,
  CategoricalBarChart, DonutChart…), icons, or UI patterns (forms validation,
  filtering, app structure). Trigger even when the user only says "Dynatrace app",
  "Strato", "AppToolkit", "dt-app", or names a component, and when building,
  styling, or debugging the React frontend of a Dynatrace app. Covers component
  props, usage, import paths, and theming.
---

# Dynatrace Developer — Strato design system

Strato is Dynatrace's design system for building apps on the Dynatrace Platform
(App Engine / AppToolkit). It is the successor to Barista and provides **design
tokens**, **React components**, **charts**, and **icons**, documented at
<https://developer.dynatrace.com/design/>.

This skill covers the **design** side a frontend developer needs day to day:
components, tokens, charts, icons, and patterns. For the platform/SDK side
(app functions, AppToolkit CLI, platform services) see
[`references/develop-overview.md`](references/develop-overview.md) and the live
docs at <https://developer.dynatrace.com/develop/>.

## Packages & setup

Strato ships as scoped npm packages:

```bash
npm install @dynatrace/strato-components           # core, production-ready React components
npm install @dynatrace/strato-components-preview    # newer/preview components (forms, tables helpers, filters…)
npm install @dynatrace/strato-design-tokens         # colors, typography, spacing, borders… as JS/CSS tokens
npm install @dynatrace/strato-icons                 # functional icon set
npm install @dynatrace/strato-geo                   # geospatial map components
```

Apps are scaffolded and maintained with the **`dt-app`** CLI. Keep Strato current
(recommended every ~2 weeks) — it updates all `@dynatrace/strato-*` packages at once:

```bash
npx dt-app update
```

> Many components live in **`@dynatrace/strato-components`**, but a number of the
> most-used ones (form controls, the `DataTable` helpers, filters, some content
> components) are in **`@dynatrace/strato-components-preview`**. When an import
> fails, check the other package. The exact import path is shown at the top of
> every component's doc page and in this skill's reference files.

## How component documentation is organized

Every component on developer.dynatrace.com has up to three tabs, and this skill
mirrors them:

- **Overview** — what it is, when to use it, and runnable usage notes.
- **Properties** — the props/TypeScript API (name, type, default, description).
- **Usage** — guidance and do/don't examples.

The fastest path: open the matching reference file below, find the component, and
read its **Import**, **Overview**, and **Props** in one place.

## Component catalogue → reference files

The full Strato component set, grouped the same way the docs are. Open the
reference file for the group you need; each lists every component with its import
path, an overview, and its props.

| Group | Reference file | Components (examples) |
|-------|----------------|-----------------------|
| Buttons | [`references/buttons.md`](references/buttons.md) | Button, IntentButton, NotifyButton, RunQueryButton |
| Content | [`references/content.md`](references/content.md) | Accordion, Avatar, Chip, CodeSnippet, Card, Tooltip, Surface… (24) |
| Forms | [`references/forms.md`](references/forms.md) | TextInput, TextArea, Select, Checkbox, Radio, FormField, Switch… (15) |
| Tables | [`references/tables.md`](references/tables.md) | **DataTable**, SimpleTable, convertToColumns |
| Typography | [`references/typography.md`](references/typography.md) | Heading, Text, Paragraph, Code, ExternalLink… (13) |
| Layouts | [`references/layouts.md`](references/layouts.md) | Flex, Grid, Container, Page, Sidebar… (11) |
| Overlays | [`references/overlays.md`](references/overlays.md) | Modal, Popover, Drawer… (4) |
| Navigation | [`references/navigation.md`](references/navigation.md) | Tabs, Breadcrumbs, Menu… (4) |
| Filters | [`references/filters.md`](references/filters.md) | FilterBar, and related filter components (4) |
| Notifications | [`references/notifications.md`](references/notifications.md) | Toast/notification components (2) |
| Editors | [`references/editors.md`](references/editors.md) | Code/DQL editor components (2) |
| Charts | [`references/charts.md`](references/charts.md) | TimeseriesChart, CategoricalBarChart, DonutChart, PieChart, HoneycombChart, XYChart series… (24) |
| Geo maps | [`references/geo-maps.md`](references/geo-maps.md) | Map and geospatial components (6) |

Design foundations (tokens, theming, layout, a11y, versioning, patterns) →
[`references/foundations.md`](references/foundations.md).

## Quick patterns

### Import and render a component

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import { DataTable } from '@dynatrace/strato-components/tables';
import { TextInput, FormField } from '@dynatrace/strato-components-preview/forms';

<Button variant="emphasized" color="primary" onClick={run}>Run</Button>
```

### DataTable — the most common table (full detail in [`references/tables.md`](references/tables.md))

Memoize `data` and `columns` with `useMemo` so they don't change every render —
this is the #1 DataTable pitfall.

```tsx
import { DataTable } from '@dynatrace/strato-components/tables';

const columns = useMemo(() => [
  { header: 'Name', accessor: 'name', autoWidth: true },
  { header: 'CPU',  accessor: 'cpu', columnType: 'number' },
], []);
const data = useMemo(() => rows, [rows]);

<DataTable data={data} columns={columns} sortable selectableRows="multiple" fullWidth>
  <DataTable.Pagination />
</DataTable>;
```

Column types: `text` (auto-detects links), `datetime`, `bit`, `number`, `long`,
`currency`, `log-content`, `sparkline`, `meterbar`, `markdown`, `gantt`. Enable
resizing with `resizable` in the table config; track widths via
`onColumnSizingChange` / `columnSizing`.

### Consume design tokens (don't hard-code colors/spacing)

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';

const box = { background: Colors.Background.Surface.Default, padding: Spacings.Size16 };
```

Tokens cover Colors, Typography, Spacings, Borders, BoxShadows, Elevations,
Breakpoints, Animations. Details and the named scales →
[`references/foundations.md`](references/foundations.md).

## Working effectively in a Dynatrace app

- **Prefer Strato components and tokens over custom CSS.** The design system
  encodes spacing, color, a11y, and theming (light/dark) — hand-rolled styles
  drift and break theming. Reach for a component first; reach for tokens when you
  must style.
- **Find the right component by group**, not by guessing the name — scan the
  catalogue table above, open the group reference, and confirm the import path
  there (preview vs. core matters).
- **Check Props before inventing props.** The reference files carry the real
  prop names, defaults, and descriptions. Prop **types** may be partial there
  (the doc site renders full TypeScript types client-side), so for an exact type
  open the live page linked in each section — it's the source of truth.
- **Forms**: combine `FormField` (label/validation/help) with the input controls,
  and follow the forms-validation pattern in
  [`references/foundations.md`](references/foundations.md).
- **Charts**: pick the chart by data shape (timeseries → `TimeseriesChart`,
  categories → `CategoricalBarChart`, parts-of-whole → `DonutChart`/`PieChart`);
  see [`references/charts.md`](references/charts.md).

## Reference files

- `references/foundations.md` — Strato overview, design tokens (colors,
  typography, spacing), layout, accessibility, versioning, forms pattern
- `references/buttons.md`, `content.md`, `forms.md`, `tables.md`,
  `typography.md`, `layouts.md`, `overlays.md`, `navigation.md`, `filters.md`,
  `notifications.md`, `editors.md` — component groups (import + overview + props)
- `references/charts.md`, `geo-maps.md` — data visualizations
- `references/develop-overview.md` — index/map of the platform/SDK side, fanning
  out to the full develop references below
- `references/develop-guides.md`, `develop-sdks.md`,
  `develop-platform-services.md`, `develop-reference.md`,
  `develop-extensions.md`, `develop-test-troubleshoot.md` — the complete
  **develop** docs (app functions, data, SDKs, platform services, APIs,
  extensions, testing)
