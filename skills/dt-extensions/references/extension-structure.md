# Extension Structure

Scraped from [Extension Structure guide](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/guides/extension_structure.html).

## Directory layout

```
my_extension
├── README.md
├── activation.json
├── extension/
│   ├── activationSchema.json
│   └── extension.yaml
├── my_extension/
│   ├── __init__.py
│   └── __main__.py
├── secrets.json
└── setup.py
```

Generate with `dt-sdk create my_extension`.

## extension.yaml

Main extension definition. Example:

```yaml
name: custom:my-extension
version: 0.0.1
minDynatraceVersion: "1.285"
author:
  name: "Dynatrace"

python:
  runtime:
    module: my_extension
    version:
      min: "3.10"
  activation:
    remote:
      path: activationSchema.json
    local:
      path: activationSchema.json
```

| Field | Notes |
|-------|-------|
| `name` | Unique; custom extensions use `custom:` namespace. Only Dynatrace uses `com.dynatrace.extension`. |
| `version` | Must bump on every upload; environment rejects duplicate versions. |
| `minDynatraceVersion` | Minimum ActiveGate/OneAgent version; extension won't activate below this. |
| `python.runtime.module` | Importable Python package name (needs `__init__.py`). |
| `python.runtime.version.min` | Mandatory; actual interpreter comes from host (3.10 or 3.14). |
| `python.activation.local` | Runs on OneAgent. |
| `python.activation.remote` | Runs on ActiveGate. |

Custom Python runtime is **not supported** — ActiveGate/OneAgent supply the interpreter.

Other EF2 datasources (snmp, jmx, prometheus, sql, wmi) use the same `extension.yaml`
format but cannot mix with Python in one extension.

## activationSchema.json

Settings 2.0 schema describing monitoring configuration UI and validation.
Defines field types, lists, passwords, allowed scopes, etc.

Minimal remote example:

```json
{
  "types": {
    "pythonRemote": {
      "type": "object",
      "properties": {
        "host": {
          "displayName": "Host",
          "type": "text",
          "nullable": false,
          "default": ""
        }
      }
    }
  },
  "dynatrace": "1",
  "description": "Extension configuration",
  "schemaId": "python-extension.activation",
  "displayName": "Extension configuration",
  "allowedScopes": ["environment"],
  "multiObject": false,
  "properties": {
    "pythonRemote": {
      "displayName": "Python Remote Extension",
      "type": { "$ref": "#/types/pythonRemote" }
    }
  }
}
```

## activation.json

Local dev config for `dt-sdk run`. Must satisfy mandatory fields from schema.
Supports `{{secretKey}}` placeholders resolved from `secrets.json`.

```json
{
  "enabled": true,
  "description": "my_extension activation",
  "version": "0.0.1",
  "activationContext": "REMOTE",
  "pythonRemote": {
    "endpoints": [
      {
        "url": "http://127.0.0.1:15672",
        "user": "guest",
        "password": "{{myPassword}}"
      }
    ]
  }
}
```

In production, Dynatrace provides per-instance activation config when monitoring
configuration is created.

## secrets.json

Key-value secrets for local testing (gitignored by default):

```json
{ "myPassword": "secretPassword" }
```

Only string secrets supported. Reference as `{{myPassword}}` in activation.json.

## setup.py

```python
from setuptools import setup, find_packages

setup(
    name="my_extension",
    version="0.0.1",
    description="My_extension python EF2 extension",
    author="Dynatrace",
    packages=find_packages(),
    python_requires=">=3.10",
    include_package_data=True,
    install_requires=["dt-extensions-sdk"],
    extras_require={"dev": ["dt-extensions-sdk[cli]"]},
)
```

- `install_requires` — runtime deps bundled into extension (keep total zip ≤ 15 MB).
- `dt-extensions-sdk` must always be listed.
- Version must match `extension.yaml`.
