# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Also find which values are common in both the lists.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list1 = ["White", "Black", "Red"]
color_list2 = ["Red", "Green"]
li1 = []
li2 = []
for i in range(len(color_list1)):
    for j in range(len(color_list2)):
        if color_list1[i] == color_list2[j]:
            li1.append(color_list1[i])
            break
    else:
        li2.append(color_list1[i])
print("Common Colors in both lists : ", set(li1))
print("color_list1 - color_list2 : ", set(li2))