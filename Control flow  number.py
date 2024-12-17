# Write a program to find whether a number is positive, negative, or zero.
def check_number(num):
    if num >0:
        return "Positive"
    elif  num < 0:
        return "Negative"
    else:
        return "Zero"
number = float(input("Enter the number : "))
result = check_number(number)
print(f"The number is {result}.")