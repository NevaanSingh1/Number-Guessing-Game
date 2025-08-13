# Number Guessing Game
import random
number = random.randint(1, 10)
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > 10:
        print("The number is too high!")
    elif guess == number:
        print("You guessed it right!")
        break
    else:
        print("You guessed it wrong. Try again!")
    attempts += 1

if attempts == max_attempts and guess != number:
    print("Out of guesses! The computer chose:", number)
