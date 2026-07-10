# Usage snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## usage

Part 5. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 27: literal ---
class TLS(Packet):
    [...]

    @classmethod
    def tcp_reassemble(cls, data, metadata, session):
# output: length = struct.unpack("!H", data[3:5])[0] + 5
        if len(data) == length:
            return TLS(data)
```

```python
# --- snippet 28: literal ---
a=sniff(filter="tcp and ( port 25 or port 110 )",
 prn=lambda x: x.sprintf("%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%  %2s,TCP.flags% : %TCP.payload%"))
# output: 192.168.8.10:47226 -> 213.228.0.14:110   S :
# output: 213.228.0.14:110 -> 192.168.8.10:47226  SA :
# output: 192.168.8.10:47226 -> 213.228.0.14:110   A :
# output: 213.228.0.14:110 -> 192.168.8.10:47226  PA : +OK <13103.1048117923@pop2-1.free.fr>

# output: 192.168.8.10:47226 -> 213.228.0.14:110   A :
# output: 192.168.8.10:47226 -> 213.228.0.14:110  PA : USER toto

# output: 213.228.0.14:110 -> 192.168.8.10:47226   A :
# output: 213.228.0.14:110 -> 192.168.8.10:47226  PA : +OK

# output: 192.168.8.10:47226 -> 213.228.0.14:110   A :
# output: 192.168.8.10:47226 -> 213.228.0.14:110  PA : PASS tata

# output: 213.228.0.14:110 -> 192.168.8.10:47226  PA : -ERR authorization failed

# output: 192.168.8.10:47226 -> 213.228.0.14:110   A :
# output: 213.228.0.14:110 -> 192.168.8.10:47226  FA :
# output: 192.168.8.10:47226 -> 213.228.0.14:110  FA :
# output: 213.228.0.14:110 -> 192.168.8.10:47226   A :
```

```python
# --- snippet 29: literal ---
srloop(IP(dst="www.target.com/30")/TCP())
# output: RECV 1: Ether / IP / TCP 192.168.11.99:80 > 192.168.8.14:20 SA / Padding
# output: fail 3: IP / TCP 192.168.8.14:20 > 192.168.11.96:80 S
        IP / TCP 192.168.8.14:20 > 192.168.11.98:80 S
        IP / TCP 192.168.8.14:20 > 192.168.11.97:80 S
# output: RECV 1: Ether / IP / TCP 192.168.11.99:80 > 192.168.8.14:20 SA / Padding
# output: fail 3: IP / TCP 192.168.8.14:20 > 192.168.11.96:80 S
        IP / TCP 192.168.8.14:20 > 192.168.11.98:80 S
        IP / TCP 192.168.8.14:20 > 192.168.11.97:80 S
# output: RECV 1: Ether / IP / TCP 192.168.11.99:80 > 192.168.8.14:20 SA / Padding
# output: fail 3: IP / TCP 192.168.8.14:20 > 192.168.11.96:80 S
        IP / TCP 192.168.8.14:20 > 192.168.11.98:80 S
        IP / TCP 192.168.8.14:20 > 192.168.11.97:80 S
# output: RECV 1: Ether / IP / TCP 192.168.11.99:80 > 192.168.8.14:20 SA / Padding
# output: fail 3: IP / TCP 192.168.8.14:20 > 192.168.11.96:80 S
        IP / TCP 192.168.8.14:20 > 192.168.11.98:80 S
        IP / TCP 192.168.8.14:20 > 192.168.11.97:80 S
