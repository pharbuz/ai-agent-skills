# Build/dissect snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## build_dissect

Part 2. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 14: literal ---
class Dot11(Packet):
    def guess_payload_class(self, payload):
        if self.FCfield & 0x40:
            return Dot11WEP
        else:
            return Packet.guess_payload_class(self, payload)
```

```python
# --- snippet 15: literal ---
p=TCP()
p.payload_guess
[({'dport': 2000}, <class 'scapy.Skinny'>), ({'sport': 2000}, <class 'scapy.Skinny'>), ... )]
```

```python
# --- snippet 16: literal ---
p = IP()/TCP()
hexdump(p)
# output: 0000 45 00 00 28 00 01 00 00 40 06 7C CD 7F 00 00 01 E..(....@.|.....
# output: 0010 7F 00 00 01 00 14 00 50 00 00 00 00 00 00 00 00 .......P........
# output: 0020 50 02 20 00 91 7C 00 00 P. ..|..
```

```python
# --- snippet 17: literal ---
class XNumberField(FieldLenField):

    def __init__(self, name, default, sep="\r\n"):
        FieldLenField.__init__(self, name, default, fld)
# output: self.sep = sep

    def i2m(self, pkt, x):
# output: x = FieldLenField.i2m(self, pkt, x)
        return "%02x" % x

    def m2i(self, pkt, x):
        return int(x, 16)

    def addfield(self, pkt, s, val):
        return s+self.i2m(pkt, val)

    def getfield(self, pkt, s):
# output: sep = s.find(self.sep)
        return s[sep:], self.m2i(pkt, s[:sep])
```

```python
# --- snippet 18: literal ---
class Foo(Packet):
# output: fields_desc = [
          ByteField("type", 0),
          XNumberField("len", None, "\r\n"),
          StrFixedLenField("sep", "\r\n", 2)
          ]

      def post_build(self, p, pay):
        if self.len is None and pay:
# output: l = len(pay)
# output: p = p[:1] + struct.pack("!B", l) + p[2:]
        return p+pay
```

```python
# --- snippet 19: literal ---
class Bar1(Packet):
# output: fields_desc = [
          IntField("val", 0),
          ]

class Bar2(Packet):
# output: fields_desc = [
          IPField("addr", "127.0.0.1")
          ]
```

```python
# --- snippet 20: literal ---
def __div__(self, other):
    if isinstance(other, Packet):
# output: cloneA = self.copy()
# output: cloneB = other.copy()
        cloneA.add_payload(cloneB)
        return cloneA
# output: elif type(other) is str:
        return self/Raw(load=other)
```

```python
# --- snippet 21: literal ---
IP()/"AAAA"
<IP  |<Raw  load='AAAA' |>>
```

```python
# --- snippet 22: literal ---
bind_layers( Foo, Bar1, {'type':1} )
bind_layers( Foo, Bar2, {'type':2} )
```

```python
# --- snippet 23: literal ---
hexdump(raw(p))
Packet.str=Foo
Packet.iter=Foo
Packet.iter=Bar1
Packet.build=Foo
Packet.build=Bar1
Packet.post_build=Bar1
Packet.post_build=Foo
```
