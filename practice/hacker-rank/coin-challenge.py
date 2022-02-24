"""https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=true"""

"""https://www.ideserve.co.in/learn/coin-change-problem-number-of-ways-to-make-change"""

"""
n = 50
c = {1,5,10,20}

ans = 
get ways to make change of 50 using 0 coins of 20
+ get ways to make change of 50 using 1 coin of 20 with {1,5,10}
+ get ways to make change of 50 using 2 coins of 20 with {1,5,10}

ans = 
+ get ways to make change of 50 using 0 coins of 20 with {1,5,10}
+ get ways to make change of 30 using 0 coins of 20 with {1,5,10}
+ get ways to make change of 10 using 0 coins of 20 with {1,5,10}

"""


from re import L
n = 3
c = [8, 3, 1, 2]

n = 4
c = [1, 2, 3]

# n = 50
# c = [20, 10, 5, 1]


# first iteration


def get_change(n, c):
    first_num = c[0]
    remainder = n
    while remainder >= 0:
        print(remainder, "call recursive fn")
        remainder = remainder - first_num
        # do something with the remainder

# first iteration


print(get_change(n, c))
