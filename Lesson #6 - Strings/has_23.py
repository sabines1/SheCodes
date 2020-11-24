# Given an int array length 2, return True if it contains a 2 or a 3.
#
# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has_23(a):
    for i in a:
        if i == 2 or i == 3:
            return True
    else:
        return False

has_23([2, 5])