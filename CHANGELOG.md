# Changelog  
<a id="top"></a>  

All notable changes to **agentic-proteins** are documented here.  
This project adheres to [Semantic Versioning](https://semver.org) and the  
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.  

<a id="unreleased"></a>  
## [Unreleased]  

<!-- unreleased start -->
### Added
* (add new entries via fragments in `changelog.d/`)

### Changed
* (add here)

### Fixed
* (add here)
<!-- unreleased end -->  

  

---  

<!-- release start -->  
<a id="v0-2-0"></a>  

## [0.2.1]  

### Added  
- Expanded unit and integration coverage with new invariants, API, and docs gates.  
- Additional tests for provider isolation, reproducibility, and abuse-case blocking.  
- Fancy PyPI readme fragments for README + changelog publishing.  

### Changed  
- Refactored `tests/unit` into a structured layout for clearer ownership.  

### Fixed  
- Coverage floors and CI gates stabilized around new test layout.  

## [0.2.0]  

### Added  
- Architecture invariants, threat model skeleton, and design debt ledger.  
- Reproducible runs via `agentic-proteins reproduce <run_id>` with hash checks.  
- Determinism tests, artifact immutability tests, and invariant regression coverage.  
- Provider isolation checks and chaos failure test for mid-run provider loss.  
- Benchmark regression gate and per-module coverage floors in CI.  
- Documentation system contracts, lint gates, and CLI surface audit coverage.  
- API error taxonomy enforcement, correlation ID logging test, and OpenAPI drift guard.  
- Dependency allowlist enforcement for SBOM changes.  

<a id="v0-1-0"></a>  

## [0.1.0]  

### Added
- Deterministic, artifact-first execution engine with explicit run directories and state snapshots.
- Agent-based architecture covering planning, analysis, execution, verification, and reporting.
- End-to-end design loop with failure handling, stagnation detection, and human-in-the-loop gating.
- CLI for running, resuming, inspecting, comparing, and exporting protein design runs.
- Local and remote provider abstractions with explicit capability and requirement checks.
- Structured reporting system with machine-readable artifacts and human-readable summaries.
- Integrated evaluation pipeline supporting structure-based metrics and ground-truth comparison.
- Reproducibility controls, observability hooks, and execution telemetry.
- Example datasets and reference runs for local experimentation and validation.
- Comprehensive test suite covering unit, integration, regression, and execution boundaries.
<!-- release end -->
