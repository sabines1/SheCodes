str1 = 'abcde'
str2 = 'acdzr'

#-------------------calculate count of bools -----------------------

def calc_bools(str1, str2):
    count_bools = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count_bools += 1
    return(count_bools)

print(calc_bools(str1, str2))