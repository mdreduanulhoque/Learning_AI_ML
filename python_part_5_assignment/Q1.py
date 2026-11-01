"""
Q1. Create a program that:

1. Opens a file "names.txt" in write mode
2. Writes 5 names (one per line) entered by the user
3. Then opens the same file in read mode and prints all names
"""
print("Enter 'exit' to stop name inputs")

f = open("D:/AAAAAAAAAAAAAAA/Learning_AI_ML/python_part_5_assignment/names.txt", "a")
inp = ""
while(inp != "exit"):
    inp = input("Enter a name: ")
    f.writelines(inp + "\n")
f.close()

with open("D:/AAAAAAAAAAAAAAA/Learning_AI_ML/python_part_5_assignment/names.txt", "r") as Read:
    data = Read.read()
    print(data)