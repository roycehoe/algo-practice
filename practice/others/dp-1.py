"""
How many paths from (n,m) to (0,0)
"""


def get_ways(n, m):
    if n == 0 or m == 0:
        return 0
    if n == 1:
        return 1
    if m == 1:
        return 1

    return get_ways(n, m-1) + get_ways(n-1, m)


num_list = [1, 2, 3, 9, 5]


def get_ways(num_list):
    if len(num_list) == 0:
        return 0
    if len(num_list) == 1:
        return num_list[0]

    if get_ways(num_list[1::]) > get_ways(num_list[:-1:]):
        return sum(num_list[1::])
    return sum(num_list[:-1:])


print(get_ways(num_list))
