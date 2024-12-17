#Use the isinstance() function to check the data type of a variable.
my_int = 10
my_float = 10.5
my_str = "Hello, World!"
my_bool = True
if isinstance(my_int, int):
    print(f"The type of my_int {my_int} variable is an integer")
if isinstance(my_float, float):
    print(f"The type of my_float {my_float} variable is a float")
if isinstance(my_str, str):
    print(f"The type of my_str {my_str} variable is a string")
if isinstance(my_bool, bool):
    print(f"The type of my_bool {my_bool} variable is a boolean")