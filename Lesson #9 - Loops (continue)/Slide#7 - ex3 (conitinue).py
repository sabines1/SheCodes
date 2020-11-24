for i in range(1,21):
    num = input("Next number: ")
    if i%7 == 0:
        if num == 'Boom':
            print('OK1')
        else:
            print('NOK1 - you were supposed to enter "Boom"')
    elif int(num )== i:
        print('OK2')
    else:
        print('You are wrong')
        break

