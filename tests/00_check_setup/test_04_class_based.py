"""Example of class based tests with setup methods and teardown methods"""

from rich.console import Console

from src.sample import add

console = Console()


# Both class and def must follow naming conventions as specified in pytest.ini
class TestSample:
    # We can define setup and teardown methods as well. The setup method is run before the test method and the teardown method is run after the test method for each test.

    def setup_method(self, method):
        console.print(f"\n[dark_orange italic]Running setup for {method.__name__}[/]")

    def teardown_method(self, method):

        console.print(
            f"\n[dark_orange italic]Running teardown for {method.__name__}[/]"
        )

    def test_0031_SET_add_num(self):
        """fn test in a class"""
        assert add(1, 2) == 3

    def test_0032_SET_add_num_will_fail(self):
        """failing fn test in a class"""
        console.print("[yellow]Example of failed test[/]⚠️")
        assert add(1, 2) == 5
