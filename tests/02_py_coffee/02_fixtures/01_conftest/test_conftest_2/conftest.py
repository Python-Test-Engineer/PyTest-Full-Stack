"""A simple conftest file for pytest"""

from rich.console import Console

console = Console()

import pytest


# A simple fixture that generates an input
@pytest.fixture
def initial_value() -> int:
    """Doc"""
    console.print("\n[cyan]Inner level providing the value 10![/]")
    console.print("[green]Closest conftest applies[/]")
    return 10
