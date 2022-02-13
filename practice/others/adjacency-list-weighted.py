adjacency_list = {}
nodes_list = []


def add_node(node, nodes_list):
    if node not in nodes_list:
        nodes_list.append(node)
    else:
        print(f'node {node} already exists')


def __nodes_exists(first_node, second_node, nodes_list):
    return first_node in nodes_list and second_node in nodes_list


def __create_edge(first_node, second_node, weight, adjacency_list):
    temp = []

    temp.append([second_node, weight])
    adjacency_list[first_node] = temp

    return adjacency_list


def __extend_edge(first_node, second_node, weight, adjacency_list):
    temp = []

    temp.extend(adjacency_list[first_node])
    temp.append([second_node, weight]))
    adjacency_list[first_node]=temp

    return adjacency_list


def add_edge(first_node, second_node, weight, nodes_list, adjacency_list):

    if __nodes_exists(first_node, second_node, nodes_list):
        if first_node not in adjacency_list:
            adjacency_list=__create_edge(
                first_node, second_node, weight, adjacency_list)

        elif first_node in adjacency_list:
            adjacency_list=__extend_edge(
                first_node, second_node, weight, adjacency_list)

    else:
        print("Nodes do not exist")
