"""
Q7. Design a program to continuously input a number n from user & print if it is
positive or negative until the user enters "Quit".
"""
print("Game start  ... ... ... ...")

i = 0
while(i < 1):
    a = input("Enter your number: ")
    if(a == "Quit"):
        break
    n = int(a)
    if(n >= 0):
        print(n, "is positive")
    else:
        print(n, "is negative")