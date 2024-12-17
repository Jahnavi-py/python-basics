#Use nested loops to print a multiplication table for numbers 1 through 5.
for i in range(1,6):
    for j in range(1,6):
        print(f"{i * j}", end="\t")
    print()