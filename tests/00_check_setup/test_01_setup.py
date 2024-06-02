"""Some basic asserts"""

from time import sleep
import pytest


def test_0001_pass():
    sleep(1)
    """A test"""
    assert True


@pytest.mark.xfail
def test_0002_xfail():
    """A test"""
    assert 0


@pytest.mark.xfail
def test_0003_xpass():
    """A test"""
    assert True


def test_0004_fail():
    """A test"""
    assert False


@pytest.mark.outer
@pytest.mark.setup
@pytest.mark.inner
def test_0005_many_markers():
    """A test"""
    assert 1 in divmod(9, 5)
    assert "this" in "this is pytest"
    assert [1, 2, 4] == [1, 2, 4]


def test_0006_case01():
    """A test"""
    print("---> Sanity Marker", end=" ")
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
        # assert 3 > 3


@pytest.mark.skip(reason="data not ready")
def test_0346_skip():
    """A test"""
    print("---> Sanity Marker", end=" ")
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
        # assert 3 > 3


@pytest.mark.skip(reason="no way of currently testing this")
def test_0358_skip():
    """A test"""
    assert True


@pytest.mark.xfail
def test_0233_xpass():
    """A test"""
    assert True


def test_0234_xpass():
    """A test"""
    assert True


def test_0236_fail():
    """A test"""
    assert False


def func1():
    """A test"""
    raise ValueError("EXPECTED IndexError func1 raised")
