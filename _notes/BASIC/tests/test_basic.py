def add(x, y):
    return x + y


def test_add_pass():
    actual_result = add(1, 2)
    expected_result = 3
    assert actual_result == expected_result


def test_add_fail():
    actual_result = add(2, 2) + 1  # introduce failure
    expected_result = 4
    assert actual_result == expected_result
