# Source: build_dissect

********************
Adding new protocols
********************

Adding a new protocol (or more correctly: a new *layer*) in Scapy is very easy. All the magic is in the fields. If the 
fields you need are already there and the protocol is not too brain-damaged, 
this should be a matter of minutes. 

Simple example
==============

A layer is a subclass of the ``Packet`` class. All the logic behind layer manipulation 
is held by the ``Packet`` class and will be inherited. 
A simple layer is compounded by a list of fields that will be either concatenated 
when assembling the layer or dissected one by one when disassembling a string. 
The list of fields is held in an attribute named ``fields_desc``. Each field is an instance 
of a field class:: 

    class Disney(Packet): 
        name = "DisneyPacket " 
        fields_desc=[ ShortField("mickey",5), 
                     XByteField("minnie",3) , 
                     IntEnumField("donald" , 1 , 
                          { 1: "happy", 2: "cool" , 3: "angry" } ) ]
                       
In this example, our layer has three fields. The first one is a 2-byte integer 
field named ``mickey`` and whose default value is 5. The second one is a 1-byte 
integer field named ``minnie`` and whose default value is 3. The difference between 
a vanilla ``ByteField`` and an ``XByteField`` is only the fact that the preferred human 
representation of the field’s value is in hexadecimal. The last field is a 4-byte 
integer field named ``donald``. It is different from a vanilla ``IntField`` by the fact 
that some of the possible values of the field have literate representations. For 
example, if it is worth 3, the value will be displayed as angry. Moreover, if the 
"cool" value is assigned to this field, it will understand that it has to take the 
value 2. 

If your protocol is as simple as this, it is ready to use:: 

    >>> d=Disney(mickey=1) 
    >>> ls(d) 
    mickey : ShortField = 1 (5) 
    minnie : XByteField = 3 (3) 
    donald : IntEnumField = 1 (1) 
    >>> d.show() 
    ###[ Disney Packet ]### 
    mickey= 1 
    minnie= 0x3 
    donald= happy 
    >>> d.donald="cool" 
    >>> raw(d)
    ’\x00\x01\x03\x00\x00\x00\x02’ 
    >>> Disney(_) 
    <Disney mickey=1 minnie=0x3 donald=cool |> 


This chapter explains how to build a new protocol within Scapy. There are two main objectives:

* Dissecting: this is done when a packet is received (from the network or a file) and should be converted to Scapy’s internals.
* Building: When one wants to send such a new packet, some stuff needs to be adjusted automatically in it.

Layers
======

Before digging into dissection itself, let us look at how packets are
organized.

::

    >>> p = IP()/TCP()/"AAAA"
    >>> p
    <IP  frag=0 proto=TCP |<TCP  |<Raw  load='AAAA' |>>>
    >>> p.summary()
    'IP / TCP 127.0.0.1:ftp-data > 127.0.0.1:www S / Raw'

We are interested in 2 "inside" fields of the class ``Packet``:

* ``p.underlayer``
* ``p.payload``

And here  is the  main "trick".  You do not  care about  packets, only
about layers, stacked one after the other. 

One can easily  access a layer by its name: ``p[TCP]`` returns the ``TCP``
and following layers. This is a shortcut for ``p.getlayer(TCP)``.

.. note::
   There is  an optional argument (``nb``) which returns  the ``nb`` th  layer of required protocol.

Let's put everything together now, playing with the ``TCP`` layer::

    >>> tcp=p[TCP]
    >>> tcp.underlayer
    <IP  frag=0 proto=TCP |<TCP  |<Raw  load='AAAA' |>>>
    >>> tcp.payload
    <Raw  load='AAAA' |>

As expected, ``tcp.underlayer`` points to the beginning of our IP packet,
and ``tcp.payload`` to its payload.

Building a new layer
--------------------

.. index::
   single: Layer

VERY EASY! A layer is mainly a list of fields. Let's look at ``UDP`` definition::

    class UDP(Packet):
        name = "UDP"
        fields_desc = [ ShortEnumField("sport", 53, UDP_SERVICES),
                        ShortEnumField("dport", 53, UDP_SERVICES),
                        ShortField("len", None),
                        XShortField("chksum", None), ]

And you are done! There are many fields already defined for
convenience, look at the doc``^W`` sources as Phil would say.

So, defining a layer is simply gathering fields in a list. The goal is
here to  provide the  efficient default values  for each field  so the
user does not have to give them when he builds a packet. 

The main  mechanism  is based on  the ``Field`` structure.  Always keep in
mind that a layer is just a little more than a list of fields, but not
much more. 

So, to understand how layers are working, one needs to look quickly
at how the fields are handled.


Manipulating packets == manipulating its fields
-----------------------------------------------

.. index::
   single: i2h()
   single: i2m()
   single: m2i()

A field should be considered in different states:

- ``i`` (nternal) : this is the way Scapy manipulates it.
- ``m`` (achine) : this is where the truth is, that is the layer as it is
    on the network.
- ``h`` (uman) : how the packet is displayed to our human eyes.

This explains  the mysterious  methods ``i2h()``, ``i2m()``,  ``m2i()`` and  so on
available  in  each field:  they are the conversion  from one  state  to
another, adapted to a specific use.

Other special functions:

- ``any2i()`` guess the input representation and returns the internal one.
- ``i2repr()`` a nicer ``i2h()``

However, all these are "low level" functions. The functions adding or
extracting a field to the current layer are:

- ``addfield(self, pkt, s, val)``:  copy the network  representation of
  field ``val`` (belonging to layer ``pkt``) to the raw string packet ``s``::
