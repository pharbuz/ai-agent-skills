# Click documentation coverage

This skill was derived from the complete stable documentation tree (38 Markdown
pages) downloaded from the Click repository. The source snapshot used while creating it is
`pallets/click` commit `8abb77a8432e03ed14a95f972b44f905279415a7` (2026-11-10).
The local source checkout was used for research; this package contains
original summaries and examples rather than a verbatim copy of the docs.

| Source page | Covered by |
| --- | --- |
| `index`, `quickstart`, `click-concepts`, `design-opinions`, `why` | `SKILL.md`, this map |
| `commands`, `commands-and-groups`, `arguments`, `parameters`, `options`, `option-decorators` | `commands-options.md` |
| `parameter-types`, `handling-files`, `prompts`, `utils`, `unicode-support`, `wincmd` | `types-io-prompts.md` |
| `advanced`, `complex`, `entry-points`, `setuptools`, `virtualenv`, `support-multiple-versions` | `context-groups.md`, `testing-packaging.md`, `advanced-errors-extensions.md` |
| `testing` | `testing-packaging.md` |
| `shell-completion` | `testing-packaging.md` |
| `exceptions`, `command-line-reference` | `advanced-errors-extensions.md`, `commands-options.md` |
| `extending-click`, `contrib` | `advanced-errors-extensions.md` |
| `api` | `api-reference.md` plus official API link below |
| `documentation` | help section in `commands-options.md`; official docs |
| `faqs` | relevant cautions in topic files; official docs |
| `standalone-apps-briefcase`, `standalone-apps-nuitka` | packaging section; official docs |
| `changes`, `upgrade-guides`, `license`, `contributing` | compatibility note and links below |

## Source links

- [Stable documentation](https://click.palletsprojects.com/en/stable/)
- [API reference](https://click.palletsprojects.com/en/stable/api/)
- [Upgrade guides](https://click.palletsprojects.com/en/stable/upgrading/)
- [FAQ](https://click.palletsprojects.com/en/stable/faqs/)
- [Click source repository](https://github.com/pallets/click)
- [Click BSD-3-Clause license](https://github.com/pallets/click/blob/main/LICENSE.txt)

When exact signatures, deprecations, version markers, or platform behavior
matter, open the relevant official page for the installed Click version rather
than trusting a condensed reference.
