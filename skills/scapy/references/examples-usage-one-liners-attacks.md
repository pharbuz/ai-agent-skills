# Usage snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## usage

Part 7. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 57: literal ---
res, unans = sr( IP(dst="192.168.1.0/24")/UDP()
                /ISAKMP(init_cookie=RandString(8), exch_type="identity prot.")
                /ISAKMP_payload_SA(prop=ISAKMP_payload_Proposal())
              )
```

```python
# --- snippet 58: literal ---
res.nsummary(prn=lambda s,r: r.src, lfilter=lambda s,r: r.haslayer(ISAKMP) )
```

```python
# --- snippet 59: literal ---
conf.iface = "tap0"
llmnrd(iface="tap0", from_ip=Net("10.0.0.1/24"))
```

```python
# --- snippet 60: literal ---
sr1(IP(dst="192.168.122.17")/UDP()/NBNSHeader()/NBNSNodeStatusRequest())
```

```python
# --- snippet 61: literal ---
conf.checkIPaddr = False  # Mandatory because we are using a broadcast destination and receiving unicast
sr1(IP(dst="192.168.0.255")/UDP()/NBNSHeader()/NBNSQueryRequest(QUESTION_NAME="DC1"))
```

```python
# --- snippet 62: literal ---
# For interface 'eth0'
ans, _ = sr(IPv6(dst="ff02::fb%eth0")/UDP(sport=5353, dport=5353)/DNS(rd=0, qd=[DNSQR(qname='_spotify-connect._tcp.local', qtype="PTR")]), multi=True, timeout=2)
ans.show()
```

```python
# --- snippet 63: literal ---
ans, unans = sr(IP(dst="4.2.2.1",ttl=(1,10))/TCP(dport=53,flags="S"))
```

```python
# --- snippet 64: literal ---
ans.summary( lambda s,r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))
# output: 192.168.1.1     time-exceeded
# output: 68.86.90.162    time-exceeded
# output: 4.79.43.134     time-exceeded
# output: 4.79.43.133     time-exceeded
# output: 4.68.18.126     time-exceeded
# output: 4.68.123.38     time-exceeded
# output: 4.2.2.1         SA
```

```python
# --- snippet 65: literal ---
res, unans = sr(IP(dst="target", ttl=(1,20))
              /UDP()/DNS(qd=DNSQR(qname="test.com"))
```

```python
# --- snippet 66: literal ---
res.make_table(lambda s,r: (s.dst, s.ttl, r.src))
```

```python
# --- snippet 67: literal ---
ans, unans = traceroute("4.2.2.1",l4=UDP(sport=RandShort())/DNS(qd=DNSQR(qname="thesprawl.org")))
# output: Begin emission:
..*....******...******.***...****Finished to send 30 packets.
*****...***...............................
# output: Received 75 packets, got 28 answers, remaining 2 packets
   4.2.2.1:udp53
# output: 1  192.168.1.1     11
# output: 4  68.86.90.162    11
# output: 5  4.79.43.134     11
# output: 6  4.79.43.133     11
# output: 7  4.68.18.62      11
# output: 8  4.68.123.6      11
# output: 9  4.2.2.1
...
```

```python
# --- snippet 68: literal ---
sr1(IP(dst="172.16.1.232")/ICMP())
<IP src=172.16.1.232 proto=1 [...] |<ICMP code=0 type=0 [...]|
<Padding load=’0O\x02\x01\x00\x04\x06public\xa2B\x02\x02\x1e’ |>>>
```

```python
# --- snippet 69: literal ---
sr1(IP(dst="172.16.1.1", options="\x02")/ICMP())
<IP src=172.16.1.1 [...] |<ICMP code=0 type=12 [...] |
<IPerror src=172.16.1.24 options=’\x02\x00\x00\x00’ [...] |
<ICMPerror code=0 type=8 id=0x0 seq=0x0 chksum=0xf7ff |
<Padding load=’\x00[...]\x00\x1d.\x00V\x1f\xaf\xd9\xd4;\xca’ |>>>>>
```

```python
# --- snippet 70: literal ---
sendp(Ether()/Dot1Q(vlan=2)/Dot1Q(vlan=7)/IP(dst=target)/ICMP())
```

```python
# --- snippet 71: literal ---
#! /usr/bin/env python
from scapy.all import *

def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn=arp_monitor_callback, filter="arp", store=0)
```

```python
# --- snippet 72: literal ---
conf.checkIPaddr = False
hw = get_if_hwaddr(conf.iface)
dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=hw)/DHCP(options=[("message-type","discover"),"end"])
ans, unans = srp(dhcp_discover, multi=True)      # Press CTRL-C after several seconds
# output: Begin emission:
# output: Finished to send 1 packets.
.*...*..
# output: Received 8 packets, got 2 answers, remaining 0 packets
```

```python
# --- snippet 73: literal ---
ans, unans = sr(IP(dst="172.16.5/24", ttl=15)/TCP())
for i in unans: print(i.dst)
```

```python
# --- snippet 74: literal ---
sr1(IP(dst="72.14.207.99")/TCP(dport=80,flags="S",options=[('Timestamp',(0,0))]))
```

```python
# --- snippet 75: python3 ---
# First, generate some packets...
# output: packets = IP(src="192.0.2.9", dst=Net("192.0.2.10/30"))/ICMP()

# Show them with Wireshark
wireshark(packets)
```
