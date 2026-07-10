# Source: usage

*****
Usage
*****

Starting Scapy
==============

Scapy's interactive shell is run in a terminal session. Root privileges are needed to
send the packets, so we're using ``sudo`` here::
  
    $ sudo scapy -H
    Welcome to Scapy (2.4.0)
    >>> 

On Windows, please open a command prompt (``cmd.exe``) and make sure that you have 
administrator privileges::

    C:\>scapy
    Welcome to Scapy (2.4.0)
    >>>

If you do not have all optional packages installed, Scapy will inform you that 
some features will not be available:: 
                                 
    INFO: Can't import python matplotlib wrapper. Won't be able to plot.
    INFO: Can't import PyX. Won't be able to use psdump() or pdfdump().

The basic features of sending and receiving packets should still work, though. 

Interactive tutorial
====================

This section will show you several of Scapy's features with Python 2.
Just open a Scapy session as shown above and try the examples yourself.

.. note:: You can configure the Scapy terminal by modifying the ``~/.config/scapy/prestart.py`` file.

First steps
-----------

Let's build a packet and play with it::

    >>> a=IP(ttl=10) 
    >>> a 
    < IP ttl=10 |> 
    >>> a.src 
    ’127.0.0.1’ 
    >>> a.dst="192.168.1.1" 
    >>> a 
    < IP ttl=10 dst=192.168.1.1 |> 
    >>> a.src 
    ’192.168.8.14’ 
    >>> del(a.ttl) 
    >>> a 
    < IP dst=192.168.1.1 |> 
    >>> a.ttl 
    64 

Stacking layers
---------------

The ``/`` operator has been used as a composition operator between two layers. When doing so, the lower layer can have one or more of its defaults fields overloaded according to the upper layer. (You still can give the value you want). A string can be used as a raw layer.

::

    >>> IP()
    <IP |>
    >>> IP()/TCP()
    <IP frag=0 proto=TCP |<TCP |>>
    >>> Ether()/IP()/TCP()
    <Ether type=0x800 |<IP frag=0 proto=TCP |<TCP |>>>
    >>> IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"
    <IP frag=0 proto=TCP |<TCP |<Raw load='GET / HTTP/1.0\r\n\r\n' |>>>
    >>> Ether()/IP()/IP()/UDP()
    <Ether type=0x800 |<IP frag=0 proto=IP |<IP frag=0 proto=UDP |<UDP |>>>>
    >>> IP(proto=55)/TCP()
    <IP frag=0 proto=55 |<TCP |>>


.. image:: graphics/fieldsmanagement.png
   :scale: 90

Each packet can be built or dissected (note: in Python ``_`` (underscore) is the latest result)::

    >>> raw(IP())
    'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xe7\x7f\x00\x00\x01\x7f\x00\x00\x01'
    >>> IP(_)
    <IP version=4L ihl=5L tos=0x0 len=20 id=1 flags= frag=0L ttl=64 proto=IP
     chksum=0x7ce7 src=127.0.0.1 dst=127.0.0.1 |>
    >>>  a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"
    >>>  hexdump(a)   
    00 02 15 37 A2 44 00 AE F3 52 AA D1 08 00 45 00  ...7.D...R....E.
    00 43 00 01 00 00 40 06 78 3C C0 A8 05 15 42 23  .C....@.x<....B#
    FA 97 00 14 00 50 00 00 00 00 00 00 00 00 50 02  .....P........P.
    20 00 BB 39 00 00 47 45 54 20 2F 69 6E 64 65 78   ..9..GET /index
    2E 68 74 6D 6C 20 48 54 54 50 2F 31 2E 30 20 0A  .html HTTP/1.0 .
    0A                                               .
    >>> b=raw(a)
    >>> b
    '\x00\x02\x157\xa2D\x00\xae\xf3R\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00@\x06x<\xc0
     \xa8\x05\x15B#\xfa\x97\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00
     \xbb9\x00\x00GET /index.html HTTP/1.0 \n\n'
    >>> c=Ether(b)
    >>> c
    <Ether dst=00:02:15:37:a2:44 src=00:ae:f3:52:aa:d1 type=0x800 |<IP version=4L
     ihl=5L tos=0x0 len=67 id=1 flags= frag=0L ttl=64 proto=TCP chksum=0x783c
     src=192.168.5.21 dst=66.35.250.151 options='' |<TCP sport=20 dport=80 seq=0L
     ack=0L dataofs=5L reserved=0L flags=S window=8192 chksum=0xbb39 urgptr=0
     options=[] |<Raw load='GET /index.html HTTP/1.0 \n\n' |>>>>

We see that a dissected packet has all its fields filled. That's because I consider that each field has its value imposed by the original string. If this is too verbose, the method hide_defaults() will delete every field that has the same value as the default::

    >>> c.hide_defaults()
    >>> c
    <Ether dst=00:0f:66:56:fa:d2 src=00:ae:f3:52:aa:d1 type=0x800 |<IP ihl=5L len=67
     frag=0 proto=TCP chksum=0x783c src=192.168.5.21 dst=66.35.250.151 |<TCP dataofs=5L
     chksum=0xbb39 options=[] |<Raw load='GET /index.html HTTP/1.0 \n\n' |>>>>

Reading PCAP files
------------------

.. index::
   single: rdpcap()

You can read packets from a pcap file and write them to a pcap file. 

    >>> a=rdpcap("/spare/captures/isakmp.cap")
    >>> a
    <isakmp.cap: UDP:721 TCP:0 ICMP:0 Other:0>

Graphical dumps (PDF, PS)
-------------------------

.. index::
   single: pdfdump(), psdump()

If you have PyX installed, you can make a graphical PostScript/PDF dump of a packet or a list of packets (see the ugly PNG image below. PostScript/PDF are far better quality...)::

    >>> a[423].pdfdump(layer_shift=1)
    >>> a[423].psdump("/tmp/isakmp_pkt.eps",layer_shift=1)
    
.. image:: graphics/isakmp_dump.png



=======================   ====================================================
Command                   Effect
=======================   ====================================================
raw(pkt)                  assemble the packet
hexdump(pkt)              have a hexadecimal dump 
ls(pkt)                   have the list of fields values 
pkt.summary()             for a one-line summary 
pkt.show()                for a developed view of the packet 
pkt.show2()               same as show but on the assembled packet (checksum is calculated, for instance) 
pkt.sprintf()             fills a format string with fields values of the packet 
pkt.decode_payload_as()   changes the way the payload is decoded 
pkt.psdump()              draws a PostScript diagram with explained dissection 
pkt.pdfdump()             draws a PDF with explained dissection 
pkt.command()             return a Scapy command that can generate the packet 
pkt.json()                return a JSON string representing the packet
