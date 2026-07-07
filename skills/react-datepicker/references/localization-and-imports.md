# Localization and Imports

Use this file when the task mentions locales, TypeScript types, or copying
examples from the documentation site.

## Required imports

```tsx
import { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
```

CSS module variants also exist:

```tsx
import "react-datepicker/dist/react-datepicker-cssmodules.css";
// or
import "react-datepicker/dist/react-datepicker.module.css";
```

## Locale setup

`react-datepicker` relies on `date-fns` locale objects.

```tsx
import DatePicker, { registerLocale, setDefaultLocale } from "react-datepicker";
import { pl } from "date-fns/locale/pl";

registerLocale("pl", pl);
setDefaultLocale("pl"); // optional global default
```

Then either:

```tsx
<DatePicker locale="pl" selected={date} onChange={setDate} />
```

or rely on `setDefaultLocale(...)`.

## Common date-fns helpers

Examples often need:

```tsx
import {
  addDays,
  addMonths,
  getMonth,
  getYear,
  setHours,
  setMinutes,
  subDays,
} from "date-fns";
```

These are common in examples for range defaults, custom headers, and time setup.

## TypeScript types

Useful exported types include:

```tsx
import type {
  ReactDatePickerCustomHeaderProps,
  ReactDatePickerProps,
  CalendarContainerProps,
} from "react-datepicker";
```

Use `ReactDatePickerCustomHeaderProps` with `renderCustomHeader`.

## Extra utilities used by examples

Many custom-header examples use a `range()` helper for year lists.
You can either:

- install `lodash/range`, or
- write a tiny local helper with `Array.from(...)`

Prefer the local helper unless the project already depends on Lodash.
