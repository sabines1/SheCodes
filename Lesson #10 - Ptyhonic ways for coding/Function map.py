# a = list(range(1,20))
#
# def double(x):
#      return(x*2)
#
# print(list(map(double, a)))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Multiple Iterables to the Map Function

list_a = [1, 2, 3]
list_b = [10, 20, 30]

print(list(map(lambda x, y: x + y, list_a, list_b)))  # Output: [11, 22, 33]


