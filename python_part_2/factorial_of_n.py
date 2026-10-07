
n = int(input("Enter value of n: "))

fac = 1
for i in range(1,n+1):
    fac *= i
    i+=1

print("Factorial of", n , "is", fac)