# Building Extensions

Scraped from [Building Extensions guide](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/guides/building.html).

## Native dependencies

Some packages (e.g. `requests` → `charset_normalizer`) ship platform-specific
wheels compiled for specific Python versions and OS.

Extensions run on ActiveGate or OneAgent (Linux or Windows) with Python **3.10**
or **3.14**. Wheels in `extension/lib/` must match those targets.

`dt-sdk build` downloads wheels into `extension/lib/`. Use flags for cross-build:

### From Windows (add Linux wheels)

```bash
dt-sdk build --extra-platform manylinux2014_x86_64
```

`manylinux2014_x86_64` works for many packages but not all — verify per dependency.

### From Linux (add Windows wheels)

```bash
dt-sdk build --extra-platform win_amd64
```

### Multiple Python versions

```bash
dt-sdk build --python-version 3.10 --python-version 3.14
```

### macOS ARM64

```bash
dt-sdk build --only-extra-platforms --extra-platform manylinux2014_x86_64
```

Builds wheels only for specified extra platforms (not native arm64).

## PyPI access

### Mirror

```bash
PIP_INDEX_URL=http://my-pypi-server:8080/simple \
PIP_TRUSTED_HOST=my-pypi-server \
dt-sdk build
```

PowerShell:

```powershell
$ENV:PIP_INDEX_URL="http://my-pypi-server:8080/simple"
$ENV:PIP_TRUSTED_HOST="my-pypi-server"
dt-sdk build
```

All pip environment variables work (SDK wraps pip).

### Local wheel directory

```bash
dt-sdk build --find-links /path/to/whl/files
```

Combine with `--no-index` to use only local wheels.

## Musl vs libc

Extensions run on **libc** systems (Ubuntu, CentOS, Windows).

**Do not build on musl** (Alpine). Alpine downloads musl-linked wheels incompatible
with production hosts.

Use `python:3.14` or other libc-based Docker images for CI builds.

## Size limit

Total extension zip must be **≤ 15 MB**. Cross-platform native deps increase size
quickly — audit `install_requires` and wheel count.

## Supported Python

Dynatrace supports 3.10 and 3.14. Python 3.10 support is being phased out;
prefer 3.14 for new extensions.
