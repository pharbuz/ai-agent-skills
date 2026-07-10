
    >>> ans, unans = sr(IP(dst="172.20.80.192/28")/TCP(dport=[20,21,22,25,53,80]))
    Received 142 packets, got 25 answers, remaining 71 packets
    >>> ans.make_table(lambda s,r: (s.dst, s.dport, r.sprintf("%IP.id%")))
       172.20.80.196 172.20.80.197 172.20.80.198 172.20.80.200 172.20.80.201 
    20 0             4203          7021          -             11562             
    21 0             4204          7022          -             11563             
    22 0             4205          7023          11561         11564             
    25 0             0             7024          -             11565             
    53 0             4207          7025          -             11566             
    80 0             4028          7026          -             11567             

It can help identify network topologies very easily when playing with TTL, displaying received TTL, etc.

Routing
-------

.. index::
   single: Routing, conf.route

Now Scapy has its own routing table, so that you can have your packets routed differently than the system::

    >>> conf.route
    Network         Netmask         Gateway         Iface
    127.0.0.0       255.0.0.0       0.0.0.0         lo
    192.168.8.0     255.255.255.0   0.0.0.0         eth0
    0.0.0.0         0.0.0.0         192.168.8.1     eth0
    >>> conf.route.delt(net="0.0.0.0/0",gw="192.168.8.1")
    >>> conf.route.add(net="0.0.0.0/0",gw="192.168.8.254")
    >>> conf.route.add(host="192.168.1.1",gw="192.168.8.1")
    >>> conf.route
    Network         Netmask         Gateway         Iface
    127.0.0.0       255.0.0.0       0.0.0.0         lo
    192.168.8.0     255.255.255.0   0.0.0.0         eth0
    0.0.0.0         0.0.0.0         192.168.8.254   eth0
    192.168.1.1     255.255.255.255 192.168.8.1     eth0
    >>> conf.route.resync()
    >>> conf.route
    Network         Netmask         Gateway         Iface
    127.0.0.0       255.0.0.0       0.0.0.0         lo
    192.168.8.0     255.255.255.0   0.0.0.0         eth0
    0.0.0.0         0.0.0.0         192.168.8.1     eth0

Matplotlib
----------

.. index::
   single: Matplotlib, plot()

We can easily plot some harvested values using Matplotlib. (Make sure that you have matplotlib installed.)
For example, we can observe the IP ID patterns to know how many distinct IP stacks are used behind a load balancer::

    >>> a, b = sr(IP(dst="www.target.com")/TCP(sport=[RandShort()]*1000))
    >>> a.plot(lambda q,r: r.id)
    [<matplotlib.lines.Line2D at 0x2367b80d6a0>]

.. image:: graphics/ipid.png


TCP traceroute (2)
------------------

.. index::
   single: traceroute(), Traceroute

Scapy also has a powerful TCP traceroute function. Unlike other traceroute programs that wait for each node to reply before going to the next, Scapy sends all the packets at the same time. This has the disadvantage that it can't know when to stop (thus the maxttl parameter) but the great advantage that it took less than 3 seconds to get this multi-target traceroute result::

    >>> traceroute(["www.yahoo.com","www.altavista.com","www.wisenut.com","www.copernic.com"],maxttl=20)
    Received 80 packets, got 80 answers, remaining 0 packets
       193.45.10.88:80    216.109.118.79:80  64.241.242.243:80  66.94.229.254:80   
    1  192.168.8.1        192.168.8.1        192.168.8.1        192.168.8.1        
    2  82.243.5.254       82.243.5.254       82.243.5.254       82.243.5.254     
    3  213.228.4.254      213.228.4.254      213.228.4.254      213.228.4.254      
    4  212.27.50.46       212.27.50.46       212.27.50.46       212.27.50.46       
    5  212.27.50.37       212.27.50.41       212.27.50.37       212.27.50.41       
    6  212.27.50.34       212.27.50.34       213.228.3.234      193.251.251.69     
    7  213.248.71.141     217.118.239.149    208.184.231.214    193.251.241.178    
    8  213.248.65.81      217.118.224.44     64.125.31.129      193.251.242.98     
    9  213.248.70.14      213.206.129.85     64.125.31.186      193.251.243.89     
    10 193.45.10.88    SA 213.206.128.160    64.125.29.122      193.251.254.126    
    11 193.45.10.88    SA 206.24.169.41      64.125.28.70       216.115.97.178     
    12 193.45.10.88    SA 206.24.226.99      64.125.28.209      66.218.64.146      
    13 193.45.10.88    SA 206.24.227.106     64.125.29.45       66.218.82.230      
    14 193.45.10.88    SA 216.109.74.30      64.125.31.214      66.94.229.254   SA 
    15 193.45.10.88    SA 216.109.120.149    64.124.229.109     66.94.229.254   SA 
    16 193.45.10.88    SA 216.109.118.79  SA 64.241.242.243  SA 66.94.229.254   SA 
    17 193.45.10.88    SA 216.109.118.79  SA 64.241.242.243  SA 66.94.229.254   SA 
    18 193.45.10.88    SA 216.109.118.79  SA 64.241.242.243  SA 66.94.229.254   SA 
    19 193.45.10.88    SA 216.109.118.79  SA 64.241.242.243  SA 66.94.229.254   SA 
    20 193.45.10.88    SA 216.109.118.79  SA 64.241.242.243  SA 66.94.229.254   SA 
    (<Traceroute: UDP:0 TCP:28 ICMP:52 Other:0>, <Unanswered: UDP:0 TCP:0 ICMP:0 Other:0>)

