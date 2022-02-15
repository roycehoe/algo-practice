"""
https://open.kattis.com/problems/expectedearnings
"""

n, k, p = input("").split()
n = int(n)
k = int(k)
p = float(p)


def is_negative_e(n, k, p):
    win = n - k
    lose = k
    e = (win * p) - (lose * (1-p))
    if e < 0:
        return True
    return False


if is_negative_e(n, k, p):
    print("spela")
else:
    print("spela inte!")
