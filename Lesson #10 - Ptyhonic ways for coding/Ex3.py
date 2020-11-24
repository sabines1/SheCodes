movie = ['movie1', 'movie2', 'movie3']
actor = ['actor1', 'actor2', 'actor3']

movies = {m:a for (m,a) in zip (movie, actor)}
#print(movies)
# Output :
# {'movie1': 'actor1', 'movie2': 'actor2', 'movie3': 'actor3'}
# EX3 : convert the dictionary "movies" to the list below
# ['movie1 is played by actor1', 'movie2 is played by actor2', 'movie3 is played by actor3']

#print([m + ' is played by ' + a  for (m, a) in (movies.items())])

print([m + ' is played by ' + a for (m,a) in (movies.items())])






















