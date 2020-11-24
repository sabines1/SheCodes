# my_string = 'XLIX'
#
# def convert_string_to_list (string1):
#     return([char for char in string1])
#
# mylist =(convert_string_to_list(my_string))
# print(mylist)
#
# my_new_list = []
# def convert_listofchar_to_listofint(mylist):
#     for item in mylist:
#         if item == 'M':
#             item = 1000
#             my_new_list.append(item)
#         elif item == 'D':
#             item = 500
#             my_new_list.append(item)
#         elif item == 'C':
#             item = 100
#             my_new_list.append(item)
#         elif item == 'L':
#             item = 50
#             my_new_list.append(item)
#         elif item == 'X':
#             item = 10
#             my_new_list.append(item)
#         elif item == 'V':
#             item = 5
#             my_new_list.append(item)
#         else:
#             item = 1
#             my_new_list.append(item)
#     else:
#         return(my_new_list)
#
# my_new_list = (convert_listofchar_to_listofint(mylist))
# print(my_new_list)
#
#

# my_new_list = [10, 50, 1, 10]  # [1000, 1000, 100, 100, 100, 10, 10, 1]
#
#
# def func_sum(my_new_list):
#     sum = 0




    # ~~~~~~~~~~~~~~~~~~~~~~~~IT DIDN'T WORK :
#     for i in range(len(my_new_list)):
#         print(i)
#         if len(my_new_list) > 1 and (i + 1) <= (len(my_new_list) - 1):
#             if my_new_list[i] >= my_new_list[i + 1]:
#                 sum = sum + my_new_list[i]
#             elif my_new_list[i] < my_new_list[i + 1]:
#                 sum = my_new_list[i + 1] - my_new_list[i]
#         # elif len(my_new_list) > 1 and (i+1) == (len(my_new_list)):
#
#         elif len(my_new_list) == 1:
#             return (i)
#         else:
#             return (sum)
#
# print(func_sum(my_new_list))
#~~~~~~~~~~~~~~~~~~~~~~~~~~ THE ABOVE DIDN'T WORK

my_new_list = [10, 50, 1, 10]  # [1000, 1000, 100, 100, 100, 10, 10, 1]


def func_sum(my_new_list):
    sum = 0
    for i in range(len(my_new_list)):   # 0 - 4 not included
        if my_new_list[i] > my_new_list[i+1] and (i+1) < len(my_new_list)-1 :
            sum += my_new_list[i]
        elif i == len(my_new_list)-1 :
            if my_new_list[i] > my_new_list[i-1] :
                sum = sum + (my_new_list[i] - my_new_list[i -1] )
            else :
                sum = sum + (my_new_list[i-1] - my_new_list[i])     #    NOT SURE
        else:
            sum -= my_new_list[i]

print(func_sum(my_new_list))