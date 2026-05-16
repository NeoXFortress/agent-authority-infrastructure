# Reference Architecture

Agent Authority Infrastructure can be represented as a five-layer stack.

## Layer 1: User / Mission

The starting point is the mission context. This includes the human, program, system, or workflow that tasks the agent and defines what the agent is supposed to accomplish.

## Layer 2: Agent Runtime

The agent runtime includes the model, orchestration framework, reasoning loop, prompts, tools interface, and framework-specific execution context.

Examples include LangChain, AutoGen, CrewAI, model-provider tool-calling flows, and custom runtimes.

## Layer 3: Agent Authority Layer

The Agent Authority Layer is where AAI lives.

Core components:

- Agent Registry
- Policy Engine
- Decision Gate
- Human Review Path
- Receipt Generator

This layer evaluates agent intent before tool execution and produces evidence after each decision.

## Layer 4: Tools / Actions

The tools and actions layer contains the APIs, databases, filesystems, message queues, external services, and operational systems that the agent may attempt to use.

## Layer 5: Evidence & Audit Plane

The evidence and audit plane contains signed action receipts, hash-chained ledger entries, evidence packs, and exports for SIEM, GRC, RMF, audit, and closeout review.

## Architecture Diagram

![Agent Authority Infrastructure reference architecture](../architecture/reference-architecture.svg)

## Design Principle

AAI should sit underneath the agent framework, beside model evaluation and red-teaming, and upstream of SIEM, GRC, RMF, and audit systems.

It should not replace those systems. It should produce evidence those systems can consume.
