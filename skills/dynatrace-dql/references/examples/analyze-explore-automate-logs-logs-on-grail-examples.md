> Source: [https://docs.dynatrace.com/docs/analyze-explore-automate/logs/logs-on-grail-examples](https://docs.dynatrace.com/docs/analyze-explore-automate/logs/logs-on-grail-examples)

# Log on Grail examples

Log Management and Analytics powered by Grail enables you to pinpoint and retrieve any log data with the help of [Dynatrace Query Language](/platform/grail/dynatrace-query-language). After reviewing the [fundamentals of DQL queries](/platform/grail/dynatrace-query-language/dql-guide), use the examples on this page to start getting answers from your log data.

To run DQL queries with logs on Grail, go to  **Logs & Events Classic** > **Advanced mode**.

- [Example 1](/analyze-explore-automate/logs/logs-on-grail-examples#logexample1) - Get the distribution of HTTP status codes and counts per error type.

- [Example 2](/analyze-explore-automate/logs/logs-on-grail-examples#logexample2) - Define an average cart size based on logs.

- [Example 3](/analyze-explore-automate/logs/logs-on-grail-examples#logexample3) - Track user changes with audit logs.

- [Example 4](/analyze-explore-automate/logs/logs-on-grail-examples#logexample4) - Create a log metric.

- [Example 5](/analyze-explore-automate/logs/logs-on-grail-examples#logexample5) - Create a log alert.



### Example 1: Status codes and counts

In this example, you get the distribution of HTTP status codes and counts per error type.

The proxy server logs HTTP response status codes. You need to see the response code distribution over a certain timeframe, and focus on errors.

1.

2.
-

Search for relevant logs.

You need to start with a search for logs from the HAProxy instance. As the `haproxy` string is included in the log message, let's use the `contains()` function.

```
fetch logs
| filter contains(content, "haproxy")

```

A search for the `haproxy` string is performed across all records in the timeframe, so you should narrow it to optimize the query. If the entity that produces logs can be identified in advance, it's much more cost-effective to search within that specific entity.

```
fetch logs
| filter dt.entity.process_group=="PROCESS_GROUP-123F4A56BCDA0EA9"

```

**Results table**

timestamp

content

log.source

dt.entity.host

…

2022-08-10 14:05:42

2022-08-10T11:05:42Z localhost haproxy[12529]: 123.45.67.891:23456 http-in~ individual_servers/abcde1 123/0/0/1/456 HTTP_STATUS 200 284 - - –NN 5749/5745/0/1/0…

/var/abcde/abc/defrghytji/HOST-1…

HOST-AB-12-34567

…

2022-08-10 14:05:46

2022-08-10T11:05:46Z localhost haproxy[12528]: 12.345.67.123:12345 http-in~ local/local1 5432/0/0/103/1234 HTTP_STATUS 200 138 - - – 7416/7413/407/408/0 0/…

/var/abcde/abc/defrghytji/HOST-A2…

HOST-CD-76-54321

…

2022-08-10 14:05:50

2022-08-10T11:05:50Z localhost haproxy[12529]: 11.222.33.123:45678 http-in~ local/local1 19/0/1/110/123 HTTP_STATUS 204 64 - - – 5753/5749/358/359/0 0/0…

/var/abcde/abc/defrghytji/HOST-A23…

HOST-AR-78-12345

…

3.

4.
-

Extract your metric from the content field.

The log content field includes the HTTP_STATUS codes you need. Now let's use the `parse` command to create a [Dynatrace Pattern Language](/platform/grail/dynatrace-pattern-language) pattern with the following elements:

- `LD`: start by matching any [line data](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings#line-data) at the beginning of the field

- `'HTTP_STATUS '`: [literal expression](/platform/grail/dynatrace-pattern-language/log-processing-literal-expression) that immediately precedes the numerical Http Status, and takes into account a space

- `INT:httpstatus`: [integer](/platform/grail/dynatrace-pattern-language/log-processing-numeric#int-integer) that will be parsed out as a new field `httpstatus`

```
fetch logs
| filter dt.entity.process_group=="PROCESS_GROUP-123F4A56BCDA0EA9"
| parse content, "LD 'HTTP_STATUS ' INT:httpstatus"

```

**Results table**

timestamp

content

httpstatus

2022-08-10 14:05:42

2022-08-10T11:05:42Z localhost haproxy[12529]: 123.45.67.891:23456 http-in~ individual_servers/abcde1 123/0/0/1/456 HTTP_STATUS 200 284 - - –NN 5749/5745/0/1/ 0…

200

2022-08-10 14:05:46

2022-08-10T11:05:46Z localhost haproxy[12528]: 12.345.67.123:12345 http-in~ local/local1 5432/0/0/103/1234 HTTP_STATUS 200 138 - - – 7416/7413/407/408/0 0/…

200

2022-08-10 14:05:50

2022-08-10T11:05:50Z localhost haproxy[12529]: 11.222.33.123:45678 http-in~ local/local1 19/0/1/110/123 HTTP_STATUS 204 64 - - – 5753/5749/358/359/0 0/0…

204

5.

6.
-

Filter a range of values.

You can select a range of values for further analysis using DQL. We select only the HTTP status codes that begin with 400 and higher, as those include client side and server side errors.

```
fetch logs
| filter dt.entity.process_group=="PROCESS_GROUP-802F3A32CECA0EA9"
| parse content, "LD 'HTTP_STATUS ' INT:httpstatus"
| filter httpstatus >= 400

```

7.

8.
-

Aggregate the results.

You need to aggregate the results with count() to get a summary of how many times each status code occurs.

```
fetch logs
| filter dt.entity.process_group=="PROCESS_GROUP-802F3A32CECA0EA9"
| parse content, "LD 'HTTP_STATUS ' INT:httpstatus"
| filter httpstatus >= 400
| summarize count(), by:{httpstatus}

```

**Results table**

count()

httpstatus

4

403

779

404

1

500

9

503

9.

### Example 2: Average cart size

In this example, you will define an average cart size based on logs.

Your application logs context data that is relevant to your business. You need to retrieve that data from logs and create a report for a specific timeframe.

1.

2.
-

Select the specific process data for a defined timeframe.

You need to query logs from the last three hours, which is your timeframe, and then specify the process that handles cart actions in your store, `cartservice cartservice-*`.

```
fetch logs, from:now()-3h
| filter dt.process.name=="cartservice cartservice-*"

```

**Results table**

timestamp

content

log.source

dt.process.name

…

2022-08-05 11:29:57

{"@t":"2022-08-05T08:29:57.6864969Z","@m":"Slow GetCartAsync request detected for userId=a433448b-c38d-4144-9591-f510829d4gh2","@i":"abc0f94a"}

/var/log/pods/prod_cartservice-74c8d7d674-7dqf

cartservice cartservice-*

…

2022-08-05 11:29:57

{"@t":"2022-08-05T08:29:57.8068740Z","@m":"No carts for user ab51dc18-7724-44fb-cdf8-8bda633f0022","@i":"c9315217"}

/var/log/pods/prod_cartservice-74c8d7d674-7dqf

cartservice cartservice-*

…

2022-08-05 11:29:58

{"@t":"2022-08-05T08:29:57.6864541Z","@m":"GetCartAsync called with userId=z433448a-c38d-4123-9591-f510829d4ab2","@i":"1feab40c"}

/var/log/pods/prod_cartservice-74c8d7d674-7dqf

cartservice cartservice-*

…

2022-08-05 11:30:01

{"@t":"2022-08-05T08:30:01.1058085Z","@m":"Checking CartService Health","@i":"a01f1123"}

/var/log/pods/prod_cartservice-74c8d7d674-7dqf

cartservice cartservice-*

…

3.

4.
-

Check the types and counts of products added to carts.

You need to get an overview of the type and quantity of products users added to their carts. Since logs contain various events, you need to specify the events where items were added to carts, using the `contains()` function. To clean up the results table, it is a good idea to leave only timestamp and log content.

```
fetch logs, from:now()-3h
| filter dt.process.name=="cartservice cartservice-*"
| filter contains(content, "AddItemAsync")
| fields timestamp, content

```

**Results table**

timestamp

content

2022-08-05 11:55:04

{"@t":"2022-08-05T08:55:04.9934166Z","@m":"AddItemAsync called with userId=a332eabc-f52f-40d5-a09f-51bb96f5d119, productId=1ZYFJ3GM2N, quantity=1","@i":"18b35248"}

2022-08-05 11:55:07

{"@t":"2022-08-05T08:55:07.1405993Z","@m":"AddItemAsync called with userId=5ddcdd66-f0fd-4608-839e-0cd7841a3bbc, productId=L2ECAV7KIM, quantity=5","@i":"04fe325f"}

2022-08-05 11:55:32

{"@t":"2022-08-05T08:55:32.5027148Z","@m":"AddItemAsync called with userId=66734557-683c-4864-b3c7-8f08b52f0b17, productId=LS3PSXUNUM, quantity=5","@i":"987426bd"}

2022-08-05 11:30:01

{"@t":"2022-08-05T08:55:58.6888309Z","@m":"AddItemAsync called with userId=c673ca76-3966-4174-b950-4c3f3aa22dfe, productId=4SIQT8TOJO, quantity=2","@i":"99a07cd5"}

5.

6.
-

Extract the products and corresponding quantities.

You need to extract the product identifiers and quantities from logs with the `parse` command.

Using the [Dynatrace Pattern Language](/platform/grail/dynatrace-pattern-language), create a pattern and match the following parts of the `content` field:

- `LD`: start by matching any [line data](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings#line-data) at the start of the field

- `'userId='`: [literal expression](/platform/grail/dynatrace-pattern-language/log-processing-literal-expression) that immediately precedes user ID

- `LD:userId`: any line data that will be parsed out as a new field with the `userId` name

- `', productId='`: literal expression that ends user ID and separates it from product ID

- `LD:productId`: any line data that will be parsed out as a new field with the `productId` name

- `', quantity='`: literal expression that ends product ID and separates it from quantity

- `INT:productQuantity`: [integer](/platform/grail/dynatrace-pattern-language/log-processing-numeric#int-integer) that will be parsed out as a new field with the `productQuantity` name

The remaining fields are ignored.

```
fetch logs, from:now()-3h
| filter dt.process.name=="cartservice cartservice-*"
| filter contains(content, "AddItemAsync")
| fields timestamp, content
| parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"

```

**Results table**

timestamp

content

userId

productId

productQuantity

2022-08-05 11:55:04

{"@t":"2022-08-05T08:55:04.9934166Z","@m":"AddItemAsync called with userId=a332efea-f52f-40d5-a09f-51bb96f5d119, productId=1ZYFJ3GM2N, quantity=1","@i":"18b35248"}

a332efea-f52f-40d5-a09f-51bb96f5d119

1ZYFJ3GM2N

1

2022-08-05 11:55:07

{"@t":"2022-08-05T08:55:07.1405993Z","@m":"AddItemAsync called with userId=5bdcdd66-f0fd-4608-839e-0cd7841a3bbc, productId=L2ECAV7KIM, quantity=5","@i":"04fe325f"}

5bdcdd66-f0fd-4608-839e-0cd7841a3bbc

L2ECAV7KIM

5

2022-08-05 11:55:32

{"@t":"2022-08-05T08:55:32.5027148Z","@m":"AddItemAsync called with userId=66734557-683c-4864-c3c7-8f08b52f0b17, productId=LS3PSXUNUM, quantity=5","@i":"987426bd"}

66734557-683c-4864-c3c7-8f08b52f0b17

LS3PSXUNUM

5

2022-08-05 11:30:01

{"@t":"2022-08-05T08:55:58.6888309Z","@m":"AddItemAsync called with userId=d673ca76-3966-4174-b950-4c3f3aa22dfe, productId=4SIQT8TOJO, quantity=2","@i":"99a07cd5"}

d673ca76-3966-4174-b950-4c3f3aa22dfe

4SIQT8TOJO

2

7.

8.
-

Clean the data.

As the user ID and the original log record are no longer relevant, let's clean up the result table using the `fields` command.

```
fetch logs, from:now()-3h
| filter dt.process.name=="cartservice cartservice-*"
| filter contains(content, "AddItemAsync")
| fields timestamp, content
| parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"
| fields productId , productQuantity

```

**Results table**

productId

productQuantity

1ZYFJ3GM2N

1

L2ECAV7KIM

5

LS3PSXUNUM

5

4SIQT8TOJO

2

9.

10.
-

Summarize events per product.

To see the total amount of each product added to a cart, use the `sum()` function.

```
fetch logs, from:now()-3h
| filter dt.process.name=="cartservice cartservice-*"
| filter contains(content, "AddItemAsync")
| fields timestamp, content
| parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"
| fields productId , productQuantity
| summarize sum(productQuantity), by:{productId}

```

**Results table**

productId

sum(productQuantity)

APUK6V6EV0

61

B9ECA1YMWWN1N4OV7KIM

47

66CDHSJNUP

38

9DIQT8TOJO

32

11.

12.
-

Find the most popular products.

To understand the behavior of an average user, we want to determine the average size of the cart for each product. To do that, we use the `avg()` function and name the new field `averageProductQuantity`. Then we sort the average values from highest to lowest, and we limit the results so that we see the five most popular products.

```
fetch logs, from:now()-3h
| filter dt.process.name=="cartservice cartservice-*"
| filter contains(content, "AddItemAsync")
| fields timestamp, content
| parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"
| fields productId , productQuantity
| summarize averageProductQuantity = avg(productQuantity), by:{productId}
| sort averageProductQuantity desc
| limit 5

```

**Results table**

averageProductQuantity

productId

4.746268656716418

1ZYFJ3GM2N

4.4375

26VCHSJNUP

4.415584415584416

LS3PSXUNUM

4.3604651162790695

L4ECAV7KIM

4.2682926829268295

1YMWWN1N4O

13.

### Example 3: Track user changes

In this example, you track user changes with audit logs. You want to track the type and quantity of actions performed by users.

1.

2.
-

Check the availability of recent audits logs.

- Find out if any audit logs have been available within the last five minutes.

- Set the time range and filter only logs whose source path ends with your designated path.

```
fetch logs, from:now()-5m
| filter endsWith(log.source,"change.log")

```

**Results table**

content

timestamp

dt.entity.host

dt.entity.process_group

2022-07-15 09:08:00 UTC {"eventType":"UPDATE","tenantId":"abc","use…

15.7.2022 12:08

HOST-1

PROCESS_GROUP-12ED48520DB559D1

2022-07-15 09:08:07 UTC {"eventType":"CREATE","tenantId":"efg","use…

15.7.2022 12:08:07

HOST-2

PROCESS_GROUP-34ED48520DB559D2

2022-07-15 09:11:19 UTC {"eventType":"UPDATE","tenantId":"hij","use…

15.7.2022 12:11:19

HOST-3

PROCESS_GROUP-56ED48520DB559D3

2022-07-15 09:11:19 UTC {"eventType":"DELETE","tenantId":"klm","use…

15.7.2022 12:11:19

HOST-4

PROCESS_GROUP-78ED48520DB559D4

3.

4.
-

Extract relevant fields for a single user.

- The retrieved table includes record updates, deletions, and creations.

- If you limit your query to the last result, you can understand actions performed by a single user.

Then we do the following:

- Use `parse` to turn the `content` field into a JSON object

- Use `fieldsAdd` to extract relevant fields from that object

- Use `fields` to add a relevant field

- Use `fieldsRemove` to retrieve only the columns that you need

```
fetch logs, from:now()-5m
| filter endsWith(log.source,"change.log")
| limit 1
| parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"
| fields ts, settings
| fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]
| fieldsRemove settings

```

**Results table**

ts

type

tenant

user

2022-07-14 09:19:34

UPDATE

abc

1aae042c-ab34-4f01-8d46-128971703d5a

5.

6.
-

Get the users who performed updates and deletions.

To get users who made updates or deletions only:

- Remove the `limit` command

- Add a filter for the two action types: update and delete.

```
fetch logs, from:now()-5m
| filter endsWith(log.source,"change.log")
| parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"
| fields ts, settings
| fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]
| fieldsRemove settings
| filter in(type,array("UPDATE","DELETE"))

```

**Results table**

ts

type

tenant

user

2022-07-14 09:19:34

UPDATE

abc

2aae042c-ab34-4f01-8d46-128971703d5b

2022-07-14 05:11:04

UPDATE

abc

386b63fc-1516-4b46-9714-ee53dd76c99c

2022-07-14 05:00:49

DELETE

abc

486b63fc-1516-4b46-9714-ee53dd76c99d

2022-07-14 04:21:43

DELETE

abc

586b63fc-1516-4b46-9714-ee53dd76c99e

7.

8.
-

Find out the change types and the number of changes performed by each user.

You can count the records using the `summarize` command.

```
fetch logs, from:now()-5m
| filter endsWith(log.source,"change.log")
| parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"
| fields ts, settings
| fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]
| fieldsRemove settings
| filter in(type,array("UPDATE","DELETE"))
| summarize count(), by:{user,type}

```

**Results table**

user

type

count()

686b63fc-1516-4b46-9714-ee53dd76c99f

DELETE

78

786b63fc-1516-4b46-9714-ee53dd76c99g

UPDATE

34

8aae042c-ab34-4f01-8d46-128971703d5h

UPDATE

20

9d4a7ac8-e451-6469-cced-6f4358ef343i

UPDATE

17

9.

10.
-

Count the events per user, split by action type (create, update, delete).

You can perform the calculation by combining the `summarize` commmand with the `countIf` function.

```
fetch logs, from:now()-5m
| filter endsWith(log.source,"change.log")
| parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"
| fields ts, settings
| fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]
| fieldsRemove settings
| filter in(type,array("UPDATE","DELETE"))
| summarize {countIf(type=="CREATE"), countIf(type=="UPDATE"), countIf(type=="DELETE")}, by:{tenant, user}

```

**Results table**

tenant

user

countIf(type=="CREATE")

countIf(type=="UPDATE")

countIf(type=="DELETE")

def

186b63fc-1516-4b46-9714-ee53dd76c99a

0

34

78

ghi

2aae042c-ab34-4f01-8d46-128971703d5b

19

20

8

jkl

3d4a7ac8-e451-6469-cced-6f4358ef343c

2

17

11

11.

### Example 4: Create a log metric

In this example, you need to count how many refused connections are recorded in your log data. For that, filter the correct logs and turn the number of occurrences into a log metric.

- [Create connections refused metric](/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric#lma-uc-create-connections-refused-metric)

In this example, you need to monitor an attribute of your logs, and you need to keep an eye on the error levels reported in your logs from your K8s cluster.

- [Create log attribute metric](/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric#lma-uc-create-log-attribute-metric)

### Example 5: Create a log alert

In this example, you need to set an alert based on the occurrence of log events. See how you can extract data from logs, create a processing rule, build an alert by forming a log event, and check if your alert captures logs that meet predefined criteria.

- [Set up alerts based on events extracted from logs](/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events)

### Create anomaly detection metric

In this use case, you need to automate anomaly detection. See how you can extract data from logs, create a processing rule, create a metric, and create an alert that generates a notification if an anomaly occurs.

- [Set up custom alerts based on metrics extracted from logs](/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics)
