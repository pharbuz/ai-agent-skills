# Migration And Compatibility

## aiodns 4.x

aiodns 4.x adds `query_dns()` and deprecates `query()`.

```python
# Old, deprecated compatibility format
mx_records = await resolver.query("example.com", "MX")
for record in mx_records:
    print(record.host, record.priority)

# New, native pycares format
result = await resolver.query_dns("example.com", "MX")
for record in result.answer:
    print(record.data.exchange, record.data.priority)
```

The old compatibility method remains available for projects that still expect
aiodns 3.x result classes from `aiodns.compat`.

## Future aiodns 5.x

The README documents this planned transition:

- 4.x: `query()` is deprecated and returns compatibility types;
  `query_dns()` returns pycares 5.x types.
- 5.x: `query()` becomes the primary API returning pycares 5.x types;
  `query_dns()` remains as an alias.

To reduce churn, application code can wrap query behavior behind a local helper:

```python
async def query_records(resolver, host: str, qtype: str):
    result = await resolver.query_dns(host, qtype)
    return result.answer
```

## Deprecated APIs

- Replace `query()` with `query_dns()` in aiodns 4.x code.
- Replace `gethostbyname()` with `getaddrinfo()`.

If maintaining old code, suppress deprecation warnings only around compatibility
tests, not in production code.

## Version Checks

```python
import aiodns
from packaging.version import Version

if Version(aiodns.__version__) >= Version("4"):
    ...
```

Prefer dependency pins and CI test matrices over runtime version branching when
maintaining libraries.
