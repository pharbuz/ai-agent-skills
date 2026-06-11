---
name: dt-extensions
description: >-
  Build, test, package, and ship Python Extensions 2.0 for Dynatrace using
  dt-extensions-sdk (dt-sdk CLI). Trigger WHENEVER the user works on a Python EF2
  extension, imports from dynatrace_extension, subclasses Extension, runs dt-sdk
  create/build/run/upload/gencerts, edits extension.yaml or activationSchema.json,
  reports metrics/events via report_metric/report_dt_event, schedules query()
  callbacks, signs extension zips, or migrates EF1 Python extensions to EF2.
  Covers extension structure, activation config, CLI workflow, Extension API,
  cross-platform builds, certificates, and EF1→EF2 migration.
---

# dt-extensions — Python Extensions 2.0 SDK

`dt-extensions-sdk` is the Python library and CLI (`dt-sdk`) for building
**Extensions Framework 2.0** Python extensions. Install as `dt-extensions-sdk`,
import runtime from `dynatrace_extension`.

```bash
pip install dt-extensions-sdk[cli]   # adds dt-sdk CLI
python -m venv .venv && source .venv/bin/activate
pip install dt-extensions-sdk        # per-extension venv (recommended)
```

Requirements: **Python 3.10 or 3.14**. `[cli]` adds typer, pyyaml, dt-cli;
only `dt-extensions-sdk` core is bundled into the built extension zip.

## Mental model

1. **Scaffold** — `dt-sdk create my_extension` → project with `extension.yaml`,
   `activationSchema.json`, Python module, `setup.py`.
2. **Implement** — subclass `dynatrace_extension.Extension` in `__main__.py`;
   override `query()` (default every 60s) and/or `initialize()` + `schedule()`.
3. **Test locally** — `dt-sdk run` with `activation.json` + `secrets.json`.
4. **Build & sign** — `dt-sdk gencerts` (once), then `dt-sdk build` → signed
   zip in `dist/`.
5. **Upload** — `dt-sdk upload` with tenant URL + API token.

Extensions run on **OneAgent** (`local` activation) or **ActiveGate**
(`remote` activation). Python interpreter is supplied by the host — no BYO Python.

## Extension skeleton

```
my_extension/
├── activation.json          # local dev config
├── extension/
│   ├── activationSchema.json
│   └── extension.yaml       # name, version, python runtime, activation paths
├── my_extension/
│   ├── __init__.py
│   └── __main__.py          # ExtensionImpl class
├── secrets.json             # {{placeholders}} for activation.json (gitignored)
└── setup.py                 # install_requires must include dt-extensions-sdk
```

Key rules:

- `extension.yaml` `name` must use `custom:` namespace (e.g. `custom:my-extension`).
- Bump `version` in **both** `extension.yaml` and `setup.py` before each upload.
- Extension zip must stay **≤ 15 MB**.
- `minDynatraceVersion` gates activation on older agents.

Full file-by-file reference → [`references/extension-structure.md`](references/extension-structure.md).

## Minimal ExtensionImpl

```python
from datetime import timedelta
from dynatrace_extension import Extension, MetricType

class ExtensionImpl(Extension):
    def initialize(self):
        config = self.get_activation_config()
        # schedule extra callbacks beyond default query()
        self.schedule(self.my_method, timedelta(minutes=5))

    def query(self):
        self.report_metric(
            "my_metric", 1,
            dimensions={"my_dimension": "dimension1"},
            metric_type=MetricType.GAUGE,
        )

    def my_method(self):
        endpoints = self.get_activation_config().get("pythonRemote", {}).get("endpoints", [])
        for ep in endpoints:
            dims = self.get_tags_and_fields_dimensions(ep)
            self.report_metric("endpoint.status", 1, dimensions=dims)

    def on_shutdown(self):
        pass  # runs before metrics flush on SIGINT/shutdown
```

`query()` is auto-scheduled every **60 seconds**. Use `initialize()` to read
activation config and call `self.schedule(callback, interval)` for other intervals.
Intervals accept `timedelta` or seconds (`int`).

## Reporting data

| Goal | Method |
|------|--------|
| Gauge/counter metric | `self.report_metric(key, value, dimensions={}, metric_type=MetricType.GAUGE)` |
| Raw MINT lines | `self.report_mint_lines(["my_metric 1"])` |
| Log-ingest event | `self.report_event(title, description, severity=Severity.INFO)` |
| Events v2 / problems | `self.report_dt_event(DtEventType.CUSTOM_ALERT, title, entity_selector=...)` |
| Custom logs | `self.report_log_event({...})` / `self.report_log_lines([...])` |

