"""https://open.kattis.com/problems/owlandfox"""


t = input("")
t = int(t)

for i in range(0, t):
    place = 0
    n = input("")
    n = int(n)
    while True:
        if n // 10**place % 10:
            print(n - 10**place)
            break
        place += 1

"""
Do something like
Look at ones place. If zero, move to next place. Else, minus one and print result
Look at tens place. If zero, move to next place. Else, minus ten and print result
Need tracker for place
"""
