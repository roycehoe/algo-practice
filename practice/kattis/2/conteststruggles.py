"""https://open.kattis.com/problems/conteststruggles"""

n, k = input("").split()
d, s = input("").split()

n = int(n)
k = int(k)
d = int(d)
s = int(s)

if d == 0:
    print(0)
else:
    dif_sum = n * d
    solved_sum = s * k
    remaining_qns = n - k

    ans = (dif_sum - solved_sum)/remaining_qns

    print(ans if ans <= 100 or ans >= 0 else "impossible")
