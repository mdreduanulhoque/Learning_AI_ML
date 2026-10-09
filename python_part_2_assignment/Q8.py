"""
Q8. Let's create a Simple Calculator that performs arithmetic operations. Create
a function calculator(a, b, operation) that performs addition, subtraction,
multiplication, or division based on the operation parameter.
"""

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "wrong opeator input"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter opration (+, -, *, /): ")

res = calculator(a,b,op)
print(res)