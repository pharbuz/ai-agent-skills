# Source: advanced_usage/pipetools

.. _pipetools:

PipeTools
=========

Scapy's ``pipetool`` is a smart piping system allowing to perform complex stream data management.

The goal is to create a sequence of steps with one or several inputs and one or several outputs, with a bunch of blocks in between.
PipeTools can handle varied sources of data (and outputs) such as user input, pcap input, sniffing, wireshark...
A pipe system is implemented by manually linking all its parts. It is possible to dynamically add an element while running or set multiple drains for the same source.

.. note:: Pipetool default objects are located inside ``scapy.pipetool``

Demo: sniff, anonymize, send to Wireshark
-----------------------------------------

The following code will sniff packets on the default interface, anonymize the source and destination IP addresses and pipe it all into Wireshark. Useful when posting online examples, for instance.

.. code-block:: python3

    source = SniffSource(iface=conf.iface)
    wire = WiresharkSink()
    def transf(pkt):
        if not pkt or IP not in pkt:
            return pkt
        pkt[IP].src = "1.1.1.1"
        pkt[IP].dst = "2.2.2.2"
        return pkt

    source > TransformDrain(transf) > wire
    p = PipeEngine(source)
    p.start()
    p.wait_and_stop()

The engine is pretty straightforward:

.. image:: ../graphics/pipetool_demo.svg

Let's run it:

.. image:: ../graphics/animations/pipetool_demo.gif

Class Types
-----------

There are 3 different class of objects used for data management:

- ``Sources``
- ``Drains``
- ``Sinks``

They are executed and handled by a :class:`~scapy.pipetool.PipeEngine` object.

When running, a pipetool engine waits for any available data from the Source, and send it in the Drains linked to it.
The data then goes from Drains to Drains until it arrives in a Sink, the final state of this data.

Let's see with a basic demo how to build a pipetool system.

.. image:: ../graphics/pipetool_engine.png

For instance, this engine was generated with this code:

.. code:: pycon

    >>> s = CLIFeeder()
    >>> s2 = CLIHighFeeder()
    >>> d1 = Drain()
    >>> d2 = TransformDrain(lambda x: x[::-1])
    >>> si1 = ConsoleSink()
    >>> si2 = QueueSink()
    >>> 
    >>> s > d1
    >>> d1 > si1
    >>> d1 > si2
    >>> 
    >>> s2 >> d1
    >>> d1 >> d2
    >>> d2 >> si1
    >>> 
    >>> p = PipeEngine()
    >>> p.add(s)
    >>> p.add(s2)
    >>> p.graph(target="> the_above_image.png")

``start()`` is used to start the :class:`~scapy.pipetool.PipeEngine`:

.. code:: pycon

    >>> p.start()

Now, let's play with it by sending some input data

.. code:: pycon

    >>> s.send("foo")
    >'foo'
    >>> s2.send("bar")
    >>'rab'
    >>> s.send("i like potato")
    >'i like potato'
    >>> print(si2.recv(), ":", si2.recv())
    foo : i like potato

Let's study what happens here:

- there are **two canals** in a :class:`~scapy.pipetool.PipeEngine`, a lower one and a higher one. Some Sources write on the lower one, some on the higher one and some on both.
- most sources can be linked to any drain, on both lower and higher canals. The use of ``>`` indicates a link on the low canal, and ``>>`` on the higher one.
- when we send some data in ``s``, which is on the lower canal, as shown above, it goes through the :class:`~scapy.pipetool.Drain` then is sent to the :class:`~.scapy.pipetool.QueueSink` and to the :class:`~scapy.pipetool.ConsoleSink`
- when we send some data in ``s2``, it goes through the Drain, then the TransformDrain where the data is reversed (see the lambda), before being sent to :class:`~scapy.pipetool.ConsoleSink` only. This explains why we only have the data of the lower sources inside the QueueSink: the higher one has not been linked.

Most of the sinks receive from both lower and upper canals. This is verifiable using the `help(ConsoleSink)`

.. code:: pycon

    >>> help(ConsoleSink)
    Help on class ConsoleSink in module scapy.pipetool:
    class ConsoleSink(Sink)
     |  Print messages on low and high entries
     |     +-------+
     |  >>-|--.    |->>
     |     | print |
     |   >-|--'    |->
     |     +-------+
     |
     [...]


Sources
^^^^^^^

A Source is a class that generates some data.

There are several source types integrated with Scapy, usable as-is, but you may
also create yours.

Default Source classes
~~~~~~~~~~~~~~~~~~~~~~

For any of those class, have a look at ``help([theclass])`` to get more information or the required parameters.

- :class:`~scapy.pipetool.CLIFeeder` : a source especially used in interactive software. its ``send(data)`` generates the event data on the lower canal
- :class:`~scapy.pipetool.CLIHighFeeder` : same than CLIFeeder, but writes on the higher canal
- :class:`~scapy.pipetool.PeriodicSource` : Generate messages periodically on the low canal.
- :class:`~scapy.pipetool.AutoSource`: the default source, that must be extended to create custom sources. 

Create a custom Source
~~~~~~~~~~~~~~~~~~~~~~

To create a custom source, one must extend the :class:`~scapy.pipetool.AutoSource` class.

.. note::

    Do NOT use the default :class:`~scapy.pipetool.Source` class except if you are really sure of what you are doing: it is only used internally, and is missing some implementation. The :class:`~scapy.pipetool.AutoSource` is made to be used.


To send data through it, the object must call its ``self._gen_data(msg)`` or ``self._gen_high_data(msg)`` functions, which send the data into the PipeEngine.

The Source should also (if possible), set ``self.is_exhausted`` to ``True`` when empty, to allow the clean stop of the :class:`~scapy.pipetool.PipeEngine`. If the source is infinite, it will need a force-stop (see PipeEngine below)
