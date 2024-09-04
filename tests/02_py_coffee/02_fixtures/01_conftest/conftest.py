"""A simple conftest file for pytest"""

import pytest

from rich.console import Console

console = Console()


# A simple fixture that generates an input
@pytest.fixture
def initial_value() -> int:
    """Doc"""
    console.print("\n[cyan]Higher level providing the value 50![/]")
    return 50
