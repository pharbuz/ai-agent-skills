# Project Resources Content

Use this when the task is about installation, dependencies, release behavior,
license, support, or where to validate ambiguous examples.

## Downloads And Dependencies

Install the official package from PyPI:

```bash
pip install pysnmp
```

Core dependency:

- `pyasn1`: ASN.1 data model and BER codecs.

Optional capabilities:

- `pysmi`: enables MIB services, ASN.1 MIB parsing/compilation, and symbolic MIB
  workflows.
- `cryptography`: enables stronger SNMPv3 encryption support.

Use a virtual environment. Pin package versions for production pollers and
agents. Development branches can contain recent fixes but may change public
interfaces.

## Changelog Use

The changelog is included from the project change log and should be checked
before relying on recently introduced behavior. The v7.1 docs observed here
show `7.1.27` as the documented version and list many 7.1.x releases. For
migration tasks, check the changelog together with `upgrade.html` because patch
releases may alter compatibility shims, transport behavior, or command return
details.

## License

The download page states PySNMP is provided under a BSD-style license and the
license page includes the repository `LICENSE.rst`. For legal/compliance tasks,
open the actual license text from the package or repository rather than relying
on a paraphrase.

## Support Options

The docs point to PySNMP support options and LeXtudio commercial support,
especially for migration from legacy 4.x/5.x code and hard production issues.
For normal coding tasks, exhaust troubleshooting, FAQ, API reference, and tests
before escalating.

## Further Development And Reliable Sources

- Match sources to the docs branch/tag, e.g. `release-7.1`.
- If examples are stale, inspect tests in the PySNMP GitHub repository.
- If docs and installed behavior disagree, inspect installed package types and
  local source.
- Use `mibs.pysnmp.com` or local MIB directories for symbolic MIB workflows.

## Related Resource Content

- Quick Start: virtualenv setup, `pipenv install pysnmp`, basic GET, basic TRAP.
- HLAPI tutorial: SnmpEngine lifecycle, credentials, transport targets, context,
  MIB object identity, scalar/table indexing, command operations, notifications.
- API Reference: generated signatures/classes/constants.
- Examples: runnable patterns, with the documented caveat that some examples may
  be older than current best practices.
- Troubleshooting/FAQ/Performance: operational diagnosis and tuning.
