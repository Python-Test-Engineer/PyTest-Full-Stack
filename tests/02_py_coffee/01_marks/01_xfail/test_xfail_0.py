"""A simple example xfail tests in pytest
By specifying on the commandline:

pytest --runxfail
you can force the running and reporting of an xfail marked test as if it weren’t marked at all. This also causes pytest.xfail() to produce no effect.

"""

import pytest


# Simple function that squares a number (with a bug!)
def square(num: int) -> int:
    """Doc"""
    return num + num


# A single test marked with xfail (we expect the test to fail)
@pytest.mark.xfail
def test_0220_XFL_square() -> None:
    """Doc"""
    num = 5
    result = square(num)
    assert result == num**2
