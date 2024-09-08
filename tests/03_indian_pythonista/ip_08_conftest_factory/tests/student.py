"""docstring"""
from datetime import datetime


class Student:
    """docstring"""

    def __init__(self, name, dob, branch, credits):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credits

    def get_age(self) -> datetime:
        """docstring"""
        return (datetime.now() - self.dob).days // 365

    def get_credits(self) -> float:
        """docstring"""
        return self.credits


def is_eligible_for_degree(student) -> int:
    """docstring"""
    return student.get_credits() >= 20
