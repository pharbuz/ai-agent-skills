# Public Models And Imports

The package import is `async_upnp_client`.

## Client And Model API

| Model | Import | Represents / contains |
|---|---|---|
| `UpnpFactory` | `from async_upnp_client.client_factory import UpnpFactory` | Builds `UpnpDevice` trees from description/SCPD XML. |
| `UpnpRequester` | `from async_upnp_client.client import UpnpRequester` | Abstract async HTTP requester; implement `async_http_request()`. |
| `UpnpDevice` | `from async_upnp_client.client import UpnpDevice` | Device info, services, embedded devices, SSDP headers, availability. |
| `UpnpService` | `from async_upnp_client.client import UpnpService` | Service info, state variables, actions, event callback. |
| `UpnpAction` | `from async_upnp_client.client import UpnpAction` | SOAP action metadata, argument validation, request/response parsing. |
| `UpnpStateVariable` | `from async_upnp_client.client import UpnpStateVariable` | State variable metadata, Python/UPnP value conversion, constraints. |
| `AiohttpRequester` | `from async_upnp_client.aiohttp import AiohttpRequester` | Owns aiohttp client lifecycle for UPnP HTTP requests. |
| `AiohttpSessionRequester` | `from async_upnp_client.aiohttp import AiohttpSessionRequester` | Uses caller-provided aiohttp session. |

## SSDP And Eventing

| Model | Import | Represents / contains |
|---|---|---|
| `SsdpSearchListener` | `from async_upnp_client.search import SsdpSearchListener` | Sends M-SEARCH and receives search responses. |
| `async_search` | `from async_upnp_client.search import async_search` | Convenience one-shot SSDP search. |
| `SsdpAdvertisementListener` | `from async_upnp_client.advertisement import SsdpAdvertisementListener` | Receives SSDP alive/byebye/update advertisements. |
| `SsdpListener` | `from async_upnp_client.ssdp_listener import SsdpListener` | Combines search and advertisements into tracked devices. |
| `SsdpDevice` | `from async_upnp_client.ssdp_listener import SsdpDevice` | UDN, locations, search/advertisement headers, last_seen, validity. |
| `UpnpEventHandler` | `from async_upnp_client.event_handler import UpnpEventHandler` | SUBSCRIBE/UNSUBSCRIBE and NOTIFY handling for services. |
| `UpnpEventHandlerRegister` | `from async_upnp_client.event_handler import UpnpEventHandlerRegister` | Per-device event handler registry. |
| `AiohttpNotifyServer` | `from async_upnp_client.aiohttp import AiohttpNotifyServer` | aiohttp web server for UPnP NOTIFY callbacks. |

## Data Models

Import from `async_upnp_client.const`:

- `DeviceInfo`: device_type, friendly_name, manufacturer, model fields, udn,
  presentation_url, description url, icons, XML.
- `ServiceInfo`: service_id, service_type, control_url, event_sub_url, scpd_url,
  XML.
- `ActionInfo` / `ActionArgumentInfo`: action name and argument metadata.
- `StateVariableInfo` / `StateVariableTypeInfo`: state variable type,
  allowed values/ranges, default, XML.
- `HttpRequest` / `HttpResponse`: immutable request/response values for hooks
  and requesters.
- `NotificationSubType`, `SsdpSource`, `AddressTupleV4Type`,
  `AddressTupleV6Type`, `AddressTupleVXType`.

## Profiles

| Profile | Import | Use |
|---|---|---|
| `IgdDevice` | `from async_upnp_client.profiles.igd import IgdDevice` | Internet Gateway Device: WAN status, external IP, port mappings, traffic counters. |
| `DmrDevice` | `from async_upnp_client.profiles.dlna import DmrDevice` | DLNA Digital Media Renderer: playback, volume, metadata, transport. |
| `DmsDevice` | `from async_upnp_client.profiles.dlna import DmsDevice` | DLNA Digital Media Server: content directory capabilities. |
| `PrinterDevice` | `from async_upnp_client.profiles.printer import PrinterDevice` | UPnP printer attributes. |
