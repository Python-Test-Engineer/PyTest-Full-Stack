"""Mock open example"""

from unittest import mock

from rich.console import Console

console = Console()


def do_open(path):
    """Regular function"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


builtin_open = open  # save the unpatched version


def mock_open(*args, **kwargs):
    """A mocked open"""
    if args[0] == "test.txt":
        # mocked open for path "test.txt"
        return mock.mock_open(read_data="data in test.txt")(*args, **kwargs)
    # unpatched version for every other path
    return builtin_open(*args, **kwargs)


@mock.patch("builtins.open", mock_open)
def test_0040_SET_open():
    """Testing patch"""
    assert do_open("test.txt") == "data in test.txt"


@mock.patch("builtins.open", mock_open)
def test_0041_open2():
    """Testing patch"""
    assert do_open(__file__) != "data in test.txt"
