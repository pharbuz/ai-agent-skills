# Roles

A role tells AutomatedLab what a machine should become. A machine can have zero,
one, or several roles. Some roles are mutually exclusive (e.g. `RootDC` and
`FirstChildDC`, or two different `SQLServer*` versions on one box).

## Two ways to assign a role

**Simple** — no customization:

```powershell
Add-LabMachineDefinition -Name DC1  -Roles RootDC
Add-LabMachineDefinition -Name CA1  -Roles CaRoot, Routing
Add-LabMachineDefinition -Name Web1 -Roles WebServer
```

**Customized** — build a role object with `Get-LabMachineRoleDefinition` and a
`-Properties` hashtable, then pass it to `-Roles`:

```powershell
$role = Get-LabMachineRoleDefinition -Role Exchange2019 -Properties @{ OrganizationName = 'TestOrg' }
Add-LabMachineDefinition -Name EX1 -Memory 8GB -DomainName contoso.com -Roles $role -DiskName ExDataDisk
```

When a role's RAM is left to AL, it is sized automatically from the role.

## Full list of built-in roles

| Category | Roles |
|----------|-------|
| Active Directory | `RootDC`, `FirstChildDC`, `DC` |
| Certificate Services (PKI) | `CaRoot`, `CaSubordinate` |
| SQL Server | `SQLServer2008`, `SQLServer2008R2`, `SQLServer2012`, `SQLServer2014`, `SQLServer2016`, `SQLServer2017`, `SQLServer2019`, `SQLServer2022`, `SQLServer2025` |
| Web / network infra | `WebServer`, `Routing`, `DHCP`, `FileServer` |
| Failover Clustering | `FailoverNode`, `FailoverStorage` |
| Virtualization | `HyperV` |
| SharePoint | `SharePoint2013`, `SharePoint2016`, `SharePoint2019` |
| System Center — Config Mgr | `ConfigurationManager` |
| System Center — Operations Mgr | `ScomManagement`, `ScomConsole`, `ScomGateway`, `ScomReporting`, `ScomWebConsole` |
| System Center — VMM | `Scvmm2016`, `Scvmm2019`, `Scvmm2022` |
| ADFS | `ADFS`, `ADFSProxy`, `ADFSWAP` |
| Remote Desktop Services | `RemoteDesktopConnectionBroker`, `RemoteDesktopGateway`, `RemoteDesktopLicensing`, `RemoteDesktopSessionHost`, `RemoteDesktopVirtualizationHost`, `RemoteDesktopWebAccess` |
| DevOps / TFS | `AzDevOps`, `Tfs2015`, `Tfs2017`, `Tfs2018`, `TfsBuildWorker` |
| Dynamics 365 | `DynamicsAdmin`, `DynamicsBackend`, `DynamicsFrontend`, `DynamicsFull` |
| Visual Studio | `VisualStudio2013`, `VisualStudio2015` |
| DSC | `DSCPullServer` |
| Management | `WindowsAdminCenter` |

> Roles are Windows-based — Linux VMs do not take roles (but can still be
> domain-joined). Products not on this list (e.g. Skype for Business) are built
> on top of AL by combining `Invoke-LabCommand`, `Install-LabSoftwarePackage`,
> and ISO mounting.

---

## Active Directory: RootDC / FirstChildDC / DC

AL supports multi-forest and/or multi-domain labs in a single deployment. It
infers domains from the DC machines; for complex topologies declare them with
`Add-LabDomainDefinition`.

### RootDC — starts a forest
One per forest. Two RootDCs in the same domain is an error.
Properties: `ForestFunctionalLevel`, `DomainFunctionalLevel`, `SiteName`,
`SiteSubnet`, `DatabasePath`, `LogPath`, `SysvolPath`, `DsrmPassword`.

```powershell
$role = Get-LabMachineRoleDefinition -Role RootDC -Properties @{
    ForestFunctionalLevel = 'Win2012R2'
    DomainFunctionalLevel = 'Win2012R2'
    SiteName              = 'Frankfurt'
    SiteSubnet            = '192.168.10.0/24'
}
Add-LabMachineDefinition -Name DC1 -IpAddress 192.168.10.10 -DomainName contoso.com -Roles $role
```

