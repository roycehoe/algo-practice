from sqlite3 import connect


MOVE_MAP = {'a1': ['b3'], 'a2': ['b4'], 'a3': ['b5'], 'a4': ['b6', 'b2'], 'a5': ['b7', 'b3'], 'a6': ['b8', 'b4'], 'a7': ['b5'], 'a8': ['b6'], 'b1': ['c3'], 'b2': ['c4'], 'b3': ['c5'], 'b4': ['c6', 'c2'], 'b5': ['c7', 'c3'], 'b6': ['c8', 'c4'], 'b7': ['c5'], 'b8': ['c6'], 'c1': ['d3', 'b3'], 'c2': ['d4', 'b4'], 'c3': ['d5', 'b5'], 'c4': ['d6', 'b6', 'd2', 'b2'], 'c5': ['d7', 'b7', 'd3', 'b3'], 'c6': ['d8', 'b8', 'd4', 'b4'], 'c7': ['d5', 'b5'], 'c8': ['d6', 'b6'], 'd1': ['e3', 'c3'], 'd2': ['e4', 'c4'], 'd3': ['e5', 'c5'], 'd4': ['e6', 'c6', 'e2', 'c2'], 'd5': ['e7', 'c7', 'e3', 'c3'], 'd6': ['e8', 'c8', 'e4', 'c4'], 'd7': ['e5', 'c5'], 'd8': ['e6', 'c6'], 'e1': ['f3', 'd3'], 'e2': [
    'f4', 'd4'], 'e3': ['f5', 'd5'], 'e4': ['f6', 'd6', 'f2', 'd2'], 'e5': ['f7', 'd7', 'f3', 'd3'], 'e6': ['f8', 'd8', 'f4', 'd4'], 'e7': ['f5', 'd5'], 'e8': ['f6', 'd6'], 'f1': ['g3', 'e3'], 'f2': ['g4', 'e4'], 'f3': ['g5', 'e5'], 'f4': ['g6', 'e6', 'g2', 'e2'], 'f5': ['g7', 'e7', 'g3', 'e3'], 'f6': ['g8', 'e8', 'g4', 'e4'], 'f7': ['g5', 'e5'], 'f8': ['g6', 'e6'], 'g1': ['h3', 'f3'], 'g2': ['h4', 'f4'], 'g3': ['h5', 'f5'], 'g4': ['h6', 'f6', 'h2', 'f2'], 'g5': ['h7', 'f7', 'h3', 'f3'], 'g6': ['h8', 'f8', 'h4', 'f4'], 'g7': ['h5', 'f5'], 'g8': ['h6', 'f6'], 'h1': ['g3'], 'h2': ['g4'], 'h3': ['g5'], 'h4': ['g6', 'g2'], 'h5': ['g7', 'g3'], 'h6': ['g8', 'g4'], 'h7': ['g5'], 'h8': ['g6']}

"""
Write a function that takes in:
 - n = number of moves
 - start = start position
 - map = adjacency list

Which outputs a list of positions that can be moved to
"""


def bfs(adj_list, source_node):
    traveled = set()
    queue = [source_node]

    while len(queue) > 0:
        current_node = queue.pop(0)
        traveled.add(current_node)
        print(queue)
        connecting_nodes = adj_list.get(current_node)

        for connecting_node in connecting_nodes:
            if connecting_node not in traveled:
                queue.append(connecting_node)


print(bfs(MOVE_MAP, 'a1'))
