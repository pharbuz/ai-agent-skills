=======================   ====================================================



Generating sets of packets
--------------------------

For the moment, we have only generated one packet. Let see how to specify sets of packets as easily. Each field of the whole packet (ever layers) can be a set. This implicitly defines a set of packets, generated using a kind of cartesian product between all the fields.

::

    >>> a=IP(dst="www.slashdot.org/30")
    >>> a
    <IP  dst=Net('www.slashdot.org/30') |>
    >>> [p for p in a]
    [<IP dst=66.35.250.148 |>, <IP dst=66.35.250.149 |>,
     <IP dst=66.35.250.150 |>, <IP dst=66.35.250.151 |>]
    >>> b=IP(ttl=[1,2,(5,9)])
    >>> b
    <IP ttl=[1, 2, (5, 9)] |>
    >>> [p for p in b]
    [<IP ttl=1 |>, <IP ttl=2 |>, <IP ttl=5 |>, <IP ttl=6 |>, 
     <IP ttl=7 |>, <IP ttl=8 |>, <IP ttl=9 |>]
    >>> c=TCP(dport=[80,443])
    >>> [p for p in a/c]
    [<IP frag=0 proto=TCP dst=66.35.250.148 |<TCP dport=80 |>>,
     <IP frag=0 proto=TCP dst=66.35.250.148 |<TCP dport=443 |>>,
     <IP frag=0 proto=TCP dst=66.35.250.149 |<TCP dport=80 |>>,
     <IP frag=0 proto=TCP dst=66.35.250.149 |<TCP dport=443 |>>,
     <IP frag=0 proto=TCP dst=66.35.250.150 |<TCP dport=80 |>>,
     <IP frag=0 proto=TCP dst=66.35.250.150 |<TCP dport=443 |>>,
     <IP frag=0 proto=TCP dst=66.35.250.151 |<TCP dport=80 |>>,
     <IP frag=0 proto=TCP dst=66.35.250.151 |<TCP dport=443 |>>]

Some operations (like building the string from a packet) can't work on a set of packets. In these cases, if you forgot to unroll your set of packets, only the first element of the list you forgot to generate will be used to assemble the packet.

On the other hand, it is possible to move sets of packets into a `PacketList` object, which provides some operations on lists of packets.

::

    >>> p = PacketList(a)
    >>> p
    <PacketList: TCP:0 UDP:0 ICMP:0 Other:4>
    >>> p = PacketList([p for p in a/c])
    >>> p
    <PacketList: TCP:8 UDP:0 ICMP:0 Other:0>

===============  ====================================================
Command          Effect
===============  ====================================================
summary()        displays a list of summaries of each packet 
nsummary()       same as previous, with the packet number 
conversations()  displays a graph of conversations 
show()           displays the preferred representation (usually nsummary()) 
filter()         returns a packet list filtered with a lambda function 
hexdump()        returns a hexdump of all packets 
hexraw()         returns a hexdump of the Raw layer of all packets 
padding()        returns a hexdump of packets with padding 
nzpadding()      returns a hexdump of packets with non-zero padding 
plot()           plots a lambda function applied to the packet list 
make\_table()    displays a table according to a lambda function 
===============  ====================================================



Sending packets
---------------

.. index::
   single: Sending packets, send
   
Now that we know how to manipulate packets. Let's see how to send them. The send() function will send packets at layer 3. That is to say, it will handle routing and layer 2 for you. The sendp() function will work at layer 2. It's up to you to choose the right interface and the right link layer protocol. send() and sendp() will also return sent packet list if return_packets=True is passed as parameter.

::

    >>> send(IP(dst="1.2.3.4")/ICMP())
    .
    Sent 1 packets.
    >>> sendp(Ether()/IP(dst="1.2.3.4",ttl=(1,4)), iface="eth1")
    ....
    Sent 4 packets.
    >>> sendp("I'm travelling on Ethernet", iface="eth1", loop=1, inter=0.2)
    ................^C
    Sent 16 packets.
    >>> sendp(rdpcap("/tmp/pcapfile")) # tcpreplay
    ...........
    Sent 11 packets.
    
    Returns packets sent by send()
    >>> send(IP(dst='127.0.0.1'), return_packets=True)
    .
    Sent 1 packets.
    <PacketList: TCP:0 UDP:0 ICMP:0 Other:1>

.. _multicast:

Multicast on layer 3: Scope Identifiers
---------------------------------------

