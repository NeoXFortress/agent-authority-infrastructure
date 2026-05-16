# Definition

## Canonical Definition

Agent Authority Infrastructure (AAI) is the runtime authority, approval, and tamper-evident evidence layer for AI agents.

AAI defines what an AI agent is allowed to do before execution, enforces allow / deny / human-review decisions at runtime, and preserves verifiable evidence after each action.

## Short Definition

Agent Authority Infrastructure decides what AI agents are allowed to do, enforces the decision before execution, and produces evidence afterward.

## Expanded Definition

AAI is a security and governance layer that sits between AI-agent intent and tool execution. It consumes identity, mission scope, policy, and context; evaluates whether a proposed action is authorized; routes the action to allow, deny, or human review; and records the decision as signed, tamper-evident evidence.

AAI is useful when an organization needs to answer reviewer questions such as:

- Which agent attempted the action?
- What mission or workflow was the agent operating under?
- Which tool or resource did the agent attempt to use?
- Was the action allowed, denied, or escalated?
- Which policy version governed the decision?
- Who approved the action if human review was required?
- What evidence exists after the action?

## Tagline

Authority before action. Proof after action.

In body copy, prefer "evidence" over "proof." The tagline keeps "proof" because it is memorable and plain-language.

## Audience

This framework is written for:

- Federal AI program leaders
- Authorizing Officials
- ISSOs and ISSMs
- RMF and ATO reviewers
- Federal systems integrators
- Defense and regulated AI teams
- Security architects
- GRC and audit teams
- AI platform teams deploying agents into high-trust workflows
