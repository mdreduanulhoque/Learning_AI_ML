"""
Q5. Write a function to return the sum of digits of a number, n

"""
def sum_pf_digits(n):
    sum = 0
    for i in n:
        sum += int(i)

    return sum


n = input("Enter a number: ")
sum = sum_pf_digits(n)

print("Sum of digits of", n, "is", sum)