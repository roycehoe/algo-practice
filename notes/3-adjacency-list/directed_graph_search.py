adj_list = {0: [1, 2, 3, 4], 1: [], 2: [6], 3: [], 4: [5], 5: [], 6: []}


def has_path(source, destination, adj_list):
    connecting_nodes = adj_list.get(source)
    return destination in connecting_nodes


def bfs(adj_list, source_node):
    stack = [source_node]

    while len(stack) > 0:
        current_node = stack.pop(0)
        print(current_node)
        connecting_nodes = adj_list.get(current_node)
        for connecting_node in connecting_nodes:
            stack.append(connecting_node)


def dfs(adj_list, source_node):
    queue = [source_node]
    while len(queue) > 0:
        current_node = queue.pop()
        print(current_node)
        connecting_nodes = adj_list[current_node]
        for connecting_node in connecting_nodes:
            queue.append(connecting_node)


def dfs_recursive(adj_list, source_node):
    print(source_node)
    for connecting_node in adj_list[source_node]:
        dfs_recursive(adj_list, connecting_node)
