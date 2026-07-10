# Source: layers/bluetooth

*********
Bluetooth
*********

.. note::

   If you're new to using Scapy, start with the :doc:`usage documentation
   <../usage>`, which describes how to use Scapy with Ethernet and IP.

.. warning::

   Scapy does not support Bluetooth interfaces on Windows.

What is Bluetooth?
==================

Bluetooth is a short range, mostly point-to-point wireless communication
protocol that operates on the 2.4GHz `ISM band`__.

__ https://en.wikipedia.org/wiki/ISM_band

`Bluetooth standards are publicly available`__ from the `Bluetooth Special
Interest Group.`__

__ https://www.bluetooth.com/specifications/bluetooth-core-specification

__ https://www.bluetooth.com/

Broadly speaking, Bluetooth has *three* distinct physical-layer protocols:

Bluetooth Basic Rate (BR) and Enhanced Data Rate (EDR)
   These are the "classic" Bluetooth physical layers.
   
   :abbr:`BR (Basic Rate)` reaches effective speeds of up to 721kbit/s. This was
   ratified as ``IEEE 802.15.1-2002`` (v1.1) and ``-2005`` (v1.2).

   :abbr:`EDR (Enhanced Data Rate)` was introduced as an optional feature of
   Bluetooth 2.0 (2004). It can reach effective speeds of 2.1Mbit/s, and has
   lower power consumption than BR.

   In Bluetooth 4.0 and later, this is not supported by *Low Energy* interfaces,
   unless they are marked as *dual-mode*.

Bluetooth High Speed (HS)
  Introduced as an optional feature of Bluetooth 3.0 (2009), this extends
  Bluetooth by providing ``IEEE 802.11`` (WiFi) as an alternative, higher-speed
  data transport. Nodes negotiate switching with
  :abbr:`AMP (Alternative MAC/PHY)`.
    
  This is only supported by Bluetooth interfaces marked as *+HS*. Not all
  Bluetooth 3.0 and later interfaces support it.

Bluetooth Low Energy (BLE)
  Introduced in Bluetooth 4.0	(2010), this is an alternate physical layer
  designed for low power, embedded systems. It has shorter setup times, lower
  data rates and smaller :abbr:`MTU (maximum transmission unit)` sizes.  It adds
  broadcast and mesh network topologies, in addition to point-to-point links.

  This is only supported by Bluetooth interface marked as *+LE* or
  *Low Energy* -- not all Bluetooth 4.0 and later interfaces support it.

Most Bluetooth interfaces on PCs use USB connectivity (even on laptops), and
this is controlled with the Host-Controller Interface (HCI).  This typically
doesn't support promiscuous mode (sniffing), however there are many other
dedicated, non-HCI devices that support it.

Bluetooth sockets (``AF_BLUETOOTH``)
------------------------------------

There are multiple protocols available for Bluetooth through ``AF_BLUETOOTH``
sockets:

Host-controller interface (HCI) ``BTPROTO_HCI``
  This is the "base" level interface for communicating with a Bluetooth
  controller.  Everything is built on top of this, and this represents about as
  close to the physical layer as one can get with regular Bluetooth hardware.

  Scapy class: ``BluetoothMonitorSocket``

  Allows to capture all HCI transactions that are taking place over all HCI
  interfaces (including in BlueZ core). It is intended to perform monitoring of
  transactions, device attachment and removal, BlueZ logging...

  Scapy class: ``BluetoothUserSocket``

  This socket interacts with a Bluetooth controller with complete and exclusive
  control of de device. This means that BlueZ will not try to take control of
  the interface and will not help you manage connections via this interface.

  Scapy class: ``BluetoothHCISocket``

  Using HCI protocol, this socket interacts with a Bluetooth controller but
  does not have exclusive control over it, allowing BlueZ and other
  applications to still use the adapter to communicate with devices.

Logical Link Control and Adaptation Layer Protocol (L2CAP) ``BTPROTO_L2CAP``
  Scapy class: ``BluetoothL2CAPSocket``

  Sitting above the HCI, it provides connection and connection-less data
  transport to higher level protocols. It provides protocol multiplexing, packet
  segmentation and reassembly operations.

  When communicating with a single device, one may use a L2CAP channel.

RFCOMM ``BluetoothRFCommSocket``
  Scapy class: ``BluetoothRFCommSocket``

  RFCOMM is a serial port emulation protocol which operates over L2CAP.
  
  In addition to regular data transfer, it also supports manipulation of all of
  RS-232's non-data control circuitry (:abbr:`RTS (Request To Send)`,
  :abbr:`DTR (Data Terminal Ready)`, etc.)

Bluetooth on Linux
------------------

Linux's Bluetooth stack is developed by `the BlueZ project`__. `The Linux kernel
contains drivers to provide access to Bluetooth`__ interfaces using HCI, which
are exposed through sockets with ``AF_BLUETOOTH``.

__ http://www.bluez.org/

__ https://git.kernel.org/pub/scm/linux/kernel/git/bluetooth/bluetooth.git

BlueZ also provides a user-space companion to these kernel interfaces. The key
components are:

``bluetoothd``
  A daemon that provides access to Bluetooth devices over D-Bus.

``bluetoothctl``
  An interactive command-line program which interfaces with the ``bluetoothd``
  over D-Bus.

``hcitool``
  A command-line program which interfaces directly with kernel interfaces.


`Support for Classic Bluetooth in bluez is quite mature`__, however `BLE is
under active development`__.

__ http://www.bluez.org/profiles/

__ https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/TODO

First steps
===========

.. note::

   You must run these examples as ``root``.  These have only been tested on
   Linux, and require Scapy v2.4.3 or later.

Verify Bluetooth device
-----------------------

Before doing anything else, you'll want to check that your Bluetooth device has
actually been detected by the operating system:
