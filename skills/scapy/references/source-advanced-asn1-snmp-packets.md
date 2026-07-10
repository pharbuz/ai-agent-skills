    
The ``Context`` class must be specified::

    >>> (dcert,remain) = BERcodec_Object.dec(cert, context=ASN1_Class_X509)
    >>> dcert.show()
    # ASN1_SEQUENCE:
      # ASN1_SEQUENCE:
        # ASN1_X509_CONT0:
          <ASN1_INTEGER[2L]>
        <ASN1_INTEGER[1L]>
        # ASN1_SEQUENCE:
          <ASN1_OID['.1.2.840.113549.1.1.5']>
          <ASN1_NULL[0L]>
        # ASN1_SEQUENCE:
          # ASN1_SET:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.4.6']>
              <ASN1_PRINTABLE_STRING['US']>
          # ASN1_SET:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.4.10']>
              <ASN1_PRINTABLE_STRING['AOL Time Warner Inc.']>
          # ASN1_SET:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.4.11']>
              <ASN1_PRINTABLE_STRING['America Online Inc.']>
          # ASN1_SET:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.4.3']>
              <ASN1_PRINTABLE_STRING['AOL Time Warner Root Certification Authority 2']>
        # ASN1_SEQUENCE:
          <ASN1_UTC_TIME['020529060000Z']>
          <ASN1_UTC_TIME['370928234300Z']>
        # ASN1_SEQUENCE:
          # ASN1_SET:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.4.6']>
              <ASN1_PRINTABLE_STRING['US']>
          # ASN1_SET:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.4.10']>
              <ASN1_PRINTABLE_STRING['AOL Time Warner Inc.']>
          # ASN1_SET:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.4.11']>
              <ASN1_PRINTABLE_STRING['America Online Inc.']>
          # ASN1_SET:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.4.3']>
              <ASN1_PRINTABLE_STRING['AOL Time Warner Root Certification Authority 2']>
        # ASN1_SEQUENCE:
          # ASN1_SEQUENCE:
            <ASN1_OID['.1.2.840.113549.1.1.1']>
            <ASN1_NULL[0L]>
          <ASN1_BIT_STRING['\x000\x82\x02\n\x02\x82\x02\x01\x00\xb47Z\x08\x16\x99\x14\xe8U\xb1\x1b$k\xfc\xc7\x8b\xe6\x87\xa9\x89\xee\x8b\x99\xcdO@\x86\xa4\xb6M\xc9\xd9\xb1\xdc<M\r\x85L\x15lF\x8bRx\x9f\xf8#\xfdg\xf5$:h]\xd0\xf7daAT\xa3\x8b\xa5\x08\xd2)[\x9b`O&\x83\xd1c\x12VIv\xa4\x16\xc2\xa5\x9dE\xac\x8b\x84\x95\xa8\x16\xb1\xec\x9f\xea$\x1a\xef\xb9W\\\x9a$!,M\x0eq\x1f\xa6\xac]Et\x03\x98\xc4T\x8c\x16JAw\x86\x95u\x0cG\x01f`\xfc\x15\xf1\x0f\xea\xf5\x14x\xc7\x0e\xd7n\x81\x1c^\xbf^\xe7:*\xd8\x97\x170|\x00\xad\x08\x9d3\xaf\xb8\x99a\x80\x8b\xa8\x95~\x14\xdc\x12l\xa4\xd0\xd8\xef@I\x026\xf9n\xa9\xd6\x1d\x96V\x04\xb2\xb3-\x16V\x86\x8f\xd9 W\x80\xcdg\x10m\xb0L\xf0\xdaF\xb6\xea%.F\xaf\x8d\xb0\x8584\x8b\x14&\x82+\xac\xae\x99\x0b\x8e\x14\xd7R\xbd\x9ei\xc3\x86\x02\x0b\xeavu1\t\xce3\x19!\x85C\xe6\x89-\x9f%7g\xf1#j\xd2\x00m\x97\xf9\x9f\xe7)\xca\xdd\x1f\xd7\x06\xea\xb8\xc9\xb9\t!\x9f\xc8?\x06\xc5\xd2\xe9\x12F\x00N{\x08\xebB=+Hn\x9dg\xddK\x02\xe4D\xf3\x93\x19\xa5\'\xceiz\xbeg\xd3\xfcP\xa4,\xab\xc3k\xb9\xe3\x80L\xcf\x05aK+\xdc\x1b\xb9\xa6\xd2\xd0\xaa\xf5+s\xfb\xce\x905\x9f\x0cR\x1c\xbf\\!a\x11[\x15K\xa9$Q\xfc\xa4\\\xf7\x17\x9d\xb0\xd2\xfa\x07\xe9\x8fV\xe4\x1a\x8ch\x8a\x04\xd3|Z\xe3\x9e\xa2\xa1\xcaq[\xa2\xd4\xa0\xe7)\x85]\x03h*O\xd2\x06\xd7=\xf9\xc3\x03/?e\xf9g\x1eG@\xd3c\x0f\xe3\xd5\x8e\xf9\x85\xab\x97L\xb3\xd7&\xeb\x96\n\x94\xde\x856\x9c\xc8\x7f\x81\t\x02I*\x0e\xf5d2\x0c\x82\xd1\xbaj\x82\x1b\xb3Kt\x11\xf3\x8cw\xd6\x9f\xbf\xdc7\xa4\xa7U\x04/\xd41\xe8\xd3F\xb9\x03|\xda\x12NYd\xb7Q11P\xa0\xca\x1c\'\xd9\x10.\xad\xd6\xbd\x10f+\xc3\xb0"J\x12[\x02\x03\x01\x00\x01']>
        # ASN1_X509_CONT3:
          # ASN1_SEQUENCE:
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.29.19']>
              <ASN1_BOOLEAN[-1L]>
              <ASN1_STRING['0\x03\x01\x01\xff']>
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.29.14']>
              <ASN1_STRING['\x04\x14Oim\x03~\x9d\x9f\x07\x18C\xbc\xb7\x10N\xd5\xbf\xa9\xc4 (']>
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.29.35']>
              <ASN1_STRING['0\x16\x80\x14Oim\x03~\x9d\x9f\x07\x18C\xbc\xb7\x10N\xd5\xbf\xa9\xc4 (']>
            # ASN1_SEQUENCE:
              <ASN1_OID['.2.5.29.15']>
              <ASN1_BOOLEAN[-1L]>
              <ASN1_STRING['\x03\x02\x01\x86']>
      # ASN1_SEQUENCE:
        <ASN1_OID['.1.2.840.113549.1.1.5']>
        <ASN1_NULL[0L]>
      <ASN1_BIT_STRING['\x00;\xf3\xae\xca\xe8.\x87\x85\xfbeY\xe7\xad\x11\x14\xa5W\xbcX\x9f$\x12W\xbb\xfb?4\xda\xee\xadz*4rp1k\xc7\x19\x98\x80\xc9\x82\xde7w^T\x8b\x8e\xf2\xeagO\xc9t\x84\x91V\t\xd5\xe5z\x9a\x81\xb6\x81\xc2\xad6\xe4\xf1T\x11S\xf34E\x01&\xc8\xe5\x1a\xbc4D!\xde\xad%\xfcv\x16w!\x90\x80\x98W\x9dN\xea\xec/\xaa<\x14{W\xc1~\x18\x14g\xee$\xc6\xbd\xba\x15\xb0\xd2\x18\xbd\xb7U\x81\xacS\xc0\xe8\xddi\x12\x13B\xb7\x02\xb5\x05A\xcayPn\x82\x0eqr\x93F\xe8\x9d\r]\xbd\xae\xce)\xadc\xd5U\x16\x800\'\xffv\xba\xf7\xb8\xd6J\xe3\xd9\xb5\xf9R\xd0N@\xa9\xc7\xe5\xc22\xc7\xaav$\xe1k\x05P\xeb\xc5\xbf\nT\xe5\xb9B<$\xfb\xb7\x07\x9c0\x9fyZ\xe6\xe0@R\x15\xf4\xfc\xaa\xf4V\xf9D\x97\x87\xed\x0eer^\xbe&\xfbM\xa4-\x08\x07\xde\xd8\\\xa0\xdc\x813\x99\x18%\x11w\xa7\xeb\xfdX\t,\x99k\x1b\x8a\xf3R?\x1aMH`\xf1\xa0\xf63\x02S\x8b\xed%\t\xb8\r-\xed\x97s\xec\xd7\x96\x1f\x8e`\x0e\xda\x10\x9b/\x18$\xf6\xa6M\n\xf9;\xcbu\xc2\xcc/\xce$i\xc9\n"\x8eY\xa7\xf7\x82\x0c\xd7\xd7k5\x9cC\x00j\xc4\x95g\xba\x9cE\xcb\xb8\x0e7\xf7\xdcN\x01O\xbe\n\xb6\x03\xd3\xad\x8aE\xf7\xda\'M)\xb1H\xdf\xe4\x11\xe4\x96F\xbdl\x02>\xd6Q\xc8\x95\x17\x01\x15\xa9\xf2\xaa\xaa\xf2\xbf/e\x1bo\xd0\xb9\x1a\x93\xf5\x8e5\xc4\x80\x87>\x94/f\xe4\xe9\xa8\xffA\x9cp*O*9\x18\x95\x1e~\xfba\x01<Q\x08.(\x18\xa4\x16\x0f1\xfd:l#\x93 v\xe1\xfd\x07\x85\xd1[?\xd2\x1cs2\xdd\xfa\xb9\xf8\x8c\xcf\x02\x87z\x9a\x96\xe4\xedO\x89\x8dSC\xab\x0e\x13\xc0\x01\x15\xb4y8\xdb\xfcn=\x9eQ\xb6\xb8\x13\x8bg\xcf\xf9|\xd9"\x1d\xf6]\xc5\x1c\x01/\x98\xe8z$\x18\xbc\x84\xd7\xfa\xdcr[\xf7\xc1:h']>

