# Decision Gate

The Decision Gate enforces the Policy Engine result before tool execution.

The gate should be external to the model recommendation path. A model may suggest an action. The Decision Gate determines whether the action is allowed to execute.

Outcomes:

- Allow and proceed
- Deny and block
- Hold for human review

The Decision Gate is the action boundary.
