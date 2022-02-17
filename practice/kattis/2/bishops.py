"""https://open.kattis.com/problems/bishops"""

from sys import stdin

for n in stdin:
    n = int(n)

    if n == 0:
        ans = 0
    if n == 1:
        ans = 1
    else:
        ans = n + (n-2)

    print(ans)


# n = input('')
# n = int(n)

# if n == 0:
#     ans = 0
# if n == 1:
#     ans = 1
# else:
#     ans = n + (n-2)


# print(ans)
