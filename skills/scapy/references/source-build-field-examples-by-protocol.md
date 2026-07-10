
First, a lenfield is declared using ``FieldLenField`` (or a derivate). If its value is None when assembling a packet, its value will be deduced from the varfield that was referenced. The reference is done using either the ``length_of`` parameter or the ``count_of`` parameter. The ``count_of`` parameter has a meaning only when varfield is a field that holds a list (``PacketListField`` or ``FieldListField``). The value will be the name of the varfield, as a string. According to which parameter is used the ``i2len()`` or ``i2count()`` method will be called on the varfield value. The returned value will the be adjusted by the function provided in the adjust parameter. adjust will be applied to 2 arguments: the packet instance and the value returned by ``i2len()`` or ``i2count()``. By default, adjust does nothing::

    adjust=lambda pkt,x: x

For instance, if ``the_varfield`` is a list

::

    FieldLenField("the_lenfield", None, count_of="the_varfield")

or if the length is in 16bits words::

    FieldLenField("the_lenfield", None, length_of="the_varfield", adjust=lambda pkt,x:(x+1)/2)

The variable length field
~~~~~~~~~~~~~~~~~~~~~~~~~

A varfield can be: ``StrLenField``, ``PacketLenField``, ``PacketListField``, ``FieldListField``, ...

For the two firsts, when a packet is being dissected, their lengths are deduced from a lenfield already dissected. The link is done using the ``length_from`` parameter, which takes a function that, applied to the partly dissected packet, returns the length in bytes to take for the field. For instance::

    StrLenField("the_varfield", "the_default_value", length_from = lambda pkt: pkt.the_lenfield)

or

::

    StrLenField("the_varfield", "the_default_value", length_from = lambda pkt: pkt.the_lenfield-12)

For the ``PacketListField`` and ``FieldListField`` and their derivatives, they work as above when they need a length. If they need a number of elements, the length_from parameter must be ignored and the count_from parameter must be used instead. For instance::

    FieldListField("the_varfield", ["1.2.3.4"], IPField("", "0.0.0.0"), count_from = lambda pkt: pkt.the_lenfield)

Examples
^^^^^^^^

::

    class TestSLF(Packet):
        fields_desc=[ FieldLenField("len", None, length_of="data"),
                      StrLenField("data", "", length_from=lambda pkt:pkt.len) ]
    
    class TestPLF(Packet):
        fields_desc=[ FieldLenField("len", None, count_of="plist"),
                      PacketListField("plist", None, IP, count_from=lambda pkt:pkt.len) ]
    
    class TestFLF(Packet):
        fields_desc=[ 
           FieldLenField("the_lenfield", None, count_of="the_varfield"), 
           FieldListField("the_varfield", ["1.2.3.4"], IPField("", "0.0.0.0"), 
                           count_from = lambda pkt: pkt.the_lenfield) ]

    class TestPkt(Packet):
        fields_desc = [ ByteField("f1",65),
                        ShortField("f2",0x4244) ]
        def extract_padding(self, p):
            return "", p
    
    class TestPLF2(Packet):
        fields_desc = [ FieldLenField("len1", None, count_of="plist",fmt="H", adjust=lambda pkt,x:x+2),
                        FieldLenField("len2", None, length_of="plist",fmt="I", adjust=lambda pkt,x:(x+1)/2),
                        PacketListField("plist", None, TestPkt, length_from=lambda x:(x.len2*2)/3*3) ]

Test the ``FieldListField`` class::
    
    >>> TestFLF("\x00\x02ABCDEFGHIJKL")
    <TestFLF  the_lenfield=2 the_varfield=['65.66.67.68', '69.70.71.72'] |<Raw  load='IJKL' |>>


Special
-------

::

    Emph     # Wrapper to emphasize field when printing, e.g. Emph(IPField("dst", "127.0.0.1")),
    
    ActionField
    
    ConditionalField(fld, cond)
            # Wrapper to make field 'fld' only appear if
            # function 'cond' evals to True, e.g. 
            # ConditionalField(XShortField("chksum",None),lambda pkt:pkt.chksumpresent==1)
            # When hidden, it won't be built nor dissected and the stored value will be 'None'
            
    
    PadField(fld, align, padwith=None)  
           # Add bytes after the proxified field so that it ends at
           # the specified alignment from its beginning

    BitExtendedField(extension_bit)
           # Field with a variable number of bytes. Each byte is made of:
           # - 7 bits of data
           # - 1 extension bit:
           #    * 0 means that it is the last byte of the field ("stopping bit")
           #    * 1 means that there is another byte after this one ("forwarding bit")
           # extension_bit is the bit number [0-7] of the extension bit in the byte

    MSBExtendedField, LSBExtendedField      # Special cases of BitExtendedField

TCP/IP
------

::

    IPField
    SourceIPField
    
    IPoptionsField
    TCPOptionsField
    
    MACField
    DestMACField(MACField)
    SourceMACField(MACField)
    
    ICMPTimeStampField

802.11
------

::

    Dot11AddrMACField
    Dot11Addr2MACField
    Dot11Addr3MACField
    Dot11Addr4MACField
    Dot11SCField

DNS
---

::

    DNSStrField
    DNSRRCountField
    DNSRRField
    DNSQRField

ASN.1
-----

::

    ASN1F_element
    ASN1F_field
    ASN1F_INTEGER
    ASN1F_enum_INTEGER
    ASN1F_STRING
    ASN1F_OID
    ASN1F_SEQUENCE
    ASN1F_SEQUENCE_OF
    ASN1F_PACKET
    ASN1F_CHOICE

Other protocols
---------------

::

    NetBIOSNameField         # NetBIOS (StrFixedLenField)
