"""Test"""

import pytest
from tut8.myapp.student import is_eligible_for_degree


def test_0109_student_is_eligible_for_degree_false(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam", 19)) is False


def test_0110_student_is_eligible_for_degree_true(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam", 21)) is True


@pytest.mark.parametrize("credits,expected", [(19, False), (21, True)])
def test_0111_student_is_eligible_for_degree(make_dummy_student, credits, expected):
    assert is_eligible_for_degree(make_dummy_student("sam", credits)) is expected
