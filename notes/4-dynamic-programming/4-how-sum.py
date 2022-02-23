"""
Create a function that takes in two arguments: an array of numbers,
and a target sum

It should return an array containing any combination of elements that
add up exactly to the target sum
Return None if no such combination exists

https://www.youtube.com/watch?v=oBt53YbR9Kk&t=2341s
"""


def how_sum(target, nums):
    if target == 0:
        return []
    if target < 0:
        return None

    for num in nums:
        remainder = target - num
        remainer_result = how_sum(remainder, nums)
        if remainer_result is not None:
            return [*remainer_result, num]

    return None


def how_sum(target, nums, memo={}):
    if target in memo:
        return memo.get(target)

    if target == 0:
        return []
    if target < 0:
        return None

    for num in nums:
        remainder = target - num
        remainer_result = how_sum(remainder, nums, memo)
        if remainer_result is not None:
            memo[target] = [*remainer_result, num]
            return [*remainer_result, num]

    memo[target] = None
    return None


print(how_sum(300, [7, 14]))
