import mytests as module_name
from mytests import MyTestSample
from rich.console import Console
from results import Results

r = Results.get_instance()
console = Console()

all_funcs = dir(module_name)
function_names = [func for func in all_funcs if func.startswith("my_test_")]
console.print(function_names)

all_objs = dir(MyTestSample)
method_names = [(str(obj)) for obj in all_objs if obj.startswith("my_test_")]
console.print(method_names)
# # Dictionary to store function names as keys and functions as values
test_dict = {}
test_class_dict = {}

# # Populate the dictionary
for func_name in function_names:
    test_dict[func_name] = module_name.__dict__[func_name]
for method_name in method_names:
    test_class_dict[method_name] = MyTestSample.__dict__[method_name]

console.print("test dict", test_dict)
console.print("test class dict", test_class_dict)
# # Now you can access and call the functions using the dictionary
for test_name, func in test_dict.items():
    print(f"\nCalling function: {test_name}")
    func()
for test_class_name, method in test_class_dict.items():
    print(f"\nCalling function: {test_class_name}")
    print(method)
    t = MyTestSample()
    t.my_test_50()

console.print("[dark_orange]Test results[/]")
console.print(r.get_results())
console.print("[green]================ Test Summary ===================[/]")
r.get_result_totals()
console.print("[green]=================================================[/]")
