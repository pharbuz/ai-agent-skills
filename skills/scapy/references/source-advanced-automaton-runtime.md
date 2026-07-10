
.. note:: If you want to pass a parameter to an action, you can use the ``action_parameters`` function while raising the next state.

In the following example, the ``send_copy`` action takes a parameter passed by ``is_fin``::

    class Example(Automaton):
        @ATMT.state()
        def WAITING(self):
            pass

        @ATMT.state()
        def FIN_RECEIVED(self):
            pass

        @ATMT.receive_condition(WAITING)
        def is_fin(self, pkt):
            if pkt[TCP].flags.F:
                raise self.FIN_RECEIVED().action_parameters(pkt)

        @ATMT.action(is_fin)
        def send_copy(self, pkt):
            send(pkt)


Methods to overload
^^^^^^^^^^^^^^^^^^^

Two methods are hooks to be overloaded:

* The ``parse_args()`` method is called with arguments given at ``__init__()`` and ``run()``. Use that to parametrize the behavior of your automaton.

* The ``master_filter()`` method is called each time a packet is sniffed and decides if it is interesting for the automaton. When working on a specific protocol, this is where you will ensure the packet belongs to the connection you are being part of, so that you do not need to make all the sanity checks in each transition.

Timer configuration
^^^^^^^^^^^^^^^^^^^

Some protocols allow timer configuration. In order to configure timeout values during class initialization one may use ``timer_by_name()`` method, which returns ``Timer`` object associated with the given function name::

    class Example(Automaton):
	def __init__(self, *args, **kwargs):
	    super(Example, self).__init__(*args, **kwargs)
	    timer = self.timer_by_name("waiting_timeout")
	    timer.set(1)

	@ATMT.state(initial=1)
	def WAITING(self):
	    pass

	@ATMT.state(final=1)
	def END(self):
	    pass

	@ATMT.timeout(WAITING, 10.0)
	def waiting_timeout(self):
	    raise self.END()
