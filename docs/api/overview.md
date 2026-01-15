# HTTP API Overview

The HTTP API is a thin wrapper over the CLI/runtime. It exposes the same capabilities as the CLI, nothing more.

Scope:

- Provides synchronous endpoints for run, resume, inspect, and compare.
- Returns the same JSON payloads as the CLI `--json` output.
- Uses the same runtime entrypoints and artifacts on disk.
- Resolves relative file paths against the server base directory.

Non-goals (v1):

- No streaming responses.
- No authentication/authorization.
- No async background jobs.
- Not a second execution engine.

Stability policy:

- Versioned under `/api/v1`.
- Payloads match CLI JSON contracts (not additional guarantees).
- Backwards-incompatible changes require a new API version.

Deferred (explicitly out of scope):

- Auth and multi-tenant runs.
- Async job queue and worker pool.
- Streaming logs or event feeds.

Module refs: agentic_proteins.api, agentic_proteins.interfaces.cli.
