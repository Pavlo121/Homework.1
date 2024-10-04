import math
from operator import length_hint


class Vector:
    def __init__(self, number1 , number2):
        self.number1 = number1
        self.number2 = number2


    def __add__(self, other):
        return Vector(self.number1 + other.number1, self.number2 + other.number2)


    def __sub__(self, other):
        return Vector(self.number1 - other.number1, self.number2 - other.number2)

    def __mul__(self, other):
        return Vector(self.number1 * other.number1, self.number2 * other.number2)

    def length(self):
        return math.sqrt(self.number1**2 +  self.number2**2)

    def __lt__(self, other):
        return self.length() < other.length()

    def __eq__(self, other):
        return self.length() == other.length()

    def __repr__(self):
        return f"Vector({self.number1}, {self.number2})"

a1 = Vector(3,4)
a2 = Vector(1, 2)
a3 = a1 + a2
a4 = a1 - a2
a5 = a1 * a2

length_a1 = a1.length()
length_a2 = a2.length()

is_a1_shorter = a1 < a2
is_a2_shorter = a2 == a1

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(f"Длина a1: {length_a1}")
print(f"Ддина a2: {length_a2}")
print(f"a1 < a2: {is_a1_shorter}")
print(f"a1 == a2: {is_a2_shorter}")