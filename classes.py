import math

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first + " " + self.last

person = Person("Willian", "Cruz")
print(person.full_name())

print("---------------------------------------------------------------")

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def area(self):
        return math.pi * pow(self.radius, 2)

circle = Circle(3, "blue")
print(circle.area())

print("---------------------------------------------------------------")

class ObjectCounter:
    num_instances = 0
    def __init__(self):
        type(self).num_instances += 1

ObjectCounter()
ObjectCounter()
ObjectCounter()
counter = ObjectCounter()
print(counter.num_instances)

print("---------------------------------------------------------------")

class Animal:
    num_animals = 0
    total_animals = 0

    def __init__(self):
        type(self).num_animals += 1
        Animal.total_animals += 1

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Criando instâncias
dog1 = Dog()
cat1 = Cat()
cat2 = Cat()

print("Número total de animais:", Animal.total_animals)
print("Número total de cães:", Dog.num_animals)
print("Número total de gatos:", Cat.num_animals)

print("---------------------------------------------------------------")

class Record:
    """Hold a record of data."""

john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

john_record = Record()

for field, value in john.items():
    setattr(john_record, field, value)

john_record.name

john_record.department
