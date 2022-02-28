"""https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python"""

"""
https://www.youtube.com/watch?v=cVZMah9kEjI
"""


def merge(left, right):
    result = []
    result_length = len(left) + len(right)
    index_left = 0
    index_right = 0

    while len(result) < result_length:
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
        if index_left == len(left):
            result += right[index_right:]

    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2

    left = merge_sort(array[:midpoint])
    right = merge_sort(array[midpoint:])

    return merge(left, right)


test = [1, 5, 87, 4, 5, 8, 4, 3, 6, 734, 2457, 457, 34568, 43, 7, 1]
test = merge_sort(test)
print(test)
