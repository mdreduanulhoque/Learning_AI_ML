"""
Q7. Write a program that takes a string from the user and prints the number of
spaces in the string.

"""

str = input("ENter a string: ")

spaces = 0
for s in str:
    if(s == " "):
        spaces+=1

print("The word", str, "has", spaces, "spaces.")