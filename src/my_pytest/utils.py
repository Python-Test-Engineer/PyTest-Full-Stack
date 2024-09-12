from rich.console import Console

console = Console()


def color_result(actual_result, expected_result):
    if actual_result != expected_result:
        console.print("[red bold]FAILED ❌[/]")
    else:
        console.print("[green bold]PASSED ✅[/]")
        
def add_result():
    try:
        assert (
            actual_result == expected_result
        ), f"Actual result should be {expected_result}"
        r.add_result({"test_name": sys._getframe().f_code.co_name, "result": "PASSED"})
    except Exception as e:
        r.add_result({"test_name": sys._getframe().f_code.co_name, "result": "FAILED"})
        print(e)
