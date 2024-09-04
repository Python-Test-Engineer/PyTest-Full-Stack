"""A simple example using the importorskip in pytest.

If the module `module_does_not_exist` is not installed, this module will be skipped.
"""

import pytest

my_import = pytest.importorskip("module_does_not_exist")


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


def test_0210_SKP_square() -> None:
    """Doc"""
    num = 7
    result = square(num)
    assert result == num**2


def test_0211_SKP_square() -> None:
    """Doc"""
    num = 5
    result = square(num)
    assert result == num**2
