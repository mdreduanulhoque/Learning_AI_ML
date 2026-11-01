# Basic syntex:
# [expression for item in iterable]

nums = [x for x in range(1, 6)]
print(nums)

# list comprehansion with condition
# [expression for item in iterable if condition]

n = [x for x in range(1, 14) if x%2 == 0]
print(n)