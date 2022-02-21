"""https://www.hackerrank.com/challenges/bfsshortreach/problem?isFullScreen=true"""


def create_node(node, adj_list):
    adj_list[node] = []
    return adj_list


def create_bidirectional_edge(first_node, second_node, adj_list):
    adj_list[first_node].append(second_node)
    adj_list[second_node].append(first_node)
    return adj_list


n = 4  # nodes
m = 2  # edges
edges = [[1, 2], [1, 3]]
s = 1  # start

adj_list = {}

for i in range(1, n+1):
    adj_list = create_node(i, adj_list)

for edge in edges:
    adj_list = create_bidirectional_edge(edge[0], edge[1], adj_list)


def get_bfs_count(adj_list, start, end):
    visited = set()
    queue = [start]
    count = 0

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node == end:
            return count

        visited.add(current_node)
        children = adj_list.get(current_node)
        for child in children:
            if child not in visited:
                queue.append(child)
        count += 1

    return 0


print(get_bfs_count(adj_list, 1, 3))
