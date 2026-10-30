"""
Q6. Create an abstract class Employee with an abstract method calculate_salary().
Create subclasses Intern, FullTimeEmployee, and 
ContractEmployee that implement the method differently.
"""
from abc import ABC, abstractmethod

class Employee:
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("Print from Intern Class")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Print from FullTimeEmployee")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Print from ContractEmployee")

i1 = Intern()
f1 = FullTimeEmployee()
c1 = ContractEmployee()

i1.calculate_salary()
f1.calculate_salary()
c1.calculate_salary()