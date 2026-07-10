    
    ISAKMPTransformSetField  # ISAKMP (StrLenField) 
    
    TimeStampField           # NTP (BitField)


Design patterns
===============
Some patterns are similar to a lot of protocols and thus can be described the same way in Scapy.

The following parts will present several models and conventions that can be followed when implementing a new protocol.

Field naming convention
-----------------------
The goal is to keep the writing of packets fluent and intuitive. The basic instructions are the following :

* Do not use any value from the ``Packet.__slots__``` list as a field name (such as name, time or original), as they are reserved for Scapy internals
* Use inverted camel case and common abbreviations (e.g. len, src, dst, dstPort, srcIp).
* Wherever it is either possible or relevant, prefer using the names from the specifications. This aims to help newcomers to easily forge packets.

Add new protocols to Scapy
--------------------------

New protocols can go either in ``scapy/layers`` or to ``scapy/contrib``. Protocols in ``scapy/layers`` should be usually found on common networks, while protocols in ``scapy/contrib`` should be uncommon or specific.

To be precise, ``scapy/layers`` protocols should not be importing ``scapy/contrib`` protocols, whereas ``scapy/contrib`` protocols may import both ``scapy/contrib`` and ``scapy/layers`` protocols.

Scapy provides an ``explore()`` function, to search through the available layer/contrib modules. Therefore, modules contributed back to Scapy must provide information about them, knowingly:

- A **contrib** module must have defined, near the top of the module (below the license header is a good place) **(without the brackets)** `Example <https://github.com/secdev/scapy/blob/0f6ac82ed66919a20226a3d8d164b810c8eb293c/scapy/contrib/openflow.py#L11-L12>`_ ::

    # scapy.contrib.description = [...]
    # scapy.contrib.status = [...]
    # scapy.contrib.name = [...] (optional)

- If the contrib module does not contain any packets, and should not be indexed in `explore()`, then you should instead set::

    # scapy.contrib.status = skip 

- A **layer** module must have a docstring, in which the first line shortly describes the module.
