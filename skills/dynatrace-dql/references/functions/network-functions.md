> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/network-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/network-functions)

# Network functions

Functions related to IP addresses.

## ip

You can use this function to create an IP address.

#### Syntax

`ip(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to create a new IP address. |  |  |

#### Returns

The data type of the returned value is `ip`.

#### Examples

##### Example 1

```
data record(value = "127.0.0.1"),
     record(value = "2001:0db8:0000:0000:0000:8a2e:0370:7334"),
     record(value = "2001:db8::8a2e:370:7334"),
     record(value = "::1"),
     record(value = "317.0.0.1") // invalid IPv4
| fieldsAdd ip(value)

```

Query result:

| value |  | ip(value) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `127.0.0.1` |  | `2001:0db8:0000:0000:0000:8a2e:0370:7334` |  | `2001:0db8::8a2e:0370:7334` |  | `2001:db8::8a2e:370:7334` |
| `2001:0db8::8a2e:0370:7334` |  | `::1` |  | `::0001` |  | `317.0.0.1` |  | *null* |

## ipIn

This function returns a Boolean which indicates if at least one IP address of the first parameter can be found in the following ones - the same behavior as the in() function.

#### Syntax

`ipIn(needle_expressions, haystack_expressions...)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| needle_expressions |  | string, ip, array of string expressions/IP addresses |  | Represents the IP addresses that needs to be found in the haystack_expressions. |  |  |
| haystack_expressions |  | string, ip, array of string expressions/ip addresses |  | The variable argument list where the needle_expressions should be found. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "127.0.0.1", b = "127.0.0.1"),
     record(a = "127.0.0.1", b = "127.0.0.1/8"),
     record(a = "127.0.0.1/8", b = "127.0.0.1"),
     record(a = "127.0.0.1/8", b = "127.0.0.1/16"),
     record(a = array("127.0.0.1", "10.0.0.1"), b = "127.0.0.1"),
     record(a = array("127.0.0.1", "10.0.0.1"), b = array("127.0.0.1/8", "10.0.0.2"))
| fieldsAdd ipIn(a, b)

```

Query result:

| a |  | b |  | ipIn(a, b) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `127.0.0.1` |  | `true` |  | `127.0.0.1` |  | `127.0.0.1/8` |  | `true` |
| `127.0.0.1/8` |  | `127.0.0.1` |  | `false` |  | `127.0.0.1/8` |  | `127.0.0.1/16` |  | `false` |
| `[127.0.0.1, 10.0.0.1]` |  | `127.0.0.1` |  | `true` |  | `[127.0.0.1, 10.0.0.1]` |  | `[127.0.0.1/8, 10.0.0.2]` |  | `true` |

##### Example 2

```
data record(a = ip("127.0.0.1"), b = ip("127.0.0.1")),
     record(a = array(ip("127.0.0.1"), ip("10.0.0.1")), b = ip("127.0.0.1")),
     record(a = array(ip("127.0.0.1"), ip("10.0.0.1")), b = array(ip("127.0.0.1"), ip("10.0.0.2")))
| fieldsAdd ipIn(a, b)

```

Query result:

| a |  | b |  | ipIn(a, b) |
| --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `127.0.0.1` |  | `true` |
| `[127.0.0.1, 10.0.0.1]` |  | `127.0.0.1` |  | `true` |
| `[127.0.0.1, 10.0.0.1]` |  | `[127.0.0.1, 10.0.0.2]` |  | `true` |

##### Example 3

```
data record(a = ip("127.0.0.1"), b = "127.0.0.1/8"),
     record(a = array("127.0.0.1", ip("10.0.0.1")), b = "127.0.0.1"),
     record(a = array("127.0.0.1", ip("10.0.0.1")), b = array("127.0.0.1/8", ip("10.0.0.2")))
| fieldsAdd ipIn(a, b)

```

Query result:

| a |  | b |  | ipIn(a, b) |
| --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `127.0.0.1/8` |  | `true` |
| `[127.0.0.1, 10.0.0.1]` |  | `127.0.0.1` |  | `true` |
| `[127.0.0.1, 10.0.0.1]` |  | `[127.0.0.1/8, 10.0.0.2]` |  | `true` |

## ipIsLinkLocal

Checks if an IP address is a link-local IP address.

#### Syntax

`ipIsLinkLocal(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to check if it is a particular type of IP address. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "169.254.0.0"),
     record(a = "169.254.255.255"),
     record(a = "169.255.0.0")
| fieldsAdd ipIsLinkLocal(a)

```

Query result:

| a |  | ipIsLinkLocal(a) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `169.254.0.0` |  | `true` |  | `169.254.255.255` |  | `true` |  | `169.255.0.0` |  | `false` |

## ipIsLoopback

Checks if an IP address is a loopback IP address.

#### Syntax

`ipIsLoopback(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to check if it is a particular type of IP address. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "127.0.0.1"),
     record(a = "10.0.0.1"),
     record(a = "::1")
| fieldsAdd ipIsLoopback(a)

```

Query result:

| a |  | ipIsLoopback(a) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `true` |  | `10.0.0.1` |  | `false` |  | `::1` |  | `true` |

## ipIsPrivate

Checks if an IP address is a private IP address.

#### Syntax

`ipIsPrivate(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to check if it is a particular type of IP address. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "127.0.0.1"),
     record(a = "10.0.0.1"),
     record(a = "::1"),
     record(a = "172.16.1.1"),
     record(a = "1.2.3.4")
