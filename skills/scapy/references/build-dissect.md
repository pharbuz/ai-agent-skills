# Building And Dissecting Protocols

Read `references/sample-code-manifest.md` for exact source and example files.
For custom layer work, start with:

- `source-build-simple-layer-and-fields.md`
- `source-build-variable-length-and-dissecting.md`
- `source-build-layer-binding-and-payload-guess.md`
- `source-build-packet-building-and-fields.md`
- `source-build-dependent-fields-and-payloads.md`
- `source-build-field-type-catalog.md`
- `examples-build-layer-basics.md`
- `examples-build-dissection-binding.md`
- `examples-build-fields-catalog.md`

## New Layer Pattern

Define a protocol as a `Packet` subclass with `fields_desc`.

```python
from scapy.packet import Packet
from scapy.fields import ByteField, ShortField, IntEnumField

class Disney(Packet):
    name = "DisneyPacket"
    fields_desc = [
        ShortField("mickey", 5),
        ByteField("minnie", 3),
        IntEnumField("donald", 1, {1: "happy", 2: "cool", 3: "angry"}),
    ]
```

Use Scapy field classes instead of manual slicing whenever possible. Field
objects convert between internal, machine, and human representations.

## Binding Layers

Use `bind_layers(lower, upper, field=value)` so Scapy can dissect payloads.

```python
bind_layers(UDP, MyProtocol, dport=12345)
bind_layers(MyProtocol, NextProtocol, msg_type=1)
```

Use `payload_guess`, `guess_payload_class`, or custom logic only when static
field-based binding cannot describe the protocol.

## Build Hooks

- `post_build(self, pkt, pay)`: fill length/checksum fields after payload build.
- `post_dissect` / `pre_dissect`: adjust bytes around dissection.
- `extract_padding`: split real payload from padding.
- `answers(self, other)`: define request/response matching for `sr`.

## Field Choices

- Numeric: `ByteField`, `ShortField`, `IntField`, `LongField`.
- Hex display: `XByteField`, `XShortField`, `XIntField`.
- Enums: `ByteEnumField`, `ShortEnumField`, `IntEnumField`.
- Length-linked strings/lists: use `FieldLenField`, `StrLenField`,
  `PacketListField` rather than manual length management.
- Conditional/variable fields: `ConditionalField`, custom `Field` subclasses.

## Debugging Dissection

- Start with `raw(pkt)` and reparse with `MyPacket(raw_bytes)`.
- Use `show2()` to force build-time fields.
- Use `hexdump`, `ls`, and `conf.debug_dissector` when dissection fails.
- Keep test packets/pcaps for custom protocols; field regressions are easy to
  miss without raw-byte tests.
