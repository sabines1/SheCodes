#
# list1 =[]
# list1.append(2)
# print(list1)


# L = ['red', 'green', 'blue']
# L.append('yellow')
# print(L)
###########################################
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.keys()
#
# print(x)
###############################################
# Rot13 = ''
# alphabit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# message = 'Ayelet'
# for i in message:
#     Rot13 = Rot13 + alphabit[alphabit.index(i) + 13]
#
# print(Rot13)
#####################################
# def rot13_encode(a ):
#     Rot13=''
#     alphabit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for i in message:
#         if i in alphabit:
#             Rot13 += alphabit[alphabit.index(i) + 13]
#         else:
#             Rot13 += i
#     return Rot13
#
# rot13_encode('sabine')

######################################
# def rot13_decode(message ):
#     Rot13=''
#     alphabit = 'nopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
#     for i in message:
#         if i in alphabit:
#             Rot13 += alphabit[alphabit.index(i) + 13]
#         else:
#             Rot13 += i
#     return Rot13
#
# print(rot13_decode('Fnovar'))
#------------------------------------------
# def double_list(x):
#   for i in range(0, 3):
#     x[i] = x[i] * 2
#     return (x)
# # Don't forget to return your new list!
#
# print(double_list([1,2,3]))

#-----------------------------------------------
# board= []
# for item in range(5):
#   board.append(['O']*5)
#   print(''.join(str(board)))
#------------------------------------------
# s = '******'
# print(s.replace('*', '', 1))
#----------------------------------------
count = 0
for i in range(10):
      print('doing some stuff')
      count +=1