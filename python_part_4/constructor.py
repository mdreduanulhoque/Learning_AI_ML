# Default constructor

class student:
    def __init__(self):
        print("Dfault Initializer Classed")
s1 = student()

# Parameterized Constructor

class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
c1 = car("R3UIB", "RED")
c2 = car("PE85BH", "PURPLE")

print(c1.color)
print(c2.name)