---
name: scapy
description: >-
  Build, debug, or extend packet-crafting, sniffing, routing, dissector, and
  protocol tooling with Scapy. Trigger WHENEVER the user installs or imports
  `scapy`, `scapy.all`, `Packet`, `Field`, `bind_layers`, `send`, `sendp`,
  `sr`, `sr1`, `srp`, `sniff`, `AsyncSniffer`, `rdpcap`, `wrpcap`, `hexdump`,
  `ls`, `raw`, `IP`, `IPv6`, `TCP`, `UDP`, `ICMP`, `Ether`, `ARP`, `DNS`,
  `Raw`, `conf`, routing/interface helpers, Scapy contrib layers, automata,
  custom dissectors, packet fields, pcap processing, fuzzing, or fixes root
  privileges, libpcap/Npcap, interface, routing, checksum, layer binding,
  optional dependency, or platform-specific Scapy issues.
---

# Scapy

Use this skill for Scapy packet work. Scapy is both an interactive shell and a
Python library for building, dissecting, sending, receiving, sniffing, and
extending packets. Prefer `from scapy.all import ...` for small scripts and
explicit imports from `scapy.layers.*` / `scapy.packet` / `scapy.fields` in
larger codebases.

## Default Workflow

1. Inspect the target OS, privileges, Scapy version, and whether live packet I/O
   is allowed. Sending/sniffing often needs root/admin or capabilities.
2. Read [references/sample-code-manifest.md](references/sample-code-manifest.md)
   and the relevant `references/examples-*.md` snippet before writing code from
   memory.
3. For packet construction, compose layers with `/` and verify with `show2()`,
   `raw()`, and `hexdump()`.
4. For live I/O, choose layer 3 (`send`, `sr`, `sr1`) vs layer 2 (`sendp`,
   `srp`) intentionally.
5. For sniffing, use `sniff(...)` or `AsyncSniffer`, set `iface`, `filter`,
   `lfilter`, `prn`, `count`, `timeout`, and `store` deliberately.
6. For custom protocols, define a `Packet` subclass with `fields_desc`, then use
   `bind_layers`/`guess_payload_class`/`post_build` as needed.
7. For PCAP workflows, use `rdpcap`, `wrpcap`, `PcapReader`, or `PcapWriter`
   instead of ad hoc byte parsing.
8. Verify platform-specific dependencies: Npcap on Windows, libpcap when BPF or
   pcap provider behavior matters, optional packages for plotting/PDF/TLS/etc.

## Minimal Patterns

```python
from scapy.all import ICMP, IP, sr1

reply = sr1(IP(dst="8.8.8.8") / ICMP(), timeout=2, verbose=False)
if reply:
    reply.show()
```

```python
from scapy.all import Ether, IP, TCP, raw, hexdump

pkt = Ether() / IP(dst="example.com") / TCP(dport=80)
pkt.show2()
hexdump(raw(pkt))
```

## Decision Rules

- Use `send`/`sr`/`sr1` for routed L3 packets; use `sendp`/`srp` for Ethernet
  frames or custom L2.
- Use `conf.iface`, `conf.route`, `get_if_addr`, `get_if_hwaddr`, and routing
  helpers before hardcoding interfaces or gateways.
- Use BPF `filter` for kernel/libpcap filtering and `lfilter` for Python-level
  packet predicates.
- Use `store=False` for long-running sniffers to avoid memory growth.
- Use `show()` for current fields and `show2()` when defaults/checksums/lengths
  must be computed by packet build.
- Treat extracted doc snippets as examples; adapt outputs/prompts into normal
  Python before committing application code.

## References

- Read [references/usage-io.md](references/usage-io.md) for packet creation,
  send/receive, sniffing, PCAP, fuzzing, and common one-liners.
- Read [references/build-dissect.md](references/build-dissect.md) for custom
  protocol layers, fields, binding, dissection, and build hooks.
- Read [references/routing-interfaces.md](references/routing-interfaces.md) for
  interface/routing helpers and platform caveats.
- Read [references/advanced-layers.md](references/advanced-layers.md) for
  Automaton, ASN.1/SNMP, pipes, HTTP/TCP/TUN/TAP/Bluetooth, and contrib layers.
- Read [references/install-troubleshoot.md](references/install-troubleshoot.md)
  for installation, optional dependencies, permissions, libpcap/Npcap, and FAQ.
- Read [references/sample-code-manifest.md](references/sample-code-manifest.md)
  to locate source-page markdown references and extracted Python snippets.
