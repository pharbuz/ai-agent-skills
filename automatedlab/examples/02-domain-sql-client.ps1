<#
    Example 02 — Domain with SQL Server and a client (Hyper-V)

    A root domain controller (contoso.com), a SQL Server, and a Windows client,
    all on an automatic network. Demonstrates $PSDefaultParameterValues to share
    settings, and registering a product ISO for the SQL role.

    Prerequisites:
      - Windows Server + Windows 11 ISOs in LabSources\ISOs.
      - A SQL Server ISO in LabSources\ISOs (adjust the path/name below).
        Verify OS names with: Get-LabAvailableOperatingSystem -Path C:\LabSources
#>

New-LabDefinition -Name Lab1 -DefaultVirtualizationEngine HyperV

# Register the SQL media so the SQLServer2022 role can install from it.
Add-LabIsoImageDefinition -Name SQLServer2022 -Path "$labSources\ISOs\SQLServer2022.iso"

# Settings shared by every machine — overridable per machine.
$PSDefaultParameterValues = @{
    'Add-LabMachineDefinition:DomainName'      = 'contoso.com'
    'Add-LabMachineDefinition:Memory'          = 2GB
    'Add-LabMachineDefinition:OperatingSystem' = 'Windows Server 2022 Datacenter (Desktop Experience)'
}

Add-LabMachineDefinition -Name DC1     -Roles RootDC
Add-LabMachineDefinition -Name SQL1     -Roles SQLServer2022 -Memory 4GB
Add-LabMachineDefinition -Name Client1 -OperatingSystem 'Windows 11 Pro'   # override the default OS

Install-Lab
Show-LabDeploymentSummary

# Post-deployment check — confirm SQL is up (note -PassThru to get output back):
Invoke-LabCommand -ComputerName SQL1 -PassThru -ScriptBlock {
    (Get-Service 'MSSQLSERVER').Status
}
