# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

li = [1, 5, 38, 3]

ipnumber = int(input("Enter a Number:  "))
print(True if ipnumber in li else False)
