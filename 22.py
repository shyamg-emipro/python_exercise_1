# Create a function which takes a value. Define a global dictionary. The function should be able to display a statement whether the passed value is in the dictionary or not.
dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}


def findvalue(value):
    return True if value in dict1.values() else False


print(findvalue(8))
