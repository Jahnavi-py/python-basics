#Write a program to check if an element exists in a tuple.
my_tuple = (10, 20, 30, 40, 50)
element = int(input("Enter the element to check: "))
if element in my_tuple:
    print(f"The element {element} exists in the tuple.")
else:
    print(f"The element {element} does not exist in the tuple.")