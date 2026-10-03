"""
Take the radius (r) as user input and print the area.
Use the formula:
Area = PI * r^2
(value of PT = 3.14)
"""
PI = 3.14
r = float(input("Enter the value of radius: "))

Area = PI * pow(r, 2)

print("Area = ", Area)