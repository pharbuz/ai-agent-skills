

Using Nordic Semiconductor's nRF Sniffer
========================================

Since **Scapy >2.5.0**, Scapy supports `Wireshark's extcap <https://www.wireshark.org/docs/man-pages/extcap.html>`_ interfaces.
You can therefore use your USB nordic bluetooth dongle, provided that you `have installed <https://infocenter.nordicsemi.com/topic/ug_sniffer_ble/UG/sniffer_ble/installing_sniffer_plugin.html>`_ the Wireshark module properly.

.. code:: pycon

   >>> load_contrib("nrf_sniffer")
   >>> load_extcap()
   >>> conf.ifaces
   Source           Index  Name                          Address
   nrf_sniffer_ble  100    nRF Sniffer for Bluetooth LE  /dev/ttyUSB0-None
   [...]
   >>> sniff(iface="/dev/ttyUSB0-None", prn=lambda x: x.summary())
   NRFS2_PCAP / NRFS2_Packet / NRF2_Packet_Event / BTLE / BTLE_ADV / BTLE_ADV_IND
   NRFS2_PCAP / NRFS2_Packet / NRF2_Packet_Event / BTLE / BTLE_ADV / BTLE_ADV_IND
   NRFS2_PCAP / NRFS2_Packet / NRF2_Packet_Event / BTLE / BTLE_ADV / BTLE_ADV_IND
   NRFS2_PCAP / NRFS2_Packet / NRF2_Packet_Event / BTLE / BTLE_ADV / BTLE_ADV_NONCONN_IND
   NRFS2_PCAP / NRFS2_Packet / NRF2_Packet_Event / BTLE / BTLE_ADV / BTLE_ADV_NONCONN_IND
   NRFS2_PCAP / NRFS2_Packet / NRF2_Packet_Event / BTLE / BTLE_ADV / BTLE_ADV_IND
