<#
    Example 03 — Multi-forest Active Directory with custom networks (Hyper-V)

    Two separate forests on two manually-defined subnets, each with its own root
    domain controller, plus a member server in the first forest. Shows explicit
    networks, static IPs, and a customized RootDC role (functional level + site).

    Prerequisites:
      - Windows Server ISO in LabSources\ISOs.
      - Verify OS names with: Get-LabAvailableOperatingSystem -Path C:\LabSources
#>

New-LabDefinition -Name MultiForest -DefaultVirtualizationEngine HyperV

# Two isolated subnets.
Add-LabVirtualNetworkDefinition -Name ForestA -AddressSpace 192.168.10.0/24
Add-LabVirtualNetworkDefinition -Name ForestB -AddressSpace 192.168.20.0/24

# Declare the domains explicitly — AL cannot infer topology in multi-forest labs.
Add-LabDomainDefinition -Name contoso.com  -AdminUser Install -AdminPassword 'Somepass1'
Add-LabDomainDefinition -Name fabrikam.com -AdminUser Install -AdminPassword 'Somepass1'
Set-LabInstallationCredential -Username Install -Password 'Somepass1'

$PSDefaultParameterValues = @{
    'Add-LabMachineDefinition:OperatingSystem' = 'Windows Server 2022 Datacenter'
    'Add-LabMachineDefinition:Memory'          = 1GB
}

# Forest A — customized root DC (functional level + AD site).
$rootA = Get-LabMachineRoleDefinition -Role RootDC -Properties @{
    DomainFunctionalLevel = 'WinThreshold'
    ForestFunctionalLevel = 'WinThreshold'
    SiteName              = 'Frankfurt'
    SiteSubnet            = '192.168.10.0/24'
}
Add-LabMachineDefinition -Name DCA1 -Roles $rootA -Network ForestA -IpAddress 192.168.10.10 -DomainName contoso.com
Add-LabMachineDefinition -Name FSA1 -Roles FileServer -Network ForestA -IpAddress 192.168.10.20 -DomainName contoso.com

# Forest B — default root DC.
Add-LabMachineDefinition -Name DCB1 -Roles RootDC -Network ForestB -IpAddress 192.168.20.10 -DomainName fabrikam.com

Install-Lab
Show-LabDeploymentSummary
