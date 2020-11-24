
s1="abcde"
s2="edcba"   #s2="eeddc"

char_dic={}  # {a:1,b:1,c:1,d:1}
if len(s1)!=len(s2):
    print("not same")
else:
    for char in s1:
        print("test")
        if char in char_dic:
            char_dic[char]=char_dic[char]+1
        else:
            char_dic[char]=1

    # here we have: {a:1,b:1,c:1,d:1}
    for char in s2:
        if char not in char_dic:
            print("not same")
            break
        else:
            # in case in char dic
            char_dic[char]=char_dic[char]-1
            # here we have 2 cases:
              # 1: {a: 0, b: 0, c: 0, d: 0} < =  s1="abcde"  s2="edcab"
              # 2: {a: -1, b: 0, c: 0, d: 1}  < =  s1="abcde"  s2="abcea"
    is_same=True
    for val in char_dic.values():
        if val!=0:
            is_same=False
            print("not same")
            break
    if is_same:
     print("same")
print(char_dic)