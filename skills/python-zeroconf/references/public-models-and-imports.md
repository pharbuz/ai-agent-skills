# Public Models And Imports

The package name is `zeroconf`, while this skill is named `python-zeroconf` to
match the project/docs name.

## Core Sync API

| Model | Import | Represents / contains |
|---|---|---|
| `Zeroconf` | `from zeroconf import Zeroconf` | mDNS engine, sockets, cache, listeners, service registration, query/send APIs. |
| `ServiceInfo` | `from zeroconf import ServiceInfo` | DNS-SD service instance: type, name, server, addresses, port, TXT properties, TTLs. |
| `ServiceBrowser` | `from zeroconf import ServiceBrowser` | Background browser for one or more service types; emits add/update/remove events. |
| `ZeroconfServiceTypes` | `from zeroconf import ZeroconfServiceTypes` | Discovers advertised DNS-SD service types via `_services._dns-sd._udp.local.`. |
| `RecordUpdateListener` | `from zeroconf import RecordUpdateListener` | Low-level DNS record update callback interface. |
| `ServiceListener` | `from zeroconf import ServiceListener` | Listener protocol/class for browser service events when available in installed version. |

## Async API

| Model | Import | Represents / contains |
|---|---|---|
| `AsyncZeroconf` | `from zeroconf.asyncio import AsyncZeroconf` | Async wrapper around a `Zeroconf` instance with async register/get/update/close methods. |
| `AsyncServiceInfo` | `from zeroconf.asyncio import AsyncServiceInfo` | Async-capable service info resolution and cache update model. |
| `AsyncServiceBrowser` | `from zeroconf.asyncio import AsyncServiceBrowser` | Async browser with `async_cancel()`. |
| `AsyncZeroconfServiceTypes` | `from zeroconf.asyncio import AsyncZeroconfServiceTypes` | Async service type discovery via `async_find()`. |

## Enums And Constants

| Model | Import | Values / use |
|---|---|---|
| `ServiceStateChange` | `from zeroconf import ServiceStateChange` | Service browser event values: Added, Removed, Updated. |
| `InterfaceChoice` | `from zeroconf import InterfaceChoice` | Interface selection values such as All or Default. |
| `IPVersion` | `from zeroconf import IPVersion` | IP protocol selection: V4Only, V6Only, All. |
| `DNSQuestionType` | `from zeroconf import DNSQuestionType` | mDNS question type: `QM` multicast question, `QU` unicast response requested. |

## Exceptions

| Exception | Import | Typical cause |
|---|---|---|
| `Error` | `from zeroconf import Error` | Base zeroconf exception. |
| `NonUniqueNameException` | `from zeroconf import NonUniqueNameException` | Service registration name conflict. |
| `ServiceNameAlreadyRegistered` | `from zeroconf import ServiceNameAlreadyRegistered` | Same service name already registered locally. |
| `BadTypeInNameException` | `from zeroconf import BadTypeInNameException` | Service name/type mismatch. |
| `NamePartTooLongException` | `from zeroconf import NamePartTooLongException` | DNS label exceeds max label length. |
| `NotRunningException` | `from zeroconf import NotRunningException` | Operation on stopped/not running Zeroconf engine. |
| `EventLoopBlocked` | `from zeroconf import EventLoopBlocked` | Event loop blocked long enough to affect async operation. |
| `IncomingDecodeError` | `from zeroconf import IncomingDecodeError` | Malformed incoming DNS packet. |
| `AbstractMethodException` | `from zeroconf import AbstractMethodException` | Listener base method not implemented. |

## Utility

```python
from zeroconf import current_time_millis
```

Use it only when matching library internals or timestamps in tests; prefer
standard `time` APIs in application logic.
