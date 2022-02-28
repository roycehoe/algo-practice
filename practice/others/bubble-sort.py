"""https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python"""
"""https://www.geeksforgeeks.org/bubble-sort/"""

array = [1, 5, 7, 34, 3, 7, 8, 1, 99]


array_length = len(array)
start_index = 0
is_no_swap_made = False

for element in array:
    if is_no_swap_made:
        break

    for array_index in range(0, array_length):
        if array_index + 1 < array_length:
            first, second = array[array_index], array[array_index+1]
            if first > second:
                array[array_index], array[array_index+1] = second, first
            else:
                is_no_swap_made = True


print(array)
