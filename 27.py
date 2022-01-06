# Define a global dictionary. Define a function which takes 2 values 1st as key and 2nd as value. The function should add those key values to the global dictionary.

dict1 = {}


def add_to_dictionary(key, value):
    dict1[key] = value


add_to_dictionary('Name', 'Emipro')
add_to_dictionary('year', 2011)

print(dict1)
