# Asyncio API

Use `zeroconf.asyncio` in asyncio apps.

## Imports

```python
from zeroconf.asyncio import (
    AsyncServiceBrowser,
    AsyncServiceInfo,
    AsyncZeroconf,
    AsyncZeroconfServiceTypes,
)
```

## AsyncZeroconf

`AsyncZeroconf` wraps a regular `Zeroconf` instance at `.zeroconf` and exposes:

- `async_register_service(info, allow_name_change=False, cooperating_responders=False)`
- `async_unregister_service(info)`
- `async_unregister_all_services()`
- `async_update_service(info)`
- `async_get_service_info(type_, name, timeout=...)`
- `async_add_service_listener(type_, listener)`
- `async_remove_service_listener(listener)`
- `async_remove_all_service_listeners()`
- `async_update_interfaces(interfaces)`
- `async_close()`

Always `await aiozc.async_close()` during shutdown.

## AsyncServiceBrowser

```python
browser = AsyncServiceBrowser(aiozc.zeroconf, "_http._tcp.local.", handlers=[handler])
...
await browser.async_cancel()
```

It exposes `types`, `zc`, `query_scheduler`, `done`, and `async_cancel()`.

## AsyncServiceInfo

`AsyncServiceInfo` has the same service fields as `ServiceInfo`, plus async
resolution/cache behavior. Important fields include:

- `type`, `name`, `server`, `port`, `weight`, `priority`
- `addresses`, `text`, `properties`
- `host_ttl`, `other_ttl`, `interface_index`
- `key`, `server_key`

Use async methods inherited from service info behavior, such as
`async_request()` and `async_wait()` when available in the installed version.

## Async Service Type Discovery

```python
types = await AsyncZeroconfServiceTypes.async_find(timeout=3)
```

## Event Loop Rules

- Do not call blocking sync methods like `get_service_info()` in latency-sensitive
  async paths.
- Keep callbacks fast; slow handlers can block mDNS processing.
- If a callback must do I/O, schedule a task and handle cancellation/errors.
- Handle `EventLoopBlocked` as an operational symptom: reduce blocking work,
  move CPU-heavy code off the loop, or fix sync calls in async handlers.
