from fns import add, mul


def test_add():
    print("Test add called")
    actual_result = add(5, 2)
    expected_result = 7
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    if actual_result != expected_result:
        print("FAILED")
    else:
        print("PASSED")
    assert (
        actual_result == expected_result
    ), f"Actual result should be {expected_result}"


def test_add_fail():
    print("Test add_fail called")
    actual_result = add(1, 2)
    expected_result = 6
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    if actual_result != expected_result:
        print("FAILED")
    else:
        print("PASSED")
    try:
        assert (
            actual_result == expected_result
        ), f"Actual result should be {expected_result}"
    except Exception as e:
        print(e)


def test_mul():
    print("Test mul called")
    actual_result = mul(2, 3)
    expected_result = 6
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    if actual_result != expected_result:
        print("FAILED")
    else:
        print("PASSED")
    assert (
        actual_result == expected_result
    ), f"Actual result should be {expected_result}"


def test_mul_fail():
    print("Test mul_fail called")
    actual_result = mul(2, 2)
    expected_result = 9
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    if actual_result != expected_result:
        print("FAILED")
    else:
        print("PASSED")
    try:
        assert actual_result == expected_result, "Actual result should be 4"
    except Exception as e:
        print(e)
