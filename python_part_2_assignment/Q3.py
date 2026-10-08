"""
Q3. Write a function that prints the digits of a number, n .

For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.

[Hint - The right most digit of a number N is N%10.

And to remove the right most digit from a number, we can do N = N / 10.]
"""

def digits_of_n(n):
    for i in n:
        print(i)

n = input("Enter a number: ")

digits_of_n(n)