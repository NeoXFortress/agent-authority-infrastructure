# What Agent Authority Infrastructure Is Not

Clear boundaries make the category more useful.

## Not a Guardrail

Guardrails filter model inputs and outputs. AAI governs the actions that follow from model output.

A guardrail might detect unsafe generated text. AAI decides whether the agent is allowed to call a tool, access a resource, or take an external action.

## Not a Model Risk Platform

Model risk management platforms govern models across registration, validation, monitoring, and retirement.

AAI governs runtime actions. It can feed action-level evidence into model risk workflows, but it does not replace them.

## Not a SIEM

SIEMs aggregate and correlate logs.

AAI produces signed, action-level records that a SIEM can ingest. AAI is upstream of the SIEM, not a replacement for it.

## Not Red-Teaming

Red-teaming tests model behavior, failure modes, and adversarial prompts.

AAI governs whether an intended action is allowed to execute at runtime. A model can pass evaluation and still attempt an unauthorized action.

## Not an Agent Framework

Agent frameworks help teams build agents.

AAI should be framework-agnostic. It should sit between the agent runtime and tools, regardless of whether the agent uses LangChain, AutoGen, CrewAI, model-provider tool calling, or a custom runtime.

## Not an Identity Provider

Identity providers answer who the user, service, or agent is.

AAI consumes identity and answers a different question: what is this agent allowed to do right now?
