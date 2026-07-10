

.. index::
   single: DNS, Etherleak

A DNS query (``rd`` = recursion desired). The host 192.168.5.1 is my DNS server. Note the non-null padding coming from my Linksys having the Etherleak flaw::

    >>> sr1(IP(dst="192.168.5.1")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.slashdot.org")))
    Begin emission:
    Finished to send 1 packets.
    ..*
    Received 3 packets, got 1 answers, remaining 0 packets
    <IP version=4L ihl=5L tos=0x0 len=78 id=0 flags=DF frag=0L ttl=64 proto=UDP chksum=0xaf38
     src=192.168.5.1 dst=192.168.5.21 options='' |<UDP sport=53 dport=53 len=58 chksum=0xd55d
     |<DNS id=0 qr=1L opcode=QUERY aa=0L tc=0L rd=1L ra=1L z=0L rcode=ok qdcount=1 ancount=1
     nscount=0 arcount=0 qd=<DNSQR qname='www.slashdot.org.' qtype=A qclass=IN |> 
     an=<DNSRR rrname='www.slashdot.org.' type=A rclass=IN ttl=3560L rdata='66.35.250.151' |>
     ns=0 ar=0 |<Padding load='\xc6\x94\xc7\xeb' |>>>>

The "send'n'receive" functions family is the heart of Scapy. They return a couple of two lists. The first element is a list of couples (packet sent, answer), and the second element is the list of unanswered packets. These two elements are lists, but they are wrapped by an object to present them better, and to provide them with some methods that do most frequently needed actions::

    >>> sr(IP(dst="192.168.8.1")/TCP(dport=[21,22,23]))
    Received 6 packets, got 3 answers, remaining 0 packets
    (<Results: UDP:0 TCP:3 ICMP:0 Other:0>, <Unanswered: UDP:0 TCP:0 ICMP:0 Other:0>)
    >>> ans, unans = _
    >>> ans.summary()
    IP / TCP 192.168.8.14:20 > 192.168.8.1:21 S ==> Ether / IP / TCP 192.168.8.1:21 > 192.168.8.14:20 RA / Padding
    IP / TCP 192.168.8.14:20 > 192.168.8.1:22 S ==> Ether / IP / TCP 192.168.8.1:22 > 192.168.8.14:20 RA / Padding
    IP / TCP 192.168.8.14:20 > 192.168.8.1:23 S ==> Ether / IP / TCP 192.168.8.1:23 > 192.168.8.14:20 RA / Padding
    
If there is a limited rate of answers, you can specify a time interval (in seconds) to wait between two packets with the inter parameter. If some packets are lost or if specifying an interval is not enough, you can resend all the unanswered packets, either by calling the function again, directly with the unanswered list, or by specifying a retry parameter. If retry is 3, Scapy will try to resend unanswered packets 3 times. If retry is -3, Scapy will resend unanswered packets until no more answer is given for the same set of unanswered packets 3 times in a row. The timeout parameter specify the time to wait after the last packet has been sent::

    >>> sr(IP(dst="172.20.29.5/30")/TCP(dport=[21,22,23]),inter=0.5,retry=-2,timeout=1)
    Begin emission:
    Finished to send 12 packets.
    Begin emission:
    Finished to send 9 packets.
    Begin emission:
    Finished to send 9 packets.
    
    Received 100 packets, got 3 answers, remaining 9 packets
    (<Results: UDP:0 TCP:3 ICMP:0 Other:0>, <Unanswered: UDP:0 TCP:9 ICMP:0 Other:0>)


SYN Scans
---------

.. index::
   single: SYN Scan

Classic SYN Scan can be initialized by executing the following command from Scapy's prompt::

    >>> sr1(IP(dst="72.14.207.99")/TCP(dport=80,flags="S"))

The above will send a single SYN packet to Google's port 80 and will quit after receiving a single response::

    Begin emission:
    .Finished to send 1 packets.
    *
    Received 2 packets, got 1 answers, remaining 0 packets
    <IP  version=4L ihl=5L tos=0x20 len=44 id=33529 flags= frag=0L ttl=244
    proto=TCP chksum=0x6a34 src=72.14.207.99 dst=192.168.1.100 options=// |
    <TCP  sport=www dport=ftp-data seq=2487238601L ack=1 dataofs=6L reserved=0L
    flags=SA window=8190 chksum=0xcdc7 urgptr=0 options=[('MSS', 536)] |
    <Padding  load='V\xf7' |>>>

From the above output, we can see Google returned “SA” or SYN-ACK flags indicating an open port.

Use either notations to scan ports 440 through 443 on the system:

    >>> sr(IP(dst="192.168.1.1")/TCP(sport=666,dport=(440,443),flags="S"))

or

    >>> sr(IP(dst="192.168.1.1")/TCP(sport=RandShort(),dport=[440,441,442,443],flags="S"))

In order to quickly review responses simply request a summary of collected packets::

    >>> ans, unans = _
    >>> ans.summary()
    IP / TCP 192.168.1.100:ftp-data > 192.168.1.1:440 S ======> IP / TCP 192.168.1.1:440 > 192.168.1.100:ftp-data RA / Padding
    IP / TCP 192.168.1.100:ftp-data > 192.168.1.1:441 S ======> IP / TCP 192.168.1.1:441 > 192.168.1.100:ftp-data RA / Padding
    IP / TCP 192.168.1.100:ftp-data > 192.168.1.1:442 S ======> IP / TCP 192.168.1.1:442 > 192.168.1.100:ftp-data RA / Padding
    IP / TCP 192.168.1.100:ftp-data > 192.168.1.1:https S ======> IP / TCP 192.168.1.1:https > 192.168.1.100:ftp-data SA / Padding

The above will display stimulus/response pairs for answered probes. We can display only the information we are interested in by using a simple loop:

    >>> ans.summary( lambda s,r: r.sprintf("%TCP.sport% \t %TCP.flags%") )
    440      RA
    441      RA
    442      RA
    https    SA

Even better, a table can be built using the ``make_table()`` function to display information about multiple targets::

    >>> ans, unans = sr(IP(dst=["192.168.1.1","yahoo.com","slashdot.org"])/TCP(dport=[22,80,443],flags="S"))
    Begin emission:
    .......*.**.......Finished to send 9 packets.
    **.*.*..*..................
    Received 362 packets, got 8 answers, remaining 1 packets
    >>> ans.make_table(
    ...    lambda s,r: (s.dst, s.dport,
    ...    r.sprintf("{TCP:%TCP.flags%}{ICMP:%IP.src% - %ICMP.type%}")))
        66.35.250.150                192.168.1.1 216.109.112.135 
    22  66.35.250.150 - dest-unreach RA          -               
    80  SA                           RA          SA              
    443 SA                           SA          SA              

The above example will even print the ICMP error type if the ICMP packet was received as a response instead of expected TCP.

For larger scans, we could be interested in displaying only certain responses. The example below will only display packets with the “SA” flag set::

    >>> ans.nsummary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA")
    0003 IP / TCP 192.168.1.100:ftp_data > 192.168.1.1:https S ======> IP / TCP 192.168.1.1:https > 192.168.1.100:ftp_data SA

In case we want to do some expert analysis of responses, we can use the following command to indicate which ports are open::

    >>> ans.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open"))
    https is open

Again, for larger scans we can build a table of open ports::

    >>> ans.filter(lambda s,r: TCP in r and r[TCP].flags&2).make_table(lambda s,r:
    ...             (s.dst, s.dport, "X"))
        66.35.250.150 192.168.1.1 216.109.112.135 
    80  X             -           X               
    443 X             X           X

If all of the above methods were not enough, Scapy includes a report_ports() function which not only automates the SYN scan, but also produces a LaTeX output with collected results::

    >>> report_ports("192.168.1.1",(440,443))
    Begin emission:
    ...*.**Finished to send 4 packets.
    *
    Received 8 packets, got 4 answers, remaining 0 packets
    '\\begin{tabular}{|r|l|l|}\n\\hline\nhttps & open & SA \\\\\n\\hline\n440
     & closed & TCP RA \\\\\n441 & closed & TCP RA \\\\\n442 & closed & 
    TCP RA \\\\\n\\hline\n\\hline\n\\end{tabular}\n'


TCP traceroute
--------------

.. index::
   single: Traceroute

A TCP traceroute::

    >>> ans, unans = sr(IP(dst=target, ttl=(4,25),id=RandShort())/TCP(flags=0x2))
    *****.******.*.***..*.**Finished to send 22 packets.
    ***......
    Received 33 packets, got 21 answers, remaining 1 packets
    >>> for snd,rcv in ans:
    ...     print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))
    ...
    5 194.51.159.65 0
    6 194.51.159.49 0
    4 194.250.107.181 0
    7 193.251.126.34 0
    8 193.251.126.154 0
    9 193.251.241.89 0
    10 193.251.241.110 0
    11 193.251.241.173 0
    13 208.172.251.165 0
    12 193.251.241.173 0
    14 208.172.251.165 0
    15 206.24.226.99 0
    16 206.24.238.34 0
    17 173.109.66.90 0
    18 173.109.88.218 0
    19 173.29.39.101 1
    20 173.29.39.101 1
    21 173.29.39.101 1
    22 173.29.39.101 1
    23 173.29.39.101 1
    24 173.29.39.101 1
