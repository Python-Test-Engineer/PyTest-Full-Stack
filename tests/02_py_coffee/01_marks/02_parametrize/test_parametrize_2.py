"""A simple tests with parametrized input"""


import math

import pytest


# Simple function that raises a base to a power
def pow(base: int, exponent: int) -> int:
    """Doc"""
    return base**exponent


# Our test parametrized test
@pytest.mark.parametrize("base", [1, 2, 3])
@pytest.mark.parametrize("exponent", [4, 5, 6])
def test_0236_PRM_pow(base: int, exponent: int) -> None:
    """Doc"""
    # Test if our function matches math.pow
    result = pow(base, exponent)
    assert result == math.pow(base, exponent)
