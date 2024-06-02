"""Test import from src folder"""

from src.sample import add


def test_0012_add_num():
    """basic test"""
    assert add(1, 2) == 3


class TestSample:
    """Class test"""

    def test_0013_add_num(self):
        """fn test"""
        assert add(1, 2) == 3

    def test_0333_add_num_fail(self):
        """fn test"""

        assert add(1, 2) == 5
