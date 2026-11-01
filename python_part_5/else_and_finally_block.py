# else block executes when no exception found
# finally block will be executed anyhow, it does not matter u found exception or not

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", x)
finally:
    print("Execution Done")
    

