"""A simple conftest file for pytest"""


import pytest


# A simple fixture that generates an input
@pytest.fixture
def initial_value() -> int:
    """Doc"""
    return 5
