"""A simple example using conftest with test fixtures"""

from rich.console import Console

console = Console()


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# One test that uses our fixture
def test_0252_CNF_square(initial_value: int) -> None:
    """Doc"""
    console.print(f"\n[dark_orange]Initial value: {initial_value}[/]")
    result = square(initial_value)
    assert result == initial_value**2
