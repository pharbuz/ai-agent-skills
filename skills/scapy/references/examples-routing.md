# Routing snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## routing

```python
# Extracted Python snippets from doc/scapy/routing.rst
# Source: https://scapy.readthedocs.io/en/latest/
# Snippets may require root/admin privileges, live network access, or optional dependencies.


# --- snippet 1: pycon ---
conf.ifaces
# output: Source  Index  Name  MAC                IPv4          IPv6
# output: sys     1      lo    00:00:00:00:00:00  127.0.0.1     ::1
# output: sys     2      eth0  Microsof:12:cb:ef  10.0.0.5  fe80::10a:2bef:dc12:afae
conf.ifaces.dev_from_index(2)
<NetworkInterface eth0 [UP+BROADCAST+RUNNING+SLAVE]>

# --- snippet 2: pycon ---
load_extcap()
conf.ifaces
# output: Source       Index  Name                                     Address
# output: ciscodump    100    Cisco remote capture                     ciscodump
# output: dpauxmon     100    DisplayPort AUX channel monitor capture  dpauxmon
# output: randpktdump  100    Random packet generator                  randpkt
# output: sdjournal    100    systemd Journal Export                   sdjournal
# output: sshdump      100    SSH remote capture                       sshdump
# output: udpdump      100    UDP Listener remote capture              udpdump
# output: wifidump     100    Wi-Fi remote capture                     wifidump
# output: Source  Index  Name  MAC                IPv4          IPv6
# output: sys     1      lo    00:00:00:00:00:00  127.0.0.1     ::1
# output: sys     2      eth0  Microsof:12:cb:ef  10.0.0.5  fe80::10a:2bef:dc12:afae

# --- snippet 3: pycon ---
load_extcap()
sniff(
    iface="sshdump",
    prn=lambda x: x.summary(),
    remote_host="192.168.0.1",
    remote_username="root",
    remote_password="SCAPY",
)

# --- snippet 4: python ---
conf.ifaces.dev_from_networkname("sshdump").get_extcap_config()

# --- snippet 5: pycon ---
conf.route

# output: Network          Netmask          Gateway   Iface  Output IP  Metric
# output: 0.0.0.0          0.0.0.0          10.0.0.1  eth0   10.0.0.5   100
# output: 10.0.0.0         255.255.255.0    0.0.0.0   eth0   10.0.0.5   0
# output: 127.0.0.0        255.0.0.0        0.0.0.0   lo     127.0.0.1  1
# output: 168.63.129.16    255.255.255.255  10.0.0.1  eth0   10.0.0.5   100
# output: 169.254.169.254  255.255.255.255  10.0.0.1  eth0   10.0.0.5   100

# --- snippet 6: pycon ---
conf.route.route("127.0.0.1")
('lo', '127.0.0.1', '0.0.0.0')

# --- snippet 7: pycon ---
gw = conf.route.route("0.0.0.0")[2]
gw
'10.0.0.1'

# --- snippet 8: pycon ---
ip = get_if_addr(conf.iface)  # default interface
ip = get_if_addr("eth0")
ip
'10.0.0.5'

# --- snippet 9: pycon ---
mac = get_if_hwaddr(conf.iface)  # default interface
mac = get_if_hwaddr("eth0")
mac
'54:3f:19:c9:38:6d'
```
