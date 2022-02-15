"""https://open.kattis.com/problems/locustlocus"""


def get_lcm(x, y):
    greater = x if x > y else y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm


n = input("")
n = int(n)
ans = 999999999999999999999999999

for i in range(0, n):
    year, x, y = input("").split()

    year = int(year)
    x = int(x)
    y = int(y)

    lcm = get_lcm(x, y)
    placeholder_ans = year + lcm

    if placeholder_ans < ans:
        ans = placeholder_ans

print(ans)
