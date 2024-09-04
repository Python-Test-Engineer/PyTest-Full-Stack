""" A simple using pytest cache"""


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# One test that uses our fixture
def test_0260_CHE_square(expensive_value: int) -> None:
    """Doc"""
    result = square(expensive_value)
    assert result == expensive_value**2
