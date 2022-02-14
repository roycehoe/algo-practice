"""https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true"""

"""
Steps
 - Create adj list
 - Get all connected components
 - For each connected component:
  - Get cost of building 1 library + minimum spanning treee
  - Get cost of building library in all cities
  - Return the minimum for this
  - Sum up minimum for all connected components
"""


c_road = 2  # cost of building road
c_lib = 3  # cost of building library
cities = [[1, 2], [3, 1], [2, 3]]


def get_build_library_cost(adj_list, c_lib):
    nodes = len(adj_list)
    MST_paths = nodes - 1
    return c_lib * MST_paths


def get_build_roads_cost(adj_list, c_road, c_lib):
    nodes = len(adj_list)
    MST_paths = nodes - 1
    return (c_lib + c_road * MST_paths)


def get_cheapest_build(adj_list, c_road, c_lib):
    build_roads_cost = get_build_roads_cost(adj_list, c_road, c_lib)
    build_library_cost = get_build_library_cost(adj_list, c_lib)
    return build_roads_cost if build_roads_cost < build_library_cost else build_library_cost


def create_adj_list(cities):
    adj_list = {}
    for i in cities:
        adj_list[i[0]] = [i[1]]
    return adj_list


test = create_adj_list(cities)
print(test)


def main(number_of_cities, c_lib, c_road, city_array):
    pass


"""

n, m, c_lib, c_road = input("").split()
n = int(n)
m = int(m)
c_lib = int(c_lib)
c_road = int(c_road)
cities = []

for i in range(0, n):
    first_node, second_node = input("").split()
    first_node = int(first_node)
    second_node = int(second_node)
    cities.append([first_node, second_node])

print(cities)

"""
