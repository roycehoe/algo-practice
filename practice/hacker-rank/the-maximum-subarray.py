import itertools


arr = [-1, 2, 3, -4, 5, 10]
arr = [2, -1, 2, 3,  4, -5]
arr = [-2, -3, -1, -4, -6]
arr = [2, -1, 2, 3, 4, -5]
arr = [0, 0, 0, 1, -1]
arr = [1, -1, -1, -1, -1, 5]
arr = [-2387513869853631, 349878693257425, -23434261, -1253623436, 3451, 5]

ans_list = []
arr_count = len(arr)

for i in range(0, arr_count+1):
    for j in range(0, arr_count+1):
        if arr[i:j] != []:
            ans_list.append(arr[i:j])


first_ans = -10e9
ans = ()
second_ans = 0


for i in ans_list:
    first_ans = max(first_ans, sum(i))
    if first_ans == sum(i):
        ans = i


def is_all_negative(arr):
    for i in arr:
        if i >= 1:
            return False

    return True


if is_all_negative(arr):
    second_ans = min(ans)
else:
    for i in arr:
        if i >= 0:
            second_ans += i

print(ans)
print(first_ans, second_ans)
