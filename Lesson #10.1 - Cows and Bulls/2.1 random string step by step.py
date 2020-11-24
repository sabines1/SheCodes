# קביעת אורך המחרוזת
import random as rd
length = rd.randint(5,5)
print(length)

# שליפת אותיות
import string as st
print(st.ascii_letters)

# מתוך רצף כלשהו, הפונקצייה choices, שולפת מספר רנדומלי של פריטים - הפלט רשימה
import string as st, random as rd
print(rd.choices(st.ascii_letters, k = 5))

# הפיכת הרשימה הנ"ל למחרוזת
print(''.join (rd.choices(st.ascii_letters, k = 5)))

# פונקצייה שמגרילה מחרוזת

import string as st, random as rd

def rand_str ():
   return(''.join(rd.choices(st.ascii_letters, k=rd.randint(5,5))))

print(rand_str())