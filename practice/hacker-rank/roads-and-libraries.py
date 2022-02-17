"""https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true"""


def is_existing_node(dict, parent):
    return False if dict.get(parent) is None else True


def create_node(dict, parent, child):
    dict[parent] = [child]
    return dict


def extend_node(dict, parent, child):
    temp = dict.get(parent)
    temp.append(child)
    dict[parent] = temp
    return dict


def add_node(dict, parent, child):
    if is_existing_node(dict, parent):
        return extend_node(dict, parent, child)
    return create_node(dict, parent, child)


def get_connected_nodes(nodes, start):
    visited = set()

    stack = [start]

    while len(stack) > 0:
        parent = stack.pop()
        if parent not in visited:
            visited.add(parent)

            children = nodes.get(parent)
            for child in children:
                stack.append(child)

    return visited


def get_cheapest_option(path, c_road, c_lib):
    tc_road = ((len(path) - 1) * c_road) + c_lib
    tc_lib = len(path) * c_lib
    return tc_lib if tc_lib < tc_road else tc_road


#########


q = int(input())
for i in range(0, q):
    n, m, c_lib, c_road = map(int, input().split())

    ans = 0
    nodes = {}
    paths = []
    visited = set()

    for j in range(0, m):
        parent, child = input().split()
        parent = int(parent)
        child = int(child)
        nodes = add_node(nodes, parent, child)
        nodes = add_node(nodes, child, parent)

    for node in nodes:
        if node not in visited:
            connected_nodes = get_connected_nodes(nodes, node)
            for connected_node in connected_nodes:
                visited.add(connected_node)
            paths.append(connected_nodes)

    for path in paths:
        ans += get_cheapest_option(path, c_road, c_lib)

    print(ans)
