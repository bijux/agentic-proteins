# Threat Model

## Abuse cases
- Path traversal via candidate IDs to read/write outside the candidate store.
- Crafted sequence inputs to bypass validation and inject unsupported characters.
- Unauthorized resume requests to force execution of stale or unapproved runs.

## Resource exhaustion risks
- Large batch runs exhausting local disk through artifact growth.
- Oversized sequences driving unbounded memory usage in planning and tooling.
- High-frequency API requests saturating CPU and log I/O.

## Trust assumptions
- Local filesystem permissions prevent cross-tenant artifact access.
- Provider backends return deterministic results for the same inputs and seed.
- CI artifacts and version metadata are not tampered with between steps.
