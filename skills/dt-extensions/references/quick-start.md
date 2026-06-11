# Quick Start

Source: https://dynatrace-extensions.github.io/dt-extensions-python-sdk/

End-to-end workflow from zero to uploaded extension.

## 1. Install

```bash
pip install dt-extensions-sdk[cli]
```

See [`installation.md`](installation.md).

## 2. Create extension

```bash
dt-sdk create my_extension
cd my_extension
```

Generated structure — see [`extension-structure.md`](extension-structure.md).

## 3. Run locally

```bash
dt-sdk run
```

Sample output:

```
Running: .venv/dt-extensions-sdk/bin/python -m my_extension --activationconfig activation.json
[INFO] api (MainThread): Starting <class '__main__.ExtensionImpl'> my_extension, version: 1.1.0
[INFO] dynatrace_extension.sdk.extension: query method started for my_extension.
[INFO] dynatrace_extension.sdk.extension: query method ended for my_extension.
```

Default template reports one metric in `query()`:

```python
self.report_metric("my_metric", 1, dimensions={"my_dimension": "dimension1"})
```

On `Ctrl+C`, metrics flush to EEC plus self-monitoring (`dsfm:datasource.python.*`).

### Custom scheduling

```python
from datetime import timedelta

def initialize(self):
    self.schedule(self.my_method, timedelta(minutes=5))
```

`query()` always runs every 60 seconds regardless.

## 4. Generate certificates

```bash
dt-sdk gencerts
```

Creates CA + developer PEM in `~/.dynatrace/certificates/`. Upload certificate
to environment and OneAgent/ActiveGate hosts.

Cert docs: https://docs.dynatrace.com/docs/extend-dynatrace/extensions20/sign-extension

Skip if you already have certificates uploaded.

## 5. Build

```bash
dt-sdk build
```

Stages:
1. Download dependencies → `extension/lib/`
2. Build wheel
3. Assemble unsigned zip
4. Sign with developer certificate → `dist/custom_my-extension-0.0.1.zip`

Cross-platform: see [`building.md`](building.md).

## 6. Upload

```bash
dt-sdk upload -u https://<tenant>.live.dynatrace.com -t $DT_API_TOKEN
```

Requires API token with extension upload permission.

Then in tenant: **Infrastructure Observability → Extensions → Add monitoring configuration**.
