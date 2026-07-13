# Public Models And Imports

Prefer root imports when available. The `pyroute2` root package re-exports its
public API so code is less sensitive to internal package moves.

```python
from pyroute2 import IPRoute, AsyncIPRoute, NDB, NetNS
```

The direct import path below is useful for docs lookup, type stubs, or when a
project already imports from implementation modules.

## RTNL And Network State

| Model | Root import | Direct path | Represents / contains |
|---|---|---|---|
| `IPRoute` | `from pyroute2 import IPRoute` | `pyroute2.iproute.IPRoute` | Sync rtnetlink API; link/addr/route/rule/tc/neighbour/fdb/vlan methods. |
| `AsyncIPRoute` | `from pyroute2 import AsyncIPRoute` | `pyroute2.iproute.AsyncIPRoute` | Async rtnetlink API; awaited calls and async iteration over dumps. |
| `RawIPRoute` | `from pyroute2 import RawIPRoute` | `pyroute2.iproute.RawIPRoute` | Lower-level RTNL socket variant for raw-style workflows. |
| `ChaoticIPRoute` | `from pyroute2 import ChaoticIPRoute` | `pyroute2.iproute.ChaoticIPRoute` | Testing/fault-injection variant of IPRoute behavior. |
| `IPBatch` | `from pyroute2 import IPBatch` | `pyroute2.iproute.IPBatch` | Batch builder for grouped RTNL operations. |
| `NetNS` | `from pyroute2 import NetNS` | `pyroute2.iproute.NetNS` | RTNL API scoped to a named network namespace. |
| `IPRSocket` | `from pyroute2 import IPRSocket` | `pyroute2.netlink.rtnl.iprsocket.IPRSocket` | Synchronous rtnetlink socket. |
| `AsyncIPRSocket` | `from pyroute2 import AsyncIPRSocket` | `pyroute2.netlink.rtnl.iprsocket.AsyncIPRSocket` | Async rtnetlink socket. |
| `NDB` | `from pyroute2 import NDB` | `pyroute2.ndb.main.NDB` | High-level RTNL database/object API: interfaces, addresses, routes, sources, transactions. |
| `IPDB` | `from pyroute2 import IPDB` | `pyroute2.ipdb.IPDB` | Deprecated older high-level network DB; prefer NDB for new code. |

## NDB Internal Models

| Model | Import path | Represents / contains |
|---|---|---|
| `RTNL_Object` | `from pyroute2.ndb.objects import RTNL_Object` | Base for NDB objects; `apply`, `commit`, `remove`, `rollback`, key/state tables. |
| `View` | `from pyroute2.ndb.view import View` | NDB object view; indexed access, `get`, `exists`, `create`, `dump`, `summary`. |
| `RecordSet` | `from pyroute2.ndb.report import RecordSet` | Immutable report/list result; `format`, `select_fields`, `select_records`, `count`. |
| `Transaction` | `from pyroute2.ndb.transaction import Transaction` | Multi-operation commit/rollback unit; append/insert/commit/cancel/done. |
| `CheckProcess` | `from pyroute2.ndb.transaction import CheckProcess` | Transaction check that validates external process execution. |
| `PingAddress` | `from pyroute2.ndb.transaction import PingAddress` | Transaction check that validates reachability. |
| `Not` | `from pyroute2.ndb.transaction import Not` | Negates a transaction check. |

## Netfilter, IP Sets, And Load Balancing

| Model | Root import | Direct path | Represents / contains |
|---|---|---|---|
| `IPSet` / `AsyncIPSet` | `from pyroute2 import IPSet, AsyncIPSet` | `pyroute2.ipset` | Kernel ipset create/add/delete/flush/destroy/query operations. |
| `WiSet` | `from pyroute2 import WiSet` | `pyroute2.wiset.WiSet` | Higher-level ipset wrapper with list insert/content helpers. |
| `IPVS` / `AsyncIPVS` | `from pyroute2 import IPVS, AsyncIPVS` | `pyroute2.ipvs` | Linux IP Virtual Server services and destinations. |
| `IPVSService` | `from pyroute2 import IPVSService` | `pyroute2.ipvs.IPVSService` | IPVS virtual service model. |
| `IPVSDest` | `from pyroute2 import IPVSDest` | `pyroute2.ipvs.IPVSDest` | IPVS backend destination model. |
| `IPVSSocket` / `AsyncIPVSSocket` | `from pyroute2 import IPVSSocket, AsyncIPVSSocket` | `pyroute2.netlink.generic.ipvs` | Generic netlink socket for IPVS. |
| `NFCTSocket` / `AsyncNFCTSocket` | `from pyroute2 import NFCTSocket, AsyncNFCTSocket` | `pyroute2.netlink.nfnetlink.nfctsocket` | Netfilter conntrack socket. |
| `NFTSocket` / `AsyncNFTSocket` | `from pyroute2 import NFTSocket, AsyncNFTSocket` | `pyroute2.netlink.nfnetlink.nftsocket` | nftables netlink socket. |
| `IPQSocket` | `from pyroute2 import IPQSocket` | `pyroute2.netlink.ipq.IPQSocket` | ip_queue netlink socket. |
| `Conntrack` / `AsyncConntrack` | `from pyroute2 import Conntrack, AsyncConntrack` | `pyroute2.conntrack` | High-level conntrack API. |
| `ConntrackEntry` | `from pyroute2 import ConntrackEntry` | `pyroute2.conntrack.ConntrackEntry` | Conntrack entry data model. |

