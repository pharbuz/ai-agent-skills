<#
    Example 05 — Domain lab in Azure

    The same definition style as Hyper-V, but deployed to Azure. AL creates a
    resource group per lab; Remove-Lab deletes it entirely.

    Prerequisites:
      - The Az PowerShell modules installed and you are signed in:
            Connect-AzAccount
      - From Linux/macOS, Azure is the ONLY supported engine.
      - Choose VM sizes with decent IOPS or deployments time out.
#>

# Sign in first (interactive) — uncomment if not already connected:
# Connect-AzAccount

New-LabDefinition -Name AzureLab -DefaultVirtualizationEngine Azure

# Creates the lab-sources RG and the per-lab RG. Pick a region close to you.
Add-LabAzureSubscription -DefaultLocationName 'West Europe'

$PSDefaultParameterValues = @{
    'Add-LabMachineDefinition:DomainName'      = 'contoso.com'
    'Add-LabMachineDefinition:OperatingSystem' = 'Windows Server 2022 Datacenter'
}

Add-LabMachineDefinition -Name DC1 -Roles RootDC -AzureProperties @{ RoleSize = 'Standard_D2s_v5' }
Add-LabMachineDefinition -Name MS1 -AzureProperties @{
    RoleSize               = 'Standard_D2s_v5'
    AutoshutdownTime       = '19:00'
    AutoshutdownTimezoneId = 'W. Europe Standard Time'
}

Install-Lab
Show-LabDeploymentSummary

# Connection cmdlets work transparently against the Azure load balancer:
#   Invoke-LabCommand -ComputerName DC1 -ScriptBlock { Get-ADDomain } -PassThru
# Remove-Lab -Name AzureLab -Confirm:$false   # deletes the whole resource group
