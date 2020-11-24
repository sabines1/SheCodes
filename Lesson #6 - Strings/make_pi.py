#  make_pi
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
#
# make_pi() → [3, 1, 4]

# My bad solution :
# def make_pi():
#     pi = (str(3.14))
#     l = [pi[0], pi[2], pi[3]]
#     print (l)
#
# make_pi()

#Google solution :
import math


def make_pi():
    arr = []
    num = int(math.pi * 100)
    arr1 = []

    # Append the array with
    while num > 0:
        arr.append(num % 10)
        num = int(num / 10)

    # Reverse the array
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print(arr)


make_pi()