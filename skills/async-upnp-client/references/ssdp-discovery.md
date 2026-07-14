# SSDP Discovery

SSDP is UPnP discovery over UDP multicast. The package splits this into
search, advertisement, and combined listener modules.

## One-Shot Search

```python
from async_upnp_client.search import async_search


async def on_response(headers):
    print(headers.get("LOCATION"), headers.get("ST"), headers.get("_udn"))


await async_search(async_callback=on_response)
```

Use `SsdpSearchListener` when you need to control lifecycle or target address.

## Long-Running Listener

```python
from async_upnp_client.ssdp_listener import SsdpListener


async def on_alive(headers):
    ...


listener = SsdpListener(on_alive=on_alive, on_byebye=..., on_update=...)
await listener.async_start()
try:
    await listener.async_search()
finally:
    await listener.async_stop()
```

`SsdpListener` combines advertisements and search responses and tracks devices.

## SsdpDevice

Important fields/properties:

- `udn`
- `locations`
- `location`
- `valid_to`
- `last_seen`
- `search_headers`
- `advertisement_headers`
- `userdata`
- `combined_headers(device_or_service_type)`
- `all_combined_headers`

The tracker purges expired locations based on `CACHE-CONTROL: max-age=...`.

## Headers

Useful SSDP headers:

- `LOCATION`: device description URL.
- `ST`: search target.
- `USN`: unique service name.
- `NT`: notification type.
- `NTS`: `ssdp:alive`, `ssdp:byebye`, or `ssdp:update`.
- `_udn`, `_timestamp`, `_host`, `_port`, `_source`: parsed helper fields.

Treat headers case-insensitively. Use `CaseInsensitiveDict` helpers instead of
manual `.lower()` maps.

## Validity Filtering

The listener validates locations. It ignores unusable locations such as
loopback, localhost, link-local, missing `_udn`, or missing type headers.

## IPv6

IPv6 is supported, but multicast over IPv6 requires a `scope_id`/interface id.
Use `AddressTupleVXType` shapes:

```python
("239.255.255.250", 1900)          # IPv4
("ff02::c", 1900, 0, scope_id)     # IPv6
```

Find scope ids via `ifaddr`, Linux `ip address`, Windows `ipconfig /all`, or
macOS `ifconfig`.
