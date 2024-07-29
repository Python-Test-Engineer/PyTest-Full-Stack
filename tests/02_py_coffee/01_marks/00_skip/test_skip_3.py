"""A simple example using the skip marker in pytest"""

import pytest


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# A single test marked with skip
@pytest.mark.skip(reason="Look! We are skipping this test!")
def test_SKP05_square() -> None:
    """Doc"""
    num = 5
    result = square(num)
    assert result == num**2
