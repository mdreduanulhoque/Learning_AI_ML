"""
Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3
and 5.
"""

print("Nmbers between 1 to 100, divisible by both 5 and 3")
for i in range(1, 101):
    if (i%3 == 0 and i%5 ==  0):
        print(i)