.. index::
   single: Multicast

.. note:: This feature is only available since Scapy 2.6.0.

If you try to use multicast addresses (IPv4) or link-local addresses (IPv6), you'll notice that Scapy follows the routing table and takes the first entry. In order to specify which interface to use when looking through the routing table, Scapy supports scope identifiers (similar to RFC6874 but for both IPv6 and IPv4).

.. code:: python

    >>> conf.checkIPaddr = False  # answer IP will be != from the one we requested
    # send on interface 'eth0'
    >>> sr(IP(dst="224.0.0.1%eth0")/ICMP(), multi=True)
    >>> sr(IPv6(dst="ff02::1%eth0")/ICMPv6EchoRequest(), multi=True)

You can use both ``%eth0`` format or ``%15`` (the interface id) format. You can query those using ``conf.ifaces``.

.. note::

   Behind the scene, calling ``IP(dst="224.0.0.1%eth0")`` creates a ``ScopedIP`` object that contains ``224.0.0.1`` on the scope of the interface ``eth0``. If you are using an interface object (for instance ``conf.iface``), you can also craft that object. For instance::
        >>> pkt = IP(dst=ScopedIP("224.0.0.1", scope=conf.iface))/ICMP()

Fuzzing
-------

.. index::
   single: fuzz(), fuzzing

The function fuzz() is able to change any default value that is not to be calculated (like checksums) by an object whose value is random and whose type is adapted to the field. This enables quickly building fuzzing templates and sending them in a loop. In the following example, the IP layer is normal, and the UDP and NTP layers are fuzzed. The UDP checksum will be correct, the UDP destination port will be overloaded by NTP to be 123 and the NTP version will be forced to be 4. All the other ports will be randomized. Note: If you use fuzz() in IP layer, src and dst parameter won't be random so in order to do that use RandIP().::

    >>> send(IP(dst="target")/fuzz(UDP()/NTP(version=4)),loop=1)
    ................^C
    Sent 16 packets.

Injecting bytes
---------------

.. index::
   single: RawVal

In a packet, each field has a specific type. For instance, the length field of the IP packet ``len`` expects an integer. More on that later. If you're developing a PoC, there are times where you'll want to inject some value that doesn't fit that type. This is possible using ``RawVal``

.. code::

    >>> pkt = IP(len=RawVal(b"NotAnInteger"), src="127.0.0.1")
    >>> bytes(pkt)
    b'H\x00NotAnInt\x0f\xb3er\x00\x01\x00\x00@\x00\x00\x00\x7f\x00\x00\x01\x7f\x00\x00\x01\x00\x00'

Send and receive packets (sr)
-----------------------------

.. index::
   single: sr()

Now, let's try to do some fun things. The sr() function is for sending packets and receiving answers. The function returns a couple of packet and answers, and the unanswered packets. The function sr1() is a variant that only returns one packet that answered the packet (or the packet set) sent. The packets must be layer 3 packets (IP, ARP, etc.). The function srp() do the same for layer 2 packets (Ethernet, 802.3, etc.). If there is no response, a None value will be assigned instead when the timeout is reached.

::

    >>> p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
    Begin emission:
    ...Finished to send 1 packets.
    .*
    Received 5 packets, got 1 answers, remaining 0 packets
    >>> p
    <IP version=4L ihl=5L tos=0x0 len=39 id=15489 flags= frag=0L ttl=42 proto=ICMP
     chksum=0x51dd src=66.35.250.151 dst=192.168.5.21 options='' |<ICMP type=echo-reply
     code=0 chksum=0xee45 id=0x0 seq=0x0 |<Raw load='XXXXXXXXXXX'
     |<Padding load='\x00\x00\x00\x00' |>>>>
    >>> p.show()
    ---[ IP ]---
    version   = 4L
    ihl       = 5L
    tos       = 0x0
    len       = 39
    id        = 15489
    flags     = 
    frag      = 0L
    ttl       = 42
    proto     = ICMP
    chksum    = 0x51dd
    src       = 66.35.250.151
    dst       = 192.168.5.21
    options   = ''
    ---[ ICMP ]---
       type      = echo-reply
       code      = 0
       chksum    = 0xee45
       id        = 0x0
       seq       = 0x0
    ---[ Raw ]---
          load      = 'XXXXXXXXXXX'
    ---[ Padding ]---
             load      = '\x00\x00\x00\x00'
