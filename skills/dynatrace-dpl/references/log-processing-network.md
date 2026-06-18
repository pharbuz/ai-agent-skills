> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-network](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-network)

# DPL Network Data

## IPADDR

Matches IPv4 addresses in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation#IPv4_address)
and IPv6 addresses in [hextet notation](https://en.wikipedia.org/wiki/IPv6_address).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| ipaddr |  | none |  | none |

#### Example

```
192.168.33.1
1080:0:0:0:8:800:200C:417A

```

Pattern:

```
IPADDR:ip EOL;

```

Parsing results ip-addresses in lines 1-2 being parsed into ipaddr field `ip`:ip`192.168.33.1``1080:0:0:0:8:800:200C:417A`

## IPV4, IPV4ADDR

Matches IPv4 addresses in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation#IPv4_address)

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| ipaddr |  | none |  | none |

## IPV6, IPV6ADDR

Matches IPv6 addresses in [hextet notation](https://en.wikipedia.org/wiki/IPv6_address).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| ipaddr |  | none |  | none |

#### Example

```
fe80:0:0:0:8e1:734c:9cca:6bc3
::1
2a00:1450:4010:c05::69

```

Pattern:

```
IPV6:ip EOL;

```

Parsing results addresses in lines 1-3 being extracted into ipaddr field `ip`:ip`fe80::8e1:734c:9cca:6bc3``::1``2a00:1450:4010:c05::69`
