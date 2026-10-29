# zizo
Personal assistant setup.


# NOTES

## 5 core pieces of every agent (the roots)
- Model (the brain) decides what to do next.
- Agent loop: think → call a tool → see the result → repeat until done. The loop stops when it reaches a final result, an error, a cancellation or a timeout. This loop is the heart of every agent (only about 50 lines of code)
- Tools are functions the agent can call: read a file, run tests, git push. In 2026 they’re typed functions with Pydantic or JSON schemas, and the agent fills in the arguments while your code validates them before running anything.
- Context: what you put in front of the model each turn (instructions, memory, files, history). Good context matters more than a smarter model.
- Memory: what survives between sessions. Clawdbot for example uses two layers, JSONL logs of every message and tool call plus markdown files holding summarized long-term knowledge. That’s the same idea as zizos brain.


## The other possible branches after the roots
- MCP: the standard way to plug tools and data into any agent. It’s the connection layer that defines how an agent reaches a database, an API or a file system.
- Skills: reusable know-how packaged as a folder containing a SKILL.md file, loaded only when needed.
- Gateway / channels: reaching your agent from WhatsApp, Telegram or your phone. In Clawdbot for example, one long-running Gateway owns the messaging surfaces and coordinates the agent’s work.
- Sub-agents: a main agent delegating tasks to helper agents.
- Guardrails: permissions, sandboxing and human approval before risky actions.
- Evals and observability: logs, cost tracking and tests to check the agent actually works.
- Scheduling: the agent doing things on its own on a timer.


## Possible vs. not possible

- Possible: reading and editing your code, running tests, committing, pushing to GitHub and opening pull requests, remembering you across projects, running on a schedule, and working from your phone.

- Limitations: it makes confident mistakes, drifts on long tasks, can run up costs in loops, can be tricked by malicious text in files or web pages (prompt injection), and has no real taste or judgment about what’s worth building.

## Auto-pushing to GitHub

Very doable, using either a git push tool or the GitHub MCP server. The safe pattern is:
- zizo pushes to a branch and opens a pull request.
- I review and merge to main.
- Give it a GitHub token limited to the repos I choose. Never give it main account password.

This keeps it fast and I´ll still be in charge.
