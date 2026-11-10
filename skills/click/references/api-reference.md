# Click API reference

Use this file as a decision guide for the public API documented at
[`click.palletsprojects.com/en/stable/api/`](https://click.palletsprojects.com/en/stable/api/).
Prefer decorators and utilities for application code. Instantiate or subclass
core classes when building reusable frameworks, plugin loaders, or custom
parsers. Signatures can vary by Click version; consult the installed version's
API page before exposing a low-level class.

## Decorators

| API | Use |
| --- | --- |
| `command(name=None, **attrs)` | Turn a callback into `Command`; callback receives parsed parameters as keyword arguments. |
| `group(name=None, **attrs)` | Turn a callback into `Group`; use `@cli.command()` and `@cli.group()` for children. |
| `argument(*param_decls, **attrs)` | Declare positional input; support `nargs`, `required`, `type`, `envvar`, and `default`. |
| `option(*param_decls, **attrs)` | Declare named input; support flags, defaults, prompts, env vars, callbacks, and types. |
| `password_option(...)` | Shortcut for a hidden-input option with a confirmation prompt. |
| `confirmation_option(...)` | Add a boolean confirmation flag that aborts when not accepted. |
| `version_option(version=None, ...)` | Add an eager `--version` option and exit after printing the version. |
| `custom_version_option(...)` | Build a version option with a custom callback/parameter class. |
| `help_option(param_decls=None, ...)` | Build or customize the eager help option. |
| `pass_context(f)` | Inject the current `Context` as the first callback argument. |
| `pass_obj(f)` | Inject `ctx.obj` as the first callback argument. |
| `make_pass_decorator(object_type, ensure=False)` | Create a decorator that finds or creates a typed object in the context chain. |
| `pass_meta_key(key, ...)` | Inject a value from `Context.meta`; use for framework metadata. |

Decorator order matters: Click applies decorators bottom-up. Put
`@click.pass_context` or `@click.pass_obj` closest to the function, and put
parameter decorators above it. `Group.command` and `Group.group` are the
equivalent registration methods when the parent is already defined.

## Command classes

### `Command`

Use `Command` directly for programmatic construction or subclass it for
custom invocation/help/parsing. Important constructor attributes include
`name`, `context_settings`, `callback`, `params`, `help`, `epilog`,
`short_help`, `options_metavar`, `add_help_option`, `no_args_is_help`,
`hidden`, `deprecated`, and `context_settings`.

| Method | Purpose |
| --- | --- |
| `make_context(info_name, args, parent=None, **extra)` | Create and configure a `Context` without invoking the command. |
| `parse_args(ctx, args)` | Parse arguments and return leftovers; override only for a custom parser. |
| `invoke(ctx)` | Execute callback in an existing context; exception handling is not `main`'s responsibility. |
| `main(args=None, prog_name=None, complete_var=None, standalone_mode=True, **extra)` | Public entry point; parse, invoke, handle Click exceptions, and normally exit. |
| `get_params(ctx)` | Return parameters used for parsing/help. |
| `get_help(ctx)` / `format_help(ctx, formatter)` | Render or customize help. |
| `get_usage(ctx)` / `format_usage(ctx, formatter)` | Render or customize usage. |
| `get_short_help_str(limit=45)` | Create group listing text. |
| `shell_complete(ctx, incomplete)` | Return completion items for this command. |
| `__call__(...)` | Alias for `main`; useful as a console-script target. |

Prefer `main` for normal execution and `CliRunner.invoke` in tests. Use
`standalone_mode=False` when embedding a command and you need return values or
exceptions instead of `SystemExit`.

### `Group`

`Group` extends `Command` with child command management.

| Method | Purpose |
| --- | --- |
| `add_command(cmd, name=None)` | Register a command, optionally under another name. |
| `command(name=None, **attrs)` | Decorator that creates and registers a child `Command`. |
| `group(name=None, **attrs)` | Decorator that creates and registers a child `Group`. |
| `result_callback(replace=False)` | Decorate a callback that receives child results, especially for `chain=True`. |
| `get_command(ctx, cmd_name)` | Resolve a child; override for aliases or lazy loading. |
| `list_commands(ctx)` | Return child names; override for dynamic/plugin commands. |
| `resolve_command(ctx, args)` | Resolve command name and remaining args; customize only with parser expertise. |

Use `CommandCollection` to expose commands from multiple groups without
nesting them. `MultiCommand` and `BaseCommand` are compatibility aliases
deprecated for removal; use `Group` and `Command` instead.

## Parameters

### `Parameter`

Base class for `Option` and `Argument`. Constructor controls `param_decls`,
`type`, `required`, `default`, `callback`, `nargs`, `multiple`, `envvar`,
` expose_value`, `is_eager`, and `shell_complete`.

| Method | Purpose |
| --- | --- |
| `get_default(ctx, call=True)` | Resolve the default, calling a callable when requested. |
| `consume_value(ctx, opts)` | Select the value and its source from parser/env/default. |
| `process_value(ctx, value)` | Validate missing values, convert with `type`, then call callback. |
| `type_cast_value(ctx, value)` | Apply the parameter type, `nargs`, and `multiple` conversion. |
| `resolve_envvar_value(ctx)` / `value_from_envvar(ctx)` | Resolve and split environment values. |
| `handle_parse_result(ctx, opts, args)` | Integrate parsing, processing, and callback result. |
| `get_help_record(ctx)` / `get_usage_pieces(ctx)` | Produce help and usage fragments. |
| `shell_complete(ctx, incomplete)` | Produce parameter completion items. |

### `Option`

Use `Option` for named values and flags. Important attributes include
`is_flag`, `flag_value`, `count`, `prompt`, `confirmation_prompt`,
`hide_input`, `prompt_required`, `show_default`, `show_envvar`,
`allow_from_autoenv`, `help`, `metavar`, `multiple`, `nargs`, `expose_value`, and
`secondary_opts` for paired flags.

Methods used by custom option implementations include `get_default`,
`add_to_parser`, `get_help_record`, `get_help_extra`, `prompt_for_value`,
`resolve_envvar_value`, `value_from_envvar`, `consume_value`, and
`process_value`. Override only when a custom `Option` is truly reusable.

### `Argument`

Use `Argument` for positional values. It supports `nargs`, `required`,
`default`, `type`, `envvar`, and `metavar`; it does not support option-only
features such as prompts or flags. Its customization points mirror parameter
help/usage and conversion methods.

## `Context` and global state

`Context` stores invocation state, parsed parameters, parent links, cleanup
callbacks, `obj`, `meta`, `default_map`, and `protected_args`.

| Method/property | Purpose |
| --- | --- |
| `scope(cleanup=True)` | Temporarily make a context current; supports nested/manual invocation. |
| `with_resource(cm)` | Enter a context manager and close it with the context. |
| `call_on_close(f)` / `close()` | Register and run cleanup callbacks. |
| `find_root()` / `find_object(type)` / `ensure_object(type)` | Navigate or initialize shared typed state. |
| `lookup_default(name, call=True)` | Resolve a default from `default_map`. |
| `get_usage()` / `get_help()` | Render current command help. |
| `invoke(command, *args, **kwargs)` | Invoke another command with explicit values. |
| `forward(command, *args, **kwargs)` | Invoke another command using current parameters. |
| `exit(code=0)` / `abort()` / `fail(message)` | End with a deliberate result or usage error. |
| `set_parameter_source(name, source)` / `get_parameter_source(name)` | Track or inspect `ParameterSource`. |

`get_current_context(silent=False)` accesses the active context. Prefer
explicit `pass_context`/`pass_obj`; use globals only for utilities that truly
need ambient invocation state. `ParameterSource` values are
`COMMANDLINE`, `ENVIRONMENT`, `DEFAULT`, `DEFAULT_MAP`, `PROMPT`, and
`None` when no source is known.

## Parameter types

| Type | Use and key methods |
| --- | --- |
| `STRING`, `INT`, `FLOAT`, `BOOL`, `UUID`, `UNPROCESSED` | Built-in singleton types; use as `type=` or rely on explicit inference. |
| `ParamType` | Base for conversion; implement `convert`, optionally `get_metavar`, `get_missing_message`, `split_envvar_value`, `shell_complete`, and use `fail`. |
| `Choice(choices, case_sensitive=True, max_args=None)` | Validate enumerated values; use `normalize_choice`, `convert`, `get_invalid_choice_message`, and `shell_complete`. |
| `DateTime(formats=None)` | Parse one or more datetime formats. |
| `IntRange(min=None, max=None, min_open=False, max_open=False, clamp=False)` | Parse bounded integers; optionally clamp closed bounds. |
| `FloatRange(...)` | Parse bounded floats; clamp only when both bounds are closed. |
| `File(mode="r", encoding=None, errors="strict", lazy=None, atomic=False)` | Open stdin/stdout or files, including `-`; use `resolve_lazy_flag` and `convert`. |
| `Path(...)` | Validate file-system paths (`exists`, `file_okay`, `dir_okay`, permissions, `resolve_path`, `path_type`). |
| `Tuple(types)` | Convert fixed-arity values with a different type per position. |

For custom types, `convert(value, param, ctx)` must return the application
value or call `fail`. Implement `shell_complete` when completion is meaningful.

## Utilities

### Terminal UI

| API | Use |
| --- | --- |
| `echo(message=None, file=None, nl=True, err=False, color=None)` | Robust Unicode/text/bytes output. |
| `style(text, fg=None, bg=None, bold=False, dim=False, underline=False, ...)` | Build ANSI-styled text. |
| `secho(message, **style_kwargs)` | `style` then `echo`. |
| `echo_via_pager(text_or_generator, color=None)` / `get_pager_file(...)` | Send long output through the configured pager. |
| `prompt(text, default=None, hide_input=False, confirmation_prompt=False, type=None, ...)` | Typed interactive input. |
| `confirm(text, default=False, abort=False, ...)` | Boolean confirmation; abort when `abort=True`. |
| `progressbar(iterable=None, length=None, label=None, show_eta=True, show_percent=True, ...)` | Display progress while iterating. |
| `clear()` | Clear the terminal screen. |
| `edit(text=None, editor=None, envvar=None, require_save=True, extension=None)` | Open an editor and return edited text. |
| `launch(url, wait=False, locate=False)` | Open a URL or file with the platform handler. |
| `getchar(echo=False)` / `pause(info=None, err=False)` | Read one terminal character or pause. |

### `progressbar`

Use it as an iterator or context manager. The returned progress-bar object
supports `update(n_steps, current_item=None)`, `finish()`, `render_progress()`,
`make_step(n_steps)`, `generator()`, `__enter__`, and `__exit__`. These are
instance methods on the object returned by `progressbar`; do not import the
private implementation class directly. Do not mix `length`, `iterable`, and
manual updates incorrectly.

```python
with click.progressbar(items, label="Downloading") as bar:
    for item in bar:
        download(item)

with click.progressbar(length=total, label="Working") as bar:
    for chunk in chunks:
        process(chunk)
        bar.update(1)
```

### Files, streams, and application directories

| API | Use |
| --- | --- |
| `open_file(filename, mode="r", encoding=None, errors="strict", lazy=None, atomic=False)` | Open a path or `-` with Click's stream/atomic semantics. |
| `get_binary_stream(name)` / `get_text_stream(name)` | Obtain robust stdin/stdout/stderr streams (deprecated in favor of newer internals; verify version). |
| `get_app_dir(app_name, roaming=True, force_posix=False)` | Return a platform-appropriate per-user application directory. |
| `format_filename(filename, shorten=False)` | Safely render paths containing undecodable bytes. |

### Formatting

`HelpFormatter` builds sections, rows, definitions, usage, and epilog text.
Use `formatter.section(name)`, `write_usage`, `write_heading`,
`write_dl`, `write_paragraph`, and `write_text` in custom help rendering.
Use `wrap_text(text, width=78, initial_indent="", subsequent_indent="",
preserve_paragraphs=False)` for Click-compatible wrapping. Prefer command
metadata over direct formatter use.

## Exceptions

| Exception | Use |
| --- | --- |
| `ClickException(message, exit_code=1)` | Expected application error; `show()` writes it. |
| `UsageError(message, ctx=None)` | Invalid command usage. |
| `BadParameter(message, ctx=None, param=None, param_hint=None)` | Invalid value; includes parameter context. |
| `MissingParameter(...)` | Required parameter missing. |
| `FileError(name, message)` | File opening/handling failure. |
| `NoSuchOption`, `NoSuchCommand` | Unknown command-line token. |
| `BadOptionUsage`, `BadArgumentUsage` | Option/argument syntax misuse. |
| `Abort` | Intentional abort; Click renders `Aborted!`. |
| `Exit(code=0)` | Internal deliberate exit signal. |

Use `show(file=None)` and `format_message()` when rendering custom
`ClickException` subclasses. Do not catch broad exceptions and convert
unexpected defects into a successful result.

## Shell completion and testing API

`CompletionItem(value, type=None, help=None)` represents a suggestion.
Implement `ParamType.shell_complete`, parameter `shell_complete`, or a custom
`ShellComplete` subclass. Register custom shells with
`add_completion_class(name, cls)`; use `get_completion_class` to resolve one.
`split_arg_string` parses a shell-like incomplete argument string.

`CliRunner` exposes `invoke(cli, args=None, input=None, env=None, catch_exceptions=True,
color=False, **extra)`, `isolated_filesystem(temp_dir=None)`, and
`get_default_prog_name`. `Result` exposes `output`, `stdout`, `stderr`,
`return_value`, `exception`, `exc_info`, `exit_code`, and `output_bytes`.
Use temporary paths and process isolation; do not invoke runners concurrently
in threads.

## Deprecated/internal APIs

Do not build new code on `BaseCommand`, `MultiCommand`, `OptionParser`,
`get_binary_stream`, `get_text_stream`, or `click.__version__`. These are
compatibility exports in current docs and may be removed; use `Command`,
`Group`, normal parsing, robust stream helpers, and
`importlib.metadata.version("click")`/feature detection instead.
