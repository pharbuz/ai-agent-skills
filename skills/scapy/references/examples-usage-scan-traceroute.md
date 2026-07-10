# Usage snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## usage

Part 3. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 19: literal ---
ans, unans = sr(IP(dst=target, ttl=(4,25),id=RandShort())/TCP(flags=0x2))
*****.******.*.***..*.**Finished to send 22 packets.
***......
# output: Received 33 packets, got 21 answers, remaining 1 packets
for snd,rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))
...
# output: 5 194.51.159.65 0
# output: 6 194.51.159.49 0
# output: 4 194.250.107.181 0
# output: 7 193.251.126.34 0
# output: 8 193.251.126.154 0
# output: 9 193.251.241.89 0
# output: 10 193.251.241.110 0
# output: 11 193.251.241.173 0
# output: 13 208.172.251.165 0
# output: 12 193.251.241.173 0
# output: 14 208.172.251.165 0
# output: 15 206.24.226.99 0
# output: 16 206.24.238.34 0
# output: 17 173.109.66.90 0
# output: 18 173.109.88.218 0
# output: 19 173.29.39.101 1
# output: 20 173.29.39.101 1
# output: 21 173.29.39.101 1
# output: 22 173.29.39.101 1
# output: 23 173.29.39.101 1
# output: 24 173.29.39.101 1
```

```python
# --- snippet 20: literal ---
lsc()
sr               : Send and receive packets at layer 3
sr1              : Send packets at layer 3 and return only the first answer
srp              : Send and receive packets at layer 2
srp1             : Send and receive packets at layer 2 and return only the first answer
srloop           : Send a packet at layer 3 in loop and print the answer each time
srploop          : Send a packet at layer 2 in loop and print the answer each time
sniff            : Sniff packets
# output: p0f              : Passive OS fingerprinting: which OS emitted this TCP SYN ?
# output: arpcachepoison   : Poison target's cache with (your MAC,victim's IP) couple
send             : Send packets at layer 3
sendp            : Send packets at layer 2
# output: traceroute       : Instant TCP traceroute
# output: arping           : Send ARP who-has requests to determine which hosts are up
ls               : List  available layers, or infos on a given layer
lsc              : List user commands
# output: queso            : Queso OS fingerprinting
# output: nmap_fp          : nmap fingerprinting
# output: report_ports     : portscan a target and output a LaTeX table
# output: dyndns_add       : Send a DNS add message to a nameserver for "name" to have a new "rdata"
# output: dyndns_del       : Send a DNS delete message to a nameserver for "name"
[...]
```

```python
# --- snippet 21: literal ---
conf.use_pcap = True
```

```python
# --- snippet 22: literal ---
conf.L3socket=L3pcapSocket  # Receive/send L3 packets through libpcap
conf.L2listen=L2ListenTcpdump  # Receive L2 packets through TCPDump
```
