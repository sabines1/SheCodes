import string as st, random as rd

def rand_str ():
   return(''.join(rd.choices(st.ascii_lowercase, k=rd.randint(5,5))))

str1 =(rand_str())
print("The computer random string is: ", str1)

str2 = input("Guess a string ( 5 characters): ")
#-------------------calculate count of bools -----------------------

def calc_bools(str1, str2):
    count_bools = 0
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

flag = False

while flag == False:
    if calc_bools(str1, str2) == len(str1):
        print ("You Won!!!")
        break
    else:
        print("You are wrong")
        print("The number of your bools is : ",calc_bools(str1, str2))
        print("The number of your hits is: ", calc_hits(str1, str2))
        str2 = input("Guess again a string ( 5 characters): ")
        flag = False