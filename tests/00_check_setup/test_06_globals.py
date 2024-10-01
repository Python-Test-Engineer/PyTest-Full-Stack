"""Examples of using globals"""

# We don't need to import pytest for built-in fixtures

from rich.console import Console

console = Console()


# Simple function that squares a number
def square(num: int) -> int:
    return num * num


# Simple function that cubes another
def cube(num: int) -> int:
    return square(num) * num


# Using pytest.config for global values
def test_0065_SET_globals(global_value):
    if global_value:
        print(global_value)

    num = 5
    result = square(num)
    assert result == num**2


# Define another test in the same file
def test_0066_SET_request_config(request):
    print("\n")
    console.print(f"type(request): {type(request)}")
    # console.print(dir(request))
    if request.config.my_global_value is not None:
        print(f"\nrequest.config.my_global_value: {request.config.my_global_value}")
    num = 5
    result = cube(num)
    assert result == num**3
