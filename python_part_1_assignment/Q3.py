"""
Ask the user to enter two integers and one float. Convert them all to floats
and print their average.
"""

num1 = float(input("Enter first integer: "))
num2 = float(input("Enter second integer: "))
num3 = float(input("Enter a float number: "))

avg = (num1 + num2 + num3)/3

print("Average:", avg)