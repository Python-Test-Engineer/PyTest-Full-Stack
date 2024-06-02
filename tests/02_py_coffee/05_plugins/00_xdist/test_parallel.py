""" A simple test of parallelizing tests with xdist"""

import time

import pytest


# A simple function that sleeps for 1 second
def sleep() -> None:
    """Doc"""
    time.sleep(1)


# A test for our sleep function
@pytest.mark.parametrize("variant", range(3))
def test_0090_sleep(variant: int) -> None:
    """Doc"""
    sleep()