| fieldsAdd ipIsPrivate(a)

```

Query result:

| a |  | ipIsPrivate(a) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `false` |  | `10.0.0.1` |  | `true` |  | `::1` |  | `false` |  | `172.16.1.1` |  | `true` |  | `1.2.3.4` |  | `false` |

## ipIsPublic

Checks if an IP address is a public IP address.

#### Syntax

`ipIsPublic(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to check if it is a particular type of IP address. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "1.2.3.4"),
     record(a = "2001:0db8:0000:0000:0000:8a2e:0370:7334"),
     record(a = "10.0.0.1"),
     record(a = "::1")
| fieldsAdd ipIsPublic(a)

```

Query result:

| a |  | ipIsPublic(a) |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1.2.3.4` |  | `true` |  | `2001:0db8:0000:0000:0000:8a2e:0370:7334` |  | `true` |  | `10.0.0.1` |  | `false` |  | `::1` |  | `false` |

## ipMask

Masks an IP address with given bits (optional parameter for IPv6 addresses).

#### Syntax

`ipMask(expression, maskBits [, ipv6MaskBits])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to check if it is a particular type of IP address. |  |  |

#### Returns

The data type of the returned value is `ip`.

#### Examples

##### Example 1

```
data record(a = "127.1.2.3"),
     record(a = "2001:0db8:0000:0000:0000:8a2e:0370:7334")
| fieldsAdd ipMask(a, 8),
            ipMask(a, 16, ipv6MaskBits: 32)

```

Query result:

| a |  | ipMask(a, 8) |  | ipMask(a, 16, ipv6MaskBits:32) |
| --- | --- | --- | --- | --- |
| `127.1.2.3` |  | `127.0.0.0` |  | `127.1.0.0` |
| `2001:0db8:0000:0000:0000:8a2e:0370:7334` |  | `2000::0000` |  | `2001:0db8::0000` |

## isIp

Checks if an expression is an IPv4/v6 address.

#### Syntax

`isIp(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to check if it contains/produces an IPv4/v6 address. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "127.0.0.1"),
     record(a = "127.0.0."),
     record(a = toIp("127.0.0.1")),
     record(a = "2001:0db8:0000:0000:0000:8a2e:0370:7334"),
     record(a = toIp("2001:0db8:0000:0000:0000:8a2e:0370:7334")),
     record(a = "2001:0db8:0000:0000:0000:8a2e:0370:")
| fieldsAdd isIp(a)

```

Query result:

| a |  | isIp(a) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `true` |  | `127.0.0.` |  | `false` |  | `127.0.0.1` |  | `true` |  | `2001:0db8:0000:0000:0000:8a2e:0370:7334` |  | `true` |  | `2001:0db8::8a2e:0370:7334` |  | `true` |  | `2001:0db8:0000:0000:0000:8a2e:0370:` |  | `false` |

## isIpV4

Checks if an expression is an IPv4 address.

#### Syntax

`isIpV4(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to check if it contains/produces an IPv4 address. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "127.0.0.1"),
     record(a = "127.0.0."),
     record(a = toIp("127.0.0.1")),
     record(a = "2001:0db8:0000:0000:0000:8a2e:0370:7334"),
     record(a = toIp("2001:0db8:0000:0000:0000:8a2e:0370:7334")),
     record(a = "2001:0db8:0000:0000:0000:8a2e:0370:")
| fieldsAdd isIpV4(a)

```

Query result:

| a |  | isIpV4(a) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `true` |  | `127.0.0.` |  | `false` |  | `127.0.0.1` |  | `true` |  | `2001:0db8:0000:0000:0000:8a2e:0370:7334` |  | `false` |  | `2001:0db8::8a2e:0370:7334` |  | `false` |  | `2001:0db8:0000:0000:0000:8a2e:0370:` |  | `false` |

## isIpV6

Checks if an expression is an IPv6 address.

#### Syntax

`isIpV6(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, ip address |  | The expression to check if it contains/produces an IPv6 address. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "127.0.0.1"),
     record(a = "127.0.0."),
     record(a = toIp("127.0.0.1")),
     record(a = "2001:0db8:0000:0000:0000:8a2e:0370:7334"),
     record(a = toIp("2001:0db8:0000:0000:0000:8a2e:0370:7334")),
     record(a = "2001:0db8:0000:0000:0000:8a2e:0370:")
| fieldsAdd isIpV6(a)

```

Query result:

| a |  | isIpV6(a) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `false` |  | `127.0.0.` |  | `false` |  | `127.0.0.1` |  | `false` |  | `2001:0db8:0000:0000:0000:8a2e:0370:7334` |  | `true` |  | `2001:0db8::8a2e:0370:7334` |  | `true` |  | `2001:0db8:0000:0000:0000:8a2e:0370:` |  | `false` |

## IP address mathematical operations

-

IP address + numeric

-

IP address + IP address

-

IP address - numeric

-

IP address - IP address

#### Examples

##### Example 1

```
data record(a = toIp("127.0.0.10"), b = toIp("10.0.0.1"))
| fieldsAdd a + b, a - b, a + 1, a - 1

```

Query result:

| a |  | b |  | a + b |  | a - b |  | a + 1 |  | a - 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `127.0.0.10` |  | `10.0.0.1` |  | `137.0.0.11` |  | `117.0.0.9` |  | `127.0.0.11` |  | `127.0.0.9` |
