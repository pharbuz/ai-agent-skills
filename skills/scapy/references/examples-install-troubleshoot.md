# Installation and troubleshooting snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## installation

```python
# Extracted Python snippets from doc/scapy/installation.rst
# Source: https://scapy.readthedocs.io/en/latest/
# Snippets may require root/admin privileges, live network access, or optional dependencies.


# --- snippet 1: python ---
p=sniff(count=50)
p.plot(lambda x:len(x))

# --- snippet 2: python ---
p=IP()/ICMP()
p.pdfdump("test.pdf")

# --- snippet 3: python ---
p=rdpcap("myfile.pcap")
p.conversations(type="jpg", target="> test.jpg")

# --- snippet 4: python ---
enc=rdpcap("weplab-64bit-AA-managed.pcap")
enc.show()
enc[0]
conf.wepkey="AA\x00\x00\x00"
dec=Dot11PacketList(enc).toEthernet()
dec.show()
dec[0]

# --- snippet 5: python ---
load_module("nmap")
nmap_fp("192.168.0.1")
# output: Begin emission:
# output: Finished to send 8 packets.
# output: Received 19 packets, got 4 answers, remaining 4 packets
(0.88749999999999996, ['Draytek Vigor 2000 ISDN router'])

# --- snippet 6: literal ---
from scapy.config import conf
conf.use_pcap = True

# --- snippet 7: literal ---
conf.use_pcap = True

# --- snippet 8: literal ---
conf.use_pcap = True
```

## troubleshooting

```python
# Extracted Python snippets from doc/scapy/troubleshooting.rst
# Source: https://scapy.readthedocs.io/en/latest/
# Snippets may require root/admin privileges, live network access, or optional dependencies.


# --- snippet 1: literal ---
# Of course, conf.iface can be replaced by any interfaces accessed through conf.ifaces
conf.iface.setmonitor(True)

# --- snippet 2: literal ---
conf.L3socket
<class __main__.L3PacketSocket at 0xb7bdf5fc>
conf.L3socket = L3RawSocket
sr1(IP() / ICMP())
<IP  version=4L ihl=5L tos=0x0 len=28 id=40953 flags= frag=0L ttl=64 proto=ICMP chksum=0xdce5 src=127.0.0.1 dst=127.0.0.1 options='' |<ICMP  type=echo-reply code=0 chksum=0xffff id=0x0 seq=0x0 |>>

# --- snippet 3: literal ---
# Layer 3
sr1(IPv6() / ICMPv6EchoRequest())
<IPv6  version=6 tc=0 fl=866674 plen=8 nh=ICMPv6 hlim=64 src=::1 dst=::1 |<ICMPv6EchoReply  type=Echo Reply code=0 cksum=0x7ebb id=0x0 seq=0x0 |>>

# Layer 2
srp1(Ether() / IPv6() / ICMPv6EchoRequest(), iface=conf.loopback_name)
<Ether  dst=00:00:00:00:00:00 src=00:00:00:00:00:00 type=IPv6 |<IPv6  version=6 tc=0 fl=866674 plen=8 nh=ICMPv6 hlim=64 src=::1 dst=::1 |<ICMPv6EchoReply  type=Echo Reply code=0 cksum=0x7ebb id=0x0 seq=0x0 |>>>

# --- snippet 4: literal ---
# output: On Linux, libpcap does not support loopback IPv4 pings:
conf.use_pcap = True
sr1(IP() / ICMP())
# output: Begin emission:
# output: Finished sending 1 packets.
    .....................................

# output: You can disable libpcap using ``conf.use_pcap = False`` or bypass it on layer 3 using ``conf.L3socket = L3RawSocket``.

# --- snippet 5: literal ---
# Layer 3
sr1(IP() / ICMP())
<IP  version=4L ihl=5L tos=0x0 len=28 id=40953 flags= frag=0L ttl=64 proto=ICMP chksum=0xdce5 src=127.0.0.1 dst=127.0.0.1 options='' |<ICMP  type=echo-reply code=0 chksum=0xffff id=0x0 seq=0x0 |>>
sr1(IPv6() / ICMPv6EchoRequest())
<IPv6  version=6 tc=0 fl=866674 plen=8 nh=ICMPv6 hlim=64 src=::1 dst=::1 |<ICMPv6EchoReply  type=Echo Reply code=0 cksum=0x7ebb id=0x0 seq=0x0 |>>

# Layer 2
srp1(Loopback() / IP() / ICMP(), iface=conf.loopback_name)
<Loopback  type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=28 id=56066 flags= frag=0 ttl=64 proto=icmp chksum=0x0 src=127.0.0.1 dst=127.0.0.1 |<ICMP  type=echo-reply code=0 chksum=0xffff id=0x0 seq=0x0 |>>>
srp1(Loopback() / IPv6() / ICMPv6EchoRequest(), iface=conf.loopback_name)
<Loopback  type=IPv6 |<IPv6  version=6 tc=0 fl=0 plen=8 nh=ICMPv6 hlim=64 src=::1 dst=::1 |<ICMPv6EchoReply  type=Echo Reply code=0 cksum=0x7ebb id=0x0 seq=0x0 |>>>

# --- snippet 6: literal ---
conf.sniff_promisc = False

# --- snippet 7: literal ---
C:/Windows/System32/wpcap.dll
C:/Windows/System32/Packet.dll
```
