# השחקן בוחר האם הוא רוצה להיות זוג או איזוגי
# אם הסכום של המספרים זוגי - השחקן ניצח
# אחרת המחשב ניצח
# # יש לבצע וולידצייה על ה- input,
# שזה מספרים ולא אותיות


# השחקן בוחר האם הוא יהיה זוגי או אי -זוגי
def player_and_computer_input():
    player_choice = input(" Enter your choice: odd or even : ")
    #print("The player choice is: ", player_choice)
    if player_choice == 'odd':
        computer_select = 'even'
    else:
        computer_select = 'odd'
    print("The computer choice is:", computer_select)
    return computer_select,player_choice


# השחקן בוחר מספר זוגי או אי זוגי בהתאם לבחירה שלו לעיל
def player_choose_number(player_choice):
    if player_choice == 'odd':
        player_numb = int(input("Please enter an odd number between 1-100: "))
        # while input is wrong
        while player_numb%2 == 0:
            player_numb = int(input("Please enter an odd number between 1-100: "))
    else:
        player_numb = int(input("Please enter an even number between 1-100: "))
        while player_numb%2 != 0:
            player_numb = int(input("Please enter an even number between 1-100: "))
    print("The player num is:", player_numb)
    return player_numb


# המחשב מגריל מספר זוגי או אי זוגי בהתאם לבחירה של השחקן היריב לעיל
def computer_choose_number(computer_input):
    import random as rd
    if computer_input== 'odd':
        computer_numb =rd.randrange(1,100,2)
    else:
        computer_numb = rd.randrange(2, 100, 2)

    print("The computer num is:", computer_numb)
    return computer_numb

# אם סכום המספרים זוגי - השחקן ניצח
# אם סכום המספרים אי-זוגי - המחשב ניצח
def odd_even_game(player_numb, computer_numb):
    res = player_numb + computer_numb
    if res%2 == 0:
        print("The sum of the nums is:" , res, "The EVEN player won !")
    else:
        print("The sum of the nums is:" , res, "The ODD player won !")

def func_main():
    computer_choice,player_choice=player_and_computer_input()
    player_numb=player_choose_number(player_choice)
    computer_numb=computer_choose_number(computer_choice)
    odd_even_game(player_numb, computer_numb)

func_main()


