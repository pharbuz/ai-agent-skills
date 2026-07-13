# NDB

`NDB` is the high-level RTNL API. It collects netlink events into an SQL
database, exposes Python objects for interfaces/routes/addresses, monitors
updates without polling, and applies changes back to the system.

Use NDB when the task needs object-style state, transactions, rollback, reports,
or coordination across namespaces/sources.

## Start And Reports

```python
from pyroute2 import NDB


with NDB() as ndb:
    for interface in ndb.interfaces.dump():
        print(interface.ifname)

    for line in ndb.routes.summary().format("csv"):
        print(line)
```

`dump()` and `summary()` produce record sets. Records are immutable snapshots,
not live RTNL objects.

## Interface Changes

```python
from pyroute2 import NDB


with NDB() as ndb:
    with ndb.interfaces["eth0"] as eth0:
        eth0.set(state="up")
        eth0.add_ip("10.0.0.1/24")
```

The context manager commits automatically and waits for the change to appear.

## Create Virtual Interfaces

```python
with NDB() as ndb:
    ndb.interfaces.create(ifname="br0", kind="bridge").commit()
    ndb.interfaces.create(
        ifname="v0p0",
        kind="veth",
        peer={"ifname": "v0p1"},
    ).commit()
```

Use explicit cleanup in tests and scripts that create interfaces.

## Routes

```python
with NDB() as ndb:
    ndb.routes.create(
        dst="10.10.0.0/24",
        gateway="192.0.2.1",
        oif=ndb.interfaces["eth0"]["index"],
    ).commit()
```

For multiple tables, metrics, MPLS, or policy routing, inspect the existing
project's pyroute2 version and route object examples before editing.

## Sources And Namespaces

NDB can aggregate multiple RTNL sources, including network namespaces.

```python
with NDB() as ndb:
    for name in ["netns01", "netns02"]:
        ndb.sources.add(netns=name)

    report = ndb.addresses.summary()
    report.select_records(target=lambda value: value.startswith("netns"))
    report.select_fields("address", "ifname", "target")
    for line in report.format("json"):
        print(line)
```

## Transactions And Rollback

Use NDB transactions when several changes must be committed together or rolled
back on failure. Prefer NDB over raw `IPRoute` when waiting and rollback
behavior matters more than one-to-one netlink control.
