#Create a program that uses the break statement to exit a loop early
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
for num in numbers:
    if num == target:
        print(f"Found target: {target}!")
        break
    print(f"Checking {num}...")
print("Loop terminated.")
