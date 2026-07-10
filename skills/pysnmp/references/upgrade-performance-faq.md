# Upgrade, Performance, FAQ Content

Use this file for migration work, slow polling, protocol failures, and common
FAQ symptoms from the v7.1 docs.

## Upgrade To 6.x/7.x

- Remove old `-lextudio` package names; migrate to official `pysnmp` packages.
- 5.1.0 was a transition release for 4.x users and is not Python 3.12
  compatible. Do not target it for new work.
- 6.0 removed asyncore dependency and added an asyncio-based sync API for
  migration, but that sync API was removed in 6.2 because it was not stable
  enough.
- 7.0 applied PEP 8 cleanup: many fields/methods were renamed, many types moved
  under `v3arch`, and new v1arch types were introduced for simpler v1/v2c work.
- 7.1 changed transport construction for async DNS:
  `UdpTransportTarget(...)` became `await UdpTransportTarget.create(...)`.
- 7.1 revised `next_cmd`, `bulk_cmd`, `walk_cmd`, and `bulk_walk_cmd` parameters
  and return behavior.
- Old names may still work through compatibility layers, but docs warn that
  compatibility is deprecated and should not be relied on for future majors.

Migration rule: inspect imports, run tests against real/demo agents, and avoid
blind global renames.

## Built-In Debugging

Enable subsystem debug logs at app startup:

```python
from pysnmp import debug

debug.set_logger(debug.Debug("dsp", "msgproc", "secmod"))
# or full debug:
debug.set_logger(debug.Debug("all"))
```

Useful flags include `io`, `dsp`, `msgproc`, `secmod`, `mibbuild`, `mibview`,
`mibinstrum`, `acl`, `proxy`, and `app`. Use full debugging only briefly; it is
verbose and may expose sensitive data.

Packet-level tools recommended by docs: Wireshark, tcpdump, and Net-SNMP CLI
tools for comparing agent behavior.

## Performance Tuning

- Disable MIB support when the app can use numeric OIDs and raw values; MIB
  metadata loading is expensive.
- Run production benchmarks with `python -O`.
- Choose the right HLAPI: v1arch is fastest for SNMPv1/SNMPv2c-only workloads;
  v3arch is required for SNMPv3 and full security/access-control behavior.
- Use GETBULK/BULKWALK for large SNMPv2c/SNMPv3 tables.
- Reuse one engine inside one event loop for related polling; bound concurrency
  with `asyncio.Semaphore`.
- Avoid `prettyPrint()` inside hot loops unless text output is needed.

## FAQ Symptom Fixes

- **Ignored packets/timeouts for some OIDs**: some agents encode BER integers
  incorrectly, especially counters that decode as negative. Confirm with packet
  capture/Net-SNMP. Prefer vendor fix; hacks are type-specific and unsafe for
  normal signed integers.
- **Garbled values in apps**: use `prettyPrint()` on PyASN1 values. `str(...)`
  can show binary bytes for types such as `IpAddress` or `OctetString`.
- **Garbled values in tools**: use tool options for hex/text rendering and load
  relevant MIBs so display hints can be applied.
- **OID not increasing**: agent returned an OID not greater than requested,
  which can create infinite GETNEXT/GETBULK loops. Use
  `ignoreNonIncreasingOid=True` only when you also have a reliable stop
  condition.
- **Custom MIBs in manager**: configure MIB compiler/sources for local dirs or
  remote repositories, or precompile MIBs with PySMI `mibdump` and add the
  compiled directory to the MIB builder.
- **Reuse SnmpEngine across threads**: do not share one engine across multiple
  `asyncio.run()` event loops. Preferred pattern is one engine in one event loop
  with `asyncio.gather`; otherwise use one engine per thread and detach/close
  dispatcher before the loop is destroyed.
- **Listen on multiple interfaces**: register multiple socket transports with
  distinct transport domain suffixes on the same engine.
- **Peer information in receivers**: SNMP identity should be based on community
  or SNMPv3 context/security, not transport address. If transport details are
  still needed, retrieve them from the message dispatcher using state reference.
- **Constraints verification errors**: SET values and response values can be
  validated against MIB constraints when MIB lookup is enabled; violations raise
  exceptions and usually indicate wrong type/value or bad agent data.
- **Agent-side MIB objects**: create `MibScalarInstance` objects, clone syntax
  with current values, export them through the engine's MIB builder, and update
  instance syntax when backing data changes.
