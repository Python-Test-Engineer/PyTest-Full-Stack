"""A simple example of test fixtures"""

from random import randint
import pytest


# Change scope to function to see difference
@pytest.fixture(scope="module")
def initial_value() -> int:
    print(randint(10000, 99999))
    print("Generating an initial value!")
    return 5


def square(num: int) -> int:
    """Doc"""
    return num * num


def cube(num: int) -> int:
    """Doc"""
    return square(num) * num


# initial_value is a fixture that is called once when scope=module but every test if scope=function (default)
def test_0244_FXT_square(initial_value: int):
    """Doc"""
    result = square(initial_value)
    assert result == initial_value**2


# One test that uses our fixture
def test_0245_FXT_cube(initial_value: int):
    """Doc"""
    result = cube(initial_value)
    assert result == initial_value**3
