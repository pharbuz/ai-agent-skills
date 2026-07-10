# Advanced snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## advanced_usage__asn1_snmp

Part 4. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 4: literal ---
class Example(Automaton):
    @ATMT.state()
    def WAITING(self):
        pass

    @ATMT.condition(WAITING)
    def it_is_raining(self):
        if not self.have_umbrella:
# output: raise self.ERROR_WET()

    @ATMT.receive_condition(WAITING, prio=1)
    def it_is_ICMP(self, pkt):
        if ICMP in pkt:
# output: raise self.RECEIVED_ICMP(pkt)

    @ATMT.receive_condition(WAITING, prio=2)
    def it_is_IP(self, pkt):
        if IP in pkt:
# output: raise self.RECEIVED_IP(pkt)

    @ATMT.timeout(WAITING, 10.0)
    def waiting_timeout(self):
# output: raise self.ERROR_TIMEOUT()
```

```python
# --- snippet 5: literal ---
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
# output: raise self.END()

    @ATMT.condition(BEGIN, prio=2)
    def certainly_go_to_end(self):
# output: raise self.END()

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
```

```python
# --- snippet 6: literal ---
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
# output: raise self.FIN_RECEIVED().action_parameters(pkt)

    @ATMT.action(is_fin)
    def send_copy(self, pkt):
        send(pkt)
```

```python
# --- snippet 7: literal ---
class Example(Automaton):
	def __init__(self, *args, **kwargs):
	    super(Example, self).__init__(*args, **kwargs)
# output: timer = self.timer_by_name("waiting_timeout")
	    timer.set(1)

	@ATMT.state(initial=1)
	def WAITING(self):
	    pass

	@ATMT.state(final=1)
	def END(self):
	    pass

	@ATMT.timeout(WAITING, 10.0)
	def waiting_timeout(self):
# output: raise self.END()

## advanced_usage__pipetools

```python
# Extracted Python snippets from doc/scapy/advanced_usage/pipetools.rst
# Source: https://scapy.readthedocs.io/en/latest/
# Snippets may require root/admin privileges, live network access, or optional dependencies.
```

```python
# --- snippet 1: literal ---
class TransformDrain(Drain):
    def __init__(self, f, name=None):
        Drain.__init__(self, name=name)
# output: self.f = f
    def push(self, msg):
        self._send(self.f(msg))
    def high_push(self, msg):
        self._high_send(self.f(msg))
```

```python
# --- snippet 2: pycon ---
a2 = CLIHighFeeder()
a2 >> b
a2.send("hello")
```

```python
# --- snippet 3: pycon ---
a2 = CLIHighFeeder()
b2 = DownDrain()
a2 >> b2
b2 > b
a2.send("hello")

## layers__http

```python
# Extracted Python snippets from doc/scapy/layers/http.rst
# Source: https://scapy.readthedocs.io/en/latest/
# Snippets may require root/admin privileges, live network access, or optional dependencies.
```
