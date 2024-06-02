"""docstring"""
from datetime import datetime

import pytest
from tut7.myapp.student import Student


@pytest.fixture
def make_dummy_student():
    """docstring"""

    def _make_dummy_student(name, credits):
        """docstring"""
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student
