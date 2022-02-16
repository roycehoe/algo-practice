"""https://open.kattis.com/problems/beehives"""

from math import sqrt


d, n = input('').split()
d = float(d)
n = int(n)

data = []

for i in range(0, n):
    x, y = input('').split()
    x = float(x)
    y = float(y)
    data.append((x, y))


def get_d(first_t, second_t):
    a = first_t[0] - second_t[0]
    b = first_t[1] - second_t[1]
    return sqrt(a ** 2 + b ** 2)


def is_sour(first_n, second_n, d):
    return True if get_d(first_n, second_n) < d else False


sour = set()

for i in data:
    for j in data:
        if i != j:
            if is_sour(i, j, d):
                sour.add(i)
                sour.add(j)

sour_count = (len(sour))
sweet_count = (len(data) - len(sour))

print(f'{sour_count} sour, {sweet_count} sweet')
