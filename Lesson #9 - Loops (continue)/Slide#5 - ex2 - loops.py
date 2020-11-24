import random

num_computer = random.randint(1,10)
print('The computer number is: ', num_computer)
num = int(input('Please guess a number between 1 and 10: '))

def new_guess_func(num):
    while num != num_computer:
        if num < num_computer:
            print('Too low')
            num = int(input('Please try again: '))
        elif num > num_computer:
            print('Too high')
            num = int(input('Please try again: '))
    print('You win!')

new_guess_func(num)