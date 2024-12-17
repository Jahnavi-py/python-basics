#Write a program to swap two numbers using the XOR operator.
a = 30
b = 10
print("Before Swapping a:", a)
print("Before Swapping b:",b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping a:", a)
print("After swapping b:", b)