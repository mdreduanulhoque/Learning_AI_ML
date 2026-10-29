
class student():
    section = "A"
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def display(self):          # instance methods
        print(f"Name = {self.name}    CGPA = {self.cgpa}    Seection = {self.section}")

    @classmethod
    def change_section(cls, section_new):         # class methods
        cls.section = section_new

    @staticmethod
    def sum_(a, b):          #static Methos
        print(f"Sum of {a} and {b} is {a+b}")

s1 = student("Rakib", 3.21)
s1.display()

s1.change_section("B")
s1.display()

s1.sum_(4,9)