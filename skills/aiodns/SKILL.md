---
name: aiodns
description: >-
  Build, debug, migrate, or test asynchronous DNS resolution code with
  `aiodns`. Trigger WHENEVER the user installs or imports `aiodns`; uses
  `aiodns.DNSResolver`, `query_dns`, deprecated `query`, `getaddrinfo`,
  `getnameinfo`, `gethostbyaddr`, deprecated `gethostbyname`, resolver
  nameservers, timeouts, pycares DNSResult/DNSRecord data, A/AAAA/ANY/CAA/CNAME
  MX/NAPTR/NS/PTR/SOA/SRV/TXT records, qclass IN/CHAOS/HS/NONE/ANY, cancellation,
  resolver shutdown, async context managers, Windows selector event loop issues,
  pycares/c-ares errors, or fixes DNS timeouts, NXDOMAIN, cancelled queries,
  malformed hostnames, invalid query types, event loop ownership, and
  aiodns 3.x-to-4.x or future 5.x migration problems.
---

# aiodns

Use this skill for asyncio DNS resolution with `aiodns`, a small wrapper around
`pycares`/c-ares. PyPI and the repository README showed `aiodns 4.0.4` on
2026-07-14; it requires Python `>=3.10`.

```bash
python -m pip show aiodns pycares
python - <<'PY'
import aiodns
print(aiodns.__version__)
PY
```

## Default Workflow

1. Check installed `aiodns` and `pycares` versions.
2. Create one long-lived `DNSResolver` per app/event-loop scope; avoid creating
   a resolver for every query.
3. Prefer `await resolver.query_dns(host, qtype)` in aiodns 4.x.
4. Read answers from `DNSResult.answer`; each item is a `pycares.DNSRecord` with
   `type`, `ttl`, and `data`.
5. Use `getaddrinfo()` for socket connection address selection; do not use
   deprecated `gethostbyname()` in new code.
6. Catch `aiodns.error.DNSError` and inspect `exc.args[0]` for c-ares errno.
7. Call `await resolver.close()` during shutdown from the event loop that
   created the resolver.
8. In tests, use short timeouts, explicit nameservers when appropriate, and
   skip live DNS tests when outbound DNS is blocked.

## Minimal Query

```python
import asyncio
import aiodns


async def main() -> None:
    resolver = aiodns.DNSResolver(timeout=5)
    try:
        result = await resolver.query_dns("example.com", "A")
        for record in result.answer:
            print(record.data.addr, record.ttl)
    finally:
        await resolver.close()


asyncio.run(main())
```

## DNSResolver API

```python
resolver = aiodns.DNSResolver(
    nameservers=["1.1.1.1", "8.8.8.8"],
    timeout=5.0,
)
```

Main methods:

- `query_dns(host, qtype, qclass=None)`: recommended aiodns 4.x DNS query.
- `query(host, qtype, qclass=None)`: deprecated compatibility API.
- `getaddrinfo(host, family=socket.AF_UNSPEC, port=None, proto=0, type=0, flags=0)`.
- `getnameinfo(sockaddr, flags=0)`.
- `gethostbyaddr(name)`.
- `gethostbyname(host, family)`: deprecated; use `getaddrinfo()`.
- `cancel()`: cancels pending queries with `ARES_ECANCELLED`.
- `close()`: async cleanup; cancels pending queries and releases resources.

Supported query types: `A`, `AAAA`, `ANY`, `CAA`, `CNAME`, `MX`, `NAPTR`, `NS`,
`PTR`, `SOA`, `SRV`, `TXT`.

Supported query classes: `IN`, `CHAOS`, `HS`, `NONE`, `ANY`.

## Migration Rule

For aiodns 4.x:

```python
# Deprecated 3.x-compatible result shape
records = await resolver.query("example.com", "MX")

# Recommended 4.x shape
result = await resolver.query_dns("example.com", "MX")
records = result.answer
```

In 4.x, `query_dns()` returns native `pycares 5.x` result types. The README says
future aiodns 5.x will make `query()` the primary pycares-returning API and keep
`query_dns()` as a compatibility alias.

## Decision Rules

- Use `query_dns()` for DNS RR queries and `getaddrinfo()` for connecting
  sockets.
- Do not assume every query returns a list in the new API; always inspect
  `DNSResult.answer`, `authority`, and `additional`.
- Do not close a resolver from a different loop than the one that created it.
- Do not rely on implicit GC cleanup; always `await resolver.close()`.
- On Windows, only switch to `WindowsSelectorEventLoopPolicy` for custom
  non-thread-safe pycares/c-ares builds that require `add_reader/add_writer`.
- Treat `query()` and `gethostbyname()` deprecation warnings as migration work,
  not noise.

## References

- Read [references/resolver-api.md](references/resolver-api.md) for
  constructor options, method behavior, query types/classes, and lifecycle.
- Read [references/results-and-records.md](references/results-and-records.md)
  for `pycares` result shapes and record field access by RR type.
- Read [references/migration-and-compatibility.md](references/migration-and-compatibility.md)
  for aiodns 3.x→4.x and future 5.x migration rules.
- Read [references/errors-windows-and-testing.md](references/errors-windows-and-testing.md)
  for `DNSError`, c-ares errno constants, cancellation, Windows loops, and tests.
- Read [references/examples.md](references/examples.md) for complete code
  patterns in Markdown form.
