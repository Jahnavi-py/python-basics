#Write a program to find the length of a tuple without using the len() function
my_tuple = (1, 2, 3, 4, 5)
length = 0
for _ in my_tuple:
    length += 1
print(f"Length of the tuple is: {length}")