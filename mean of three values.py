a = float(input("Enter the number for a : "))
b = float(input("Enter the number for b : "))
c = float(input("Enter the number for c : "))
if a > b:
    if a < c:
        mean = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if  a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
print("The median of three values is : ", median)