# Networking And Troubleshooting

## Interfaces And IP Versions

Use explicit interface/IP choices when hosts have multiple NICs, VPNs,
containers, or IPv6 quirks.

```python
from zeroconf import InterfaceChoice, IPVersion, Zeroconf

zc = Zeroconf(
    interfaces=InterfaceChoice.All,
    ip_version=IPVersion.All,
)
```

Common choices:

- `InterfaceChoice.Default`: default interfaces.
- `InterfaceChoice.All`: all detected interfaces.
- `IPVersion.V4Only`: IPv4 mDNS only.
- `IPVersion.V6Only`: IPv6 mDNS only.
- `IPVersion.All`: both stacks.

Installed versions may accept a list of interface addresses in `interfaces`.
Use that when binding to a specific NIC is required.

## Multicast Environment

mDNS uses UDP multicast on port 5353. Check:

- local firewall allows UDP 5353,
- network allows multicast,
- Docker/VM/VPN routing does not hide the target interface,
- Wi-Fi client isolation is disabled when discovering LAN devices,
- service type matches exactly, including trailing dot.

## Name And Type Problems

- `BadTypeInNameException`: `ServiceInfo.name` does not contain the service
  type or the type is malformed.
- `NamePartTooLongException`: a DNS label is longer than allowed.
- `NonUniqueNameException`: another responder already owns the name.
- `ServiceNameAlreadyRegistered`: local process already registered the name.

Use unique names in tests, e.g. include process id or UUID.

## Lifecycle Problems

- `NotRunningException`: operation happened after `close()` or before start.
- Hanging tests: browser not canceled or Zeroconf not closed.
- Stale data: service removed but cache has old records; trust remove events
  and request fresh details for add/update.
- Missing details in browser callback: call `get_service_info()` or async
  equivalent with a timeout.

## TXT Properties

TXT values are bytes on the wire. Use:

```python
info.properties
info.decoded_properties
```

Do not assume arbitrary bytes decode as UTF-8. Use `decoded_properties` only for
human-readable properties.

## Test Strategy

- Mark live mDNS tests as integration tests.
- Use short timeouts and unique service names.
- Always unregister and close in `finally`.
- Skip live tests on CI runners that block multicast.
- For unit tests, isolate `ServiceInfo` construction, property encoding, and
  callback behavior without relying on network discovery.
