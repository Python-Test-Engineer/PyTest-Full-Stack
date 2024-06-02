"""A simple tests with parametrized input"""


import pytest


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# Our test parametrized test
@pytest.mark.parametrize("num,ref", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
def test_0075_square(num: int, ref: int):
    """Doc"""
    result = square(num)
    assert result == ref
