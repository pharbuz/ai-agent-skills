# Samples

PySNMP v7.1 samples are organized by API level and architecture. The docs warn
that some examples may be old; use them for structure, then verify names against
v7.1 API reference, installed types, or tests in the matching GitHub branch.

The actual Python sample files are bundled locally under `assets/samples/`.
Read `references/sample-code-manifest.md` to find the exact file for a sample
page. The upstream license is copied to `assets/LICENSE.rst`.

## Samples Overview

- **HLAPI v3arch asyncio**: compact manager operations and notification
  originator using `SnmpEngine`. Supports SNMPv1, SNMPv2c, and SNMPv3.
- **HLAPI v1arch asyncio**: compact manager operations and notifications using
  `SnmpDispatcher`. Supports SNMPv1/SNMPv2c and can be faster/lighter.
- **Low-level v3arch asyncio**: full SNMP application patterns for agents,
  command responders, and notification receivers.
- **Low-level v1arch asyncio**: packet-level SNMPv1/v2c manager/agent patterns
  with explicit transports and message handling.
- **SMI samples**: MIB tree browsing and agent-side MIB object implementation.

## HLAPI v3arch asyncio

Use these first for new high-level code.

- **Asynchronous SNMP (v3arch)**: section overview; v3arch supports all SNMP
  versions through the full architecture.
- **Various SNMP versions**: shows SNMPv1 GET with
  `CommunityData("public", mpModel=0)`, SNMPv2c with `CommunityData("public")`,
  and SNMPv3 GETBULK with `UsmUserData(...)`; all use `SnmpEngine`,
  `UdpTransportTarget.create`, `ContextData`, and `ObjectType`. Code examples:
  `assets/samples/hlapi/v3arch/asyncio/manager/cmdgen/v1-get.py`,
  `v2c-get.py`, `usm-sha-aes128.py`, `getbulk-to-eom.py`.
- **Walking operations**: demonstrates GETBULK/BULKWALK-style loops, repeating
  requests with the last returned var-binds, printing `prettyPrint()` output,
  and stopping with `is_end_of_mib`.
- **Advanced Command Generator**: covers stronger SNMPv3 auth/privacy variants,
  dynamic host targets, multiple requests, engine reuse, and transport options
  around manager command generation.
- **Common notifications**: basic `send_notification` examples for common
  TRAP/INFORM use, including `NotificationType`, `load_mibs`, and payload
  var-binds. Code examples:
  `assets/samples/hlapi/v3arch/asyncio/agent/ntforg/default-v1-trap.py`,
  `send-trap.py`, `v3-inform.py`.
- **Advanced Notification Originator**: multiple notification targets,
  mixed community/SNMPv3 credentials, trap vs inform behavior, and advanced
  sender-side notification setup.

## HLAPI v1arch asyncio

Use for high-level SNMPv1/SNMPv2c-only code when v3arch features are unnecessary.

- **Asynchronous SNMP (v1arch)**: section overview; uses a dispatcher-oriented
  API rather than `SnmpEngine`.
- **Various SNMP versions**: shows v1/v2c command generation with
  `SnmpDispatcher`, `CommunityData`, `UdpTransportTarget.create`, and
  `ObjectType`. Code examples:
  `assets/samples/hlapi/v1arch/asyncio/manager/cmdgen/v1-get.py`,
  `v2c-get-slim.py`, `v2c-bulk-slim.py`.
- **Walking operations**: v1arch GETNEXT/GETBULK walking patterns and end-of-MIB
  handling for v1/v2c agents.
- **Advanced Command Generator**: performance-oriented v1arch manager options,
  target setup, request reuse, and transport tweaks.
- **Common notifications**: v1arch notification originator basics for community
  based TRAP/INFORM.
- **Advanced Notification Originator**: advanced community-based notification
  targets and transport setup.

## Low-Level v3arch asyncio

Use for SNMP applications rather than one-shot manager commands.

- **Asynchronous SNMP (v3arch)**: low-level v3arch overview for standard SNMP
  applications.
- **Agent-Side MIB Implementations**: command responder backed by custom MIB
  instrumentation and exported MIB objects. Code examples live under
  `assets/samples/v3arch/asyncio/agent/cmdrsp/`.
- **Various SNMP versions**: agent command responder setup for v1/v2c/v3 message
  processing and security models.
- **Transport Tweaks (Manager Side, v3arch)**: notification receiver/manager
  transport binding, multiple interfaces, local addresses, and inbound messages.

## Low-Level v1arch asyncio

Use when performance and packet-level control matter more than concise code.

- **Fetching Variables**: manager-side GET flow with explicit v1arch transport
  setup such as `udp.DOMAIN_NAME` and `UdpAsyncioTransport().open_client_mode()`.
  Code example: `assets/samples/v1arch/asyncio/manager/cmdgen/fetch-scalar-value.py`.
- **Modifying Variables**: low-level SET flow, request construction, response
  parsing, and write-error handling.
- **MIB Walking Operations**: GETNEXT/GETBULK table traversal, lexicographic
  progression, and stop conditions.
- **Transport Tweaks (Manager Side, v1arch)**: client transport tuning, IPv4/IPv6
  setup, binding local endpoints, and timeout/retry behavior.
- **Agent-side MIB implementations**: command responder plus MIB-backed values.
- **Transport Tweaks (Agent Side, v1arch)**: notification originator or agent
  local transport binding and server-side endpoint setup.
- **Transport Tweaks (Manager Side, v1arch)**: notification receiver transport
  binding and multiple listening endpoints.

## SMI Samples

- **Browsing MIB Tree (Manager Side)**: uses `MibBuilder` and
  `MibViewController` to load MIBs, inspect symbols, resolve names/OIDs, and add
  MIB sources such as local directories. Code examples live under
  `assets/samples/smi/manager/`.
- **Implementing MIB Objects (Agent Side)**: uses MIB builder imports,
  `MibScalarInstance`, syntax cloning, and `export_symbols` to expose static or
  dynamic managed objects from an agent. Code examples live under
  `assets/samples/smi/agent/`.

## Sample Usage Rules

- Replace demo host, ports, communities, users, and auth/privacy keys.
- Use `demo.pysnmp.com` only for disposable examples.
- Prefer explicit imports in production; docs samples may use wildcard imports.
- For symbolic MIB names, install/configure MIB sources or use numeric OIDs.
- For SNMPv3 notifications, align engine IDs, users, auth/privacy protocols, and
  VACM on sender and receiver.
- Do not rewrite sample code from memory when a bundled example matches the task;
  read the relevant local `.py` file first and adapt it.
