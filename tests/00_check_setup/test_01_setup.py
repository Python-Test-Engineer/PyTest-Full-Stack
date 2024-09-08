"""Some basic asserts"""

from time import sleep
import pytest
from rich.console import Console

console = Console()


# A test with console formatting and sleep
def test_0001_SET_pass():
    sleep(1)
    console.print("\n[blue bold]Testing Rich[/]\n")
    assert True


# A test that is expected to fail so xfail will give a 'pass'
@pytest.mark.xfail
def test_0002_SET_xfail():
    assert 0


# A test that was expected to fail but passes so is an xpas
@pytest.mark.xfail
def test_0003_SET_xpass():
    assert True


# A test fail to show as an example
def test_0004_SET_this_will_fail():
    console.print("[red italic]Example of a failed test[/]⚠️")
    assert False


# A test to show we can have many markers and their order
@pytest.mark.outer
@pytest.mark.setup
@pytest.mark.inner
def test_0005_SET_many_markers():
    assert 1 in divmod(9, 5)
    assert "this" in "this is pytest"
    assert [1, 2, 4] == [1, 2, 4]


# A test using pytest.raises
def test_0006_SET_case01():
    console.print("[dark_orange bold]Example [/]")
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0


# A test with skip and optional reason
@pytest.mark.skip(reason="data not ready")
def test_0007_SET_skip():
    assert True


# Raise a ValueError
def func1():
    raise ValueError("EXPECTED IndexError func1 raised")
