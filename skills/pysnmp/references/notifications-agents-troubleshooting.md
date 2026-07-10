# Notifications, Agents, Troubleshooting

## Sending TRAP/INFORM

Use `send_notification(...)` from `pysnmp.hlapi.v3arch.asyncio`.

```python
error_indication, error_status, error_index, var_binds = await send_notification(
    snmp_engine,
    CommunityData("public", mpModel=0),
    await UdpTransportTarget.create((host, 162)),
    ContextData(),
    "trap",
    NotificationType(ObjectIdentity("1.3.6.1.6.3.1.1.5.2"))
    .load_mibs("SNMPv2-MIB")
    .add_varbinds(
        ("1.3.6.1.6.3.1.1.4.3.0", "1.3.6.1.4.1.20408.4.1.1.2"),
        ("1.3.6.1.2.1.1.1.0", OctetString("my system")),
    ),
)
```

Use `"inform"` when the sender needs an acknowledgement. Use `"trap"` when no
response is expected.

## Receivers And Agents

PySNMP supports lower-level agent, command responder, and notification receiver
APIs. For these tasks:

- Read the existing code before changing architecture; low-level setup is more
  verbose and version-sensitive.
- Keep engine, transport, VACM, USM/community, and context setup together.
- Bind receiver sockets deliberately; UDP/162 may require elevated privileges.
- For custom MIB objects, isolate MIB instrumentation code from transport setup.

## Migration To v7.1

PySNMP v7 uses snake_case in many public APIs. Prefer v7 names in new code.

Common migrations:

- `getCmd` -> `get_cmd`
- `setCmd` -> `set_cmd`
- `nextCmd` -> `next_cmd`
- `bulkCmd` -> `bulk_cmd`
- `sendNotification` -> `send_notification`
- `UdpTransportTarget((host, port))` -> `await UdpTransportTarget.create((host, port))`
- `closeDispatcher()` -> `close_dispatcher()`
- `loadMibs(...)` -> `load_mibs(...)`
- `addVarBinds(...)` -> `add_varbinds(...)`

Do not mechanically rename without checking imports; older examples may use
different namespaces (`hlapi.asyncore`, sync APIs, or legacy camelCase names).

## Debugging

Use PySNMP built-in debug logging when protocol behavior is unclear. Keep it off
in normal production logs because it can expose sensitive data and generate high
volume.

Check these first:

- Target host/port, route, firewall, and UDP reachability.
- SNMP version and credential model (`mpModel=0` for v1, default v2c).
- Timeout/retry values relative to device latency.
- OID instance suffix: scalar objects usually need `.0`.
- MIB availability when using symbolic names.
- Device access controls: community views, VACM, source ACLs, engine ID, USM
  auth/privacy settings.

## Common Failures

- `TypeError` around transport construction: use
  `await UdpTransportTarget.create(...)` in v7 asyncio code.
- `No SNMP response received`: verify UDP/161 reachability, community/user,
  SNMP version, source ACLs, timeout/retries.
- `authorizationError` or `notWritable`: verify VACM/view and write permission.
- MIB lookup errors: use numeric OIDs or configure MIB sources and load MIBs.
- Walk never ends: check for non-increasing OIDs and stop on `is_end_of_mib`.
- Garbled values: verify MIB type, encoding expectations, and use
  `prettyPrint()` only for presentation.
- Event loop errors: do not call `asyncio.run()` from inside an already-running
  event loop; expose async functions to the caller instead.
- Resource leak warnings: close `SnmpEngine` with `close_dispatcher()` when the
  client lifecycle ends.

## Batch Polling Pattern

For many devices, collect per-device errors instead of failing the whole batch:

```python
results = await asyncio.gather(
    *(poll_device(host) for host in hosts),
    return_exceptions=True,
)
```

Throttle concurrency with `asyncio.Semaphore` if devices or local sockets are
overloaded. Use one event loop and avoid sharing an engine across threads unless
the PySNMP FAQ guidance is followed.
