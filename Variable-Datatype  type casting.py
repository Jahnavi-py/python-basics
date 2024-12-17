#Write a program to demonstrate type casting between int, float, and str.
my_int = 10
my_float = 20.5
my_string = "30"
int_to_float = float(my_int)
print(f"Integer to Float: {int_to_float} ({type(int_to_float)})")
float_to_int = int(my_float)
print(f"Float to Integer: {float_to_int} ({type(float_to_int)})")
string_to_int = int(my_string)
print(f"String to Integer: {string_to_int} ({type(string_to_int)})")
string_to_float = float(my_string)
print(f"String to Float: {string_to_float} ({type(string_to_float)})")
float_to_string = str(my_float)
print(f"Float to String: {float_to_string} ({type(float_to_string)})")
int_to_string = str(my_int)
print(f"Integer to String: {int_to_string} ({type(int_to_string)})")