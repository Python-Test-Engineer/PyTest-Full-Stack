"""A simple example of test fixtures"""

from random import randint
import pytest
from rich.console import Console

console = Console()


# A simple fixture that generates some inputs
@pytest.fixture
def initial_value():
    console.print(f"\n[dark_orange]initial_value fixture {randint(10000, 99999)}[/]")
    return 5


def square(num: int) -> int:
    """Doc"""
    return num * num


# We pass in the fixture - dependency injection
def test_0240_FXT_square(initial_value: int) -> None:
    """Doc"""
    result = square(initial_value)
    assert result == initial_value**2
