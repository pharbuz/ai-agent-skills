# Advanced Usage And Layers

Source docs and extracted snippets are bundled as markdown references. Use
`references/sample-code-manifest.md` to locate every available file.

## Automaton

Read `source-advanced-automaton-states.md`,
`source-advanced-automaton-conditions-actions.md`,
`source-advanced-automaton-runtime.md`, `examples-advanced-automaton-basics.md`,
and `examples-advanced-automaton-runtime.md` for Scapy's state-machine
framework. Use `Automaton` and `ATMT` decorators when protocol interaction is
stateful and event-driven rather than a single `sr1` request.

Use automata for handshakes, retransmission logic, fuzzers with state, or
protocol clients. Avoid it for simple one-shot probes.

## ASN.1 / SNMP

Read `source-advanced-asn1-snmp-intro.md`,
`source-advanced-asn1-snmp-encoding.md`,
`source-advanced-asn1-snmp-packets.md`,
`source-advanced-asn1-snmp-snmp-layers.md`, and
`examples-advanced-asn1-snmp-basics.md` for ASN.1 packet definitions and
SNMP-specific examples. Use Scapy ASN.1 support when crafting/dissecting ASN.1
encoded protocols; for full SNMP manager behavior, PySNMP may be better.

## Pipes

Read `source-advanced-pipetools-overview.md`,
`source-advanced-pipetools-pipes.md`, `source-advanced-pipetools-examples.md`,
and `examples-advanced-pipetools-http.md` for packet processing pipelines. Use
pipe tools when chaining sources, transforms, sinks, queues, or live packet
processing components.

## HTTP / TCP / TUN-TAP / Bluetooth

- HTTP: read `source-layers-http-basics.md`, `source-layers-http-advanced.md`,
  and `examples-advanced-http-layer.md`; HTTP support may require loading the
  HTTP layer and understanding request/response classes.
- TCP: read `source-layers-tcp.md` for TCP-specific helpers and behavior.
- TUN/TAP: read `source-layers-tuntap-interfaces.md` and
  `source-layers-tuntap-examples.md` for virtual interface integration.
- Bluetooth: read `source-layers-bluetooth-overview.md`,
  `source-layers-bluetooth-low-energy.md`, `source-layers-bluetooth-hci.md`,
  `source-layers-bluetooth-sockets.md`, and
  `source-layers-bluetooth-platform-notes.md`; platform and adapter support
  matters.

## Contrib Layers

Use `load_contrib("name")` or imports from `scapy.contrib.*` for protocols not
loaded by default. Check whether a contrib layer is experimental before relying
on it in production.

Common contrib domains include automotive, industrial/scada, routing protocols,
wireless/Bluetooth-related formats, tunneling, IoT, and application protocols.

## Extending Scapy

Read `source-extending.md`, `examples-build-layer-basics.md`,
`examples-build-dissection-binding.md`, and
`examples-build-special-fields-extending.md`.
For reusable add-ons, package protocol definitions as modules, avoid global side
effects where possible, and document required `bind_layers` calls or
`load_contrib` usage.
