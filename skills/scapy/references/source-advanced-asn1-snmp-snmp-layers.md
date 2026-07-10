    
    class SNMPnext(ASN1_Packet):
        ASN1_codec = ASN1_Codecs.BER
        ASN1_root = ASN1F_SNMP_PDU_NEXT( ASN1F_INTEGER("id",0),
                                         ASN1F_enum_INTEGER("error",0, SNMP_error),
                                         ASN1F_INTEGER("error_index",0),
                                         ASN1F_SEQUENCE_OF("varbindlist", [], SNMPvarbind)
                                         )
    # [...]
    
    class SNMP(ASN1_Packet):
        ASN1_codec = ASN1_Codecs.BER
        ASN1_root = ASN1F_SEQUENCE(
            ASN1F_enum_INTEGER("version", 1, {0:"v1", 1:"v2c", 2:"v2", 3:"v3"}),
            ASN1F_STRING("community","public"),
            ASN1F_CHOICE("PDU", SNMPget(),
                         SNMPget, SNMPnext, SNMPresponse, SNMPset,
                         SNMPtrapv1, SNMPbulk, SNMPinform, SNMPtrapv2)
            )
        def answers(self, other):
            return ( isinstance(self.PDU, SNMPresponse)    and
                     ( isinstance(other.PDU, SNMPget) or
                       isinstance(other.PDU, SNMPnext) or
                       isinstance(other.PDU, SNMPset)    ) and
                     self.PDU.id == other.PDU.id )
    # [...]
    bind_layers( UDP, SNMP, sport=161)
    bind_layers( UDP, SNMP, dport=161)

That wasn't that much difficult. If you think that can't be that short to implement SNMP encoding/decoding and that I may have cut too much, just look at the complete source code.

Now, how to use it? As usual::

    >>> a=SNMP(version=3, PDU=SNMPget(varbindlist=[SNMPvarbind(oid="1.2.3",value=5),
    ...                                            SNMPvarbind(oid="3.2.1",value="hello")]))
    >>> a.show()
    ###[ SNMP ]###
      version= v3
      community= 'public'
      \PDU\
       |###[ SNMPget ]###
       |  id= 0
       |  error= no_error
       |  error_index= 0
       |  \varbindlist\
       |   |###[ SNMPvarbind ]###
       |   |  oid= '1.2.3'
       |   |  value= 5
       |   |###[ SNMPvarbind ]###
       |   |  oid= '3.2.1'
       |   |  value= 'hello'
    >>> hexdump(a)
    0000   30 2E 02 01 03 04 06 70  75 62 6C 69 63 A0 21 02   0......public.!.
    0010   01 00 02 01 00 02 01 00  30 16 30 07 06 02 2A 03   ........0.0...*.
    0020   02 01 05 30 0B 06 02 7A  01 04 05 68 65 6C 6C 6F   ...0...z...hello
    >>> send(IP(dst="1.2.3.4")/UDP()/SNMP())
    .
    Sent 1 packets.
    >>> SNMP(raw(a)).show()
    ###[ SNMP ]###
      version= <ASN1_INTEGER[3L]>
      community= <ASN1_STRING['public']>
      \PDU\
       |###[ SNMPget ]###
       |  id= <ASN1_INTEGER[0L]>
       |  error= <ASN1_INTEGER[0L]>
       |  error_index= <ASN1_INTEGER[0L]>
       |  \varbindlist\
       |   |###[ SNMPvarbind ]###
       |   |  oid= <ASN1_OID['.1.2.3']>
       |   |  value= <ASN1_INTEGER[5L]>
       |   |###[ SNMPvarbind ]###
       |   |  oid= <ASN1_OID['.3.2.1']>
       |   |  value= <ASN1_STRING['hello']>
       
       

Resolving OID from a MIB
------------------------

About OID objects
^^^^^^^^^^^^^^^^^

OID objects are created with an ``ASN1_OID`` class::

    >>> o1=ASN1_OID("2.5.29.10")
    >>> o2=ASN1_OID("1.2.840.113549.1.1.1")
    >>> o1,o2
    (<ASN1_OID['.2.5.29.10']>, <ASN1_OID['.1.2.840.113549.1.1.1']>)

Loading a MIB
^^^^^^^^^^^^^

Scapy can parse MIB files and become aware of a mapping between an OID and its name::

    >>> load_mib("mib/*")
    >>> o1,o2
    (<ASN1_OID['basicConstraints']>, <ASN1_OID['rsaEncryption']>)

The MIB files I've used are attached to this page.

Scapy's MIB database
^^^^^^^^^^^^^^^^^^^^

All MIB information is stored into the conf.mib object. This object can be used to find the OID of a name

::

    >>> conf.mib.sha1_with_rsa_signature
    '1.2.840.113549.1.1.5'

or to resolve an OID::

    >>> conf.mib._oidname("1.2.3.6.1.4.1.5")
    'enterprises.5'

It is even possible to graph it::

    >>> conf.mib._make_graph()
