---
name: async-upnp-client
description: >-
  Build, debug, or refactor asyncio UPnP, SSDP, DLNA, IGD, printer, and UPnP
  eventing code with `async_upnp_client`. Trigger WHENEVER the user installs or
  imports `async_upnp_client`; uses `UpnpFactory`, `UpnpDevice`, `UpnpService`,
  `UpnpAction`, `UpnpStateVariable`, `UpnpRequester`, `AiohttpRequester`,
  `AiohttpSessionRequester`, `SsdpSearchListener`, `SsdpAdvertisementListener`,
  `SsdpListener`, `SsdpDevice`, `UpnpEventHandler`, `AiohttpNotifyServer`,
  IGD profile `IgdDevice`, DLNA `DmrDevice`/`DmsDevice`, printer profile,
  `upnp-client` CLI, SOAP action calls, SCPD/device description parsing, SSDP
  search/advertisements, subscriptions, state variable events, IPv6 scope IDs,
  non-strict parsing, or fixes UPnP XML errors, action validation failures,
  SOAP faults, callback URLs, event resubscribe failures, multicast discovery,
  bad LOCATION headers, unavailable devices, and aiohttp session lifecycle.
---

# async_upnp_client

Use this skill for Python asyncio UPnP work with the `async_upnp_client`
package. PyPI and the repository README showed `async-upnp-client 0.47.0` on
2026-07-14; it requires Python `>=3.10`.

```bash
python -m pip show async-upnp-client
python - <<'PY'
import async_upnp_client
print(getattr(async_upnp_client, "__version__", "unknown"))
PY
```

## Choose The API

- Use `UpnpFactory` plus an `UpnpRequester` implementation to create a
  `UpnpDevice` from a device description URL.
- Use `AiohttpRequester` or `AiohttpSessionRequester` for normal HTTP/SOAP
  client calls.
- Use `SsdpSearchListener` or `async_search()` for one-shot SSDP discovery.
- Use `SsdpListener` for long-running combined search + advertisement tracking.
- Use `UpnpEventHandler` with `AiohttpNotifyServer` to subscribe to UPnP event
  notifications.
- Use profile wrappers for standard domains: `IgdDevice`, `DmrDevice`,
  `DmsDevice`, and `PrinterDevice`.

## Default Workflow

1. Identify the target: raw UPnP device/service/action, SSDP discovery,
   eventing, IGD, DLNA DMR/DMS, printer, or CLI.
2. Check package version and whether `aiohttp` is already used by the app.
3. Discover devices via SSDP or accept a known description URL.
4. Create `UpnpDevice` with `UpnpFactory.async_create_device(description_url)`.
5. Locate service/action by service type, service id, or profile helper.
6. Validate action argument names and types against `UpnpAction.arguments` and
   `UpnpStateVariable` metadata before calling.
7. Always close aiohttp sessions/requesters, stop SSDP listeners, and unsubscribe
   event handlers during shutdown.
8. For IPv6 SSDP or callback URLs, include the correct scope/interface id.

## Minimal Device Action

```python
from async_upnp_client.aiohttp import AiohttpRequester
from async_upnp_client.client_factory import UpnpFactory


async def get_device(description_url: str):
    requester = AiohttpRequester(timeout=10)
    factory = UpnpFactory(requester, non_strict=True)
    device = await factory.async_create_device(description_url)
    return device


async def call_action(description_url: str) -> None:
    device = await get_device(description_url)
    service = device.service_id("urn:upnp-org:serviceId:RenderingControl")
    if not service:
        return
    result = await service.async_call_action(
        "GetVolume",
        InstanceID=0,
        Channel="Master",
    )
    print(result["CurrentVolume"])
```

## Minimal SSDP Search

```python
from async_upnp_client.search import async_search


async def on_response(headers):
    print(headers.get("LOCATION"), headers.get("ST"), headers.get("_udn"))


await async_search(async_callback=on_response)
```

## Decision Rules

- Prefer `service.async_call_action("ActionName", **kwargs)` for application
  code; use `service.action(name)` when inspecting metadata or validation.
- Use `non_strict=True` for consumer devices with imperfect XML only after
  logging/understanding the parse issue.
- Treat SSDP headers as case-insensitive; use the library's
  `CaseInsensitiveDict` helpers when available.
- Never trust SSDP `LOCATION` blindly; the listener filters loopback,
  link-local, localhost, and invalid URLs.
- For long-running discovery, use `SsdpListener` rather than repeated one-shot
  search loops.
- For eventing, run a reachable notify server and unsubscribe on shutdown.
- For Home Assistant-style apps, reuse existing aiohttp sessions via
  `AiohttpSessionRequester`.

## References

- Read [references/public-models-and-imports.md](references/public-models-and-imports.md)
  for public classes, import paths, and what each model contains.
- Read [references/client-actions-and-models.md](references/client-actions-and-models.md)
  for `UpnpFactory`, devices, services, actions, state variables, SOAP calls,
  and parse hooks.
- Read [references/ssdp-discovery.md](references/ssdp-discovery.md) for
  search, advertisements, `SsdpListener`, `SsdpDevice`, headers, and IPv6.
- Read [references/eventing-and-aiohttp.md](references/eventing-and-aiohttp.md)
  for subscriptions, notify servers, callback URLs, resubscribe/unsubscribe,
  and aiohttp requesters.
- Read [references/profiles-and-cli.md](references/profiles-and-cli.md) for
  IGD, DLNA DMR/DMS, printer helpers, and `upnp-client` CLI usage.
- Read [references/troubleshooting-and-testing.md](references/troubleshooting-and-testing.md)
  for exceptions, malformed devices, multicast, XML, SOAP faults, and tests.
- Read [references/examples.md](references/examples.md) for complete code
  patterns in Markdown form.
