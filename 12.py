# Define a global dictionary with key & values. Iterate through it and print the key and value of it separately in the following format.
#   WritKey is <key> and Value is <value>

dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("WritKey is ", end=" ")
li = list(dic1.keys())

for i in range(len(li)):
    print(li[i], end=" ")


print("Values is ", end=" ")
li = list(dic1.values())

for i in range(len(li)):
    print(li[i], end=" ")
