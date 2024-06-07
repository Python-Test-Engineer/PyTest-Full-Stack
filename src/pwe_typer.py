# https://pytest-with-eric.com/pytest-advanced/pytest-argparse-typer/

import typer

app = typer.Typer()


@app.command()
def greet(name: str, age: int = 0):
    """Greet someone."""
    if age:
        typer.echo(f"Hello, {name}! You are {age} years old.")
    else:
        typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
