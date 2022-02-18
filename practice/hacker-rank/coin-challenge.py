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


def can_give_change(n, denomination):
    return False if n % denomination else True


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

n = 6
c = [1, 2]


def main(c, n):
    ans = 0

    for i in c:
        if can_give_change(n, i):
            ans += 1

    return ans


# print(main(c, n))

def factorial(n):
    if n <= 1:
        return 1
    return n + factorial(n-1)


print(factorial(5))
