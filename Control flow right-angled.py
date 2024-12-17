#Use nested loops to generate a right-angled triangle of numbers.
rows = int(input("Enter the number of rows for the triangle: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()