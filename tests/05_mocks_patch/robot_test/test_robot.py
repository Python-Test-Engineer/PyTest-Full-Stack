from unittest import TestCase
import unittest

from robot import Robot, CleaningRobot


class MockRobot(Robot):
    """Simulate a Robot so as not to wear it out"""

    def __init__(self):
        self.tasks = []

    def fetch(self, tool):
        self.tasks.append(f"Physical Movement! Fetching...{tool}")

    def move_forward(self, tool):
        self.tasks.append(f"Physical Movement! Moving forward with...{tool}")

    def move_backward(self, tool):
        self.tasks.append(f"Physical Movement! Moving backward with...{tool}")

    def replace(self, tool):
        self.tasks.append(f"Physical Movement! Replacing...{tool}")


class MockCleaningRobot(CleaningRobot, MockRobot):
    """Inject a mcok robot into the robot dependency"""


class TestCleaningRobot(TestCase):
    def test_0150_clean(self):
        t = MockCleaningRobot()
        t.clean("mop")
        expected = (
            ["Physical Movement! Fetching...mop"]
            + [
                "Physical Movement! Moving forward with...mop",
                "Physical Movement! Moving backward with...mop",
            ]
            * 2
            + ["Physical Movement! Replacing...mop"]
        )
        self.assertEqual(t.tasks, expected)


if __name__ == "__main__":
    unittest.main()
