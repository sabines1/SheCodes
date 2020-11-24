# Given 2 arrays of ints, a and b,
# return True if they have the same first element or they have the same last element.
# Both arrays will be length 1 or more.


# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(l1, l2):
    if ((l1[0] == l2[0]) or (l1[-1]==l2[-1])):
        #return True
        print('True')
    else:
        #return False
        print ('False')

l1 = [1,2,3,4,8]
l2 = [2,3,8]

common_end (l1, l2)