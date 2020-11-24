# לפניך רשימה של ערכי אנרגיה בג'אול
# joules = [5000, 8000,10000,6000, 12000]
# ניתן להמיר ג'אול לקילו-קלוריות ע"י חילוק ב-4184
# כתבי שורת קוד אחת המייצרת רשימה של tuples שהערך הראשון בכל tuple
# זה האנרגייה בג'אול
# והערך השני זה האנרגייה בקילו-קלוריות, כך :
# Out : [(5000, 1.195), (8000, 1.91), (10000, 2.39), (6000, 1.43), (12000, 2.86)]

joules = [5000, 8000,10000,6000, 12000]
# kilo = []
#
# def convert(x):
#     for i in x:
#         i = i/4184
#         kilo.append(i)
#     return(kilo)
#
# kilo = (convert(joules))
#
# print(list(zip(joules, kilo)))

#---------------------------------------
#The suggested solution :
#print([(j, cal) for (j, cal) in zip(joules,(map(lambda j: j/4184 ,joules )))])

#Other suggested solution :
print([(j,cal) for (j,cal) in zip (joules, (j/4184 for j in joules))])
















