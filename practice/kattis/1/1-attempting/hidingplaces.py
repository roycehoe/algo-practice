"""
https://open.kattis.com/problems/hidingplaces
"""

# x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# y = ['1', '2', '3', '4', '5', '6', '7', '8']

# POSITION_NAME = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7',
#                  'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

# KNIGHT_MOVEMENTS = [(1, 2), (-1, 2), (1, -2), (-1, -2),
#                     (2, 1), (-2, 1), (2, -1), (-2, -1)]


# def get_coordinates(position_name, x, y):
#     x_position = position_name[0]
#     y_position = position_name[1]

#     x_coordinate = int(x.index(x_position))
#     y_coordinate = int(y.index(y_position))
#     return (x_coordinate, y_coordinate)


# def get_position_name(coordinates, x, y):
#     x_coordinate = coordinates[0]
#     y_coordinate = coordinates[1]

#     x_name = x[x_coordinate]
#     y_name = y[y_coordinate]
#     return x_name+y_name


# def is_valid_coordinates(coordinates):
#     return coordinates[0] < 8 and coordinates[0] > 0 and coordinates[1] > 0 and coordinates[1] < 8


# def get_new_coordinates(coordinates, movement):
#     return tuple(sum(i) for i in zip(coordinates, movement))


# def get_knight_movements(start_position_name, knight_movements, x, y):
#     movement_list = []

#     old_coordinates = get_coordinates(start_position_name, x, y)
#     for knight_movement in knight_movements:
#         new_coordinates = get_new_coordinates(old_coordinates, knight_movement)
#         print(old_coordinates)
#         print(new_coordinates)
#         if is_valid_coordinates(new_coordinates):
#             new_position_name = get_position_name(new_coordinates, x, y)
#             movement_list.append(new_position_name)

#     return movement_list


# print(get_knight_movements('a1', KNIGHT_MOVEMENTS, x, y))

# adj_list = {}

# for position in POSITION_NAME:
#     adj_list[position] = get_knight_movements(position, KNIGHT_MOVEMENTS, x, y)

# print(adj_list)


adj_list = {'a1': ['b3', 'c2'], 'a2': ['b4', 'c3'], 'a3': ['b5', 'c4', 'c2'], 'a4': ['b6', 'b2', 'c5', 'c3'], 'a5': ['b7', 'b3', 'c6', 'c4'], 'a6': ['b8', 'b4', 'c7', 'c5'], 'a7': ['b5', 'c8', 'c6'], 'a8': ['b6', 'c7'], 'b1': ['c3', 'd2'], 'b2': ['c4', 'd3'], 'b3': ['c5', 'd4', 'd2'], 'b4': ['c6', 'c2', 'd5', 'd3'], 'b5': ['c7', 'c3', 'd6', 'd4'], 'b6': ['c8', 'c4', 'd7', 'd5'], 'b7': ['c5', 'd8', 'd6'], 'b8': ['c6', 'd7'], 'c1': ['d3', 'b3', 'e2'], 'c2': ['d4', 'b4', 'e3'], 'c3': ['d5', 'b5', 'e4', 'e2'], 'c4': ['d6', 'b6', 'd2', 'b2', 'e5', 'e3'], 'c5': ['d7', 'b7', 'd3', 'b3', 'e6', 'e4'], 'c6': ['d8', 'b8', 'd4', 'b4', 'e7', 'e5'], 'c7': ['d5', 'b5', 'e8', 'e6'], 'c8': ['d6', 'b6', 'e7'], 'd1': ['e3', 'c3', 'f2', 'b2'], 'd2': ['e4', 'c4', 'f3', 'b3'], 'd3': ['e5', 'c5', 'f4', 'b4', 'f2', 'b2'], 'd4': ['e6', 'c6', 'e2', 'c2', 'f5', 'b5', 'f3', 'b3'], 'd5': ['e7', 'c7', 'e3', 'c3', 'f6', 'b6', 'f4', 'b4'], 'd6': ['e8', 'c8', 'e4', 'c4', 'f7', 'b7', 'f5', 'b5'], 'd7': ['e5', 'c5', 'f8', 'b8', 'f6', 'b6'], 'd8': ['e6', 'c6', 'f7', 'b7'], 'e1': ['f3', 'd3', 'g2', 'c2'], 'e2': ['f4', 'd4', 'g3', 'c3'], 'e3': ['f5', 'd5', 'g4', 'c4', 'g2', 'c2'], 'e4': ['f6', 'd6', 'f2', 'd2', 'g5', 'c5', 'g3', 'c3'], 'e5': ['f7', 'd7', 'f3', 'd3', 'g6', 'c6', 'g4', 'c4'], 'e6': ['f8', 'd8', 'f4', 'd4', 'g7', 'c7', 'g5', 'c5'], 'e7': ['f5', 'd5', 'g8', 'c8', 'g6', 'c6'], 'e8': ['f6', 'd6', 'g7', 'c7'], 'f1': ['g3', 'e3', 'h2', 'd2'], 'f2': ['g4', 'e4', 'h3', 'd3'], 'f3': ['g5', 'e5', 'h4', 'd4', 'h2', 'd2'], 'f4': ['g6', 'e6', 'g2', 'e2', 'h5', 'd5', 'h3', 'd3'], 'f5': ['g7', 'e7', 'g3', 'e3', 'h6', 'd6', 'h4', 'd4'], 'f6': ['g8', 'e8', 'g4', 'e4', 'h7', 'd7', 'h5', 'd5'], 'f7': ['g5', 'e5', 'h8', 'd8', 'h6', 'd6'], 'f8': ['g6', 'e6', 'h7', 'd7'], 'g1': ['h3', 'f3', 'e2'], 'g2': ['h4', 'f4', 'e3'], 'g3': ['h5', 'f5', 'e4', 'e2'], 'g4': ['h6', 'f6', 'h2', 'f2', 'e5', 'e3'], 'g5': ['h7', 'f7', 'h3', 'f3', 'e6', 'e4'], 'g6': ['h8', 'f8', 'h4', 'f4', 'e7', 'e5'], 'g7': ['h5', 'f5', 'e8', 'e6'], 'g8': ['h6', 'f6', 'e7'], 'h1': ['g3', 'f2'], 'h2': ['g4', 'f3'], 'h3': ['g5', 'f4', 'f2'], 'h4': ['g6', 'g2', 'f5', 'f3'], 'h5': ['g7', 'g3', 'f6', 'f4'], 'h6': ['g8', 'g4', 'f7', 'f5'], 'h7': ['g5', 'f8', 'f6'], 'h8': ['g6', 'f7']}