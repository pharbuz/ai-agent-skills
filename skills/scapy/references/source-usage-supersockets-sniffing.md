
Note that the TCP traceroute and some other high-level functions are already coded::

    >>> lsc()
    sr               : Send and receive packets at layer 3
    sr1              : Send packets at layer 3 and return only the first answer
    srp              : Send and receive packets at layer 2
    srp1             : Send and receive packets at layer 2 and return only the first answer
    srloop           : Send a packet at layer 3 in loop and print the answer each time
    srploop          : Send a packet at layer 2 in loop and print the answer each time
    sniff            : Sniff packets
    p0f              : Passive OS fingerprinting: which OS emitted this TCP SYN ?
    arpcachepoison   : Poison target's cache with (your MAC,victim's IP) couple
    send             : Send packets at layer 3
    sendp            : Send packets at layer 2
    traceroute       : Instant TCP traceroute
    arping           : Send ARP who-has requests to determine which hosts are up
    ls               : List  available layers, or infos on a given layer
    lsc              : List user commands
    queso            : Queso OS fingerprinting
    nmap_fp          : nmap fingerprinting
    report_ports     : portscan a target and output a LaTeX table
    dyndns_add       : Send a DNS add message to a nameserver for "name" to have a new "rdata"
    dyndns_del       : Send a DNS delete message to a nameserver for "name"
    [...]

Scapy may also use the GeoIP2 module, in combination with matplotlib and `cartopy <http://scitools.org.uk/cartopy/docs/latest/installing.html>`_ to generate fancy graphics such as below:

.. image:: graphics/traceroute_worldplot.png

In this example, we used the `traceroute_map()` function to print the graphic. This method is a shortcut which uses the `world_trace` of the `TracerouteResult` objects.
It could have been done differently:

    >>> conf.geoip_city = "path/to/GeoLite2-City.mmdb"
    >>> a, _ = traceroute(["www.google.co.uk", "www.secdev.org"], verbose=0)
    >>> a.world_trace()

or such as above:

    >>> conf.geoip_city = "path/to/GeoLite2-City.mmdb"
    >>> traceroute_map(["www.google.co.uk", "www.secdev.org"])

To use those functions, it is required to have installed the `geoip2 <https://pypi.python.org/pypi/geoip2>`_ module, `its database <https://dev.maxmind.com/geoip/geoip2/geolite2/>`_ (`direct download <https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz>`_)
but also the `cartopy <http://scitools.org.uk/cartopy/docs/latest/installing.html>`_ module.

Configuring super sockets
-------------------------

.. index::
   single: super socket

Different super sockets are available in Scapy: the **native** ones, and the ones that use **libpcap** (to send/receive packets).

By default, Scapy will try to use the native ones (*except on Windows, where the winpcap/npcap ones are preferred*). To manually use the **libpcap** ones, you must:

* On Unix/OSX: be sure to have libpcap installed.
* On Windows: have Npcap/Winpcap installed. (default)

Then use::

    >>> conf.use_pcap = True

This will automatically update the sockets pointing to ``conf.L2socket`` and ``conf.L3socket``.

If you want to manually set them, you have a bunch of sockets available, depending on your platform. For instance, you might want to use::

    >>> conf.L3socket=L3pcapSocket  # Receive/send L3 packets through libpcap
    >>> conf.L2listen=L2ListenTcpdump  # Receive L2 packets through TCPDump

Sniffing
--------

.. index::
   single: sniff()

