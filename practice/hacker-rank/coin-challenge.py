"""https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=true"""

"""
n - amount to make change for
c - available coin denominations

Tips:
 - Store previously computed solutions

n = 5
c = [a,b,c,d,e]

find a combination that using just [a], I can get 5
find a combination that using [a,b], I can get 5
find a combination that using [a,b, c], I can get 5
find a combination that using [a,b, c, d], I can get 5
find a combination that using [a,b, c, d, e], I can get 5

show all combinations. That is my answer
"""


# n = 5
# c = [1, 2, 3, 4, 5]

# ans = 0
# for i in c:
#     if can_give_change(n, i):
#         ans += 1


"""
Base case done. Now I need to somehow create a list of 2 numbers, and then see if I can create n with them
"""


"""
I think I have the solution. Lets say:
n = 6
c = [1,2,3]

get case for [1]
get case for [2]
get case for [3]

for [1,2]:
    If 1 appears 1 time, can I get n? ie. If n = 5
    If 1 appears 2 times, can I get n? ie. if n = 4
    If 1 appears 3 times, can I get n? ie. if n = 3
    If 1 appears 4 times, can I get n? ie. if n = 2

I NEED A RECURSIVE FUNCTION. Function might change (n)
"""


def can_give_change(n, denomination):
    return False if n % denomination else True


n = 10
c = [1, 2, 3, 5, 10]


def get_change(n, c):
    if len(c) <= 1:
        if can_give_change(n, c[0]):
            return 1
        return 0

    if can_give_change(n, c[0]):
        return 1 + get_change(n, c[1::])
    return get_change(n, c[1::])


n = 10
c = [1, 2]


def test(n, c):
    print(n)
    if n == 0:
        return 0
    return test(n-1, c)


print(test(n, c))
