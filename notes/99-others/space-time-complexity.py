"""
Quick revision

O(n) represents the complexity of a function.
Note that {n} is the input
"""


"""
Space complexity
[https://en.wikipedia.org/wiki/Space_complexity]

The memory space required to solve an instance of the computational problem
"""


def space_complexity_one(x):
    """
    x could be a list of 1 character or 1,000,000. It does not matter. The worst case
    scenario is that it will take O(1) time for this function to run, irrespective of
    input size.
    """
    print(x)


def space_complexity_n(x):
    """
    The complexity of the function increases linearly and directly proportionately to the size
    of the input. If x is a list of 1 element, it would take the function O(1) time to run. IF x is a list of 
    1,000,000 elements, it would take the function O(1,000,000) time to run
    """
    for i in x:
        print(i)


def space_complexity_n_squared(x):
    """
    The complexity of this function increases expodentially.
    Let us take x to be 100 elements long.
    The first statement, {for i in x}, that would be 100 iterations.
    The second statement, {for j in x}, that would be 100 iterations for each iteration outlined
    in the first statement.
    Hence, the time complexity is O(n squared)
    """
    for i in x:
        for j in x:
            print(i + j)

###########################


def space_complexity_n(x):
    """
    Let us take x to be 5.
    5 -> 4 -> 3 -> 2 -> 1. 1 is returned.
    This means that this function is called 5 times.
    This function has O(n) complexity.
    """
    if x <= 1:
        return 1
    return space_complexity_n(x-1)


def space_complexity_n(x):
    """
    Let us take x to be 5.

    Same as before, this function has O(n/2) complexity.
    However, in calculating complexity, we omit any multiplicative constants. Since O(n/2) is also O(1/2 * n), we can remove 1/2.
    Hence, the time complexity is O(n)
    """
    if x <= 2:
        return 1
    return space_complexity_n(x-2)


def space_complexity_two_n_squared(x):
    """
    Let us take the previous examples and stack them together.

    If you were to draw a tree for this, you would notice that for each branch, the number of nodes double.
    Also, notice that the height of the tree is {n}
    That means the total number of nodes, which is the total number of function calls, is 2*2*2*2.... n times
    Hence, the time complexity is O(2**n)

    The space complexity is different. It is O(n). Because at any one time, only {n} number of elements are stored in memory.
    You can check it out by drawing a tree
    """
    if x <= 2:
        return 1
    return space_complexity_two_n_squared(x-1) + space_complexity_two_n_squared(x-2)
