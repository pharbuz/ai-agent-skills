<#
    Example 01 — Single Windows Server (Hyper-V)

    The smallest possible lab: one server, no domain, automatic networking and IP.
    AL creates a virtual switch and picks a free subnet for you.

    Prerequisites:
      - A Windows Server ISO in LabSources\ISOs whose name matches the
        -OperatingSystem string below. Verify with:
            Get-LabAvailableOperatingSystem -Path C:\LabSources
      - Elevated PowerShell, Hyper-V enabled.
#>

New-LabDefinition -Name SingleServer -DefaultVirtualizationEngine HyperV

Add-LabMachineDefinition -Name SRV1 -OperatingSystem 'Windows Server 2022 Datacenter (Desktop Experience)' -Memory 2GB

Install-Lab
Show-LabDeploymentSummary

# Try it out:
#   Invoke-LabCommand -ComputerName SRV1 -ScriptBlock { $env:COMPUTERNAME } -PassThru
# Tear down when finished:
#   Remove-Lab -Name SingleServer -Confirm:$false
