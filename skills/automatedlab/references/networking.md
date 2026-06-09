# Networking & IP addresses

AutomatedLab can handle networking entirely for you, or you can define every
detail. It also supports multiple subnets and internet-connected labs, and takes
care of routing when a machine has the `Routing` role.

## Fully automatic (the default)

If you just want machines that can talk to each other and don't care about IPs,
define nothing. AL:

- creates the virtual switch,
- finds a free subnet by incrementing `192.168.1.0` until one is free (no existing
  switch in that range and not routable),
- assigns IPs to each machine.

Many intro scripts have no network definition at all. AL prints the chosen subnet
during deployment.

## Manual network definition

Use `Add-LabVirtualNetworkDefinition` (works for both Hyper-V and Azure) when you
need a specific range:

```powershell
Add-LabVirtualNetworkDefinition -Name MySimpleNetwork -AddressSpace 10.1.0.0/16
```

Attach machines to it with `Add-LabMachineDefinition -Network MySimpleNetwork`.

### Hyper-V properties (`-HyperVProperties`)

| Key | Meaning |
|-----|---------|
| `SwitchType` | `Internal` (default) or `External`. `External` requires `AdapterName` |
| `AdapterName` | Host NIC that bridges to the external network |

### Azure properties (`-AzureProperties`)

| Key | Meaning |
|-----|---------|
| `SubnetName` | Name of the subnet to create |
| `SubnetAddressPrefix` | Prefix length (e.g. `24`) |
| `LocationName` | Azure location (should match the lab's default) |
| `DnsServers` | Comma-separated DNS servers |
| `ConnectToVnets` | Peer with other lab VNets (set on all participating definitions) |
| `PeeringVnetResourceIds` | Peer with VNets not managed by AL (full resource IDs) |

## Internet-connected labs

### Hyper-V — bridge to the host's external network

```powershell
Add-LabVirtualNetworkDefinition -Name MyConnectedNet -AddressSpace 10.1.0.0/16 `
    -HyperVProperties @{ SwitchType = 'External'; AdapterName = 'Ethernet' }
```

That's all it takes for machines to reach the internet. For an isolated lab whose
machines still need outbound access, add a router VM instead:

```powershell
Add-LabMachineDefinition -Name Router1 -Roles Routing   # NAT/RRAS between lab subnet and outside
```

### Azure — internet by default

Azure networks are internet-connected through a load balancer that initially
exposes only WinRM and RDP. NAT rules map random external ports to 5985/5986/3389
per machine; the chosen ports are stored so connection cmdlets
(`Enter-LabPSSession`, `Connect-LabVM`) work transparently. Generate an RDP file
with `Get-AzureRmRemoteDesktopFile`.

## Multiple subnets / DMZ

Define several networks and place machines on the right one. A machine with the
`Routing` role bridges the subnets (and optionally the internet), which is how you
build a DMZ:

```powershell
Add-LabVirtualNetworkDefinition -Name Internal -AddressSpace 192.168.10.0/24
Add-LabVirtualNetworkDefinition -Name DMZ      -AddressSpace 192.168.20.0/24 `
    -HyperVProperties @{ SwitchType = 'External'; AdapterName = 'Ethernet' }

# Router sits on both networks; list both with -Network
Add-LabMachineDefinition -Name Edge1 -Roles Routing -Network Internal, DMZ
Add-LabMachineDefinition -Name DC1   -Roles RootDC  -Network Internal -IpAddress 192.168.10.10
Add-LabMachineDefinition -Name Web1  -Roles WebServer -Network DMZ    -IpAddress 192.168.20.10
```
