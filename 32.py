# students = {'Aex':{'class':'V', 'roll_id':2}, 'Puja':{'class':'V',’roll_id':3}}
# Using the above dictionary, print the following output.
# Aex
# class : V
# roll_id : 2
# Puja
# class : V
# roll_id : 3

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

for x in students:
    print(x)
    for y in students[x]:
        print(y, " : ", students[x][y])
