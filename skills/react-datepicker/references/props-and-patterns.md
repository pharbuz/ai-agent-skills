# Props and Patterns

Use this file when the task is about picking the right `react-datepicker`
configuration rather than basic installation.

## Core value flow

- `selected`: the current `Date | null`
- `onChange`: update the value state; this is the main callback
- `onSelect`: fires when the user selects a day, useful for side effects
- `value`: string override for advanced controlled-input scenarios

Keep app state as `Date` until the boundary where you submit or serialize it.

## Selection modes

### Single date

Use `selected` + `onChange`.

### Range

Use:

- `selectsRange`
- `startDate`
- `endDate`

`onChange` receives `[Date | null, Date | null]`.

### Start/end paired inputs

Use two pickers with:

- start picker: `selectsStart`, `startDate`, `endDate`
- end picker: `selectsEnd`, `startDate`, `endDate`, optional `minDate={startDate}`

## Constraints

- `minDate` / `maxDate`: broad date bounds
- `includeDates` / `excludeDates`: explicit allow/deny lists
- `includeDateIntervals` / `excludeDateIntervals`: range-based rules
- `filterDate(date)`: custom logic
- `minTime` / `maxTime`, `includeTimes`, `excludeTimes`, `filterTime`: time rules

Prefer `minDate` / `maxDate` first. Reach for `filterDate` only when the rule
cannot be expressed declaratively.

## Display and layout

- `dateFormat`: input format; use `P` for localized date, `Pp` for date+time
- `monthsShown`: multi-month calendar
- `inline`: renders calendar without popover
- `showMonthDropdown`, `showYearDropdown`, `scrollableYearDropdown`: easier long-range navigation
- `isClearable`: adds clear control
- `placeholderText`: input affordance
- `showIcon`, `icon`, `calendarIconClassName`: icon customization

## Time selection

- `showTimeSelect`: dropdown-like time list
- `showTimeInput`: editable time input
- `timeIntervals`: default is 30; common values are 15 or 60
- `timeFormat`: displayed time format
- Combine with `dateFormat="Pp"` so the input reflects both date and time

## Customization hooks

- `renderCustomHeader`: replace month/year navigation UI
- `calendarContainer`: wrap or decorate the popup container
- `customInput`: render your own input component
- `dayClassName`, `weekDayClassName`, `timeClassName`, `calendarClassName`,
  `className`, `wrapperClassName`, `popperClassName`: CSS hooks
- `withPortal`, `portalId`, `portalHost`: useful in modals or shadow DOM
- `popperPlacement`, `popperModifiers`: popup positioning

For a custom header, the exported `ReactDatePickerCustomHeaderProps` type is the
main TypeScript contract.

## Recommended implementation order

1. Get the controlled picker working.
2. Add formatting and placeholder.
3. Add constraints.
4. Add range or time behavior.
5. Add localization or timezone handling.
6. Only then customize popup/header/input visuals.
