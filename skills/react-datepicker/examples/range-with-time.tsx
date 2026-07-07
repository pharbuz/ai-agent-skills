import { useState } from "react";
import DatePicker from "react-datepicker";
import { addDays, setHours, setMinutes } from "date-fns";
import "react-datepicker/dist/react-datepicker.css";

export function RangeWithTimeDatePicker() {
  const [range, setRange] = useState<[Date | null, Date | null]>([
    new Date(),
    addDays(new Date(), 2),
  ]);
  const [startDate, endDate] = range;

  return (
    <DatePicker
      selectsRange
      startDate={startDate}
      endDate={endDate}
      onChange={(nextRange) => {
        setRange(nextRange);
      }}
      minDate={new Date()}
      showTimeSelect
      minTime={setHours(setMinutes(new Date(), 0), 9)}
      maxTime={setHours(setMinutes(new Date(), 0), 18)}
      timeIntervals={30}
      dateFormat="Pp"
      placeholderText="Choose a date range"
    />
  );
}
