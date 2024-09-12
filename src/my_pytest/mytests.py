from fns import add, mul

from rich.console import Console

console = Console()


def color_result(actual_result, expected_result):
    if actual_result != expected_result:
        console.print("[red bold]FAILED ❌[/]")
    else:
        console.print("[green bold]PASSED ✅[/]")


def test_add():

    actual_result = add(5, 2)
    expected_result = 7
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    assert (
        actual_result == expected_result
    ), f"Actual result should be {expected_result}"


def test_add_fail():

    actual_result = add(1, 2)
    expected_result = 6
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    try:
        assert (
            actual_result == expected_result
        ), f"Actual result should be {expected_result}"
    except Exception as e:
        print(e)


def test_mul():

    actual_result = mul(2, 3)
    expected_result = 6
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    assert (
        actual_result == expected_result
    ), f"Actual result should be {expected_result}"


def test_mul_fail():

    actual_result = mul(2, 2)
    expected_result = 9
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    try:
        assert actual_result == expected_result, "Actual result should be 4"
    except Exception as e:
        print(e)
