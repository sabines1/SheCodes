# 4. Write a Python program to construct the following pattern, using a nested for loop.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# MY UNFINISHED SOLUTION :
# pat = '*'
# for item in range(9):
#     for num in range (9):
#         if num <= 4 and len(pat) <= 5:
#             print (pat)
#             pat = pat +'*'
#         elif num > 4 and len(pat)== 6:
#             pat = pat.replace('*', '', num - 1)
#             print(pat)

# THE SUGGESTED SOLUTION :
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

# Dikla Kupperman solution
def rhombus(n):
    half = int(n/2)
    for i in range (1, n):
        if i < n/2 :
            print (((' ')*(half-i)) + (('*')*i))
        elif i== half:
            print('*'*i)
        else:
            print(((' ') * (i-half)) + (('*') * (n - i)  ))

rhombus(10)