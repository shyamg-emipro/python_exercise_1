# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Also find which values are common in both the lists.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list1 = ["White", "Black", "Red"]
color_list2 = ["Red", "Green"]

print("Common Colors in both lists : ", set(color_list1).intersection(set(color_list2)))
print("color_list1 - color_list2 : ", set(color_list1).difference(set(color_list2)))