## Generic Netlink And Device Families

| Model | Root import | Direct path | Represents / contains |
|---|---|---|---|
| `GenericNetlinkSocket` / `AsyncGenericNetlinkSocket` | `from pyroute2 import GenericNetlinkSocket, AsyncGenericNetlinkSocket` | `pyroute2.netlink.generic` | Generic netlink base socket. |
| `WireGuard` / `AsyncWireGuard` | `from pyroute2 import WireGuard, AsyncWireGuard` | `pyroute2.netlink.generic.wireguard` | WireGuard device/peer management. |
| `NlEthtool` / `AsyncNlEthtool` | `from pyroute2 import NlEthtool, AsyncNlEthtool` | `pyroute2.netlink.generic.ethtool` | Generic-netlink ethtool interface. |
| `Ethtool` | `from pyroute2 import Ethtool` | `pyroute2.ethtool.ethtool.Ethtool` | Higher-level ethtool helper API. |
| `NL80211` / `AsyncNL80211` | `from pyroute2 import NL80211, AsyncNL80211` | `pyroute2.netlink.nl80211` | Wi-Fi/nl80211 generic netlink API. |
| `IW` / `AsyncIW` | `from pyroute2 import IW, AsyncIW` | `pyroute2.iwutil` | Higher-level wireless helper API. |
| `L2tp` / `AsyncL2tp` | `from pyroute2 import L2tp, AsyncL2tp` | `pyroute2.netlink.generic.l2tp` | L2TP generic netlink API. |
| `MPTCP` / `AsyncMPTCP` | `from pyroute2 import MPTCP, AsyncMPTCP` | `pyroute2.netlink.generic.mptcp` | Multipath TCP generic netlink API. |
| `DL` / `AsyncDL` | `from pyroute2 import DL, AsyncDL` | `pyroute2.devlink` | Devlink high-level API. |
| `DevlinkSocket` / `AsyncDevlinkSocket` | `from pyroute2 import DevlinkSocket, AsyncDevlinkSocket` | `pyroute2.netlink.devlink` | Devlink netlink socket. |

## Events, Diagnostics, Namespaces, And Protocol Helpers

| Model | Root import | Direct path | Represents / contains |
|---|---|---|---|
| `EventSocket` / `AsyncEventSocket` | `from pyroute2 import EventSocket, AsyncEventSocket` | `pyroute2.netlink.event` | Generic netlink event socket. |
| `AcpiEventSocket` / `AsyncAcpiEventSocket` | `from pyroute2 import AcpiEventSocket, AsyncAcpiEventSocket` | `pyroute2.netlink.event.acpi_event` | ACPI event socket. |
| `DQuotSocket` / `AsyncDQuotSocket` | `from pyroute2 import DQuotSocket, AsyncDQuotSocket` | `pyroute2.netlink.event.dquot` | Disk quota event socket. |
| `ThermalEventSocket` / `AsyncThermalEventSocket` | `from pyroute2 import ThermalEventSocket, AsyncThermalEventSocket` | `pyroute2.netlink.event.thermal` | Thermal event socket. |
| `DiagSocket` | `from pyroute2 import DiagSocket` | `pyroute2.netlink.diag.DiagSocket` | Socket diagnostics netlink API. |
| `UeventSocket` | `from pyroute2 import UeventSocket` | `pyroute2.netlink.uevent.UeventSocket` | Kernel uevent socket. |
| `TaskStats` / `AsyncTaskStats` | `from pyroute2 import TaskStats, AsyncTaskStats` | `pyroute2.netlink.taskstats` | Taskstats netlink API. |
| `ProcEventSocket` | `from pyroute2 import ProcEventSocket` | `pyroute2.netlink.connector.cn_proc.ProcEventSocket` | Process connector events. |
| `NSPopen` | `from pyroute2 import NSPopen` | `pyroute2.nslink.nspopen.NSPopen` | Run subprocesses inside a network namespace. |
| `Plan9ClientSocket` / `Plan9ServerSocket` | `from pyroute2 import Plan9ClientSocket, Plan9ServerSocket` | `pyroute2.plan9.client/server` | Plan9 9p2000 protocol sockets. |

## Exceptions

Import from root or from the direct module:

```python
from pyroute2 import NetlinkError, NetlinkDecodeError, NetlinkDumpInterrupted
from pyroute2.netlink.exceptions import NetlinkError
```

`CommitException` and `CreateException` come from deprecated `IPDB`; avoid
using them in new NDB code unless maintaining existing IPDB integrations.
