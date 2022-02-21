"""
https://youtu.be/oBt53YbR9Kk?t=4205

Write a function that takes in a target sum, and an array of
numbers as arguments

Return a boolean indicating whether it is possible to generate the target sum using numbers from the array

You can use as many numbers in the array as you like
"""


import functools


def can_sum(target, num_array):
    if target == 0:
        return True
    if target < 0:
        return False

    for num in num_array:
        remainder = target - num
        if can_sum(remainder, num_array) is True:
            return True

    return False


@functools.cache
def can_sum(target, num_array):
    if target == 0:
        return True
    if target < 0:
        return False

    for num in num_array:
        remainder = target - num
        if can_sum(remainder, num_array) == True:
            return True

    return False


def can_sum(target, num_array, memo={}):
    if target in memo:
        return memo.get(target)

    if target == 0:
        return True
    if target < 0:
        return False

    for num in num_array:
        remainder = target - num
        if can_sum(remainder, num_array) == True:
            memo[target] = True
            return True

    memo[target] = False
    return False


print(can_sum(100, (1, 3, 8, 12, 2)))
