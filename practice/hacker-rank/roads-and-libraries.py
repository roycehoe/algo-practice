"""https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true"""

"""
minimum cost problem

Find out number of connected components
For each connected component, build 1 library
Build roads between all connected components
Ensure built roads do not create an infinite loop

Minimal spanning tree problem
 - Add node
 - Check if cycle is formed
 - If cycle formed, discard
 - Else, continue
 - Return when all nodes traversed

For each connected component:
 - Get cost of building roads + 1 library
 - Get cost of building library
 - Return minimum cost

Add all costs up for all components


"""

c_road = 2  # cost of building road
c_lib = 3  # cost of building library
cities = [[1, 2], [3, 1], [2, 3]]


def create_adj_list(cities):
    adj_list = {}
    for i in cities:
        adj_list[i[0]] = [i[1]]
    return adj_list


def get_min_span_tree(adj_list):
    pass


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
