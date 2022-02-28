"""https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python"""

array = [8, 2, 6, 4, 5]


def quicksort(array):
    if len(array) <= 1:
        return array

    mid_index = len(array)//2
    mid_element = array[mid_index]
    low, same, high = [], [], []

    for i in array:
        if i > mid_element:
            high.append(i)
        elif i < mid_element:
            low.append(i)
        else:
            same.append(i)

    ans = quicksort(low) + same + quicksort(high)
    return ans


print(quicksort(array))
