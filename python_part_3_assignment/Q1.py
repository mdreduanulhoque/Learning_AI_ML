"""
Q1. Ask the user for a string and check whether it is a palindrome or not.
A palindrome is a string which is same when we read it forward & backward. Eg -
"madam", "racecar" etc.

[Hint - A palindrome string is equal to the reversed version of the string. We can
use a loop to reverse the string manually. ]
"""

str = input("Enter your word: ")

if len(str)%2 == 0:
    s1 = str[:(len(str)/2)]
    s2 = str[(len(str)/2):]
    if(s1 == s2):
        print(str, "is a palendrome")
    else:
        print(str, "is not a palendrome")
else:
    s1 = str[:int((len(str)/2))]
    s2 = str[int((len(str)/2))+1:]
    if(s1 == s2):
        print(str, "is a palendrome")
    else:
        print(str, "is not a palendrome")