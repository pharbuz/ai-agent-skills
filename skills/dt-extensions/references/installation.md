# Installation

Source: https://dynatrace-extensions.github.io/dt-extensions-python-sdk/guides/installation.html

## Requirements

`dt-extensions-sdk` requires:

- **Python 3.10 or 3.14**

## Installing from PyPI

Install system-wide or as project dependency:

```bash
pip install dt-extensions-sdk[cli]
```

Once installed, `dt-sdk` binary is available in `PATH`.

### Core vs CLI package

Installing `dt-extensions-sdk[cli]` adds optional dependencies required for CLI
tools: `typer[all]`, `pyyaml`, `dt-cli`.

When the extension is **built**, only the core `dt-extensions-sdk` package is
bundled into the extension zip — CLI extras are ignored.

If you omit `[cli]`, only the core runtime package is installed (sufficient for
ActiveGate/OneAgent execution, but no `dt-sdk` commands).

## Virtual environment (recommended)

One venv per extension project:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install dt-extensions-sdk[cli]
```

Keeps dependencies isolated between extensions.

## Quick install summary

| Goal | Command |
|------|---------|
| Full dev toolchain | `pip install dt-extensions-sdk[cli]` |
| Runtime only (in setup.py) | `install_requires=["dt-extensions-sdk"]` |
| Dev extras in setup.py | `extras_require={"dev": ["dt-extensions-sdk[cli]"]}` |
