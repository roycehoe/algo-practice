"""
1. Write a Python program to calculate the sum of a list of numbers
"""

data = [1, 2, 3, 4, 5]


def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1::])


"""
Write a Python program to get the sum of a non-negative integer
"""


def sum_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_digits(num // 10)


"""
7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
"""


def sum_series(num):
    if num <= 0:
        return 0
    return num + sum_series(num - 2)


"""
10. Write a Python program to calculate the value of 'a' to the power 'b'.
"""


def power(a, b):
    if b <= 0:
        return 1
    return a * power(a, b-1)


"""
11. Write a Python program to find  the greatest common divisor (gcd) of two integers
"""


def gcd(larger, smaller):
    if larger % smaller == 1:
        return 1
    temp = larger % smaller
    return temp * gcd(larger/temp, smaller/temp)


print(gcd(24, 18))
