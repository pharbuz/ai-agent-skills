
This example sets up a virtual iBeacon:

.. code-block:: python3

   # Load the contrib module for iBeacon
   load_contrib('ibeacon')

   # Beacon data consists of a UUID, and two 16-bit integers: "major" and
   # "minor".
   #
   # iBeacon sits on top of Apple's BLE protocol.
   p = Apple_BLE_Submessage()/IBeacon_Data(
      uuid='fb0b57a2-8228-44cd-913a-94a122ba1206',
      major=1, minor=2)

   # build_set_advertising_data() wraps an Apple_BLE_Submessage or
   # Apple_BLE_Frame into a HCI_Cmd_LE_Set_Advertising_Data payload, that can
   # be sent to the BLE controller.
   bt.sr(p.build_set_advertising_data())

Once :ref:`advertising has been started <le-adv-start>`, the beacon may then be
detected with `Beacon Locator`__ (Android):

.. image:: ../graphics/ble_ibeacon.png

__ https://github.com/vitas/beaconloc


.. _le-adv-start:

Starting advertising
--------------------

.. code-block:: python3

   bt.sr(HCI_Hdr()/
         HCI_Command_Hdr()/
         HCI_Cmd_LE_Set_Advertise_Enable(enable=True))

.. _le-adv-stop:

Stopping advertising
--------------------

.. code-block:: python3

   bt.sr(HCI_Hdr()/
         HCI_Command_Hdr()/
         HCI_Cmd_LE_Set_Advertise_Enable(enable=False))


Resources and references
------------------------

  * `16-bit UUIDs for members`__: List of registered UUIDs which appear in
    ``EIR_CompleteList16BitServiceUUIDs`` and ``EIR_ServiceData16BitUUID``.

__ https://www.bluetooth.com/specifications/assigned-numbers/16-bit-uuids-for-members

  * `16-bit UUIDs for SDOs`__: List of registered UUIDs which are used by
    Standards Development Organisations.
  
__ https://www.bluetooth.com/specifications/assigned-numbers/16-bit-uuids-for-sdos

  * `Company Identifiers`__: List of company IDs, which appear in
    ``EIR_Manufacturer_Specific_Data.company_id``.
  
__ https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers

  * `Generic Access Profile`__: List of assigned type IDs and links to
    specification definitions, which appear in ``EIR_Header``.
 
__ https://www.bluetooth.com/specifications/assigned-numbers/generic-access-profile

.. _apple-ble:

Apple/iBeacon broadcast frames
==============================

.. note::

    This describes the wire format for Apple's Bluetooth Low Energy
    advertisements, based on (limited) publicly available information. It is not
    specific to using Bluetooth on Apple operating systems.

`iBeacon`__ is Apple's proximity beacon protocol. Scapy includes a contrib
module, ``ibeacon``, for working with Apple's :abbr:`BLE (Bluetooth Low Energy)`
broadcasts:

__ https://en.wikipedia.org/wiki/IBeacon

.. code-block:: pycon

   >>> load_contrib('ibeacon')

:ref:`Setting up advertising for iBeacon <adv-ibeacon>` (above) describes how to
broadcast a simple beacon.

While this module is called ``ibeacon``, Apple has other "submessages" which are
also advertised within their manufacturer-specific data field, including:

 * `AirDrop`__
 * AirPlay
 * AirPods
 * `Handoff`__
 * Nearby
 * `Overflow area`__

__ https://en.wikipedia.org/wiki/AirDrop
__ https://en.wikipedia.org/wiki/OS_X_Yosemite#Continuity
__ https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393252-startadvertising

For compatibility with these other broadcasts, Apple BLE frames in Scapy are
layered on top of ``Apple_BLE_Submessage`` and ``Apple_BLE_Frame``:

 * ``HCI_Cmd_LE_Set_Advertising_Data``, ``HCI_LE_Meta_Advertising_Report``,
   ``BTLE_ADV_IND``, ``BTLE_ADV_NONCONN_IND`` or ``BTLE_ADV_SCAN_IND`` contain
   one or more...
 * ``EIR_Hdr``, which may have a payload of one...
 * ``EIR_Manufacturer_Specific_Data``, which may have a payload of one...
 * ``Apple_BLE_Frame``, which contains one or more...
 * ``Apple_BLE_Submessage``, which contains a payload of one...
 * ``Raw`` (if not supported), or ``IBeacon_Data``.

This module only presently supports ``IBeacon_Data`` submessages. Other
submessages are decoded as ``Raw``.

One might sometimes see multiple submessages in a single broadcast, such as
Handoff and Nearby.  This is not mandatory -- there are also Handoff-only and
Nearby-only broadcasts.

Inspecting a raw BTLE advertisement frame from an Apple device:

.. code-block:: python3

    p = BTLE(hex_bytes('d6be898e4024320cfb574d5a02011a1aff4c000c0e009c6b8f40440f1583ec895148b410050318c0b525b8f7d4'))
    p.show()

Results in the output:

.. code-block:: text

    ###[ BT4LE ]###
      access_addr= 0x8e89bed6
      crc= 0xb8f7d4
    ###[ BTLE advertising header ]###
         RxAdd= public
         TxAdd= random
         RFU= 0
         PDU_type= ADV_IND
         unused= 0
         Length= 0x24
    ###[ BTLE ADV_IND ]###
            AdvA= 5a:4d:57:fb:0c:32
            \data\
             |###[ EIR Header ]###
             |  len= 2
             |  type= flags
             |###[ Flags ]###
             |     flags= general_disc_mode+simul_le_br_edr_ctrl+simul_le_br_edr_host
             |###[ EIR Header ]###
             |  len= 26
             |  type= mfg_specific_data
             |###[ EIR Manufacturer Specific Data ]###
             |     company_id= 0x4c
             |###[ Apple BLE broadcast frame ]###
             |        \plist\
             |         |###[ Apple BLE submessage ]###
             |         |  subtype= handoff
             |         |  len= 14
             |         |###[ Raw ]###
             |         |     load= '\x00\x9ck\x8f@D\x0f\x15\x83\xec\x89QH\xb4'
             |         |###[ Apple BLE submessage ]###
             |         |  subtype= nearby
             |         |  len= 5
             |         |###[ Raw ]###
             |         |     load= '\x03\x18\xc0\xb5%'
