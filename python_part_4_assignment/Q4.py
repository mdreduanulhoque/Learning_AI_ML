"""
Q4. Create a class Shape with a method area().
Create subclasses Circle, Rectangle, and Triangle that override the area() method.
"""
class Shape():
    def area(self):
        print("Area method from Shape class")

class Circle(Shape):
    def area(self):
        print("Area method from Circle class")

class Rectangle(Shape):
    def area(self):
        print("Area method from Rectangle class")

class Triangle(Shape):
    def area(self):
        print("Area method from Triangle class")

s1 = Shape()
c1 = Circle()
r1 = Rectangle()
t1 = Triangle()

s1.area()
c1.area()
r1.area()
t1.area()