### FirstChildDC — child domain or new tree
Needs the new domain name and parent. If `NewDomain` is a short name → child
domain; if it's an FQDN → new domain tree.
Properties: `ParentDomain`, `NewDomain`, `DomainFunctionalLevel`, `SiteName`,
`SiteSubnet`.

```powershell
$role = Get-LabMachineRoleDefinition -Role FirstChildDC -Properties @{
    ParentDomain = 'contoso.com'; NewDomain = 'emea'; DomainFunctionalLevel = 'Win2012R2'
}
Add-LabMachineDefinition -Name LDC1 -IpAddress 192.168.50.10 -DomainName emea.contoso.com -Roles $role
```

### DC — additional / read-only DC
Adds a DC to an existing root or child domain. Requires a RootDC or FirstChildDC
to exist. Properties: `SiteName`, `SiteSubnet`, `IsReadOnly` ('true' for RODC).

```powershell
$role = Get-LabMachineRoleDefinition -Role DC -Properties @{ SiteName = 'Milano'; IsReadOnly = 'true' }
Add-LabMachineDefinition -Name RODC1 -IpAddress 192.168.60.10 -DomainName emea.contoso.com -Roles $role
```

Functional level values: `Win2008R2`, `Win2012`, `Win2012R2`, `WinThreshold` (2016).
Install only AD across the lab with `Install-Lab -Domains`.

---

## SQL Server

Deploys any version from 2012 to 2025 on Windows. A bare role assignment installs
a default instance with sample databases. On Azure a managed instance is deployed
by default, unless role properties force an IaaS VM (e.g. custom service accounts).

```powershell
# Default install (engine + sample DBs)
Add-LabMachineDefinition -Name SQL1 -Roles SQLServer2022

# Engine + tools only
$role = Get-LabMachineRoleDefinition -Role SQLServer2022 -Properties @{ Features = 'SQL,Tools' }
Add-LabMachineDefinition -Name SQL1 -Roles $role
```

All SQL role properties are optional:

| Property | Meaning |
|----------|---------|
| `Features` | Comma-separated feature list, e.g. `'SQL,Tools'` |
| `ConfigurationFile` | Full local path to a setup config file (single params can still be overridden) |
| `InstanceName` | Default `MSSQLSERVER` |
| `Collation` | Collation to use |
| `SQLSvcAccount` / `SQLSvcPassword` | SQL service account |
| `AgtSvcAccount` / `AgtSvcPassword` | Agent service account |
| `RsSvcAccount` / `RsSvcPassword` | Reporting Services account |
| `AsSvcAccount` / `AsSvcPassword` / `AsSysAdminAccounts` | Analysis Services |
| `IsSvcAccount` / `IsSvcPassword` | Integration Services |
| `AgtSvcStartupType` / `BrowserSvcStartupType` / `RsSvcStartupType` | Service start types |
| `SQLSysAdminAccounts` | Comma-separated sysadmin accounts |

Referenced service accounts are created automatically if they don't exist. From
SQL 2017+, Reporting Services is downloaded on first use; offline, place it at
`"$labSources\SoftwarePackages\SQLServerReportingServices.exe"`. Tweakable URLs:
`Get-PSFConfig -Module AutomatedLab -Name SQL*`.

---

## PKI (CaRoot / CaSubordinate)

```powershell
Add-LabMachineDefinition -Name CA1 -Roles CaRoot                  # standalone/enterprise root CA
Add-LabMachineDefinition -Name SubCA1 -Roles CaSubordinate        # subordinate CA, chains to the root
```

For two-tier deployments, see the PKI sample scripts in the AutomatedLab docs
(`SampleScripts\HyperV\...\PKI ...`). A CA often pairs with `WebServer` for
publishing CRLs/AIA and with the `Routing` role for connectivity.
