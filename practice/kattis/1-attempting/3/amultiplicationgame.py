"""
https://open.kattis.com/problems/amultiplicationgame
"""

"""
Let n = 100
Let p = multiplied int
Let Stan,Ollie = A,B
Let winner = A

Perfect play if:
    B: p = p ^ ?. Forced winning move.
    A: p = p ^ 9. Winning move. p > n. Initial p must be {n/9 rounded up} < p < {n-1}
    A: wins
"""

"""
n = 1000

Winner: 112-999
Loser: 56-111
Winner: 7-55
Loser: 4-6
Winner: 1-3
Create situation where, no matter what loser does, loser will put winner in winning situation

formula:

winner: x, y
loser range: (x/2) rounded up, x-1

loser: x, y
winner range: (x/9) rounded up, x-1
"""




from math import ceil
def winning_range(n):
    ceiling = n - 1
    floor = ceil(n/9)
    print(f'ceiling{ceiling}, floor{floor}')


winning_range(1000)


def losing_range(winning_range_floor):
    losing_range_ceiling = winning_range_floor - 1
    losing_range_floor = ceil(winning_range_floor/9)
    print(f'ceiling{losing_range_ceiling}, floor{losing_range_floor}')


"""
n = 1000

wr: 999-112
lr: 

"""


def get_winner(num):
    round = 1
    p = 1
    winner = ""

    if round % 2:  # odd round
        winner = "stan"
    else:
        winner = "ollie"

    # something here
    print(f'{winner} wins.')
