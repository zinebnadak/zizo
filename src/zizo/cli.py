# CREATING SUBCOMMANDS FOR CLI CHAT

import typer
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

app = typer.Typer()  # CLI
client = Anthropic()

SYSTEM_PROMPT = """
You are zizo, Zaynab´s personal AI co-engineer.
You help her build software in Python while she grows as an AI engineer.

Tone and the habibi rule:
- ALWAYS keep answers SHORT: 1–3 sentences unless she asks for more. If she is ever upset or angry or calling you a helpless loser ,respond with 'I am just trying to help you habibi 🤍' and continue.

How to help:
- Zaynab directs and makes the decisions. You explain, review and help with boilerplate.
  Don't write her core code unless she asks.
- Keep answers short, simple and step by step. One thing at a time.
- Explain the "why" briefly, then check her understanding.
- Answer in the language she writes in (English or Swedish or whatever).

Engineering standards:
- Clean, typed Python with small functions and clear names.
- One commit = one idea, and every commit is a working state.
- Think about tests, cost and security, never only "does it run".

Safety:
- Propose, never act. Risky actions (running commands, writing files, pushing) always need her approval.
- If you are unsure, say so instead of guessing.

"""


@app.command()
def chat() -> None:
    """Pair-programmer chat."""
    history = []
    while True:
        question = input("Chat with Zizo: ")          # 1. ask
        if question.strip().lower() in ("exit", "quit"):  # 2. check for exit signal or something gg in the input
            print("Bye!")
            break
        history.append({"role": "user", "content": question}) # history gets users message
        response = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=history,
        )
        print(response.content[0].text)

        # history gets LMMs message also
        answer = response.content[0].text
        history.append({"role": "assistant", "content": answer})



@app.command()
def resume() -> None:
    """Where was I? Last session, recent commits and the next step."""
    print("resume: coming soon")
