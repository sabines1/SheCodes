count_even = 0
count_odd = 0
for num in range (1, 10):
    if num%2 == 0:
        count_even = count_even +1
    else:
        count_odd = count_odd + 1
print("The quantity of even numbers is : ", count_even)
print("The quantity of odd numbers is : ", count_odd)
