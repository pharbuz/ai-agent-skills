> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-time-date](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-time-date)

# DPL Time and Date

## ISO8601

Matches timestamp in the form of `yyyy-MM-ddTHH:mm:ssZ`

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| timestamp |  | none |  | none |

#### Example

Parsing date time string `raw_text` with pattern expression `ISO8601:parsed_timestamp`:

| raw_text |  | parsed_timestamp |
| --- | --- | --- |
| `2019-01-01T13:23:45Z` |  | `2019-01-01 13:23:45.000 +0000` |

## HTTPDATE

Matches timestamp in the form of `dd/MMM/yyyy:HH:mm:ss Z`

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| timestamp |  | none |  | none |

#### Example

Parsing date time string `raw_text` with pattern expression `HTTPDATE:parsed_timestamp`:

| raw_text |  | parsed_timestamp |
| --- | --- | --- |
| `26/Dec/2018:02:59:40 +0100` |  | `2018-12-26 01:59:40.000 +0000` |

## JSONTIMESTAMP

Matches timestamp in the form of `yyyy-MM-ddTHH:mm:ss.SSSZ`

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| timestamp |  | none |  | none |

#### Example

Parsing date time string `raw_text` with pattern expression `JSONTIMESTAMP:parsed_timestamp`:

| raw_text |  | parsed_timestamp |
| --- | --- | --- |
| `2019-01-01T01:01:01.123PST` |  | `2019-01-01 09:01:01.123 +0000` |

## TIMESTAMP, TIME

Allows parsing time and date fields in any format with millisecond precision.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| timestamp |  | none |  |  |

#### Example

Parsing following date-time with day abbreviations in German:

```
Do, 24 Mai 2018 14:30:34 CET
Fr, 25 Mai 2018 09:01:00 CET

```

We can use pattern specifying German locale:

`TIMESTAMP('EEE, d MMM yyyy HH:mm:ss Z', locale='de'):parsed_timestamp EOL`:

| parsed_timestamp |
| --- |

## Unix Timestamp (Epoch)

| epoch |  | pattern |  | result |
| --- | --- | --- | --- | --- |
| `1576590440` |  | `TIMESTAMP('s'):result` |  | `2019-12-17 13:47:20.000 +0000` |
| `1576590440679` |  | `TIMESTAMP('S'):result` |  | `2019-12-17 13:47:20.679 +0000` |
| `1576590440.679` |  | `TIMESTAMP('s.S'):result` |  | `2019-12-17 13:47:20.678 +0000` |
| `1576590440.678599` |  | `TIMESTAMP('s.SSSSSS'):result` |  | `2019-12-17 13:47:20.678 +0000` |

## Conversion Patterns

