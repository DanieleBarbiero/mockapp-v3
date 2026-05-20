# AGENTS.md

## Project purpose

This repository contains a small mock Python application used to verify that VS Code, Codex, GitHub, and the local Python environment behave consistently.

## Python version

Use Python 3.12.

The project requires:

```text
>=3.12,<3.13
````

<!-- aggiunta mia -->

## Python interpreter enforcement

Before running any command that invokes Python, pip, pytest, or project tooling that depends on Python, inspect `.codex/config.toml`.

Read the configured project interpreter from the variable `PROJECT_PYTHON` under `[shell_environment_policy.set]`.

Use that interpreter as the only valid Python executable for this project.

If the user asks to run a command containing `python`, `pip`, `pytest`, or another Python entry point, rewrite the command so it uses the configured interpreter from `.codex/config.toml`.

Examples:

```powershell
# User asks:
python --version

# Run instead:
.\.venv\Scripts\python.exe --version
```

```powershell
# User asks:
python -m pytest

# Run instead:
.\.venv\Scripts\python.exe -m pytest
```

```powershell
# User asks:
pip install -e ".[dev]"

# Run instead:
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

Do not use the global `python` executable unless `.codex/config.toml` explicitly points to it.

Before modifying code or running tests, ensure the project is installed with:

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

After any code change, run tests with:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

When reporting command results, mention which interpreter was used.

<!-- fine aggiunta -->

## Repository layout

Use the `src/` layout:

```text
mockapp-vscode-codex/
  pyproject.toml
  src/
    mockapp/
      __init__.py
      __main__.py
      main.py
  tests/
    test_smoke.py
```

The Python package is `mockapp`.

`src` is not a Python package and must not be imported as one.

## Import rules

Use absolute imports from the top-level package:

```python
from mockapp.main import greet
```

Do not use imports such as:

```python
from src.mockapp.main import greet
import main
```

## Setup command

From the repository root:

```bash
python -m pip install -e ".[dev]"
```

## Test command

From the repository root:

```bash
python -m pytest
```

## Run command

From the repository root:

```bash
python -m mockapp
```

## VS Code rules

VS Code should use the project virtual environment:

```text
.venv
```

Do not rely on custom `PYTHONPATH` settings to make imports work.

Imports must work because the package is installed in editable mode.

## Codex rules

Before running tests or modifying code, make sure the project has been installed with:

```bash
python -m pip install -e ".[dev]"
```

After any code change, run:

```bash
python -m pytest
```

Show the diff and the test result.