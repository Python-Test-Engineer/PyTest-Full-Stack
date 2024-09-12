class Results:
    __instance = None

    @staticmethod
    def get_instance():
        """Static access method."""
        if Results.__instance == None:
            Results()
        return Results.__instance

    def __init__(self):
        """Virtually private constructor."""
        if Results.__instance != None:
            raise Exception("This class is a Results!")
        else:
            Results.__instance = self
            Results.test_results = []

    def add_result(self, result):
        self.test_results.append(result)

    def get_results(self):
        return self.test_results
