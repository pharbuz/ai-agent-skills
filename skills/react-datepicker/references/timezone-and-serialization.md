# Timezone and Serialization

Use this file when the user reports timezone bugs, off-by-one dates, or needs a
timezone-aware picker.

## `timeZone` prop

In the current v9 line, `react-datepicker` supports a `timeZone` prop with IANA
zone identifiers such as:

- `UTC`
- `Europe/Warsaw`
- `America/New_York`

Install the optional peer dependency first:

```bash
npm install date-fns-tz
```

Example:

```tsx
<DatePicker
  selected={date}
  onChange={setDate}
  showTimeSelect
  timeZone="Europe/Warsaw"
  dateFormat="Pp"
/>
```

## The "one day off" bug

Typical failure mode:

- the user selects a date-only value
- app calls `toISOString()`
- midnight in local time becomes the previous UTC date

This is a JavaScript `Date` serialization issue, not a picker rendering bug.

## Safe strategies

### Date-only API field

Send `YYYY-MM-DD`, not full ISO datetime.

```tsx
import { format } from "date-fns";

const handleChange = (date: Date | null) => {
  if (!date) return;
  const payload = format(date, "yyyy-MM-dd");
  submit(payload);
};
```

### True timestamp field

If the backend expects a moment in time, ISO is fine:

```tsx
const handleChange = (date: Date | null) => {
  if (!date) return;
  submit(date.toISOString());
};
```

### Local-date normalization

When the backend wants a logical local date but still expects ISO, normalize it
deliberately before calling `toISOString()`.

```tsx
const normalized = new Date(
  date.getTime() - date.getTimezoneOffset() * 60_000,
);
submit(normalized.toISOString());
```

## Practical rule

- Birthdays, vacations, booking days: use date-only strings
- Meeting timestamps, event times, reminders: use datetimes
- If the display timezone must differ from the browser timezone, add
  `timeZone` plus `date-fns-tz`
