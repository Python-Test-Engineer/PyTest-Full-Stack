"""A simple example using the skip marker in pytest"""

import pytest

my_import = pytest.importorskip("my_module")


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# A single test marked with skip
def test_0057_square() -> None:
    """Doc"""
    num = 5
    result = square(num)
    assert result == num**2
