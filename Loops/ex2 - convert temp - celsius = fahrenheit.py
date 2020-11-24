# Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

def convert_to_cel(far):
    cel = (far-32)*5/9
    return cel

far = 140
print(convert_to_cel(far))

def convert_to_far(cel):
    far = (9*cel+160)/5
    return far

cel = 60
print(convert_to_far(cel))