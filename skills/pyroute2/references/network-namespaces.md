# Network Namespaces

Network namespace operations usually require root or `CAP_SYS_ADMIN` /
`CAP_NET_ADMIN`, depending on the action and environment.

## netns Module

```python
from pyroute2 import netns

netns.create("test")
try:
    print(netns.listnetns())
finally:
    netns.remove("test")
```

Useful functions:

- `listnetns(nspath=None)`: list known namespaces.
- `create(name)`: create a namespace.
- `remove(name)`: remove a namespace.
- `attach(...)`: attach a process namespace under a netns name.
- `setns(name_or_path)`: switch current process namespace.
- `pushns(name)` / `popns()` / `dropns()`: save, restore, or discard namespace
  stack entries.
- `pid_to_ns(pid=1)` and `ns_pids()`: map processes and namespaces.

`setns("/proc/1/ns/net")` can be used to return to the initial namespace in
typical Linux systems.

## NetNS

`NetNS` gives an RTNL API bound to one namespace.

```python
from pyroute2 import NetNS

with NetNS("test") as ipr:
    for link in ipr.link("dump"):
        print(link.get("ifname"))
```

## Move An Interface

To move an interface into a namespace, set `net_ns_fd` to a namespace name or
file descriptor.

```python
from pyroute2 import IPRoute, netns

netns.create("test")
try:
    with IPRoute() as ipr:
        ipr.link("add", ifname="v0p0", kind="veth", peer="v0p1")
        peer_index = ipr.link_lookup(ifname="v0p1")[0]
        ipr.link("set", index=peer_index, net_ns_fd="test")
finally:
    netns.remove("test")
```

## NSPopen

`NSPopen` starts a subprocess inside a network namespace. It uses a helper
Python process, so file descriptors from the target process are not meaningful
in the main process.

```python
from subprocess import PIPE
from pyroute2 import NSPopen

proc = NSPopen("test", ["ip", "addr"], stdout=PIPE)
try:
    stdout, stderr = proc.communicate()
finally:
    proc.wait()
    proc.release()
```

Always call `release()` to stop the proxy process and release resources.

## Pitfalls

- Namespace system calls use `ctypes`; strict SELinux policies can break this.
- Namespace names are resolved via standard locations such as `/var/run/netns`.
- Moving the current Python process with `setns()` affects all subsequent
  network operations in that process; prefer `NetNS` or `NSPopen` for isolation.
