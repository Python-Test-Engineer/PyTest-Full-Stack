"""A simple example of test fixtures"""

import pytest


# A simple fixture that generates some inputs
@pytest.fixture
def initial_value():
    return 5


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# One test that uses our fixture
def test_0240_FXT_square(initial_value: int) -> None:
    """Doc"""
    result = square(initial_value)
    assert result == initial_value**2
