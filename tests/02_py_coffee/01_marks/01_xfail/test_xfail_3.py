"""#A simple example xfail tests in pytest"""


import sys

import pytest


# Simple function that squares a number (with a bug!)
def square(num: int) -> int:
    """Doc"""
    return num + num


# A single test marked with xfail (we expect the test to fail)
@pytest.mark.xfail(
    sys.version_info > (3, 6), reason="Test requires Python version <= 3.6!"
)
def test_0224_XFL_square() -> None:
    """Doc"""
    num = 5
    result = square(num)
    assert result == num**2
