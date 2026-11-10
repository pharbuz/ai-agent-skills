# Testing, packaging, help, and completion

## Testing

`click.testing.CliRunner` invokes commands in-process and returns a `Result`.
Assert `exit_code`, `output`, `exception`, and side effects:

```python
from click.testing import CliRunner

def test_greet():
    result = CliRunner().invoke(cli, ["greet", "Ada", "--count", "2"])
    assert result.exit_code == 0
    assert result.output == "Hello Ada!\nHello Ada!\n"
```

Pass `input=` for prompts, `env=` for environment variables,
`terminal_width=` for wrapping, and `color=True` or context settings when
testing ANSI output. Use `tmp_path` plus absolute paths for file tests.

`CliRunner` changes process-global streams and environment for simplicity and
is not thread-safe. Run CLI cases in separate processes for parallel tests.
The isolated-filesystem helper is deprecated in recent Click versions; prefer
pytest's `tmp_path`. Test both successful and failing invocations, including
invalid types, missing files, help, aborts, and expected exit codes.

## Packaging

Prefer an installable package and a `pyproject.toml` entry point:

```toml
[project.scripts]
my-tool = "my_package.cli:cli"
```

Declare Click in `[project.dependencies]`, install with `python -m pip install
-e .`, and run the generated executable. This supports platform-specific
wrappers and is required for normal completion behavior. Keep the import path
free of expensive side effects.

## Shell completion

Click supports Bash 4.4+, Zsh, Fish, and PowerShell for installed entry
points. For an executable `foo-bar`, Click uses `_FOO_BAR_COMPLETE`:

```console
_FOO_BAR_COMPLETE=bash_source foo-bar > ~/.foo-bar-complete.bash
source ~/.foo-bar-complete.bash
```

Use the matching `zsh_source`, `fish_source`, or `powershell_source` value for
other shells. For custom values, provide `shell_complete(ctx, param,
incomplete)` on a parameter or `ParamType`; return strings or
`click.shell_completion.CompletionItem` objects.

Completion should be cheap, deterministic, and free of destructive side
effects. Test completion through the installed executable and the supported
shell's conventions.

## Documentation and compatibility

Use docstrings and option metadata to generate useful help. For applications
supporting multiple Click versions, use feature detection instead of version
string comparisons and consult the upgrade guide before relying on changed
behavior.
