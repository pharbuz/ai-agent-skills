
For instance, here is how :class:`~scapy.pipetool.CLIHighFeeder` is implemented:

.. code:: python3

    class CLIFeeder(CLIFeeder):
        def send(self, msg):
            self._gen_high_data(msg)
        def close(self):
            self.is_exhausted = True

Drains
^^^^^^

Default Drain classes
~~~~~~~~~~~~~~~~~~~~~

Drains need to be linked on the entry that you are using. It can be either on the lower one (using ``>``) or the upper one (using ``>>``).
See the basic example above.

- :class:`~scapy.pipetool.Drain` : the most basic Drain possible. Will pass on both low and high entry if linked properly.
- :class:`~scapy.pipetool.TransformDrain` : Apply a function to messages on low and high entry
- :class:`~scapy.pipetool.UpDrain` : Repeat messages from low entry to high exit
- :class:`~scapy.pipetool.DownDrain` : Repeat messages from high entry to low exit

Create a custom Drain
~~~~~~~~~~~~~~~~~~~~~

To create a custom drain, one must extend the :class:`~scapy.pipetool.Drain` class.

A :class:`~scapy.pipetool.Drain` object will receive data from the lower canal in its ``push`` method, and from the higher canal from its ``high_push`` method.

To send the data back into the next linked Drain / Sink, it must call the ``self._send(msg)`` or ``self._high_send(msg)`` methods.

For instance, here is how :class:`~scapy.pipetool.TransformDrain` is implemented::

    class TransformDrain(Drain):
        def __init__(self, f, name=None):
            Drain.__init__(self, name=name)
            self.f = f
        def push(self, msg):
            self._send(self.f(msg))
        def high_push(self, msg):
            self._high_send(self.f(msg))

Sinks
^^^^^

Sinks are destinations for messages.

A :py:class:`~scapy.pipetool.Sink` receives data like a :py:class:`~scapy.pipetool.Drain`, but doesn't send any
messages after it.

Messages on the low entry come from :py:meth:`~scapy.pipetool.Sink.push`, and messages on the
high entry come from :py:meth:`~scapy.pipetool.Sink.high_push`.

Default Sinks classes
~~~~~~~~~~~~~~~~~~~~~

- :class:`~scapy.pipetool.ConsoleSink` : Print messages on low and high entries to ``stdout``
- :class:`~scapy.pipetool.RawConsoleSink` : Print messages on low and high entries, using os.write
- :class:`~scapy.pipetool.TermSink` : Prints messages on the low and high entries, on a separate terminal
- :class:`~scapy.pipetool.QueueSink` : Collects messages on the low and high entries into a :py:class:`Queue`

Create a custom Sink
~~~~~~~~~~~~~~~~~~~~

To create a custom sink, one must extend :py:class:`~scapy.pipetool.Sink` and implement
:py:meth:`~scapy.pipetool.Sink.push` and/or :py:meth:`~scapy.pipetool.Sink.high_push`.

This is a simplified version of :py:class:`~scapy.pipetool.ConsoleSink`:

.. code-block:: python3

    class ConsoleSink(Sink):
        def push(self, msg):
            print(">%r" % msg)
        def high_push(self, msg):
            print(">>%r" % msg)

Link objects
------------

As shown in the example, most sources can be linked to any drain, on both low
and high entry.

The use of ``>`` indicates a link on the low entry, and ``>>`` on the high
entry.

For example, to link ``a``, ``b`` and ``c`` on the low entries:

.. code-block:: pycon

    >>> a = CLIFeeder()
    >>> b = Drain()
    >>> c = ConsoleSink()
    >>> a > b > c
    >>> p = PipeEngine()
    >>> p.add(a)

This wouldn't link the high entries, so something like this would do nothing:

.. code-block:: pycon

    >>> a2 = CLIHighFeeder()
    >>> a2 >> b
    >>> a2.send("hello")

Because ``b`` (:py:class:`~scapy.pipetool.Drain`) and ``c`` (:py:class:`scapy.pipetool.ConsoleSink`) are not
linked on the high entry.

However, using a :py:class:`~scapy.pipetool.DownDrain` would bring the high messages from
:py:class:`~scapy.pipetool.CLIHighFeeder` to the lower channel:

.. code-block:: pycon

    >>> a2 = CLIHighFeeder()
    >>> b2 = DownDrain()
    >>> a2 >> b2
    >>> b2 > b
    >>> a2.send("hello")

The PipeEngine class
--------------------

The :class:`~scapy.pipetool.PipeEngine` class is the core class of the Pipetool system. It must be initialized and passed the list of all Sources.

There are two ways of passing sources:

- during initialization: ``p = PipeEngine(source1, source2, ...)``
- using the ``add(source)`` method

A :class:`~scapy.pipetool.PipeEngine` class must be started with ``.start()`` function. It may be force-stopped with the ``.stop()``, or cleanly stopped with ``.wait_and_stop()``

A clean stop only works if the Sources is exhausted (has no data to send left).

It can be printed into a graph using ``.graph()`` methods. see ``help(do_graph)`` for the list of available keyword arguments.

Scapy advanced PipeTool objects
-------------------------------

.. note:: Unlike the previous objects, those are not located in ``scapy.pipetool`` but in ``scapy.scapypipes``

Now that you know the default PipeTool objects, here are some more advanced ones, based on packet functionalities.

- :class:`~scapy.scapypipes.SniffSource` : Read packets from an interface and send them to low exit.
- :class:`~scapy.scapypipes.RdpcapSource` : Read packets from a PCAP file send them to low exit.
- :class:`~scapy.scapypipes.InjectSink` : Packets received on low input are injected (sent) to an interface
- :class:`~scapy.scapypipes.WrpcapSink` : Packets received on low input are written to PCAP file
- :class:`~scapy.scapypipes.UDPDrain` : UDP payloads received on high entry are sent over UDP (complicated, have a look at ``help(UDPDrain)``)
- :class:`~scapy.scapypipes.FDSourceSink` : Use a file descriptor as source and sink
- :class:`~scapy.scapypipes.TCPConnectPipe`: TCP connect to addr:port and use it as source and sink
- :class:`~scapy.scapypipes.TCPListenPipe` : TCP listen on [addr:]port and use the first connection as source and sink (complicated, have a look at ``help(TCPListenPipe)``)

Triggering
----------

Some special sort of Drains exists: the Trigger Drains.

Trigger Drains are special drains, that on receiving data not only pass it by but also send a "Trigger" input, that is received and handled by the next triggered drain (if it exists).
