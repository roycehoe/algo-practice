"""
Create a function that takes in two arguments: an array of numbers,
and a target sum

It should return an array containing any combination of elements that
add up exactly to the target sum
Return None if no such combination exists

https://www.youtube.com/watch?v=oBt53YbR9Kk&t=2341s
"""


import functools


def how_sum(target, num_array):
    if target == 0:
        return []
    if target < 0:
        return None

    for num in num_array:
        remainder = target - num
        remainder_result = how_sum(remainder, num_array)
        if remainder_result is not None:
            return [*remainder_result, num]
        # Unpack operator used above to unpack whatever elements are in
        # the remainder_result list

    return None


@functools.cache
def how_sum(target, num_array, memo={}):
    if target in memo:
        return memo.get(target)

    if target == 0:
        return []
    if target < 0:
        return None

    for num in num_array:
        remainder = target - num
        remainder_result = how_sum(remainder, num_array, memo={})
        if remainder_result is not None:
            memo[target] = [*remainder_result, num]
            return memo[target]

    memo[target] = None
    return None


print(how_sum(300, [7, 14]))
