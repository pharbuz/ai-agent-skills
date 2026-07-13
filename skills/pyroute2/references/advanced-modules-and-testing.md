# Advanced Modules And Testing

## Other Modules

- `IPSet`: manage kernel ipset sets and entries.
- `WiSet`: higher-level ipset-related helper module.
- WireGuard module: manage WireGuard devices through generic netlink.
- Generic netlink event protocols: ACPI, disk quota, and other event families.
- MPLS howto: configure MPLS labels/routes via `IPRoute` or `NDB`.
- `tc`: traffic control operations through RTNL; validate qdisc/class/filter
  parameters against the running kernel.

Use these modules only when the target project already uses them or the task
explicitly needs the subsystem. pyroute2 exposes many kernel-specific surfaces;
kernel support matters as much as library support.

## Threading, Forking, And Async

The 0.9 series uses an asyncio core. Synchronous APIs are wrappers over that
core. Be cautious around:

- sharing pyroute2 objects across threads,
- using pyroute2 objects before and after `os.fork()`,
- multiprocessing workers inheriting open sockets,
- mixing sync wrappers inside an already-running event loop.

Prefer creating and closing pyroute2 objects inside the thread/process/task that
uses them.

## Debugging

For RTNL debugging:

- print whole messages when field names are unclear,
- inspect `msg["header"]`, `msg.get("event")`, and `msg.get("attrs")`,
- use `.get(("nested", "field"))` for nested NLAs,
- compare with `ip -details -json ...` where possible,
- use `pyroute2` decoder/debug tooling when analyzing raw netlink traffic.

Remember that successful RTNL responses do not always mean immediate visibility
of dependent state. Use NDB or `ensure()`/`poll()`.

## Permissions

Read-only dumps often work unprivileged. Mutations generally need root or
`CAP_NET_ADMIN`; namespace creation may also need `CAP_SYS_ADMIN` depending on
the environment.

In containers, failures may come from missing capabilities, read-only
`/var/run/netns`, unavailable kernel modules, or blocked namespace operations.

## Test Strategy

- Mark live mutation tests as Linux-only.
- Skip tests when `os.geteuid() != 0` or required capabilities are missing.
- Use unique names for temp interfaces and namespaces.
- Clean up in `finally` blocks.
- Prefer network namespaces and veth pairs for integration tests.
- Keep pure parsing/message transformation code unit-tested without real
  netlink sockets.

```python
import os
import pytest


pytestmark = pytest.mark.skipif(
    os.name != "posix" or os.geteuid() != 0,
    reason="pyroute2 mutation tests require Linux root/CAP_NET_ADMIN",
)
```
