# CREATING SUBCOMMANDS FOR CLI CHAT 

import typer
from dotenv import load_dotenv
from anthropic import Anthropic

app = typer.Typer() #CLI
load_dotenv()
client = Anthropic() 

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "Hälsa användaren Zaynab på en mening "}],
)

@app.command()
def chat() -> None:
    """Pair-programmer chat."""
    client = Anthropic()
    print(response.content[0].text) # calling the API

@app.command()
def resume() -> None:
    """Where was I? Last session, recent commits and theee next step."""
    print("resume: coming soon")
