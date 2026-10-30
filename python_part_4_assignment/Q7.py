"""
Q7. Create a class Person that allows the constructor to work with:

name only
name + age
name + age + address

As direct constructor overloading (multiple constructors) is not allowed, 
use default parameters to simulate constructor overloading.
"""


class Person:
    def __init__(self, name, age=None, address=None):
            self.name = name
            self.age = age
            self.address = address


p1 = Person("MRi")
p2 = Person("grs", 56)
p3 = Person("gsr", 40, "gsr")

print(p2.age)