# Errors, Windows, And Testing

## DNSError

Import:

```python
import aiodns
from aiodns import error
```

DNS failures raise `aiodns.error.DNSError`. The first argument is a c-ares errno.

```python
try:
    await resolver.query_dns("missing.example.invalid", "A")
except aiodns.error.DNSError as exc:
    errno = exc.args[0]
    if errno == aiodns.error.ARES_ENOTFOUND:
        ...
```

Common errno constants re-exported by `aiodns.error`:

- `ARES_ENOTFOUND`: domain not found / NXDOMAIN-style result.
- `ARES_ETIMEOUT`: query timed out.
- `ARES_ECANCELLED`: query was canceled.
- `ARES_EBADNAME`: malformed domain name.
- `ARES_ECONNREFUSED`: nameserver refused connection.
- `ARES_EREFUSED`: DNS response refused.
- `ARES_ESERVFAIL`: server failure.
- `ARES_ENODATA`: no data for requested type.

## Synchronous Validation Errors

Invalid query type or query class raises `ValueError` before awaiting:

```python
resolver.query_dns("example.com", "INVALID")
resolver.query_dns("example.com", "A", qclass="INVALID")
```

## Windows Event Loop

Official prebuilt `pycares` wheels on PyPI 4.7.0+ include thread-safe c-ares,
so the old ProactorEventLoop limitation usually does not apply.

Only for custom pycares builds linked against non-thread-safe system c-ares,
switch very early:

```python
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

On Python 3.14+, event loop policy APIs are deprecated; prefer creating a
selector loop directly in tests if needed.

## Testing

- Use one resolver per event loop and close it in teardown.
- Use short timeouts and explicit nameservers for deterministic integration
  tests.
- Mark live DNS tests and skip them when outbound DNS is blocked.
- Test invalid qtypes/qclasses without network access.
- For cancellation tests, call `resolver.cancel()` and assert `ARES_ECANCELLED`.
- Avoid depending on unstable public DNS answers; check shape more than exact
  record values.

```python
resolver = aiodns.DNSResolver(timeout=1)
try:
    result = await resolver.query_dns("example.com", "A")
    assert result.answer
finally:
    await resolver.close()
```
