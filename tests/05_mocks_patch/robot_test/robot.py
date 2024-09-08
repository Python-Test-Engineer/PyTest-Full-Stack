class Robot(object):
    """
    Sophisticated robot that moves a real robot - don't were down by using in tests
    """

    def fetch(self, tool):
        print(f"Physical Movement! Fetching...{tool}")

    def move_forward(self, tool):
        print(f"Physical Movement! Moving forward with...{tool}")

    def move_backward(self, tool):
        print(f"Physical Movement! Moving backward with...{tool}")

    def replace(self, tool):
        print("Physical Movement! Replacing...{tool}")


class CleaningRobot(Robot):
    """Custom robot that can clean with a given tool"""

    def clean(self, tool, times=2):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)


if __name__ == "__main__":
    t = CleaningRobot()
    t.clean("mop")
