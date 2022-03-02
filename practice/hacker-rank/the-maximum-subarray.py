import itertools
from re import A


arr = [-1, 2, 3, -4, 5, 10]
arr = [1, 2, 3, 4]
arr = [-2, -3, -1, -4, -6]
arr = [1, -1, -1, -1, -1, 5, -2, 100, 54, -9]
# arr = [-10]
# arr = [1]


"""
Solution probably inefficient
New implementation.

Create arrays that are flanked by positive numbers
compare 3 arrays:
 - The current array
 - The array with the righthand side removed till the next positive number
 - The array with the lefthand side removed till the next positive number

If the largest array is the current array, return the current array
If the second or third array is the largest array, that is now the current array
"""


def get_largest_array(*arrs):
    max_arr = []
    arrs = list(arrs)

    for i in range(len(arrs)):
        current_max = sum(max_arr)
        possible_max = sum(arrs[i])
        if possible_max >= current_max:
            max_arr = arrs[i]

    return max_arr


def is_all_negative(arr):
    for i in arr:
        if i >= 1:
            return False

    return True


def get_next_positive_number_index(arr, reverse=False):
    if reverse:

        for i in range(len(arr)-1, 0, -1):
            if arr[i] >= 0:
                return i

    for i in range(len(arr)-1):
        if arr[i] >= 0:
            return i


right_index = get_next_positive_number_index(arr)
left_index = get_next_positive_number_index(arr, reverse=True)

right_array = arr[right_index:]
left_array = arr[:left_index]

print(right_array)
print(left_array)
