"""Mock ope"""

from unittest import mock


def do_open(path):
    """docstring"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


builtin_open = open  # save the unpatched version


def mock_open(*args, **kwargs):
    """docstring"""
    if args[0] == "foo":
        # mocked open for path "foo"
        return mock.mock_open(read_data="bar")(*args, **kwargs)
    # unpatched version for every other path
    return builtin_open(*args, **kwargs)


@mock.patch("builtins.open", mock_open)
def test_0126_open():
    """docstring"""
    assert do_open("foo") == "bar"


@mock.patch("builtins.open", mock_open)
def test_0127_open2():
    """docstring"""
    assert do_open(__file__) != "bar"
