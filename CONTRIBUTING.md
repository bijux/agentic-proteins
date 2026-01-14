# Contributing

## Quick start

- Install dev tooling: `python -m pip install -U pip tox`
- Run tests: `tox -e py311`
- Run docs build: `tox -e docs`
- Run lint: `tox -e lint`
- Run quality gates: `tox -e quality`

## Code style

- Use Ruff formatting and linting.
- Keep modules import-safe and avoid side effects at import time.
- Prefer explicit, typed interfaces for public boundaries.

## Pull requests

- Keep changes focused and testable.
- Add or update tests for behavioral changes.
- Update docs if a public interface changes.
- Ensure CI gates are green before review.
