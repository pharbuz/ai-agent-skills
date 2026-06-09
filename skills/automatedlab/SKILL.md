---
name: automatedlab
description: >-
  Create, deploy, and manage virtual machine labs (Hyper-V and Azure) with the
  AutomatedLab PowerShell framework. Use this WHENEVER the user wants to build a
  lab, a test/VM environment, a domain controller / Active Directory lab, or a
  SQL, Exchange, SharePoint, PKI/CA, failover cluster, or Linux lab — or when
  they write, run, or debug scripts using cmdlets like New-LabDefinition,
  Add-LabMachineDefinition, Install-Lab, Invoke-LabCommand, Get-LabVM,
  Install-LabSoftwarePackage, or Remove-Lab, even if they never say the word
  "AutomatedLab". Also trigger when the user asks to spin up VMs, provision a
  domain, stand up a test environment, or reproduce an infrastructure setup.
---

# AutomatedLab

AutomatedLab (AL) is a PowerShell framework for rapidly building entire labs of
virtual machines — from a single VM to multi-domain environments with AD, SQL,
Exchange, PKI, and more — on **Hyper-V** (local) or **Azure** (cloud). The whole
lab is described as code, so you can redeploy or tear it down with one command.

Source documentation: <https://automatedlab.org/en/latest/>

## Mental model: a lab moves through 4 phases

Every AL script follows the same cycle. Respect this order — it is the heart of
the framework:

1. **Define** — describe the lab in memory: `New-LabDefinition`, optionally
   networks, domains, and credentials, then machines via
   `Add-LabMachineDefinition`. Nothing touches disk or the hypervisor yet.
2. **Deploy** — `Install-Lab` takes the definition and creates switches, base
   disks, VMs, promotes domain controllers, and installs roles. This is when
   everything is actually built.
3. **Customize** — after deployment, configure the machines:
   `Invoke-LabCommand` (run code inside a VM), `Install-LabSoftwarePackage`,
   `Install-LabWindowsFeature`, `Copy-LabFileItem`, mounting ISOs.
4. **Manage** — `Import-Lab` (load an existing lab in a new session), snapshots
   (`Checkpoint-LabVM` / `Restore-LabVMSnapshot`), and finally `Remove-Lab` to
   delete everything.

## Canonical skeleton

Every lab starts from this pattern. A single server is literally three lines:

```powershell
New-LabDefinition -Name GettingStarted -DefaultVirtualizationEngine HyperV
Add-LabMachineDefinition -Name FirstServer -OperatingSystem 'Windows Server 2022 Datacenter'
Install-Lab
Show-LabDeploymentSummary
```

A lab with a domain, several machines, and shared settings — the pattern you'll
use most often (`$PSDefaultParameterValues` removes repetition):

```powershell
New-LabDefinition -Name Lab1 -DefaultVirtualizationEngine HyperV

# Settings shared by ALL machines — cleaner than repeating them on every call
$PSDefaultParameterValues = @{
    'Add-LabMachineDefinition:DomainName'      = 'contoso.com'
    'Add-LabMachineDefinition:Memory'          = 2GB
    'Add-LabMachineDefinition:OperatingSystem' = 'Windows Server 2022 Datacenter (Desktop Experience)'
}

Add-LabMachineDefinition -Name DC1     -Roles RootDC
Add-LabMachineDefinition -Name SQL1    -Roles SQLServer2022
Add-LabMachineDefinition -Name Client1 -OperatingSystem 'Windows 11 Pro'  # overrides default OS

Install-Lab
Show-LabDeploymentSummary
```

AL handles automatically whatever you leave undefined: it picks a free IP range,
creates a virtual switch, sizes RAM from the roles, and chooses the fastest disk
for the VMs. The more you leave to automation, the shorter the script.

## Before you generate a script — prerequisites

AL cannot install an OS without the installation media. When generating a script
for the user, always remind them of what must exist on their side:

- **OS ISO files** (and product media such as SQL/Exchange) in the
  `LabSources\ISOs` folder. Check available OSes with
  `Get-LabAvailableOperatingSystem -Path <path to LabSources>`. The string in
  `-OperatingSystem` must match a name from that list exactly.
- **Hyper-V**: PowerShell launched elevated (as admin), a CPU with virtualization
  (Intel VT-x / AMD-V), plenty of RAM, and fast storage (SSD/NVMe — not HDD).
- **Azure**: run `Connect-AzAccount` before deploying and add
  `Add-LabAzureSubscription` to the script. From Linux/macOS, AL works **only**
  against Azure.
- Module installed: `Install-Module AutomatedLab -SkipPublisherCheck`, and on
  first use `Enable-LabHostRemoting -Force` plus `New-LabSourcesFolder`.

