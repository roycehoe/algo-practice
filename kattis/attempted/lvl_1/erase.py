"""https://open.kattis.com/problems/erase"""

n = input("")
n = int(n)
bd = input("")
ad = input("")


if n % 2:
    bd = ''.join('1' if x == '0' else '0' for x in bd)

if bd == ad:
    print("Deletion succeeded")
else:
    print("Deletion failed")
