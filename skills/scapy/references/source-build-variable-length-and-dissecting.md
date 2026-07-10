
      class StrFixedLenField(StrField):
          def addfield(self, pkt, s, val):
              return s+struct.pack("%is"%self.length,self.i2m(pkt, val))

- ``getfield(self, pkt, s)``: extract from the raw packet ``s`` the field
  value belonging to layer ``pkt``. It returns a list, the 1st element
  is the raw packet string after having removed the extracted field,
  the second one is the extracted field itself in internal
  representation::

      class StrFixedLenField(StrField):
          def getfield(self, pkt, s):
              return s[self.length:], self.m2i(pkt,s[:self.length])
       
When defining your own layer, you usually just need to define some
``*2*()`` methods, and sometimes also the ``addfield()`` and ``getfield()``.


Example: variable length quantities
-----------------------------------

There is a way to represent integers on a variable length quantity often
used in  protocols, for instance  when dealing with  signal processing
(e.g. MIDI). 

Each byte  of the number is  coded with the  MSB set to 1,  except the
last byte. For instance, 0x123456 will be coded as 0xC8E856:: 

    def vlenq2str(l):
        s = []
        s.append(l & 0x7F)
        l = l >> 7
        while l > 0:
            s.append( 0x80 | (l & 0x7F) )
            l = l >> 7
        s.reverse()
        return bytes(bytearray(s))
    
    def str2vlenq(s=b""):
        i = l = 0
        while i < len(s) and ord(s[i:i+1]) & 0x80:
            l = l << 7
            l = l + (ord(s[i:i+1]) & 0x7F)
            i = i + 1
        if i == len(s):
            warning("Broken vlenq: no ending byte")
        l = l << 7
        l = l + (ord(s[i:i+1]) & 0x7F)
    
        return s[i+1:], l

We will  define a field which  computes automatically the  length of an
associated string, but used that encoding format::

    class VarLenQField(Field):
        """ variable length quantities """
        __slots__ = ["fld"]
    
        def __init__(self, name, default, fld):
            Field.__init__(self, name, default)
            self.fld = fld
            
        def i2m(self, pkt, x):
            if x is None:
                f = pkt.get_field(self.fld)
                x = f.i2len(pkt, pkt.getfieldval(self.fld))
                x = vlenq2str(x)
            return raw(x)
    
        def m2i(self, pkt, x):
            if s is None:
                return None, 0
            return str2vlenq(x)[1]
    
        def addfield(self, pkt, s, val):
            return s+self.i2m(pkt, val)
    
        def getfield(self, pkt, s):
            return str2vlenq(s)

And now, define a layer using this kind of field::

    class FOO(Packet):
        name = "FOO"
        fields_desc = [ VarLenQField("len", None, "data"),
                        StrLenField("data", "", length_from=lambda pkt: pkt.len) ]
    
    >>> f = FOO(data="A"*129)
    >>> f.show()
    ###[ FOO ]###
      len= None
      data=    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

Here, ``len``  has yet to be computed and only the default value is
displayed. This is the current internal representation of our
layer. Let's force the computation now::

    >>> f.show2()
    ###[ FOO ]###
      len= 129
      data= 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

The method ``show2()`` displays the fields with their values as they will
be sent to the network, but in a human readable way, so we see ``len=129``.
Last but not least, let us look now at the machine representation::

    >>> raw(f)
    '\x81\x01AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

The first 2 bytes are ``\x81\x01``, which is 129 in this encoding.


 
Dissecting 
==========
.. index::
   dissecting
   
Layers only are list of fields, but what is the glue between each
field, and after, between each  layer. These are the mysteries explain
in this section.

The basic stuff
---------------

The core function for dissection is ``Packet.dissect()``::

    def dissect(self, s):
        s = self.pre_dissect(s)
        s = self.do_dissect(s)
        s = self.post_dissect(s)            
        payl,pad = self.extract_padding(s)
        self.do_dissect_payload(payl)
        if pad and conf.padding:
            self.add_payload(Padding(pad))

When called, ``s`` is a string containing what is going to be
dissected. ``self`` points to the current layer.
 
::

    >>> p=IP("A"*20)/TCP("B"*32)
    WARNING: bad dataofs (4). Assuming dataofs=5
    >>> p
    <IP  version=4L ihl=1L tos=0x41 len=16705 id=16705 flags=DF frag=321L ttl=65 proto=65 chksum=0x4141
    src=65.65.65.65 dst=65.65.65.65 |<TCP  sport=16962 dport=16962 seq=1111638594L ack=1111638594L dataofs=4L
    reserved=2L flags=SE window=16962 chksum=0x4242 urgptr=16962 options=[] |<Raw  load='BBBBBBBBBBBB' |>>>

``Packet.dissect()`` is called 3 times:

1. to dissect the ``"A"*20`` as an IPv4 header
2. to dissect the ``"B"*32`` as a TCP header
3. and  since  there  are still  12  bytes  in  the packet,  they  are
   dissected as "``Raw``" data (which is some kind of default layer type)


For a given layer, everything is quite straightforward:

- ``pre_dissect()`` is called to prepare the layer.
