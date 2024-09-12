import mytests as module_name


all_funcs = dir(module_name)
# print(all_funcs)
function_names = [func for func in all_funcs if func.startswith("test_")]
# print(function_names)


# # Dictionary to store function names as keys and functions as values
function_dict = {}

# # Populate the dictionary
for func_name in function_names:
    # print(f"Adding function: {func_name}")
    function_dict[func_name] = module_name.__dict__[func_name]

print(function_dict)
# # Now you can access and call the functions using the dictionary
for test_name, func in function_dict.items():
    print(f"\nCalling function: {test_name}")
    func()
