# Source: advanced_usage/asn1_snmp

ASN.1 and SNMP
==============

What is ASN.1?
--------------

.. note::

   This is only my view on ASN.1, explained as simply as possible. For more theoretical or academic views, I'm sure you'll find better on the Internet.

ASN.1 is a notation whose goal is to specify formats for data exchange. It is independent of the way data is encoded. Data encoding is specified in Encoding Rules.

The most used encoding rules are BER (Basic Encoding Rules) and DER (Distinguished Encoding Rules). Both look the same, but the latter is specified to guarantee uniqueness of encoding. This property is quite interesting when speaking about cryptography, hashes, and signatures.

ASN.1 provides basic objects: integers, many kinds of strings, floats, booleans, containers, etc. They are grouped in the so-called Universal class. A given protocol can provide other objects which will be grouped in the Context class. For example, SNMP defines PDU_GET or PDU_SET objects. There are also the Application and Private classes.

Each of these objects is given a tag that will be used by the encoding rules. Tags from 1 are used for Universal class. 1 is boolean, 2 is an integer, 3 is a bit string, 6 is an OID, 48 is for a sequence. Tags from the ``Context`` class begin at 0xa0. When encountering an object tagged by 0xa0, we'll need to know the context to be able to decode it. For example, in SNMP context, 0xa0 is a PDU_GET object, while in X509 context, it is a container for the certificate version.

Other objects are created by assembling all those basic brick objects. The composition is done using sequences and arrays (sets) of previously defined or existing objects. The final object (an X509 certificate, a SNMP packet) is a tree whose non-leaf nodes are sequences and sets objects (or derived context objects), and whose leaf nodes are integers, strings, OID, etc.

Scapy and ASN.1
---------------

Scapy provides a way to easily encode or decode ASN.1 and also program those encoders/decoders. It is quite laxer than what an ASN.1 parser should be, and it kind of ignores constraints. It won't replace neither an ASN.1 parser nor an ASN.1 compiler. Actually, it has been written to be able to encode and decode broken ASN.1. It can handle corrupted encoded strings and can also create those.

ASN.1 engine
^^^^^^^^^^^^

Note: many of the classes definitions presented here use metaclasses. If you don't look precisely at the source code and you only rely on my captures, you may think they sometimes exhibit a kind of magic behavior.
``
Scapy ASN.1 engine provides classes to link objects and their tags. They inherit from the ``ASN1_Class``. The first one is ``ASN1_Class_UNIVERSAL``, which provide tags for most Universal objects. Each new context (``SNMP``, ``X509``) will inherit from it and add its own objects.

::

    class ASN1_Class_UNIVERSAL(ASN1_Class):
        name = "UNIVERSAL"
    # [...]
        BOOLEAN = 1
        INTEGER = 2
        BIT_STRING = 3
    # [...]

    class ASN1_Class_SNMP(ASN1_Class_UNIVERSAL):
        name="SNMP"
        PDU_GET = 0xa0
        PDU_NEXT = 0xa1
        PDU_RESPONSE = 0xa2
    
    class ASN1_Class_X509(ASN1_Class_UNIVERSAL):
        name="X509"
        CONT0 = 0xa0
        CONT1 = 0xa1
    # [...]

All ASN.1 objects are represented by simple Python instances that act as nutshells for the raw values. The simple logic is handled by ``ASN1_Object`` whose they inherit from. Hence they are quite simple::

    class ASN1_INTEGER(ASN1_Object):
        tag = ASN1_Class_UNIVERSAL.INTEGER
    
    class ASN1_STRING(ASN1_Object):
        tag = ASN1_Class_UNIVERSAL.STRING
    
    class ASN1_BIT_STRING(ASN1_STRING):
        tag = ASN1_Class_UNIVERSAL.BIT_STRING

These instances can be assembled to create an ASN.1 tree::

    >>> x=ASN1_SEQUENCE([ASN1_INTEGER(7),ASN1_STRING("egg"),ASN1_SEQUENCE([ASN1_BOOLEAN(False)])])
    >>> x
    <ASN1_SEQUENCE[[<ASN1_INTEGER[7]>, <ASN1_STRING['egg']>, <ASN1_SEQUENCE[[<ASN1_BOOLEAN[False]>]]>]]>
    >>> x.show()
    # ASN1_SEQUENCE:
      <ASN1_INTEGER[7]>
      <ASN1_STRING['egg']>
      # ASN1_SEQUENCE:
        <ASN1_BOOLEAN[False]>

Encoding engines
^^^^^^^^^^^^^^^^^

As with the standard, ASN.1 and encoding are independent. We have just seen how to create a compounded ASN.1 object. To encode or decode it, we need to choose an encoding rule. Scapy provides only BER for the moment (actually, it may be DER. DER looks like BER except only minimal encoding is authorised which may well be what I did). I call this an ASN.1 codec.

Encoding and decoding are done using class methods provided by the codec. For example the ``BERcodec_INTEGER`` class provides a ``.enc()`` and a ``.dec()`` class methods that can convert between an encoded string and a value of their type. They all inherit from BERcodec_Object which is able to decode objects from any type::

    >>> BERcodec_INTEGER.enc(7)
    '\x02\x01\x07'
    >>> BERcodec_BIT_STRING.enc("egg")
    '\x03\x03egg'
    >>> BERcodec_STRING.enc("egg")
    '\x04\x03egg'
    >>> BERcodec_STRING.dec('\x04\x03egg')
    (<ASN1_STRING['egg']>, '')
    >>> BERcodec_STRING.dec('\x03\x03egg')
    Traceback (most recent call last):
      File "<console>", line 1, in ?
      File "/usr/bin/scapy", line 2099, in dec
        return cls.do_dec(s, context, safe)
      File "/usr/bin/scapy", line 2178, in do_dec
        l,s,t = cls.check_type_check_len(s)
      File "/usr/bin/scapy", line 2076, in check_type_check_len
        l,s3 = cls.check_type_get_len(s)
      File "/usr/bin/scapy", line 2069, in check_type_get_len
        s2 = cls.check_type(s)
      File "/usr/bin/scapy", line 2065, in check_type
        (cls.__name__, ord(s[0]), ord(s[0]),cls.tag), remaining=s)
    BER_BadTag_Decoding_Error: BERcodec_STRING: Got tag [3/0x3] while expecting <ASN1Tag STRING[4]>
    ### Already decoded ###
    None
    ### Remaining ###
    '\x03\x03egg'
    >>> BERcodec_Object.dec('\x03\x03egg')
    (<ASN1_BIT_STRING['egg']>, '')

ASN.1 objects are encoded using their ``.enc()`` method. This method must be called with the codec we want to use. All codecs are referenced in the ASN1_Codecs object. ``raw()`` can also be used. In this case, the default codec (``conf.ASN1_default_codec``) will be used.

::

    >>> x.enc(ASN1_Codecs.BER)
