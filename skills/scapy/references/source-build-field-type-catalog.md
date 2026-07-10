

We are now able to understand all the magic behind it!

::

    >>> p = Foo()/Bar1(val=0x1337)
    >>> p
    <Foo  type=1 |<Bar1  val=4919 |>>
    >>> p.show()
    ###[ Foo ]###
      type= 1
      len= 4
      sep= '\r\n'
    ###[ Bar1 ]###
        val= 4919
        
Our 2 problems have been solved without us doing much: so good to be
lazy :)

Under the hood: putting everything together
-------------------------------------------

Last but not least, it is very useful to understand when each function
is called when a packet is built::

    >>> hexdump(raw(p))
    Packet.str=Foo
    Packet.iter=Foo
    Packet.iter=Bar1
    Packet.build=Foo
    Packet.build=Bar1
    Packet.post_build=Bar1
    Packet.post_build=Foo

As you can see, it first runs through the list of each field, and then
build  them starting  from the  beginning. Once  all layers  have been
built, it then calls ``post_build()`` starting from the end.


Fields 
======

.. index::
   single: fields

Here's a list of fields that Scapy supports out of the box:     

Simple datatypes
----------------

Legend: 

- ``X`` - hexadecimal representation
- ``LE`` - little endian (default is big endian = network byte order)
- ``Signed`` - signed (default is unsigned)

::

    ByteField           
    XByteField    
    
    ShortField
    SignedShortField
    LEShortField
    XShortField
    
    X3BytesField        # three bytes as hex
    XLE3BytesField      # little endian three bytes as hex
    ThreeBytesField     # three bytes as decimal
    LEThreeBytesField   # little endian three bytes as decimal
    LE3BytesEnumField
    XLE3BytesEnumField

    IntField
    SignedIntField
    LEIntField
    LESignedIntField
    XIntField
    
    LongField
    SignedLongField
    LELongField
    LESignedLongField
    XLongField
    LELongField
    
    IEEEFloatField
    IEEEDoubleField 
    BCDFloatField       # binary coded decimal
    
    BitField
    XBitField
    
    BitFieldLenField    # BitField specifying a length (used in RTP)
    FlagsField          
    FloatField

Enumerations
------------

Possible field values are taken from a given enumeration (list, dictionary, ...)  
e.g.::

    ByteEnumField("code", 4, {1:"REQUEST",2:"RESPONSE",3:"SUCCESS",4:"FAILURE"})

::

    EnumField(name, default, enum, fmt = "H")
    CharEnumField
    BitEnumField
    ShortEnumField
    LEShortEnumField
    ByteEnumField
    IntEnumField
    SignedIntEnumField
    LEIntEnumField
    XShortEnumField

Strings
-------

::

    StrField(name, default, fmt="H", remain=0, shift=0)
    StrLenField(name, default, fld=None, length_from=None, shift=0):
    StrFixedLenField
    StrNullField
    StrStopField

Lists and lengths
-----------------

::

    FieldList(name, default, field, fld=None, shift=0, length_from=None, count_from=None)
      # A list assembled and dissected with many times the same field type
        
      # field: instance of the field that will be used to assemble and disassemble a list item
      # length_from: name of the FieldLenField holding the list length
         
    FieldLenField     #  holds the list length of a FieldList field
    LEFieldLenField
    
    LenField          # contains len(pkt.payload)
    
    PacketField       # holds packets
    PacketLenField    # used e.g. in ISAKMP_payload_Proposal
    PacketListField


Variable length fields
^^^^^^^^^^^^^^^^^^^^^^

This is about how fields that have a variable length can be handled with Scapy. These fields usually know their length from another field. Let's call them varfield and lenfield. The idea is to make each field reference the other so that when a packet is dissected, varfield can know its length from lenfield when a packet is assembled, you don't have to fill lenfield, that will deduce its value directly from varfield value.

Problems arise when you realize that the relation between lenfield and varfield is not always straightforward. Sometimes, lenfield indicates a length in bytes, sometimes a number of objects. Sometimes the length includes the header part, so that you must subtract the fixed header length to deduce the varfield length. Sometimes the length is not counted in bytes but in 16bits words. Sometimes the same lenfield is used by two different varfields. Sometimes the same varfield is referenced by two lenfields, one in bytes one in 16bits words.

 
The length field
~~~~~~~~~~~~~~~~
