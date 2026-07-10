---
name: pysnmp
description: >-
  Build, configure, debug, or migrate Python SNMP code with PySNMP v7.1.
  Trigger WHENEVER the user installs or imports `pysnmp`; uses
  `pysnmp.hlapi.v3arch.asyncio`, `SnmpEngine`, `CommunityData`, `UsmUserData`,
  `UdpTransportTarget`, `Udp6TransportTarget`, `ContextData`, `ObjectIdentity`,
  `ObjectType`, `get_cmd`, `set_cmd`, `next_cmd`, `bulk_cmd`, `walk_cmd`,
  `bulk_walk_cmd`, `send_notification`, MIB loading, SNMPv1/v2c/v3 credentials,
  SNMP manager GET/SET/WALK/BULKWALK operations, TRAP/INFORM sending or
  receiving, asyncio integration, v1arch/v3arch HLAPI, low-level v1arch/v3arch
  examples, SMI/MIB object browsing or implementation, troubleshooting,
  performance tuning, downloads, changelog, license, FAQ, support options, or
  fixes PySNMP 4/5/6-to-7 migration issues, camelCase-to-snake_case breakage,
  transport creation errors, MIB resolution failures, timeouts, garbled values,
  ignored packets, non-increasing OIDs, or SnmpEngine lifecycle problems.
---

# PySNMP

Use this skill for PySNMP 7.1 work. Prefer the high-level asyncio API
`pysnmp.hlapi.v3arch.asyncio` for new manager/notification code, but consult
the low-level v1arch/v3arch examples when building agents, notification
receivers, packet-level tools, or SMI/MIB integrations. The v7.1 docs identify
the library as PySNMP 7.1.27; use Python 3.10+ unless the target project proves
otherwise.

## Default Workflow

1. Inspect installed `pysnmp` version and existing import style before editing.
2. Decide the API layer: HLAPI v3arch for most work, HLAPI v1arch for
   performance-sensitive SNMPv1/v2c only, low-level APIs for agents/receivers or
   packet-level control, SMI APIs for MIB browsing/implementation.
3. Prefer `from pysnmp.hlapi.v3arch.asyncio import ...` for new HLAPI code.
4. Create one `SnmpEngine()` per logical client/app scope; close it with
   `snmp_engine.close_dispatcher()` when done.
5. Await transport creation: `await UdpTransportTarget.create((host, port))`.
6. Pass `ContextData()` before object/notification arguments.
7. Always handle `errorIndication`, `errorStatus`, `errorIndex`, and var-binds.
8. Use SNMPv2c by default for community polling unless the target requires v1
   (`CommunityData("public", mpModel=0)`) or SNMPv3 (`UsmUserData(...)`).
9. For walks, stop on `is_end_of_mib(...)` or use `walk_cmd`/`bulk_walk_cmd`
   helpers when suitable.

## Minimal GET Pattern

```python
import asyncio
from pysnmp.hlapi.v3arch.asyncio import (
    CommunityData,
    ContextData,
    ObjectIdentity,
    ObjectType,
    SnmpEngine,
    UdpTransportTarget,
    get_cmd,
)


async def get_sysdescr(host: str, community: str = "public") -> None:
    snmp_engine = SnmpEngine()
    try:
        result = await get_cmd(
            snmp_engine,
            CommunityData(community),  # SNMPv2c; use mpModel=0 for SNMPv1.
            await UdpTransportTarget.create((host, 161), timeout=1, retries=3),
            ContextData(),
            ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)),
        )

        error_indication, error_status, error_index, var_binds = result
        if error_indication:
            raise RuntimeError(str(error_indication))
        if error_status:
            failing_oid = error_index and var_binds[int(error_index) - 1][0] or "?"
            raise RuntimeError(f"{error_status.prettyPrint()} at {failing_oid}")

        for oid, value in var_binds:
            print(f"{oid.prettyPrint()} = {value.prettyPrint()}")
    finally:
        snmp_engine.close_dispatcher()


asyncio.run(get_sysdescr("demo.pysnmp.com"))
```

## Decision Rules

- Use v3arch HLAPI for both community-based and SNMPv3 USM operations.
- Use explicit imports in application code; wildcard imports are acceptable only
  in small examples.
- Use `CommunityData(name)` for SNMPv2c, `CommunityData(name, mpModel=0)` for
  SNMPv1, and `UsmUserData(...)` for SNMPv3.
- Use `ObjectIdentity("MIB", "symbol", index)` when MIBs are available; use
  dotted OIDs when MIB resolution is unavailable or not needed.
- Use `ObjectType(..., value)` for SET values and choose PySNMP ASN.1 value
  classes intentionally (`Integer`, `OctetString`, `Gauge32`, etc.).
- Use `Udp6TransportTarget` for IPv6 and `set_local_address(...)` when binding a
  local interface matters.
- Do not mix old camelCase PySNMP examples with v7.1 snake_case APIs.

## References

- Read [references/api-reference-index.md](references/api-reference-index.md)
  for v7.1 API reference content: API layers, shared inputs, return shape, and
  both v3arch/v1arch GET/SET/GETNEXT/GETBULK/WALK/BULK WALK/TRAP/INFORM
  semantics.
- Read [references/manager-operations.md](references/manager-operations.md)
  for GET, SET, GETNEXT, GETBULK, WALK, BULKWALK, and error handling.
- Read [references/credentials-transports-mibs.md](references/credentials-transports-mibs.md)
  for SNMP versions, USM auth/privacy, transports, MIBs, and value types.
- Read [references/notifications-agents-troubleshooting.md](references/notifications-agents-troubleshooting.md)
  for TRAP/INFORM, receivers/agents, migration notes, debugging, and common
  failure modes.
- Read [references/samples.md](references/samples.md) for the full v7.1 samples
  content: HLAPI v3arch/v1arch, low-level v3arch/v1arch,
  manager/agent/notification patterns, transport tweaks, and SMI examples.
- Read [references/sample-code-manifest.md](references/sample-code-manifest.md)
  to locate the bundled Python sample files copied under `assets/samples/`.
- Read [references/upgrade-performance-faq.md](references/upgrade-performance-faq.md)
  for Upgrade to 6.x/7.x, troubleshooting, performance tuning, FAQ topics, and
  concrete symptom fixes.
- Read [references/project-resources.md](references/project-resources.md) for
  downloads, dependencies, changelog usage, license handling, support options,
  further development, and related resources.
