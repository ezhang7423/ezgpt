# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console
from typer_config.decorators import dump_json_config, use_json_config

from ezgpt import setup_experiment

setup_experiment()
from ezgpt import LOG_DIR, version

app = typer.Typer(
    name="ezgpt",
    help="faster, simpler, more interpretable nanoGPT",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]ezgpt[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
@use_json_config()
@dump_json_config(str(LOG_DIR / "config.json"))
def main(
    name: str = typer.Option(..., help="Person to greet."),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the ezgpt package.",
    ),
) -> None:
    """Print a greeting with a giving name."""
    console.print(f"[bold green]{name}[/]")


app()
