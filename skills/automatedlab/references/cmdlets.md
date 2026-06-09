# Cmdlet reference (by phase)

A focused reference for the cmdlets you reach for most. For full parameter lists,
run `Get-Help <Cmdlet> -Full` in a session with AutomatedLab imported.

## Table of contents

- [Phase 1 — Define](#phase-1--define)
- [Phase 2 — Deploy](#phase-2--deploy)
- [Phase 3 — Customize](#phase-3--customize)
- [Phase 4 — Manage](#phase-4--manage)
- [Discovery / introspection](#discovery--introspection)

---

## Phase 1 — Define

### New-LabDefinition
Creates the in-memory container that holds networks and machines. Mandatory:
a unique `-Name` and the virtualization engine.

```powershell
New-LabDefinition -Name MyLab -DefaultVirtualizationEngine HyperV -VmPath D:\AutomatedLab-VMs
```

- `-Name` — unique lab name.
- `-DefaultVirtualizationEngine` — `HyperV` (local) or `Azure` (cloud).
- `-VmPath` — where VMs are created. If omitted, AL picks the fastest non-system
  drive (via `Get-DiskSpeed`, cached) and makes an `AutomatedLab-VMs` folder.

Definitions are exported to XML (default `~\Documents\AutomatedLab-Labs` /
`C:\ProgramData\AutomatedLab\Labs`) so you can `Import-Lab` later.

### Add-LabMachineDefinition
Adds one machine. Ranges from trivial to highly customized — same cmdlet.

```powershell
Add-LabMachineDefinition -Name DC1 -Roles RootDC `
    -OperatingSystem 'Windows Server 2022 Datacenter' -Domain contoso.com
```

Common parameters:

| Parameter | Meaning |
|-----------|---------|
| `-Name` | Machine (computer) name |
| `-OperatingSystem` | Exact OS name from `Get-LabAvailableOperatingSystem`, or an OS object |
| `-Roles` | One or more role names, or a role object from `Get-LabMachineRoleDefinition` |
| `-DomainName` | Domain to join / create |
| `-IpAddress` | Static IP (otherwise auto-assigned) |
| `-Memory` / `-MinMemory` / `-MaxMemory` | RAM (dynamic memory if min/max given) |
| `-Processors` | vCPU count |
| `-Network` | Name of a network from `Add-LabVirtualNetworkDefinition` |
| `-DiskName` | Attach a data disk from `Add-LabDiskDefinition` |
| `-PostInstallationActivity` | Custom-role / activity object to run after install |
| `-AzureProperties` | Hashtable of Azure-specific options (see azure.md) |
| `-SkipDeployment` | Reference an existing machine instead of creating it (see lab-management.md) |

If a name/version combo is ambiguous (e.g. 32-bit vs 64-bit with the same name),
fetch the OS object explicitly and pass it:

```powershell
$os = Get-LabAvailableOperatingSystem -UseOnlyCache |
      Where-Object { $_.OperatingSystemName -eq 'Windows 10 Enterprise LTSC' -and $_.Architecture -eq 'x64' }
Add-LabMachineDefinition -Name Client1 -OperatingSystem $os
```

### Get-LabMachineRoleDefinition
Produces a role object with tuning options, for passing to `-Roles`.

```powershell
$role = Get-LabMachineRoleDefinition -Role FirstChildDC -Properties @{
    ParentDomain = 'contoso.com'; NewDomain = 'emea'; DomainFunctionalLevel = 'Win2012R2'
}
Add-LabMachineDefinition -Name LDC1 -IpAddress 192.168.50.10 -DomainName emea.contoso.com -Roles $role
```

### Add-LabVirtualNetworkDefinition
Manual network. See [networking.md](networking.md).

### Add-LabDomainDefinition
Declare a domain explicitly (needed in multi-forest labs where AL cannot infer
the topology) and supply admin credentials for it.

```powershell
Add-LabDomainDefinition -Name contoso.com -AdminUser admin -AdminPassword 'Somepass1'
```

### Set-LabInstallationCredential
Sets the username/password of the lab admin account used everywhere.

```powershell
Set-LabInstallationCredential -Username Install -Password 'Somepass1'
```

### Add-LabDiskDefinition
Define an extra data disk to attach via `-DiskName`.

```powershell
Add-LabDiskDefinition -Name SqlData -DiskSizeInGb 50
```

### Add-LabIsoImageDefinition
Register a product ISO (SQL, Exchange, …) so a role can install from it.

```powershell
Add-LabIsoImageDefinition -Name SQLServer2022 -Path "$labSources\ISOs\SQLServer2022.iso"
```

---

## Phase 2 — Deploy

### Install-Lab
Builds everything defined so far. Run once after all definitions.

```powershell
Install-Lab                # full deployment
Install-Lab -Domains       # only stand up Active Directory / promote DCs
```

Since v5.23, deployments are validated before and after install when Pester
5.0.1+ is present (Pester is an optional dependency, not auto-installed).

### Show-LabDeploymentSummary
Prints a summary (machines, IPs, time taken). Call it after `Install-Lab`.

```powershell
Show-LabDeploymentSummary
Show-LabDeploymentSummary -Detailed
```

---

## Phase 3 — Customize

### Invoke-LabCommand
Run code inside lab VMs. Handles auth, name resolution, and CredSSP. Returns data
only with `-PassThru`. Full treatment in [customizing.md](customizing.md).

```powershell
Invoke-LabCommand -ComputerName (Get-LabVM) -ScriptBlock { hostname } -PassThru
Invoke-LabCommand -ComputerName Web1 -FilePath .\Configure.ps1 -DependencyFolderPath "$labSources\Tools\App"
```

### Install-LabSoftwarePackage
Install `.exe` / `.msi` / `.msu` packages in VMs.

```powershell
Install-LabSoftwarePackage -ComputerName Server1 -Path "$labSources\SoftwarePackages\npp.exe" -CommandLine /S
Install-LabSoftwarePackage -LocalPath C:\setup.exe -CommandLine '/qn' -ComputerName (Get-LabVM) -AsJob
```

- `-Path` (host file, copied in) vs `-LocalPath` (already on the VM).
- `-AsScheduledJob -UseShellExecute` for installers that refuse to run remotely
  (e.g. .NET Framework). `-AsJob` to background it.

### Install-LabWindowsFeature
Enable Windows roles/features (wraps `Install-WindowsFeature`).

```powershell
Install-LabWindowsFeature -FeatureName RSAT -ComputerName 'Server1','Server2' -IncludeAllSubFeature
$jobs = Install-LabWindowsFeature -FeatureName RSAT -ComputerName (Get-LabVM) -AsJob -PassThru
Wait-LWLabJob -Job $jobs -ProgressIndicator 10 -NoDisplay
```

### Mount-LabIsoImage / Dismount-LabIsoImage
Mount an ISO inside a VM; `-PassThru` returns the drive it landed on.

```powershell
$drive = Mount-LabIsoImage -ComputerName Web1 -IsoPath "$labSources\ISOs\App.iso" -PassThru
Install-LabSoftwarePackage -ComputerName Web1 -LocalPath "$($drive.DriveLetter)\setup.exe" -CommandLine /silent
Dismount-LabIsoImage -ComputerName Web1
```

### Copy-LabFileItem
Copy files from host to VM(s).

```powershell
Copy-LabFileItem -Path "$labSources\Tools\config.json" -ComputerName Web1 -DestinationFolderPath C:\App
```

### Send-ModuleToPSSession
Push a locally available PowerShell module into VM sessions.

```powershell
Send-ModuleToPSSession -Module (Get-Module NTFSSecurity -ListAvailable) `
    -Session (New-LabPSSession -ComputerName (Get-LabVM -Role ADDS))
```

---

## Phase 4 — Manage

### Import-Lab
Load an already-deployed lab into a fresh session.

```powershell
Import-Lab -Name MyLab -NoValidation   # -NoValidation = fast import
```

### Snapshots
```powershell
Checkpoint-LabVM       -ComputerName DC1 -SnapshotName clean
Get-LabVMSnapshot      -ComputerName DC1
Restore-LabVMSnapshot  -ComputerName DC1 -SnapshotName clean
Remove-LabVMSnapshot   -ComputerName DC1 -SnapshotName clean
```

### Start/stop/restart
```powershell
Start-LabVM   -ComputerName DC1
Stop-LabVM    -ComputerName DC1
Restart-LabVM -ComputerName DC1 -Wait
```

### Remove-Lab
Deletes VMs, disks, and switches. Leaves base disks for the next deployment.

```powershell
Remove-Lab -Name MyLab -Confirm:$false
Remove-LabVM -Name OldMachine     # remove a single VM from an imported lab
```

---

## Discovery / introspection

```powershell
Get-LabAvailableOperatingSystem -Path C:\LabSources   # OS names you can deploy
Get-LabVM                                             # machines in the current lab
Get-LabVM -Role SQLServer2022                         # filter by role
Get-Lab -List                                         # all known labs on the host
Get-LabConfigurationItem -Name RequiredAzStackModules # AL configuration values
Get-PSFConfig -Module AutomatedLab -Name SQL*         # tweakable settings (URLs etc.)
Enter-LabPSSession -ComputerName DC1                  # interactive remote session
Connect-LabVM -ComputerName Client1                   # open a console/RDP to the VM
```
