"""https://www.youtube.com/watch?v=5sJ3rTGenXs&list=PLxNPSjHT5qvuZ_JT1bknzrS8YqLiMjNpS&index=8

This explains how we can pass a value on the command line to determine how many values will be in our list
"""

import pytest


# Simple function that computes the sum of list elements
def sum_elements(elements: list[int]) -> int:
    """Doc"""
    total = 0
    for e in elements:
        total += e
    return total


# One test that uses our fixture
# The 'num_elements' parameter is automatically forwarded to our fixture
@pytest.mark.parametrize("num_elements", [1, 2, 3, 4, 5])
def test_0086_sum(element_list: list[int]) -> None:
    """Doc"""
    result = sum_elements(element_list)
    assert result == sum(element_list)
