# My simple Solution

movie = ['movie1', 'movie2', 'movie3']
actor = ['actor1', 'actor2', 'actor3']

#new_list = list(zip(movie, actor))

# for i in range(len(new_list)):
#     print(new_list[i][0] + " is played with actor " + new_list[i][1])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The pythonic way : FAILED
# print ((new_list[i][0] + " is played with actor " + new_list[i][1])) for i in range(len(new_list))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The pythonic way : FAILED
#((new_list[i][0] + " is played with actor " + new_list[i][1])) for i in range(len(new_list))

# THE SUGGESTED SOLUTION :
#print([m + ' is played by ' + a for (m, a) in zip(movie, actor)])

print([m + " is played by " + a for (m, a) in (zip(movie, actor))])






















