"""A simple example of test fixtures"""

import pytest


# A simple fixture that generates some inputs
@pytest.fixture
def initial_value():
    """Doc"""
    return 5


# A simple fixture that logs a test is starting
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
