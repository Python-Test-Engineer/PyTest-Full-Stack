"""docstring"""
from datetime import datetime


class Student:
    """docstring"""

    def __init__(self, name, dob, branch):
        """docstring"""
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = 0

    def get_age(self) -> int:
        """docstring"""
        return (datetime.now() - self.dob).days // 365

    def add_credits(self, value):
        """docstring"""
        self.credits += value

    def get_credits(self):
        """docstring"""
        return self.credits
