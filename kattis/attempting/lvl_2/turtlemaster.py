"""
https://open.kattis.com/problems/turtlemaster
"""

"""
init game
run game
If fire, check if direction facing is ice castle. If ice castle, destroy, else error
If coordinates == cordinates of castle or OOB, error



"""


game = [["." for i in range(8)] for i in range(8)]

game = [input("") for i in range(8) for i in range(8)]


print(game)
