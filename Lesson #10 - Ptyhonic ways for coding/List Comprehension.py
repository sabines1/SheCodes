
a = list(range(1,20))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DOUBLE EACH ELEMENT IN THE LIST
# print([x*2 for x in a])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRINT THE WHOLE LIST
#print([x for x in a])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRINT THE EVEN NUMBERS ONLY IN THE LIST
print([ x for x in a if x%2 == 0])