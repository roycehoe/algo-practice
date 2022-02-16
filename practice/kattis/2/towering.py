"""https://open.kattis.com/problems/towering"""

temp = input("").split()
temp = [int(i) for i in temp]
b, x, y = temp[:6], temp[6], temp[7]

largest_h = max(b)
b.remove(largest_h)


def is_tower(x, y, height):
    return height == x or y == height


for i in range(0, len(b)):
    for j in range(0, len(b)):
        if i != j:
            first_box = b[i]
            second_box = b[j]
            height = largest_h + first_box + second_box
            if is_tower(x, y, height):
                ans = [largest_h, first_box, second_box]

b.remove(ans[1])
b.remove(ans[2])
ans.sort(reverse=True)
b.sort(reverse=True)

ans = ans + b

print(" ".join(map(str, ans)))
