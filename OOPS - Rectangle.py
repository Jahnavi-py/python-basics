#Define a class Rectangle and calculate the perimeter and area.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length * self.width
rectangle = Rectangle(5,3)
print(f"Perimeter of rectangle is : {rectangle.perimeter()}")
print(f"Area of rectangle is : {rectangle.area()}")