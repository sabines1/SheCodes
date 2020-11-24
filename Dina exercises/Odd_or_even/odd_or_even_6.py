def user_odd_or_even(user_choice):
    while user_choice == '':
        user_choice = input('Please enter your choice "odd" or "even": ')
    return user_choice

def computer_odd_or_even(user_choice):
    if user_choice == 'odd':
        computer_choice = 'even'
    else:
        computer_choice = 'odd'
    return computer_choice

def user_number(user_choice):
    if user_choice == 'odd':
        user_num = int(input ("Please enter an odd number between 1-100: "))
        while user_num%2 == 0:
            user_num = int(input("Please enter an odd number between 1-100: "))
    else:
        user_num = int(input("Please enter an even number between 1-100: "))
        while user_num % 2 != 0:
            user_num = int(input("Please enter an even number between 1-100: "))
    return user_num

def computer_number(computer_choice):
    from random import randrange
    if computer_choice == 'odd':
        computer_num = randrange(1,100,2)
    else:
        computer_num = randrange(2,100,2)
    return computer_num

def sum_odd_or_even(user_num, computer_num):
    res = user_num + computer_num
    if res%2 == 0 :
        print("The sum of the num is", res)
        print("The EVEN player won !!!")
    else:
        print("The sum of the num is", res)
        print("The ODD player won")


def main_func():
    user_choice = ''
    user_choice = user_odd_or_even(user_choice)
    computer_choice = computer_odd_or_even(user_choice)
    print("The computer choice is: ", computer_choice)
    user_num = user_number(user_choice)
    print("The user number is : ", user_num)
    computer_num = computer_number(computer_choice)
    print("The computer number is: ", computer_num)
    sum_odd_or_even(user_num, computer_num)

print(main_func())



