# Define a dictionary, which is having keys as subject name such as maths, sci etc. and marks as values. Sum all the marks. and print the total.
dict1 = {
    "maths": 70,
    "science": 80,
    "social science": 70,
    "English": 90,
    "Gujarat": 90,
    "Computer": 90
}
sum1 = 0
for x in dict1.values():
    sum1 = sum1 + x
print("Sum of all subject marks is ", sum1)