```

```python
# --- snippet 30: literal ---
wrpcap("temp.cap",pkts)
```

```python
# --- snippet 31: literal ---
pkt_hex = Ether(import_hexcap())
# output: 0000   00 50 56 FC CE 50 00 0C  29 2B 53 19 08 00 45 00   .PV..P..)+S...E.
# output: 0010   00 54 00 00 40 00 40 01  5A 7C C0 A8 19 82 04 02   .T..@.@.Z|......
# output: 0020   02 01 08 00 9C 90 5A 61  00 01 E6 DA 70 49 B6 E5   ......Za....pI..
# output: 0030   08 00 08 09 0A 0B 0C 0D  0E 0F 10 11 12 13 14 15   ................
# output: 0040   16 17 18 19 1A 1B 1C 1D  1E 1F 20 21 22 23 24 25   .......... !"#$%
# output: 0050   26 27 28 29 2A 2B 2C 2D  2E 2F 30 31 32 33 34 35   &'()*+,-./012345
# output: 0060   36 37                                              67
pkt_hex
<Ether  dst=00:50:56:fc:ce:50 src=00:0c:29:2b:53:19 type=0x800 |<IP  version=4L
ihl=5L tos=0x0 len=84 id=0 flags=DF frag=0L ttl=64 proto=icmp chksum=0x5a7c
src=192.168.25.130 dst=4.2.2.1 options='' |<ICMP  type=echo-request code=0
chksum=0x9c90 id=0x5a61 seq=0x1 |<Raw  load='\xe6\xdapI\xb6\xe5\x08\x00\x08\t\n
\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e
\x1f !"#$%&\'()*+,-./01234567' |>>>>
```

```python
# --- snippet 32: literal ---
pkts = sniff(count = 1)
pkt = pkts[0]
pkt
<Ether  dst=00:50:56:fc:ce:50 src=00:0c:29:2b:53:19 type=0x800 |<IP  version=4L
ihl=5L tos=0x0 len=84 id=0 flags=DF frag=0L ttl=64 proto=icmp chksum=0x5a7c
src=192.168.25.130 dst=4.2.2.1 options='' |<ICMP  type=echo-request code=0
chksum=0x9c90 id=0x5a61 seq=0x1 |<Raw  load='\xe6\xdapI\xb6\xe5\x08\x00\x08\t\n
\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e
\x1f !"#$%&\'()*+,-./01234567' |>>>>
pkt_raw = raw(pkt)
pkt_raw
'\x00PV\xfc\xceP\x00\x0c)+S\x19\x08\x00E\x00\x00T\x00\x00@\x00@\x01Z|\xc0\xa8
\x19\x82\x04\x02\x02\x01\x08\x00\x9c\x90Za\x00\x01\xe6\xdapI\xb6\xe5\x08\x00
\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b
\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'
```

```python
# --- snippet 33: literal ---
ans, unans = sr(IP(dst="www.test.fr/30", ttl=(1,6))/TCP())
# output: Received 49 packets, got 24 answers, remaining 0 packets
ans.make_table( lambda s,r: (s.dst, s.ttl, r.src) )
# output: 216.15.189.192  216.15.189.193  216.15.189.194  216.15.189.195
# output: 1 192.168.8.1     192.168.8.1     192.168.8.1     192.168.8.1
# output: 2 81.57.239.254   81.57.239.254   81.57.239.254   81.57.239.254
# output: 3 213.228.4.254   213.228.4.254   213.228.4.254   213.228.4.254
# output: 4 213.228.3.3     213.228.3.3     213.228.3.3     213.228.3.3
# output: 5 193.251.254.1   193.251.251.69  193.251.254.1   193.251.251.69
# output: 6 193.251.241.174 193.251.241.178 193.251.241.174 193.251.241.178
```

```python
# --- snippet 34: literal ---
ans, unans = sr(IP(dst="172.20.80.192/28")/TCP(dport=[20,21,22,25,53,80]))
# output: Received 142 packets, got 25 answers, remaining 71 packets
ans.make_table(lambda s,r: (s.dst, s.dport, r.sprintf("%IP.id%")))
# output: 172.20.80.196 172.20.80.197 172.20.80.198 172.20.80.200 172.20.80.201
# output: 20 0             4203          7021          -             11562
# output: 21 0             4204          7022          -             11563
# output: 22 0             4205          7023          11561         11564
# output: 25 0             0             7024          -             11565
# output: 53 0             4207          7025          -             11566
# output: 80 0             4028          7026          -             11567
```
