"""Test import from src folder"""

from rich.console import Console

from src.sample import add

console = Console()


# Both class and def must follow naming conventions as specified in pytest.ini
class TestSample:
    """Class based est"""

    def test_0031_SET_add_num(self):
        """fn test in a class"""
        assert add(1, 2) == 3

    def test_0032_SET_add_num_will_fail(self):
        """failing fn test in a class"""
        console.print("[red italic]Example of failed test[/]⚠️")
        assert add(1, 2) == 5
