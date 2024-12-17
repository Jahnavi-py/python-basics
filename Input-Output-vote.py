#Write a program to take user input for their age and display whether they are eligible to vote (18+).
age = int(input("Enter your age:"))
if age >= 18:
    print("Your eligible to vote.")
else:
    print("your not eligible to vote.")