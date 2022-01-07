# Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

data = input("Enter comma separated numbers:  ")  # Input from user
list1 = [int(x) for x in data.split(",")]  # split data and convert to list and change list items from str to int using list comprehension
tuple1 = tuple(list1)
print("List:  ", list1)
print("Tuple: ", tuple1)
