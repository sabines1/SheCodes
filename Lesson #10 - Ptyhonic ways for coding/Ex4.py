# # צרי רשימה הכוללת הכפלה ב-100 של כל אחד מהמספרים 1-9 (כולל) אם הוא המתחלק ב-2 ללא שארית
# # print([ num*100 for num in range(1,10) if num%2 == 0])
#
#
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #TRANSFORM THE ABOVE LIST TO EXPRESSION WITH FILTER/REDUCE/MAP/LAMBDA
# a = list(range(1, 10))
#
# def is_even (x):
#     if x%2 == 0:
#         return(x)
#
# new_list = list(filter(is_even , a))
# print(list (map (lambda num: num*100, new_list)))

#print([num*100 for num in range(1,10) if num%2==0])

# #def multiply_by_100(x):
#     return(x*100)

def is_even(x):
    return(x%2 == 0)

#print(list(map( multiply_by_100, (filter (is_even, range(1,10))))))



print(list(map(lambda x: x*100, (filter (is_even, range(1,10))))))











