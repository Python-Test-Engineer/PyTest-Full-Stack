"""A simple conftest file for pytest"""


import pytest


# A simple fixture that prints that tests are starting
@pytest.fixture(autouse=True)
def log_start():
    """Doc"""
    print("Test Starting!")
