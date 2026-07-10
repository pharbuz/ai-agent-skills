
    server = HTTP_Server.spawn(
        port=8080,
        iface="eth0",
        mech=HTTP_AUTH_MECHS.NTLM,
        ssp=NTLMSSP(IDENTITIES={"user": MD4le("password")}),
    )

Or **basic auth**:

.. code:: python

    server = HTTP_Server.spawn(
        port=8080,
        iface="eth0",
        mech=HTTP_AUTH_MECHS.BASIC,
        BASIC_IDENTITIES={"user": MD4le("password")},
    )

- ``TCP_client.tcplink``:

Send an HTTPRequest to ``www.secdev.org`` and write the result in a file:

.. code:: python

    load_layer("http")
    req = HTTP()/HTTPRequest(
        Accept_Encoding=b'gzip, deflate',
        Cache_Control=b'no-cache',
        Connection=b'keep-alive',
        Host=b'www.secdev.org',
        Pragma=b'no-cache'
    )
    a = TCP_client.tcplink(HTTP, "www.secdev.org", 80)
    answer = a.sr1(req)
    a.close()
    with open("www.secdev.org.html", "wb") as file:
        file.write(answer.load)

``TCP_client.tcplink`` makes it feel like it only received one packet, but in reality it was recombined in ``TCPSession``.
If you performed a plain ``sniff()``, you would have seen those packets.

- ``sniff()``:

Dissect a pcap which contains a JPEG image that was sent over HTTP using chunks. This is able to reconstruct all HTTP streams in parallel.

.. note::

    The ``http_chunk.pcap.gz`` file is available in ``scapy/test/pcaps``

.. code:: python

    load_layer("http")
    pkts = sniff(offline="http_chunk.pcap.gz", session=TCPSession)
    # a[29] is the HTTPResponse
    with open("image.jpg", "wb") as file:
        file.write(pkts[29].load)


HTTP 2.X
--------

The HTTP 2 documentation is available as a Jupyter notebook over here: `HTTP 2 Tuto <https://github.com/secdev/scapy/blob/master/doc/notebooks/HTTP_2_Tuto.ipynb>`_
