"""
https://open.kattis.com/problems/hidingplaces

Take in coordinate -> output coordinate(s)
"""

"""
strategy

Create list of all positions
create dictionary of all positions that a position can move to
 - Knight can (-1, +2), (1-, -2), (+1, +2), (+1, -2)
And then somehow get the answer from there
"""


x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = ['1', '2', '3', '4', '5', '6', '7', '8']
# print([i+j for i in x for j in y])

POSITIONS = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7',
             'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

KNIGHT_MOVEMENTS = [(1, 2), (-1, 2), (1, -2), (-1, -2)]


# def get_c(position, x, y):
#     return (x.index(position[0]), y.index(position[1]))


# def move_c(c, m_c):
#     return ((c[0] + m_c[0]), (c[1] + m_c[1]))


# def is_valid_c(c):
#     x = c[0]
#     y = c[1]
#     return y > 0 and y < 8 and x > 0 and x < 8


# def get_p(c, x, y):
#     return x[(c[0])] + y[(c[1])]


# move_map = {}
# for i in POSITIONS:
#     c = get_c(i, x, y)
#     valid_moves = []
#     for j in KNIGHT_MOVEMENTS:
#         new_c = move_c(c, j)
#         print(new_c)
#         if is_valid_c(new_c):
#             valid_moves.append(get_p(new_c, x, y))
#         move_map[i] = valid_moves

# print(move_map)

MOVE_MAP = {'a1': ['b3'], 'a2': ['b4'], 'a3': ['b5'], 'a4': ['b6', 'b2'], 'a5': ['b7', 'b3'], 'a6': ['b8', 'b4'], 'a7': ['b5'], 'a8': ['b6'], 'b1': ['c3'], 'b2': ['c4'], 'b3': ['c5'], 'b4': ['c6', 'c2'], 'b5': ['c7', 'c3'], 'b6': ['c8', 'c4'], 'b7': ['c5'], 'b8': ['c6'], 'c1': ['d3', 'b3'], 'c2': ['d4', 'b4'], 'c3': ['d5', 'b5'], 'c4': ['d6', 'b6', 'd2', 'b2'], 'c5': ['d7', 'b7', 'd3', 'b3'], 'c6': ['d8', 'b8', 'd4', 'b4'], 'c7': ['d5', 'b5'], 'c8': ['d6', 'b6'], 'd1': ['e3', 'c3'], 'd2': ['e4', 'c4'], 'd3': ['e5', 'c5'], 'd4': ['e6', 'c6', 'e2', 'c2'], 'd5': ['e7', 'c7', 'e3', 'c3'], 'd6': ['e8', 'c8', 'e4', 'c4'], 'd7': ['e5', 'c5'], 'd8': ['e6', 'c6'], 'e1': ['f3', 'd3'], 'e2': [
    'f4', 'd4'], 'e3': ['f5', 'd5'], 'e4': ['f6', 'd6', 'f2', 'd2'], 'e5': ['f7', 'd7', 'f3', 'd3'], 'e6': ['f8', 'd8', 'f4', 'd4'], 'e7': ['f5', 'd5'], 'e8': ['f6', 'd6'], 'f1': ['g3', 'e3'], 'f2': ['g4', 'e4'], 'f3': ['g5', 'e5'], 'f4': ['g6', 'e6', 'g2', 'e2'], 'f5': ['g7', 'e7', 'g3', 'e3'], 'f6': ['g8', 'e8', 'g4', 'e4'], 'f7': ['g5', 'e5'], 'f8': ['g6', 'e6'], 'g1': ['h3', 'f3'], 'g2': ['h4', 'f4'], 'g3': ['h5', 'f5'], 'g4': ['h6', 'f6', 'h2', 'f2'], 'g5': ['h7', 'f7', 'h3', 'f3'], 'g6': ['h8', 'f8', 'h4', 'f4'], 'g7': ['h5', 'f5'], 'g8': ['h6', 'f6'], 'h1': ['g3'], 'h2': ['g4'], 'h3': ['g5'], 'h4': ['g6', 'g2'], 'h5': ['g7', 'g3'], 'h6': ['g8', 'g4'], 'h7': ['g5'], 'h8': ['g6']}


def depth_first_search_while(graph, root_node):
    stack = [root_node]
    while len(stack) > 0:
        current = stack.pop(0)
        print(current)
        for i in graph[current]:
            stack.append(i)


def depth_first_search_recursive(graph, root_node):
    # no base case since if graph[root_node] is empty, this does not run
    for i in graph[root_node]:
        depth_first_search_recursive(graph, i)


depth_first_search_while(MOVE_MAP, 'a1')

# def depth_first_search_while(graph, root_node):
#     queue = [root_node]
#     while len(stack) > 0:
#         current = stack.pop(0)
#         print(current)
#         for i in graph[current]:
#             stack.append(i)
