import math

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first + " " + self.last

person = Person("Willian", "Cruz")
print(person.full_name())

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def area(self):
        return math.pi * pow(self.radius, 2)

circle = Circle(3, "blue")
print(circle.area())

