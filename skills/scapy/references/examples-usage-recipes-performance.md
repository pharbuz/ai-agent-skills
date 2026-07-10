# Usage snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## usage

Part 8. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 76: literal ---
ans, unans = srloop(IP(dst="192.168.1.1")/TCP(dport=80,flags="S"))
```

```python
# --- snippet 77: literal ---
load_module("nmap")
```

```python
# --- snippet 78: literal ---
conf.nmap_base
```

```python
# --- snippet 79: literal ---
nmap_fp("192.168.1.1",oport=443,cport=1)
# output: Begin emission:
.****..**Finished to send 8 packets.
*................................................
# output: Received 58 packets, got 7 answers, remaining 1 packets
(1.0, ['Linux 2.4.0 - 2.5.20', 'Linux 2.4.19 w/grsecurity patch',
'Linux 2.4.20 - 2.4.22 w/grsecurity.org patch', 'Linux 2.4.22-ck2 (x86)
# output: w/grsecurity.org and HZ=1000 patches', 'Linux 2.4.7 - 2.6.11'])
```

```python
# --- snippet 80: literal ---
conf.p0f_base
```
