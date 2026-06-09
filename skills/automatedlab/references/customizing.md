# Customizing machines after deployment

Everything here runs **after** `Install-Lab`. The VMs must exist first.

## Invoke-LabCommand — run code inside VMs

Works like `Invoke-Command`, but AL adds name resolution (Hyper-V via LMHosts,
Azure via the load balancer's public IP/port), authentication with the lab
account, and CredSSP. **Without `-PassThru` it returns nothing.**

```powershell
# One machine
Invoke-LabCommand -ComputerName Client1 -ScriptBlock { Get-Date } -PassThru

# All machines, or filtered by role
Invoke-LabCommand -ComputerName (Get-LabVM) -ScriptBlock { hostname } -PassThru
Invoke-LabCommand -ComputerName (Get-LabVM -Role WebServer) -ScriptBlock { Restart-Service W3SVC }
```

### Passing local variables and functions

Local functions/variables aren't available in the remote session. Instead of
rewriting code with `$using:`, pass them through — your code stays runnable
locally too:

```powershell
function Foo { "value of '`$someVar' is $someVar" }
$someVar = 123

Invoke-LabCommand -ComputerName Client1 -ScriptBlock { Foo } `
    -Variable (Get-Variable -Name someVar) -Function (Get-Command -Name Foo)
```

### Double-hop / CredSSP

Every AL machine is enabled as a CredSSP server, so `Invoke-LabCommand` tries
CredSSP first (falling back with a warning if it fails). This makes double-hop
scenarios work out of the box — e.g. reading AD from a member server:

```powershell
Invoke-LabCommand -ComputerName Web1 -ScriptBlock { Get-ADUser -Identity John }
```

### Running a script with supporting files

Put the supporting files in one folder and ship it with `-DependencyFolderPath`.
It is copied to the OS root (`C:\` on Windows, `/` on Linux); your script itself
is referenced with `-FilePath`.

```powershell
Invoke-LabCommand -ComputerName (Get-LabVM) -FilePath .\ConfigureAgent.ps1 `
    -DependencyFolderPath "$labSources\Tools\AgentFiles" -PassThru
```

### Using a local module on the VMs

Send a module the host has but the VM doesn't, then call it remotely:

```powershell
$vms = Get-LabVM -Role ADDS
Send-ModuleToPSSession -Module (Get-Module NTFSSecurity -ListAvailable) `
    -Session (New-LabPSSession -ComputerName $vms)
Invoke-LabCommand -ScriptBlock { Get-NTFSAccess -Path C:\ } -ComputerName $vms -PassThru
```

`Send-ModuleToPSSession` tries SMB first, then the PSSession; `-Scope AllUsers`
or `CurrentUser` controls where it lands, and a switch can pull dependencies too.

## Install-LabSoftwarePackage — install .exe/.msi/.msu

AL copies the installer in (via `Copy-LabFileItem`) and runs it through
`Invoke-LabCommand`. The package must support silent install — pass its silent
switch with `-CommandLine`. `$labSources` always resolves correctly (also on Azure).

```powershell
# From the host, to one or all machines
Install-LabSoftwarePackage -ComputerName Server1 -Path "$labSources\SoftwarePackages\npp.exe" -CommandLine /S
Install-LabSoftwarePackage -ComputerName (Get-LabVM) -Path "$labSources\SoftwarePackages\npp.exe" -CommandLine /S

# Already on the VM → -LocalPath; background with -AsJob
Install-LabSoftwarePackage -LocalPath C:\setup.exe -CommandLine '/qn' -ComputerName (Get-LabVM -Role VisualStudio2015) -AsJob
```

### Installers that refuse to run remotely (e.g. .NET Framework)

Some installers detect the NETWORK token and abort. Use `-AsScheduledJob
-UseShellExecute` so the work runs locally on the VM:

```powershell
Install-LabSoftwarePackage -ComputerName Client7 -AsScheduledJob -UseShellExecute `
    -Path "$labSources\SoftwarePackages\NDP452.exe" -CommandLine '/q /norestart'
Restart-LabVM -ComputerName Client7 -Wait
```

### Installing from a mounted ISO

`Mount-LabIsoImage -PassThru` returns the drive letter inside the VM (which isn't
fixed when the VM has multiple disks):

```powershell
$drive = Mount-LabIsoImage -ComputerName Web1 -IsoPath "$labSources\ISOs\App.iso" -PassThru
Install-LabSoftwarePackage -ComputerName Web1 -LocalPath "$($drive.DriveLetter)\setup.exe" -CommandLine /silent
Dismount-LabIsoImage -ComputerName Web1
```

## Install-LabWindowsFeature — enable roles/features

Wraps `Install-WindowsFeature`; AL handles auth and naming.

```powershell
Install-LabWindowsFeature -FeatureName RSAT -ComputerName 'Server1','Server2' -IncludeAllSubFeature

# Background on many machines, then wait
$jobs = Install-LabWindowsFeature -FeatureName RSAT -ComputerName (Get-LabVM) -IncludeAllSubFeature -AsJob -PassThru
$result = Wait-LWLabJob -Job $jobs -ProgressIndicator 10 -NoDisplay -PassThru
```

`-AsJob -PassThru` returns the job objects; `-PassThru` alone returns the feature
install result.
