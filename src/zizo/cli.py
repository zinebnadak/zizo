# CREATING SUBCOMMANDS FOR CLI CHAT 

import typer

app = typer.Typer() #CLI

@app.command()
def chat() -> None:
    """Pair-programmer chat."""
    print("chat: coming soon")

@app.command()
def resume() -> None:
    """Where was I? Last session, recent commits and theee next step."""
    print("resume: coming soon")
