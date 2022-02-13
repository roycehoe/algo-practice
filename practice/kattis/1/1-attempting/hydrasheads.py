"""https://open.kattis.com/problems/hydrasheads"""

"""
Move/Results:
-1h = +1h. Ignore this. Does nothing. [M1]
-1t = +2t [M2]
-2h = nothing [M3]
-2t = +1h [M4]

Dead when:
0h,0t, 4th is last move
2h,0t must be the second last result. Goal.


Strategy:
Think of this as a 2d graph
(3,3), how to move to (0,0) where (h,t)

Options

(0,1) [M2]
(-2,0) [M3]
(1,-2) [M4]

(3,3), move to (0,0)

M4 (4,1)
M3 (2,1)
M3 (0,1)
M2 (0,2)
M2 (0,3)
M2 (0,4)
M4 (1,2)
M4 (2,0)
M3 (0,0)

(1,1) to (0,0)

"""


h, t = [int(i) for i in input("").split()]
