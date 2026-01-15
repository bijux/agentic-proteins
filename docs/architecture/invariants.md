- Determinism: identical inputs and seeds must yield identical outputs and artifact hashes.
- State transitions: lifecycle states change only via explicit, allowed transitions.
- Artifact immutability: once written, artifact payloads are content-addressed and never mutated.
- Provider isolation: a run only invokes the explicitly selected provider(s) and records their versions.
- Failure containment: failures write explicit error artifacts without producing partial tool outputs.

Module refs: agentic_proteins.runtime, agentic_proteins.runtime.control.
