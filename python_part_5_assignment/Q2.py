"""
Q2. Create a program that:

1. Opens a file "log.txt" in append mode
2. Adds a new log entry (like "Program run successfully")
3. Opens the file in read mode and prints all logs
"""

with open("D:/AAAAAAAAAAAAAAA/Learning_AI_ML/python_part_5_assignment/log.txt", "a") as f:
    f.writelines("Program run successfully\n")

with open("D:/AAAAAAAAAAAAAAA/Learning_AI_ML/python_part_5_assignment/log.txt", "r") as k:
    data = k.read()
    print(data)