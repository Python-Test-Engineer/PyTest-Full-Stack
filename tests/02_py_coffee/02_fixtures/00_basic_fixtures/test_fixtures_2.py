"""A simple example of test fixtures"""

import pytest


# A simple fixture that generates some inputs
@pytest.fixture(scope="module")
def initial_value() -> int:
    """Doc"""
    print("Generating an initial value!")
    return 5


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# Simple function that squares a number
def cube(num: int) -> int:
    """Doc"""
    return square(num) * num


# One test that uses our fixture
def test_0079_square(initial_value: int):
    """Doc"""
    result = square(initial_value)
    assert result == initial_value**2


# One test that uses our fixture
def test_0080_cube(initial_value: int):
    """Doc"""
    result = cube(initial_value)
    assert result == initial_value**3
