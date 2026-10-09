"""
Q10. Let's create a "Number Guessing Game". Given a secret number (already
decided by you), write a program that asks the user to guess it and prints:

"Too high"      if the guess is above the number

"Too low"       if the guess is below

"Correct!"      if the guess matches

"""

a = 7
n = 0
while( a != n):
    n = int(input("Enter your guess: "))
    if(n > a):
        print("Guess low")
    if(n < a):
        print("Guess high")

print("Correct")