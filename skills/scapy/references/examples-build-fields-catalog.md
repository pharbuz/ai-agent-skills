# Build/dissect snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## build_dissect

Part 3. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 24: literal ---
ByteField
XByteField

ShortField
SignedShortField
LEShortField
XShortField

# output: X3BytesField        # three bytes as hex
# output: XLE3BytesField      # little endian three bytes as hex
# output: ThreeBytesField     # three bytes as decimal
# output: LEThreeBytesField   # little endian three bytes as decimal
LE3BytesEnumField
XLE3BytesEnumField

IntField
SignedIntField
LEIntField
LESignedIntField
XIntField

LongField
SignedLongField
LELongField
LESignedLongField
XLongField
LELongField

IEEEFloatField
IEEEDoubleField
# output: BCDFloatField       # binary coded decimal

BitField
XBitField

# output: BitFieldLenField    # BitField specifying a length (used in RTP)
FlagsField
FloatField
```

```python
# --- snippet 25: literal ---
ByteEnumField("code", 4, {1:"REQUEST",2:"RESPONSE",3:"SUCCESS",4:"FAILURE"})
```

```python
# --- snippet 26: literal ---
EnumField(name, default, enum, fmt = "H")
CharEnumField
BitEnumField
ShortEnumField
LEShortEnumField
ByteEnumField
IntEnumField
SignedIntEnumField
LEIntEnumField
XShortEnumField
```

```python
# --- snippet 27: literal ---
StrField(name, default, fmt="H", remain=0, shift=0)
StrLenField(name, default, fld=None, length_from=None, shift=0):
StrFixedLenField
StrNullField
StrStopField
```

```python
# --- snippet 28: literal ---
FieldList(name, default, field, fld=None, shift=0, length_from=None, count_from=None)
  # A list assembled and dissected with many times the same field type

  # field: instance of the field that will be used to assemble and disassemble a list item
  # length_from: name of the FieldLenField holding the list length

FieldLenField     #  holds the list length of a FieldList field
LEFieldLenField

# output: LenField          # contains len(pkt.payload)

PacketField       # holds packets
PacketLenField    # used e.g. in ISAKMP_payload_Proposal
PacketListField
```

```python
# --- snippet 29: literal ---
FieldLenField("the_lenfield", None, count_of="the_varfield")
```

```python
# --- snippet 30: literal ---
FieldLenField("the_lenfield", None, length_of="the_varfield", adjust=lambda pkt,x:(x+1)/2)
```

```python
# --- snippet 31: literal ---
StrLenField("the_varfield", "the_default_value", length_from = lambda pkt: pkt.the_lenfield)
```

```python
# --- snippet 32: literal ---
StrLenField("the_varfield", "the_default_value", length_from = lambda pkt: pkt.the_lenfield-12)
```

```python
# --- snippet 33: literal ---
FieldListField("the_varfield", ["1.2.3.4"], IPField("", "0.0.0.0"), count_from = lambda pkt: pkt.the_lenfield)
```

```python
# --- snippet 34: literal ---
class TestSLF(Packet):
    fields_desc=[ FieldLenField("len", None, length_of="data"),
                  StrLenField("data", "", length_from=lambda pkt:pkt.len) ]

class TestPLF(Packet):
    fields_desc=[ FieldLenField("len", None, count_of="plist"),
                  PacketListField("plist", None, IP, count_from=lambda pkt:pkt.len) ]

class TestFLF(Packet):
    fields_desc=[
       FieldLenField("the_lenfield", None, count_of="the_varfield"),
       FieldListField("the_varfield", ["1.2.3.4"], IPField("", "0.0.0.0"),
# output: count_from = lambda pkt: pkt.the_lenfield) ]

class TestPkt(Packet):
# output: fields_desc = [ ByteField("f1",65),
                    ShortField("f2",0x4244) ]
    def extract_padding(self, p):
        return "", p

class TestPLF2(Packet):
# output: fields_desc = [ FieldLenField("len1", None, count_of="plist",fmt="H", adjust=lambda pkt,x:x+2),
                    FieldLenField("len2", None, length_of="plist",fmt="I", adjust=lambda pkt,x:(x+1)/2),
                    PacketListField("plist", None, TestPkt, length_from=lambda x:(x.len2*2)/3*3) ]
```
