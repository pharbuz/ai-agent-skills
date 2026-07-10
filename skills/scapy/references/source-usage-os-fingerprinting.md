
**Programmatically:**

.. code:: python

    # Before any other Scapy import
    from scapy.config import conf
    conf.route_autoload = False
    conf.route6_autoload = False
    # Import Scapy here
    from scapy.all import *

At anytime, you can trigger the routes loading using ``conf.route.resync()`` or ``conf.route6.resync()``, or add the routes yourself `as shown here <#routing>`_.


OS Fingerprinting
-----------------

ISN
^^^

Scapy can be used to analyze ISN (Initial Sequence Number) increments to possibly discover vulnerable systems. First we will collect target responses by sending a number of SYN probes in a loop::

    >>> ans, unans = srloop(IP(dst="192.168.1.1")/TCP(dport=80,flags="S"))

Once we obtain a reasonable number of responses we can start analyzing collected data with something like this:

    >>> temp = 0
    >>> for s, r in ans:
    ...    temp = r[TCP].seq - temp
    ...    print("%d\t+%d" % (r[TCP].seq, temp))
    ... 
    4278709328      +4275758673
    4279655607      +3896934
    4280642461      +4276745527
    4281648240      +4902713
    4282645099      +4277742386
    4283643696      +5901310

nmap_fp
^^^^^^^

Nmap fingerprinting (the old "1st generation" one that was done by Nmap up to v4.20) is supported in Scapy. In Scapy v2 you have to load an extension module first::

    >>> load_module("nmap")

If you have Nmap installed you can use it's active os fingerprinting database with Scapy. Make sure that version 1 of signature database is located in the path specified by::

    >>> conf.nmap_base

Then you can use the ``nmap_fp()`` function which implements same probes as in Nmap's OS Detection engine::

    >>> nmap_fp("192.168.1.1",oport=443,cport=1)
    Begin emission:
    .****..**Finished to send 8 packets.
    *................................................
    Received 58 packets, got 7 answers, remaining 1 packets
    (1.0, ['Linux 2.4.0 - 2.5.20', 'Linux 2.4.19 w/grsecurity patch', 
    'Linux 2.4.20 - 2.4.22 w/grsecurity.org patch', 'Linux 2.4.22-ck2 (x86)
    w/grsecurity.org and HZ=1000 patches', 'Linux 2.4.7 - 2.6.11'])

p0f
^^^

If you have p0f installed on your system, you can use it to guess OS name and version right from Scapy (only SYN database is used). First make sure that p0f database exists in the path specified by::

    >>> conf.p0f_base

For example to guess OS from a single captured packet:

    >>> sniff(prn=prnp0f)
    192.168.1.100:54716 - Linux 2.6 (newer, 1) (up: 24 hrs)
      -> 74.125.19.104:www (distance 0)
    <Sniffed: TCP:339 UDP:2 ICMP:0 Other:156>
