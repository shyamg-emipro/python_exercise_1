# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

li = [1, 5, 38, 3]

ipnumber = int(input("Enter a Number:  "))

if ipnumber in li:
    print(bool(1))
else:
    print(bool(0))
