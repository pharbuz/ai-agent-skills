# Model Fields And Message Shapes

Pyroute2 "models" are usually API objects or parsed netlink messages, not
dataclasses with fixed Python attributes. Use this as a field guide.

## IPRoute / AsyncIPRoute

Import:

```python
from pyroute2 import IPRoute, AsyncIPRoute
```

What the model contains:

- RTNL socket state and lifecycle: `bind()`, `get()`, `close()`.
- Link model operations: `link`, `get_links`, `link_lookup`, `brport`, `vlan_filter`.
- Address model operations: `addr`, `get_addr`, `flush_addr`.
- Route model operations: `route`, `get_routes`, `get_default_routes`,
  `flush_routes`.
- Rule model operations: `rule`, `get_rules`, `flush_rules`.
- Neighbour/FDB/VLAN operations: `neigh`, `get_neighbours`, `fdb`, `get_vlans`.
- Traffic control: `tc`, `get_qdiscs`, `get_classes`, `get_filters`.
- Namespace helpers: `get_netnsid`, `get_netns_info`.
- State helpers: `filter_messages`, `ensure`, `poll`, `dump`, `probe`.

Returned records are parsed netlink messages. Typical link fields:

```python
link.get("index")
link.get("ifname")
link.get("address")
link.get("state")
link.get("flags")
link.get(("linkinfo", "kind"))
link.get(("stats64", "rx_bytes"))
```

Typical address fields:

```python
addr.get("index")
addr.get("ifname")
addr.get("address")
addr.get("prefixlen")
addr.get("family")
addr.get("scope")
```

Typical route fields:

```python
route.get("dst")
route.get("dst_len")
route.get("gateway")
route.get("oif")
route.get("table")
route.get("family")
route.get("priority")
```

## Netlink Message Shape

Every parsed netlink message has:

- `msg["header"]`: parsed netlink header.
- `msg["attrs"]`: list-like chain of NLAs.
- top-level data fields such as `family`, `flags`, `index`, `prefixlen`.
- injected fields such as `event` for RTNL notifications.

Header fields commonly include:

```python
msg["header"]["type"]
msg["header"]["flags"]
msg["header"]["sequence_number"]
msg["header"]["pid"]
msg["header"]["error"]
```

Use `.get(...)` for fields and first matching NLA:

```python
ifname = msg.get("ifname")
kind = msg.get(("linkinfo", "kind"))
```

Use `.get_attrs("NLA_NAME")` when an NLA can repeat.

## NDB

Import:

```python
from pyroute2 import NDB
```

Top-level NDB model fields/views:

- `ndb.interfaces`: interface view.
- `ndb.addresses`: IP address view.
- `ndb.routes`: route view.
- `ndb.sources`: RTNL sources, including namespaces.
- reports from `.dump()` and `.summary()`.

Interface object fields commonly include:

```python
iface["ifname"]
iface["index"]
iface["state"]
iface["address"]
```

Address object/report fields commonly include `address`, `prefixlen`, `ifname`,
`index`, and `target`. Route summaries commonly include `target`, `tflags`,
`table`, `ifname`, `dst`, `dst_len`, and `gateway`.

NDB objects expose methods such as `set`, `add_ip`, `del_ip`, `commit`,
`remove`, `rollback`, and context-manager auto-commit.

## IPSet And WiSet

Imports:

```python
from pyroute2 import IPSet, AsyncIPSet, WiSet
```

`IPSet` contains kernel ipset operations: `create`, `add`, `delete`, `flush`,
`destroy`, `headers`, `list`, protocol version lookup, and supported revision
queries. Set entries vary by ipset type; common fields are set name, family,
type, revision, entry address/network, port, protocol, timeout, and counters.

`WiSet` wraps ipset content with helper operations such as `insert_list`,
`from_netlink`, `content`, `create`, `add`, `delete`, `flush`, and `destroy`.

## IPVS

Imports:

```python
from pyroute2 import IPVS, AsyncIPVS, IPVSService, IPVSDest
```

`IPVS` manages virtual services and backend destinations. Service models contain
protocol/address/port/scheduler/flags/timeouts/stats depending on kernel
response. Destination models contain address/port/weight/forwarding method and
connection counters.

## WireGuard

Imports:

```python
from pyroute2 import WireGuard, AsyncWireGuard
```

WireGuard models contain device-level fields such as interface name/index,
private/public keys, listen port, fwmark, and peer lists. Peer records contain
public key, endpoint, allowed IPs, persistent keepalive, handshake time, and
transfer counters when returned by the kernel.

## Event And Diagnostic Sockets

Imports:

```python
from pyroute2 import EventSocket, DiagSocket, UeventSocket, TaskStats
```

These classes expose parsed event/diagnostic messages. Inspect each returned
message's `header`, top-level fields, and `attrs`; exact fields depend on the
kernel family and event type.
