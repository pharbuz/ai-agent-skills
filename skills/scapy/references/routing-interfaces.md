# Routing And Interfaces

Read `references/source-routing.md` and `references/examples-routing.md` for
exact examples.

## Interface Helpers

- `show_interfaces()` lists interfaces.
- `get_if_list()` returns interface names.
- `get_if_addr(iface)` returns IPv4 address.
- `get_if_hwaddr(iface)` returns MAC address.
- `conf.iface` is the default interface.
- Use `iface=...` on send/sniff functions when ambiguity matters.

## Routes

- `conf.route` displays and controls IPv4 routes.
- `conf.route6` handles IPv6 routes.
- Use route lookup before hardcoding a source address or interface.
- `conf.route.route(dst)` can reveal selected interface/source/gateway.

## Next Hop And MAC

- Use Scapy route helpers to find gateways/default routes.
- For L2 destination MAC, use ARP/neighbor discovery or `getmacbyip`.
- Do not assume destination MAC is the target host; routed traffic uses the next
  hop MAC.

## Layer 3 vs Layer 2

- `send`/`sr` use routing and build L2 for you.
- `sendp`/`srp` require a link-layer frame such as `Ether(...)`.
- Use `sendp` for ARP, custom EtherTypes, VLAN tags, and raw L2 protocols.

## Platform Notes

- Interface names differ by OS; avoid hardcoded `eth0`/`en0` in reusable code.
- Windows generally requires Npcap and Administrator privileges.
- Linux raw sockets usually require root or capabilities.
- macOS/BSD behavior differs around BPF devices and monitor mode.
