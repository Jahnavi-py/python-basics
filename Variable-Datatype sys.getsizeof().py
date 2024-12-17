#write a program to find the size of a variable using the sys.getsizeof() method.
import sys
my_int = 10
my_float = 20.5
my_string = "Hello, world!"
my_bool = True
print(f"Size of {my_int} : {sys.getsizeof(my_int)}", "bytes")
print(f"Size of {my_float} :{sys.getsizeof(my_float)}", "bytes")
print(f"Size of {my_string}: {sys.getsizeof(my_string)}" , "bytes")
print(f"Size of {my_bool} : {sys.getsizeof(my_bool)}" , "bytes")