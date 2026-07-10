- ``do_dissect()`` perform the real dissection of the layer.
- ``post_dissection()`` is  called when some  updates are needed  on the
  dissected inputs (e.g. deciphering, uncompressing, ... )
- ``extract_padding()`` is an important  function which should be called
  by every  layer containing  its own size, so that it can tell apart 
  in  the payload what is really related to this layer and what will
  be considered as additional padding bytes.
- ``do_dissect_payload()``  is the  function in  charge of  dissecting the
  payload  (if  any).  It   is  based  on  ``guess_payload_class()``  (see
  below). Once the type of the  payload is known, the payload is bound
  to the current layer with this new type::

      def do_dissect_payload(self, s):
          cls = self.guess_payload_class(s)
          p = cls(s, _internal=1, _underlayer=self)
          self.add_payload(p)

At the  end, all  the layers  in the packet  are dissected,  and glued
together with their known types.


Dissecting fields
-----------------

The  method with  all the  magic  between a  layer and  its fields  is
``do_dissect()``. If you have  understood the different representations of
a layer, you  should understand that "dissecting" a  layer is building
each of its fields from the machine to the internal representation. 

Guess what? That is exactly what ``do_dissect()`` does::

    def do_dissect(self, s):
        flist = self.fields_desc[:]
        flist.reverse()
        while s and flist:
            f = flist.pop()
            s,fval = f.getfield(self, s)
            self.fields[f] = fval
        return s

So, it  takes the raw string packet,  and feed each field  with it, as
long as there are data or fields remaining::

    >>> FOO("\xff\xff"+"B"*8)
    <FOO  len=2097090 data='BBBBBBB' |>

When writing ``FOO("\xff\xff"+"B"*8)``, it calls ``do_dissect()``. The first
field is VarLenQField.  Thus, it takes bytes as long as their MSB is
set, thus until (and including) the first '``B``'. This mapping is done
thanks to ``VarLenQField.getfield()`` and can be cross-checked::

    >>> vlenq2str(2097090)
    '\xff\xffB'

Then, the  next field is extracted  the same way, until 2097090 bytes
are put in ``FOO.data`` (or less  if 2097090 bytes are  not available, as
here).

If  there are  some bytes  left after  the dissection  of  the current
layer, it is mapped  in the same way to the what  the next is expected
to be (``Raw`` by default)::

    >>> FOO("\x05"+"B"*8)
    <FOO  len=5 data='BBBBB' |<Raw  load='BBB' |>>

Hence, we need now to understand how layers are bound together.

Binding layers
--------------

One of the cool features with Scapy when dissecting layers is that it
tries to guess for us what the next layer is. The official way to link 2
layers is using ``bind_layers()`` function.

Available inside the ``packet`` module, this function can be used as following::

    bind_layers(ProtoA, ProtoB, FieldToBind=Value)

Each time a packet ``ProtoA()/ProtoB()`` will be created, the ``FieldToBind`` of
``ProtoA`` will be equal to ``Value``.

For instance,  if you have a class ``HTTP``, you may expect  that all the
packets coming from or going to  port 80 will be decoded as such. This
is simply done that way::

    bind_layers( TCP, HTTP, sport=80 )
    bind_layers( TCP, HTTP, dport=80 )

That's  all folks!  Now every  packet  related to  port  80 will  be
associated to the  layer ``HTTP``, whether it is read from  a pcap file or
received from the network.

The ``guess_payload_class()`` way
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes,  guessing the payload  class is  not as  straightforward as
defining a single  port. For instance, it can depend on  a value of a
given byte in the current layer. The 2 needed methods are:

- ``guess_payload_class()`` which must return  the guessed class for the
  payload (next layer). By default, it uses links between classes
  that have been put in place by ``bind_layers()``.

- ``default_payload_class()``  which returns  the  default value.   This
  method  defined in the  class ``Packet``  returns ``Raw``,  but it  can be
  overloaded.

For  instance, decoding  802.11  changes depending  on  whether it  is
ciphered or not::

    class Dot11(Packet):
        def guess_payload_class(self, payload):
            if self.FCfield & 0x40:
                return Dot11WEP
            else:
                return Packet.guess_payload_class(self, payload)

Several comments are needed here:

- this  cannot be  done  using  ``bind_layers()``  because the  tests  are
  supposed to be "``field==value``", but it is more complicated here as we
  test a single bit in the value of a field.
  
- if the  test fails, no assumption is  made, and we plug  back to the
  default guessing mechanisms calling ``Packet.guess_payload_class()``

Most of  the time,  defining a method  ``guess_payload_class()`` is  not a
necessity as the same result can be obtained from ``bind_layers()``.

Changing the default behavior
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you do not like Scapy's  behavior for a given layer, you can either
change or disable it through  a call to ``split_layers()``. For instance,
if you do not want UDP/53 to be bound with ``DNS``, just add in your code::

    split_layers(UDP, DNS, sport=53)

Now every packet  with source port 53 will not be  handled as DNS, but
whatever you specify instead.



Under the hood: putting everything together
-------------------------------------------

In  fact, each  layer  has a  field  payload_guess. When  you use  the
bind_layers() way, it adds the defined next layers to that list.

::

    >>> p=TCP()
    >>> p.payload_guess
    [({'dport': 2000}, <class 'scapy.Skinny'>), ({'sport': 2000}, <class 'scapy.Skinny'>), ... )]

Then,  when it  needs to  guess  the next  layer class,  it calls  the
default method ``Packet.guess_payload_class()``.  This method runs through
each  element  of  the   list  payload_guess,  each  element  being  a
tuple:
