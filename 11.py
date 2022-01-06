# Take 3 global dictionaries as follows. Define a function, which takes those 3 dictionaries and concatenate them.
#
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Output should be - {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


def concatdict(dict1, dict2, dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1


print(concatdict(dic1, dic2, dic3))
