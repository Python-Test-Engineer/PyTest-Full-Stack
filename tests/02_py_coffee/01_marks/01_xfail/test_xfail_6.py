"""A simple example xfail tests in pytest"""

import pytest


# Simple function that squares a number (with a bug!)
def square(num: int) -> int:
    """Doc"""
    return num + num


# A single test marked with xfail (we expect the test to fail)
@pytest.mark.xfail(run=False)
def test_0072_square() -> None:
    """Doc"""
    num = 5
    result = square(num)
    assert result == num**2
