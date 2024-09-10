"""A simple example xfail tests in pytest"""

import pytest


# Simple function that squares a number (with a bug!)
def square(num: int) -> int:
    """Doc"""
    return num + num


# A single test marked with xfail (we expect the test to fail)
# If a test should be marked as xfail and reported as such but should not be even executed, use the run parameter as False
@pytest.mark.xfail(run=False)
def test_0227_XFL_square() -> None:
    num = 5
    result = square(num)
    assert result == num**2
