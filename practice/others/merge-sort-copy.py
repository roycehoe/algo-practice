test = [1, 5, 87, 4, 5, 8, 4, 3, 6, 734, 2457, 457, 34568, 43, 7, 1]


def merge(left, right):
    merged_list = []
    merged_list_target_length = len(left) + len(right)
    left_index = 0
    right_index = 0
    merged_index = 0

    while merged_list_target_length != len(merged_list):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

        if left_index >= len(left):
            merged_list += right[right_index:]
        elif right_index >= len(right):
            merged_list += left[left_index:]

    return merged_list


def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array)//2
    left = merge_sort(array[:midpoint])
    right = merge_sort(array[midpoint:])

    return merge(left, right)
