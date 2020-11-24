# כתבי פונקצייה שמקבלת מספר חיובי בצורת רשימה של ספרות בין 0 ל-9
# ומחזירה את ערך המספר גדול ב-1 ברשימה
# לדוגמא :
#digits =[5,1] return [5,2]
#digits = [9] return [1,0]
#digits = [9,9,9] return [1,0,0,0]


digits = [9,9,9]

def plus_one(digits):
    # convert list of int to list of chars
    s = [str(i) for i in digits]
    #print(s)
    # convert list of chars to string, convert string to int
    res = int(''.join(s))
    #print(res)
    # Adding one to the number
    res = res + 1
    #print(res)
    # Convert int to str
    res = str(res)
    #print(res)
    # Convert str to list of chars
    return([str(i) for i in res])

print(plus_one(digits))
