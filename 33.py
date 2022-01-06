# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

for x in range(len(dict2)):
    for y in range(len(dict1)):
        if list(dict1.items())[y] == list(dict2.items())[x]:
            print(list(dict1.items())[y], " is present in both dict1 and dict2")
