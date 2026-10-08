"""
Q2. Write a function that takes two integers a and b and prints all even
numbers between them (inclusive).
"""
def print_even_in_range(s, e):
    for i in range(s, e+1):
        if(i % 2 == 0):
            print(i, "is an even number")
        i+=1


s = int(input("Enter starting number: "))
e = int(input("Enter ending number: "))

print_even_in_range(s, e)