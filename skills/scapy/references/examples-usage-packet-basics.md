# Usage snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## usage

Part 1. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 1: literal ---
a=IP(ttl=10)
a
< IP ttl=10 |>
a.src
’127.0.0.1’
a.dst="192.168.1.1"
a
< IP ttl=10 dst=192.168.1.1 |>
a.src
’192.168.8.14’
del(a.ttl)
a
< IP dst=192.168.1.1 |>
a.ttl
64
```

```python
# --- snippet 2: literal ---
IP()
<IP |>
IP()/TCP()
<IP frag=0 proto=TCP |<TCP |>>
Ether()/IP()/TCP()
<Ether type=0x800 |<IP frag=0 proto=TCP |<TCP |>>>
IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"
<IP frag=0 proto=TCP |<TCP |<Raw load='GET / HTTP/1.0\r\n\r\n' |>>>
Ether()/IP()/IP()/UDP()
<Ether type=0x800 |<IP frag=0 proto=IP |<IP frag=0 proto=UDP |<UDP |>>>>
IP(proto=55)/TCP()
<IP frag=0 proto=55 |<TCP |>>
```

```python
# --- snippet 3: literal ---
raw(IP())
'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xe7\x7f\x00\x00\x01\x7f\x00\x00\x01'
IP(_)
<IP version=4L ihl=5L tos=0x0 len=20 id=1 flags= frag=0L ttl=64 proto=IP
 chksum=0x7ce7 src=127.0.0.1 dst=127.0.0.1 |>
 a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"
 hexdump(a)
# output: 00 02 15 37 A2 44 00 AE F3 52 AA D1 08 00 45 00  ...7.D...R....E.
# output: 00 43 00 01 00 00 40 06 78 3C C0 A8 05 15 42 23  .C....@.x<....B#
# output: FA 97 00 14 00 50 00 00 00 00 00 00 00 00 50 02  .....P........P.
# output: 20 00 BB 39 00 00 47 45 54 20 2F 69 6E 64 65 78   ..9..GET /index
# output: 2E 68 74 6D 6C 20 48 54 54 50 2F 31 2E 30 20 0A  .html HTTP/1.0 .
# output: 0A                                               .
b=raw(a)
b
'\x00\x02\x157\xa2D\x00\xae\xf3R\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00@\x06x<\xc0
 \xa8\x05\x15B#\xfa\x97\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00
 \xbb9\x00\x00GET /index.html HTTP/1.0 \n\n'
c=Ether(b)
c
<Ether dst=00:02:15:37:a2:44 src=00:ae:f3:52:aa:d1 type=0x800 |<IP version=4L
 ihl=5L tos=0x0 len=67 id=1 flags= frag=0L ttl=64 proto=TCP chksum=0x783c
 src=192.168.5.21 dst=66.35.250.151 options='' |<TCP sport=20 dport=80 seq=0L
 ack=0L dataofs=5L reserved=0L flags=S window=8192 chksum=0xbb39 urgptr=0
 options=[] |<Raw load='GET /index.html HTTP/1.0 \n\n' |>>>>
```

```python
# --- snippet 4: literal ---
c.hide_defaults()
c
<Ether dst=00:0f:66:56:fa:d2 src=00:ae:f3:52:aa:d1 type=0x800 |<IP ihl=5L len=67
 frag=0 proto=TCP chksum=0x783c src=192.168.5.21 dst=66.35.250.151 |<TCP dataofs=5L
 chksum=0xbb39 options=[] |<Raw load='GET /index.html HTTP/1.0 \n\n' |>>>>
```

```python
# --- snippet 5: literal ---
a=IP(dst="www.slashdot.org/30")
a
<IP  dst=Net('www.slashdot.org/30') |>
[p for p in a]
[<IP dst=66.35.250.148 |>, <IP dst=66.35.250.149 |>,
 <IP dst=66.35.250.150 |>, <IP dst=66.35.250.151 |>]
b=IP(ttl=[1,2,(5,9)])
b
<IP ttl=[1, 2, (5, 9)] |>
[p for p in b]
[<IP ttl=1 |>, <IP ttl=2 |>, <IP ttl=5 |>, <IP ttl=6 |>,
 <IP ttl=7 |>, <IP ttl=8 |>, <IP ttl=9 |>]
c=TCP(dport=[80,443])
[p for p in a/c]
[<IP frag=0 proto=TCP dst=66.35.250.148 |<TCP dport=80 |>>,
 <IP frag=0 proto=TCP dst=66.35.250.148 |<TCP dport=443 |>>,
 <IP frag=0 proto=TCP dst=66.35.250.149 |<TCP dport=80 |>>,
 <IP frag=0 proto=TCP dst=66.35.250.149 |<TCP dport=443 |>>,
 <IP frag=0 proto=TCP dst=66.35.250.150 |<TCP dport=80 |>>,
 <IP frag=0 proto=TCP dst=66.35.250.150 |<TCP dport=443 |>>,
 <IP frag=0 proto=TCP dst=66.35.250.151 |<TCP dport=80 |>>,
 <IP frag=0 proto=TCP dst=66.35.250.151 |<TCP dport=443 |>>]
```

```python
# --- snippet 6: literal ---
p = PacketList(a)
p
<PacketList: TCP:0 UDP:0 ICMP:0 Other:4>
p = PacketList([p for p in a/c])
p
<PacketList: TCP:8 UDP:0 ICMP:0 Other:0>
```

```python
# --- snippet 7: literal ---
send(IP(dst="1.2.3.4")/ICMP())
# output: .
# output: Sent 1 packets.
sendp(Ether()/IP(dst="1.2.3.4",ttl=(1,4)), iface="eth1")
# output: ....
# output: Sent 4 packets.
sendp("I'm travelling on Ethernet", iface="eth1", loop=1, inter=0.2)
................^C
# output: Sent 16 packets.
sendp(rdpcap("/tmp/pcapfile")) # tcpreplay
...........
# output: Sent 11 packets.

# output: Returns packets sent by send()
send(IP(dst='127.0.0.1'), return_packets=True)
# output: .
# output: Sent 1 packets.
<PacketList: TCP:0 UDP:0 ICMP:0 Other:1>
```

```python
# --- snippet 8: literal ---
pkt = IP(dst=ScopedIP("224.0.0.1", scope=conf.iface))/ICMP()
```

```python
# --- snippet 9: literal ---
send(IP(dst="target")/fuzz(UDP()/NTP(version=4)),loop=1)
................^C
# output: Sent 16 packets.
```

```python
# --- snippet 10: literal ---
pkt = IP(len=RawVal(b"NotAnInteger"), src="127.0.0.1")
bytes(pkt)
b'H\x00NotAnInt\x0f\xb3er\x00\x01\x00\x00@\x00\x00\x00\x7f\x00\x00\x01\x7f\x00\x00\x01\x00\x00'
```