Installation and host configuration details → [`references/install.md`](references/install.md).

## Core cmdlets (cheat sheet)

| Phase | Cmdlet | Purpose |
|-------|--------|---------|
| Define | `New-LabDefinition` | Start a lab; `-Name`, `-DefaultVirtualizationEngine HyperV\|Azure`, `-VmPath` |
| Define | `Add-LabMachineDefinition` | Add a machine; `-Name`, `-OperatingSystem`, `-Roles`, `-DomainName`, `-IpAddress`, `-Memory`, `-Network` |
| Define | `Add-LabVirtualNetworkDefinition` | Manual network; `-AddressSpace`, `-HyperVProperties`, `-AzureProperties` |
| Define | `Add-LabDomainDefinition` | Explicit domain definition (multi-forest environments) |
| Define | `Set-LabInstallationCredential` | Username/password for the lab admin account |
| Define | `Get-LabMachineRoleDefinition` | Role with parameters (`-Role`, `-Properties @{}`) |
| Define | `Add-LabDiskDefinition` | Additional data disks |
| Define | `Add-LabIsoImageDefinition` | Register product ISO (e.g. SQL) for use in the lab |
| Deploy | `Install-Lab` | Builds the whole lab; `-Domains` installs only AD |
| Deploy | `Show-LabDeploymentSummary` | Post-deployment summary |
| Customize | `Invoke-LabCommand` | Run a ScriptBlock/script inside a VM (auth + naming handled) |
| Customize | `Install-LabSoftwarePackage` | Install .exe/.msi/.msu inside a VM |
| Customize | `Install-LabWindowsFeature` | Enable Windows roles/features |
| Customize | `Mount-LabIsoImage` / `Dismount-LabIsoImage` | Mount an ISO inside a VM |
| Customize | `Copy-LabFileItem` | Copy files host → VM |
| Manage | `Get-LabVM` (alias `Get-LabMachine`) | List machines; `-Role`, `-All` |
| Manage | `Import-Lab` | Load an existing lab; `-Name`, `-NoValidation` |
| Manage | `Checkpoint-LabVM` / `Restore-LabVMSnapshot` | Snapshots |
| Manage | `Remove-Lab` | Delete the whole lab (VMs, disks, switches) |

Full reference with parameters and examples → [`references/cmdlets.md`](references/cmdlets.md).

## Roles — the heart of machine configuration

A role tells AL what a machine should be (DC, SQL, CA, web…). A machine can have
zero, one, or many roles. Simple assignment (no tuning):

```powershell
Add-LabMachineDefinition -Name DC1  -Roles RootDC
Add-LabMachineDefinition -Name CA1  -Roles CaRoot, Routing      # multiple roles at once
Add-LabMachineDefinition -Name Web1 -Roles WebServer
```

When a role needs tuning (e.g. forest functional level, SQL features), use
`Get-LabMachineRoleDefinition` with a `-Properties` hashtable:

```powershell
$role = Get-LabMachineRoleDefinition -Role SQLServer2022 -Properties @{ Features = 'SQL,Tools' }
Add-LabMachineDefinition -Name SQL1 -Roles $role
```

Key role families: **RootDC / FirstChildDC / DC** (Active Directory),
**SQLServer2012…2022/2025**, **CaRoot / CaSubordinate** (PKI), **WebServer**,
**Routing** (router / internet access), **DHCP**, **FailoverNode/Storage**,
**HyperV**, **SharePoint2013/2016/2019**, **ConfigurationManager**, the Remote
Desktop Services roles, **SCVMM**, **ADFS**, and more.

Full role list + AD/SQL/PKI tuning → [`references/roles.md`](references/roles.md).

## Customizing machines after deployment

`Invoke-LabCommand` is your main remote control — it works like `Invoke-Command`
but handles authentication, name resolution (Hyper-V and Azure), and CredSSP
(double-hop) for you. Without `-PassThru` it returns no data.

```powershell
# On a specific machine
Invoke-LabCommand -ComputerName DC1 -ScriptBlock { Get-ADDomain } -PassThru

# On all / selected machines by role
Invoke-LabCommand -ComputerName (Get-LabVM) -ScriptBlock { Get-Date } -PassThru
Invoke-LabCommand -ComputerName (Get-LabVM -Role WebServer) -ScriptBlock { ... }

# Push local variables/functions into the remote session
Invoke-LabCommand -ComputerName Client1 -ScriptBlock { Foo } `
    -Variable (Get-Variable someVar) -Function (Get-Command Foo)
