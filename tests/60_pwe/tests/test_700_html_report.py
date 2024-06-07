import pytest


def add_numbers(a, b):
    return a + b


def test_addition():
    assert add_numbers(3, 4) == 7


def test_addition_failure():
    assert add_numbers(5, 6) == 12  # This will fail


def test_addition_type_error():
    with pytest.raises(TypeError):
        add_numbers("three", "four")
