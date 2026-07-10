# Usage snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## usage

Part 2. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 11: literal ---
p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
# output: Begin emission:
# output: ...Finished to send 1 packets.
.*
# output: Received 5 packets, got 1 answers, remaining 0 packets
p
<IP version=4L ihl=5L tos=0x0 len=39 id=15489 flags= frag=0L ttl=42 proto=ICMP
 chksum=0x51dd src=66.35.250.151 dst=192.168.5.21 options='' |<ICMP type=echo-reply
 code=0 chksum=0xee45 id=0x0 seq=0x0 |<Raw load='XXXXXXXXXXX'
 |<Padding load='\x00\x00\x00\x00' |>>>>
p.show()
---[ IP ]---
# output: version   = 4L
# output: ihl       = 5L
# output: tos       = 0x0
# output: len       = 39
# output: id        = 15489
# output: flags     =
# output: frag      = 0L
# output: ttl       = 42
# output: proto     = ICMP
# output: chksum    = 0x51dd
src       = 66.35.250.151
# output: dst       = 192.168.5.21
# output: options   = ''
---[ ICMP ]---
# output: type      = echo-reply
# output: code      = 0
# output: chksum    = 0xee45
# output: id        = 0x0
# output: seq       = 0x0
---[ Raw ]---
# output: load      = 'XXXXXXXXXXX'
---[ Padding ]---
# output: load      = '\x00\x00\x00\x00'
```

```python
# --- snippet 12: literal ---
sr1(IP(dst="192.168.5.1")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.slashdot.org")))
# output: Begin emission:
# output: Finished to send 1 packets.
..*
# output: Received 3 packets, got 1 answers, remaining 0 packets
<IP version=4L ihl=5L tos=0x0 len=78 id=0 flags=DF frag=0L ttl=64 proto=UDP chksum=0xaf38
 src=192.168.5.1 dst=192.168.5.21 options='' |<UDP sport=53 dport=53 len=58 chksum=0xd55d
 |<DNS id=0 qr=1L opcode=QUERY aa=0L tc=0L rd=1L ra=1L z=0L rcode=ok qdcount=1 ancount=1
 nscount=0 arcount=0 qd=<DNSQR qname='www.slashdot.org.' qtype=A qclass=IN |>
 an=<DNSRR rrname='www.slashdot.org.' type=A rclass=IN ttl=3560L rdata='66.35.250.151' |>
 ns=0 ar=0 |<Padding load='\xc6\x94\xc7\xeb' |>>>>
```

```python
# --- snippet 13: literal ---
sr(IP(dst="192.168.8.1")/TCP(dport=[21,22,23]))
# output: Received 6 packets, got 3 answers, remaining 0 packets
(<Results: UDP:0 TCP:3 ICMP:0 Other:0>, <Unanswered: UDP:0 TCP:0 ICMP:0 Other:0>)
ans, unans = _
ans.summary()
IP / TCP 192.168.8.14:20 > 192.168.8.1:21 S ==> Ether / IP / TCP 192.168.8.1:21 > 192.168.8.14:20 RA / Padding
IP / TCP 192.168.8.14:20 > 192.168.8.1:22 S ==> Ether / IP / TCP 192.168.8.1:22 > 192.168.8.14:20 RA / Padding
IP / TCP 192.168.8.14:20 > 192.168.8.1:23 S ==> Ether / IP / TCP 192.168.8.1:23 > 192.168.8.14:20 RA / Padding
```

```python
# --- snippet 14: literal ---
sr(IP(dst="172.20.29.5/30")/TCP(dport=[21,22,23]),inter=0.5,retry=-2,timeout=1)
# output: Begin emission:
# output: Finished to send 12 packets.
# output: Begin emission:
# output: Finished to send 9 packets.
# output: Begin emission:
# output: Finished to send 9 packets.

# output: Received 100 packets, got 3 answers, remaining 9 packets
(<Results: UDP:0 TCP:3 ICMP:0 Other:0>, <Unanswered: UDP:0 TCP:9 ICMP:0 Other:0>)
```

```python
# --- snippet 15: literal ---
sr1(IP(dst="72.14.207.99")/TCP(dport=80,flags="S"))
```

```python
# --- snippet 16: literal ---
# output: Begin emission:
# output: .Finished to send 1 packets.
*
# output: Received 2 packets, got 1 answers, remaining 0 packets
<IP  version=4L ihl=5L tos=0x20 len=44 id=33529 flags= frag=0L ttl=244
proto=TCP chksum=0x6a34 src=72.14.207.99 dst=192.168.1.100 options=// |
<TCP  sport=www dport=ftp-data seq=2487238601L ack=1 dataofs=6L reserved=0L
flags=SA window=8190 chksum=0xcdc7 urgptr=0 options=[('MSS', 536)] |
<Padding  load='V\xf7' |>>>
```

```python
# --- snippet 17: literal ---
ans, unans = sr(IP(dst=["192.168.1.1","yahoo.com","slashdot.org"])/TCP(dport=[22,80,443],flags="S"))
# output: Begin emission:
.......*.**.......Finished to send 9 packets.
**.*.*..*..................
# output: Received 362 packets, got 8 answers, remaining 1 packets
ans.make_table(
   lambda s,r: (s.dst, s.dport,
   r.sprintf("{TCP:%TCP.flags%}{ICMP:%IP.src% - %ICMP.type%}")))
# output: 66.35.250.150                192.168.1.1 216.109.112.135
# output: 22  66.35.250.150 - dest-unreach RA          -
# output: 80  SA                           RA          SA
# output: 443 SA                           SA          SA
```

```python
# --- snippet 18: literal ---
report_ports("192.168.1.1",(440,443))
# output: Begin emission:
...*.**Finished to send 4 packets.
*
# output: Received 8 packets, got 4 answers, remaining 0 packets
'\\begin{tabular}{|r|l|l|}\n\\hline\nhttps & open & SA \\\\\n\\hline\n440
 & closed & TCP RA \\\\\n441 & closed & TCP RA \\\\\n442 & closed &
TCP RA \\\\\n\\hline\n\\hline\n\\end{tabular}\n'
```
