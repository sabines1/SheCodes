#Write a Python program that accepts a word from the user and reverse it

word = input("Please enter a word : ")
word = list(word)

word = word[::-1]
word = ''.join(word)
print(word)



# rev = []
# for i in range (len(word),0, -1):
#     rev.append(word[i])
# print(rev)