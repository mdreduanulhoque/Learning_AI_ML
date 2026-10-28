"""
Q10. Ask the user for a string and print:

. All unique characters
. The count of unique characters
"""

str = input("Enter a string: ")

print("Entered String: ", str)
s = set(str)
print("Unique Character Count: ", len(s))