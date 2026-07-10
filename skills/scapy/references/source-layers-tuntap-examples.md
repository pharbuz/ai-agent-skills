
            On Linux, this will be truncated to 16 bytes.

        :param bool mode_tun:
            If True, create as TUN interface (layer 3). If False, creates a TAP
            interface (layer 2).

            If not supplied, attempts to detect from the ``iface`` parameter.

        :param bool strip_packet_info:
            If True (default), any :py:class:`TunPacketInfo` will be stripped
            from the packet (so you get :py:class:`Ether` or :py:class:`IP`).

            Only Linux TUN interfaces have :py:class:`TunPacketInfo` available.

            This has no effect for interfaces that do not have
            :py:class:`TunPacketInfo` available.

        :param int default_read_size:
            Sets the default size that is read by
            :py:meth:`SuperSocket.raw_recv` and :py:meth:`SuperSocket.recv`.
            This defaults to :py:data:`scapy.data.MTU`.

            :py:class:`TunTapInterface` always adds overhead for
            :py:class:`TunPacketInfo` headers, if required.

.. py:class:: TunPacketInfo(Packet)

    Abstract class used to stack layer 3 protocols on a platform-specific
    header.

    See :py:class:`LinuxTunPacketInfo` for an example.

    .. py:method:: guess_payload_class(payload)

        The default implementation expects the field ``proto`` to be declared,
        with a value from :py:data:`scapy.data.ETHER_TYPES`.

Linux-specific structures
-------------------------

.. py:class:: LinuxTunPacketInfo(TunPacketInfo)

    Packet header used for Linux TUN packets.

    This is ``struct tun_pi``, declared in :file:`linux/if_tun.h`.

    .. py:attribute:: flags

        Flags to set on the packet. Only ``TUN_VNET_HDR`` is supported.

    .. py:attribute:: proto

        Layer 3 protocol number, per :py:data:`scapy.data.ETHER_TYPES`.

        Used by :py:meth:`TunTapPacketInfo.guess_payload_class`.

.. py:class:: LinuxTunIfReq(Packet)

    Internal "packet" used for ``TUNSETIFF`` requests on Linux.

    This is ``struct ifreq``, declared in :file:`linux/if.h`.
