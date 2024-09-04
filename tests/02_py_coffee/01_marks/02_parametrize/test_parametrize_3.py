"""A simple tests with parametrized input"""

import pytest


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# Our test parametrized test
@pytest.mark.parametrize("num", [1, 2, pytest.param(3, marks=pytest.mark.skip), 4, 5])
def test_0237_PRM_square(num: int) -> None:
    """Doc"""
    result = square(num)
    assert result == num**2
