"""A simple example of tests using pytest"""
# By Nick from CoffeeBeforeArch


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# Simple function that cubes another
def cube(num: int) -> int:
    """Doc"""
    return square(num) * num


# Tests start with "test_"
def test_0201_GEN_quare():
    """Doc"""
    num = 5
    result = square(num)
    assert result == num**2


# Define another test in the same file
def test_0202_GEN_1_cube():
    """Doc"""
    num = 5
    result = cube(num)
    assert result == num**3