Activation config: `self.get_activation_config()` (replaces EF1 `self.config`).
Endpoint dimensions: `get_fields_dimensions`, `get_tags_dimensions`,
`get_tags_and_fields_dimensions`.

API detail → [`references/api-extension.md`](references/api-extension.md);
`Severity` → [`references/api-events-severity.md`](references/api-events-severity.md);
`DtEventType` → [`references/api-events-type.md`](references/api-events-type.md);
`Metric` / `MetricType` → [`references/api-metrics-metric.md`](references/api-metrics-metric.md),
[`references/api-metrics-type.md`](references/api-metrics-type.md).

## CLI workflow

```bash
dt-sdk create my_extension          # scaffold
cd my_extension
dt-sdk run                          # local test (activation.json + secrets.json)
dt-sdk run --fastcheck              # remote fastcheck mode
dt-sdk run --local-ingest           # also send metrics to localhost:14499

dt-sdk gencerts                     # CA + developer PEM → ~/.dynatrace/certificates/
dt-sdk build                        # wheel → assemble → sign → dist/custom_*.zip
dt-sdk build --extra-platform manylinux2014_x86_64   # from Windows, add Linux wheels
dt-sdk build --python-version 3.10 --python-version 3.14

dt-sdk upload -u https://<env>.live.dynatrace.com -t $DT_API_TOKEN
# or env vars: tenant URL + API token with extension upload permission
```

Low-level commands (`wheel`, `assemble`, `sign`) are invoked by `build`.
Full flags and offline PyPI options → [`references/cli-commands.md`](references/cli-commands.md).

## Cross-platform builds

Extensions run on **Linux or Windows** ActiveGate/OneAgent with Python 3.10/3.14.

| Build host | Add wheels for |
|------------|----------------|
| Windows | `--extra-platform manylinux2014_x86_64` |
| Linux | `--extra-platform win_amd64` |
| macOS ARM | `--only-extra-platforms` (build only for extra platforms) |

Native deps (e.g. `charset_normalizer`) need platform-matched wheels. Use
`--find-links /path/to/whl` or `PIP_INDEX_URL` for offline/mirror builds.
**Do not build on musl/Alpine** — use libc-based images (`python:3.14`, Ubuntu).

Detail → [`references/building.md`](references/building.md).

## EF1 → EF2 migration

| EF1 | EF2 |
|-----|-----|
| `self.config.get(...)` | `self.get_activation_config().get(...)` |
| `device.absolute("key", val, dims)` | `self.report_metric("key", val, dims)` |
| `self.results_builder.report_custom_info_event` | `self.report_dt_event(...)` |
| `topology_builder.create_group` / `create_device` | Define topology in `extension.yaml` |

Use VS Code **Dynatrace Extensions** add-on: `Convert Python` imports
`plugin.json` → `activationSchema.json`. Remove `activation.remote` or
`activation.local` in `extension.yaml` if extension is local-only or remote-only.

Full migration steps → [`references/migration.md`](references/migration.md).

## Common pitfalls

- **Version mismatch** — `extension.yaml` and `setup.py` versions must match and
  increment on every upload.
- **15 MB limit** — trim dependencies; cross-platform wheels add size fast.
- **Wrong platform wheels** — always pass `--extra-platform` when cross-building.
- **Alpine/musl CI** — produces incompatible native wheels; use Debian/Ubuntu.
- **Topology in code** — EF2 defines groups/devices in `extension.yaml`, not Python.
- **Secrets in git** — keep `secrets.json` gitignored; use `{{key}}` in activation.

## Reference files

All pages from [official docs](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/)
are in `references/`:

| File | Covers |
|------|--------|
| `quick-start.md` | End-to-end workflow |
| `installation.md` | Requirements, PyPI, venv |
| `extension-structure.md` | extension.yaml, activationSchema, setup.py |
| `building.md` | Cross-platform builds, PyPI mirror |
| `migration.md` | EF1→EF2 migration |
| `cli-commands.md` | All 9 CLI commands (`--help` output) |
| `api-extension.md` | Full `Extension` class API |
| `api-events-severity.md` | `Severity` enum |
| `api-events-type.md` | `DtEventType` enum |
| `api-metrics-metric.md` | `Metric` class |
| `api-metrics-type.md` | `MetricType` enum |
