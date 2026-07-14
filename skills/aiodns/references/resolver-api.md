# Resolver API

Import:

```python
import aiodns
from aiodns import DNSResolver
```

## Constructor

```python
resolver = DNSResolver(
    nameservers=["1.1.1.1", "8.8.8.8"],
    timeout=5.0,
    tries=4,
    rotate=True,
)
```

`DNSResolver(nameservers=None, loop=None, **kwargs)` creates a `pycares.Channel`.
Most extra keyword arguments are forwarded to `pycares.Channel`, such as
`timeout`, `tries`, `ndots`, `tcp_port`, `udp_port`, `servers`, `domains`,
`lookups`, `rotate`, `local_ip`, `local_dev`, and `resolvconf_path`.

Prefer not to pass `loop` in modern asyncio code unless integrating with legacy
loop management. The resolver belongs to the loop that created it.

## Properties

```python
resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
print(resolver.nameservers)
```

In pycares 5.x, servers may internally include `:53`; aiodns strips the port in
the `nameservers` property for compatibility.

## Queries

```python
result = await resolver.query_dns("example.com", "A")
```

`query_dns(host, qtype, qclass=None)` returns a `pycares.DNSResult` with:

- `answer`
- `authority`
- `additional`

Each section is a list of `pycares.DNSRecord`.

Supported `qtype`: `A`, `AAAA`, `ANY`, `CAA`, `CNAME`, `MX`, `NAPTR`, `NS`,
`PTR`, `SOA`, `SRV`, `TXT`.

Supported `qclass`: `IN`, `CHAOS`, `HS`, `NONE`, `ANY`.

Invalid query types/classes raise `ValueError` synchronously.

## Address Helpers

```python
info = await resolver.getaddrinfo("example.com", family=socket.AF_INET, port=443)
name = await resolver.getnameinfo(("127.0.0.1", 0))
host = await resolver.gethostbyaddr("127.0.0.1")
```

Use `getaddrinfo()` instead of deprecated `gethostbyname()`.

## Cancellation And Shutdown

```python
resolver.cancel()
await resolver.close()
```

`cancel()` cancels pending DNS queries with `ARES_ECANCELLED`. `close()` cancels
pending queries, removes readers/writers/timers if used, closes the pycares
channel, and must be awaited.

The async context manager exists, but the README discourages frequent
create/destroy patterns for normal apps:

```python
async with aiodns.DNSResolver() as resolver:
    await resolver.query_dns("example.com", "A")
```
