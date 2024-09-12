from rich.console import Console
from results import Results

r = Results.get_instance()
console = Console()


def color_result(actual_result, expected_result):
    if actual_result != expected_result:
        console.print("[red bold]FAILED ❌[/]")
    else:
        console.print("[green bold]PASSED ✅[/]")


def store_result(test_name, actual_result, expected_result, test_message=None):
    try:
        assert (
            actual_result == expected_result
        ), f"Actual result should be {expected_result}"
        r.add_result(
            {
                "test_name": test_name,
                "test_result": "PASSED",
                "test_message": test_message,
            }
        )
    except Exception as e:
        r.add_result(
            {"test_name": test_name, "test_result": "FAILED", "test_message": str(e)}
        )
        print(e)
