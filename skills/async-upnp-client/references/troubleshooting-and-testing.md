# Troubleshooting And Testing

## Common Exceptions

Import from `async_upnp_client.exceptions`:

- `UpnpError`: base library error.
- `UpnpResponseError`: HTTP response failure.
- `UpnpActionError`: SOAP action/fault failure.
- `UpnpActionResponseError`: invalid action response.
- `UpnpValueError`: invalid/coercion failure for UPnP values.
- `UpnpXmlParseError`: malformed XML.
- `UpnpXmlContentError`: XML parsed but required content is missing/invalid.

## Discovery Problems

- SSDP uses UDP multicast `239.255.255.250:1900` for IPv4.
- Firewalls, Docker, VPNs, VLANs, and Wi-Fi isolation often block discovery.
- Some devices answer only on one interface; bind to the right source/target.
- IPv6 multicast requires a scope id/interface id.
- Device `LOCATION` URLs can be stale, private, loopback, or link-local.

## Description/SCPD Problems

- Use `non_strict=True` for devices with broken XML, bad data types, or missing
  expected elements.
- Use factory hooks to normalize malformed responses in a contained way.
- Log `device.device_info`, `service.service_info`, actions, and state variables
  before guessing action arguments.

## Action Problems

- Validate exact argument names and casing with `action.arguments`.
- Check `direction`: only `in` arguments are passed to calls.
- UPnP booleans are often represented as `1`/`0` or `true`/`false`; let
  `UpnpStateVariable` coerce values.
- SOAP faults may indicate unsupported actions, invalid instance IDs, wrong
  channel names, or missing profile support.

## Eventing Problems

- The device must be able to reach your callback URL.
- NAT, containers, and wrong bind address can make a local notify server
  unreachable.
- Resubscribe before timeout for long-running subscriptions.
- Always unsubscribe on shutdown to avoid stale subscriptions on devices.

## Test Strategy

- Unit-test XML parsing, action request creation, and response parsing with
  fixtures.
- Mock `UpnpRequester.async_http_request()` for deterministic SOAP tests.
- Mark live SSDP and device tests as integration tests.
- Use the `upnp-client --debug-traffic` CLI output to capture real device
  behavior before writing regression tests.
- Keep timeouts short in tests and stop listeners/notify servers in `finally`.