ASN.1 layers
^^^^^^^^^^^^

While this may be nice, it's only an ASN.1 encoder/decoder. Nothing related to Scapy yet.

ASN.1 fields
~~~~~~~~~~~~

Scapy provides ASN.1 fields. They will wrap ASN.1 objects and provide the necessary logic to bind a field name to the value. ASN.1 packets will be described as a tree of ASN.1 fields. Then each field name will be made available as a normal ``Packet`` object, in a flat flavor (ex: to access the version field of a SNMP packet, you don't need to know how many containers wrap it).

Each ASN.1 field is linked to an ASN.1 object through its tag.


ASN.1 packets
~~~~~~~~~~~~~

ASN.1 packets inherit from the Packet class. Instead of a ``fields_desc`` list of fields, they define ``ASN1_codec`` and ``ASN1_root`` attributes. The first one is a codec (for example: ``ASN1_Codecs.BER``), the second one is a tree compounded with ASN.1 fields.

A complete example: SNMP
------------------------

SNMP defines new ASN.1 objects. We need to define them::

    class ASN1_Class_SNMP(ASN1_Class_UNIVERSAL):
        name="SNMP"
        PDU_GET = 0xa0
        PDU_NEXT = 0xa1
        PDU_RESPONSE = 0xa2
        PDU_SET = 0xa3
        PDU_TRAPv1 = 0xa4
        PDU_BULK = 0xa5
        PDU_INFORM = 0xa6
        PDU_TRAPv2 = 0xa7

These objects are PDU, and are in fact new names for a sequence container (this is generally the case for context objects: they are old containers with new names). This means creating the corresponding ASN.1 objects and BER codecs is simplistic::

    class ASN1_SNMP_PDU_GET(ASN1_SEQUENCE):
        tag = ASN1_Class_SNMP.PDU_GET
    
    class ASN1_SNMP_PDU_NEXT(ASN1_SEQUENCE):
        tag = ASN1_Class_SNMP.PDU_NEXT
    
    # [...]
    
    class BERcodec_SNMP_PDU_GET(BERcodec_SEQUENCE):
        tag = ASN1_Class_SNMP.PDU_GET
    
    class BERcodec_SNMP_PDU_NEXT(BERcodec_SEQUENCE):
        tag = ASN1_Class_SNMP.PDU_NEXT
    
    # [...]

Metaclasses provide the magic behind the fact that everything is automatically registered and that ASN.1 objects and BER codecs can find each other.

The ASN.1 fields are also trivial::
    
    class ASN1F_SNMP_PDU_GET(ASN1F_SEQUENCE):
        ASN1_tag = ASN1_Class_SNMP.PDU_GET
    
    class ASN1F_SNMP_PDU_NEXT(ASN1F_SEQUENCE):
        ASN1_tag = ASN1_Class_SNMP.PDU_NEXT
    
    # [...]

Now, the hard part, the ASN.1 packet::

    SNMP_error = { 0: "no_error",
                   1: "too_big",
    # [...]
                 }
    
    SNMP_trap_types = { 0: "cold_start",
                        1: "warm_start",
    # [...]
                      }
    
    class SNMPvarbind(ASN1_Packet):
        ASN1_codec = ASN1_Codecs.BER
        ASN1_root = ASN1F_SEQUENCE( ASN1F_OID("oid","1.3"),
                                    ASN1F_field("value",ASN1_NULL(0))
                                    )
    
    
    class SNMPget(ASN1_Packet):
        ASN1_codec = ASN1_Codecs.BER
        ASN1_root = ASN1F_SNMP_PDU_GET( ASN1F_INTEGER("id",0),
                                        ASN1F_enum_INTEGER("error",0, SNMP_error),
                                        ASN1F_INTEGER("error_index",0),
                                        ASN1F_SEQUENCE_OF("varbindlist", [], SNMPvarbind)
                                        )
