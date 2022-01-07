# students = {'Aex':{'class':'V', 'roll_id':2}, 'Puja':{'class':'V',’roll_id':3}}
# Using the above dictionary, print the following output.
# Aex
# class : V
# roll_id : 2
# Puja
# class : V
# roll_id : 3

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

for name, details in students.items():
    print(name)
    for key, value in details.items():
        print(key, " : ", value)
