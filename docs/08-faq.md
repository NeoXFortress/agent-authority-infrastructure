# FAQ

## What is Agent Authority Infrastructure?

Agent Authority Infrastructure is the runtime authority, approval, and tamper-evident evidence layer for AI agents.

## How is AAI different from guardrails?

Guardrails filter model inputs and outputs. AAI governs the actions an agent attempts to take after the model produces output.

## How is AAI different from a SIEM?

A SIEM aggregates and correlates logs. AAI produces signed, action-level evidence that a SIEM can ingest.

## How does AAI relate to NIST AI RMF?

AAI can support AI RMF-aligned governance and risk narratives by producing runtime evidence for authority, approval, monitoring, and accountability.

## Does AAI replace RMF or ATO review?

No. AAI does not grant an authorization or replace an Authorizing Official. It can support security-review and RMF/ATO readiness by producing better evidence.

## What does an AAI evidence pack include?

An evidence pack may include policy context, allowed actions, denied actions, escalated actions, human-review decisions, receipt verification status, and closeout summaries.

## Is AAI compatible with LangChain, AutoGen, CrewAI, and custom agents?

The framework is intended to be framework-agnostic. AAI should sit between the agent runtime and tools.

## Who needs AAI?

Teams deploying AI agents in high-trust environments where security, compliance, mission, audit, or operational reviewers need evidence of bounded action.

## Is this open source?

This repository is public framework documentation. It is not the NeoXFortress Gateway product implementation.

## Why use the phrase "authority" instead of only "authorization"?

"Authorization" often sounds like IAM, RBAC, or token validation. "Authority" is broader: mission scope, policy, tool boundary, human review, and evidence.
