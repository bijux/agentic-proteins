# Agents Subsystem

Decision logic by agent:

Planner

- Inputs: goal and constraints from PlannerAgentInput.
- Allowed decisions: emit a PlanDecision with tasks, dependencies, and rationale.
- Forbidden: tool execution, runtime state changes.
- Trusted signals: input goal and constraints only.

InputValidation

- Inputs: sequence and sequence_id from InputValidationAgentInput.
- Allowed decisions: valid flag, warnings, and errors.
- Forbidden: tool execution and candidate mutation.
- Trusted signals: sequence format and validation rules.

QualityControl

- Inputs: candidate and evaluation bundle from QualityControlAgentInput.
- Allowed decisions: QCStatus and constraint_violations.
- Forbidden: tool execution or plan changes.
- Trusted signals: candidate metrics and evaluation observations.

Critic

- Inputs: critic_name, target_agent_name, qc_output, observations, tool_reliability.
- Allowed decisions: blocking flag and inconsistencies.
- Forbidden: tool execution and persistent memory writes.
- Trusted signals: QC output and tool reliability summary.

FailureAnalysis

- Inputs: failure_type and related context from FailureAnalysisAgentInput.
- Allowed decisions: failure classification and replan recommendation.
- Forbidden: tool execution.
- Trusted signals: failure type and run metadata.

Coordinator

- Inputs: prior decisions, QC output, critic output, loop state and limits.
- Allowed decisions: continue, replan, or terminate with reason codes.
- Forbidden: tool execution.
- Trusted signals: QC status, critic output, loop state.

Reporting

- Inputs: tool outputs and QC status from ReportingAgentInput.
- Allowed decisions: summary payload and confidence statement.
- Forbidden: tool execution and state updates.
- Trusted signals: tool outputs and QC status.

Module refs: agentic_proteins.agents, agentic_proteins.agents.schemas, agentic_proteins.validation.agents.
