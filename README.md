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

## OpenClaw/Clawdbot vs own build 

### OpenClaw/Clawdbot

- Pros
Works today: phone chat, memory, skills, and many integrations already built.
Large community and ecosystem.
Saves you weeks or months of building.

- Cons
You learn to configure an agent, not to build one.
A weak portfolio signal, since many people run it.
A large codebase you don’t fully understand, so it’s hard to trust and fix.
A real security history: many CVEs and malicious community plugins.
It’s general-purpose, while you want something shaped around how you work.
Building your own

### Own build 

- Pros
You deeply understand every agent concept, which is exactly the AI-engineer skill set.
A strong, unique portfolio piece you can explain line by line in interviews.
Small, so you control and trust it, with security designed in from the start.
Shaped exactly around your workflow.

- Cons
Slower to become useful at first.
You’ll reinvent things that already exist.
Phone access and many integrations come much later.


### Building a hybrid (claudes answer)
Build the core yourself: the agent loop, tools, memory, resume/wrap/review/learn. That’s the learning and the portfolio. The core loop is small, so it isn’t a huge cost.
Use existing tools for daily productivity right now. Keep using Claude Code (or OpenClaw in a sandboxed account) while zizo grows. “From scratch” shouldn’t stop you from being productive today.
“From scratch” doesn’t mean no libraries. Use the Anthropic SDK, the Ollama client and the official MCP Python SDK. Build the architecture, not the plumbing.
Long term, zizo’s real value is its brain: your memory, conventions and modes. In v0.2, expose it as an MCP server, and it can plug into any agent, including Claude Code or OpenClaw. You aren’t competing with them; you’re building the personal layer they all lack.


## Interestingg Sources 
- https://bibek-poudel.medium.com/how-openclaw-works-understanding-ai-agents-through-a-real-architecture-5d59cc7a4764
- https://kanerika.com/blogs/openclaw-architecture/
- https://futureagi.com/blog/llm-agent-architectures-core-components/
- https://pub.towardsai.net/mcp-vs-agent-skills-what-the-2026-spec-change-finally-settled-for-me-9972d7456fba