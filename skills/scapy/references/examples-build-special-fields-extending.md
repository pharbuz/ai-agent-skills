# Build/dissect snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## build_dissect

Part 4. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 35: literal ---
# output: Emph     # Wrapper to emphasize field when printing, e.g. Emph(IPField("dst", "127.0.0.1")),

ActionField

ConditionalField(fld, cond)
        # Wrapper to make field 'fld' only appear if
        # function 'cond' evals to True, e.g.
        # ConditionalField(XShortField("chksum",None),lambda pkt:pkt.chksumpresent==1)
        # When hidden, it won't be built nor dissected and the stored value will be 'None'


PadField(fld, align, padwith=None)
       # Add bytes after the proxified field so that it ends at
       # the specified alignment from its beginning

BitExtendedField(extension_bit)
       # Field with a variable number of bytes. Each byte is made of:
       # - 7 bits of data
       # - 1 extension bit:
       #    * 0 means that it is the last byte of the field ("stopping bit")
       #    * 1 means that there is another byte after this one ("forwarding bit")
       # extension_bit is the bit number [0-7] of the extension bit in the byte

MSBExtendedField, LSBExtendedField      # Special cases of BitExtendedField
```

```python
# --- snippet 36: literal ---
IPField
SourceIPField

IPoptionsField
TCPOptionsField

MACField
DestMACField(MACField)
SourceMACField(MACField)

ICMPTimeStampField
```

```python
# --- snippet 37: literal ---
Dot11AddrMACField
Dot11Addr2MACField
Dot11Addr3MACField
Dot11Addr4MACField
Dot11SCField
```

```python
# --- snippet 38: literal ---
DNSStrField
DNSRRCountField
DNSRRField
DNSQRField
```

```python
# --- snippet 39: literal ---
# output: NetBIOSNameField         # NetBIOS (StrFixedLenField)

# output: ISAKMPTransformSetField  # ISAKMP (StrLenField)

# output: TimeStampField           # NTP (BitField)

## extending

```python
# Extracted Python snippets from doc/scapy/extending.rst
# Source: https://scapy.readthedocs.io/en/latest/
# Snippets may require root/admin privileges, live network access, or optional dependencies.
```

```python
# --- snippet 1: literal ---
#! /usr/bin/env python

import sys
from scapy.all import sr1,IP,ICMP

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()
```

```python
# --- snippet 2: literal ---
#! /usr/bin/env python
# arping2tex : arpings a network and outputs a LaTeX table as a result

import sys
if len(sys.argv) != 2:
    print("Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24")
    sys.exit(1)

from scapy.all import srp, Ether, ARP, conf
conf.verb = 0
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=sys.argv[1]),
                 timeout=2)

print(r"\begin{tabular}{|l|l|}")
print(r"\hline")
print(r"MAC & IP\\")
print(r"\hline")
for snd,rcv in ans:
    print(rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\"))
print(r"\hline")
print(r"\end{tabular}")
```

```python
# --- snippet 3: literal ---
#! /usr/bin/env python
from scapy.all import *

def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn=arp_monitor_callback, filter="arp", store=0)
```

```python
# --- snippet 4: literal ---
#! /usr/bin/env python

# Set log level to benefit from Scapy warnings
import logging
# output: logger = logging.getLogger("scapy")
logger.setLevel(logging.INFO)

from scapy.all import *

class Test(Packet):
# output: name = "Test packet"
# output: fields_desc = [ ShortField("test1", 1),
                    ShortField("test2", 2) ]

def make_test(x,y):
    return Ether()/IP()/Test(test1=x,test2=y)

if __name__ == "__main__":
    interact(mydict=globals(), mybanner="Test add-on v3.14")
```
