"""https://open.kattis.com/problems/bishops"""

n = input('')
n = int(n)

if n == 1:
    ans = 1
else:
    ans = n + (n-2)

print(ans)
