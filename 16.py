# Write a Python program to display your details like name, age, address in three different lines.
# Expected Output
# Name : Joseph Moscot
# Age : 39
# Address : Bohemian Street, Lane 3, Grex County

details = {
    "Name": "Joseph Moscot",
    "Age": 39,
    "Address": "Bohemian Street, Lane 3, Grex County"
}
for key, value in details.items():
    print(key, " : ", value)