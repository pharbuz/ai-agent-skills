# Eventing And aiohttp

UPnP eventing uses HTTP `SUBSCRIBE`, `UNSUBSCRIBE`, and device `NOTIFY`
callbacks.

## Requesters

```python
from async_upnp_client.aiohttp import AiohttpRequester, AiohttpSessionRequester

requester = AiohttpRequester(timeout=10)
requester = AiohttpSessionRequester(session)
```

Use `AiohttpSessionRequester` when the app already owns an `aiohttp`
`ClientSession`. Use `AiohttpRequester` for standalone tools.

## Notify Server

```python
from async_upnp_client.aiohttp import AiohttpNotifyServer

notify_server = AiohttpNotifyServer(requester, source=("0.0.0.0", 0))
await notify_server.async_start_server()
try:
    print(notify_server.callback_url)
finally:
    await notify_server.async_stop_server()
```

For IPv6, the source uses `AddressTupleVXType`; include the correct scope id.

## Event Handler

```python
from async_upnp_client.event_handler import UpnpEventHandler

event_handler = UpnpEventHandler(notify_server, requester)
sid, timeout = await event_handler.async_subscribe(service)
...
await event_handler.async_unsubscribe(service)
await event_handler.async_stop()
```

Useful methods:

- `sid_for_service(service)`
- `service_for_sid(sid)`
- `handle_notify(http_request)`
- `async_subscribe(service, timeout=...)`
- `async_resubscribe(service_or_sid)`
- `async_resubscribe_all()`
- `async_unsubscribe(service_or_sid)`
- `async_unsubscribe_all()`
- `async_stop()`

## Event Handler Register

`UpnpEventHandlerRegister` manages one event handler per device:

```python
register = UpnpEventHandlerRegister(requester, AiohttpNotifyServer)
handler = await register.async_add_device(device)
...
await register.async_remove_device(device)
```

## Event Callbacks

`UpnpService` emits event callbacks with changed state variables:

```python
def on_event(service, state_variables):
    for state_var in state_variables:
        print(state_var.name, state_var.value)

service.on_event = on_event
```

Always unsubscribe and stop the notify server on shutdown. Broken callback URLs
are a common cause of "subscribed but no events" bugs.
