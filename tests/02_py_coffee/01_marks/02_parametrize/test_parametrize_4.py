"""A simple tests with parametrized input"""

import pytest


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# Our test parametrized test
@pytest.mark.parametrize(
    "num",
    [
        pytest.param(-1, id="negative"),
        pytest.param(0, id="zero"),
        pytest.param(1, id="positive"),
    ],
)
def test_0238_PRM_square(num: int) -> None:
    """We can use friendly ids"""
    result = square(num)
    assert result == num**2
