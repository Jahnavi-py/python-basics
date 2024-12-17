#Check the memory size of an integer and a float using sys.getsizeof().
import sys
integer = 4
float = 0.5
print(f"The memory size of integer {integer} is : {sys.getsizeof(integer)}", "bytes")
print(f"The memory size of float is {float} : {sys.getsizeof(float)}", "bytes")
