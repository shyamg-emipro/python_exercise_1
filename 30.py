# Define a global dictionary. Iterate through it and print the key and value of it separately in the following format.
# Key is <key> and Value is <value>.
# The loop statement should be enough to extract key and value, so don't use the "get" method or [] to extract the value from the dictionary.

dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

print("Key is ", [n for n in dict1.keys()], " and Value is ", [n for n in dict1.values()])
