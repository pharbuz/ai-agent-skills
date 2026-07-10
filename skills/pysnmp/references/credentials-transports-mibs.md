# Credentials, Transports, MIBs

## SNMP Versions

Community-based credentials:

```python
CommunityData("public")              # SNMPv2c, mpModel=1 default
CommunityData("public", mpModel=0)   # SNMPv1
```

SNMPv3 USM credentials:

```python
UsmUserData("usr-none-none")

UsmUserData(
    "usr-sha-aes",
    authKey="authenticationkey",
    privKey="encryptionkey",
    authProtocol=USM_AUTH_HMAC96_SHA,
    privProtocol=USM_PRIV_CFB128_AES,
)
```

Prefer SHA/AES protocols for new SNMPv3 deployments when the device supports
them. Keep legacy MD5/DES only for existing devices.

## Context

Most commands need `ContextData()`.

```python
ContextData()
ContextData(contextName="vrf-blue")
```

Use non-default context only when the SNMP agent exposes multiple contexts or
VRFs.

## Transports

PySNMP 7.1 asyncio transport targets are created asynchronously.

```python
target = await UdpTransportTarget.create((host, 161), timeout=1, retries=3)
target = target.set_local_address(("192.0.2.10", 0))
```

Use IPv6 with:

```python
target = await Udp6TransportTarget.create(("2001:db8::1", 161))
```

Common ports: manager requests use UDP/161; notifications are commonly sent to
UDP/162.

## Object Identities

Use symbolic MIB names when MIBs are installed and loaded:

```python
ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0))
ObjectType(ObjectIdentity("IF-MIB", "ifDescr", 1))
```

Use dotted numeric OIDs when MIB loading is unavailable or unnecessary:

```python
ObjectType(ObjectIdentity("1.3.6.1.2.1.1.1.0"))
```

For table roots, omit the instance index:

```python
ObjectType(ObjectIdentity("IF-MIB", "ifTable"))
```

## MIB Loading

Use `.load_mibs(...)` on `ObjectIdentity` or `NotificationType` when a symbolic
MIB must be resolved:

```python
ObjectIdentity("SNMPv2-MIB", "sysDescr", 0).load_mibs("SNMPv2-MIB")
```

If custom MIBs are needed, configure MIB sources before resolving names. Avoid
hardcoding symbolic names without ensuring the MIB is available in deployment.
For small tools that must run anywhere, prefer numeric OIDs in config.

## Value Types For SET

Use PySNMP ASN.1 types, not plain Python values, when ambiguity matters:

```python
ObjectType(ObjectIdentity("SNMPv2-MIB", "sysName", 0), OctetString("edge-1"))
ObjectType(ObjectIdentity("1.3.6.1.2.1.2.2.1.7.1"), Integer(2))
```

When a device rejects SET, verify write community/user permissions, value type,
OID instance suffix, and device VACM/access-control rules before changing code.

## Security Handling

- Do not log community strings, auth keys, or privacy keys.
- Load credentials from environment, secret stores, or app config.
- Prefer timeouts and retry counts that fit the polling interval.
- Surface per-host timeout/errors as data in batch pollers; do not let one host
  stop all polling unless the caller requested fail-fast behavior.
