"""
https://leetcode.com/problems/subarray-sum-equals-k/
"""

n = [1, 2, 3, 4]
k = 3


def get_subarray_count(num_arr, goal):
    arr_length = len(num_arr)
    hash = {}
    ans = 0
    sum_tracker = 0

    for arr_index in range(arr_length):
        sum_tracker += num_arr[arr_index]

        if sum_tracker == goal:
            ans += 1
        if (sum_tracker - goal) in hash:
            ans += hash[sum_tracker - goal]

        if sum_tracker not in hash:
            hash[sum_tracker] = 0

        hash[sum_tracker] += 1

    return ans


print(get_subarray_count(n, k))
