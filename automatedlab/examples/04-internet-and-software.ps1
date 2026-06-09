<#
    Example 04 — Internet-connected lab, plus software & Windows features (Hyper-V)

    A domain with a web server on an External (internet-connected) switch.
    After deployment it installs the IIS Windows feature and a software package,
    showing the customize phase.

    Prerequisites:
      - Windows Server ISO in LabSources\ISOs.
      - An External Hyper-V switch is created by bridging the host NIC named below
        ('Ethernet') — change AdapterName to match your host's adapter
        (Get-NetAdapter shows the names).
      - For the software step: place the installer in
        LabSources\SoftwarePackages\ (the example uses Notepad++ with /S silent).
#>

New-LabDefinition -Name WebLab -DefaultVirtualizationEngine HyperV

# External network = internet access for the lab. AdapterName must be a real host NIC.
Add-LabVirtualNetworkDefinition -Name WebNet -AddressSpace 192.168.30.0/24 `
    -HyperVProperties @{ SwitchType = 'External'; AdapterName = 'Ethernet' }

$PSDefaultParameterValues = @{
    'Add-LabMachineDefinition:DomainName'      = 'contoso.com'
    'Add-LabMachineDefinition:Network'         = 'WebNet'
    'Add-LabMachineDefinition:OperatingSystem' = 'Windows Server 2022 Datacenter (Desktop Experience)'
    'Add-LabMachineDefinition:Memory'          = 2GB
}

Add-LabMachineDefinition -Name DC1  -Roles RootDC    -IpAddress 192.168.30.10
Add-LabMachineDefinition -Name Web1 -Roles WebServer -IpAddress 192.168.30.20

Install-Lab
Show-LabDeploymentSummary

# --- Customize phase (runs after Install-Lab) ---

# Enable IIS with management tools on the web server.
Install-LabWindowsFeature -ComputerName Web1 -FeatureName Web-Server -IncludeManagementTools

# Install a silent software package from the host onto the web server.
Install-LabSoftwarePackage -ComputerName Web1 `
    -Path "$labSources\SoftwarePackages\npp.exe" -CommandLine /S

# Drop a default page and confirm IIS serves it.
Invoke-LabCommand -ComputerName Web1 -PassThru -ScriptBlock {
    Set-Content -Path C:\inetpub\wwwroot\index.html -Value '<h1>AutomatedLab</h1>'
    (Invoke-WebRequest -Uri http://localhost -UseBasicParsing).StatusCode
}
