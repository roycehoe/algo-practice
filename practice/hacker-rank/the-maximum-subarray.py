import itertools
from re import A


arr = [-1, 2, 3, -4, 5, 10]
arr = [1, 2, 3, 4]
arr = [-2, -3, -1, -4, -6]
arr = [-5, 1, -1, -1, -1, -1, 5, -2, 100, 54, -9]


def remove_left_negative_numbers(arr):
    for i in range(len(arr)-1):
        if arr[i] >= 0:
            return arr[i:]


def remove_right_negative_numbers(arr):
    for i in range(len(arr)-1, 0, -1):
        if arr[i] >= 0:
            return arr[:i+1]


def remove_left_positive_numbers(arr):
    for i in range(len(arr)-1):
        if arr[i] <= 0:
            return arr[i:]


def remove_right_positive_numbers(arr):
    for i in range(len(arr)-1, 0, -1):
        if arr[i] <= 0:
            return arr[:i+1]


def get_base_arr(arr):
    if arr == []:
        return []
    arr = remove_left_negative_numbers(arr)
    arr = remove_right_negative_numbers(arr)
    return arr


def get_right_arr(arr):
    if arr == []:
        return []
    arr = remove_left_positive_numbers(arr)
    arr = get_base_arr(arr)
    return arr


def get_left_arr(arr):
    if arr == []:
        return []
    arr = remove_right_positive_numbers(arr)
    arr = get_base_arr(arr)
    return arr


base_arr = get_base_arr(arr)
right_arr = get_right_arr(base_arr)
left_arr = get_left_arr(base_arr)


def get_largest_arr(base_arr, right_arr, left_arr):
    base_sum, right_sum, left_sum = sum(
        base_arr), sum(right_arr), sum(left_arr)
    max_sum = max(base_sum, right_sum, left_sum)

    if max_sum == base_sum:
        return base_arr
    elif max_sum == right_sum:
        return right_arr
    else:
        return left_arr


def get_largest_subarr(arr):
    base_arr = get_base_arr(arr)
    right_arr = get_right_arr(base_arr)
    left_arr = get_left_arr(base_arr)

    return get_largest_arr(base_arr, get_largest_subarr(right_arr), get_largest_subarr(left_arr))


print(get_largest_subarr(arr))
