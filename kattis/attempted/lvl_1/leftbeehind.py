"""https://open.kattis.com/problems/leftbeehind"""

print_l = []

while True:
    x, y = [int(i) for i in input("").split()]
    if x == 0 and y == 0:
        break
    if x + y == 13:
        print_l.append('Never speak again.')
    elif x == y:
        print_l.append('Undecided.')
    elif x < y:
        print_l.append('Left beehind.')
    else:
        print_l.append('To the convention.')


for i in print_l:
    print(i)
