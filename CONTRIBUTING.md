# Contributing to LDICA Master Learning Hub

Thank you for helping improve the LDICA Master Learning Hub. Keep changes focused, testable, and relevant to the learning platform.

## Development setup

Use Python 3.12 or another version supported by the project dependencies.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

The application creates its local SQLite database under Flask's instance directory by default. It generates a local session key on first run when no valid `SECRET_KEY` is configured.

## Validate changes

Run the structural validator and test suite before opening a pull request:

```bash
python scripts/validate_project.py
python -m pytest -q
```

The GitHub Actions workflow runs the same checks for pull requests and pushes to the default development branches. If a test requires external tools or hardware simulators, document that requirement and make the test skip clearly when the tool is unavailable.

## Branch and pull-request workflow

1. Create a short, descriptive branch from `master`.
2. Make a focused change and add or update tests where behavior changes.
3. Use clear commit messages such as `fix: handle empty search queries` or `test: cover secure cookie defaults`.
4. Open a pull request explaining the problem, the change, and the validation performed.
5. Address review feedback and wait for checks before merging.

Prefer small pull requests that can be reviewed independently. Do not split one unchanged implementation into many pull requests solely to increase repository metrics.

## Configuration and secrets

- Do not commit `.env` files, credentials, tokens, database files, or local session keys.
- The repository's `.gitignore` excludes `.env` and local runtime artifacts.
- Configure deployment values through your local environment or the deployment platform's secret/configuration manager.
- Never put real secrets in documentation, examples, test fixtures, or commit messages.

## Content and simulation changes

- Keep syllabus topics aligned with the catalog and lesson bank.
- Add tests for numerical edge cases and invalid inputs when changing simulation algorithms.
- Clearly distinguish idealized educational models from physical-device guarantees.
- Do not claim that a simulation or test passed unless it was actually run.
