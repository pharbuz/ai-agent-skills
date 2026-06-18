> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-comparison](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-comparison)

# DQL compared to SQL and more

This page compares the most common use cases between DQL and other well-established data query and processing languages like SQL, Splunk's SPL, and Microsoft's Kusto Query Language.

### Loading data for querying

#### Dynatrace Query Language (DQL)

```
fetch events

```

#### Structured Query Language (SQL)

```
SELECT * FROM events

```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*

```

#### Kusto Query Language (KQL)

```
events

```

### Filtering

Narrows the number of records based on a filter expression. In this example, we are searching for payment events.

#### Dynatrace Query Language (DQL)

```
fetch events
| filter event.type == "travel.funnel.booking-payment"

```

#### Structured Query Language (SQL)

```
SELECT * FROM events WHERE 'event.type'="travel.funnel.booking-payment"

```

#### Splunk Search Processing language (SPL)

```
sourcetype = event* | where event.type = "travel.funnel.booking-payment"

```

#### Kusto Query Language (KQL)

```
events
| where ['event.type'] == "travel.funnel.booking-payment"

```

We can add as many filters as needed to the pipeline. For example, we can look for bookings made by higher level loyalty customers traveling with children.

#### Dynatrace Query Language (DQL)

```
fetch events
| filter event.type == "travel.funnel.booking-payment" and loyaltyStatus == "Platinum" and childrenTravelers > 0

```

#### Structured Query Language (SQL)

```
SELECT * FROM events WHERE 'event.type'="travel.funnel.booking-payment" AND loyaltyStatus = "Platinum" AND childrenTravelers > 0

```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*
| where event.type = "travel.funnel.booking-payment" AND loyaltyStatus = "Platinum" AND childrenTravelers > 0

```

#### Kusto Query Language (KQL)

```
events
| where ['event.type'] == "travel.funnel.booking-payment" and loyaltyStatus == "Platinum" and childrenTravelers > 0

```

### Field selection

Selecting just the relevant fields can be done in any pipeline stage. In this example, we will select only the product of successful bookings.

#### Dynatrace Query Language (DQL)

```
fetch events
| filter event.type == "travel.funnel.booking-payment"
| fields product

```

#### Structured Query Language (SQL)

```
SELECT product FROM events WHERE 'event.type'="travel.funnel.booking-payment"

```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*
| where event.type = "travel.funnel.booking-payment"
| fields product

```

#### Kusto Query Language (KQL)

```
event
| where ['event.type'] == "travel.funnel.booking-payment"
| project product

```

### Calculations and sorting

We can transform the selected records in the pipelines. For example, we select the booked trips' duration in days and we will turn it into weeks.

#### Dynatrace Query Language (DQL)

```
fetch event
| filter event.type == "travel.funnel.booking-payment"
| fieldsAdd journeyWeeks = journeyDuration/7
| sort journeyWeeks desc

```

#### Structured Query Language (SQL)

```
SELECT journeyDuration/7 AS journeyWeeks FROM events WHERE 'event.type'="travel.funnel.booking-payment" ORDER BY journeyWeeks DESC

```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*
| where event.type = "travel.funnel.booking-payment"
| eval journeyweeks = journeyDuration/7
| sort -journeyweeks

```

#### Kusto Query Language (KQL)

```
event
| where ['event.type'] == "travel.funnel.booking-payment"
| project journeyWeeks = journeyDuration/7
| sort journeyweeks desc

```

### Grouping

If we are interested only in unique values in our key, we can deduplicate the results by grouping them.

#### Dynatrace Query Language (DQL)

```
fetch events
| summarize count(), by:event.type
| fields event.type

```

#### Structured Query Language (SQL)

```
SELECT DISTINCT 'event.type' FROM events

```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*
| stats count by event.type

```

#### Kusto Query Language (KQL)

```
events
| summarize by event.type

```

### Aggregation

After grouping selected records based on a field, we can aggregate the results to a new output.

#### Dynatrace Query Language (DQL)

```
fetch events
| filter event.type == "travel.funnel.booking-payment"
| summarize sum = sum(amount), by:travelAgency

```

#### Structured Query Language (SQL)

```
SELECT sum(amount) AS sum FROM events GROUP BY sum, travelAgency WHERE 'event.type' == "travel.funnel.booking-payment"

```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*
| where event.type = "travel.funnel.booking-payment"
| stats sum(amount) as total_amount by travelAgency

```

#### Kusto Query Language (KQL)

```
event
| filter event.type == "travel.funnel.booking-payment"
| summarize sum = sum(amount) by travelAgency

```

Let's take a look at a bit more complex use case, where we want to add a new field, based on a mathematical expression, to our result table.

#### Dynatrace Query Language (DQL)

```
fetch events
| filter event.type == "travel.funnel.booking-payment"
| summarize sum = sum(amount), by:{travelAgency, travelers}
| fieldsAdd has_more_than_2 = travelers > 2

```

#### Structured Query Language (SQL)

```
SELECT sum(amount) AS sum, travelers > 2  AS has_more_than_2 FROM events  GROUP BY sum, has_more_than_2, travelAgency, travelers WHERE 'event.type' == "travel.funnel.booking-payment"

```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*
| where event.type = "travel.funnel.booking-payment"
| stats sum(amount) as total_amount by travelAgency, travelers
| eval has_more_than_2 = travelers > 2

```

#### Kusto Query Language (KQL)

```
events
| where ['event.type'] == "travel.funnel.booking-payment"
| summarize sumBytes = sum(amount) by travelAgency, travelers
| project has_more_than_2 = travelers > 2

```
