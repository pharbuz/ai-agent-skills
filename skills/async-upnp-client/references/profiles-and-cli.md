# Profiles And CLI

Profiles wrap common UPnP service sets into domain-specific APIs.

## IGD

```python
from async_upnp_client.profiles.igd import IgdDevice

igd = IgdDevice(device, event_handler=None)
external_ip = await igd.async_get_external_ip_address()
status = await igd.async_get_status_info()
```

Capabilities include:

- external IP and connection status
- total bytes/packets sent/received
- common link properties
- generic/specific port mapping lookup
- add/delete port mapping
- IPv6 firewall pinholes
- NAT/RSIP status
- default connection service
- traffic/status polling

Named tuple models include `CommonLinkProperties`, `ConnectionTypeInfo`,
`StatusInfo`, `NatRsipStatusInfo`, `PortMappingEntry`, `FirewallStatus`,
`Pinhole`, `TrafficCounterState`, and `IgdState`.

## DLNA

```python
from async_upnp_client.profiles.dlna import DmrDevice, DmsDevice, PlayMode
```

`DmrDevice` supports renderer controls:

- update/ping/event handling
- transport state, play/pause/stop/next/previous
- seek absolute/relative time
- set current/next transport URI
- volume/mute/brightness/contrast/sharpness/color temperature
- presets and play mode
- current media metadata: title, artist, album, image, duration, position

`DmsDevice` supports media server data:

- search capabilities
- sort capabilities
- system update id
- URL normalization

DLNA enums include `TransportState`, `PlayMode`, `DlnaOrgOp`, `DlnaOrgCi`,
`DlnaOrgPs`, and `DlnaOrgFlags`.

## Printer

```python
from async_upnp_client.profiles.printer import PrinterDevice

attrs = await printer.async_get_printer_attributes()
```

## CLI

The package provides `upnp-client`.

Common commands:

```bash
upnp-client --pprint search
upnp-client --pprint advertisements
upnp-client --pprint call-action DESCRIPTION_URL SERVICE/ACTION Arg=value
upnp-client --pprint subscribe DESCRIPTION_URL '*'
upnp-client --debug-traffic --pprint call-action ...
```

The CLI emits one JSON line per action call or subscription event. Use it to
inspect devices before encoding assumptions in application code.
