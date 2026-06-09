<#
    Example 06 — Mixed Windows + Linux lab (Hyper-V)

    A Windows root DC and a domain-joined Linux client. Linux VMs do not take AL
    roles (the roles are Windows-based) but come up domain-joined and reachable
    over WinRM/SSH.

    Notes & prerequisites:
      - Linux labs need internet access during setup so PowerShell and the
        omi-psrp-server can be downloaded — hence the Routing machine / External
        network here. Without omid the install will hit a long timeout.
      - Provide SSH keys for reliable Linux remoting (WSMAN support is spotty):
        pass -SshPublicKeyPath / -SshPrivateKeyPath.
      - Supported distros include RHEL 7+, CentOS 7+, Ubuntu 14.04+, Fedora 27+,
        SLES 12.3+. Match -OperatingSystem to an available image.
      - Add extra package groups with -RhelPackage (e.g. domain-client). List
        them with: Get-LabAvailableOperatingSystem | Select -Expand LinuxPackageGroup
#>

New-LabDefinition -Name LinuxLab -DefaultVirtualizationEngine HyperV

# External network so the Linux VM can download its remoting components.
Add-LabVirtualNetworkDefinition -Name LinNet -AddressSpace 192.168.40.0/24 `
    -HyperVProperties @{ SwitchType = 'External'; AdapterName = 'Ethernet' }

$PSDefaultParameterValues = @{
    'Add-LabMachineDefinition:DomainName' = 'contoso.com'
    'Add-LabMachineDefinition:Network'    = 'LinNet'
}

# Windows domain controller (provides DNS/DHCP the Linux box joins against).
Add-LabMachineDefinition -Name DC1 -Roles RootDC, Routing `
    -OperatingSystem 'Windows Server 2022 Datacenter' -IpAddress 192.168.40.10

# Domain-joined Linux client with the domain-client package group.
Add-LabMachineDefinition -Name LIN1 -OperatingSystem 'CentOS 7.4' -RhelPackage domain-client `
    -IpAddress 192.168.40.20 `
    -SshPublicKeyPath  "$HOME/.ssh/id_rsa.pub" `
    -SshPrivateKeyPath "$HOME/.ssh/id_rsa"

Install-Lab
Show-LabDeploymentSummary

# Run a command on the Linux VM (PowerShell must be present on the distro):
#   Invoke-LabCommand -ComputerName LIN1 -ScriptBlock { hostnamectl } -PassThru
