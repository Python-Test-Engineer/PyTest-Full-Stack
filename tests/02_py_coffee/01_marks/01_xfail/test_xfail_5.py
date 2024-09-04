"""A simple example xfail tests in pytest"""

import pytest


# Simple function that squares a number (with a bug!)
def square(num: int) -> int:
    """Doc"""
    return num + num


# A single test marked with xfail (we expect the test to fail)
@pytest.mark.xfail(strict=True)
def test_0226_XFL_square() -> None:
    """strict parameter
    https://docs.pytest.org/en/stable/how-to/skipping.html#strict-parameter
    Both XFAIL and XPASS don’t fail the test suite by default. You can change this by setting the strict keyword-only parameter to True:

    @pytest.mark.xfail(strict=True)
    def test_function(): ...
    This will make XPASS (“unexpectedly passing”) results from this test to fail the test suite.

    You can change the default value of the strict parameter using the xfail_strict ini option:

    [pytest]
    xfail_strict=true"""
    num = 5
    result = square(num)
    assert result == num**2
