"""A simple example of test fixtures"""

from random import randint
import pytest
from rich.console import Console

console = Console()


# A simple fixture that generates some inputs
@pytest.fixture
def initial_value():
    console.print(
        f"\n[dark_orange]Generating an initial value! {randint(10000, 99999)}[/]"
    )
    return 5


# autouse=True will run the fixture before every test without needing to be called
@pytest.fixture(autouse=True)
def log_start():
    """Doc"""
    print("Test Starting!")


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# One test that uses our fixture
def test_0243_FXT_square(initial_value: int):
    """Doc"""
    result = square(initial_value)
    assert result == initial_value**2
