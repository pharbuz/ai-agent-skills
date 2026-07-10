# Installation And Troubleshooting

Read `references/sample-code-manifest.md` for installation/troubleshooting
source markdown and extracted snippets before resolving environment issues.

## Installation

```bash
pip install scapy
```

Use a virtual environment for library work. Use the system package only when the
OS distribution requires it for packet capture integration.

## Privileges

- Sending raw packets and sniffing usually require root/admin privileges.
- On Linux, capabilities may be used instead of full root in controlled setups.
- On Windows, run as Administrator and install Npcap.

## Optional Dependencies

Scapy can work without all optional packages, but features may be disabled.
Common optional areas:

- plotting/graphs/PDF output,
- cryptography/TLS-related features,
- libpcap provider behavior,
- Bluetooth, CAN, and other platform-specific interfaces.

If Scapy prints warnings at startup, map each missing package to the feature the
user actually needs before installing broad dependency sets.

## libpcap / Npcap

- Use libpcap/Npcap when BPF filters, capture performance, or platform capture
  behavior require it.
- Windows packet capture normally depends on Npcap.
- BPF `filter=` expressions may fail or behave differently without a pcap
  provider.

## Common Problems

- `PermissionError` or no packets sent: run with privileges or configure
  capabilities.
- No sniffed packets: verify `iface`, monitor/promiscuous mode, firewall, and
  whether traffic reaches that interface.
- BPF filter errors: install/enable libpcap/Npcap or simplify the filter.
- Wrong interface/source address: inspect `conf.iface`, `show_interfaces()`, and
  `conf.route`.
- Checksums/lengths look unset: use `show2()` or build bytes with `raw(pkt)`.
- Custom layer not dissected: verify `bind_layers` conditions and field values.
- Importing `scapy.all` is slow: use explicit imports in production modules.

## Safety

Packet crafting can disrupt networks. Prefer lab interfaces, test pcaps, and
explicit target ranges. Do not run flooding/fuzzing examples against networks
without authorization.
