# Task 5
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # To check if two points are equal  
    def __eq__(self, other):
      return self.x == other.x and self.y == other.y

    # Return string representation of the point          
    def __str__(self):
        return f"point(x={self.x}, y={self.y})"
    
    # Calculate Euclidean distance between two points
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
            

# Vector class inherits from Point
class Vector(Point):
    def __init__(self, x, y):
        # Call parent class constructor
        super().__init__(x, y)
        
    # Override string representation method
    def __str__(self):
        return f"vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        vector_x = self.x + other.x
        vector_y = self.y + other.y
        return Vector(vector_x , vector_y)

p1 = Point(5, 6)
print(p1)
p2 = Point(2, 4)
print(p2)
print(p1 == p2)
print(p1.distance(p2))

v1 = Vector(4, 4)
print(v1)
v2 = Vector(1, 2)
print(v2)
print(v1 == v2)
print(v1 + v2)      