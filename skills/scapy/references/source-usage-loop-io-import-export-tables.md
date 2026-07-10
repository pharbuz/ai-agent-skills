
Demo of both bpf filter and sprintf() method::

    >>> a=sniff(filter="tcp and ( port 25 or port 110 )",
     prn=lambda x: x.sprintf("%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%  %2s,TCP.flags% : %TCP.payload%"))
    192.168.8.10:47226 -> 213.228.0.14:110   S : 
    213.228.0.14:110 -> 192.168.8.10:47226  SA : 
    192.168.8.10:47226 -> 213.228.0.14:110   A : 
    213.228.0.14:110 -> 192.168.8.10:47226  PA : +OK <13103.1048117923@pop2-1.free.fr>
    
    192.168.8.10:47226 -> 213.228.0.14:110   A : 
    192.168.8.10:47226 -> 213.228.0.14:110  PA : USER toto
    
    213.228.0.14:110 -> 192.168.8.10:47226   A : 
    213.228.0.14:110 -> 192.168.8.10:47226  PA : +OK 
    
    192.168.8.10:47226 -> 213.228.0.14:110   A : 
    192.168.8.10:47226 -> 213.228.0.14:110  PA : PASS tata
    
    213.228.0.14:110 -> 192.168.8.10:47226  PA : -ERR authorization failed
    
    192.168.8.10:47226 -> 213.228.0.14:110   A : 
    213.228.0.14:110 -> 192.168.8.10:47226  FA : 
    192.168.8.10:47226 -> 213.228.0.14:110  FA : 
    213.228.0.14:110 -> 192.168.8.10:47226   A : 

Send and receive in a loop 
--------------------------

.. index::
   single: srloop()

Here is an example of a (h)ping-like functionality : you always send the same set of packets to see if something change::

    >>> srloop(IP(dst="www.target.com/30")/TCP())
    RECV 1: Ether / IP / TCP 192.168.11.99:80 > 192.168.8.14:20 SA / Padding
    fail 3: IP / TCP 192.168.8.14:20 > 192.168.11.96:80 S
            IP / TCP 192.168.8.14:20 > 192.168.11.98:80 S
            IP / TCP 192.168.8.14:20 > 192.168.11.97:80 S
    RECV 1: Ether / IP / TCP 192.168.11.99:80 > 192.168.8.14:20 SA / Padding
    fail 3: IP / TCP 192.168.8.14:20 > 192.168.11.96:80 S
            IP / TCP 192.168.8.14:20 > 192.168.11.98:80 S
            IP / TCP 192.168.8.14:20 > 192.168.11.97:80 S
    RECV 1: Ether / IP / TCP 192.168.11.99:80 > 192.168.8.14:20 SA / Padding
    fail 3: IP / TCP 192.168.8.14:20 > 192.168.11.96:80 S
            IP / TCP 192.168.8.14:20 > 192.168.11.98:80 S
            IP / TCP 192.168.8.14:20 > 192.168.11.97:80 S
    RECV 1: Ether / IP / TCP 192.168.11.99:80 > 192.168.8.14:20 SA / Padding
    fail 3: IP / TCP 192.168.8.14:20 > 192.168.11.96:80 S
            IP / TCP 192.168.8.14:20 > 192.168.11.98:80 S
            IP / TCP 192.168.8.14:20 > 192.168.11.97:80 S

.. _import-export:

Importing and Exporting Data
----------------------------
PCAP
^^^^

It is often useful to save capture packets to pcap file for use at later time or with different applications::

    >>> wrpcap("temp.cap",pkts)

To restore previously saved pcap file:

    >>> pkts = rdpcap("temp.cap")

or

    >>> pkts = sniff(offline="temp.cap")

Hexdump
^^^^^^^

Scapy allows you to export recorded packets in various hex formats.

Use ``hexdump()`` to display one or more packets using classic hexdump format::

    >>> hexdump(pkt)
    0000   00 50 56 FC CE 50 00 0C  29 2B 53 19 08 00 45 00   .PV..P..)+S...E.
    0010   00 54 00 00 40 00 40 01  5A 7C C0 A8 19 82 04 02   .T..@.@.Z|......
    0020   02 01 08 00 9C 90 5A 61  00 01 E6 DA 70 49 B6 E5   ......Za....pI..
    0030   08 00 08 09 0A 0B 0C 0D  0E 0F 10 11 12 13 14 15   ................
    0040   16 17 18 19 1A 1B 1C 1D  1E 1F 20 21 22 23 24 25   .......... !"#$%
    0050   26 27 28 29 2A 2B 2C 2D  2E 2F 30 31 32 33 34 35   &'()*+,-./012345
    0060   36 37                                              67

