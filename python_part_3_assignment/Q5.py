"""
Q5. Create a dictionary where:

· Keys = student names

· Values = marks (integer)

Write a menu-based program where user presses a key ('A', 'B', 'C', 'D')
depending on the operation they want to perform on the dictionary:

A - Add a student
B - Update marks
C - Search for a student
D - Display all students and marks

"""
def add_student(name, mark):
    result[name] = mark
    print("Student Marks Added")

def update_mark(name, mark):
    result[name] = mark
    print("Mark Upgraded")

def search(name):
    print("Marks of", name, "is", result.get(name))

def display():
    print(result)

result = {
    "name" : "Rakib",
    "marks" : 67
}


print("Welcome TO Result Management System")
print("A - Add a student")
print("B - Update marks")
print("C - Search for a student")
print("D - Display all students and marks")
print("Q - Exit")

while(True):
    inp = input("Enter your choice: ")
    if(inp == "A"): 
        n = input("Enter Student's Name: ")
        m = input("Enter Student's Marks: ")
        add_student(name=n, mark=m)
    elif(inp == "B"):   
        n = input("Enter Student's Name: ")
        m = input("Enter Student's Marks: ")
        update_mark(name=n, mark=m)
    elif(inp == "C"):
        n = input("Enter Student's Name: ")
        search(name=n)
    elif(inp == "D"):
        display()
    elif(inp == "Q"):
        break;