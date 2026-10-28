"""
Q9. Given a list, print all elements that appear more than once in the list.
[Hint - use sets]
"""

li = [0, 1, 2, 23, 44, 65, 65, 7, 8, 44, 89, 0]

li = sorted(li)

for i in range(1, len(li)):
    if(li[i] == li[i-1]):
        print(li[i])