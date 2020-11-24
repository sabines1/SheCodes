import string as st, random as rd

def rand_str ():
   return(''.join(rd.choices(st.ascii_lowercase, k=rd.randint(5,5))))

str1 =(rand_str())
print("The computer random string is: ", str1)

str2 = input("Guess a string ( 5 characters): ")



#-------------------Verifications on the input --------------------
def input_verifications (str2):
    while len(str2) != 5:
        if len(str2) > 5:
            str2 = input("The string you've entered is too long. Please enter a 5 characters string: ")
        elif len(str2) < 5:
            str2 = input("The string you've entered is too short. Please enter a 5 characters string: ")
        elif len(str2) == 0:
            str2 = input("We are waiting for your input.Please enter a 5 characters string: ")
        else:
            break
input_verifications (str2)



#-------------------calculate count of bools -----------------------

def calc_bools(str1, str2):
    count_bools = 0
    input_verifications(str2)
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count_bools += 1
    return(count_bools)

#print("The number of bools is : ",calc_bools(str1, str2))

#-------------------calculate count of hits -----------------------
# bools - matches = hits

def calc_bools(str1, str2):
    count_bools = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count_bools += 1
    return(count_bools)

def calc_match (str1, str2):
   count = 0
   for i in str1:
       if i in str2:
           count = count + 1
   return(count)

def calc_hits(str1, str2):
    return(calc_match(str1, str2) - calc_bools(str1, str2))

#print("The number of hits is: ", calc_hits(str1, str2))

#-------------------------------THE GAME ------------------------------------------

def func_game(str1, str2):
    flag = False

    while flag == False:
        if calc_bools(str1, str2) == len(str1):
            print ("You Won!!!")
            break
        else:
            print("You are wrong")
            input_verifications(str2)
            print("The number of your bools is : ",calc_bools(str1, str2))
            print("The number of your hits is: ", calc_hits(str1, str2))
            str2 = input("Guess again a string ( 5 characters): ")
            input_verifications(str2)
            flag = False

func_game(str1, str2)