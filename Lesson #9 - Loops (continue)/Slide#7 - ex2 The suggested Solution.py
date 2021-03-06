def valid_input(user_input):
    if user_input == "Boom":
        return True
    else:
        return user_input.isdigit()
def check_boom(user_input):
    if user_input != "Boom":
        print("GAME OVER - YOU LOSE")
    return

def seven_boom_with_user():
    for num in range(1,22):
        #Take input from the user
        x = input("Enter the next number or \"Boom\":\n")
        if not valid_input(x):
            print("GAME OVER - Invalid Input")
            return
        #Game logic
        if num % 7 == 0:
            check_boom(x)
        elif "7" in str(num):
            check_boom(x)
        else:
            if int(x) != num:
                print("GAME OVER - YOU LOSE!")
                return
    print("GAME OVER - YOU WON!")