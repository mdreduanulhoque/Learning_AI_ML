"""
Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and
compute simple interest:
SI=(P*R*T)/100
"""

P = float(input("Enter the value of principal amount: "))
R = float(input("ENter the value of rate of interest: "))
T = float(input("Enter the value fo time duration: "))

SI=(P*R*T)/100

print("Simple interest amount:", SI)