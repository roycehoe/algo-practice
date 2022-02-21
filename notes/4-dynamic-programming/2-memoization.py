"""
https://youtu.be/oBt53YbR9Kk?t=2158

Memoization reduces the time complexity of the function from O(2**n) to O(2n), which is O(n)
"""


"""
PROBLEM:
You are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel
to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m*n?
"""

"""
APPROACH:

What happens if {m} and {n} is 1?
It would take 1 way to travel from start to end. You just do nothing.

What happens if {m} is 0?
There is no way to travel to the end if m is zero.

What happens if {n} is 0?
There is no way to travel to the end if n is zero.

Draw a tree
"""




import functools
@functools.cache
def get_grid_travel_ways(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return get_grid_travel_ways(m-1, n) + get_grid_travel_ways(m, n-1)
    # m-1 reflects the scenario where I move right
    # n-1 reflects the scenario where I move down


def get_grid_travel_ways(m, n, memo={}):
    if (m, n) in memo:
        return memo.get((m, n))

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[(m, n)] = get_grid_travel_ways(m-1, n, memo) + \
        get_grid_travel_ways(m, n-1, memo)

    return memo.get((m, n))
    # m-1 reflects the scenario where I move right
    # n-1 reflects the scenario where I move down


"""
TAKEAWAYS:
 - Visualize the problem as a tree
 - Implement the tree using recursion
 - Test your code to make sure the brute force solution works

 - Implement a memo object
 - Add base case to return memo values
 - Store returned values in memo
"""