Hexdump above can be reimported back into Scapy using ``import_hexcap()``::

    >>> pkt_hex = Ether(import_hexcap())
    0000   00 50 56 FC CE 50 00 0C  29 2B 53 19 08 00 45 00   .PV..P..)+S...E.
    0010   00 54 00 00 40 00 40 01  5A 7C C0 A8 19 82 04 02   .T..@.@.Z|......
    0020   02 01 08 00 9C 90 5A 61  00 01 E6 DA 70 49 B6 E5   ......Za....pI..
    0030   08 00 08 09 0A 0B 0C 0D  0E 0F 10 11 12 13 14 15   ................
    0040   16 17 18 19 1A 1B 1C 1D  1E 1F 20 21 22 23 24 25   .......... !"#$%
    0050   26 27 28 29 2A 2B 2C 2D  2E 2F 30 31 32 33 34 35   &'()*+,-./012345
    0060   36 37                                              67
    >>> pkt_hex
    <Ether  dst=00:50:56:fc:ce:50 src=00:0c:29:2b:53:19 type=0x800 |<IP  version=4L 
    ihl=5L tos=0x0 len=84 id=0 flags=DF frag=0L ttl=64 proto=icmp chksum=0x5a7c 
    src=192.168.25.130 dst=4.2.2.1 options='' |<ICMP  type=echo-request code=0 
    chksum=0x9c90 id=0x5a61 seq=0x1 |<Raw  load='\xe6\xdapI\xb6\xe5\x08\x00\x08\t\n
    \x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e
    \x1f !"#$%&\'()*+,-./01234567' |>>>>

Binary string
^^^^^^^^^^^^^

You can also convert entire packet into a binary string using the ``raw()`` function::

    >>> pkts = sniff(count = 1)
    >>> pkt = pkts[0]
    >>> pkt
    <Ether  dst=00:50:56:fc:ce:50 src=00:0c:29:2b:53:19 type=0x800 |<IP  version=4L 
    ihl=5L tos=0x0 len=84 id=0 flags=DF frag=0L ttl=64 proto=icmp chksum=0x5a7c 
    src=192.168.25.130 dst=4.2.2.1 options='' |<ICMP  type=echo-request code=0 
    chksum=0x9c90 id=0x5a61 seq=0x1 |<Raw  load='\xe6\xdapI\xb6\xe5\x08\x00\x08\t\n
    \x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e
    \x1f !"#$%&\'()*+,-./01234567' |>>>>
    >>> pkt_raw = raw(pkt)
    >>> pkt_raw
    '\x00PV\xfc\xceP\x00\x0c)+S\x19\x08\x00E\x00\x00T\x00\x00@\x00@\x01Z|\xc0\xa8
    \x19\x82\x04\x02\x02\x01\x08\x00\x9c\x90Za\x00\x01\xe6\xdapI\xb6\xe5\x08\x00
    \x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b
    \x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

We can reimport the produced binary string by selecting the appropriate first layer (e.g. ``Ether()``).

    >>> new_pkt = Ether(pkt_raw)
    >>> new_pkt
    <Ether  dst=00:50:56:fc:ce:50 src=00:0c:29:2b:53:19 type=0x800 |<IP  version=4L 
    ihl=5L tos=0x0 len=84 id=0 flags=DF frag=0L ttl=64 proto=icmp chksum=0x5a7c 
    src=192.168.25.130 dst=4.2.2.1 options='' |<ICMP  type=echo-request code=0 
    chksum=0x9c90 id=0x5a61 seq=0x1 |<Raw  load='\xe6\xdapI\xb6\xe5\x08\x00\x08\t\n
    \x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e
    \x1f !"#$%&\'()*+,-./01234567' |>>>>

Making tables
-------------

.. index::
   single: tables, make_table()

Now we have a demonstration of the ``make_table()`` presentation function. It takes a list as parameter, and a function who returns a 3-uple. The first element is the value on the x axis from an element of the list, the second is about the y value and the third is the value that we want to see at coordinates (x,y). The result is a table. This function has 2 variants, ``make_lined_table()`` and ``make_tex_table()`` to copy/paste into your LaTeX pentest report. Those functions are available as methods of a result object :

Here we can see a multi-parallel traceroute (Scapy already has a multi TCP traceroute function. See later)::

    >>> ans, unans = sr(IP(dst="www.test.fr/30", ttl=(1,6))/TCP())
    Received 49 packets, got 24 answers, remaining 0 packets
    >>> ans.make_table( lambda s,r: (s.dst, s.ttl, r.src) )
      216.15.189.192  216.15.189.193  216.15.189.194  216.15.189.195  
    1 192.168.8.1     192.168.8.1     192.168.8.1     192.168.8.1     
    2 81.57.239.254   81.57.239.254   81.57.239.254   81.57.239.254   
    3 213.228.4.254   213.228.4.254   213.228.4.254   213.228.4.254   
    4 213.228.3.3     213.228.3.3     213.228.3.3     213.228.3.3     
    5 193.251.254.1   193.251.251.69  193.251.254.1   193.251.251.69  
    6 193.251.241.174 193.251.241.178 193.251.241.174 193.251.241.178 

Here is a more complex example to distinguish machines or their IP stacks from their IPID field. We can see that 172.20.80.200:22 is answered by the same IP stack as 172.20.80.201 and that 172.20.80.197:25 is not answered by the same IP stack as other ports on the same IP.

::
