# d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0} Sort this dictionary ascending and descending.
from operator import itemgetter

d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0}
li1 = list(d.keys())

li1.sort()
dict1 = {x: d[x] for x in li1}
print(dict1)

li1.sort(reverse=True)
dict1 = {x: d[x] for x in li1}
print(dict1)
number = { 'one' : 1 , 'two' : 2 , 'three' : 3 , 'four' : 4 , 'five' : 5 , 'six' : 6 , 'seven' : 7}

