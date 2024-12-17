#Use logical operators to check if a number is both positive and even.
num = int(input("Enter the number :"))
if num > 0 and num % 2 == 0:
    print(f"{num} is both positive and even.")
else:
    print(f"{num} is not both positive and even. ")