######################## W R O N G    S O L U T I O N ######################################

is_computer = 0

#The computer

for i in range(1,21):
    if is_computer == 0:
        if i%7 == 0:
            print('Boom')
        else:
            print(i)
        is_computer = 1
    else:
#The player
        num = input("Next number: ")
        if i%7 == 0:
            if num == 'Boom':
                print('OK1')
            else:
                print('NOK1 - you were supposed to enter "Boom"')
        elif num.isdigit()== i:
            print('OK2')
        else:
            print('You are wrong')
            break
            is_computer = 0
        is_computer = 0