We can easily capture some packets or even clone tcpdump or tshark. Either one interface or a list of interfaces to sniff on can be provided. If no interface is given, sniffing will happen on ``conf.iface``::

    >>>  sniff(filter="icmp and host 66.35.250.151", count=2)
    <Sniffed: UDP:0 TCP:0 ICMP:2 Other:0>
    >>>  a=_
    >>>  a.nsummary()
    0000 Ether / IP / ICMP 192.168.5.21 echo-request 0 / Raw
    0001 Ether / IP / ICMP 192.168.5.21 echo-request 0 / Raw
    >>>  a[1]
    <Ether dst=00:ae:f3:52:aa:d1 src=00:02:15:37:a2:44 type=0x800 |<IP version=4L
     ihl=5L tos=0x0 len=84 id=0 flags=DF frag=0L ttl=64 proto=ICMP chksum=0x3831
     src=192.168.5.21 dst=66.35.250.151 options='' |<ICMP type=echo-request code=0
     chksum=0x6571 id=0x8745 seq=0x0 |<Raw load='B\xf7g\xda\x00\x07um\x08\t\n\x0b
     \x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d
     \x1e\x1f !\x22#$%&\'()*+,-./01234567' |>>>>
    >>> sniff(iface="wifi0", prn=lambda x: x.summary())
    802.11 Management 8 ff:ff:ff:ff:ff:ff / 802.11 Beacon / Info SSID / Info Rates / Info DSset / Info TIM / Info 133
    802.11 Management 4 ff:ff:ff:ff:ff:ff / 802.11 Probe Request / Info SSID / Info Rates
    802.11 Management 5 00:0a:41:ee:a5:50 / 802.11 Probe Response / Info SSID / Info Rates / Info DSset / Info 133
    802.11 Management 4 ff:ff:ff:ff:ff:ff / 802.11 Probe Request / Info SSID / Info Rates
    802.11 Management 4 ff:ff:ff:ff:ff:ff / 802.11 Probe Request / Info SSID / Info Rates
    802.11 Management 8 ff:ff:ff:ff:ff:ff / 802.11 Beacon / Info SSID / Info Rates / Info DSset / Info TIM / Info 133
    802.11 Management 11 00:07:50:d6:44:3f / 802.11 Authentication
    802.11 Management 11 00:0a:41:ee:a5:50 / 802.11 Authentication
    802.11 Management 0 00:07:50:d6:44:3f / 802.11 Association Request / Info SSID / Info Rates / Info 133 / Info 149
    802.11 Management 1 00:0a:41:ee:a5:50 / 802.11 Association Response / Info Rates / Info 133 / Info 149
    802.11 Management 8 ff:ff:ff:ff:ff:ff / 802.11 Beacon / Info SSID / Info Rates / Info DSset / Info TIM / Info 133
    802.11 Management 8 ff:ff:ff:ff:ff:ff / 802.11 Beacon / Info SSID / Info Rates / Info DSset / Info TIM / Info 133
    802.11 / LLC / SNAP / ARP who has 172.20.70.172 says 172.20.70.171 / Padding
    802.11 / LLC / SNAP / ARP is at 00:0a:b7:4b:9c:dd says 172.20.70.172 / Padding
    802.11 / LLC / SNAP / IP / ICMP echo-request 0 / Raw
    802.11 / LLC / SNAP / IP / ICMP echo-reply 0 / Raw
    >>> sniff(iface="eth1", prn=lambda x: x.show())
    ---[ Ethernet ]---
    dst       = 00:ae:f3:52:aa:d1
    src       = 00:02:15:37:a2:44
    type      = 0x800
    ---[ IP ]---
       version   = 4L
       ihl       = 5L
       tos       = 0x0
       len       = 84
       id        = 0
       flags     = DF
       frag      = 0L
       ttl       = 64
       proto     = ICMP
       chksum    = 0x3831
       src       = 192.168.5.21
       dst       = 66.35.250.151
       options   = ''
    ---[ ICMP ]---
          type      = echo-request
          code      = 0
          chksum    = 0x89d9
          id        = 0xc245
          seq       = 0x0
    ---[ Raw ]---
             load      = 'B\xf7i\xa9\x00\x04\x149\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !\x22#$%&\'()*+,-./01234567'
    ---[ Ethernet ]---
    dst       = 00:02:15:37:a2:44
    src       = 00:ae:f3:52:aa:d1
    type      = 0x800
    ---[ IP ]---
       version   = 4L
       ihl       = 5L
       tos       = 0x0
       len       = 84
       id        = 2070
       flags     = 
       frag      = 0L
       ttl       = 42
       proto     = ICMP
       chksum    = 0x861b
       src       = 66.35.250.151
       dst       = 192.168.5.21
       options   = ''
    ---[ ICMP ]---
          type      = echo-reply
          code      = 0
          chksum    = 0x91d9
          id        = 0xc245
          seq       = 0x0
    ---[ Raw ]---
             load      = 'B\xf7i\xa9\x00\x04\x149\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !\x22#$%&\'()*+,-./01234567'
    ---[ Padding ]---
                load      = '\n_\x00\x0b'
    >>> sniff(iface=["eth1","eth2"], prn=lambda x: x.sniffed_on+": "+x.summary())
    eth3: Ether / IP / ICMP 192.168.5.21 > 66.35.250.151 echo-request 0 / Raw  
    eth3: Ether / IP / ICMP 66.35.250.151 > 192.168.5.21 echo-reply 0 / Raw    
    eth2: Ether / IP / ICMP 192.168.5.22 > 66.35.250.152 echo-request 0 / Raw  
    eth2: Ether / IP / ICMP 66.35.250.152 > 192.168.5.22 echo-reply 0 / Raw
