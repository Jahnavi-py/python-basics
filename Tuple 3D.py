#Use a tuple to store coordinates of a point in 3D space and calculate the distance from the origin.
import math
point = (3, 4, 12)
x, y, z = point
distance = math.sqrt(x**2 + y**2 + z**2)
print(f"The distance from the origin to the point {point} is {distance}")