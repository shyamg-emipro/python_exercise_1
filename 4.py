# Write a Python program to get the volume of a sphere with radius 15.
#   Formula - 4/3 πr3

import math

vol = lambda radius: 4 / 3 * math.pi * radius * radius * radius
print("Volume of the sphere which has the radius of 15 is\n", vol(15))
