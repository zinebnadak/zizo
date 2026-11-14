# CREATING SUBCOMMANDS FOR CLI CHAT

import typer
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

app = typer.Typer()  # CLI
client = Anthropic()


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
        response = client.messages.create(            # 3. only then call the API
            model="claude-haiku-5-5",
            max_tokens=500,
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
