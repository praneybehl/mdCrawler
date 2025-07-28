Skip to main content
`Auto Plan Mode` is a defensive system prompt technique that automatically forces Claude into `Plan Mode` before executing potentially destructive operations. Instead of manually activating planning, Claude automatically presents plans whenever attempting file edits, command execution, or other risky actions.
### How to Use It​
Start Claude Code with a custom system prompt that enforces automatic planning behavior:
```
# Save the system prompt to a file for reusabilityecho "CRITICAL WORKFLOW REQUIREMENT   MANDATORY PLANNING STEP: Before executing ANY tool (Read, Write, Edit, Bash, Grep, Glob,  WebSearch, etc.), you MUST:  1. FIRST: Use exit_plan_mode tool to present your plan  2. WAIT: For explicit user approval before proceeding  3. ONLY THEN: Execute the planned actions  ZERO EXCEPTIONS: This applies to EVERY INDIVIDUAL USER REQUEST involving tool usage, regardless of:  - Complexity (simple or complex)  - Tool type (file operations, searches, web requests, etc.)  - User urgency or apparent simplicity  - Whether you previously got approval in this conversation  CRITICAL: APPROVAL DOES NOT CARRY OVER BETWEEN USER INSTRUCTIONS  - Each new user message requiring tools = new planning step required  - Previous approvals are invalid for new requests  - You must reset and plan for each individual user instruction  ENFORCEMENT: If you execute ANY tool without first using exit_plan_mode for the current  user instruction, you have violated this requirement. Always plan first, execute second.  WORKFLOW FOR EACH USER REQUEST: Plan → User Approval → Execute (NEVER: Execute → Plan)" > auto-plan-mode.txt# Use the system prompt with Claude Codeclaude --append-system-prompt "$(cat auto-plan-mode.txt)"
```

**Direct Usage** : You can also paste the system prompt directly with `claude --append-system-prompt "[paste prompt]"`.
### Why Use It​
`Auto Plan Mode` eliminates the mental overhead of remembering to activate `Plan Mode` while providing safety and educational value. It automatically handles the decision of when planning is needed, making it particularly valuable for new Claude Code users.
**Benefits:**
  * **Automatic Safety** - No unwanted edits without approval, even when you forget to activate `Plan Mode`
  * **Educational Insights** - See exactly which operations Claude considers risky and how he approaches tasks
  * **Reduced Mental Load** - No need to evaluate whether each task warrants planning
  * **Consistent Protection** - Works across all session types and task complexity levels
  * **Learning Tool** - Understand Claude's decision-making patterns and task decomposition


I use `Auto Plan Mode` when working in unfamiliar codebases or when trying new techniques where I want to understand Claude's approach before allowing execution.
##### Defensive Planning Automation
`Auto Plan Mode` provides automatic safety through enforced planning workflow. Perfect for new users and unfamiliar codebases where manual planning activation might be forgotten.
![Custom image](https://www.claudelog.com/img/discovery/042_japan.png)
**See Also** : Plan Mode|System Prompt Guide
  * How to Use It
  * Why Use It


