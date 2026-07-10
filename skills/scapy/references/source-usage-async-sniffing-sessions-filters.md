
For even more control over displayed information we can use the ``sprintf()`` function::

    >>> pkts = sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
    192.168.1.100 -> 64.233.167.99
    
    64.233.167.99 -> 192.168.1.100
    
    192.168.1.100 -> 64.233.167.99
    
    192.168.1.100 -> 64.233.167.99
    'GET / HTTP/1.1\r\nHost: 64.233.167.99\r\nUser-Agent: Mozilla/5.0 
    (X11; U; Linux i686; en-US; rv:1.8.1.8) Gecko/20071022 Ubuntu/7.10 (gutsy)
    Firefox/2.0.0.8\r\nAccept: text/xml,application/xml,application/xhtml+xml,
    text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Language:
    en-us,en;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset:
    ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nKeep-Alive: 300\r\nConnection:
    keep-alive\r\nCache-Control: max-age=0\r\n\r\n'

We can sniff and do passive OS fingerprinting::

    >>> p
    <Ether dst=00:10:4b:b3:7d:4e src=00:40:33:96:7b:60 type=0x800 |<IP version=4L
     ihl=5L tos=0x0 len=60 id=61681 flags=DF frag=0L ttl=64 proto=TCP chksum=0xb85e
     src=192.168.8.10 dst=192.168.8.1 options='' |<TCP sport=46511 dport=80
     seq=2023566040L ack=0L dataofs=10L reserved=0L flags=SEC window=5840
     chksum=0x570c urgptr=0 options=[('Timestamp', (342940201L, 0L)), ('MSS', 1460),
     ('NOP', ()), ('SAckOK', ''), ('WScale', 0)] |>>>
    >>> load_module("p0f")
    >>> p0f(p)
    (1.0, ['Linux 2.4.2 - 2.4.14 (1)'])
    >>> a=sniff(prn=prnp0f)
    (1.0, ['Linux 2.4.2 - 2.4.14 (1)'])
    (1.0, ['Linux 2.4.2 - 2.4.14 (1)'])
    (0.875, ['Linux 2.4.2 - 2.4.14 (1)', 'Linux 2.4.10 (1)', 'Windows 98 (?)'])
    (1.0, ['Windows 2000 (9)'])

The number before the OS guess is the accuracy of the guess.

.. note:: When sniffing on several interfaces (e.g. ``iface=["eth0", ...]``), you can check what interface a packet was sniffed on by using the ``sniffed_on`` attribute, as shown in one of the examples above.

Asynchronous Sniffing
---------------------

.. index::
   single: AsyncSniffer()

.. note::
   Asynchronous sniffing is only available since **Scapy 2.4.3**

.. warning::
   Asynchronous sniffing does not necessarily improves performance (it's rather the opposite). If you want to sniff on multiple interfaces / socket, remember you can pass them all to a single `sniff()` call

It is possible to sniff asynchronously. This allows to stop the sniffer programmatically, rather than with ctrl^C.
It provides ``start()``, ``stop()`` and ``join()`` utils.

The basic usage would be:

.. code-block:: python

    >>> t = AsyncSniffer()
    >>> t.start()
    >>> print("hey")
    hey
    [...]
    >>> results = t.stop()

.. image:: graphics/animations/animation-scapy-asyncsniffer.svg

The ``AsyncSniffer`` class has a few useful keys, such as ``results`` (the packets collected) or ``running``, that can be used.
It accepts the same arguments than ``sniff()`` (in fact, their implementations are merged). For instance:

.. code-block:: python

    >>> t = AsyncSniffer(iface="enp0s3", count=200)
    >>> t.start()
    >>> t.join()  # this will hold until 200 packets are collected
    >>> results = t.results
    >>> print(len(results))
    200

Another example: using ``prn`` and ``store=False``

.. code-block:: python

    >>> t = AsyncSniffer(prn=lambda x: x.summary(), store=False, filter="tcp")
    >>> t.start()
    >>> time.sleep(20)
    >>> t.stop()

Advanced Sniffing - Sniffing Sessions
-------------------------------------

.. note::
   Sessions are only available since **Scapy 2.4.3**

``sniff()`` also provides **Sessions**, that allows to dissect a flow of packets seamlessly. For instance, you may want your ``sniff(prn=...)`` function to automatically defragment IP packets, before executing the ``prn``.

Scapy includes some basic Sessions, but it is possible to implement your own.
Available by default:

- :py:class:`~scapy.sessions.IPSession` -> *defragment IP packets* on-the-fly, to make a stream usable by ``prn``.
- :py:class:`~scapy.sessions.TCPSession` -> *defragment certain TCP protocols*. Currently supports:
   - HTTP 1.0
   - TLS
   - Kerberos
   - LDAP
   - SMB
   - DCE/RPC
   - Postgres
   - DOIP
   - and maybe other protocols if this page isn't up to date.
- :py:class:`~scapy.sessions.TLSSession` -> *matches TLS sessions* on the flow.
- :py:class:`~scapy.sessions.NetflowSession` -> *resolve Netflow V9 packets* from their NetflowFlowset information objects

Those sessions can be used using the ``session=`` parameter of ``sniff()``. Examples::

    >>> sniff(session=IPSession, iface="eth0")
    >>> sniff(session=TCPSession, prn=lambda x: x.summary(), store=False)
    >>> sniff(offline="file.pcap", session=NetflowSession)

.. note::
   To implement your own Session class, in order to support another flow-based protocol, start by copying a sample from `scapy/sessions.py <https://github.com/secdev/scapy/blob/master/scapy/sessions.py>`_
   Your custom ``Session`` class only needs to extend the :py:class:`~scapy.sessions.DefaultSession` class, and implement a ``process`` or a ``recv`` function, such as in the examples.


.. warning::
    The inner workings of ``Session`` is currently UNSTABLE: custom Sessions may break in the future.


How to use TCPSession to defragment TCP packets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The layer on which the decompression is applied must be immediately following the TCP layer. You need to implement a class function called ``tcp_reassemble`` that accepts the binary data, a metadata dictionary as argument and returns, when full, a packet. Let's study the (pseudo) example of TLS:

.. code::

    class TLS(Packet):
        [...]

        @classmethod
        def tcp_reassemble(cls, data, metadata, session):
            length = struct.unpack("!H", data[3:5])[0] + 5
            if len(data) == length:
                return TLS(data)


In this example, we first get the total length of the TLS payload announced by the TLS header, and we compare it to the length of the data. When the data reaches this length, the packet is complete and can be returned. When implementing ``tcp_reassemble``, it's usually a matter of detecting when a packet isn't missing anything else.

The ``data`` argument is bytes and the ``metadata`` argument is a dictionary which keys are as follow:

- ``metadata["pay_class"]``: the TCP payload class (here TLS)
- ``metadata.get("tcp_psh", False)``: will be present if the PUSH flag is set
- ``metadata.get("tcp_end", False)``: will be present if the END or RESET flag is set

If ``tcp_reassemble`` **returns any padding**, it will be kept for the next payload.

Filters
-------

.. index::
   single: filter, sprintf()
