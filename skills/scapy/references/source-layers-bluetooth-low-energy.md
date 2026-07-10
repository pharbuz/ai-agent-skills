
.. code-block:: console

   $ hcitool dev
   Devices:
	   hci0	xx:xx:xx:xx:xx:xx


.. _hci-open:

Opening a HCI socket
--------------------

The first step in Scapy is to open a HCI socket to the underlying Bluetooth
device:

.. code-block:: pycon

   >>> # Open a HCI socket to device hci0
   >>> bt = BluetoothHCISocket(0)

Send a control packet
---------------------

This packet contains no operation (ie: it does nothing), but it will test that
you can communicate through the HCI device:

.. code-block:: pycon

   >>> ans, unans = bt.sr(HCI_Hdr()/HCI_Command_Hdr())
   Received 1 packets, got 1 answers, remaining 0 packets

You can then inspect the response:

.. code-block:: pycon

   >>> # ans[0] = Answered packet #0
   >>> # ans[0][1] = The response packet
   >>> p = ans[0][1]
   >>> p.show()
   ###[ HCI header ]###
     type= Event
   ###[ HCI Event header ]###
        code= 0xf
        len= 4
   ###[ Command Status ]###
           status= 1
           number= 2
           opcode= 0x0

Receiving all events
--------------------

To start capturing all events from the HCI device, use ``sniff``:

.. code-block:: pycon

   >>> pkts = bt.sniff()
   (press ^C after a few seconds to stop...)
   >>> pkts
   <Sniffed: TCP:0 UDP:0 ICMP:0 Other:0>

Unless your computer is doing something else with Bluetooth, you'll probably get
0 packets at this point. This is because ``sniff`` doesn't actually enable any
promiscuous mode on the device.

However, this is useful for some other commands that will be explained later on.

Importing and exporting packets
-------------------------------

:ref:`Just like with other protocols <import-export>`, you can save packets for
future use in ``libpcap`` format with ``wrpcap``:

.. code-block:: pycon

   >>> wrpcap("/tmp/bluetooth.pcap", pkts)

And load them up again with ``rdpcap``:

.. code-block:: pycon

   >>> pkts = rdpcap("/tmp/bluetooth.pcap")


Working with Bluetooth Low Energy
=================================

.. note::

   This requires a Bluetooth 4.0 or later interface that supports
   :abbr:`BLE (Bluetooth Low Energy)`, either as a dedicated
   :abbr:`LE (Low Energy)` chipset or a *dual-mode* LE +
   :abbr:`BR (Basic Rate)`/:abbr:`EDR (Enhanced Data Rate)` chipset (such as an
   `RTL8723BU`__).
   
   These instructions only been tested on Linux, and require Scapy v2.4.3 or
   later. There are bugs in earlier versions which decode packets incorrectly.

__ https://www.realtek.com/en/products/communications-network-ics/item/rtl8723bu

These examples presume you have already :ref:`opened a HCI socket <hci-open>`
(as ``bt``).

Discovering nearby devices
--------------------------

Enabling discovery mode
^^^^^^^^^^^^^^^^^^^^^^^

Start active discovery mode with:

.. code-block:: pycon

   >>> # type=1: Active scanning mode
   >>> bt.sr(
   ...   HCI_Hdr()/
   ...   HCI_Command_Hdr()/
   ...   HCI_Cmd_LE_Set_Scan_Parameters(type=1))
   Received 1 packets, got 1 answers, remaining 0 packets

   >>> # filter_dups=False: Show duplicate advertising reports, because these
   >>> # sometimes contain different data!
   >>> bt.sr(
   ...   HCI_Hdr()/
   ...   HCI_Command_Hdr()/
   ...   HCI_Cmd_LE_Set_Scan_Enable(
   ...     enable=True,
   ...     filter_dups=False))
   Received 1 packets, got 1 answers, remaining 0 packets


In the background, there are already HCI events waiting on the socket. You can
grab these events with ``sniff``:

.. code-block:: pycon

   >>> # The lfilter will drop anything that's not an advertising report.
   >>> adverts = bt.sniff(lfilter=lambda p: HCI_LE_Meta_Advertising_Reports in p)
   (press ^C after a few seconds to stop...)
   >>> adverts
   <Sniffed: TCP:0 UDP:0 ICMP:0 Other:101>

Once you have the packets, disable discovery mode with:

.. code-block:: pycon

   >>> bt.sr(
   ...   HCI_Hdr()/
   ...   HCI_Command_Hdr()/
   ...   HCI_Cmd_LE_Set_Scan_Enable(
   ...     enable=False))
   Begin emission:
   Finished sending 1 packets.
   ...*
   Received 4 packets, got 1 answers, remaining 0 packets
   (<Results: TCP:0 UDP:0 ICMP:0 Other:1>, <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>)

Collecting advertising reports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
