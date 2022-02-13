adj_list = {0: [1, 2, 3, 4], 1: [0], 2: [6], 3: [], 4: [5], 5: [], 6: []}


def bfs(adj_list, source_node):
    traveled = set()
    stack = [source_node]

    while len(stack) > 0:
        current_node = stack.pop(0)
        traveled.add(current_node)
        print(current_node)
        connecting_nodes = adj_list.get(current_node)
        for connecting_node in connecting_nodes:
            if connecting_node not in traveled:
                stack.append(connecting_node)


def dfs(adj_list, source_node):
    traveled = set()
    queue = [source_node]

    while len(queue) > 0:
        current_node = queue.pop()
        traveled.add(current_node)
        print(current_node)
        connecting_nodes = adj_list.get(current_node)
        for connecting_node in connecting_nodes:
            if connecting_node not in traveled:
                queue.append(connecting_node)


traveled = set()


def dfs_recursive(adj_list, source_node, traveled):
    print(source_node)
    traveled.add(source_node)
    for connecting_node in adj_list.get(source_node):
        if connecting_node not in traveled:
            dfs_recursive(adj_list, connecting_node, traveled)
