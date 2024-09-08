"""A simple example using conftest with test fixtures"""


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# One test that uses our fixture
def test_0250_CNF_square(initial_value: int) -> None:
    """Doc"""
    result = square(initial_value)
    assert result == initial_value**2
