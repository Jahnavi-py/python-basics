#Create a program that demonstrates the immutability of tuples.
my_tuple = ([1, 2, 3], "hello")
my_tuple[0].append(4)
print(f"The immutability of tuples is {my_tuple}")