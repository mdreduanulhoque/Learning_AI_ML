# Given a list of integers compute the average of all numbers in the list.

l = [1, 2,3, 4, 5]

sum = 0
for i in l:
    sum += i

avg = sum /len(l)

print("Average of the numbers in list is", avg)