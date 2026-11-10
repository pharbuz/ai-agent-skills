---
name: click
description: Build, test, document, package, and extend Python command-line interfaces with Click. Use when creating Click commands, groups, options, arguments, prompts, custom parameter types, shell completion, CLI tests, entry points, or advanced Click integrations.
---

# Click

Use Click to create composable, testable Python CLIs with declarative decorators,
typed parameters, consistent help, and predictable error handling. Prefer the
public API and keep command callbacks focused on application behavior.

## When to use

- Add or change a `click.command`, `click.group`, option, argument, prompt, or
  parameter type.
- Build nested commands, shared context/configuration, plugins, aliases, or
  shell completion.
- Test CLI behavior with `CliRunner`, package a command as an executable, or
  diagnose parsing, output, exit-code, or terminal problems.

## Core workflow

1. **Inspect the project.** Identify its Python version, packaging backend,
   existing CLI entry points, test runner, and Click version. Preserve local
   conventions.
2. **Model the interface.** Use options for named configuration and arguments
   for required positional input. Define `type`, `default`, `required`,
   `nargs`, `multiple`, `envvar`, and help text deliberately.
3. **Implement the smallest command graph.** Start with `@click.command()`;
   use `@click.group()` and `@group.command()` for subcommands. Keep business
   logic in ordinary functions or services where practical.
4. **Make input and output robust.** Use `click.echo`/`secho`, `click.prompt`
   or `confirm`, `click.File`/`Path`, and Click exceptions instead of ad-hoc
   terminal handling. See [types, I/O, and prompts](references/types-io-prompts.md).
5. **Thread shared state explicitly.** Use `Context`, `pass_context`,
   `pass_obj`, `make_pass_decorator`, `ctx.ensure_object`, and
   `ctx.with_resource` as appropriate. Do not rely on global mutable state.
6. **Expose the command through packaging.** Prefer `[project.scripts]` in
   `pyproject.toml`; invoke the installed executable when testing completion.
7. **Test observable behavior.** Use `CliRunner.invoke`, assert exit code,
   output, exceptions, files, prompts, environment variables, and help. Do not
   run `CliRunner` invocations concurrently in threads.
8. **Validate the shipped interface.** Run the project's formatter, type checker,
   linter, and focused tests, then check `--help`, invalid input, and a real
   installed entry point.

## Design rules

- Treat command names, option names, parameter order, defaults, and exit codes
  as public API. Change them intentionally and document breaking changes.
- Keep callbacks deterministic and side effects explicit. Use a callback for
  parameter-local conversion/validation; raise `click.BadParameter` for an
  invalid value.
- Prefer `Choice`, `IntRange`/`FloatRange`, `Path`, `File`, and custom
  `ParamType` over manual parsing.
- Put group options before the subcommand and subcommand options after it.
  Use `chain=True` and `result_callback` only when a command pipeline is
  genuinely required.
- Use `--flag/--no-flag` for booleans, `count=True` for verbosity, and avoid
  `multiple=True` with automatic prompts.
- Handle expected user errors with `ClickException`, `UsageError`,
  `BadParameter`, or `FileError`; let unexpected programming errors surface.
- Preserve Unicode and stream behavior with Click's output helpers. Do not
  assume a TTY, terminal width, locale, or color support.

## Quick pattern

```python
import click

@click.group()
@click.option("--verbose", "-v", count=True)
@click.pass_context
def cli(ctx: click.Context, verbose: int) -> None:
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose

@cli.command()
@click.argument("name")
@click.option("--count", type=click.IntRange(1), default=1, show_default=True)
@click.pass_obj
def greet(obj: dict[str, int], name: str, count: int) -> None:
    for _ in range(count):
        click.echo(f"Hello {name}!")

if __name__ == "__main__":
    cli()
```

## References

- [Commands, options, and arguments](references/commands-options.md)
- [Contexts, groups, and complex applications](references/context-groups.md)
- [Types, files, I/O, prompts, and output](references/types-io-prompts.md)
- [Testing, packaging, help, and completion](references/testing-packaging.md)
- [Advanced patterns, errors, and extensions](references/advanced-errors-extensions.md)
- [Complete public API guide](references/api-reference.md)
- [Documentation coverage map](references/documentation-map.md)

Use the [official Click documentation](https://click.palletsprojects.com/en/stable/)
for exhaustive API signatures and version-specific details. The bundled
references are a practical guide, not a replacement for the API reference.
