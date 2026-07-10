
You can sometimes get multiple ``HCI_LE_Meta_Advertising_Report`` in a single
``HCI_LE_Meta_Advertising_Reports``, and these can also be for different
devices!

.. code-block:: python3

   # Rearrange into a generator that returns reports sequentially
   from itertools import chain
   reports = chain.from_iterable(
     p[HCI_LE_Meta_Advertising_Reports].reports
     for p in adverts)

   # Group reports by MAC address (consumes the reports generator)
   devices = {}
   for report in reports:
     device = devices.setdefault(report.addr, [])
     device.append(report)

   # Packet counters
   devices_pkts = dict((k, len(v)) for k, v in devices.items())
   print(devices_pkts)
   # {'xx:xx:xx:xx:xx:xx': 408, 'xx:xx:xx:xx:xx:xx': 2}


Filtering advertising reports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python3

   # Get one packet for each device that broadcasted short UUID 0xfe50 (Google).
   # Android devices broadcast this pretty much constantly.
   google = {}
   for mac, reports in devices.items():
     for report in reports:
       if (EIR_CompleteList16BitServiceUUIDs in report and
           0xfe50 in report[EIR_CompleteList16BitServiceUUIDs].svc_uuids):
         google[mac] = report
         break

   # List MAC addresses that sent such a broadcast
   print(google.keys())
   # dict_keys(['xx:xx:xx:xx:xx:xx', 'xx:xx:xx:xx:xx:xx'])

Look at the first broadcast received:

.. code-block:: pycon

   >>> for mac, report in google.items():
   ...   report.show()
   ...   break
   ...
   ###[ Advertising Report ]###
     type= conn_und
     atype= random
     addr= xx:xx:xx:xx:xx:xx
     len= 13
     \data\
      |###[ EIR Header ]###
      |  len= 2
      |  type= flags
      |###[ Flags ]###
      |     flags= general_disc_mode
      |###[ EIR Header ]###
      |  len= 3
      |  type= complete_list_16_bit_svc_uuids
      |###[ Complete list of 16-bit service UUIDs ]###
      |     svc_uuids= [0xfe50]
      |###[ EIR Header ]###
      |  len= 5
      |  type= svc_data_16_bit_uuid
      |###[ EIR Service Data - 16-bit UUID ]###
      |     svc_uuid= 0xfe50
      |     data= 'AB'
     rssi= -96

Setting up advertising
----------------------

.. note::

   Changing advertisements may not take effect until advertisements have first
   been :ref:`stopped <le-adv-stop>`.

AltBeacon
^^^^^^^^^

`AltBeacon`__ is a proximity beacon protocol developed by Radius Networks.  This
example sets up a virtual AltBeacon:

__ https://github.com/AltBeacon/spec

.. code-block:: python3

    # Load the contrib module for AltBeacon
    load_contrib('altbeacon')

    ab = AltBeacon(
        id1='2f234454-cf6d-4a0f-adf2-f4911ba9ffa6',
        id2=1,
        id3=2,
        tx_power=-59,
    )

    bt.sr(ab.build_set_advertising_data())

Once :ref:`advertising has been started <le-adv-start>`, the beacon may then be
detected with `Beacon Locator`__ (Android).

.. note::

    Beacon Locator v1.2.2 `incorrectly reports the beacon as being an
    iBeacon`__, but the values are otherwise correct.

__ https://github.com/vitas/beaconloc
__ https://github.com/vitas/beaconloc/issues/32

Eddystone
^^^^^^^^^

`Eddystone`__ is a proximity beacon protocol developed by Google. This uses an
Eddystone-specific service data field.

__ https://github.com/google/eddystone/

This example sets up a virtual `Eddystone URL`__ beacon:

__ https://github.com/google/eddystone/tree/master/eddystone-url

.. code-block:: python3

   # Load the contrib module for Eddystone
   load_contrib('eddystone')

   # Eddystone_URL.from_url() builds an Eddystone_URL frame for a given URL.
   #
   # build_set_advertising_data() wraps an Eddystone_Frame into a
   # HCI_Cmd_LE_Set_Advertising_Data payload, that can be sent to the BLE
   # controller.
   bt.sr(Eddystone_URL.from_url(
     'https://scapy.net').build_set_advertising_data())

Once :ref:`advertising has been started <le-adv-start>`, the beacon may then be
detected with `Eddystone Validator`__ or `Beacon Locator`__ (Android):

.. image:: ../graphics/ble_eddystone_url.png

__ https://github.com/google/eddystone/tree/master/tools/eddystone-validator
__ https://github.com/vitas/beaconloc

.. _adv-ibeacon:

iBeacon
^^^^^^^

`iBeacon`__ is a proximity beacon protocol developed by Apple, which uses their
manufacturer-specific data field.  :ref:`Apple/iBeacon framing <apple-ble>`
(below) describes this in more detail.

__ https://en.wikipedia.org/wiki/IBeacon
