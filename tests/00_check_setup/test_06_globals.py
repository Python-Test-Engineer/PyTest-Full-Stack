"""A simple example of tests using pytest"""

import pytest


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# Simple function that cubes another
def cube(num: int) -> int:
    """Doc"""
    return square(num) * num


# Using pytest.config for global values
def test_0065_SET_globals(global_value):
    print(global_value)
    num = 5
    result = square(num)
    assert result == num**2


# Define another test in the same file
def test_0066_SET_request_config(request):
    if request.config.my_global_value:
        print(f"\nrequest.config.my_global_value: {request.config.my_global_value}")
    num = 5
    result = cube(num)
    assert result == num**3
