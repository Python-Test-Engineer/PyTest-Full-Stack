from rich.console import Console

console = Console()


class Results:
    __instance = None

    @staticmethod
    def get_instance():
        """Static access method."""
        if Results.__instance is None:
            Results()
        return Results.__instance

    def __init__(self):
        """Virtually private constructor."""
        if Results.__instance is not None:
            raise Exception("This class is a Results!")
        else:
            Results.__instance = self
            Results.test_results = []

    def add_result(self, result):
        self.test_results.append(result)

    def get_results(self):
        return self.test_results

    def get_result_totals(self):
        num_tests = len(self.test_results)
        console.print(f"[dark_orange]Total tests: {num_tests}[/]")
        num_passed = 0
        num_failed = 0
        for result in self.test_results:
            for k, v in result.items():
                # console.print(f"[dark_orange]{k}: {v}[/]")
                if k == "test_result" and v == "PASSED":
                    num_passed += 1
                if k == "test_result" and v == "FAILED":
                    num_failed += 1
        console.print(f"[green]Passed: {num_passed}[/]")
        console.print(f"[red]Failed: {num_failed}[/]")
