# Lab lifecycle management

## Importing a deployed lab

A lab's definition is exported to XML during deployment. To work with it in a new
PowerShell session, import it first:

```powershell
Import-Lab -Name MyLab -NoValidation    # -NoValidation skips per-import checks (faster)
Get-LabVM                               # confirm what's there
```

`Get-Lab -List` shows all labs known on the host.

## Modifying an existing lab

> General rule: **AutomatedLab supports only what the product supports.** You
> cannot, for example, change the deployed domain without first removing the DC
> VMs.

### Add or remove machines

```powershell
# Remove a VM from a deployed lab
Import-Lab -Name MyLab -NoValidation
Remove-LabVM -Name OldMachine

# Add/remove via definitions, then re-run Install-Lab
Import-LabDefinition -Name MyLab
Add-LabMachineDefinition -Name NewMachine
Remove-LabMachineDefinition -Name AnotherMachine
Install-Lab
```

Alternatively, just add the new machine to your original script and re-run it —
AL detects already-deployed roles and skips them. This works as long as you don't
change key settings (like the domain).

## Joining an existing domain (`-SkipDeployment`)

You can deploy lab VMs into an existing domain by referencing the real DC with
`-SkipDeployment` instead of creating it. Supply the domain-join credentials.

```powershell
$cred = Get-Credential
Set-LabInstallationCredential -Username ($cred.UserName -split '\\')[-1] -Password $cred.GetNetworkCredential().Password
Add-LabDomainDefinition -Name corp.example.com `
    -AdminUser ($cred.UserName -split '\\')[-1] -AdminPassword $cred.GetNetworkCredential().Password

$PSDefaultParameterValues = @{
    'Add-LabMachineDefinition:DomainName'      = 'corp.example.com'
    'Add-LabMachineDefinition:OperatingSystem' = 'Windows Server 2022 Datacenter'
}

Add-LabMachineDefinition -Name ExistingDC -Roles RootDc -SkipDeployment -IpAddress 10.0.1.101
Add-LabMachineDefinition -Name NewMember1
Add-LabMachineDefinition -Name NewMember2
Install-Lab
```

Connect the lab to the existing network with an external switch
(`Add-LabVirtualNetworkDefinition -HyperVProperties @{ SwitchType = 'External' }`).

## Snapshots

```powershell
Checkpoint-LabVM      -ComputerName DC1 -SnapshotName clean
Checkpoint-LabVM      -All -SnapshotName clean        # snapshot the whole lab
Get-LabVMSnapshot     -ComputerName DC1
Restore-LabVMSnapshot -ComputerName DC1 -SnapshotName clean
Remove-LabVMSnapshot  -ComputerName DC1 -SnapshotName clean
```

A common pattern: deploy, snapshot the whole lab as `clean`, experiment, then
restore to start over without redeploying.

## Power control

```powershell
Start-LabVM   -ComputerName DC1
Stop-LabVM    -ComputerName DC1 -Wait
Restart-LabVM -ComputerName DC1 -Wait
```

## Removing a lab

```powershell
Remove-Lab -Name MyLab -Confirm:$false
```

Removes the VMs, their disks, and the virtual switches. The OS **base disks** are
kept so the next deployment is faster. On Azure, the lab's resource group is
deleted in full.

## Offline / air-gapped labs

AL can patch OS ISOs and run fully offline. Patch an ISO with the latest updates:

```powershell
Update-LabIsoImage -SourceIsoImagePath C:\LabSources\ISOs\Server2022.iso `
    -TargetIsoImagePath C:\LabSources\ISOs\Server2022_patched.iso `
    -UpdateFolderPath C:\LabSources\OSUpdates
```

For offline deployments, also pre-stage any packages the roles would otherwise
download (e.g. SQL Reporting Services at
`"$labSources\SoftwarePackages\SQLServerReportingServices.exe"`).
