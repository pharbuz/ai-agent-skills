# Results And Records

aiodns 4.x `query_dns()` returns native `pycares 5.x` result types.

## DNSResult Shape

```python
result = await resolver.query_dns("example.com", "MX")
for record in result.answer:
    ...
for record in result.authority:
    ...
for record in result.additional:
    ...
```

Each record has:

- `record.type`
- `record.ttl`
- `record.data`

`record.data` depends on the DNS record type.

## Common Record Fields

```python
# A / AAAA
record.data.addr

# CNAME / NS / PTR
record.data.name

# MX
record.data.exchange
record.data.priority

# SRV
record.data.host
record.data.port
record.data.priority
record.data.weight

# SOA
record.data.nsname
record.data.hostmaster
record.data.serial
record.data.refresh
record.data.retry
record.data.expires
record.data.minttl

# TXT
record.data.text

# CAA / NAPTR
# Inspect pycares docs or print vars(record.data) for exact fields.
```

When adding support for a less common RR type, inspect the data object in a
test:

```python
print(record.type, record.ttl, vars(record.data))
```

## getaddrinfo Result

`getaddrinfo()` returns `pycares.AddrInfoResult`:

- `cnames`: CNAME records encountered.
- `nodes`: address nodes.

Each node typically includes `family`, `socktype`, `protocol`, `addr`, `ttl`,
and `flags`.

```python
result = await resolver.getaddrinfo("example.com", port=443)
for node in result.nodes:
    print(node.family, node.socktype, node.protocol, node.addr)
```

## getnameinfo / gethostbyaddr

`getnameinfo()` returns `pycares.NameInfoResult`, usually with host/service
fields. `gethostbyaddr()` returns `pycares.HostResult` with:

- `name`
- `aliases`
- `addresses`

Use these APIs for reverse lookup flows instead of hand-building PTR names when
the socket-style result is what the caller needs.
