# list[start : end : step]   end is not included; step is default 1

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list_[2:5])
print(list_[:4])
print(list_[:])

print(list_[::2])
print(list_[1::3])

#using negative indexing
print(list_[-5:-2])