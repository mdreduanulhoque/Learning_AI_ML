# Write a program to swap values of two numbers entered by the user.

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

print("User input:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After swap:")
print("a =", a)
print("b = ", b)