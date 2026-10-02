"""
Q4. The user enters a string containing a number (e.g., "45" ). Convert it to:
· an integer
· a float
· a string again
Print all three values with their types.
"""

user_input = input("Enter a number: ")

in_int = int(user_input)
in_float = float(user_input)
in_string = str(user_input)

print("Type of in_int:", type(in_int))
print("Type of in_float:", type(in_float))
print("Type of in_string:", type(in_string))
