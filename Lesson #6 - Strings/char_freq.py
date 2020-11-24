# פונקצייה שמקבלת מחרוזת
# מייצרת מילון המקשר בין האות למספר המופעים שלה במחרוזת
# char_freq("abzz")
# נקבלת את המילון :
# freq = { 'a': 1, 'b': 1, 'z': 2}

##################################################################################################
#
# word = input("Enter a word: ")
# word = word.lower()
# list1 = list(word)
# list1 = sorted(list1)
# print(list1)
#
#
# # This function returns a list that contains only numbers : how many times a letter appears in a string
# def char_freq(word):
#     #word = input("Enter a word: ")
#     Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     list2 = []
#
#     for i in range(0,26):
#         if word.count(Alphabet[i]) > 0 :
#             list2.append(word.count(Alphabet[i]))
#     return list2
# char_freq(word)
#
#
# new_list = dict(zip(list1, list2))
# print(new_list)
#########################################################################################################
# from collections import Counter
# word = input("Enter a word: ")
# counts=Counter(word) # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
# print (counts)

# from collections import Counter
# print(Counter('cats on wheels'))
##########################################################################################################

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))


