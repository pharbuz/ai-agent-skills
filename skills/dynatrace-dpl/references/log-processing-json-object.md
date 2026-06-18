> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object)

# DPL JSON Objects

**JSON, JSON_OBJECT**

parses Json **objects** (structure of name-value pairs enclosed in curly brackets) according to [RFC 8259](https://tools.ietf.org/html/rfc8259).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| variant_object |  | none |  |  |

There are several ways how to control parsing elements from a JSON object. The easiest is to use the JSON matcher without any parameters. It will enumerate all elements, transform them into Log processing data type from their defined type in JSON and returns a variant_object with parsed elements.

#### Example

A JSON object:

```
{
    "name":"John",
    "age":33,
    "weight":72.3,
    "isMarried":true,
    "children":["Mallory", "Mary"],
    "address":{"city":"New York", "street":"1'st str 3", "zip":23456}
}

```

Can be automatically parsed as using pattern:

```
JSON:person

```

The result of parsing is a variant_object. The members have variant type transformed from their Json type (double-click on the resultset row to see the details):namevaluetype`person[name]``John``VARIANT<STRING>``person[age]``33``VARIANT<LONG>``person[weight]``72.3``VARIANT<DOUBLE>``person[isMarried]``true``VARIANT<BOOLEAN>``person[children]``['Mallory','Mary']``VARIANT<VARIANT_ARRAY>``person[address][city]``New York``VARIANT<STRING>``person[address][street]``1'st str 3``VARIANT<STRING>``person[address][zip]``23456``VARIANT<LONG>`

### Parsing selected members with a specified matcher

**JSON{ MATCHER:member_name, …}**

JSON allows extracting members explicitly as a comma-separated list of matcher-name pairs, separated by a colon (`:`) and enclosed in curly braces(`{}`). The MATCHER refers to the Dynatrace Pattern Language matchers.

When a member has a name consisting of multiple words the `member_name` should be enclosed in single or double quotes and appended with a colon ":" following a single word export name (override). See handling "client time" member in the example below.

Using override export name `null` will cause the member omitted from resultset.

#### Example

Suppose we're primarily interested in IP-address, port and
client timestamp in the following object:

```
{
 "ip":"192.168.3.20",
 "port":443,
 "client time":"2018-07-25 13:18:57 -0600",
 "ready":true,
 "descr":"2'nd floor printer"
}

```

We can extract these members explicitly. Using the `greedy` config parameter we can capture also the rest of the members.

```
JSON{
 IPADDR:"ip",
 INT:"port",
 TIMESTAMP('yyyy-MM-dd HH:mm:ss Z'):"client time":client_time
}(greedy='other members'):host

```

Resulting tuple contains explicitly parsed members with specified primitive types and the rest with VARIANT types (double-click on the resultset row to see the details):namevaluetype`host[ip]``192.168.3.20 // --``IPADDR``host[port]``443``INTEGER``host[client_time]``2018-07-25 22:18:57.000 +0300``TIMESTAMP``host[other members][ready]``true``VARIANT<BOOLEAN>``host[other members][descr]``2'nd floor printer``VARIANT<STRING>`

### Semantic validation of a JSON object

When the engine does not find an explicitly specified member then it’s respective value in output is set to NULL by default. However, sometimes we might want parsing to fail if mandatory members are not present - i.e validate semantic rules of a JSON object. This can be achieved by applying quantifier `+` (match at least one or more times) to a member.

With mandatory member missing the whole JSON matcher fails, output tuple members are set to their default values.

#### Example

Suppose our application requires 'name' and 'age' members in following JSON objects to be mandatory. The 'biography' member is optional and can be quite large, up to 50 Kb in size:

```
{
    "name":"John",
    "age":55,
    "biography":"Once upon a time there lived a man called John ..."
}
{"name":"Eve", "gender":"female"}

```

In a pattern we can enforce these semantic rules by using `+` quantifier and `maxlen` configuration parameter:

```
JSON {
    STRING+:name,
    INT+:age,
    STRING:biography
}(maxlen=51000):person

```

Parsing results in the first object successfully parsed, the second object fails due to member `age` missing.person`{name='John' age=55 biography='Once upon...'}``{name='' age=-1 biography=''}`

### Parsing non-standard JSON objects

By default, JSON matcher treats JSON object members strictly according to [RFC 8259](https://tools.ietf.org/html/rfc8259) syntax. However, under certain circumstances relaxing this validation may be a good idea. For instance, investigating a malicious behavior or when an application is producing an invalid JSON object. This can be achieved using the `strict` configuration parameter set to false.

#### Example

Suppose an incoming HTTP request contains following JSON object containing hostname, department name, and IP-address. Note the unquoted name and string values, and IP-address presented as UNICODE character string:

```
{
host:"example.com"
    ,
"department" : HR    ,
    ip : "\u0031\u0039\u0032.\u0031\u0036\u0038.\u0034\u0037.\u0030"
}

```

Pattern:

```
JSON {
 STRING:host,
 STRING:department,
 IPADDR:ip
}(strict=false):data

```

The result is (double-click on the resultset row to see the details):namevaluetype`data[host]``example.com``STRING``data[department]``HR``STRING``data[ip]``192.168.47.0``IPADDR`

### Parsing embedded single type arrays

Arrays within a JSON object, which consist of single type elements, can be parsed using the following syntax:

**conversion_type[] : member_name**

#### Example

Consider the following JSON object with numeric array members:

```
{
 "items":[1,8000,42,200,-999999]
}

```

Following pattern extracts `items` member as an array of integers `<integer>`.

```
JSON{ INT[]:items }:data

```

Result:namevaluetype`items[0]``1``INTEGER``items[1]``8000``INTEGER``items[2]``42``INTEGER``items[3]``300``INTEGER``items[4]``-999999``INTEGER`

You can parse also multidimensional arrays. Just add as many square bracket pairs your array is composed of.

#### Example

Parsing two dimensional json array:

```
{ "items":[[1,3,6,9],[4,4,59,100],[32,17,999,8]] }

```

Pattern:

```
JSON { LONG[][]:items }:data

```

Result (double-click on the resultset row to see the details):namevaluetype`data[items][0][0]``1``LONG``data[items][0][1]``3``LONG``data[items][0][2]``6``LONG``data[items][0][3]``9``LONG``data[items][1][0]``4``LONG``data[items][1][1]``4``LONG``data[items][1][2]``59``LONG``data[items][1][3]``100``LONG``data[items][2][0]``32``LONG``data[items][2][1]``17``LONG``data[items][2][2]``999``LONG``data[items][2][3]``8``LONG`

### Parsing Embedded Objects

For parsing JSON objects inside an object, you need to use the JSON {JSON_OBJECT} matcher.

#### Example

Consider following JSON with an embedded `callerId` object:

```
{
  "name":"Evelyn",
  "age":32,
  "pId":1,
  "callerId":{
     "nickname":"eve",
     "ip":"192.168.1.0"
   }
}

```

We extract `name, age` and `callerId` members:

```
JSON {
 STRING:name,
 INT:age,
 JSON {
    STRING:nickname,
    IPV4:ip
 }:callerId
}:person

```

Results:namevaluetype`person[name]``Evelyn``STRING``person[age]``32``INTEGER``person[callerId][nickname]``eve``STRING``person[callerId][ip]``291.168.1.0``IPADDR`
