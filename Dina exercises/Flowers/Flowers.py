# שלב 1
# יוצרים קובץ ראשי - נקרא לו MAIN - כל הקוד יתחיל משם
# כותבים קטע קוד שקורא נתונים מקובץ וממיר את זה ל-dictionary

#Command to install xlrd module :

pip install xlrd

# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("C:\Python - Dina projects")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(0, 0))