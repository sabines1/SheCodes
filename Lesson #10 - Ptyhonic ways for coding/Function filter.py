# a =list(range(1,20))
#
# def is_even(x):
#     return x%2 == 0
#
# #print(is_even(2))
#
# print(list(filter(is_even, a)))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a = [1, 2, 3, 4, 5, 6]
# print(list(filter(lambda x : x % 2 == 0, a))) # Output: [2, 4, 6]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Filter list of dictionaries
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

print(list(filter(lambda x : x['name'] == 'python', dict_a))) # Output: [{'name': 'python', 'points': 10}]