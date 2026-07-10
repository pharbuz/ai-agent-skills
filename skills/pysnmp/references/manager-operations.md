# Manager Operations

Use `pysnmp.hlapi.v3arch.asyncio` for new code. All examples assume:

```python
from pysnmp.hlapi.v3arch.asyncio import *
```

Prefer explicit imports in production modules.

## Error Handling

Every manager command returns:

```python
error_indication, error_status, error_index, var_binds = result
```

For bulk operations the last value may be `var_bind_table`.

```python
if error_indication:
    raise RuntimeError(str(error_indication))
if error_status:
    failing_oid = error_index and var_binds[int(error_index) - 1][0] or "?"
    raise RuntimeError(f"{error_status.prettyPrint()} at {failing_oid}")
```

Print or convert values with `prettyPrint()` at application boundaries. Keep raw
PySNMP values when further SNMP operations need ASN.1 types.

## GET

```python
snmp_engine = SnmpEngine()
try:
    result = await get_cmd(
        snmp_engine,
        CommunityData("public"),
        await UdpTransportTarget.create(("router.example", 161)),
        ContextData(),
        ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)),
    )
finally:
    snmp_engine.close_dispatcher()
```

## SET

```python
result = await set_cmd(
    snmp_engine,
    CommunityData("private"),
    await UdpTransportTarget.create((host, 161)),
    ContextData(),
    ObjectType(ObjectIdentity("SNMPv2-MIB", "sysName", 0), OctetString("edge-1")),
)
```

Choose value classes intentionally: `Integer`, `Integer32`, `OctetString`,
`ObjectIdentifier`, `IpAddress`, `Counter32`, `Counter64`, `Gauge32`, `TimeTicks`.

## GETNEXT

Use for one lexical step past an OID.

```python
result = await next_cmd(
    snmp_engine,
    CommunityData("public"),
    await UdpTransportTarget.create((host, 161)),
    ContextData(),
    ObjectType(ObjectIdentity("SNMPv2-MIB", "system")),
)
```

## GETBULK

Use for efficient SNMPv2c/SNMPv3 table retrieval. Do not use with SNMPv1.

```python
result = await bulk_cmd(
    snmp_engine,
    UsmUserData("usr-none-none"),
    await UdpTransportTarget.create((host, 161)),
    ContextData(),
    0,   # non-repeaters
    50,  # max-repetitions
    ObjectType(ObjectIdentity("SNMPv2-MIB", "system")),
)
```

## Manual Bulk Walk

```python
var_binds = [ObjectType(ObjectIdentity("SNMPv2-MIB", "system"))]
while True:
    error_indication, error_status, error_index, var_bind_table = await bulk_cmd(
        snmp_engine,
        CommunityData("public"),
        await UdpTransportTarget.create((host, 161)),
        ContextData(),
        0,
        50,
        *var_binds,
    )
    if error_indication or error_status:
        break
    for var_bind in var_bind_table:
        print(" = ".join(x.prettyPrint() for x in var_bind))
    var_binds = var_bind_table
    if is_end_of_mib(var_binds):
        break
```

## Convenience Walks

Use `walk_cmd(...)` for GETNEXT-based walks and `bulk_walk_cmd(...)` for
GETBULK-based walks. Keep explicit loop guards when walking untrusted agents or
large subtrees.

## Concurrency

Run independent commands with `asyncio.gather`. Reuse one `SnmpEngine` inside a
single event loop for related queries, but do not share it casually across
threads. If thread reuse is required, consult the PySNMP FAQ first.
