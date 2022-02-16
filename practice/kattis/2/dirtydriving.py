"""https://open.kattis.com/problems/dirtydriving"""

SAFETY_DISTANCE = 1

n, p = input("").split()
n = int(n)
p = int(p)

d = input("").split()
d = [int(i) for i in d]
d.sort()

ans = -10e9

for i in range(0, len(d)):
    current_d = d[i]
    car_n = i
    d_to_keep = p * (car_n + 1)
    net_d = d_to_keep - current_d + SAFETY_DISTANCE
    if net_d > ans:
        ans = net_d

print(ans)
