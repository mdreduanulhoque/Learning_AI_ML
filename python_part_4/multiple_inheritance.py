class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, name, salary, gpa):
        super().__init__(salary)      # call Teacher constructor
        Student.__init__(self, gpa)   # call Student constructor
        self.name = name

ta = TA("Rahul", 50000, 7.5)
print(ta.name, ta.salary, ta.gpa)