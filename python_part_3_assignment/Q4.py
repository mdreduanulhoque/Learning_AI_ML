"""

Q4. Given a tuple of integers, create:
. A tuple of all even numbers
. A tuple of all odd numbers
"""
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

tup_odd = tup[::2]
print(tup_odd)

tup_even = tup[1::2]
print(tup_even)