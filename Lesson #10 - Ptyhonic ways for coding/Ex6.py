# # כתבי קוד שמייצר רשימה של 7" בום" למספרים מ-1-99
# print([ num if num%7 != 0 else 'Boom' for num in range(1,100)])



#print([num if num%7 !=0 else "Boom" for num in range(1,100) ])

print(list(map(lambda num:num if num%7 !=0 else "Boom", range(1,100))))














