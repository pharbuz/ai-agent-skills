    
        # RECEIVED
        @ATMT.state()
        def RECEIVING(self, pkt):
            recvd = pkt[Raw].load
            self.res += recvd
            self.awaiting += 1
            if len(recvd) == self.blocksize:
                raise self.WAITING()
            raise self.END()
    
        # ERROR
        @ATMT.state(error=1)
        def ERROR(self,pkt):
            split_bottom_up(UDP, TFTP, dport=self.my_tid)
            return pkt[TFTP_ERROR].summary()
        
        #END
        @ATMT.state(final=1)
        def END(self):
            split_bottom_up(UDP, TFTP, dport=self.my_tid)
            return self.res

It can be run like this, for instance::

    >>> atmt = TFTP_read("my_file", "192.168.1.128")
    >>> atmt.run()
    >>> atmt.destroy()

Detailed documentation
----------------------

Decorators
^^^^^^^^^^
Decorator for states
~~~~~~~~~~~~~~~~~~~~

States are methods decorated by the result of the ``ATMT.state`` function. It can take 4 optional parameters, ``initial``, ``final``, ``stop`` and ``error``, that, when set to ``True``, indicating that the state is an initial, final, stop or error state.

.. note:: The ``initial`` state is called while starting the automata. The ``final`` step will tell the automata has reached its end. If you call ``atmt.stop()``, the automata will move to the ``stop`` step whatever its current state is. The ``error`` state will mark the automata as errored. If no ``stop`` state is specified, calling ``stop`` and ``forcestop`` will be equivalent.

::

    class Example(Automaton):
        @ATMT.state(initial=1)
        def BEGIN(self):
            pass

        @ATMT.state()
        def SOME_STATE(self):
            pass

        @ATMT.state(final=1)
        def END(self):
            return "Result of the automaton: 42"

        @ATMT.state(stop=1)
        def STOP(self):
            print("SHUTTING DOWN...")
            # e.g. close sockets...

        @ATMT.condition(STOP)
        def is_stopping(self):
            raise self.END()

        @ATMT.state(error=1)
        def ERROR(self):
            return "Partial result, or explanation"
    # [...]

Take for instance the TCP client:

.. image:: ../graphics/ATMT_TCP_client.svg

The ``START`` event is ``initial=1``, the ``STOP`` event is ``stop=1`` and the ``CLOSED`` event is ``final=1``.

Decorators for transitions
~~~~~~~~~~~~~~~~~~~~~~~~~~

Transitions are methods decorated by the result of one of ``ATMT.condition``, ``ATMT.receive_condition``, ``ATMT.eof``, ``ATMT.timeout``, ``ATMT.timer``. They all take as argument the state method they are related to. ``ATMT.timeout`` and ``ATMT.timer`` also have a mandatory ``timeout`` parameter to provide the timeout value in seconds. The difference between ``ATMT.timeout`` and ``ATMT.timer`` is that ``ATMT.timeout`` gets triggered only once. ``ATMT.timer`` get reloaded automatically, which is useful for sending keep-alive packets. ``ATMT.condition`` and ``ATMT.receive_condition`` have an optional ``prio`` parameter so that the order in which conditions are evaluated can be forced. The default priority is 0. Transitions with the same priority level are called in an undetermined order.

When the automaton switches to a given state, the state's method is executed. Then transitions methods are called at specific moments until one triggers a new state (something like ``raise self.MY_NEW_STATE()``). First, right after the state's method returns, the ``ATMT.condition`` decorated methods are run by growing prio. Then each time a packet is received and accepted by the master filter all ``ATMT.receive_condition`` decorated hods are called by growing prio. When a timeout is reached since the time we entered into the current space, the corresponding ``ATMT.timeout`` decorated method is called. If the socket raises an ``EOFError`` (closed) during a state, the ``ATMT.EOF`` transition is called. Otherwise it raises an exception and the automaton exits.

::

    class Example(Automaton):
        @ATMT.state()
        def WAITING(self):
            pass
    
        @ATMT.condition(WAITING)
        def it_is_raining(self):
            if not self.have_umbrella:
                raise self.ERROR_WET()
    
        @ATMT.receive_condition(WAITING, prio=1)
        def it_is_ICMP(self, pkt):
            if ICMP in pkt:
                raise self.RECEIVED_ICMP(pkt)
                
        @ATMT.receive_condition(WAITING, prio=2)
        def it_is_IP(self, pkt):
            if IP in pkt:
                raise self.RECEIVED_IP(pkt)
        
        @ATMT.timeout(WAITING, 10.0)
        def waiting_timeout(self):
            raise self.ERROR_TIMEOUT()

Decorator for actions
~~~~~~~~~~~~~~~~~~~~~

Actions are methods that are decorated by the return of ``ATMT.action`` function. This function takes the transition method it is bound to as first parameter and an optional priority ``prio`` as a second parameter. The default priority is 0. An action method can be decorated many times to be bound to many transitions.

::

    from random import random

    class Example(Automaton):
        @ATMT.state(initial=1)
        def BEGIN(self):
            pass
    
        @ATMT.state(final=1)
        def END(self):
            pass
    
        @ATMT.condition(BEGIN, prio=1)
        def maybe_go_to_end(self):
            if random() > 0.5:
                raise self.END()

        @ATMT.condition(BEGIN, prio=2)
        def certainly_go_to_end(self):
            raise self.END()
    
        @ATMT.action(maybe_go_to_end)
        def maybe_action(self):
            print("We are lucky...")

        @ATMT.action(certainly_go_to_end)
        def certainly_action(self):
            print("We are not lucky...")

        @ATMT.action(maybe_go_to_end, prio=1)
        @ATMT.action(certainly_go_to_end, prio=1)
        def always_action(self):
            print("This wasn't luck!...")

The two possible outputs are::

    >>> a=Example()
    >>> a.run()
    We are not lucky...
    This wasn't luck!...
    >>> a.run()
    We are lucky...
    This wasn't luck!...
    >>> a.destroy()
