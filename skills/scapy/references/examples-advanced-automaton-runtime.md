# Advanced snippets

Extracted from Scapy documentation source pages. These are documentation snippets, including some interactive transcript output; adapt them into clean application code before use.

## advanced_usage__asn1_snmp

Part 3. Extracted snippets; adapt transcript output into normal Python before use.

```python
# --- snippet 1: literal ---
class HelloWorld(Automaton):
    @ATMT.state(initial=1)
    def BEGIN(self):
        print("State=BEGIN")

    @ATMT.condition(BEGIN)
    def wait_for_nothing(self):
        print("Wait for nothing...")
# output: raise self.END()

    @ATMT.action(wait_for_nothing)
    def on_nothing(self):
        print("Action on 'nothing' condition")

    @ATMT.state(final=1)
    def END(self):
        print("State=END")
```

```python
# --- snippet 2: literal ---
class TFTP_read(Automaton):
    def parse_args(self, filename, server, sport = None, port=69, **kargs):
        Automaton.parse_args(self, **kargs)
# output: self.filename = filename
# output: self.server = server
# output: self.port = port
# output: self.sport = sport

    def master_filter(self, pkt):
        return ( IP in pkt and pkt[IP].src == self.server and UDP in pkt
# output: and pkt[UDP].dport == self.my_tid
# output: and (self.server_tid is None or pkt[UDP].sport == self.server_tid) )

    # BEGIN
    @ATMT.state(initial=1)
    def BEGIN(self):
        self.blocksize=512
# output: self.my_tid = self.sport or RandShort()._fix()
        bind_bottom_up(UDP, TFTP, dport=self.my_tid)
# output: self.server_tid = None
# output: self.res = b""

# output: self.l3 = IP(dst=self.server)/UDP(sport=self.my_tid, dport=self.port)/TFTP()
# output: self.last_packet = self.l3/TFTP_RRQ(filename=self.filename, mode="octet")
        self.send(self.last_packet)
        self.awaiting=1

# output: raise self.WAITING()

    # WAITING
    @ATMT.state()
    def WAITING(self):
        pass

    @ATMT.receive_condition(WAITING)
    def receive_data(self, pkt):
        if TFTP_DATA in pkt and pkt[TFTP_DATA].block == self.awaiting:
            if self.server_tid is None:
# output: self.server_tid = pkt[UDP].sport
                self.l3[UDP].dport = self.server_tid
# output: raise self.RECEIVING(pkt)
    @ATMT.action(receive_data)
    def send_ack(self):
# output: self.last_packet = self.l3 / TFTP_ACK(block = self.awaiting)
        self.send(self.last_packet)

    @ATMT.receive_condition(WAITING, prio=1)
    def receive_error(self, pkt):
        if TFTP_ERROR in pkt:
# output: raise self.ERROR(pkt)

    @ATMT.timeout(WAITING, 3)
    def timeout_waiting(self):
# output: raise self.WAITING()
    @ATMT.action(timeout_waiting)
    def retransmit_last_packet(self):
        self.send(self.last_packet)

    # RECEIVED
    @ATMT.state()
    def RECEIVING(self, pkt):
# output: recvd = pkt[Raw].load
# output: self.res += recvd
# output: self.awaiting += 1
        if len(recvd) == self.blocksize:
# output: raise self.WAITING()
# output: raise self.END()

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
```

```python
# --- snippet 3: literal ---
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
# output: raise self.END()

    @ATMT.state(error=1)
    def ERROR(self):
        return "Partial result, or explanation"
# [...]
```
