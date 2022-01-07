# Write a Python program to filter the height and width of students, which are stored in a dictionary. Height >= 6ft and Weight>= 70kg:
# Original Dictionary: {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Output : {'Cierra Vega': (6.2, 70)}

dict2 = {'Cierra Vega': (6.2, 70),
         'Alden Cantrell': (5.9, 65),
         'Kierra Gentry': (6.0, 68),
         'Pierre Cox': (5.8, 66)
         }

# def myfilter(dict1):
#     for x in dict1.values():
#         if dict1[x][0] >= 6.0 and dict1[x][1] >= 70:
#             return True
#     else:
#         return False
#
#
# print(list(filter(myfilter, dict2)))

for key, value in dict2.items():
    if value[0] >= 6.0 and value[1] >= 70:
        print(key, ":", value)
