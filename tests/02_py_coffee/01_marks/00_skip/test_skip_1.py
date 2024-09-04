"""A simple example of skipping tests that are part of a class"""

import pytest


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# Simple function that cubes another
def cube(num: int) -> int:
    """Doc"""
    return square(num) * num


# Our class containing our tests as methods
@pytest.mark.skip
class TestClass:
    """Doc"""

    # Share our common number between test instances
    num = 5

    # Test squaring of a number
    def test_0205_SKP_square(self) -> None:
        """Doc"""
        result = square(self.num)
        assert result == self.num**2

    # Test cubing of a number
    def test_0206_SKP_cube(self) -> None:
        """Doc"""
        result = cube(self.num)
        assert result == self.num**3
