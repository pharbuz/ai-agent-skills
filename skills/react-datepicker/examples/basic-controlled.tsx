import { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

export function BasicControlledDatePicker() {
  const [date, setDate] = useState<Date | null>(new Date());

  return (
    <DatePicker
      selected={date}
      onChange={(nextDate) => setDate(nextDate)}
      dateFormat="yyyy-MM-dd"
      placeholderText="Select a date"
      isClearable
    />
  );
}
