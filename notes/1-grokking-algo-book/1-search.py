"""
Big O = how fast an algo is, judged by the number of operations; used for worst case scenario
Runtime = O(n) where n=operations

simple search = O(n)
binary search = O(log n)

types of Big O runtimes:
 - log time = log n [eg. Binary search]
 - linear time = n [eg. Simple search]
 - n * log n [eg. fast sort algo, quicksort]
 - n**2 [eg. slow sort algo, selection sort]
 - n! [eg. traveling salesman]

Traveling salesman
 - A salesman must travel to 5 cities, but wants to minimize the distance traveled
 - 5 cities means that there are 5! permutations of travel
 - As cities increase, n factorial increases


"""


import math


def simple_search(number_list, number_to_find):
    """
    worst case scenario: 100 iterations
    linear time, which means that max guesses == size of list
    do not use, especially if list is large. but easy to write
    """
    iterations = 0
    for i in number_list:
        if number_to_find == i:
            print("found it!")
            break
        iterations += 1
        print(iterations)


def binary_search(list, item):
    """
    log time, which means that max guesses == log(size of list)
    Use when list is large. complicated to write
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = math.floor((low + high)/2)
        guess = list[mid]
        print(guess)

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None
