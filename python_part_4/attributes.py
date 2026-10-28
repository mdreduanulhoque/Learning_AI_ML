# attributes are variables of class which later assignes to the objects

class student:
    university = "UIU"  # will be same for all objects

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

s1 = student("Rakib" ,3.25)
s2 = student("Plni", 1.65)

print(s1.university)
print(s2.university)
print(student.university)  # initialized attributes can be accessed by class name

print(s1.name)
print(s2.cgpa)