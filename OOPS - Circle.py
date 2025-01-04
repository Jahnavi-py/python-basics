#Write a class Circle with a method to calculate the area and circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def circumference(self):
        return 2 * 3.14 * self.radius
circle = Circle(10)
print(f"The area of the circle is {circle.area()}")
print(f"The circumference of the circle is {circle.circumference()}")