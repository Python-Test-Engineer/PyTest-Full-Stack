"""A simple conftest file for pytest"""

from random import randint
import pytest

from rich.console import Console


console = Console()


# A simple fixture that prints that tests are starting
@pytest.fixture(autouse=True)
def log_start():
    console.print(
        f"\n[dark_orange]Generating an initial value! {randint(10000, 99999)}[/]"
    )
