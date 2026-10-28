"""
Q3. Input two lists of integers from the user. Merge them into one list and sort the
result.

Eg - list1 = [1, 2, 7], list2 = [2, 4, 5]
result = [1, 2, 3, 4, 5, 7] 
"""

# list1 and list2 must be in same length for this solution

list1 = [1, 2, 7]
list2 = [2, 4, 5]
res = sorted(list1 + list2)

print(res)