import sys


from fns import add, mul, sub, div
from utils import color_result, store_result
from rich.console import Console

from results import Results

r = Results.get_instance()
console = Console()


def my_test_10_add():
    actual_result = add(5, 2)
    expected_result = 7
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(sys._getframe().f_code.co_name, actual_result, expected_result)


def my_test_11_add_fail():
    actual_result = add(1, 2) + 1  # simulate error
    expected_result = 3
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(sys._getframe().f_code.co_name, actual_result, expected_result)


def my_test_20_mul():
    actual_result = mul(2, 3)
    expected_result = 6
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(sys._getframe().f_code.co_name, actual_result, expected_result)


def my_test_21_mul_fail():
    actual_result = mul(4, 2) + 1  # simulate error
    expected_result = 8
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(sys._getframe().f_code.co_name, actual_result, expected_result)


def my_test_30_sub():
    actual_result = sub(8, 2)
    expected_result = 6
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(sys._getframe().f_code.co_name, actual_result, expected_result)


def my_test_31_sub_fail():
    actual_result = sub(11, 2) + 1  # simulate error
    expected_result = 9
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(sys._getframe().f_code.co_name, actual_result, expected_result)


def my_test_40_div():
    actual_result = div(8, 2)
    expected_result = 4
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(sys._getframe().f_code.co_name, actual_result, expected_result)


def my_test_42_div_fail():
    actual_result = div(8, 2) + 1  # simulate error
    expected_result = 4
    print(f"Actual result: {actual_result} - Expected result: {expected_result}")
    color_result(actual_result, expected_result)
    store_result(sys._getframe().f_code.co_name, actual_result, expected_result)


class MyTestSample:
    # we can define setup and teardown methods as well

    def setup_method(self, method):
        console.print(f"\n[dark_orange italic]Running setup for {method.__name__}[/]")

    def teardown_method(self, method):

        console.print(
            f"\n[dark_orange italic]Running teardown for {method.__name__}[/]"
        )

    def my_test_50(self):
        console.print("[green italic]Example of PASSED test[/]✅")
        assert add(1, 2) == 3

    def my_test_51_will_fail(self):
        """failing fn test in a class"""
        console.print("[red italic]Example of failed test[/]❌")
        assert add(1, 2) == 5


if __name__ == "__main__":
    t = MyTestSample()
    t.my_test_50()
