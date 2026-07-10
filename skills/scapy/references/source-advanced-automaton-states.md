# Source: advanced_usage/automaton

Automata
========

Scapy enables to create easily network automata. Scapy does not stick to a specific model like Moore or Mealy automata. It provides a flexible way for you to choose your way to go.

An automaton in Scapy is deterministic. It has different states. A start state and some end and error states. There are transitions from one state to another. Transitions can be transitions on a specific condition, transitions on the reception of a specific packet or transitions on a timeout. When a transition is taken, one or more actions can be run. An action can be bound to many transitions. Parameters can be passed from states to transitions, and from transitions to states and actions.

From a programmer's point of view, states, transitions and actions are methods from an Automaton subclass. They are decorated to provide meta-information needed in order for the automaton to work.

First example
-------------

Let's begin with a simple example. I take the convention to write states with capitals, but anything valid with Python syntax would work as well.

::

    class HelloWorld(Automaton):
        @ATMT.state(initial=1)
        def BEGIN(self):
            print("State=BEGIN")
    
        @ATMT.condition(BEGIN)
        def wait_for_nothing(self):
            print("Wait for nothing...")
            raise self.END()
    
        @ATMT.action(wait_for_nothing)
        def on_nothing(self):
            print("Action on 'nothing' condition")
    
        @ATMT.state(final=1)
        def END(self):
            print("State=END")

In this example, we can see 3 decorators:

* ``ATMT.state`` that is used to indicate that a method is a state, and that can
  have initial, final, stop and error optional arguments set to non-zero for special states.
* ``ATMT.condition`` that indicate a method to be run when the automaton state 
  reaches the indicated state. The argument is the name of the method representing that state
* ``ATMT.action`` binds a method to a transition and is run when the transition is taken. 

Running this example gives the following result::

    >>> a=HelloWorld()
    >>> a.run()
    State=BEGIN
    Wait for nothing...
    Action on 'nothing' condition
    State=END
    >>> a.destroy()

This simple automaton can be described with the following graph:

.. image:: ../graphics/ATMT_HelloWorld.*

The graph can be automatically drawn from the code with::

    >>> HelloWorld.graph()

.. note:: An ``Automaton`` can be reset using ``restart()``. It is then possible to run it again.

.. warning:: Remember to call ``destroy()`` once you're done using an Automaton. (especially on PyPy)

Changing states
---------------

The ``ATMT.state`` decorator transforms a method into a function that returns an exception. If you raise that exception, the automaton state will be changed. If the change occurs in a transition, actions bound to this transition will be called. The parameters given to the function replacing the method will be kept and finally delivered to the method. The exception has a method action_parameters that can be called before it is raised so that it will store parameters to be delivered to all actions bound to the current transition.

As an example, let's consider the following state::

    @ATMT.state()
    def MY_STATE(self, param1, param2):
        print("state=MY_STATE. param1=%r param2=%r" % (param1, param2))

This state will be reached with the following code::

    @ATMT.receive_condition(ANOTHER_STATE)
    def received_ICMP(self, pkt):
        if ICMP in pkt:
            raise self.MY_STATE("got icmp", pkt[ICMP].type)

Let's suppose we want to bind an action to this transition, that will also need some parameters::

    @ATMT.action(received_ICMP)
    def on_ICMP(self, icmp_type, icmp_code):
        self.retaliate(icmp_type, icmp_code)

The condition should become::

    @ATMT.receive_condition(ANOTHER_STATE)
    def received_ICMP(self, pkt):
        if ICMP in pkt:
            raise self.MY_STATE("got icmp", pkt[ICMP].type).action_parameters(pkt[ICMP].type, pkt[ICMP].code)

Real example
------------

Here is a real example take from Scapy. It implements a TFTP client that can issue read requests.

.. image:: ../graphics/ATMT_TFTP_read.*

::

    class TFTP_read(Automaton):
        def parse_args(self, filename, server, sport = None, port=69, **kargs):
            Automaton.parse_args(self, **kargs)
            self.filename = filename
            self.server = server
            self.port = port
            self.sport = sport
    
        def master_filter(self, pkt):
            return ( IP in pkt and pkt[IP].src == self.server and UDP in pkt
                     and pkt[UDP].dport == self.my_tid
                     and (self.server_tid is None or pkt[UDP].sport == self.server_tid) )
            
        # BEGIN
        @ATMT.state(initial=1)
        def BEGIN(self):
            self.blocksize=512
            self.my_tid = self.sport or RandShort()._fix()
            bind_bottom_up(UDP, TFTP, dport=self.my_tid)
            self.server_tid = None
            self.res = b""
    
            self.l3 = IP(dst=self.server)/UDP(sport=self.my_tid, dport=self.port)/TFTP()
            self.last_packet = self.l3/TFTP_RRQ(filename=self.filename, mode="octet")
            self.send(self.last_packet)
            self.awaiting=1
            
            raise self.WAITING()
            
        # WAITING
        @ATMT.state()
        def WAITING(self):
            pass
    
        @ATMT.receive_condition(WAITING)
        def receive_data(self, pkt):
            if TFTP_DATA in pkt and pkt[TFTP_DATA].block == self.awaiting:
                if self.server_tid is None:
                    self.server_tid = pkt[UDP].sport
                    self.l3[UDP].dport = self.server_tid
                raise self.RECEIVING(pkt)
        @ATMT.action(receive_data)
        def send_ack(self):
            self.last_packet = self.l3 / TFTP_ACK(block = self.awaiting)
            self.send(self.last_packet)
    
        @ATMT.receive_condition(WAITING, prio=1)
        def receive_error(self, pkt):
            if TFTP_ERROR in pkt:
                raise self.ERROR(pkt)
    
        @ATMT.timeout(WAITING, 3)
        def timeout_waiting(self):
            raise self.WAITING()
        @ATMT.action(timeout_waiting)
        def retransmit_last_packet(self):
            self.send(self.last_packet)
