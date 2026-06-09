# Installation & host setup

AutomatedLab is a set of PowerShell modules. There are two ways to install it.

## From the PowerShell Gallery (recommended, works on PS 7 / Linux too)

This is the **only** supported way to install AL and its dependencies on
PowerShell Core / PowerShell 7 on both Windows and Linux / Azure Cloud Shell.

```powershell
Install-PackageProvider Nuget -Force
# -SkipPublisherCheck: AutomatedLabTest needs Pester v5. On systems where only
# Pester v3 ships, you get an error without this parameter.
Install-Module AutomatedLab -SkipPublisherCheck
```

### First-time host configuration

```powershell
# Enable the host remoting AL relies on (run once)
Enable-LabHostRemoting -Force

# Create the sample LabSources folder structure
New-LabSourcesFolder -DriveLetter C        # Windows
# On Linux, point LabSources somewhere writable, then create it:
# Set-PSFConfig -Module AutomatedLab -Name LabSourcesLocation -Value /home/youruser/labsources -PassThru | Register-PSFConfig
# New-LabSourcesFolder
```

### Telemetry opt-out (optional)

AL collects anonymous telemetry. To pre-configure it non-interactively:

```powershell
# Windows
[Environment]::SetEnvironmentVariable('AUTOMATEDLAB_TELEMETRY_OPTIN', 'false', 'Machine')
$env:AUTOMATEDLAB_TELEMETRY_OPTIN = 'false'

# Linux/macOS — drop a marker file
$null = New-Item -ItemType File -Force -Path "$((Get-PSFConfigValue -FullName AutomatedLab.LabAppDataRoot))/telemetry.disabled"
```

### Linux note

If you do not start `pwsh` with `sudo`, redirect the AL app-data root once:

```powershell
Set-PSFConfig -Module AutomatedLab -Name LabAppDataRoot -Value /home/youruser/.alConfig -PassThru | Register-PSFConfig
```

## From the MSI (Windows only)

Download from <https://github.com/AutomatedLab/AutomatedLab/releases>.

- "Typical" and "Complete" install to default locations: modules go to
  `C:\Program Files\WindowsPowerShell\Modules`, the rest to `C:\LabSources`.
- **Prefer a custom install** and place **LabSources** on a disk with enough free
  space for ISO files (it can grow large). It does not need to be an SSD, but the
  VM disk path should be. Do not move the modules unless you know what you're doing.

## The LabSources folder

This is the working directory AL reads media and packages from. `$labSources`
(an automatic variable AL defines) always points to it, so you rarely hard-code
the path. Typical layout:

```
LabSources\
├── ISOs\                 # OS and product ISO files go here
├── SoftwarePackages\     # .exe / .msi / .msu installers for Install-LabSoftwarePackage
├── Tools\                # files/agents you push into VMs
├── PostInstallationActivities\
└── CustomRoles\
```

After installation the `ISOs` folder contains only a placeholder text file. Drop
your OS ISOs there (download from the Microsoft Evaluation Center or your MSDN /
Visual Studio subscription).

## Requirements at a glance

| Area | Requirement |
|------|-------------|
| PowerShell | WMF 5+ or (ideally) PowerShell 7 |
| Windows host | Windows Server 2012 R2+ / Windows 8.1+, **elevated** session, en-us OS recommended |
| CPU | Intel VT-x or AMD-V capable |
| RAM | Generous — every VM consumes some |
| Storage | Low-latency, high-throughput (SSD/NVMe). **No spinning disks** |
| Linux/macOS | PowerShell Core 6+, SSH or gss-ntlmssp for remoting, `ip`/`route` available, **Azure only** |
| Media | OS ISO files for every role you deploy |

## Verify the media is readable

```powershell
Get-LabAvailableOperatingSystem -Path C:\LabSources
```

This lists every OS image AL finds across the ISOs in the folder. The exact
`OperatingSystemName` values it returns are what you pass to
`Add-LabMachineDefinition -OperatingSystem`.
