# write a function that receives a list of strings
# and return a list of the strings in which the first char is equal to the last char

new_list = []

def function1 (list1):
    for i in range (len(list1)):
        if list1[i][0] == list1[i][-1]:
            new_list.append(list1[i])
    return new_list

list1 = ['aba','bb','abc']
print(function1(list1))