"""Some assert examples"""

from time import sleep
import logging

import pytest

# uses config in pytest.ini
LOGGER = logging.getLogger(__name__)


def test_0021_SET_a1():
    LOGGER.info("test_a1")
    assert 4 != 3


def test_0022_SET_a2():
    sleep(2)
    LOGGER.info("test_a2")
    assert 1


def func1():
    """A test"""
    LOGGER.error("func1 ValueError")
    raise ValueError("EXPECTED IndexError func1 raised")


@pytest.mark.sanity
@pytest.mark.xfail
def test_0024_SET_case03_xfail():
    """A test"""
    LOGGER.error("test_case03 xfail")
    with pytest.raises(Exception) as excinfo:
        # assert (1,2,3) == (1,2,4)
        func1()
    print(str(excinfo))
    assert (str(excinfo.value)) == "Exception func1 raised"
