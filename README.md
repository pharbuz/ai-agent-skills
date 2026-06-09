# automatedlab-skill

An AI-agent **skill** for [AutomatedLab](https://automatedlab.org/en/latest/) —
the PowerShell framework for building virtual machine labs on Hyper-V and Azure.

The skill teaches an agent (Claude Code / any skill-aware agent) how to author and
manage AutomatedLab deployments: the define → deploy → customize → manage
workflow, the core cmdlets, the role catalogue, networking, Azure, and a set of
ready-to-run example lab scripts.

## What's inside

```
automatedlab/                  ← the skill (copy this folder into your skills dir)
├── SKILL.md                   ← entry point: workflow, cheat sheet, recipes
├── references/
│   ├── install.md             ← installing AL, LabSources, host setup
│   ├── cmdlets.md             ← full cmdlet reference by phase
│   ├── roles.md               ← every role + AD / SQL / PKI tuning
│   ├── networking.md          ← subnets, internet, DMZ, Azure VNet
│   ├── customizing.md         ← Invoke-LabCommand, software, features, CredSSP
│   ├── azure.md               ← Azure and Azure Stack Hub
│   └── lab-management.md      ← import, modify, snapshots, offline, Remove-Lab
└── examples/
    ├── 01-single-server.ps1
    ├── 02-domain-sql-client.ps1
    ├── 03-multi-forest.ps1
    ├── 04-internet-and-software.ps1
    ├── 05-azure-lab.ps1
    └── 06-linux-lab.ps1
```

## Installing the skill

Copy the `automatedlab/` folder into the location your agent reads skills from,
for example:

```bash
# Global agent skills
cp -r automatedlab ~/.agents/skills/

# or a project-local skills folder
cp -r automatedlab .agents/skills/
```

The agent loads `SKILL.md` automatically and pulls in the `references/` and
`examples/` files as needed.

## How the skill is organized

It follows progressive disclosure: `SKILL.md` is the always-loaded core (the
4-phase mental model, a cmdlet cheat sheet, and a recipe for generating lab
scripts on request), and it points to the `references/` files for depth and the
`examples/` scripts for copy-and-adapt starting points.

## Source

All content is derived from the official AutomatedLab documentation at
<https://automatedlab.org/en/latest/>. AutomatedLab itself is MIT-licensed; this
skill is provided under the MIT license too (see [LICENSE](LICENSE)).
