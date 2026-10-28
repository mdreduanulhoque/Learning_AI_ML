"""
Q8. Write a program to check whether two lists share no common elements.

# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]

[Hint - use sets]

"""

list1 = [1, 2, 3, 4] 
list2 = [3, 4, 7, 8]

set_1 = set(list1)
set_2 = set(list2)

print("Set 1 and set 2 shares", len(set_1.intersection(set_2)), "common elements")