# השחקן בוחר האם הוא רוצה להיות זוג או איזוגי
# אם הסכום של המספרים זוגי - השחקן ניצח
# אחרת המחשב ניצח
# # יש לבצע וולידצייה על ה- input,
# שזה מספרים ולא אותיות


# השחקן בוחר האם הוא יהיה זוגי או אי -זוגי


def player_input(player_choice):
    while player_choice == '':
        player_choice = input(" Enter your choice: odd or even : ")
    return player_choice

def computer_input(xplayer_input):
    if xplayer_input == 'odd':
        computer_choice = 'even'
    else:
        computer_choice = 'odd'
    return computer_choice


# השחקן בוחר מספר זוגי או אי זוגי בהתאם לבחירה שלו לעיל
def player_choose_number(player_numb, xplayer_input):
    while player_numb == 0:
        if xplayer_input == 'odd':
            player_numb = int(input("Please enter an odd number between 1-100: "))
            # while input is wrong
            while player_numb%2 == 0:
                player_numb = int(input("Please enter an odd number between 1-100: "))
        else:
            player_numb = int(input("Please enter an even number between 1-100: "))
            while player_numb%2 != 0:
                player_numb = int(input("Please enter an even number between 1-100: "))
    #print("The player num is:", player_numb)
    return player_numb


# המחשב מגריל מספר זוגי או אי זוגי בהתאם לבחירה של השחקן היריב לעיל
def computer_choose_number(xplayer_input):
    import random as rd
    if xplayer_input == 'odd':
        computer_numb =rd.randrange(2,100,2)
    else:
        computer_numb = rd.randrange(1, 100, 2)

    #print("The computer num is:", computer_numb)
    return computer_numb



# אם סכום המספרים זוגי - השחקן ניצח
# אם סכום המספרים אי-זוגי - המחשב ניצח
def odd_even_game(xplayer_numb, xcomputer_numb):
    res = xplayer_numb + xcomputer_numb
    if res%2 == 0:
        print("The sum of the nums is:" , res, "The EVEN player won !")
    else:
        print("The sum of the nums is:" , res, "The ODD player won !")

def func_main():
    player_choice = ''
    player_input(player_choice)
    xplayer_input = player_input(player_choice)
    computer_input(xplayer_input)
    xcomputer_input = computer_input(xplayer_input)
    player_numb = 0
    player_choose_number(player_numb, xplayer_input)
    xplayer_numb = player_choose_number(player_numb, xplayer_input)
    computer_choose_number(xplayer_input)
    xcomputer_numb = computer_choose_number(xplayer_input)
    print('The Computer number is: ', xcomputer_numb)

    odd_even_game(xplayer_numb, xcomputer_numb)

func_main()













