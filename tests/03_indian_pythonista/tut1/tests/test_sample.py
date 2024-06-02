from tut1.myapp.sample import add


def test_0091_add_num():
    assert add(1, 2) == 3


def test_0092_add_str():
    assert add("a", "b") == "ab"


class TestSample:
    def test_0093_add_num(self):
        assert add(1, 2) == 3

    def test_0094_add_str(self):
        assert add("a", "b") == "ab"
