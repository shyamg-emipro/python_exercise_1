# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

a = int(input("Enter no a"))
b = int(input("Enter no b"))
c = int(input("Enter no c"))
print(3 * (a + b + c) if a == b == c else (a+b+c))
if a == b == c:
    print(3 * (a + b + c))
else:
    print(a + b + c)
