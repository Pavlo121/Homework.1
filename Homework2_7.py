import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print("v1 + v2 =", v3)

v4 = v1 - v2
print("v1 - v2 =", v4)

dot_product = v1 * v2
print("v1 * v2 =", dot_product)

print("Довжина v1 =", v1.length())
