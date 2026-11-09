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
    question = input("Chat with Zizo: ")
    response = client.messages.create(  # call the API only when chatting
        model="claude-haiku-5-5",
        max_tokens=500,
        messages=[{"role": "user", "content": question}],
    )
    print(response.content[0].text)


@app.command()
def resume() -> None:
    """Where was I? Last session, recent commits and the next step."""
    print("resume: coming soon")
