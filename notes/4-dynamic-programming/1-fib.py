"""https://www.youtube.com/watch?v=oBt53YbR9Kk&t=2341s"""

import functools


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


"""
This function is bad because it takes 2**n time complexity to solve. 
In order to reduce the time complexity, we should implement memoization

Memoization stores the answers to duplicate sub-problems
"""

TYPICAL_MEMO = {
    "the key is the arguments to a function": "the value is the return value for that function"
}


@functools.cache
def fib(n):
    """
    There is a library that caches the result for you. But I will implement the caching manually
    for learning purposes
    """
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

##########################################################


def fib(n, memo={}):
    """
    There is a library that caches the result for you. But I will implement the caching manually
    for learning purposes
    """
    if n in memo:  # before any computation, check if I have cached data in the memo object
        return memo.get(n)

    if n <= 2:
        return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    # save the computed result in the memo
    # Note that memo object is passed into the recursive calls so that all recursive calls have access to the same memo object

    return memo[n]


print(fib(50))
