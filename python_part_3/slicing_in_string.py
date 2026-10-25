# slicing = str[starting index : ending index]    ending is not included
str = "HI, I am here"
print(str[6:8])

# str[: ending index+1]  default starting index is 0
# str[starting index :]  default ending index is end of string
# str[:]  default starting index is 0 & ending index is end of string

"""
Negative indexing

str = "Hello World"
    H    e    l    l    o         W    o    r    l    d
  -11   -10  -9   -8   -7   -6   -5   -4   -3   -2   -1      
"""

stri = "Hello World"
print(stri[-8:-3])