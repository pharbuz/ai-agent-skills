# ai-agent-skills

A collection of [agent skills](https://skills.sh) — reusable instruction sets
that extend AI coding agents (Claude Code, Codex, Cursor, OpenCode, and
[many more](https://skills.sh)). Each skill is a directory with a `SKILL.md`
file; this repo bundles several so they can be installed and shared from one
place via the [`skills`](https://github.com/vercel-labs/skills) CLI / skills.sh.

## Skills in this repo

| Skill | What it does |
|-------|--------------|
| [`aiocache`](skills/aiocache/) | Build, configure, debug, test, or migrate async Python caching with `aiocache` — backends, serializers, decorators, locks, plugins, testing, and migration |
| [`aiodns`](skills/aiodns/) | Build, debug, migrate, or test asynchronous DNS resolution with `aiodns` — resolvers, query APIs, timeouts, nameservers, records, and pycares integration |
| [`async-upnp-client`](skills/async-upnp-client/) | Build, debug, or refactor asyncio UPnP, SSDP, DLNA, IGD, printer, and eventing code with `async_upnp_client` |
| [`automatedlab`](skills/automatedlab/) | Build & manage Hyper-V/Azure VM labs with the AutomatedLab PowerShell framework |
| [`dt-async`](skills/dt-async/) | Call the Dynatrace REST API asynchronously in Python with the `dt-async` client (`import dynatrace`) — auth, services, pagination, DQL/Grail, integration |
| [`dt-extensions`](skills/dt-extensions/) | Build, test, package, and ship Dynatrace Extensions 2.0 with `dt-extensions-sdk` and the `dt-sdk` CLI |
| [`dynatrace-dql`](skills/dynatrace-dql/) | Write and optimize Dynatrace Query Language (DQL) queries against Grail — commands, functions, operators, best practices, domain examples |
| [`dynatrace-dpl`](skills/dynatrace-dpl/) | Write Dynatrace Pattern Language (DPL) patterns for parsing logs and Grail data — matchers, modifiers, grouping, DPL Architect |
| [`dynatrace-developer`](skills/dynatrace-developer/) | Build Dynatrace apps with the Strato design system — components, design tokens, charts, and patterns |
| [`dtrum`](skills/dtrum/) | Manually instrument Dynatrace RUM in the browser with the `dtrum` JavaScript API — custom actions, XHR/SPA tracking, user tagging, error reporting, consent & session replay |
| [`embla-carousel-react`](skills/embla-carousel-react/) | Build, configure, debug, or refactor React carousels with `embla-carousel-react` — hooks, options, plugins, events, and controls |
| [`fastapi-filters`](skills/fastapi-filters/) | Add filtering & sorting to FastAPI with `fastapi-filters` — `FilterSet`/`FilterField[T]`, type-driven operators (`?age[gt]=30`), `create_sorting`, and `ext` integrations (SQLAlchemy, Tortoise, Beanie) via `apply_filters_and_sorting` |
| [`fastapi-keycloak`](skills/fastapi-keycloak/) | Integrate Keycloak OIDC with FastAPI via `fastapi-keycloak` — `FastAPIKeycloak`, `get_current_user` / role guards, password & authorization_code flows, token refresh, and Admin API for users/roles/groups |
| [`fastapi-pagination`](skills/fastapi-pagination/) | Add pagination to FastAPI with `fastapi-pagination` — `Page`/`LimitOffsetPage`/`CursorPage`, `paginate`/`add_pagination`, ext integrations (SQLAlchemy, SQLModel, Tortoise, Beanie, Motor…), item transformers, and `CustomizedPage` customization |
| [`hvac`](skills/hvac/) | Talk to HashiCorp Vault from Python with the `hvac` client (`import hvac`) — client setup, auth methods, secrets engines, system backend, and error handling |
| [`keycloak-themes`](skills/keycloak-themes/) | Create, customize, and deploy Keycloak themes for login, account, admin, email, and welcome pages |
| [`next-themes`](skills/next-themes/) | Add, configure, debug, or refactor theme switching with `next-themes` in React and Next.js apps |
| [`opensearch-py`](skills/opensearch-py/) | Build, debug, test, or migrate Python code using the official OpenSearch client package `opensearch-py` (`import opensearchpy`) |
| [`pyroute2`](skills/pyroute2/) | Build, debug, or refactor Python Linux networking code with `pyroute2` — netlink, routes, links, namespaces, NDB, IPRoute, and WireGuard |
| [`pysnmp`](skills/pysnmp/) | Build, configure, debug, or migrate Python SNMP code with PySNMP v7.1 — managers, agents, notifications, transports, MIBs, and async HLAPI |
| [`python-stubs`](skills/python-stubs/) | Write, review, generate, test, or package Python type stubs (`.pyi`) — typeshed patterns, stubgen, stubtest, py.typed, overloads, and packaging |
| [`python-zeroconf`](skills/python-zeroconf/) | Build, debug, or refactor Python multicast DNS / DNS-SD service discovery code with `zeroconf` |
| [`react-datepicker`](skills/react-datepicker/) | Build date and time pickers with `react-datepicker` — controlled `<DatePicker />` usage, ranges, time selection, constraints, locales, `timeZone`, serialization pitfalls, and customization hooks like `renderCustomHeader` and `customInput` |
| [`react-sigma`](skills/react-sigma/) | Build, configure, debug, or refactor React graph visualizations with `@react-sigma/*` — Sigma containers, events, search, minimap, and layouts |
| [`scapy`](skills/scapy/) | Build, debug, or extend packet crafting, sniffing, routing, dissectors, and protocol tooling with Scapy |
| [`xyflow-react`](skills/xyflow-react/) | Build node-based UIs with React Flow v12 (`@xyflow/react`) — full reactflow.dev API reference: `<ReactFlow />` props, built-in components, hooks, types (`Node`/`Edge`/`ReactFlowInstance`), path utils, plus custom node/edge examples |

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
