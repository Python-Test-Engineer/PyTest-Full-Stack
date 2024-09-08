"""A simple example using the skip marker in pytest"""


import pytest


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# A single test marked with skip
def test_0207_SKP_square() -> None:
    """Doc"""
    pytest.skip()
    num = 5
    result = square(num)
    assert result == num**2
