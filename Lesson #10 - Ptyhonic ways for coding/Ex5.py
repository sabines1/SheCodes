# # צרי רשימה הכוללת הכפלה ב-100 של כל אחד מהמספרים 1-9 (כולל) אם הוא המתחלק ב-2 ללא שארית
# # אם יש שארית, אז השאירי את המספר מבלי להכפיל אותו ב-100
# print([num*100 if num%2 == 0 else num for num in range(1,10)])
#
#
# # writing the same as above but with map/lambda/filter/reduce
# a = list(range(1, 10))
# b= []
#
# def is_even (x):
#     if x%2 == 0:
#         x*100
#         b.append(x)
#     else:
#         b.append(x)
#     return (b)
#
# print(list (map(is_even, a)))

#print([num*100 if num%2==0 else num for num in range(1,10) ])

print(list(map(lambda x:x*100 if x%2==0 else x, range(1,10))))














