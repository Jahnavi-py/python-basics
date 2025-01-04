#.Create an abstract base class Shape with methods for calculating area and perimeter. Implement it for Circle and Rectangle.
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
       pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 *(self.length + self.width)
    def area(self):
        return self.length * self.width
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def circumference(self):
        return 2 * 3.14 * self.radius
rectangle = Rectangle(5, 3)
print(f"Perimeter of rectangle is : {rectangle.perimeter()}")
print(f"Area of rectangle is : {rectangle.area()}")
circle = Circle(10)
print(f"The area of the circle is {circle.area()}")
print(f"The circumference of the circle is {circle.circumference()}")