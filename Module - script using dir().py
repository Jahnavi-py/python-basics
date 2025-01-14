#Write a script that lists all the attributes and methods of the os module using the dir() function.
import os
os_attributes = dir(os)
print(f"Attributes and Methods in the os module:")
print(os_attributes)