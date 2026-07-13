# Examples

These examples are Markdown reference content. Run mutation examples only on
Linux systems where the caller has the required capabilities.

## List Links And Addresses

```python
from pyroute2 import IPRoute


with IPRoute() as ipr:
    for link in ipr.link("dump"):
        print(link.get("index"), link.get("ifname"), link.get("state"))

    for addr in ipr.addr("dump"):
        print(addr.get("ifname"), addr.get("address"), addr.get("prefixlen"))
```

## Create Dummy Interface Safely

```python
from pyroute2 import IPRoute


name = "test-dummy0"
with IPRoute() as ipr:
    existing = ipr.link_lookup(ifname=name)
    if not existing:
        ipr.link("add", ifname=name, kind="dummy")
        index = ipr.link_lookup(ifname=name)[0]
        ipr.link("set", index=index, state="up")
    else:
        index = existing[0]

    try:
        ipr.addr("add", index=index, address="192.0.2.10", prefixlen=24)
    finally:
        ipr.link("del", index=index)
```

## Read Nested Attributes

```python
from pyroute2 import IPRoute


with IPRoute() as ipr:
    for link in ipr.link("dump"):
        kind = link.get(("linkinfo", "kind"))
        print(link.get("ifname"), kind)
```

## NDB Interface Change

```python
from pyroute2 import NDB


with NDB() as ndb:
    ndb.interfaces.create(ifname="test0", kind="dummy").commit()
    try:
        with ndb.interfaces["test0"] as iface:
            iface.set(state="up")
            iface.add_ip("192.0.2.20/24")
    finally:
        ndb.interfaces["test0"].remove().commit()
```

## Namespace Veth Pair

```python
from pyroute2 import IPRoute, NetNS, netns


nsname = "testns0"
netns.create(nsname)
try:
    with IPRoute() as host:
        host.link("add", ifname="veth-host", kind="veth", peer="veth-ns")
        peer = host.link_lookup(ifname="veth-ns")[0]
        host.link("set", index=peer, net_ns_fd=nsname)

        host_idx = host.link_lookup(ifname="veth-host")[0]
        host.addr("add", index=host_idx, address="10.10.0.1", prefixlen=24)
        host.link("set", index=host_idx, state="up")

    with NetNS(nsname) as child:
        child_idx = child.link_lookup(ifname="veth-ns")[0]
        child.addr("add", index=child_idx, address="10.10.0.2", prefixlen=24)
        child.link("set", index=child_idx, state="up")
finally:
    with IPRoute() as host:
        matches = host.link_lookup(ifname="veth-host")
        if matches:
            host.link("del", index=matches[0])
    netns.remove(nsname)
```

## Async Dump

```python
import asyncio
from pyroute2 import AsyncIPRoute


async def main() -> None:
    ipr = AsyncIPRoute()
    try:
        async for route in await ipr.route("dump"):
            print(route.get("dst"), route.get("gateway"))
    finally:
        ipr.close()


asyncio.run(main())
```
