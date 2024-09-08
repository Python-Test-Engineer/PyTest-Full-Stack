""" conftest.py is a file that pytest will automatically import fixtures from """

import pytest
from rich.console import Console

console = Console()

# A simple fixture that generates some inputs
@pytest.fixture
def initial_value():
    """Doc"""
    console.print("\n[green]Providing a value to our test![/]")
    yield 5
    console.print("\n[dark_orange]Finishing Up![/]")
