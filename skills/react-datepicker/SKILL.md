---
name: react-datepicker
description: >-
  Build date and time inputs with `react-datepicker`. Trigger WHENEVER the user
  imports `react-datepicker`; renders `<DatePicker />`; wires `selected`,
  `onChange`, `startDate` / `endDate`, or `selectsRange`; enables time picking
  with `showTimeSelect`; constrains dates with `minDate`, `maxDate`,
  `includeDates`, `excludeDates`, or `filterDate`; localizes with
  `registerLocale`, `setDefaultLocale`, or a `locale` prop; customizes the
  popup with `renderCustomHeader`, `calendarContainer`, `customInput`,
  `withPortal`, or `popperPlacement`; or needs help with timezone handling,
  serialization, and the "one day off" problem. Covers the core props,
  installation, CSS, localization, time zones, common patterns, and examples.
---

# react-datepicker

`react-datepicker` is a reusable React date/time picker from HackerOne. Prefer
it when the user already chose this library or the codebase already uses it.
Current major line: v9.x.

```bash
npm install react-datepicker
```

```tsx
import { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

export function Example() {
  const [value, setValue] = useState<Date | null>(new Date());

  return <DatePicker selected={value} onChange={(date) => setValue(date)} />;
}
```

## Mental model

- It is a controlled input. Pass `selected` and update state in `onChange`.
- It works with native JavaScript `Date` objects, not strings.
- CSS is required: import `react-datepicker/dist/react-datepicker.css` once, or
  provide your own styles.
- Use `date-fns` for formatting, parsing, and locale objects.
- For date ranges, pass `startDate`, `endDate`, and `selectsRange`; `onChange`
  then receives `[start, end]`.
- For time picking, add `showTimeSelect`; use `dateFormat="Pp"` for date+time.
- For timezone-specific display in v9, use `timeZone="Area/City"` and install
  the optional peer dependency `date-fns-tz`.

## Default workflow

1. Install `react-datepicker` and import its CSS.
2. Model form state as `Date | null` or `[Date | null, Date | null]`.
3. Start with the smallest working config: `selected`, `onChange`, `dateFormat`.
4. Add constraints (`minDate`, `maxDate`, `filterDate`, `includeDates`) only
   after the base picker works.
5. If the user needs locale support, register a `date-fns` locale first.
6. If the value is sent to an API, decide explicitly whether the backend wants:
   a date-only string, a local datetime, or a UTC timestamp.

## Common patterns

### Single date

```tsx
const [date, setDate] = useState<Date | null>(null);
<DatePicker selected={date} onChange={setDate} placeholderText="Select a date" />;
```

### Date range

```tsx
const [range, setRange] = useState<[Date | null, Date | null]>([null, null]);
const [startDate, endDate] = range;

<DatePicker
  selectsRange
  startDate={startDate}
  endDate={endDate}
  onChange={(dates) => setRange(dates)}
/>;
```

### Date + time

```tsx
<DatePicker
  selected={date}
  onChange={setDate}
  showTimeSelect
  timeIntervals={15}
  dateFormat="Pp"
/>;
```

## High-value props

- Value and events: `selected`, `onChange`, `onSelect`, `value`
- Range: `selectsRange`, `startDate`, `endDate`, `selectsStart`, `selectsEnd`
- Constraints: `minDate`, `maxDate`, `includeDates`, `excludeDates`,
  `includeDateIntervals`, `excludeDateIntervals`, `filterDate`
- Time: `showTimeSelect`, `showTimeInput`, `minTime`, `maxTime`,
  `includeTimes`, `excludeTimes`, `timeIntervals`, `timeFormat`
- Display: `dateFormat`, `placeholderText`, `monthsShown`, `inline`,
  `showMonthDropdown`, `showYearDropdown`, `isClearable`, `showIcon`
- Popup/layout: `withPortal`, `portalId`, `popperPlacement`,
  `renderCustomHeader`, `calendarContainer`, `customInput`
- i18n/timezone: `locale`, `timeZone`, `weekLabel`, `useWeekdaysShort`

## Common pitfalls

- Missing CSS import: calendar renders unstyled or broken.
- Storing picker output as a string too early: keep `Date` in UI state.
- Using `toISOString()` for a date-only field: this often causes the classic
  "one day off" bug because midnight local time becomes the previous UTC day.
- Forgetting `registerLocale(...)` before `locale="pl"` or another locale key.
- Mixing date-only and datetime semantics in one field or API contract.
- Using `timeZone` without installing `date-fns-tz`: v9 falls back to local
  timezone behavior.

## What to do when asked

- For a plain form field, build the smallest controlled picker first.
- For booking/reservation flows, prefer range selection plus min/max rules.
- For localization, wire `registerLocale` and set `dateFormat` intentionally.
- For API bugs, inspect how the selected `Date` is serialized before changing
  picker props.
- For custom UI, prefer `renderCustomHeader`, `calendarContainer`, and
  `customInput` rather than rewriting the calendar from scratch.

## Reference files

- [references/props-and-patterns.md](references/props-and-patterns.md) —
  grouped props, common UI patterns, and when to use them
- [references/localization-and-imports.md](references/localization-and-imports.md) —
  locales, helper imports, CSS variants, and TypeScript types
- [references/timezone-and-serialization.md](references/timezone-and-serialization.md) —
  `timeZone`, `date-fns-tz`, and safe API serialization strategies

## Examples

- [examples/basic-controlled.tsx](examples/basic-controlled.tsx) — minimal
  single-date controlled picker
- [examples/range-with-time.tsx](examples/range-with-time.tsx) — date range
  with time selection and constraints
- [examples/custom-header-locale.tsx](examples/custom-header-locale.tsx) —
  locale registration and a custom month/year header
