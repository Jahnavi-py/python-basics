#Write a program to check if a number is divisible by both 3 and 5.
num = int(input("Enter the number : "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
elif num % 3 == 0:
    print("The number is divisible by 3 and not divisible by 5.")
elif num % 5 == 0:
    print("The number is divisible by 5 and not divisible by 3.")
else:
    print("The number is not divisible by both 3 and 5 ")