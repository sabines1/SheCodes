
s = 'anagram'
t = 'nagaram'

# s = 'rat'
# t = 'car'

# s="5b*d!"
# t="*!d5b"

def comp_len(a,b):
    if len(a)==len(b):
        return (True)
    else:
        print("LEN not identical, not anagrams")

if comp_len(s,t) == True:
    s = sorted(s)
    t = sorted(t)
    new_list = (list(zip(s,t)))
    for i in range(len(new_list)):
        if new_list[i][0] != new_list[i][1]:
            print('The 2 strings are NOT anagrams')
            break
    else:
        print ('ANAGRAM !')

