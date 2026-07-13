---
name: pyroute2
description: >-
  Build, debug, or refactor Python Linux networking code with `pyroute2`.
  Trigger WHENEVER the user installs or imports `pyroute2`; uses `IPRoute`,
  `AsyncIPRoute`, `NDB`, `NetNS`, `netns`, `NSPopen`, `IPSet`, `WiSet`,
  WireGuard, rtnetlink, netlink sockets, links, addresses, routes, rules,
  neighbours, bridges, bonds, veth, VLAN, VXLAN, MPLS, network namespaces,
  NDB transactions, RTNL objects, `nlmsg`, NLA attributes, `get_attrs`,
  `link_lookup`, `link`, `addr`, `route`, `rule`, `tc`, `bind`, `get`, or fixes
  permissions, missing CAP_NET_ADMIN, namespace lifecycle, async/sync API mixups,
  NLMSG_ERROR, delayed kernel visibility, threaded/forked process issues, or
  pyroute2 version/API compatibility problems.
---

# pyroute2

Use this skill for Python code that talks to Linux netlink through `pyroute2`.
The library is Linux-focused and often needs root or `CAP_NET_ADMIN` for
mutating network state. Always inspect the installed version before editing:
the online docs are built for `0.9.3rc1`, while PyPI showed `0.9.6` as latest
on 2026-07-13.

```bash
python -m pip show pyroute2
python - <<'PY'
import pyroute2
print(getattr(pyroute2, "__version__", "unknown"))
PY
```

## Choose The API

- Use `NDB` for high-level stateful network management, transactions, rollback,
  and waiting for changes to be applied.
- Use `IPRoute` for direct synchronous rtnetlink calls that map closely to
  Linux `ip`/`tc` operations.
- Use `AsyncIPRoute` for asyncio applications and async iteration over rtnetlink
  dumps.
- Use `NetNS` or `pyroute2.netns` for network namespace work.
- Use `IPSet`, WireGuard, generic netlink, and lower-level sockets only when the
  task explicitly needs those subsystems.

## Default Workflow

1. Confirm OS, privileges, container capabilities, pyroute2 version, and whether
   live network mutation is allowed.
2. Prefer public root imports: `from pyroute2 import IPRoute, NDB, NetNS`.
3. Use context managers or `close()`/`release()` to free sockets and namespace
   helper processes.
4. For reads, start with `link("dump")`, `addr("dump")`, `route("dump")`, or
   NDB `.summary()`/`.dump()` reports.
5. For writes, make operations idempotent where possible: lookup first, use NDB
   transactions or `ensure()`/`poll()` when kernel state appears asynchronously.
6. Access message fields and NLAs with `.get(...)`; use `.get_attrs(...)` for
   repeated NLAs.
7. In tests, use temporary namespaces/interfaces and skip mutation tests when
   required capabilities are missing.

## Minimal IPRoute Pattern

```python
from pyroute2 import IPRoute


with IPRoute() as ipr:
    for link in ipr.link("dump"):
        print(link.get("ifname"), link.get("state"), link.get("address"))

    index = ipr.link_lookup(ifname="lo")[0]
    for addr in ipr.addr("dump", index=index):
        print(f"{addr.get('address')}/{addr.get('prefixlen')}")
```

## Minimal AsyncIPRoute Pattern

```python
import asyncio
from pyroute2 import AsyncIPRoute


async def main() -> None:
    ipr = AsyncIPRoute()
    try:
        async for link in await ipr.link("dump"):
            print(link.get("ifname"), link.get("state"))
    finally:
        ipr.close()


asyncio.run(main())
```

## Minimal NDB Pattern

```python
from pyroute2 import NDB


with NDB() as ndb:
    for interface in ndb.interfaces.dump():
        print(interface.ifname)

    for line in ndb.routes.summary().format("json"):
        print(line)
```

## Decision Rules

- Do not parse `attrs` manually unless required; use `.get("ifname")`,
  `.get(("linkinfo", "kind"))`, or `.get_attrs("NLA_NAME")`.
- Do not assume netlink calls are immediately visible after success; dependent
  operations may need `NDB`, `ensure()`, or `poll()`.
- Do not import from deep package paths unless the root module does not export
  the symbol; internal paths may move between versions.
- Do not call low-level `recv()`/`recvmsg()` on pyroute2 sockets; use `get()` or
  higher-level APIs.
- Avoid destructive link/route/namespace changes without explicit target names
  and cleanup logic.

## References

- Read [references/quickstart-and-core.md](references/quickstart-and-core.md)
  for install/version checks, sync/async core behavior, imports, and resource
  release.
- Read [references/iproute-rtnl.md](references/iproute-rtnl.md) for `IPRoute`,
  links, addresses, routes, filters, `ensure()`, and message parsing.
- Read [references/public-models-and-imports.md](references/public-models-and-imports.md)
  for public classes/modules, what each model represents, and import paths.
- Read [references/model-fields-and-message-shapes.md](references/model-fields-and-message-shapes.md)
  for `IPRoute`/NDB model fields, RTNL message fields, and NLA access patterns.
- Read [references/ndb.md](references/ndb.md) for high-level interface, address,
  route, transaction, report, source, and namespace management.
- Read [references/network-namespaces.md](references/network-namespaces.md) for
  `netns`, `NetNS`, moving interfaces, `NSPopen`, and namespace pitfalls.
- Read [references/advanced-modules-and-testing.md](references/advanced-modules-and-testing.md)
  for IPSet, WireGuard, MPLS, debugging, threading/forking, permissions, and
  test strategy.
- Read [references/examples.md](references/examples.md) for complete code
  patterns in Markdown form.
