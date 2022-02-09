"""https://open.kattis.com/problems/deathknight"""

n = input("")
n = int(n)
count = 0


for i in range(0, n):
    k = input("")
    if k.find("CD") == -1:
        count += 1

print(count)
