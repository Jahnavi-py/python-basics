#Write a program to check if all elements in a tuple are the same
my_tuple = (4,4,4,4,4)
all_same = all(element == my_tuple[0] for element in my_tuple)
print(f"Are all elements the same? {all_same}")