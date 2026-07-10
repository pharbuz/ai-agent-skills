
    class Foo(Packet):
          fields_desc = [
              ByteField("type", 0),
              XNumberField("len", None, "\r\n"),
              StrFixedLenField("sep", "\r\n", 2)
              ]
            
          def post_build(self, p, pay):
            if self.len is None and pay:
                l = len(pay)
                p = p[:1] + struct.pack("!B", l) + p[2:]
            return p+pay

When ``post_build()`` is called, ``p``  is the current layer, ``pay`` the payload,
that is what has already been built. We want our length to be the full
length of the data put after  the separator, so we add its computation
in ``post_build()``. 

::

    >>> p = Foo()/("X"*32)
    >>> p.show2()
    ###[ Foo ]###
      type= 0
      len= 32
      sep= '\r\n'
    ###[ Raw ]###
         load= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

``len`` is correctly computed now::

    >>> hexdump(raw(p))
    0000   00 32 30 0D 0A 58 58 58  58 58 58 58 58 58 58 58   .20..XXXXXXXXXXX
    0010   58 58 58 58 58 58 58 58  58 58 58 58 58 58 58 58   XXXXXXXXXXXXXXXX
    0020   58 58 58 58 58                                     XXXXX

And the machine representation is the expected one.


Handling default values: automatic computation
----------------------------------------------

As we have previously seen, the dissection mechanism is built upon the
links between  the layers created  by the programmer. However,  it can
also be used during the building process.

In the  layer ``Foo()``, our  first byte is  the type, which  defines what
comes next, e.g. if ``type=0``, next layer is ``Bar0``, if it is 1, next layer
is  ``Bar1``,  and  so on.  We  would  like  then  this  field to  be  set
automatically according to what comes next.
 
::

    class Bar1(Packet):
        fields_desc = [
              IntField("val", 0),
              ]
    
    class Bar2(Packet):
        fields_desc = [
              IPField("addr", "127.0.0.1")
              ]

If we use  these classes with nothing else, we  will have trouble when
dissecting the  packets as nothing  binds Foo layer with  the multiple
``Bar*`` even when we explicitly build the packet through the call to
``show2()``::

    >>> p = Foo()/Bar1(val=1337)
    >>> p
    <Foo  |<Bar1  val=1337 |>>
    >>> p.show2()
    ###[ Foo ]###
      type= 0
      len= 4
      sep= '\r\n'
    ###[ Raw ]###
        load= '\x00\x00\x059'

Problems:
 
1. ``type`` is still  equal to 0 while we wanted  it to be automatically
   set to 1. We could of course have built ``p`` with ``p = Foo(type=1)/Bar0(val=1337)``
   but this is not very convenient.
   
2. the packet is badly dissected as ``Bar1`` is regarded as ``Raw``. This
   is because no links have been set between ``Foo()`` and ``Bar*()``.

In order to  understand what we should have done  to obtain the proper
behavior,  we must look  at how  the layers  are assembled.   When two
independent packets instances ``Foo()`` and ``Bar1(val=1337)`` are
compounded with the '/' operator, it results in a new packet where the
two previous instances are cloned  (i.e.  are now two distinct objects
structurally different, but holding the same values)::

    def __div__(self, other):
        if isinstance(other, Packet):
            cloneA = self.copy()
            cloneB = other.copy()
            cloneA.add_payload(cloneB)
            return cloneA
        elif type(other) is str:
            return self/Raw(load=other)

The right-hand side of the operator becomes the payload of the left-hand
side. This is performed through the call to ``add_payload()``. Finally, the new packet is returned.

Note: we can observe that if  other isn't a ``Packet`` but a string,
the ``Raw``  class is instantiated to  form the payload.  Like in this
example::

    >>> IP()/"AAAA"
    <IP  |<Raw  load='AAAA' |>>

Well, what  ``add_payload()`` should implement? Just  a link between
two packets? Not only, in our case, this method will appropriately set
the correct value to ``type``.

Instinctively  we feel that  the upper  layer (the  right of  '/') can
gather the  values to set the fields  to the lower layer  (the left of
'/').  Like  previously explained, there is a  convenient mechanism to
specify the bindings in  both directions between two neighboring
layers.

Once again, these information must be provided to ``bind_layers()``,
which  will   internally  call  ``bind_top_down()``   in  charge  to
aggregate the fields to overload. In our case what we need to specify
is::

    bind_layers( Foo, Bar1, {'type':1} )
    bind_layers( Foo, Bar2, {'type':2} )

Then, ``add_payload()``  iterates over the  ``overload_fields`` of
the upper packet (the payload), get the fields associated to the lower
packet (by its type) and insert them in ``overloaded_fields``.
 
For  now,   when  the   value  of  this   field  will   be  requested,
``getfieldval()``    will    return    the   value    inserted    in
``overloaded_fields``.

The fields are dispatched between three dictionaries:

- ``fields``: fields whose the value have been explicitly set, like
  ``pdst`` in TCP (``pdst='42'``)
- ``overloaded_fields``: overloaded fields
- ``default_fields``: all the fields with their default value (these fields 
    are initialized according to ``fields_desc`` by the constructor 
    by calling ``init_fields()`` ).

In the following code, we can observe how a field is selected and its
value returned::

    def getfieldval(self, attr):
       for f in self.fields, self.overloaded_fields, self.default_fields:
           if f.has_key(attr):
               return f[attr]
       return self.payload.getfieldval(attr)

Fields  inserted  in  ``fields``  have  the  higher  priority,  then
``overloaded_fields``, then finally ``default_fields``.  Hence, if
the field ``type`` is set in ``overloaded_fields``, its value will
be returned instead of the value contained in ``default_fields``.
