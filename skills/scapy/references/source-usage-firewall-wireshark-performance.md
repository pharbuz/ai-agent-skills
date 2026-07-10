-----------

TTL decrementation after a filtering operation 
only not filtered packets generate an ICMP TTL exceeded 

    >>> ans, unans = sr(IP(dst="172.16.4.27", ttl=16)/TCP(dport=(1,1024)))
    >>> for s,r in ans:
    ...     if r.haslayer(ICMP) and r.payload.type == 11:
    ...         print(s.dport)

Find subnets on a multi-NIC firewall 
only his own NIC’s IP are reachable with this TTL:: 

    >>> ans, unans = sr(IP(dst="172.16.5/24", ttl=15)/TCP())
    >>> for i in unans: print(i.dst)


TCP Timestamp Filtering
------------------------

Problem
^^^^^^^

Many firewalls include a rule to drop TCP packets that do not have TCP Timestamp option set which is a common occurrence in popular port scanners.

Solution
^^^^^^^^

To allow Scapy to reach target destination additional options must be used::

    >>> sr1(IP(dst="72.14.207.99")/TCP(dport=80,flags="S",options=[('Timestamp',(0,0))]))



Viewing packets with Wireshark
------------------------------

.. index::
   single: wireshark()

Problem
^^^^^^^

You have generated or sniffed some packets with Scapy.

Now you want to view them with `Wireshark <https://www.wireshark.org>`_, because
of its advanced packet dissection capabilities.

Solution
^^^^^^^^

That's what :py:func:`wireshark` is for!

.. code-block:: python3

    # First, generate some packets...
    packets = IP(src="192.0.2.9", dst=Net("192.0.2.10/30"))/ICMP()

    # Show them with Wireshark
    wireshark(packets)

Wireshark will start in the background, and show your packets.
 
Discussion
^^^^^^^^^^

.. py:function:: wireshark(pktlist, ...)

    With a :py:class:`Packet` or :py:class:`PacketList`, serialises your
    packets, and streams this into Wireshark via ``stdin`` as if it were a
    capture device.

    Because this uses ``pcap`` format to serialise the packets, there are some
    limitations:

    * Packets must be all of the same ``linktype``.

      For example, you can't mix :py:class:`Ether` and :py:class:`IP` at the
      top layer.

    * Packets must have an assigned (and supported) ``DLT_*`` constant for the
      ``linktype``.  An unsupported ``linktype`` is replaced with ``DLT_EN10MB``
      (Ethernet), and will display incorrectly in Wireshark.

      For example, can't pass a bare :py:class:`ICMP` packet, but you can send
      it as a payload of an :py:class:`IP` or :py:class:`IPv6` packet.

    With a filename (passed as a string), this loads the given file in
    Wireshark. This needs to be in a format that Wireshark supports.

    You can tell Scapy where to find the Wireshark executable by changing the
    ``conf.prog.wireshark`` configuration setting.

    This accepts the same extra parameters as :py:func:`tcpdump`.

.. seealso::

    :py:class:`WiresharkSink`
        A :ref:`PipeTools sink <pipetools>` for live-streaming packets.

    :manpage:`wireshark(1)`
        Additional description of Wireshark's functionality, and its
        command-line arguments.

    `Wireshark's website`__
        For up-to-date releases of Wireshark.

    `Wireshark Protocol Reference`__
        Contains detailed information about Wireshark's protocol dissectors, and
        reference documentation for various network protocols.

__ https://www.wireshark.org
__ https://wiki.wireshark.org/ProtocolReference

Performance of Scapy
--------------------

Problem
^^^^^^^

Scapy dissects slowly and/or misses packets under heavy loads.

.. note::

    Please bear in mind that Scapy is not designed to be blazing fast, but rather easily hackable & extensible. The packet model makes it VERY easy to create new layers, compared to pretty much all other alternatives, but comes with a performance cost. Of course, we still do our best to make Scapy as fast as possible, but it's not the absolute main goal.

Solution
^^^^^^^^

There are quite a few ways of speeding up scapy's dissection. You can use all of them

- **Using a BPF filter**: The OS is faster than Scapy. If you make the OS filter the packets instead of Scapy, it will only handle a fraction of the load. Use the ``filter=`` argument of the :py:func:`~scapy.sendrecv.sniff` function.
- **By disabling layers you don't use**: If you are not using some layers, why dissect them? You can let Scapy know which layers to dissect and all the others will simply be parsed as ``Raw``. This comes with a great performance boost but requires you to know what you're doing.

.. code:: python

    # Enable filtering: only Ether, IP and ICMP will be dissected
    conf.layers.filter([Ether, IP, ICMP])
    # Disable filtering: restore everything to normal
    conf.layers.unfilter()

Very slow start because of big routes
-------------------------------------

Problem
^^^^^^^

Scapy takes ages to start because you have very big routing tables.

Solution
^^^^^^^^

Disable the auto-loading of the routing tables:

**CLI:** in ``~/.config/scapy/prestart.py`` add:

.. code:: python

    conf.route_autoload = False
    conf.route6_autoload = False
