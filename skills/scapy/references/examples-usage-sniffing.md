# Usage snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## usage

Part 4. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 23: literal ---
sniff(filter="icmp and host 66.35.250.151", count=2)
<Sniffed: UDP:0 TCP:0 ICMP:2 Other:0>
 a=_
 a.nsummary()
# output: 0000 Ether / IP / ICMP 192.168.5.21 echo-request 0 / Raw
# output: 0001 Ether / IP / ICMP 192.168.5.21 echo-request 0 / Raw
 a[1]
<Ether dst=00:ae:f3:52:aa:d1 src=00:02:15:37:a2:44 type=0x800 |<IP version=4L
 ihl=5L tos=0x0 len=84 id=0 flags=DF frag=0L ttl=64 proto=ICMP chksum=0x3831
 src=192.168.5.21 dst=66.35.250.151 options='' |<ICMP type=echo-request code=0
 chksum=0x6571 id=0x8745 seq=0x0 |<Raw load='B\xf7g\xda\x00\x07um\x08\t\n\x0b
 \x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d
 \x1e\x1f !\x22#$%&\'()*+,-./01234567' |>>>>
sniff(iface="wifi0", prn=lambda x: x.summary())
# output: 802.11 Management 8 ff:ff:ff:ff:ff:ff / 802.11 Beacon / Info SSID / Info Rates / Info DSset / Info TIM / Info 133
# output: 802.11 Management 4 ff:ff:ff:ff:ff:ff / 802.11 Probe Request / Info SSID / Info Rates
# output: 802.11 Management 5 00:0a:41:ee:a5:50 / 802.11 Probe Response / Info SSID / Info Rates / Info DSset / Info 133
# output: 802.11 Management 4 ff:ff:ff:ff:ff:ff / 802.11 Probe Request / Info SSID / Info Rates
# output: 802.11 Management 4 ff:ff:ff:ff:ff:ff / 802.11 Probe Request / Info SSID / Info Rates
# output: 802.11 Management 8 ff:ff:ff:ff:ff:ff / 802.11 Beacon / Info SSID / Info Rates / Info DSset / Info TIM / Info 133
# output: 802.11 Management 11 00:07:50:d6:44:3f / 802.11 Authentication
# output: 802.11 Management 11 00:0a:41:ee:a5:50 / 802.11 Authentication
# output: 802.11 Management 0 00:07:50:d6:44:3f / 802.11 Association Request / Info SSID / Info Rates / Info 133 / Info 149
# output: 802.11 Management 1 00:0a:41:ee:a5:50 / 802.11 Association Response / Info Rates / Info 133 / Info 149
# output: 802.11 Management 8 ff:ff:ff:ff:ff:ff / 802.11 Beacon / Info SSID / Info Rates / Info DSset / Info TIM / Info 133
# output: 802.11 Management 8 ff:ff:ff:ff:ff:ff / 802.11 Beacon / Info SSID / Info Rates / Info DSset / Info TIM / Info 133
# output: 802.11 / LLC / SNAP / ARP who has 172.20.70.172 says 172.20.70.171 / Padding
# output: 802.11 / LLC / SNAP / ARP is at 00:0a:b7:4b:9c:dd says 172.20.70.172 / Padding
# output: 802.11 / LLC / SNAP / IP / ICMP echo-request 0 / Raw
# output: 802.11 / LLC / SNAP / IP / ICMP echo-reply 0 / Raw
sniff(iface="eth1", prn=lambda x: x.show())
---[ Ethernet ]---
# output: dst       = 00:ae:f3:52:aa:d1
src       = 00:02:15:37:a2:44
# output: type      = 0x800
---[ IP ]---
# output: version   = 4L
# output: ihl       = 5L
# output: tos       = 0x0
# output: len       = 84
# output: id        = 0
# output: flags     = DF
# output: frag      = 0L
# output: ttl       = 64
# output: proto     = ICMP
# output: chksum    = 0x3831
   src       = 192.168.5.21
