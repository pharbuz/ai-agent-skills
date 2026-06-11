# Migrating EF1 → EF2 Python Extensions

Scraped from [Migration guide](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/guides/migration.html).

## Requirements

- Python 3.10 or 3.14
- `dt-extensions-sdk[cli]` installed (`dt-sdk --help`)
- VS Code with **Dynatrace Extensions** add-on (recommended)

## Step-by-step (VS Code)

### 1. Create new EF2 extension

- `Dynatrace extensions: Initialize Workspace`
- Select latest schema version and signing certificates
- Project type: **Python Extension 2.0**
- Name: lowercase with underscores (Python module convention)

### 2. Import EF1 extension

`Dynatrace extensions: Convert Python` — import from:
- Extension zip file
- `plugin.json` file
- Dynatrace environment (lists all Python extensions)

This overwrites `activationSchema.json` with converted Settings 2.0 UI.
Review the schema after conversion.

**Activation context cleanup in `extension.yaml`:**
- Local (OneAgent) only → delete `activation.remote`
- Remote (ActiveGate) only → delete `activation.local`
- Both → keep both and adjust `activationSchema.json`

### 3. Move code to __main__.py

Paste EF1 extension class logic into `ExtensionImpl` in `__main__.py`.

| Description | EF1 | EF2 | Notes |
|-------------|-----|-----|-------|
| Logging | `self.logger.info(...)` | same | unchanged |
| User params | `self.config.get("x", default)` | `self.get_activation_config().get("x", default)` | find/replace `self.config.` |
| Events | `self.results_builder.report_custom_info_event` | `self.report_dt_event(...)` | topology in `extension.yaml`, not code |
| Metrics | `device.absolute("key", val, dims)` | `self.report_metric("key", val, dims)` | no `device` object in Python |
| Topology | `topology_builder.create_group`, `group.create_device` | n/a | define in `extension.yaml` |

### 4. Build and upload

- `Dynatrace extensions: Build`
- Upload and activate when prompted
- In tenant: **Infrastructure Observability → Extensions → Add monitoring configuration**
- Copy JSON snippet `value` into `activation.json` for local `dt-sdk run` testing

## Limitations

- **Process snapshot** not yet supported in EF2 SDK. Workaround: read/parse
  `/dynatrace/oneagent/plugin/oneagent_latest_snapshot.log` as JSON.
- **Metric metadata and topology** must be added to `extension.yaml` manually
  (partial automation planned).

## CLI-only migration path

Without VS Code:

```bash
dt-sdk create my_ext
# manually convert plugin.json → activationSchema.json (or use VS Code convert once)
# port __main__.py from EF1 class
dt-sdk run    # test with activation.json
dt-sdk build && dt-sdk upload
```
