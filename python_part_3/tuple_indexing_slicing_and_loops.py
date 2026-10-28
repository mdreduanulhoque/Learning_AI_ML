tup = (1, 3, 2, 3,4,5,  5)

# slicing tuples is as same as list
print(tup[1:])
print(tup[:3])
print(tup[:])


# sum of elements in tuple
sum = 0
for i in tup:
    sum += i

print("sum is: ", sum)


# index(val) - provides first occurance of that value
print(tup.index(4))

# count(val) - return total occurance of that value in the tuple
print(tup.count(5))