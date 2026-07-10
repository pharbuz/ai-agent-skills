# Build/dissect snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## build_dissect

Part 1. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 1: literal ---
class Disney(Packet):
# output: name = "DisneyPacket "
    fields_desc=[ ShortField("mickey",5),
                 XByteField("minnie",3) ,
                 IntEnumField("donald" , 1 ,
                      { 1: "happy", 2: "cool" , 3: "angry" } ) ]
```

```python
# --- snippet 2: literal ---
d=Disney(mickey=1)
ls(d)
# output: mickey : ShortField = 1 (5)
# output: minnie : XByteField = 3 (3)
# output: donald : IntEnumField = 1 (1)
d.show()
###[ Disney Packet ]###
mickey= 1
minnie= 0x3
donald= happy
d.donald="cool"
raw(d)
’\x00\x01\x03\x00\x00\x00\x02’
Disney(_)
<Disney mickey=1 minnie=0x3 donald=cool |>
```

```python
# --- snippet 3: literal ---
p = IP()/TCP()/"AAAA"
p
<IP  frag=0 proto=TCP |<TCP  |<Raw  load='AAAA' |>>>
p.summary()
'IP / TCP 127.0.0.1:ftp-data > 127.0.0.1:www S / Raw'
```

```python
# --- snippet 4: literal ---
class UDP(Packet):
# output: name = "UDP"
# output: fields_desc = [ ShortEnumField("sport", 53, UDP_SERVICES),
                    ShortEnumField("dport", 53, UDP_SERVICES),
                    ShortField("len", None),
                    XShortField("chksum", None), ]
```

```python
# --- snippet 5: literal ---
class StrFixedLenField(StrField):
      def addfield(self, pkt, s, val):
          return s+struct.pack("%is"%self.length,self.i2m(pkt, val))
```

```python
# --- snippet 6: literal ---
class StrFixedLenField(StrField):
      def getfield(self, pkt, s):
          return s[self.length:], self.m2i(pkt,s[:self.length])
```

```python
# --- snippet 7: literal ---
class VarLenQField(Field):
    """ variable length quantities """
# output: __slots__ = ["fld"]

    def __init__(self, name, default, fld):
        Field.__init__(self, name, default)
# output: self.fld = fld

    def i2m(self, pkt, x):
        if x is None:
# output: f = pkt.get_field(self.fld)
# output: x = f.i2len(pkt, pkt.getfieldval(self.fld))
# output: x = vlenq2str(x)
        return raw(x)

    def m2i(self, pkt, x):
        if s is None:
            return None, 0
        return str2vlenq(x)[1]

    def addfield(self, pkt, s, val):
        return s+self.i2m(pkt, val)

    def getfield(self, pkt, s):
        return str2vlenq(s)
```

```python
# --- snippet 8: literal ---
class FOO(Packet):
# output: name = "FOO"
# output: fields_desc = [ VarLenQField("len", None, "data"),
                    StrLenField("data", "", length_from=lambda pkt: pkt.len) ]

f = FOO(data="A"*129)
f.show()
###[ FOO ]###
  len= None
  data=    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
```

```python
# --- snippet 9: literal ---
def dissect(self, s):
# output: s = self.pre_dissect(s)
# output: s = self.do_dissect(s)
# output: s = self.post_dissect(s)
    payl,pad = self.extract_padding(s)
    self.do_dissect_payload(payl)
    if pad and conf.padding:
        self.add_payload(Padding(pad))
```

```python
# --- snippet 10: literal ---
p=IP("A"*20)/TCP("B"*32)
# output: WARNING: bad dataofs (4). Assuming dataofs=5
p
<IP  version=4L ihl=1L tos=0x41 len=16705 id=16705 flags=DF frag=321L ttl=65 proto=65 chksum=0x4141
src=65.65.65.65 dst=65.65.65.65 |<TCP  sport=16962 dport=16962 seq=1111638594L ack=1111638594L dataofs=4L
reserved=2L flags=SE window=16962 chksum=0x4242 urgptr=16962 options=[] |<Raw  load='BBBBBBBBBBBB' |>>>
```

```python
# --- snippet 11: literal ---
def do_dissect_payload(self, s):
# output: cls = self.guess_payload_class(s)
# output: p = cls(s, _internal=1, _underlayer=self)
      self.add_payload(p)
```

```python
# --- snippet 12: literal ---
bind_layers(ProtoA, ProtoB, FieldToBind=Value)
```

```python
# --- snippet 13: literal ---
bind_layers( TCP, HTTP, sport=80 )
bind_layers( TCP, HTTP, dport=80 )
```
