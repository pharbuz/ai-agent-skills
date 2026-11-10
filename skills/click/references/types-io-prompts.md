# Types, files, I/O, prompts, and output

## Parameter types

Built-in types include `str`, `int`, `float`, `bool`, `click.UUID`,
`click.DateTime`, `click.Choice`, `click.IntRange`, `click.FloatRange`,
`click.File`, and `click.Path`. `Choice` preserves the original choice value;
use `case_sensitive=False` for case-insensitive matching. Ranges can be
open-ended or clamped.

For reusable conversion, subclass `click.ParamType` and implement `convert`.
Raise `self.fail(message, param, ctx)` for a parameter-aware error. Implement
`shell_complete` on custom types when values can be completed.

```python
class HexInt(click.ParamType):
    name = "hex-int"

    def convert(self, value, param, ctx):
        try:
            return int(value, 0)
        except ValueError:
            self.fail("expected an integer such as 0xff", param, ctx)
```

For one-off conversion, a callable that raises `ValueError` works, but a
`ParamType` is clearer and supports help and completion.

## Files and paths

Use `click.File("rb")`/`click.File("w")` for streams. `"-"` means stdin when
reading and stdout when writing. Use `click.Path` when the callback should
receive a path and needs `exists`, `file_okay`, `dir_okay`, `readable`,
`writable`, `executable`, `resolve_path`, or `path_type`.

Writing is lazy by default, which avoids truncating a file before the command
can fail. Use `atomic=True` when readers must never observe a partial output.
When manually opening prompted files, close them with a context manager.

## Input

```python
value = click.prompt("Port", type=click.IntRange(1, 65535), default=8080)
confirmed = click.confirm("Continue?", default=False)
click.confirm("Delete?", abort=True)
```

For options, `prompt=True` prompts only when no value is supplied.
`prompt_required=False` prompts only when the flag is present. Avoid combining
automatic prompts with `multiple=True`; prompt interactively in the callback.
Use `hide_input=True` for secrets and `confirmation_prompt=True` when needed.
Callable defaults allow a dynamic value while retaining prompting.

## Output and terminal helpers

- `click.echo(message, err=True, nl=False)` for robust text/bytes output.
- `click.style` and `click.secho` for ANSI styles; colors are stripped when
  output is not a terminal unless explicitly forced.
- `click.echo_via_pager` or `click.get_pager_file` for long output.
- `click.getchar`, `click.pause`, and `click.clear` for terminal interaction.
- `click.format_filename` for safely displaying undecodable paths.

Do not require color, a TTY, a particular locale, or terminal width. Keep
machine-readable output separate from human-oriented styling.
