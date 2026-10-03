"""
Take a decimal number as input (like 45.78 ) and output its:

· integer part - 45
· fractional part - .78
"""

n = float(input("Enter a float number: "))

ip = int(n)
fp = n - ip

print("Integer part -", ip)
print("Fractional part -", round(fp, 2))