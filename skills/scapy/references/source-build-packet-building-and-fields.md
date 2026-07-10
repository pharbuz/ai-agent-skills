- the 1st value is a field to test (``'dport': 2000``)
- the 2nd value is the guessed class if it matches (``Skinny``)

So, the  default ``guess_payload_class()`` tries all element  in the list,
until  one   matches.  If  no   element  are  found,  it   then  calls
``default_payload_class()``. If you have redefined this method, then yours
is  called, otherwise,  the default  one is  called, and  ``Raw``  type is
returned. 

``Packet.guess_payload_class()``

- test what is in field ``guess_payload``
- call overloaded ``guess_payload_class()``


Building
========

Building a packet is as simple as building each layer. Then, some
magic happens to glue everything. Let's do magic then.

The basic stuff
---------------

The first thing to establish is: what does "build" mean? As we have seen, a
layer  can   be  represented  in  different   ways  (human,  internal,
machine). Building means going to the machine format.

The second thing to understand is ''when'' a layer is  built. The answer is not
that obvious, but as soon  as you need the machine representation, the
layers are built: when the packet is dropped on the network or written
to a file, or when it is converted as a string, ...  In  fact, machine
representation  should be  regarded as  a big  string with  the layers
appended altogether.
 
::

    >>> p = IP()/TCP()
    >>> hexdump(p)
    0000 45 00 00 28 00 01 00 00 40 06 7C CD 7F 00 00 01 E..(....@.|..... 
    0010 7F 00 00 01 00 14 00 50 00 00 00 00 00 00 00 00 .......P........ 
    0020 50 02 20 00 91 7C 00 00 P. ..|.. 

Calling ``raw()`` builds the packet:
  - non instanced fields are set to their default value
  - lengths are updated automatically
  - checksums are computed
  - and so on. 

In fact, using ``raw()`` rather than ``show2()`` or any other method
is not a random choice as all the functions building the packet calls
``Packet.__str__()`` (or ``Packet.__bytes__()`` under Python
3). However, ``__str__()`` calls another method: ``build()``::

    def __str__(self):
        return next(iter(self)).build()

What is important also to understand  is that usually, you do not care
about the machine  representation, that is why the  human and internal
representations are here. 

So, the  core method is ``build()``  (the code has been  shortened to keep
only the relevant parts)::

    def build(self,internal=0):
        pkt = self.do_build()
        pay = self.build_payload()
        p = self.post_build(pkt,pay)
        if not internal:
            pkt = self
            while pkt.haslayer(Padding):
                pkt = pkt.getlayer(Padding)
                p += pkt.load
                pkt = pkt.payload
        return p

So, it  starts by  building the current  layer, then the  payload, and
``post_build()``  is called  to update  some late  evaluated  fields (like
checksums). Last, the padding is added to the end of the packet. 

Of  course, building  a layer  is  the same  as building  each of  its
fields, and that is exactly what ``do_build()`` does.

Building fields
---------------

The building of each field of a layer is called in ``Packet.do_build()``::

    def do_build(self):
        p=""
        for f in self.fields_desc:
            p = f.addfield(self, p, self.getfieldval(f))
        return p

The  core function  to  build a  field  is ``addfield()``.   It takes  the
internal view of the  field and put it at the end  of ``p``. Usually, this
method calls  ``i2m()`` and returns something  like ``p.self.i2m(val)`` (where
``val=self.getfieldval(f)``).

If ``val`` is set, then ``i2m()`` is just a matter of formatting the value the
way it must  be. For instance, if a  byte is expected, ``struct.pack("B", val)``
is the right way to convert it.

However, things  are more complicated if  ``val`` is not set,  it means no
default  value was  provided  earlier,  and thus  the  field needs  to
compute some "stuff" right now or later. 

"Right now"  means thanks to ``i2m()``, if all pieces of information are
available.  For instance,  if  you have  to  handle a  length until  a
certain delimiter. 

Ex: counting the length until a delimiter

::

    class XNumberField(FieldLenField):
    
        def __init__(self, name, default, sep="\r\n"):
            FieldLenField.__init__(self, name, default, fld)
            self.sep = sep
    
        def i2m(self, pkt, x):
            x = FieldLenField.i2m(self, pkt, x)
            return "%02x" % x
    
        def m2i(self, pkt, x):
            return int(x, 16)
    
        def addfield(self, pkt, s, val):
            return s+self.i2m(pkt, val)
    
        def getfield(self, pkt, s):
            sep = s.find(self.sep)
            return s[sep:], self.m2i(pkt, s[:sep])

In this example,  in ``i2m()``, if ``x`` has already a  value, it is converted
to its hexadecimal value. If no value is given, a length of "0" is
returned.

The glue is provided by ``Packet.do_build()`` which calls ``Field.addfield()``
for  each field in  the layer,  which in  turn calls  ``Field.i2m()``: the
layer is built IF a value was available.


Handling default values: ``post_build``
---------------------------------------

A default  value for a  given field is  sometimes either not  known or
impossible to compute when the  fields are put together. For instance,
if we used a ``XNumberField`` as  defined previously in a layer, we expect
it  to be set  to a  given value  when the  packet is  built. However,
nothing is returned by ``i2m()`` if it is not set. 

The answer to this problem is ``Packet.post_build()``. 

When  this method is  called, the  packet is  already built,  but some
fields still need  to be computed. This is  typically what is required
to compute checksums or lengths. In fact, this is required each time a
field's value depends on something which is not in the current 

So, let  us assume we  have a packet  with a ``XNumberField``, and  have a
look to its building process::
