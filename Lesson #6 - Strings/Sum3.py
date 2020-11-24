# Given an array of ints length 3,
# return the sum of all the elements.
#
#
# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7

def sum3(l1):
    sum = 0
    for i in l1:
        sum = sum + i
    print('The sum of the 3 elements in the list is : ', sum)

l1=[5,11,2]
sum3(l1)