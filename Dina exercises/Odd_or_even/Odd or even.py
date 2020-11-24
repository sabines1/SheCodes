# השחקן בוחר האם הוא רוצה להיות זוג או איזוגי
# אם הסכום של המספרים זוגי - השחקן ניצח
# אחרת המחשב ניצח
# # יש לבצע וולידצייה על ה- input,
# שזה מספרים ולא אותיות

# השחקן בוחר האם הוא יהיה זוגי או אי -זוגי
player_choice = input(" Enter your choice: odd or even - for even enter 2 for odd enter 1 : ")
print("The player choice is: ", player_choice)

# המחשב הוא האופצייה השנייה
def computer_choice():
    if player_choice == '1':
        computer_select = '2'
    else:
        computer_select = '1'
    return computer_select
print("The computer choice is:", computer_choice())

# השחקן בוחר מספר זוגי או אי זוגי בהתאם לבחירה שלו לעיל

if player_choice == '1':
    player_numb = int(input("Please enter an odd number between 1-100: "))
    # while input is wrong
    while player_numb%2 == 0:
        player_numb = int(input("Please enter an odd number between 1-100: "))
else:
    player_numb = int(input("Please enter an even number between 1-100: "))
    while player_numb%2 != 0:
        player_numb = int(input("Please enter an even number between 1-100: "))
print("The player num is:", player_numb)


# המחשב מגריל מספר זוגי או אי זוגי בהתאם לבחירה של השחקן היריב לעיל
import random as rd
if computer_choice() == '1':
    computer_numb =rd.randrange(1,100,2)
else:
    computer_numb = rd.randrange(2, 100, 2)

print("The computer num is:", computer_numb)

# אם סכום המספרים זוגי - השחקן ניצח
# אם סכום המספרים אי-זוגי - המחשב ניצח
def odd_even_game(player_numb, computer_numb):
    res = player_numb + computer_numb
    if res%2 == 0:
        print("The sum of the nums is:" , res, "The EVEN won !")
    else:
        print("The sum of the nums is:" , res, "The ODD won !")

odd_even_game(player_numb, computer_numb)















