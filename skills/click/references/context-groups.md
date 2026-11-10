# Contexts, groups, and complex applications

## Passing shared state

Each invocation creates a linked `Context`. Store application state in
`ctx.obj`, not module globals:

```python
@click.group()
@click.option("--config", type=click.Path(exists=True))
@click.pass_context
def cli(ctx: click.Context, config: str | None) -> None:
    ctx.ensure_object(dict)
    ctx.obj["config"] = config

@cli.command()
@click.pass_obj
def show(config: dict[str, str | None]) -> None:
    click.echo(config["config"] or "default")
```

Use `@click.pass_context` when the callback needs context metadata or methods;
`@click.pass_obj` when it only needs the stored object. For nested extensions
that replace `ctx.obj`, use `make_pass_decorator(AppState, ensure=True)` and
`ctx.find_object(AppState)` to find the nearest matching state.

Useful context features:

- `ctx.params`: parsed values for the current command.
- `ctx.parent`: the parent context.
- `ctx.invoked_subcommand`: selected child when known.
- `ctx.default_map`: configuration defaults.
- `ctx.get_parameter_source(name)`: command line, env, prompt, or default.
- `ctx.call_on_close()` / `ctx.with_resource()`: deterministic cleanup.
- `ctx.exit(code)` / `ctx.abort()`: intentional termination.
- `ctx.invoke(command, **kwargs)` / `ctx.forward(command)`: compose commands.

Do not mutate `ctx.params` to smuggle application state. Prefer a state object
or a wrapper returned by a callback; direct mutation bypasses normal conversion
and parameter-source tracking.

## Group behavior

By default a group with no command shows help and exits. Set
`invoke_without_command=True` when the group callback must always run; inspect
`ctx.invoked_subcommand` to distinguish the two cases.

For a group, use:

- `chain=True` to parse a sequence of subcommands.
- `result_callback` to consume all chain results as one pipeline.
- `no_args_is_help=False` when no-command invocation should be an error.
- `context_settings` to pass parser settings consistently.

Avoid invoking one command from another unless composition is the goal. If it
is necessary, prefer `ctx.invoke` (explicit arguments) or `ctx.forward`
(current command's arguments).

## Lazy and plugin commands

For large CLIs, subclass `click.Group` and override `list_commands` and
`get_command` to discover or import commands lazily. Validate names and import
errors explicitly, sort listing output, and keep `get_command` cheap. Use
`cls=CustomGroup` with decorators so the same behavior is used by normal and
programmatic construction.

For a small multi-module project, define commands in their own modules and
attach them with `cli.add_command`. Do not defer complexity until startup
performance or plugin isolation requires it.
