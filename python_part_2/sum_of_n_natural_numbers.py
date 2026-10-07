n = int(input("Enter the value of n: "))

sum = 0
for i in range(n+1):
    sum += i
    i+=1

print("Sum of", n, "natural numbers:", sum)