"""https://open.kattis.com/problems/dst"""


def is_roll_forward(fb):
    return fb == "F"


def roll_forward(d, h, m):
    minutes = (d + m) % 60
    hour = ((d + m) // 60) + h
    if hour >= 24:
        hour = hour - 24
    return (hour, minutes)


def roll_backward(d, h, m):
    minutes = abs((m-d) % 60)
    hour = ((m-d) // 60) + h
    if hour < 0:
        hour = hour + 24
    return (hour, minutes)


n = int(input())

for i in range(0, n):
    fb, d, h, m = input().split()
    d, h, m = int(d), int(h), int(m)

    if is_roll_forward(fb):
        ans = roll_forward(d, h, m)
        print(f"{ans[0]} {ans[1]}")
    else:
        ans = roll_backward(d, h, m)
        print(f"{ans[0]} {ans[1]}")
