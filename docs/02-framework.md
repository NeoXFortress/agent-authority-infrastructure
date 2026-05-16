# The Framework: Authority, Approval, Evidence

Agent Authority Infrastructure is built on three primitives: authority, approval, and evidence.

## Authority

Authority is the explicit definition of what an AI agent is allowed to do.

Authority should be expressed at the level of action, not only at the level of model output or user role. It should account for:

- Agent identity
- Mission scope
- Tool boundary
- Data boundary
- User or system context
- Conditions and constraints
- Time or duration
- Human-review requirements
- Revocation and policy update path

### Federal Example

An RMF support agent may be authorized to read approved SSP source documents, draft control narrative updates, and generate an evidence summary for reviewer inspection.

It may not be authorized to access unrelated repositories, email the package externally, edit authoritative records, or call tools outside its mission boundary.

## Approval

Approval is the runtime decision that determines whether an intended action is allowed to execute.

Approval is not a model recommendation. The model may propose an action. A separate authority layer should evaluate that action against policy and return one of three outcomes:

- Allow
- Deny
- Human review

The separation matters. If the same model that recommends an action is treated as the system that authorized it, the deployment has no independent action boundary.

### Federal Example

An agent attempts to send a compliance package to an external recipient. The policy says external transmission requires named reviewer approval. The action is held, routed to review, and released only if the reviewer approves.

## Evidence

Evidence is the signed, tamper-evident record of the approval decision.

Evidence should help reviewers reconstruct what happened and what was prevented from happening. It should describe:

- Agent identifier
- Mission identifier
- Requested action
- Target tool or resource
- Policy version
- Decision outcome
- Human reviewer context, if applicable
- Timestamp
- Verification status

Evidence is not the same as ordinary logging. Logs are useful for observability. Evidence is structured for review, verification, and accountability.

### Federal Example

At pilot closeout, an AO receives an evidence pack showing allowed actions, denied actions, escalated actions, approvals, policy versions, and verification status for the pilot period.

## Summary

The model generates a recommendation. The authority layer decides whether the action is allowed to execute. The evidence layer preserves what happened afterward.
