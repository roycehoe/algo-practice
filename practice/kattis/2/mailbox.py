"""https://open.kattis.com/problems/mailbox"""

from math import ceil

"""
Binary search tree

Ceiling
Floor
Guess
Number

If guess is too high, lower ceiling
If guess is too lower, raise floor
If guess is correct, break

"""


def guess_too_high(guess, number):
    return guess > number


def raise_floor(guess):
    return guess - 1


def lower_ceiling(guess):
    return guess + 1


def bin_search(floor, ceiling, x):
    count = 0
    guess = 10e9

    while guess != x:
        count += 1
        guess = (floor + ceiling) // 2
        if guess_too_high(guess, x):
            ceiling = lower_ceiling(guess)
        else:
            floor = raise_floor(guess)

    return count


def mailbox_search(floor, ceiling, x, mailbox):
    guess = 10e9
    fireworks = 0

    while guess != x:
        guess = (floor + ceiling) // 2
        fireworks += guess
        print({'guess': guess,
               'ceiling': ceiling,
               'floor': floor,
               'fireworks': fireworks,
               'mailbox': mailbox})

        if guess_too_high(guess, x):
            ceiling = lower_ceiling(guess)
            mailbox -= 1
        else:
            floor = raise_floor(guess)

        if mailbox <= 1:
            break


mailbox_search(1, 100, 73, 3)
