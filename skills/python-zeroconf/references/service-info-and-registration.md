# ServiceInfo And Registration

`ServiceInfo` is the service instance model used for registration and
resolution.

## Import

```python
from zeroconf import ServiceInfo, Zeroconf
```

## Important Fields

- `type`: DNS-SD service type, e.g. `_http._tcp.local.`
- `name`: full service instance name, e.g. `Printer._ipp._tcp.local.`
- `server`: hostname target for SRV records; usually ends with `.local.`
- `addresses`: raw packed IPv4/IPv6 bytes.
- `port`, `weight`, `priority`: SRV data.
- `properties`: TXT properties as bytes/strings/None.
- `decoded_properties`: human-readable decoded TXT dict.
- `host_ttl`, `other_ttl`: TTLs for host records and other records.
- `interface_index`: IPv6 scoped interface index when relevant.
- `key`, `server_key`: normalized cache keys.

## Address Encoding

```python
import socket

ipv4 = socket.inet_aton("192.0.2.10")
ipv6 = socket.inet_pton(socket.AF_INET6, "2001:db8::10")
```

Read addresses with:

```python
info.parsed_addresses()
info.parsed_scoped_addresses()
info.addresses_by_version(...)
info.ip_addresses_by_version(...)
```

## Registration

```python
zc = Zeroconf()
info = ServiceInfo(
    "_http._tcp.local.",
    "Example._http._tcp.local.",
    addresses=[socket.inet_aton("192.0.2.10")],
    port=8080,
    properties={"path": "/"},
    server="example.local.",
)

try:
    zc.register_service(info, allow_name_change=False)
finally:
    zc.unregister_service(info)
    zc.close()
```

Use `allow_name_change=True` only when callers can tolerate the service name
changing to resolve conflicts.

## Updating

Change mutable fields on `ServiceInfo`, then call:

```python
zc.update_service(info)
```

Use update for TXT/property changes, port changes, address changes, or TTL
changes. Unregister/register may be clearer when changing identity fields such
as `type` or `name`.

## DNS Record Helpers

`ServiceInfo` can build records internally:

- `dns_pointer()`
- `dns_service()`
- `dns_text()`
- `dns_addresses()`
- `dns_nsec()`
- `get_address_and_nsec_records()`

Application code usually should not need these unless generating or testing
DNS packets directly.

## Resolution

```python
info = zc.get_service_info("_http._tcp.local.", "Example._http._tcp.local.")
if info:
    print(info.server, info.port, info.decoded_properties)
```

For existing `ServiceInfo` objects, `request(zc, timeout)` asks the network for
missing details. `load_from_cache(zc)` can populate from local cache.
