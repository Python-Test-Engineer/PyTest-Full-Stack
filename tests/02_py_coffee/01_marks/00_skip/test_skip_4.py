"""A simple example using the skip marker in pytest"""

import sys

import pytest


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# A single test marked with skip
@pytest.mark.skipif(
    sys.version_info > (3, 6), reason="Test requires Python version <= 3.6!"
)
def test_0209_SKP_square() -> None:
    """Doc"""
    num = 5
    result = square(num)
    assert result == num**2
