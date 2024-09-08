from .sample import add


def test_1091_add_num():
    assert add(1, 2) == 3


def test_1092_add_str():
    assert add("a", "b") == "ab"


class TestSample:
    def test_1093_add_num(self):
        assert add(1, 2) == 3

    def test_1094_add_str(self):
        assert add("a", "b") == "ab"
