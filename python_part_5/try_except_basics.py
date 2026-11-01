
try:
    x = (10/0)
except:
    print("Error Occured")



try:
    print(10/0)
except ZeroDivisionError:
    print("You can n ot divide by zero")

