# Examples

These examples are Markdown reference content for the skill.

## Register An HTTP Service

```python
import socket
from zeroconf import ServiceInfo, Zeroconf

service_type = "_http._tcp.local."
service_name = "Example Web._http._tcp.local."

info = ServiceInfo(
    service_type,
    service_name,
    addresses=[socket.inet_aton("192.0.2.10")],
    port=8080,
    properties={"path": "/", "version": "1"},
    server="example.local.",
)

zc = Zeroconf()
try:
    zc.register_service(info)
    input("Service registered. Press enter to exit.\n")
finally:
    zc.unregister_service(info)
    zc.close()
```

## Browse And Resolve Services

```python
from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf


def on_change(zc, service_type, name, state_change):
    if state_change is ServiceStateChange.Added:
        info = zc.get_service_info(service_type, name, timeout=3000)
        if info:
            print(name, info.server, info.port, info.decoded_properties)
    elif state_change is ServiceStateChange.Removed:
        print("removed", name)


zc = Zeroconf()
browser = ServiceBrowser(zc, "_http._tcp.local.", handlers=[on_change])
try:
    input("Browsing. Press enter to stop.\n")
finally:
    browser.cancel()
    zc.close()
```

## Async Browse

```python
import asyncio
from zeroconf import ServiceStateChange
from zeroconf.asyncio import AsyncServiceBrowser, AsyncZeroconf


async def main():
    aiozc = AsyncZeroconf()

    async def on_change(zc, service_type, name, state_change):
        if state_change is ServiceStateChange.Added:
            info = await aiozc.async_get_service_info(service_type, name)
            if info:
                print(name, info.parsed_addresses(), info.port)

    browser = AsyncServiceBrowser(
        aiozc.zeroconf,
        "_http._tcp.local.",
        handlers=[on_change],
    )
    try:
        await asyncio.sleep(30)
    finally:
        await browser.async_cancel()
        await aiozc.async_close()


asyncio.run(main())
```

## Discover Service Types

```python
from zeroconf import ZeroconfServiceTypes

for service_type in ZeroconfServiceTypes.find(timeout=3):
    print(service_type)
```

## Update TXT Properties

```python
info.properties = {"path": "/", "version": "2"}
zc.update_service(info)
```

Use this only after successful registration and before unregistering/closing.
