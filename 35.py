# Write a Python program to drop empty(None) Items from a given Dictionary.
# Original Dictionary - {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}

for x in dict1:
    if dict1[x] == None:
        del dict1[x]
        break

print(dict1)
