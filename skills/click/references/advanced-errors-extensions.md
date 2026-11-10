# Advanced patterns, errors, and extensions

## Callbacks and eager parameters

Callbacks run after type conversion for command-line, environment, prompt, and
default values. Return the possibly transformed value or raise
`click.BadParameter`. For early actions such as `--version`, use
`is_eager=True`, `expose_value=False`, and check `ctx.resilient_parsing` before
calling `ctx.exit()`.

Do not use callbacks for unrelated business logic. Keep validation local to the
parameter and test callback behavior from every input source.

## Error and exit behavior

Expected user errors should be explicit:

```python
raise click.ClickException("Could not connect")
raise click.UsageError("Choose exactly one mode", ctx)
raise click.BadParameter("must be positive", param_hint="--count")
```

Standalone `Command.main()` displays `ClickException`, handles aborts and
interrupts, and exits. For embedding or tests, use
`command.main(args, standalone_mode=False)` to receive return values and
propagate exceptions. `--help` normally exits 0; usage errors normally exit 2;
abort/interrupt normally exits 1.

Use `click.Abort`/`ctx.abort()` for an intentional abort. Do not catch broad
exceptions and turn programming failures into successful output.

## Token normalization and custom parsing

Set `token_normalize_func` in `context_settings` to normalize option, choice,
and command tokens. Use `allow_extra_args` and `ignore_unknown_options` only
when forwarding arguments to another parser; document the changed interface.
Use `resilient_parsing` only for non-destructive inspection such as completion.

## Extending Click

Subclass `click.Group`, `click.Command`, or `click.ParamType` when a reusable
behavior cannot be expressed with decorators. Override the narrowest public
method, preserve help and error semantics, and add focused tests. Common
extension points on groups are `list_commands` and `get_command`; use them for
aliases, lazy loading, or plugins.

For a new shell, subclass `ShellComplete` and register it with
`add_completion_class`; study the built-in implementations and test both
source generation and completion output.

## Interoperability

`click.command`, `click.group`, and `Command` can be called programmatically.
Use `make_context` and `with ctx` when manual invocation must manage context
and cleanup. `Command.invoke` bypasses `main`'s exception handling; use it only
when that behavior is intended.
