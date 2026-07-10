

UDP traceroute
^^^^^^^^^^^^^^

Tracerouting an UDP application like we do with TCP is not 
reliable, because there's no handshake. We need to give an applicative payload (DNS, ISAKMP, 
NTP, etc.) to deserve an answer::

    >>> res, unans = sr(IP(dst="target", ttl=(1,20))
                  /UDP()/DNS(qd=DNSQR(qname="test.com")) 

We can visualize the results as a list of routers::

    >>> res.make_table(lambda s,r: (s.dst, s.ttl, r.src))


DNS traceroute
^^^^^^^^^^^^^^

We can perform a DNS traceroute by specifying a complete packet in ``l4`` parameter of ``traceroute()`` function::

    >>> ans, unans = traceroute("4.2.2.1",l4=UDP(sport=RandShort())/DNS(qd=DNSQR(qname="thesprawl.org")))
    Begin emission:
    ..*....******...******.***...****Finished to send 30 packets.
    *****...***...............................
    Received 75 packets, got 28 answers, remaining 2 packets
       4.2.2.1:udp53      
    1  192.168.1.1     11 
    4  68.86.90.162    11 
    5  4.79.43.134     11 
    6  4.79.43.133     11 
    7  4.68.18.62      11 
    8  4.68.123.6      11 
    9  4.2.2.1            
    ...


Etherleaking 
------------

::

    >>> sr1(IP(dst="172.16.1.232")/ICMP()) 
    <IP src=172.16.1.232 proto=1 [...] |<ICMP code=0 type=0 [...]| 
    <Padding load=’0O\x02\x01\x00\x04\x06public\xa2B\x02\x02\x1e’ |>>> 

ICMP leaking
------------ 

This was a Linux 2.0 bug:: 

    >>> sr1(IP(dst="172.16.1.1", options="\x02")/ICMP()) 
    <IP src=172.16.1.1 [...] |<ICMP code=0 type=12 [...] | 
    <IPerror src=172.16.1.24 options=’\x02\x00\x00\x00’ [...] | 
    <ICMPerror code=0 type=8 id=0x0 seq=0x0 chksum=0xf7ff | 
    <Padding load=’\x00[...]\x00\x1d.\x00V\x1f\xaf\xd9\xd4;\xca’ |>>>>> 


VLAN hopping 
------------

In very specific conditions, a double 802.1q encapsulation will 
make a packet jump to another VLAN::
 
    >>> sendp(Ether()/Dot1Q(vlan=2)/Dot1Q(vlan=7)/IP(dst=target)/ICMP()) 


Wireless sniffing
-----------------

The following command will display information similar to most wireless sniffers::

>>> sniff(iface="ath0", prn=lambda x:x.sprintf("{Dot11Beacon:%Dot11.addr3%\t%Dot11Beacon.info%\t%PrismHeader.channel%\t%Dot11Beacon.cap%}"))

.. note::
    On Windows and OSX, you will need to also use `monitor=True`, which only works on scapy>2.4.0 (2.4.0dev+). This might require you to manually toggle monitor mode.

The above command will produce output similar to the one below::

    00:00:00:01:02:03 netgear      6L   ESS+privacy+PBCC
    11:22:33:44:55:66 wireless_100 6L   short-slot+ESS+privacy
    44:55:66:00:11:22 linksys      6L   short-slot+ESS+privacy
    12:34:56:78:90:12 NETGEAR      6L   short-slot+ESS+privacy+short-preamble


Recipes 
=======

Simplistic ARP Monitor
----------------------

This program uses the ``sniff()`` callback (parameter prn). The store parameter is set to 0 so that the ``sniff()`` function will not store anything (as it would do otherwise) and thus can run forever. The filter parameter is used for better performances on high load : the filter is applied inside the kernel and Scapy will only see ARP traffic.

::

    #! /usr/bin/env python
    from scapy.all import *
    
    def arp_monitor_callback(pkt):
        if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
            return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")
    
    sniff(prn=arp_monitor_callback, filter="arp", store=0)

Identifying rogue DHCP servers on your LAN 
-------------------------------------------

.. index::
   single: DHCP

Problem
^^^^^^^

You suspect that someone has installed an additional, unauthorized DHCP server on your LAN -- either unintentionally or maliciously. 
Thus you want to check for any active DHCP servers and identify their IP and MAC addresses.  

Solution
^^^^^^^^

Use Scapy to send a DHCP discover request and analyze the replies::

    >>> conf.checkIPaddr = False
    >>> hw = get_if_hwaddr(conf.iface)
    >>> dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=hw)/DHCP(options=[("message-type","discover"),"end"])
    >>> ans, unans = srp(dhcp_discover, multi=True)      # Press CTRL-C after several seconds
    Begin emission:
    Finished to send 1 packets.
    .*...*..
    Received 8 packets, got 2 answers, remaining 0 packets

In this case we got 2 replies, so there were two active DHCP servers on the test network::

    >>> ans.summary()
    Ether / IP / UDP 0.0.0.0:bootpc > 255.255.255.255:bootps / BOOTP / DHCP ==> Ether / IP / UDP 192.168.1.1:bootps > 255.255.255.255:bootpc / BOOTP / DHCP
    Ether / IP / UDP 0.0.0.0:bootpc > 255.255.255.255:bootps / BOOTP / DHCP ==> Ether / IP / UDP 192.168.1.11:bootps > 255.255.255.255:bootpc / BOOTP / DHCP

We are only interested in the MAC and IP addresses of the replies: 

    >>> for p in ans: print(p[1][Ether].src, p[1][IP].src)
    ...
    00:de:ad:be:ef:00 192.168.1.1
    00:11:11:22:22:33 192.168.1.11

Discussion
^^^^^^^^^^

We specify ``multi=True`` to make Scapy wait for more answer packets after the first response is received.
This is also the reason why we can't use the more convenient ``dhcp_request()`` function and have to construct the DHCP packet manually: ``dhcp_request()`` uses ``srp1()`` for sending and receiving and thus would immediately return after the first answer packet. 

Moreover, Scapy normally makes sure that replies come from the same IP address the stimulus was sent to. But our DHCP packet is sent to the IP broadcast address (255.255.255.255) and any answer packet will have the IP address of the replying DHCP server as its source IP address (e.g. 192.168.1.1). Because these IP addresses don't match, we have to disable Scapy's check with ``conf.checkIPaddr = False`` before sending the stimulus.  

See also
^^^^^^^^

http://en.wikipedia.org/wiki/Rogue_DHCP



Firewalking