Parsing date and time mean correctly assigning value to a **timestamp** - information describing a point in time. Log processing keeps timestamps similarly to [Unix time](https://en.wikipedia.org/wiki/Unix_time) (or epoch time) values - defined as the number of seconds that have elapsed since 00:00:00 **Coordinated Universal Time** (UTC), Thursday, 1 January 1970.

Time value is always associated with geographical location, expressed usually as timezone. Hence at parsing the **conversion** from original time zone to UTC must happen (or otherwise the resulting time will have incorrect value when converted to UTC).

When timezone is present in the time field then TIMESTAMP, TIMESTAMP _NANO can use it in conversion. In case it is not present you can specify timezone manually.LetterDate or Time componentPresentationExampleGEra markercase insensitive AD or BCyYearYear2012; 96; 0015YWeek yearYearMMonth in yearMonthJuly; Jul; 07, 7wWeek in yearNumeric27WWeek in monthNumeric2DDay in yearNumeric189dDay in monthNumeric10FDay of week in monthNumeric3EDay name in weekTextTue; TuesdayuUnnecessary numericUnnecessarymetadataaam/pm markercase insensitive am or pmHhour in day of zeroNumeric0based 24-hour clock(0 - 23)khour in day of oneNumeric24based 24-hour clock(1 - 24)Khour in day of zeroNumeric3based 12-hour clock(0 - 11)hhour in day of oneNumeric1based 12-hour clock(1 - 12)mMinute in hourNumeric30sSecond in minuteNumeric51SMillisecondsMilliseconds2019-01-01 00:00:00.957fFractional secondFractional_second2019-01-01 00:00:00.250338976z,ZTime zoneTimezoneGMT+02:00; EET

Time parsing is backed by the Java Calendar class. Depending on user Locale settings the Calendar may be Gregorian or locale-specific. Time
and Date pattern behavior may be specific to the Calendar instance.

Pattern letters are usually repeated, as their number determines the exact presentation:

### Text

If the number of pattern letters is 4 or more, the full name of a field is expected by the parser. Otherwise, the abbreviated name is expected. For instance pattern "EE" expects the abbreviated name of the day in a week, such as "Tue".

### Numeric

Digits 0 - 9, leading zeroes and spaces are allowed. Depending on the number of letters in pattern specification, the behavior of parser is as follows:

- 1 letter pattern is treated as variable length parser accepting any number of digits.

- 2 - 4 letter patterns are treated as fixed-length parsers accepting only the respective number of digits.

- 5 or more letter patterns are treated as variable-length patterns accepting any number of digits.

### Year

Numeric data is allowed only. If the calendar is Gregorian then:

- `y` - matches **variable-length years**, relative to 20'th century. When the year value is less than 32 then the date is adjusted to 21'st century, otherwise to 20'th century.

- `yy` - matches **two-digit years**, relative to 20'th century. When the year value is less than 32 then the date is adjusted to 21'st century, otherwise to 20'th century.

- `yyy` - matches **variable-length years**. The year is interpreted literally regardless of the number of digits. Therefore using the pattern `MM-dd-yyy`, a date "01-11-12" parses to Jan 11'th, 12 AD.

- `yyyy` - matches **four-digit years**. The year is interpreted literally.

If the calendar is not Gregorian and the number of pattern letters is 4 or more, a calendar specific long form is used. Otherwise, calendar specific short form is used.

Patterns with 2 and 4 parsing letters (`yy` and `yyyy` respectively) are treated as **fixed-length** parsers. Hence pattern `yy` will parse successfully only 2 digit long years and fail for any other length.

Patterns with any other length are treated as variable length, which accepts any length of years. For instance pattern `y` parses successfully both "2" and "1256". Hence variable-length time units placed consecutively without non-numeric separators in-between, **are impossible to parse correctly**.

### Month

If the number of pattern letters is 3 or more, the month is interpreted as text, otherwise as numeric:

- 1 letter pattern is treated as variable length parser, which accepts both one and two-digit months

- 2 letter pattern is treated as the fixed-length parser, which accepts only two-digit months

- 3 letter pattern expects abbreviated month names. For instance pattern `MMM-dd-yyyy` parses "Jan-11-2012" to Jan 11'th, 2012.

- 4 or more letter pattern expects full month names. For instance pattern `MMMM-dd-yyyy` parses "January-11-2012" to Jan 11'th, 2012.

### Unnecessary

intended for skipping numeric parts of time and date, which do not contribute to timestamp computation. For example the number of the day in a week. These parts of the timestamp will be parsed as follows, but are ignored in the computation of timestamp value.

### Milliseconds

The number of milliseconds. Accepts numeric values up to 9 digits. The values exceeding 999 are divided by 10, 100, 1000 or 1000000 respectively to the number of digits. The remainder of the division is used as a fractional part representing milliseconds, and the quotient is added to the main timestamp.

The single letter 'S' matches variable-length value up to 9 digits. The pattern with up to 9 letters of 'S' matches values up to the respective number of digits.

#### Example

Parsing time and date using pattern `TIMESTAMP('yyyy-MM-dd HH:mm:ss.S', tz='UTC')`:raw_textparsed_timestamp`2019-01-01 00:00:00.999``2019-01-01 00:00:00.999 +0000``2019-01-01 00:00:00.1000``2019-01-01 00:00:01.000 +0000``2019-01-01 00:00:00.60000``2019-01-01 00:01:00.000 +0000``2019-01-01 00:00:00.3600000``2019-01-01 01:00:00.000 +0000``2019-01-01 00:00:00.86400000``2019-01-02 00:00:00.000 +0000`

### Fractional_second

The fraction of a second. Single 'f' letter matches numeric values up to 9 digits.

When used with matcherdef-timestamp then only up to 3 most significant digits from the value are used.

When used with matcherdef-timestamp_nano then all digits are used (effectively representing the number of nanoseconds).

#### Example

Parsing following date-time string `raw_text` with following patterns:

`TIMESTAMP('yyyy-MM-dd HH:mm:ss.f', tz='UTC'):parsed_timestamp`raw_textparsed_timestampparsed_timestamp_nano`2019-01-01 00:00:00.999``2019-01-01 00:00:00.999 +0000``2019-01-01 00:00:00.999000000 +0000``2019-01-01 00:00:00.1222``2019-01-01 00:00:00.122 +0000``2019-01-01 00:00:00.122200000 +0000``2019-01-01 00:00:00.3335``2019-01-01 00:00:00.333 +0000``2019-01-01 00:00:00.333500000 +0000``2019-01-01 00:00:00.44456789``2019-01-01 00:00:00.444 +0000``2019-01-01 00:00:00.444567890 +0000`

### Timezone

parses time zone expressed as **timezone full name or abbreviation in English** (see [https://www.timeanddate.com/time/zones/](https://www.timeanddate.com/time/zones/))

#### Example

Parsing following date string to UTC timezone:

```
2019-01-05 13:14:25

```

we need to use the pattern:

```
TIMESTAMP('yyyy-MM-dd HH:mm:ss', timezone='UTC'):datetime

```

Results in parsing line 1 into `datetime` field as follows:datetime`2019-01-05 13:14:25 +0000`

## Examples

The result of parsing is displayed here in the UTC timezone.#time_strpatternresult1`2019 1 23 1:35:47``TIMESTAMP('yyyy M d H:m:s', tz='PST'):result``2019-01-23 09:35:47.000 +0000`2`2019-01-23 01:35:47``TIMESTAMP('yyyy-MM-dd HH:mm:ss'):result``2019-01-23 01:35:47.000 +0000`3`2019 1 23 1:35:47 +0200``TIMESTAMP('yyyy M d H:m:s Z'):result``2019-01-22 23:35:47.000 +0000`4`Wed, Jan 1 2019 1:35:47.236 CET``TIMESTAMP('EEE, MMM d yyyy H:m:s.SSS Z'):result``2019-01-01 01:35:47.236 +0000`5`January 16th 2020, 23:56:10.933``TIMESTAMP("MMMM d'th' yyyy, HH:mm:ss.S"):result``2020-01-16 23:56:10.933 +0000`6`1/23/19 1:13:47 PM EST``TIMESTAMP('M/d/yy H:m:s a Z'):result``2019-01-23 17:13:47.000 +0000`7`1/23/19 1:13:47 PM EST``TIMESTAMP('M/d/yyy H:m:s a Z'):result``0019-01-21 17:13:47.000 +0000`8`1576590440``TIMESTAMP('s'):result``2019-12-17 13:47:20.000 +0000`9`1576590440679``TIMESTAMP('S'):result``2019-12-17 13:47:20.679 +0000`10`1576590440.679``TIMESTAMP('s.S'):result``2019-12-17 13:47:20.679 +0000`11`1576590440.678599``TIMESTAMP('s.SSSSSS'):result``2019-12-17 13:47:20.678 +0000`
