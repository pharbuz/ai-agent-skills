# Browsing And Resolution

Use `ServiceBrowser` to watch for service instances of one or more DNS-SD
types.

## Imports

```python
from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf
```

## Handler Callback

```python
def on_change(zeroconf, service_type, name, state_change):
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            print(name, info.parsed_scoped_addresses(), info.port)
```

Create and later cancel the browser:

```python
zc = Zeroconf()
browser = ServiceBrowser(zc, "_http._tcp.local.", handlers=[on_change])
...
browser.cancel()
zc.close()
```

Keep the `browser` object alive. Dropping the object without cancellation can
leave work running until cleanup.

## Listener Object

Listener objects can provide service callbacks. Installed versions may expose
`ServiceListener`; otherwise any object with the expected methods works:

```python
class Listener:
    def add_service(self, zeroconf, service_type, name):
        ...

    def update_service(self, zeroconf, service_type, name):
        ...

    def remove_service(self, zeroconf, service_type, name):
        ...
```

Pass it with `listeners=[listener]` depending on the constructor signature in
the installed version.

## ServiceStateChange

Use identity comparisons:

```python
if state_change is ServiceStateChange.Added:
    ...
elif state_change is ServiceStateChange.Updated:
    ...
elif state_change is ServiceStateChange.Removed:
    ...
```

On `Removed`, `get_service_info()` may already return `None` or stale cached
data; treat the event as authoritative for removal.

## Service Type Discovery

```python
from zeroconf import ZeroconfServiceTypes

types = ZeroconfServiceTypes.find(timeout=3)
```

`ZeroconfServiceTypes` supports `find`, `add_service`, `remove_service`, and
`update_service`.

## Low-Level Record Updates

`RecordUpdateListener` exposes:

- `update_record(zc, now, record)`: legacy/sync record update callback.
- `async_update_records(zc, now, records)`: async batch callback.
- `async_update_records_complete()`: called after batch processing.

Use it for DNS-record-aware logic, not normal service browsing.
