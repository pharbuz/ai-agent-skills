
.. image:: graphics/graph_traceroute.png

If you have VPython installed, you also can have a 3D representation of the traceroute. With the right button, you can rotate the scene, with the middle button, you can zoom, with the left button, you can move the scene. If you click on a ball, it's IP will appear/disappear. If you Ctrl-click on a ball, ports 21, 22, 23, 25, 80 and 443 will be scanned and the result displayed::

    >>> res.trace3D()

.. image:: graphics/trace3d_1.png

.. image:: graphics/trace3d_2.png

Wireless frame injection
------------------------

.. index::
   single: FakeAP, Dot11, wireless, WLAN

.. note::
   See the :doc:`TroubleShooting <troubleshooting>` section for more information on the usage of Monitor mode among Scapy.

Provided that your wireless card and driver are correctly configured for frame injection, you can have a kind of FakeAP::

    >>> sendp(RadioTap()/
              Dot11(addr1="ff:ff:ff:ff:ff:ff",
                    addr2="00:01:02:03:04:05",
                    addr3="00:01:02:03:04:05")/
              Dot11Beacon(cap="ESS", timestamp=1)/
              Dot11Elt(ID="SSID", info=RandString(RandNum(1,50)))/
              Dot11EltRates(rates=[130, 132, 11, 22])/
              Dot11Elt(ID="DSset", info="\x03")/
              Dot11Elt(ID="TIM", info="\x00\x01\x00\x00"),
              iface="mon0", loop=1)

Depending on the driver, the commands needed to get a working frame injection interface may vary. You may also have to replace the first pseudo-layer (in the example ``RadioTap()``) by ``PrismHeader()``, or by a proprietary pseudo-layer, or even to remove it.


Simple one-liners
=================


ACK Scan
--------

Using Scapy's powerful packet crafting facilities we can quick replicate classic TCP Scans.
For example, the following string will be sent to simulate an ACK Scan::

    >>> ans, unans = sr(IP(dst="www.slashdot.org")/TCP(dport=[80,666],flags="A"))

We can find unfiltered ports in answered packets::

    >>> for s,r in ans:
    ...     if s[TCP].dport == r[TCP].sport:
    ...        print("%d is unfiltered" % s[TCP].dport)

Similarly, filtered ports can be found with unanswered packets::

    >>> for s in unans:     
    ...     print("%d is filtered" % s[TCP].dport)


Xmas Scan
---------

Xmas Scan can be launched using the following command::

    >>> ans, unans = sr(IP(dst="192.168.1.1")/TCP(dport=666,flags="FPU") )

Checking RST responses will reveal closed ports on the target. 

IP Scan
-------

A lower level IP Scan can be used to enumerate supported protocols::

    >>> ans, unans = sr(IP(dst="192.168.1.1",proto=(0,255))/"SCAPY",retry=2)


ARP Ping
--------

The fastest way to discover hosts on a local ethernet network is to use the ARP Ping method::

    >>> ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"), timeout=2)

Answers can be reviewed with the following command::

    >>> ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

Scapy also includes a built-in arping() function which performs similar to the above two commands:

    >>> arping("192.168.1.0/24")


ICMP Ping
---------

Classical ICMP Ping can be emulated using the following command::

    >>> ans, unans = sr(IP(dst="192.168.1.0/24")/ICMP(), timeout=3)

Information on live hosts can be collected with the following request::

    >>> ans.summary(lambda s,r: r.sprintf("%IP.src% is alive") )


TCP Ping
--------

In cases where ICMP echo requests are blocked, we can still use various TCP Pings such as TCP SYN Ping below::

    >>> ans, unans = sr( IP(dst="192.168.1.0/24")/TCP(dport=80,flags="S") )

Any response to our probes will indicate a live host. We can collect results with the following command::

    >>> ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") )


UDP Ping
--------

If all else fails there is always UDP Ping which will produce ICMP Port unreachable errors from live hosts. Here you can pick any port which is most likely to be closed, such as port 0::

    >>> ans, unans = sr( IP(dst="192.168.*.1-10")/UDP(dport=0) )

Once again, results can be collected with this command::

    >>> ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") )


DNS Requests
------------

**IPv4 (A) request:**

This will perform a DNS request looking for IPv4 addresses

    >>> ans = sr1(IP(dst="8.8.8.8")/UDP(sport=RandShort(), dport=53)/DNS(rd=1,qd=DNSQR(qname="secdev.org",qtype="A")))
    >>> ans.an[0].rdata
    '217.25.178.5'

**SOA request:**

    >>> ans = sr1(IP(dst="8.8.8.8")/UDP(sport=RandShort(), dport=53)/DNS(rd=1,qd=DNSQR(qname="secdev.org",qtype="SOA")))
    >>> ans.an[0].mname
    b'dns.ovh.net.'
    >>> ans.an[0].rname
    b'tech.ovh.net.'

**MX request:**

    >>> ans = sr1(IP(dst="8.8.8.8")/UDP(sport=RandShort(), dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com",qtype="MX")))
    >>> results = [x.exchange for x in ans.an]
    >>> results
    [b'alt1.aspmx.l.google.com.',
     b'alt4.aspmx.l.google.com.',
     b'aspmx.l.google.com.',
     b'alt2.aspmx.l.google.com.',
     b'alt3.aspmx.l.google.com.']


Classical attacks
