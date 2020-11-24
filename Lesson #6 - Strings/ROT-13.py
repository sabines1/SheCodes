# import codecs
#
# print(codecs.encode("hello", "rot-13")) # -> uryyb

#############################################

def rot13_encode(message):
    Rot13=''
    alphabit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in message:
        if i in alphabit:
            Rot13 += alphabit[alphabit.index(i) + 13]
        else:
            Rot13 += i
    return Rot13

print (rot13_encode('sabine'))

############################################

def rot13_decode(message ):
    Rot13=''
    alphabit = 'nopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
    for i in message:
        if i in alphabit:
            Rot13 += alphabit[alphabit.index(i) + 13]
        else:
            Rot13 += i
    return Rot13

print(rot13_decode('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'))