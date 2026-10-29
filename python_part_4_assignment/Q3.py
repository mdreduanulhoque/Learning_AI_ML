"""
Q3. Create a class Student with private attributes _name, _roll_no, and _marks.
Provide getter and setter methods with validation (e.g., marks cannot be
negative, roll number has to be between 1 & 100 & name cannot be empty).
"""

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name

        if(roll_no >= 1 and roll_no <= 100):
            self.__roll_no = roll_no
        else:
            print("Enter roll number between 1 to 100")
            return

        if(marks >= 0):
            self.__marks = marks
        else:
            print("Marks can not be negative")
            return

    def get_name(self):
        print("Name:", self.__name)

    def set_name(self, new_name):
        self.__name = new_name
        print("New name added")

    def get_roll_no(self):
        print("Roll Number:", self.__roll_no)

    def set_roll_no(self, new_roll):
        self.__roll_no = new_roll
        print("New roll number added")

    def get_marks(self):
        print("Marks:", self.__marks)

    def set_marks(self, new_marks):
        self.__marks = new_marks
        print("New marks added")

s1 = Student("Raib", 7, 90)

s1.set_marks(65)
s1.get_marks()

s1.set_roll_no(2)
s1.get_roll_no()
    
        