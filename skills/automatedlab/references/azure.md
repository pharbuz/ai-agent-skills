# Azure & Azure Stack Hub

AutomatedLab works with Azure Resource Manager. Most things are handled for you;
the main extra step is authentication.

## Standard Azure

Authenticate first (saves your profile so you can `Import-Lab` later), then point
the lab at Azure:

```powershell
Connect-AzAccount                       # or rely on a saved ARM profile

New-LabDefinition -Name MyLab -DefaultVirtualizationEngine Azure
Add-LabAzureSubscription -DefaultLocationName 'West Europe'

# ...Add-LabMachineDefinition / Install-Lab as usual
```

`Add-LabAzureSubscription` creates a lab-sources resource group plus a dedicated
resource group per lab. `Remove-Lab` deletes the lab's resource group and
everything in it.

> If your profile expires you'll see an error — just `Connect-AzAccount` again.
>
> **Use VM sizes with decent IOPS.** Underpowered sizes cause deployment errors
> and timeouts.

## Per-machine Azure options (`-AzureProperties`)

| Key | Meaning |
|-----|---------|
| `ResourceGroupName` | Deploy this machine into a different resource group |
| `RoleSize` | Specific size, e.g. `Standard_D2_v2` |
| `UseAllRoleSizes` | Pick a random size from the available ones |
| `LoadBalancerRdpPort` | Custom inbound NAT port for RDP (must be unique in the lab) |
| `LoadBalancerWinRmHttpPort` / `LoadBalancerWinRmHttpsPort` | Custom WinRM NAT ports (unique) |
| `LoadBalancerAllowedIp` | Comma-separated string (NOT an array) of allowed IPs, e.g. `"$(Get-PublicIpAddress), 1.2.3.4"` |
| `SubnetName` | Subnet to deploy into |
| `UseByolImage` | `'true'` for bring-your-own-license images |
| `AutoshutdownTime` / `AutoshutdownTimezoneId` | Auto-shutdown schedule (strings) |
| `StorageSku` | Data-disk SKU: `Standard_LRS`, `Premium_LRS`, or `StandardSSD_LRS` |

```powershell
Add-LabMachineDefinition -Name SQL1 -Roles SQLServer2022 -AzureProperties @{
    RoleSize          = 'Standard_D4s_v5'
    AutoshutdownTime  = '19:00'
    AutoshutdownTimezoneId = 'W. Europe Standard Time'
}
```

> SQL on Azure defaults to a **managed instance** unless properties (e.g. custom
> service accounts) force a normal IaaS VM — in which case SQL is installed from
> an ISO that must be present in your Azure LabSources.

## Lab sources on Azure

The host's LabSources can be synced to an Azure file share so VMs can reach ISOs
and packages. Sync (and related settings) are exposed via PSF config:

```powershell
Get-PSFConfig -Module AutomatedLab -Name *LabSources*
# AutoSyncLabSources, LabSourcesMaxFileSizeMb, LabSourcesSyncIntervalDays
```

## Azure Stack Hub

Targeting Azure Stack Hub needs specific (older) module versions and an explicit
environment connection.

Prerequisites: a registered Azure Stack Hub with connectivity (e.g. VPN), a
subscription with the relevant resource providers registered, a marketplace
populated with AL-compatible OS images, and internet on the host to download
modules. Validate with:

```powershell
Test-LabAzureModuleAvailability -Verbose -AzureStack
Get-LabConfigurationItem -Name RequiredAzStackModules
```

Install the required module versions:

```powershell
Remove-Module -Name Az.* -Force
if (-not (Test-LabAzureModuleAvailability -AzureStack)) {
    Install-LabAzureRequiredModule -AzureStack
}
```

Connect to the environment:

```powershell
$Environment   = 'azs'
$ArmEndpointUrl = 'https://management.local.azurestack.external'  # your own
$AADTenantName = 'YourTenant.onmicrosoft.com'                     # your own

if (-not (Get-AzEnvironment -Name $Environment)) {
    $null = Add-AzEnvironment -Name $Environment -ArmEndpoint $ArmEndpointUrl
}
$AuthEndpoint = (Get-AzEnvironment -Name $Environment).ActiveDirectoryAuthority
$TenantId = (Invoke-RestMethod "$($AuthEndpoint)$($AADTenantName)/.well-known/openid-configuration").issuer.TrimEnd('/').Split('/')[-1]
$null = Connect-AzAccount -EnvironmentName $Environment -TenantId $TenantId
```

Then in the lab script use the right location and the `AzureStack` switch:

```powershell
New-LabDefinition -Name AzSLab -DefaultVirtualizationEngine Azure
Add-LabAzureSubscription -DefaultLocationName local -Environment $Environment -AzureStack
```
