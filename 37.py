# Write a Python program to check if all values are the same in a dictionary.
# Original Dictionary:{'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
# Check all are 23 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
# Check if any one value in the dictionary is 25
# False

dict1 = {'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}


def check_for_similarity(di1):
    for x in di1:
        if di1['Cierra Vega'] != di1[x]:
            return False
    else:
        return True


if check_for_similarity(dict1):
    print("All values are same in dictionary!")
else:
    print("All values are NOT same in dictionary!")