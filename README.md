# ai-agent-skills

A collection of [agent skills](https://skills.sh) — reusable instruction sets
that extend AI coding agents (Claude Code, Codex, Cursor, OpenCode, and
[many more](https://skills.sh)). Each skill is a directory with a `SKILL.md`
file; this repo bundles several so they can be installed and shared from one
place via the [`skills`](https://github.com/vercel-labs/skills) CLI / skills.sh.

## Skills in this repo

| Skill | What it does |
|-------|--------------|
| [`automatedlab`](skills/automatedlab/) | Build & manage Hyper-V/Azure VM labs with the AutomatedLab PowerShell framework |
| [`dynatrace-developer`](skills/dynatrace-developer/) | Build Dynatrace apps with the Strato design system — components, design tokens, charts, and patterns |
| [`dt-async`](skills/dt-async/) | Call the Dynatrace REST API asynchronously in Python with the `dt-async` client (`import dynatrace`) — auth, services, pagination, DQL/Grail, integration |
| [`dynatrace-dql`](skills/dynatrace-dql/) | Write and optimize Dynatrace Query Language (DQL) queries against Grail — commands, functions, operators, best practices, domain examples |
| [`dynatrace-dpl`](skills/dynatrace-dpl/) | Write Dynatrace Pattern Language (DPL) patterns for parsing logs and Grail data — matchers, modifiers, grouping, DPL Architect |
| [`dtrum`](skills/dtrum/) | Manually instrument Dynatrace RUM in the browser with the `dtrum` JavaScript API — custom actions, XHR/SPA tracking, user tagging, error reporting, consent & session replay |

## Install

Replace `<owner>` with your GitHub account (the repo's `owner/name` is the
install path on skills.sh).

```bash
# Install all skills from this repo (pick your agent when prompted)
npx skills add <owner>/ai-agent-skills

# List what's inside without installing
npx skills add <owner>/ai-agent-skills --list

# Install a single skill, globally, for Claude Code
npx skills add <owner>/ai-agent-skills --skill dynatrace-developer -g -a claude-code
```

Use a skill once without installing it:

```bash
npx skills use <owner>/ai-agent-skills@automatedlab | claude
```

### Manual install (no CLI)

Copy a skill folder into your agent's skills directory, e.g. for Claude Code:

```bash
cp -r skills/dynatrace-developer ~/.claude/skills/    # global
# or, project-local, for agents that read .agents/skills:
cp -r skills/dynatrace-developer .agents/skills/
```

## Repository layout

skills.sh discovers every `skills/<name>/SKILL.md` automatically (the flat
layout it walks one level deep):

```
ai-agent-skills/
├── README.md
├── LICENSE
└── skills/
    ├── automatedlab/
    │   ├── SKILL.md            ← required: YAML frontmatter (name, description) + body
    │   ├── references/         ← deep-dive docs loaded on demand
    │   └── examples/           ← copy-and-adapt scripts
    └── dynatrace-developer/
        ├── SKILL.md
        └── references/
```

## Adding a new skill

1. Scaffold a folder under `skills/`:
   ```bash
   npx skills init skills/my-new-skill      # or create skills/my-new-skill/SKILL.md by hand
   ```
2. Give `SKILL.md` YAML frontmatter with a unique `name` and a `description`
   that says **what it does and when to trigger** (the description is the main
   thing that makes an agent reach for the skill).
3. Keep `SKILL.md` lean (< ~500 lines) and push depth into `references/`.
4. Commit. Once the repo is on GitHub, it's installable via the commands above.

## Publishing to skills.sh

skills.sh indexes public GitHub repos that contain `SKILL.md` files. Push this
repo to GitHub and it's installable immediately with
`npx skills add <owner>/ai-agent-skills`. The directory listing on
<https://skills.sh> is sourced from GitHub — see the
[skills CLI docs](https://github.com/vercel-labs/skills) for details and the
`metadata.internal: true` frontmatter flag to keep a work-in-progress skill
hidden from discovery.

## License

[MIT](LICENSE). Skill content is distilled from each tool's official
documentation (AutomatedLab — <https://automatedlab.org>; Dynatrace Developer /
Strato — <https://developer.dynatrace.com>); those projects retain their own
licenses and trademarks.
