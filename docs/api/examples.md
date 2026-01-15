# HTTP API Examples

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Run a sequence:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/run \
  -H 'Content-Type: application/json' \
  -d '{"sequence":"ACDEFGHIKLMNPQRSTVWY"}'
```

Run a sequence from a server-side FASTA path:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/run \
  -H 'Content-Type: application/json' \
  -d '{"sequence_file":"tests/fixtures/proteins/small_enzyme.fasta"}'
```

Resume a run:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/resume \
  -H 'Content-Type: application/json' \
  -d '{"run_id":"run-123"}'
```

Inspect a candidate:

```bash
curl http://127.0.0.1:8000/api/v1/inspect/run-123-c0
```

Compare two runs:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/compare \
  -H 'Content-Type: application/json' \
  -d '{"run_id_a":"artifacts/run-123","run_id_b":"artifacts/run-456"}'
```

Error shape:

```json
{
  "type": "https://bijux-cli.dev/docs/errors/validation-error",
  "title": "Validation error",
  "status": 422,
  "detail": "Provide sequence or sequence_file.",
  "instance": "http://127.0.0.1:8000/api/v1/run"
}
```

Module refs: agentic_proteins.api, agentic_proteins.api.v1.schema.
