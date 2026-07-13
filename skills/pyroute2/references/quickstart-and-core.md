# Quickstart And Core

pyroute2 is a Python netlink library. It is mostly used on Linux for RTNL
operations similar to `ip` and `tc`.

## Install And Version

```bash
python -m pip install pyroute2
python -m pip show pyroute2
```

The official docs fetched for this skill identify themselves as
`pyroute2 0.9.3rc1`; PyPI reported `0.9.6` and Python `>=3.9` on 2026-07-13.
Check the local package before relying on a signature.

## Public Imports

Prefer root imports. The docs state the public API is exported from
`pyroute2/__init__.py` to remain stable across package layout changes.

```python
from pyroute2 import AsyncIPRoute, IPRoute, NDB, NetNS, NSPopen
```

Avoid deep imports like `pyroute2.iproute.linux.NetNS` unless no public root
import exists for the symbol you need.

## Sync API

```python
from pyroute2 import IPRoute


def main() -> None:
    with IPRoute() as ipr:
        for link in ipr.link("dump"):
            print(link.get("ifname"), link.get("state"), link.get("address"))
```

Use `with IPRoute()` or call `ipr.close()`. Closed objects release user-space
resources immediately; the real file descriptor is fully gone after Python GC
collects the closed object.

## Async API

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

Starting with the 0.9 series, pyroute2 uses an asyncio core. Synchronous APIs
are wrappers around asynchronous APIs and remain available for compatibility.

## Netlink Sockets

Pyroute2 sockets are managed by the asyncio event loop. Direct `recv()` and
`recvmsg()` are not part of the user-facing flow. Use `get()` for low-level
parsed messages or higher-level methods like `link("dump")`.

```python
from pyroute2 import IPRoute

ipr = IPRoute()
try:
    ipr.bind()
    messages = ipr.get()
finally:
    ipr.close()
```
