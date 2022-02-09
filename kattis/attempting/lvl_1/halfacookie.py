"""
https://open.kattis.com/problems/halfacookie
"""

from math import pi, sqrt

r, x, y = input("").split()
r, x, y = float(r), float(x), float(y)
print(r, x, y)


def is_miss(r, x, y):
    return sqrt(x**2 + y**2) < r


area = pi * r**2

"""
Possible solution:
 - Draw line from center to intersect x,y. Call this line 1.
 - Draw line perpendicular to the line mentioned above. Call this line 2.
 - The area carved out by line 2 is the smaller of the circle
"""
