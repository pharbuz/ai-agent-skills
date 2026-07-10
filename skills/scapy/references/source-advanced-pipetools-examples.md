
For example, here is a basic :class:`~scapy.scapypipes.TriggerDrain` usage:

.. code:: pycon

    >>> a = CLIFeeder()
    >>> d = TriggerDrain(lambda msg: True) # Pass messages and trigger when a condition is met
    >>> d2 = TriggeredValve()
    >>> s = ConsoleSink()
    >>> a > d > d2 > s
    >>> d ^ d2 # Link the triggers
    >>> p = PipeEngine(s)
    >>> p.start()
    INFO: Pipe engine thread started.
    >>> 
    >>> a.send("this will be printed")
    >'this will be printed'
    >>> a.send("this won't, because the valve was switched")
    >>> a.send("this will, because the valve was switched again")
    >'this will, because the valve was switched again'
    >>> p.stop()

Several triggering Drains exist, they are pretty explicit. It is highly recommended to check the doc using ``help([the class])``

- :class:`~scapy.scapypipes.TriggeredMessage` : Send a preloaded message when triggered and trigger in chain
- :class:`~scapy.scapypipes.TriggerDrain` : Pass messages and trigger when a condition is met
- :class:`~scapy.scapypipes.TriggeredValve` : Let messages alternatively pass or not, changing on trigger
- :class:`~scapy.scapypipes.TriggeredQueueingValve` : Let messages alternatively pass or queued, changing on trigger
- :class:`~scapy.scapypipes.TriggeredSwitch` : Let messages alternatively high or low, changing on trigger