The last line is in fact the result of the function : a traceroute result object and a packet list of unanswered packets. The traceroute result is a more specialised version (a subclass, in fact) of a classic result object. We can save it to consult the traceroute result again a bit later, or to deeply inspect one of the answers, for example to check padding.

    >>> result, unans = _
    >>> result.show()
       193.45.10.88:80    216.109.118.79:80  64.241.242.243:80  66.94.229.254:80   
    1  192.168.8.1        192.168.8.1        192.168.8.1        192.168.8.1        
    2  82.251.4.254       82.251.4.254       82.251.4.254       82.251.4.254     
    3  213.228.4.254      213.228.4.254      213.228.4.254      213.228.4.254      
    [...]
    >>> result.filter(lambda x: Padding in x[1])

Like any result object, traceroute objects can be added :

    >>> r2, unans = traceroute(["www.voila.com"],maxttl=20)
    Received 19 packets, got 19 answers, remaining 1 packets
       195.101.94.25:80   
    1  192.168.8.1        
    2  82.251.4.254     
    3  213.228.4.254      
    4  212.27.50.169      
    5  212.27.50.162      
    6  193.252.161.97     
    7  193.252.103.86     
    8  193.252.103.77     
    9  193.252.101.1      
    10 193.252.227.245    
    12 195.101.94.25   SA 
    13 195.101.94.25   SA 
    14 195.101.94.25   SA 
    15 195.101.94.25   SA 
    16 195.101.94.25   SA 
    17 195.101.94.25   SA 
    18 195.101.94.25   SA 
    19 195.101.94.25   SA 
    20 195.101.94.25   SA 
    >>>
    >>> r3=result+r2
    >>> r3.show()
       195.101.94.25:80   212.23.37.13:80    216.109.118.72:80  64.241.242.243:80  66.94.229.254:80   
    1  192.168.8.1        192.168.8.1        192.168.8.1        192.168.8.1        192.168.8.1        
    2  82.251.4.254       82.251.4.254       82.251.4.254       82.251.4.254       82.251.4.254     
    3  213.228.4.254      213.228.4.254      213.228.4.254      213.228.4.254      213.228.4.254      
    4  212.27.50.169      212.27.50.169      212.27.50.46       -                  212.27.50.46       
    5  212.27.50.162      212.27.50.162      212.27.50.37       212.27.50.41       212.27.50.37       
    6  193.252.161.97     194.68.129.168     212.27.50.34       213.228.3.234      193.251.251.69     
    7  193.252.103.86     212.23.42.33       217.118.239.185    208.184.231.214    193.251.241.178    
    8  193.252.103.77     212.23.42.6        217.118.224.44     64.125.31.129      193.251.242.98     
    9  193.252.101.1      212.23.37.13    SA 213.206.129.85     64.125.31.186      193.251.243.89     
    10 193.252.227.245    212.23.37.13    SA 213.206.128.160    64.125.29.122      193.251.254.126    
    11 -                  212.23.37.13    SA 206.24.169.41      64.125.28.70       216.115.97.178     
    12 195.101.94.25   SA 212.23.37.13    SA 206.24.226.100     64.125.28.209      216.115.101.46     
    13 195.101.94.25   SA 212.23.37.13    SA 206.24.238.166     64.125.29.45       66.218.82.234      
    14 195.101.94.25   SA 212.23.37.13    SA 216.109.74.30      64.125.31.214      66.94.229.254   SA 
    15 195.101.94.25   SA 212.23.37.13    SA 216.109.120.151    64.124.229.109     66.94.229.254   SA 
    16 195.101.94.25   SA 212.23.37.13    SA 216.109.118.72  SA 64.241.242.243  SA 66.94.229.254   SA 
    17 195.101.94.25   SA 212.23.37.13    SA 216.109.118.72  SA 64.241.242.243  SA 66.94.229.254   SA 
    18 195.101.94.25   SA 212.23.37.13    SA 216.109.118.72  SA 64.241.242.243  SA 66.94.229.254   SA 
    19 195.101.94.25   SA 212.23.37.13    SA 216.109.118.72  SA 64.241.242.243  SA 66.94.229.254   SA 
    20 195.101.94.25   SA 212.23.37.13    SA 216.109.118.72  SA 64.241.242.243  SA 66.94.229.254   SA 

Traceroute result object also have a very neat feature: they can make a directed graph from all the routes they got, and cluster them by AS (Autonomous System). You will need graphviz. By default, ImageMagick is used to display the graph.

    >>> res, unans = traceroute(["www.microsoft.com","www.cisco.com","www.yahoo.com","www.wanadoo.fr","www.pacsec.com"],dport=[80,443],maxttl=20,retry=-2)
    Received 190 packets, got 190 answers, remaining 10 packets
       193.252.122.103:443 193.252.122.103:80 198.133.219.25:443 198.133.219.25:80  207.46...
    1  192.168.8.1         192.168.8.1        192.168.8.1        192.168.8.1        192.16...
    2  82.251.4.254        82.251.4.254       82.251.4.254       82.251.4.254       82.251...
    3  213.228.4.254       213.228.4.254      213.228.4.254      213.228.4.254      213.22...
    [...]
    >>> res.graph()                          # piped to ImageMagick's display program. Image below.
    >>> res.graph(type="ps",target="| lp")   # piped to postscript printer
    >>> res.graph(target="> /tmp/graph.svg") # saved to file
