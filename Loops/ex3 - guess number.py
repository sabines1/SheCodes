# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct,
# on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random
num =(random.randint(1, 9))
print('The computer num is ', num)

guess = input("Please enter a number between 1 and 9 : ")


while int(guess) != num:
    print("Try again")
    guess = input("Please enter a number between 1 and 9 : ")
else:
    print("Well guessed")
print("Finished")


