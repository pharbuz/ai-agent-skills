# API Reference Content

PySNMP v7.1 exposes layered APIs. Use this file for operation semantics and
selection rules; inspect installed package types when exact signatures matter.

## API Layers

- **HLAPI v3arch asyncio**: default for new code. Supports SNMPv1, SNMPv2c, and
  SNMPv3 through the full SNMPv3 architecture. Uses `SnmpEngine`, security data,
  transport target, `ContextData`, and one or more `ObjectType` values.
- **HLAPI v1arch asyncio**: simpler/faster path for SNMPv1/SNMPv2c only. It
  avoids v3arch machinery and uses a dispatcher-oriented model.
- **Low-level v3arch/v1arch**: use for command responders, notification
  receivers, custom agents, multiple transports, VACM/USM setup, and packet-level
  control.
- **SMI/MIB services**: use for symbolic MIB resolution, browsing MIB trees, and
  implementing agent-side MIB objects.

## Common HLAPI Inputs

- `SnmpEngine()`: stateful v3arch engine. Close with `close_dispatcher()` or use
  context-manager patterns where supported.
- `CommunityData("public")`: SNMPv2c; add `mpModel=0` for SNMPv1.
- `UsmUserData(user, authKey=..., privKey=..., authProtocol=..., privProtocol=...)`:
  SNMPv3 USM credentials.
- `await UdpTransportTarget.create((host, 161), timeout=1, retries=5)`: IPv4 UDP
  target. Use `Udp6TransportTarget` for IPv6. v7.1 requires async creation.
- `ContextData()`: default context; use `contextName=...` for multi-context
  agents/VRFs.
- `ObjectType(ObjectIdentity(...))`: variable binding. Scalars normally need
  instance index `0`.

## Operation Return Shape

Manager and notification calls return four fields:

```python
error_indication, error_status, error_index, var_binds = result
```

`GETBULK`/walk variants may return a var-bind table. Always handle:

- `error_indication`: local/transport/security/protocol failure.
- `error_status`: remote agent error such as noAccess, notWritable, noSuchName.
- `error_index`: 1-based index of failing var-bind when available.
- `var_binds`: returned OID/value pairs; call `prettyPrint()` for presentation.

## GET Operation

Use `get_cmd()` to read known scalar or table instances. Pass one or many
`ObjectType` objects; the response preserves request order. Scalars usually use
`ObjectIdentity("MIB", "symbol", 0)` or numeric `1.3...0`.

## SET Operation

Use `set_cmd()` for configuration writes. Each `ObjectType` includes a value:

```python
ObjectType(ObjectIdentity("SNMPv2-MIB", "sysName", 0), OctetString("edge-1"))
```

SET failures are often access-control or type/constraint issues, not Python
bugs. Verify write credentials, VACM/view, OID instance, and ASN.1 type.

## GETNEXT Operation

Use `next_cmd()` to retrieve the lexicographically next OID. It is the primitive
behind walks and works when the caller does not know exact table instances.
Guard against agents that return non-increasing OIDs.

## GETBULK Operation

Use `bulk_cmd()` for SNMPv2c/SNMPv3 table retrieval. Arguments include
`non_repeaters` and `max_repetitions`; `0, 25` or `0, 50` are common starts.
Do not use GETBULK for SNMPv1.

## WALK Operation

Use `walk_cmd()` for GETNEXT-based subtree traversal. Stop at end-of-MIB or when
the returned OID leaves the requested subtree. For broken agents, the FAQ
documents `ignoreNonIncreasingOid=True`, but use it only with a separate stop
condition.

## BULK WALK Operation

Use `bulk_walk_cmd()` for efficient SNMPv2c/SNMPv3 subtree traversal. Prefer it
for large tables when devices support GETBULK. Tune `max_repetitions` to balance
packet size, latency, and device behavior.

## TRAP/INFORM Operation

Use `send_notification()` with `NotificationType(ObjectIdentity(...))`.

- `"trap"`: one-way notification, no acknowledgement.
- `"inform"`: acknowledged notification; response var-binds are returned.
- `NotificationType(..., instanceIndex=(...))` expands table-indexed objects.
- `.add_varbinds(...)` supplies extra or explicit notification payload values.
- SNMPv3 TRAPs require sender engine ID and receiver-side user/VACM setup to be
  known before unsolicited messages arrive.

## v1arch vs v3arch

Both expose GET, SET, GETNEXT, GETBULK, WALK, BULK WALK, and TRAP/INFORM pages.
Choose v3arch unless the app is strictly SNMPv1/v2c and performance/resource
cost is the main constraint. v1arch does not cover SNMPv3 USM/VACM behavior.
