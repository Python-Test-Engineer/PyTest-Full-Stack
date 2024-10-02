def add(x, y):
    return x + y


def test_add_pass():
    assert add(1, 2) == 3


def test_add_fail():
    assert add(1, 2) == 4
