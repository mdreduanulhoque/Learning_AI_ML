# Using .format()

name = input("Enter your name: ")
age = input("Enter your age: ")


message = "Welcome {n} !! \nYou are {a} years old.".format(n=name, a=age)
# message = "Welcome {} !! \nYou are {} years old.".format(name, age)

print(message)