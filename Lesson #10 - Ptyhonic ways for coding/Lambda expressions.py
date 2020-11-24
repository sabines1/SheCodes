# Lambda is a kind of anonymous function
# add = lambda num1, num2 : num1 + num2
# print(add(3,6))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# result = map(lambda x:x**2  ,[1,2,4,99])
# print(list(result))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# def multiply2(x):
#     return x * 2
#
# print(list(map(multiply2, [1, 2, 3, 4])))  # Output [2, 4, 6, 8]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print(list(map(lambda x:x*2, [2,4,6,8]))) # Output [2, 4, 6, 8]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Iterating Over a Dictionary Using Map and Lambda :
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

map(lambda x: x['name'], dict_a)  # Output: ['python', 'java']

map(lambda x: x['points'] * 10, dict_a)  # Output: [100, 80]

map(lambda x: x['name'] == "python", dict_a)  # Output: [True, False]
