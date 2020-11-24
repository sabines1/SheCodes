from functools import reduce

a = list(range(1,20))

def sum(x, y):
     return(x+y)

print(reduce(sum, a))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# USING REDUCE WITH AN EMPTY LIST

# b= []
# print(reduce(sum, b, 10)) # 10 is the initial value supplied to the reduce function.