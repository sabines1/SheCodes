import string as st, random as rd

def rand_str ():
   return(''.join(rd.choices(st.ascii_letters, k=rd.randint(5,5))))

print(rand_str())