"""docstring"""


def validate_age(age: int) -> None:
    """docstring"""
    if age < 0:
        raise ValueError("Age cannot be less than 0")
