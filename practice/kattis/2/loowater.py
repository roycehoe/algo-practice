"""https://open.kattis.com/problems/loowater"""

n, m = input("").split()
n = int(n)
m = int(m)

dragon_d = []
knight_h = []
pay = 0
output = []

for i in range(0, n):
    dragon_d.append(int(input("")))

for i in range(0, m):
    knight_h.append(int(input("")))

dragon_d.sort()
knight_h.sort()
