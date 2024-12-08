age = int(input("Enter your age :"))
if age < 13:
    print("You are a child.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
elif age >=18 and age < 70:
    print("You are Adult.")
else:
    print("You are Senior.")