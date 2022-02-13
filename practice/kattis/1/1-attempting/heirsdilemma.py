"""https://open.kattis.com/problems/heirsdilemma"""

"""
combination is non-zero
all digits are different
combination divisible by each individual digit

"""


no_zero_l = []

li = [i for i in range(123456, 987654+1)]
for i in li:
    for j in str(i):
        if int(j)
