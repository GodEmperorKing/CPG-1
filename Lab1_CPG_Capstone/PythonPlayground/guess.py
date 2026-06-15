# guess.py
# A fun guessing game! Can you guess the secret number?
# Uses random numbers and simple if/else logic.

import random

print("I am thinking of a number between 1 and 5.")
print("Can you guess what it is?")

secret_number = random.randint(1, 5)

guess = input("Type your guess (1, 2, 3, 4, or 5) and press Enter: ")

if int(guess) == secret_number:
    print("Wow! You guessed it! You are amazing!")
else:
    print("Not quite. The secret number was " + str(secret_number) + ".")
    print("Better luck next time! Try running the program again.")