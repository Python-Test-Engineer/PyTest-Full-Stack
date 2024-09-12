import mytests as module_name
from rich.console import Console
from results import Results

r = Results.get_instance()
console = Console()

all_funcs = dir(module_name)
console.print(all_funcs)
function_names = [func for func in all_funcs if func.startswith("test_")]
console.print(function_names)


# # Dictionary to store function names as keys and functions as values
function_dict = {}

# # Populate the dictionary
for func_name in function_names:
    # print(f"Adding function: {func_name}")
    function_dict[func_name] = module_name.__dict__[func_name]

console.print(function_dict)
# # Now you can access and call the functions using the dictionary
for test_name, func in function_dict.items():
    print(f"\nCalling function: {test_name}")
    func()

console.print("[dark_orange]Test results[/]")
console.print(r.get_results())
console.print("[green]===================================[/]")
r.get_result_totals()
console.print("[green]===================================[/]")