```

Installing software and Windows features:

```powershell
Install-LabSoftwarePackage -ComputerName (Get-LabVM) -Path "$labSources\SoftwarePackages\npp.exe" -CommandLine /S
Install-LabWindowsFeature  -ComputerName 'Web1' -FeatureName Web-Server -IncludeManagementTools
```

More (CredSSP, `-AsScheduledJob` for .NET, `Send-ModuleToPSSession`, ISOs) →
[`references/customizing.md`](references/customizing.md).

## Networking

By default, define nothing — AL finds a free subnet (incrementing from
192.168.1.0) and creates a switch. Define a network manually when you need a
specific range or internet access:

```powershell
# Internal — isolated lab network with a specific range
Add-LabVirtualNetworkDefinition -Name LabNet -AddressSpace 192.168.30.0/24

# External — with internet access (Hyper-V bridges through the host NIC)
Add-LabVirtualNetworkDefinition -Name LabNet -AddressSpace 192.168.30.0/24 `
    -HyperVProperties @{ SwitchType = 'External'; AdapterName = 'Ethernet' }
```

Routing between subnets is handled by a machine with the `Routing` role. Details
(multi-subnet, DMZ, Azure VNet/peering) → [`references/networking.md`](references/networking.md).

## Azure (quick start)

```powershell
New-LabDefinition -Name MyAzureLab -DefaultVirtualizationEngine Azure
Add-LabAzureSubscription -DefaultLocationName 'West Europe'
# ...then Add-LabMachineDefinition / Install-Lab as usual
```

Requires a prior `Connect-AzAccount`. Choose VM sizes with a decent number of
IOPS, or deployments will fail with timeouts. Per-machine cloud options go
through `-AzureProperties @{ RoleSize = 'Standard_D2_v2'; ... }`. Details +
Azure Stack Hub → [`references/azure.md`](references/azure.md).

## Lab lifecycle

```powershell
Import-Lab -Name Lab1 -NoValidation     # load a lab in a new session (fast, skips validation)
Get-LabVM                               # what's in the lab
Checkpoint-LabVM -ComputerName DC1 -SnapshotName 'before-change'
Restore-LabVMSnapshot -ComputerName DC1 -SnapshotName 'before-change'
Remove-Lab -Name Lab1 -Confirm:$false   # destroy everything
```

Modifying an existing lab, offline work (ISO patching), and joining an existing
domain (`-SkipDeployment`) → [`references/lab-management.md`](references/lab-management.md).

## How to generate scripts on request

When the user says "build me a lab with…", assemble the script using this recipe:

1. **Pick the hypervisor** — default `HyperV`; use `Azure` if the user mentions
   it or is on Linux/macOS.
2. **Naming** — short, descriptive machine names (`DC1`, `SQL1`, `WEB1`,
   `CLIENT1`). Domain defaults to `contoso.com` unless another is given.
3. **Derive roles from the requirements** — "domain controller" → `RootDC`;
   "SQL database" → `SQLServer2022`; "website/IIS" → `WebServer`; "certificate
   authority" → `CaRoot`; "internet access / router" → a machine with the
   `Routing` role + an External network.
4. **Remove repetition** with `$PSDefaultParameterValues` (OS, Memory, DomainName).
5. **End with** `Install-Lab` + `Show-LabDeploymentSummary`.
6. **Add customizations** (`Invoke-LabCommand`, `Install-LabSoftwarePackage`)
   AFTER `Install-Lab`, never before.

Make sensible assumptions (RAM, OS), but **state them** in script comments and
remind the user about the ISOs. Ready-to-run patterns to copy live in
[`examples/`](examples/) — start from the closest one and adapt it rather than
writing from scratch.

## Common pitfalls

- **Missing ISO / wrong OS name** → deployment stalls. Run
  `Get-LabAvailableOperatingSystem` first.
- **Customizing before `Install-Lab`** → the VM doesn't exist yet. The phase
  order is sacred.
- **`Invoke-LabCommand` without `-PassThru`** → the command runs but you see
  nothing.
- **Changing key settings after deployment** (e.g. the domain) → unsupported; AL
  only supports what the product itself supports. Remove the DC and redeploy.
- **Non-elevated PowerShell (Hyper-V)** → deployment fails.
- **Slow disk (HDD)** → timeouts. Use SSD/NVMe.

## Helper files in this skill

- `references/install.md` — installing AL, the LabSources folder, host configuration
- `references/cmdlets.md` — full cmdlet reference by phase
- `references/roles.md` — all roles + AD / SQL / PKI tuning
- `references/networking.md` — networks, internet, multi-subnet, DMZ, Azure VNet
- `references/customizing.md` — Invoke-LabCommand, software, features, CredSSP, ISOs
- `references/azure.md` — Azure and Azure Stack Hub
- `references/lab-management.md` — import, modify, snapshots, offline, Remove-Lab
- `examples/*.ps1` — complete, working lab scripts to copy
