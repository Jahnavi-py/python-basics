#Write a program to check if a number is an integer or a float.
def check_number_type(num):
    if isinstance(num, int):
        return "Integer"
    elif isinstance(num, float):
        return "Float"
    else:
        return "Not a number"
number = 10
print(f"the given number {number} is {check_number_type(number)}")
number = 3.14
print(f"the given number {number} is {check_number_type(number)}")
number = "hello"
print(f"the given number {number} is {check_number_type(number)}")