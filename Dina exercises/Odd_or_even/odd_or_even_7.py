def user_odd_or_even():
    user_choice = ''
    while user_choice == '':
        user_choice = input('Please enter your choice "odd" or "even": ')
        while user_choice not in ('odd','even'):
            user_choice = input('Please enter your choice "odd" or "even": ')
    return user_choice

def computer_odd_or_even(user_choice):
    if user_choice == 'odd':
        computer_choice = 'even'
    else:
        computer_choice = 'odd'
    return computer_choice

def who_is_odd(_user_choice, computer_choice):
    if _user_choice == 'odd':
        odder = 'user'
        evener = 'computer'
    else:
        odder = 'computer'
        evener = 'user'
    return odder, evener

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

def sum_odd_or_even(user_num, computer_num, _odder, _evener):
    res = user_num + computer_num
    if res%2 == 0 :
        print("The sum of the num is", res)
        print("The winner is the ", _evener)
    else:
        print("The sum of the num is", res)
        print("The winner is the ", _odder)

def my_main_function():
    _user_choice = user_odd_or_even()
    computer_choice = computer_odd_or_even(_user_choice)
    print("The computer choice is: ", computer_choice)
    _odder,_evener = who_is_odd(_user_choice, computer_choice)
    user_num = user_number(_user_choice)
    computer_num = computer_number(computer_choice)
    print("The computer number is: ", computer_num)
    who_is_odd(_user_choice, computer_choice)
    sum_odd_or_even(user_num, computer_num,_odder,_evener)

if __name__ == '__main__':
    my_main_function()





