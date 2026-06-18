> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands)

# DQL extraction and parsing commands

## parse

Parses a record field and puts the result(s) into one or more fields as specified in the pattern.

The parse command works in combination with the [Dynatrace Pattern Language](/platform/grail/dynatrace-pattern-language) for parsing strings.

#### Syntax

`parse expression, pattern [, preserveFieldsOnFailure] [, parsingPrerequisite]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | A field or string expression to parse. |  |  |
| pattern |  |  |  |  |  |  |
| The parse pattern. |  |  |  |  |  |  |
| preserveFieldsOnFailure |  | boolean |  | Determines if field values should be preserved if parsing fails. When used in OpenPipeline, the value is `true`. |  |  |
| parsingPrerequisite |  | boolean |  | Determines if record should be parsed. |  |  |

#### Basic example

##### Example: Parse log content

The following example parses the `content` field, which shows the content of a log line.
The `parse` command adds the parsed fields to the set of fields of the record.

```
data record(content="117.16.75.9--[14/Mar/2016:23:34:25 +0200] GET//setup.php HTTP/1.1 404 474")
| parse content, "IPV4:ip LD HTTPDATE:time ']' LD:text"

```

Query result:

| content |
| --- |
| ip |
| time |
| text |
| `117.16.75.9--[14/Mar/2016:23:34:25 +0200] GET//setup.php HTTP/1.1 404 474` |
| `117.16.75.9` |
| `2016-03-14T21:34:25.000Z` |
| `" GET//setup.php HTTP/1.1 404 474"` |

##### Example: Handle parsing failures when overwriting fields

The following example parses the `content` field preserving existing fields specified in the pattern if parsing fails for the record.

```
data record(content = "1,alice,192.168.1.1"),
     record(content = "2,,10.6.24.18", username = "bob"),
     record(content = "3,mallory,192.168.1.3")
| parse content, "( INT:sequence LD:username IPADDR:ip)(fs=',')",
    preserveFieldsOnFailure: true

```

Query result:

| content |  | sequence |  | username |  | ip |  | `1,alice,192.168.1.1` |  | `1` |  | `alice` |  | `192.168.1.1` |  | `2,,10.6.24.18` |  | `null` |  | `bob` |  | `null` |  | `3,mallory,192.168.1.3` |  | `3` |  | `mallory` |  | `192.168.1.3` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example: Conditional parsing of log content

The following example conditionally parses the content field. The `parsingPrerequisite` parameter of the `parse` command determines which records to parse.

```
data record(content = "2016-03-14 23:37:07;www.example.com (192.168.0.1)"),
     record(content = "2016-03-14 23:37:06;www.example.com")
| parse content, "TIMESTAMP ';'LD ( '(' IPADDR:server ')' )",
    parsingPrerequisite: contains(content,"(")

```

Query result:

| content |  | server |  | `2016-03-14 23:37:07;www.example.com (192.168.0.1)` |  | `192.168.0.1` |  | `2016-03-14 23:37:06;www.example.com` |  | `null` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Practical example

##### Example: Apache access logs

In the following example, the `parse` command extracts all the relevant fields from Apache access logs.

```
fetch logs
| filter dt.entity.process_group == "PROCESS_GROUP-628E1D4CAD1B41B9"
| fieldsKeep content
| parse content, """(IPADDR:'http.client_ip' | [! \n]+):host
    ' ' ('-' | NSPACE:ident)
    ' ' ('-' | (DATA{1,8096}:auth >>(' [' HTTPDATE)))
    ' ' '[' HTTPDATE:event_time ']'
    ' ' (('\"' [A-Z-_]+:'http.method' ' '  LD{0,8096}:uri ' ' LD{3,10}:'http.flavor' '\"')
            | DQS:invalid_request
      )
    ' ' LONG:'http.status_code'
    ' ' (LONG:'http.response.content_length' | '-')
    (' ' DQS:referer (' ' DQS:user_agent)?)?"""
| summarize count = count(), by: { http.status_code }

```

In case of identical names, fields added by the parse command override the existing fields. When two identical field names are specified in the DQL statement, a warning "The field `<fieldName>` overrides an existing field." is returned.
