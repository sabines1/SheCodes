# zip takes n number of iterables and returns a list of tuples.
# the ith element of the tuple is created using the ith element from each of the iterables.

list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = list(zip(list_a, list_b))

print (zipped_list) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]