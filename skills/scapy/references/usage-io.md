# Usage And Packet I/O

Read `references/sample-code-manifest.md` for every source and example file.
For packet I/O work, start with:

- `source-usage-starting-packets-pcap.md`
- `source-usage-packet-sets-send-receive.md`
- `source-usage-supersockets-sniffing.md`
- `source-usage-async-sniffing-sessions-filters.md`
- `source-usage-loop-io-import-export-tables.md`
- `examples-usage-packet-basics.md`
- `examples-usage-send-receive.md`
- `examples-usage-sniffing.md`
- `examples-usage-import-export-tables.md`

## Packet Construction

- Build packets by stacking layers with `/`: `Ether()/IP()/TCP()/Raw(...)`.
- A string/bytes payload becomes a `Raw` layer.
- Fields can be read, assigned, or deleted to restore defaults.
- Use `raw(pkt)`/`bytes(pkt)` to build bytes, and `Layer(raw_bytes)` to dissect.
- Use `pkt.show()` for current values, `pkt.show2()` after build-time
  auto-computation, `hexdump(pkt)` for bytes, and `ls(PacketClass)` for fields.
- Use field sets like `IP(dst="192.0.2.0/30")` or `TCP(dport=[80, 443])` to
  generate packet sets.

## Sending And Receiving

- `send(pkt)`: send L3/routed packets.
- `sendp(pkt, iface=...)`: send L2 frames.
- `sr(pkt)`: send and receive answers/unanswered packets.
- `sr1(pkt)`: return the first answer.
- `srp(pkt)`: L2 send/receive, common for ARP/Ethernet discovery.
- `return_packets=True` makes send functions return sent packet lists.
- Use `timeout`, `retry`, `inter`, `loop`, and `verbose=False` intentionally.

## Sniffing

- `sniff(iface=..., filter=..., count=..., timeout=..., prn=...)` captures live
  traffic.
- `filter` is BPF/libpcap filtering; `lfilter` is Python packet filtering.
- Use `store=False` for long-running sniffers.
- Use `AsyncSniffer` when capture should run in the background.

## PCAP

- `rdpcap(path)` loads packets into a packet list.
- `wrpcap(path, packets)` writes packets.
- Prefer streaming `PcapReader`/`PcapWriter` for large captures.
- PacketList helpers include `summary`, `nsummary`, `filter`, `hexdump`,
  `conversations`, `plot`, and `make_table`.

## Recipes

- ARP scan: `srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=net), timeout=...)`.
- ICMP ping: `sr1(IP(dst=host)/ICMP(), timeout=...)`.
- TCP SYN probe: `sr1(IP(dst=host)/TCP(dport=port, flags="S"), timeout=...)`.
- DNS query: `sr1(IP(dst=dns)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=name)))`.
- Fuzzing: wrap parts of a packet with `fuzz(...)` and constrain dangerous
  fields explicitly.

For exact examples, read the bundled snippets before writing new code.
