# Define a global empty dictionary. Iterate from 1 till 10 and fill the dictionary with the key as the number and value as the square of that number.

dict1 = {}

for x in range(1, 11):
    dict1[x] = x * x

print(dict1)
