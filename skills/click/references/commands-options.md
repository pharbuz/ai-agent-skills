# Commands, options, and arguments

## Command graph

```python
@click.command("hello")
def hello() -> None:
    """Print a greeting."""
    click.echo("Hello")

@click.group()
def cli() -> None:
    """Application entry point."""

@cli.command()
@click.option("--count", type=int, default=1, show_default=True)
@click.argument("name")
def greet(count: int, name: str) -> None:
    for _ in range(count):
        click.echo(f"Hello {name}")
```

Function names become command names with underscores converted to dashes. Pass
an explicit name to `command` or `group` to override it. Register detached
commands with `group.add_command(command)`. Groups can be nested arbitrarily.

Group parameters belong to the group; child parameters belong to the child.
Therefore invoke `tool --debug sync --dry-run`, not `tool sync --debug`.

## Options

Use `@click.option` for named values. Common controls:

| Need | Pattern |
| --- | --- |
| required value | `required=True` |
| default | `default=value`, optionally `show_default=True` |
| conversion | `type=int`, `type=click.Choice(...)` |
| fixed tuple | `type=(str, int)` or `nargs=2` |
| repeated values | `multiple=True` (callback receives a tuple) |
| boolean | `is_flag=True` or `--flag/--no-flag` |
| verbosity | `count=True` (`-vvv` -> `3`) |
| environment | `envvar="NAME"` or a list of names |
| prompt | `prompt=True` or a custom prompt string |
| hidden implementation detail | `expose_value=False`, `hidden=True` |
| early exit | `is_eager=True`, usually with a callback |

Click infers a type from recognized defaults when `type` is omitted. Do not
depend on inference for a public interface: specify the type when ambiguity
would be surprising.

`flag_value` implements feature switches, but paired boolean flags are clearer
for ordinary on/off configuration. A callable default can compute a value at
invocation time; use `show_default` to describe it.

## Arguments

Use `@click.argument` for positional values:

```python
@click.command()
@click.argument("source", type=click.Path(exists=True, dir_okay=False))
@click.argument("targets", nargs=-1)
def copy(source: str, targets: tuple[str, ...]) -> None:
    ...
```

Arguments support `nargs`, `required`, `type`, `envvar`, and `default`.
Use an option instead when the value is configuration rather than the primary
object of the command.

## Environment and precedence

Values can come from the command line, prompt, environment, or default. Use
`ctx.get_parameter_source(name)` when behavior depends on where a value came
from. `auto_envvar_prefix` derives environment names; `default_map` supplies
configuration defaults. Make precedence visible in help and tests.

## Help

Use function docstrings, `help=`, `short_help=`, `epilog=`, `metavar=`,
`show_envvar=True`, and `context_settings={"help_option_names": ["-h", "--help"]}`.
Keep help actionable and avoid hiding important defaults. Use `no_args_is_help`
or `invoke_without_command` intentionally for groups.
