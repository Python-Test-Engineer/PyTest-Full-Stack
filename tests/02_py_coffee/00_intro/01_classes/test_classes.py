"""A simple exaple of tests grouped into a class """


# Simple function that squares a number
def square(num: int) -> int:
    """Doc"""
    return num * num


# Simple function that cubes another
def cube(num: int) -> int:
    """Doc"""
    return square(num) * num


# Our class containing our tests as methods
# Note: Must start with `Test`
class TestClass:
    """Doc"""

    # Share our common number between test instances
    num = 5

    # Test squaring of a number
    def test_0203_GEN_square(self):
        """Doc"""
        result = square(self.num)
        assert result == self.num**2

    # Test cubing of a number
    def test_0204_GEN_cube(self):
        """Doc"""
        result = cube(self.num)
        assert result == self.num**3
