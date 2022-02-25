"""
write a function that takes in 2 arguments: An array of numbers, and a target

The function should return an array containing the shortest combination of numbers that add up exactly to the target sum
If there is a tie for the shortest combination, you may return any one of the shortest
"""


def best_sum(target, nums):
    if target == 0:
        return []
    if target <= 0:
        return None

    shortest_combination = None

    for num in nums:
        remainder = target - num
        remainder_combination = best_sum(remainder, nums)
        #for recursive functions, shortest combination is returned
        #and assigned as remainder_combination

        #for top level,
        if remainder_combination is not None:
            combination = [*remainder_combination, num]

            if shortest_combination is None:
                shortest_combination = combination

            if len(combination) < len(shortest_combination):
                shortest_combination = combination

    return shortest_combination


def best_sum(target, nums, memo={}):
    if target in memo:
        return memo.get(target)
    if target == 0:
        return []
    if target <= 0:
        return None

    shortest_combination = None

    for num in nums:
        remainder = target - num
        remainder_combination = best_sum(remainder, nums, memo)
        if remainder_combination is not None:
            combination = [*remainder_combination, num]

            if shortest_combination is None:
                shortest_combination = combination

            if len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target] = shortest_combination
    return shortest_combination


print(best_sum(7, [1, 2, 3, 6, 7]))
