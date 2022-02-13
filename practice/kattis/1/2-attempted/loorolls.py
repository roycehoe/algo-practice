"""
https://open.kattis.com/problems/loorolls
"""

"""
l = 31
n = 6

1: -5 from 2nd roll, always ends at 36cm, 36-31=5
2: -4 from 3rd roll, always ends at 35cm, 35-31=4
3: -1 from 4th roll, always ends at 32cm, 32-31=1
4: 1 is a factor of l. Need 4 rolls

"""


l, n = [int(i) for i in input("").split()]

count = 1
while l % n:
    count += 1
    n = n - (l % n)
print(count)