# output: dst       = 66.35.250.151
# output: options   = ''
---[ ICMP ]---
# output: type      = echo-request
# output: code      = 0
# output: chksum    = 0x89d9
# output: id        = 0xc245
# output: seq       = 0x0
---[ Raw ]---
# output: load      = 'B\xf7i\xa9\x00\x04\x149\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !\x22#$%&\'()*+,-./01234567'
---[ Ethernet ]---
# output: dst       = 00:02:15:37:a2:44
src       = 00:ae:f3:52:aa:d1
# output: type      = 0x800
---[ IP ]---
# output: version   = 4L
# output: ihl       = 5L
# output: tos       = 0x0
# output: len       = 84
# output: id        = 2070
# output: flags     =
# output: frag      = 0L
# output: ttl       = 42
# output: proto     = ICMP
# output: chksum    = 0x861b
   src       = 66.35.250.151
# output: dst       = 192.168.5.21
# output: options   = ''
---[ ICMP ]---
# output: type      = echo-reply
# output: code      = 0
# output: chksum    = 0x91d9
# output: id        = 0xc245
# output: seq       = 0x0
---[ Raw ]---
# output: load      = 'B\xf7i\xa9\x00\x04\x149\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !\x22#$%&\'()*+,-./01234567'
---[ Padding ]---
# output: load      = '\n_\x00\x0b'
sniff(iface=["eth1","eth2"], prn=lambda x: x.sniffed_on+": "+x.summary())
# output: eth3: Ether / IP / ICMP 192.168.5.21 > 66.35.250.151 echo-request 0 / Raw
# output: eth3: Ether / IP / ICMP 66.35.250.151 > 192.168.5.21 echo-reply 0 / Raw
# output: eth2: Ether / IP / ICMP 192.168.5.22 > 66.35.250.152 echo-request 0 / Raw
# output: eth2: Ether / IP / ICMP 66.35.250.152 > 192.168.5.22 echo-reply 0 / Raw
```

```python
# --- snippet 24: literal ---
pkts = sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
# output: 192.168.1.100 -> 64.233.167.99

# output: 64.233.167.99 -> 192.168.1.100

# output: 192.168.1.100 -> 64.233.167.99

# output: 192.168.1.100 -> 64.233.167.99
'GET / HTTP/1.1\r\nHost: 64.233.167.99\r\nUser-Agent: Mozilla/5.0
(X11; U; Linux i686; en-US; rv:1.8.1.8) Gecko/20071022 Ubuntu/7.10 (gutsy)
Firefox/2.0.0.8\r\nAccept: text/xml,application/xml,application/xhtml+xml,
text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Language:
en-us,en;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset:
ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nKeep-Alive: 300\r\nConnection:
keep-alive\r\nCache-Control: max-age=0\r\n\r\n'
```

```python
# --- snippet 25: literal ---
p
<Ether dst=00:10:4b:b3:7d:4e src=00:40:33:96:7b:60 type=0x800 |<IP version=4L
 ihl=5L tos=0x0 len=60 id=61681 flags=DF frag=0L ttl=64 proto=TCP chksum=0xb85e
 src=192.168.8.10 dst=192.168.8.1 options='' |<TCP sport=46511 dport=80
 seq=2023566040L ack=0L dataofs=10L reserved=0L flags=SEC window=5840
 chksum=0x570c urgptr=0 options=[('Timestamp', (342940201L, 0L)), ('MSS', 1460),
 ('NOP', ()), ('SAckOK', ''), ('WScale', 0)] |>>>
load_module("p0f")
p0f(p)
(1.0, ['Linux 2.4.2 - 2.4.14 (1)'])
a=sniff(prn=prnp0f)
(1.0, ['Linux 2.4.2 - 2.4.14 (1)'])
(1.0, ['Linux 2.4.2 - 2.4.14 (1)'])
(0.875, ['Linux 2.4.2 - 2.4.14 (1)', 'Linux 2.4.10 (1)', 'Windows 98 (?)'])
(1.0, ['Windows 2000 (9)'])
```

```python
# --- snippet 26: literal ---
sniff(session=IPSession, iface="eth0")
sniff(session=TCPSession, prn=lambda x: x.summary(), store=False)
sniff(offline="file.pcap", session=NetflowSession)
```
