# Advanced snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## advanced_usage__asn1_snmp

Part 2. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 3: literal ---
# output: SNMP_error = { 0: "no_error",
# output: 1: "too_big",
# [...]
             }

# output: SNMP_trap_types = { 0: "cold_start",
# output: 1: "warm_start",
# [...]
                  }

class SNMPvarbind(ASN1_Packet):
# output: ASN1_codec = ASN1_Codecs.BER
# output: ASN1_root = ASN1F_SEQUENCE( ASN1F_OID("oid","1.3"),
                                ASN1F_field("value",ASN1_NULL(0))
                                )


class SNMPget(ASN1_Packet):
# output: ASN1_codec = ASN1_Codecs.BER
# output: ASN1_root = ASN1F_SNMP_PDU_GET( ASN1F_INTEGER("id",0),
                                    ASN1F_enum_INTEGER("error",0, SNMP_error),
                                    ASN1F_INTEGER("error_index",0),
                                    ASN1F_SEQUENCE_OF("varbindlist", [], SNMPvarbind)
                                    )

class SNMPnext(ASN1_Packet):
# output: ASN1_codec = ASN1_Codecs.BER
# output: ASN1_root = ASN1F_SNMP_PDU_NEXT( ASN1F_INTEGER("id",0),
                                     ASN1F_enum_INTEGER("error",0, SNMP_error),
                                     ASN1F_INTEGER("error_index",0),
                                     ASN1F_SEQUENCE_OF("varbindlist", [], SNMPvarbind)
                                     )
# [...]

class SNMP(ASN1_Packet):
# output: ASN1_codec = ASN1_Codecs.BER
# output: ASN1_root = ASN1F_SEQUENCE(
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
# output: self.PDU.id == other.PDU.id )
# [...]
bind_layers( UDP, SNMP, sport=161)
bind_layers( UDP, SNMP, dport=161)
```

```python
# --- snippet 4: literal ---
a=SNMP(version=3, PDU=SNMPget(varbindlist=[SNMPvarbind(oid="1.2.3",value=5),
                                           SNMPvarbind(oid="3.2.1",value="hello")]))
a.show()
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
hexdump(a)
# output: 0000   30 2E 02 01 03 04 06 70  75 62 6C 69 63 A0 21 02   0......public.!.
# output: 0010   01 00 02 01 00 02 01 00  30 16 30 07 06 02 2A 03   ........0.0...*.
# output: 0020   02 01 05 30 0B 06 02 7A  01 04 05 68 65 6C 6C 6F   ...0...z...hello
send(IP(dst="1.2.3.4")/UDP()/SNMP())
# output: .
# output: Sent 1 packets.
SNMP(raw(a)).show()
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
```

```python
# --- snippet 5: literal ---
load_mib("mib/*")
o1,o2
(<ASN1_OID['basicConstraints']>, <ASN1_OID['rsaEncryption']>)
```

```python
# --- snippet 6: literal ---
conf.mib.sha1_with_rsa_signature
'1.2.840.113549.1.1.5'
```

```python
# --- snippet 7: literal ---
conf.mib._oidname("1.2.3.6.1.4.1.5")
'enterprises.5'
```

```python
# --- snippet 8: literal ---
conf.mib._make_graph()

## advanced_usage__automaton

```python
# Extracted Python snippets from doc/scapy/advanced_usage/automaton.rst
# Source: https://scapy.readthedocs.io/en/latest/
# Snippets may require root/admin privileges, live network access, or optional dependencies.
```
