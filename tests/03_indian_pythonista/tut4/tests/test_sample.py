import pytest
from tut4.myapp.sample import add


def test_0100_add_num():
    assert add(1, 2) == 3


def test_0101_add_str():
    assert add("a", "b") == "ab"


def test_0102_add_list():
    assert add([1, 2], [3]) == [1, 2, 3]


@pytest.mark.parametrize(
    "a,b,c",
    [(1, 2, 3), ("a", "b", "ab"), ([1, 2], [3], [1, 2, 3])],
    ids=["num", "str", "list"],
)
def test_0103_add(a, b, c):
    assert add(a, b) == c


@pytest.mark.xfail
def test_0333_add_xpass(a, b, c):
    assert True
