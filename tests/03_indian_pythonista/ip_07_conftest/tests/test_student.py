"""Test"""

from .student import get_topper


def test_1109_get_topper(make_dummy_student):
    """docstring"""
    students = [
        make_dummy_student("ram", 21),
        make_dummy_student("shyam", 19),
        make_dummy_student("ravi", 22),
    ]

    topper = get_topper(students)

    assert topper == students[2]
