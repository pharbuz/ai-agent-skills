---
name: python-zeroconf
description: >-
  Build, debug, or refactor Python multicast DNS / DNS-SD service discovery
  code with the `zeroconf` package. Trigger WHENEVER the user installs or
  imports `zeroconf`; uses `Zeroconf`, `ServiceInfo`, `ServiceBrowser`,
  `ServiceListener`, `ZeroconfServiceTypes`, `IPVersion`, `InterfaceChoice`,
  `ServiceStateChange`, `DNSQuestionType`, `RecordUpdateListener`, async APIs
  from `zeroconf.asyncio` such as `AsyncZeroconf`, `AsyncServiceInfo`,
  `AsyncServiceBrowser`, or fixes mDNS browsing, service registration,
  TXT/properties encoding, IPv4/IPv6 interface selection, non-unique names,
  event-loop blocking, stale service cache, callbacks, shutdown, or network
  multicast issues.
---

# python-zeroconf

Use this skill for Python mDNS/DNS-SD with the `zeroconf` package
(`pip install zeroconf`). The docs and PyPI showed version `0.150.0` on
2026-07-14; the package requires Python `>=3.10`.

```bash
python -m pip show zeroconf
python - <<'PY'
import zeroconf
print(getattr(zeroconf, "__version__", "unknown"))
PY
```

## Choose The API

- Use synchronous `Zeroconf`, `ServiceInfo`, and `ServiceBrowser` in scripts or
  threaded/non-async apps.
- Use `zeroconf.asyncio.AsyncZeroconf`, `AsyncServiceInfo`, and
  `AsyncServiceBrowser` inside asyncio apps.
- Use `ZeroconfServiceTypes.find()` or `AsyncZeroconfServiceTypes.async_find()`
  to discover advertised service types.
- Use `ServiceListener` callback objects or handler callables for browser
  events.
- Use `RecordUpdateListener` only when reacting to low-level DNS record updates.

## Default Workflow

1. Check package version, OS/network environment, firewall, multicast support,
   interface choice, IPv4/IPv6 requirements, and whether an event loop is active.
2. Pick sync or async API; do not call blocking sync lookup/registration methods
   inside a hot asyncio path.
3. For service registration, build a valid `ServiceInfo` with matching `type_`
   and fully qualified `name`, encoded addresses, port, server, and TXT
   properties.
4. For browsing, keep a reference to `ServiceBrowser`/`AsyncServiceBrowser` and
   cancel it during shutdown.
5. Resolve service details with `get_service_info()` or
   `async_get_service_info()` after receiving an Added/Updated event.
6. Always unregister services and close Zeroconf instances during shutdown.
7. In tests, isolate service names, use short timeouts, and skip live multicast
   tests when the environment blocks UDP multicast.

## Minimal Registration

```python
import socket
from zeroconf import ServiceInfo, Zeroconf

service_type = "_http._tcp.local."
service_name = "Example Web._http._tcp.local."

info = ServiceInfo(
    type_=service_type,
    name=service_name,
    addresses=[socket.inet_aton("192.0.2.10")],
    port=8080,
    properties={"path": "/"},
    server="example.local.",
)

zeroconf = Zeroconf()
try:
    zeroconf.register_service(info)
finally:
    zeroconf.unregister_service(info)
    zeroconf.close()
```

## Minimal Browsing

```python
from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf


def on_service_state_change(zeroconf, service_type, name, state_change):
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            print(name, info.parsed_scoped_addresses(), info.port)


zeroconf = Zeroconf()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", handlers=[on_service_state_change])
try:
    input("Press enter to stop browsing\n")
finally:
    browser.cancel()
    zeroconf.close()
```

## Minimal Async Pattern

```python
import asyncio
from zeroconf.asyncio import AsyncServiceBrowser, AsyncZeroconf
from zeroconf import ServiceStateChange


async def main() -> None:
    aiozc = AsyncZeroconf()

    async def on_change(zeroconf, service_type, name, state_change):
        if state_change is ServiceStateChange.Added:
            info = await aiozc.async_get_service_info(service_type, name)
            if info:
                print(name, info.parsed_scoped_addresses(), info.port)

    browser = AsyncServiceBrowser(
        aiozc.zeroconf,
        "_http._tcp.local.",
        handlers=[on_change],
    )
    try:
        await asyncio.sleep(10)
    finally:
        await browser.async_cancel()
        await aiozc.async_close()


asyncio.run(main())
```

## Decision Rules

- Service types and names must end with `.local.` and include the service type,
  e.g. `Example._http._tcp.local.`.
- Store TXT properties as `dict[str | bytes, str | bytes | None]`; read
  `decoded_properties` when human-readable strings are needed.
- Use `socket.inet_aton()` for IPv4 address bytes and `socket.inet_pton()` for
  IPv6 address bytes.
- Catch `NonUniqueNameException` or set `allow_name_change=True` only when name
  mutation is acceptable.
- Use explicit `interfaces` and `ip_version` when hosts have multiple NICs,
  VPNs, Docker bridges, or IPv6-only/IPv4-only requirements.
- Never forget `close()` / `async_close()`; open sockets and browser threads can
  keep tests and apps alive.

## References

- Read [references/public-models-and-imports.md](references/public-models-and-imports.md)
  for every public API class/function in the docs and how to import it.
- Read [references/service-info-and-registration.md](references/service-info-and-registration.md)
  for `ServiceInfo`, properties, TTLs, addresses, registration, updates, and
  unregistering.
- Read [references/browsing-and-resolution.md](references/browsing-and-resolution.md)
  for `ServiceBrowser`, callbacks, listeners, state changes, service type
  discovery, and cache behavior.
- Read [references/asyncio-api.md](references/asyncio-api.md) for
  `AsyncZeroconf`, `AsyncServiceInfo`, `AsyncServiceBrowser`, and async
  shutdown patterns.
- Read [references/networking-and-troubleshooting.md](references/networking-and-troubleshooting.md)
  for interface selection, IPv4/IPv6, multicast, exceptions, event-loop
  blocking, and tests.
- Read [references/examples.md](references/examples.md) for complete code
  patterns in Markdown form.
