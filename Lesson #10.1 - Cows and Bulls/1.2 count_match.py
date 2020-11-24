str1 = 'abcde'
str2 = 'acdzr'

#-------------------calculate count of matches -----------------------
def calc_match (str1, str2):
   count = 0
   for i in str1:
       # I will trace each element of str1 string
       if i in str2:  # If that I is present in str2 then enter the loop
           count = count + 1
   return(count)


print(calc_match(str1, str2))