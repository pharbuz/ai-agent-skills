# Examples

These examples are Markdown reference content for the skill.

## Create Device And Call Action

```python
from async_upnp_client.aiohttp import AiohttpRequester
from async_upnp_client.client_factory import UpnpFactory


async def get_volume(description_url: str) -> int | None:
    requester = AiohttpRequester(timeout=10)
    factory = UpnpFactory(requester, non_strict=True)
    device = await factory.async_create_device(description_url)

    service = device.service_id("urn:upnp-org:serviceId:RenderingControl")
    if not service or not service.has_action("GetVolume"):
        return None

    result = await service.async_call_action(
        "GetVolume",
        InstanceID=0,
        Channel="Master",
    )
    return result.get("CurrentVolume")
```

## One-Shot SSDP Search

```python
from async_upnp_client.search import async_search


async def on_response(headers):
    print(headers.get("LOCATION"), headers.get("ST"), headers.get("_udn"))


await async_search(async_callback=on_response)
```

## Combined SSDP Listener

```python
from async_upnp_client.ssdp_listener import SsdpListener


async def on_alive(headers):
    print("alive", headers.get("_udn"), headers.get("LOCATION"))


listener = SsdpListener(on_alive=on_alive)
await listener.async_start()
try:
    await listener.async_search()
finally:
    await listener.async_stop()
```

## Subscribe To Service Events

```python
from async_upnp_client.aiohttp import AiohttpNotifyServer
from async_upnp_client.event_handler import UpnpEventHandler


def on_event(service, state_variables):
    for state_var in state_variables:
        print(state_var.name, state_var.value)


notify_server = AiohttpNotifyServer(requester, source=("0.0.0.0", 0))
await notify_server.async_start_server()
event_handler = UpnpEventHandler(notify_server, requester)
service.on_event = on_event
try:
    await event_handler.async_subscribe(service)
finally:
    await event_handler.async_unsubscribe(service)
    await event_handler.async_stop()
    await notify_server.async_stop_server()
```

## IGD External IP

```python
from async_upnp_client.profiles.igd import IgdDevice

igd = IgdDevice(device, event_handler=None)
external_ip = await igd.async_get_external_ip_address()
```

## DLNA Renderer Play

```python
from async_upnp_client.profiles.dlna import DmrDevice

dmr = DmrDevice(device, event_handler=None)
await dmr.async_update()
if dmr.can_play():
    await dmr.async_play()
```
