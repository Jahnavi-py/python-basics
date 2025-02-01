# Write a program to print the first 10 even numbers using a loop.
'''number = int(input("Enter the number :"))
for i in range(10):
    if number % 2 == 0:
        print(f"The first 10 even numbers are : {number}")
        number += 2
    else:
        print("The given number is not even")'''
print("The first 10 even numbers are : ")
for i in range(1, 11):
    print(i *2)
