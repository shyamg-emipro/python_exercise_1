# Write a Python program to drop empty(None) Items from a given Dictionary.
# Original Dictionary - {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
dict2 = {key: value for (key, value) in dict1.items() if value is not None}

print(dict2)
