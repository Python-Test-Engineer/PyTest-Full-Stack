"""Demo pytest-xdist plugin"""

import pytest
from rich.console import Console

console = Console()

num = 300_000_000


# A test with a lot of processing
def test_0051_SET_xdist_01():
    console.print("\n[blue bold]Testing xdist 01[/]\n")
    for _ in range(num):
        pass
    assert True


def test_0052_SET_xdist_02():
    console.print("\n[blue bold]Testing xdist 02[/]\n")
    for _ in range(num):
        pass
    assert True


def test_0053_SET_xdist_03():
    console.print("\n[blue bold]Testing xdist 03[/]\n")
    for _ in range(num):
        pass
    assert True


def test_0054_SET_xdist_04():
    console.print("\n[blue bold]Testing xdist 04[/]\n")
    for _ in range(num):
        pass
    assert True


# with n=2 takes 1.25s
# def test_0059_SET_xdist_09():
#     for _ in range(1):
#         pass
#     assert True
