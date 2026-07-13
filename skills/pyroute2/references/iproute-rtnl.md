# IPRoute And RTNL

`IPRoute` is the direct synchronous RTNL API. It maps closely to Linux
rtnetlink and the `ip`/`tc` tools.

## Common Operations

```python
from pyroute2 import IPRoute

with IPRoute() as ipr:
    ipr.link("add", ifname="brx", kind="bridge")
    index = ipr.link_lookup(ifname="brx")[0]
    ipr.link("set", index=index, state="up")
    ipr.addr("add", index=index, address="10.0.0.1", prefixlen=24)
    ipr.route("add", dst="10.10.0.0/24", gateway="10.0.0.254")
```

For cleanup:

```python
with IPRoute() as ipr:
    matches = ipr.link_lookup(ifname="brx")
    if matches:
        ipr.link("del", index=matches[0])
```

## Read Patterns

```python
with IPRoute() as ipr:
    links = list(ipr.link("dump"))
    addrs = list(ipr.addr("dump"))
    routes = list(ipr.route("dump"))
```

`link_lookup(ifname=...)` returns a list of indexes. Handle an empty list
instead of indexing blindly.

## Filtering

`filter_messages()` accepts a callable or a dict. Dump calls can also use
keyword filters.

```python
with IPRoute() as ipr:
    up_links = ipr.filter_messages({"state": "up"}, ipr.link("dump"))
    eth_links = ipr.filter_messages(
        lambda msg: (msg.get("ifname") or "").startswith("eth"),
        ipr.link("dump"),
    )
```

## Delayed Kernel Visibility

RTNL calls can return success before dependent state is visible. Use `ensure()`
or `poll()` for dependent changes.

```python
with IPRoute() as ipr:
    index = ipr.ensure(
        ipr.link,
        present=True,
        ifname="test0",
        kind="dummy",
        state="up",
    )
    ipr.ensure(
        ipr.addr,
        present=True,
        index=index,
        address="192.168.0.2/24",
    )
```

`poll(method, command, **spec)` repeatedly runs a dump/get operation until it
returns a truthy result or times out.

## Messages And NLAs

Netlink messages include a parsed header, fields, and a list-like NLA chain.
NLAs are parsed on demand and are not unique, so do not assume `attrs` behaves
like a dict.

```python
with IPRoute() as ipr:
    lo = tuple(ipr.link("get", index=1))[0]
    assert lo.get("index") == 1
    assert lo.get("ifname") == "lo"
    rx_bytes = lo.get(("stats64", "rx_bytes"))
```

Use `.get_attrs("NLA_NAME")` when multiple NLAs with the same name may exist.

## Errors

Some kernel subsystems return `NLMSG_ERROR` for any request. It is success when
`nlmsg["header"]["error"]` is `None` or when the embedded error is zero. A real
kernel error is raised by pyroute2's parser.
