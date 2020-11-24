# Create in one line
# A dictionary with 2 lists
# with a condition

list1 = ['1','2','3','4','5']
list2 = ['a','b','c','d','e']

print({list1[x]:list2[x] for x in range(len(list2)) if x!=4})

for x in range(len(list2):
