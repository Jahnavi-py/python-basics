x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
z = int(input("Enter the value of z : "))
if x == y == z:
    print("It is an equilateral triangle as all sides are equal.")
elif x!=y and x==z and y!=z:
    print("It is an isosceles triangle as atleast two sides are equal.")
elif x!=y!=z:
    print("It is an scalene triangle as all sides are not equal.")