import sys


from fns import add, mul
from utils import color_result
from rich.console import Console

from results import Results

r = Results.get_instance()
console = Console()


def store_result(test_name, actual_result, expected_result):
    try:
        assert (
            actual_result == expected_result
        ), f"Actual result should be {expected_result}"
        r.add_result({"test_name": test_name, "result": "PASSED"})
    except Exception as e:
        r.add_result({"test_name": test_name, "result": "FAILED"})
        print(e)


def test_add():
    test_name = sys._getframe().f_code.co_name
    actual_result = add(5, 2)
    expected_result = 7
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(test_name, actual_result, expected_result)


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
    try:
        assert (
            actual_result == expected_result
        ), f"Actual result should be {expected_result}"
    except Exception as e:
        print(e)


def test_mul_fail():

    actual_result = mul(2, 2)
    expected_result = 9
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    try:
        assert actual_result == expected_result, "Actual result should be 4"
    except Exception as e:
        print(e)
