"""Some basic asserts"""

from time import sleep
import pytest
from rich.console import Console

console = Console()


def test_0001_SET_pass():
    sleep(1)
    """A test with console formatting and sleep"""
    console.print("\n[blue bold]Testing Rich[/]\n")
    assert True


@pytest.mark.xfail
def test_0002_SET_xfail():
    """A test that is expected to fail so xfail will give a 'pass'"""
    assert 0


@pytest.mark.xfail
def test_0003_SET_xpass():
    """A test that was expected to fail but passes so is an xpass"""
    assert True


def test_0004_SET_fail():
    """A test fail to show as an example"""
    console.print("[red italic]Example of a failed test[/]⚠️")
    assert False


@pytest.mark.outer
@pytest.mark.setup
@pytest.mark.inner
def test_0005_SET_many_markers():
    """A test to show we can have many markers and their order"""
    assert 1 in divmod(9, 5)
    assert "this" in "this is pytest"
    assert [1, 2, 4] == [1, 2, 4]


def test_0006_SET_case01():
    """A test using pytest.raises"""
    console.print("[dark_orange bold]Example [/]")
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0


@pytest.mark.skip(reason="data not ready")
def test_0007_SET_skip():
    """A test with skip and optional reason"""
    assert True


def func1():
    """A test"""
    raise ValueError("EXPECTED IndexError func1 raised")
