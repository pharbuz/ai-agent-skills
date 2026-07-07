import { useState } from "react";
import DatePicker, {
  registerLocale,
  type ReactDatePickerCustomHeaderProps,
} from "react-datepicker";
import { getMonth, getYear } from "date-fns";
import { pl } from "date-fns/locale/pl";
import "react-datepicker/dist/react-datepicker.css";

registerLocale("pl", pl);

const MONTHS = [
  "styczen",
  "luty",
  "marzec",
  "kwiecien",
  "maj",
  "czerwiec",
  "lipiec",
  "sierpien",
  "wrzesien",
  "pazdziernik",
  "listopad",
  "grudzien",
];

const YEARS = Array.from({ length: 15 }, (_, index) => 2020 + index);

function CustomHeader({
  date,
  changeMonth,
  changeYear,
  decreaseMonth,
  increaseMonth,
  prevMonthButtonDisabled,
  nextMonthButtonDisabled,
}: ReactDatePickerCustomHeaderProps) {
  return (
    <div style={{ display: "flex", gap: 8, alignItems: "center", padding: 8 }}>
      <button onClick={decreaseMonth} disabled={prevMonthButtonDisabled} type="button">
        {"<"}
      </button>
      <select value={getYear(date)} onChange={(event) => changeYear(Number(event.target.value))}>
        {YEARS.map((year) => (
          <option key={year} value={year}>
            {year}
          </option>
        ))}
      </select>
      <select value={getMonth(date)} onChange={(event) => changeMonth(Number(event.target.value))}>
        {MONTHS.map((month, index) => (
          <option key={month} value={index}>
            {month}
          </option>
        ))}
      </select>
      <button onClick={increaseMonth} disabled={nextMonthButtonDisabled} type="button">
        {">"}
      </button>
    </div>
  );
}

export function CustomHeaderLocaleDatePicker() {
  const [date, setDate] = useState<Date | null>(new Date());

  return (
    <DatePicker
      locale="pl"
      selected={date}
      onChange={(nextDate) => setDate(nextDate)}
      dateFormat="P"
      renderCustomHeader={(props) => <CustomHeader {...props} />}
    />
  );
}
