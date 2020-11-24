# bools - matches = hits

str1 = 'abcde'
str2 = 'acdzr'

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

print(calc_hits(str1, str2))